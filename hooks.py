"""
MkDocs hooks for post-build processing.
- WebP image conversion and HTML reference updates
- External link marking and label paragraph styling
- Markdown image-to-figure conversion
- TelemFFB settings-table generation from the vendored defaults.xml
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image


# ---------------------------------------------------------------------------
# TelemFFB settings tables
#
# Category pages in docs/telemffb/ can place markers of the form
#     <!-- telemffb-settings parentgroup=aerodynamics -->
#     <!-- telemffb-settings parentgroup=aerodynamics grouping=Vibration -->
# which are expanded at build time into tables generated from the vendored
# copy of TelemFFB's defaults.xml (data/telemffb-defaults.xml). Update that
# file from the TelemFFB repo when a release changes settings — the tables
# follow automatically.
# ---------------------------------------------------------------------------

TELEMFFB_DEFAULTS_XML = Path(__file__).parent / "data" / "telemffb-defaults.xml"
_SIMS = ("DCS", "IL2", "IL2K", "BMS", "MSFS", "XPLANE")
_SIM_LABEL = {"XPLANE": "XP", "IL2K": "IL2 Korea"}
_DEVICES = ("joystick", "pedals", "collective", "trimwheel")
_SKIP_DATATYPES = {"group", "convert"}
# Settings that exist in defaults.xml but are not yet exposed to users.
_UNRELEASED_PREFIXES = ("ffb_api_",)

_telemffb_settings_cache = None


def _load_telemffb_settings():
    """Parse the vendored defaults.xml into deduplicated setting records."""
    global _telemffb_settings_cache
    if _telemffb_settings_cache is not None:
        return _telemffb_settings_cache

    tree = ET.parse(TELEMFFB_DEFAULTS_XML)
    # A collapsible group row inside a section (e.g. "Tap: Axis Corrections",
    # shown under Joystick Spring Mode) is not a setting, but its members
    # belong under whatever the group hangs off. Section groups such as
    # basic_group have no prereq of their own and are left alone.
    group_prereqs = {}
    for d in tree.getroot().iter("defaults"):
        if (d.findtext("datatype") or "").strip() == "group":
            gp = (d.findtext("prereq") or "").strip()
            if d.findtext("name") and gp:
                group_prereqs[d.findtext("name")] = gp

    def resolve_prereq(prereq):
        seen = set()
        while prereq.split(".")[0] in group_prereqs and prereq not in seen:
            seen.add(prereq)
            prereq = group_prereqs[prereq.split(".")[0]]
        return prereq

    settings = {}
    for d in tree.getroot().iter("defaults"):
        name = d.findtext("name")
        datatype = (d.findtext("datatype") or "").strip()
        displayname = (d.findtext("displayname") or "").strip()
        if not name or not displayname or datatype in _SKIP_DATATYPES:
            continue
        if name.startswith(_UNRELEASED_PREFIXES):
            continue
        try:
            order = float(d.findtext("order") or 0)
        except ValueError:
            order = 0.0
        sims = {s for s in _SIMS if d.findtext(s) == "true"}
        devices = {v for v in _DEVICES if d.findtext(v) == "true"}
        prereq_raw = resolve_prereq((d.findtext("prereq") or "").strip())
        rec = settings.get(name)
        if rec is None:
            settings[name] = {
                "name": name,
                "displayname": displayname,
                "info": (d.findtext("info") or "").strip(),
                "order": order,
                "prereq": prereq_raw.split(".")[0],
                # Value-scoped prereq tokens (e.g. spring_mode.FORCETRIM):
                # the modes of the parent selector this child appears under.
                "modes": tuple(prereq_raw.split(".")[1:]),
                "parentgroup": (d.findtext("parentgroup") or "").strip(),
                "grouping": (d.findtext("grouping") or "").strip(),
                "sims": sims,
                "devices": devices,
            }
        else:
            # Same setting declared per-sim: merge applicability, keep the
            # lowest-order entry's metadata.
            rec["sims"] |= sims
            rec["devices"] |= devices
            if order < rec["order"]:
                rec.update(order=order, displayname=displayname)
                if d.findtext("info"):
                    rec["info"] = d.findtext("info").strip()

    _telemffb_settings_cache = list(settings.values())
    return _telemffb_settings_cache


def _clean_info(info):
    """Normalize an info string for a table cell: strip HTML, one line."""
    text = re.sub(r"(?i)<br\s*/?>", " ", info)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("|", "\\|")
    return re.sub(r"\s+", " ", text).strip()


def _sims_label(sims):
    if set(_SIMS) <= sims:
        return "All"
    return ", ".join(_SIM_LABEL.get(s, s) for s in _SIMS if s in sims)


def _devices_label(devices):
    if {"joystick", "pedals", "collective"} <= devices:
        return "All"
    return ", ".join(v.capitalize() for v in _DEVICES if v in devices)


# Effects documented via <!-- telemffb-effect --> markers, for the coverage
# check in on_post_build.
_telemffb_documented_effects = set()


def _strip_tags(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


def _sim_badges(sims):
    return " ".join(
        f'<span class="sim-badge sim-{s.lower()}">{_SIM_LABEL.get(s, s)}</span>'
        for s in _SIMS if s in sims)


def _effect_block(name, part="both"):
    """Render the badge line and/or sub-setting table for one effect."""
    settings_by_name = {s["name"]: s for s in _load_telemffb_settings()}
    root = settings_by_name.get(name)
    if root is None:
        return f"*(unknown setting {name!r})*"
    _telemffb_documented_effects.add(name)

    parts = []
    if part in ("badges", "both"):
        devices = _devices_label(root["devices"])
        devices = "All devices" if devices == "All" else devices
        parts.append(f'{_sim_badges(root["sims"])} · {devices}')

    if part in ("table", "both"):
        # Direct children grouped by the parent-selector mode(s) they appear
        # under (value-scoped prereqs like spring_mode.FORCETRIM). Ordinary
        # bool parents have a single unscoped group, which renders without a
        # group label.
        direct = sorted((s for s in settings_by_name.values()
                         if s["prereq"] == name), key=lambda s: s["order"])
        groups = []          # [(modes_tuple, [children...])]
        for child in direct:
            for modes, members in groups:
                if modes == child["modes"]:
                    members.append(child)
                    break
            else:
                groups.append((child["modes"], [child]))

        def rows_for(children):
            lines = ["| Sub-setting | Sims | What it does |", "|---|---|---|"]
            stack = [(c, 0) for c in reversed(children)]
            while stack:
                child, depth = stack.pop()
                label = _strip_tags(child["displayname"]).replace("|", "\\|")
                if depth:
                    label = "&nbsp;&nbsp;&nbsp;&nbsp;" * depth + "↳ " + label
                if child["sims"] == root["sims"] and child["devices"] == root["devices"]:
                    sims = "—"
                else:
                    sims = ", ".join(_SIM_LABEL.get(s, s) for s in _SIMS
                                     if s in child["sims"]) or "—"
                    if child["devices"] != root["devices"]:
                        sims += f' · {_devices_label(child["devices"])}'
                lines.append(f"| {label} | {sims} | {_clean_info(child['info'])} |")
                kids = sorted((s for s in settings_by_name.values()
                               if s["prereq"] == child["name"]),
                              key=lambda s: s["order"])
                stack.extend((k, depth + 1) for k in reversed(kids))
            return "\n".join(lines)

        for modes, members in groups:
            if modes:
                label = " / ".join(_mode_label(name, m) for m in modes)
                parts.append(f"**In mode: {label}**")
            parts.append(rows_for(members))

    return "\n\n".join(parts)


# Human labels for spring-mode / g-effect enum values used in value-scoped
# prereqs (matches the labels in TelemFFB's SettingsManager enum dicts).
# A token that means different things under different selectors is keyed
# by (selector, token) in _SELECTOR_MODE_LABELS, which is checked first.
_SELECTOR_MODE_LABELS = {
    ("gforce_effect_mode", "LEGACY"): "Exponential Curve",
    ("gforce_effect_mode", "NEW"): "Linear + Deflection Based",
    ("gforce_effect_mode", "ADVANCED"): "Custom Curve",
}
_MODE_LABELS = {
    "BASIC": "Basic Dynamic",
    "CENTER": "Basic Dynamic with Spring Centering",
    "CNTR_FT": "Spring Centering + Force Trim",
    "FBW": "FlyByWire (FBW)",
    "ADVANCED": "Advanced Dynamic",
    "FORCETRIM": "Force Trim",
    "STATIC": "Static Spring",
    "DYNAMIC": "Dynamic Spring",
    "NOSPRING": "No Spring",
    "NONE": "None (Game Managed)",
    "CUSTOM": "Custom",
    "DINPUT_TAP": "Game Managed (DirectInput Tap)",
}


def _mode_label(selector, token):
    return (_SELECTOR_MODE_LABELS.get((selector, token))
            or _MODE_LABELS.get(token, token.title()))


# Settings-tab sections in app order: (parentgroup, user-facing name).
_TELEMFFB_SECTIONS = [
    ("basic", "Basic Settings"),
    ("aerodynamics", "Aerodynamics"),
    ("inertial", "Inertial"),
    ("ground", "Ground"),
    ("mechanical", "Mechanical\\Airframe"),
    ("weapons", "Weapons"),
    ("ffb", "Basic FFB Effects"),
    ("system", "System"),
]

_effect_anchor_cache = None


def _toc_slug(heading):
    """Replicate python-markdown's toc slugify (separator '-')."""
    text = _strip_tags(heading)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text.strip())


def _heading_anchor(heading):
    """A heading's anchor: its explicit `{ #id }` when it has one, else the toc slug."""
    attrs = re.search(r"\{([^}]*)\}\s*$", heading)
    if attrs:
        explicit = re.search(r"#([\w-]+)", attrs.group(1))
        if explicit:
            return explicit.group(1)
        heading = heading[:attrs.start()]
    return _toc_slug(heading)


def _effect_anchor_map():
    """Scan the TelemFFB pages for effect markers: setting -> (page, anchor)."""
    global _effect_anchor_cache
    if _effect_anchor_cache is not None:
        return _effect_anchor_cache
    mapping = {}
    marker = re.compile(r"<!--\s*telemffb-effect\s+([^>]*?)\s*-->")
    for path in sorted((Path(__file__).parent / "docs" / "telemffb").glob("*.md")):
        heading = None
        for line in path.read_text(encoding="utf-8").splitlines():
            if re.match(r"^#{1,6}\s", line):
                heading = line.lstrip("#").strip()
                continue
            m = marker.search(line)
            if m and heading:
                am = re.search(r"name=(\S+)", m.group(1))
                if am and am.group(1) not in mapping:
                    mapping[am.group(1)] = (path.name, _heading_anchor(heading))
    _effect_anchor_cache = mapping
    return mapping


def _sim_index(sim):
    """Render the per-simulator settings directory."""
    if sim not in _SIMS:
        return f"*(unknown sim {sim!r})*"
    settings_by_name = {s["name"]: s for s in _load_telemffb_settings()}
    anchors = _effect_anchor_map()
    out = []
    for parentgroup, section in _TELEMFFB_SECTIONS:
        tops = sorted((s for s in settings_by_name.values()
                       if s["parentgroup"] == parentgroup
                       and s["prereq"] not in settings_by_name
                       and sim in s["sims"]),
                      key=lambda s: s["order"])
        if not tops:
            continue
        out.append(f"## {section}")
        for s in tops:
            label = _strip_tags(s["displayname"])
            devs = _devices_label(s["devices"])
            qualifier = "" if devs == "All" else f" *({devs})*"
            loc = anchors.get(s["name"])
            if loc:
                out.append(f"-   [{label}]({loc[0]}#{loc[1]}){qualifier}")
            else:
                print(f"[TelemFFB effects] sim index {sim}: no documented "
                      f"location for {s['name']}")
                out.append(f"-   {label}{qualifier}")
        out.append("")
    return "\n".join(out).rstrip()


def _expand_telemffb_settings(markdown):
    marker = re.compile(r"<!--\s*telemffb-(effect|sim-index)\s+([^>]*?)\s*-->")
    arg = re.compile(r'(\w+)=(?:"([^"]*)"|(\S+))')

    def replace(match):
        args = {m.group(1): m.group(2) if m.group(2) is not None else m.group(3)
                for m in arg.finditer(match.group(2))}
        if match.group(1) == "effect":
            return _effect_block(args.get("name", ""), args.get("part", "both"))
        if match.group(1) == "sim-index":
            return _sim_index(args.get("sim", ""))
        return _settings_table(args.get("parentgroup", ""), args.get("grouping"))

    return marker.sub(replace, markdown)


def _report_undocumented_effects():
    """Warn about top-level settings lacking a telemffb-effect entry.

    Only parentgroups that have at least one documented effect are checked, so
    pages still using the legacy grouping tables do not produce noise during
    the transition.
    """
    if not _telemffb_documented_effects:
        return
    settings_by_name = {s["name"]: s for s in _load_telemffb_settings()}
    active_groups = {settings_by_name[n]["parentgroup"]
                     for n in _telemffb_documented_effects if n in settings_by_name}
    missing = [
        s for s in settings_by_name.values()
        if s["parentgroup"] in active_groups
        and s["prereq"] not in settings_by_name        # top-level
        and s["name"] not in _telemffb_documented_effects
        and s["sims"]                                  # hidden legacy entries
    ]
    for s in sorted(missing, key=lambda s: (s["parentgroup"], s["order"])):
        print(f"[TelemFFB effects] UNDOCUMENTED: {s['parentgroup']}: "
              f"{_strip_tags(s['displayname'])} ({s['name']})")


def convert_images_to_webp(config):
    """
    Convert all PNG, JPG, and JPEG images to WebP format and update HTML references.
    Tracks conversion statistics and updates all HTML files with new WebP paths.
    """
    site_dir = Path(config['site_dir'])
    
    print("\n[WebP Conversion] Starting image conversion...")
    
    # Track conversion statistics
    stats = {
        'converted': 0,
        'skipped': 0,
        'failed': 0,
        'total_original_size': 0,
        'total_webp_size': 0
    }
    
    # Find all images to convert
    image_extensions = ('.png', '.jpg', '.jpeg')
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(site_dir.rglob(f'*{ext}'))
    
    # Also check for existing WebP files to track skipped conversions
    existing_webp = set()
    for webp_file in site_dir.rglob('*.webp'):
        existing_webp.add(webp_file.stem)
    
    print(f"[WebP Conversion] Found {len(image_files)} images to process, {len(existing_webp)} WebP files already exist")
    
    # Convert each image to WebP
    conversion_map = {}  # Maps old path to new WebP path
    
    for img_path in image_files:
        try:
            webp_path = img_path.with_suffix('.webp')
            
            # Skip if WebP already exists and is newer than source
            # This handles incremental builds
            if webp_path.exists():
                webp_mtime = webp_path.stat().st_mtime
                img_mtime = img_path.stat().st_mtime
                
                if webp_mtime >= img_mtime:
                    # WebP is up to date, skip conversion
                    stats['skipped'] += 1
                    webp_size = webp_path.stat().st_size
                    stats['total_webp_size'] += webp_size
                    
                    # Still add to conversion map for HTML updates
                    old_rel_path = img_path.relative_to(site_dir).as_posix()
                    new_rel_path = webp_path.relative_to(site_dir).as_posix()
                    conversion_map[old_rel_path] = new_rel_path
                    
                    # Remove original image
                    img_path.unlink()
                    continue
            
            # Get original file size
            original_size = img_path.stat().st_size
            stats['total_original_size'] += original_size
            
            # Convert to WebP
            with Image.open(img_path) as img:
                # Convert RGBA to RGB if necessary (for JPEG compatibility)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Create white background
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = background
                
                # Save as WebP with quality 85 (good balance between size and quality)
                img.save(webp_path, 'WEBP', quality=85, method=6)
            
            # Get WebP file size
            webp_size = webp_path.stat().st_size
            stats['total_webp_size'] += webp_size
            
            # Calculate savings
            savings_percent = ((original_size - webp_size) / original_size) * 100 if original_size > 0 else 0
            
            # Store mapping for HTML updates (relative to site_dir)
            old_rel_path = img_path.relative_to(site_dir).as_posix()
            new_rel_path = webp_path.relative_to(site_dir).as_posix()
            conversion_map[old_rel_path] = new_rel_path
            
            stats['converted'] += 1
            
            if stats['converted'] % 50 == 0:
                print(f"[WebP Conversion] Processed {stats['converted']}/{len(image_files)} images...")
            
            # Remove original image file
            img_path.unlink()
            
        except Exception as e:
            print(f"[WebP Conversion] Failed to convert {img_path}: {e}")
            stats['failed'] += 1
    
    # Update HTML files to reference WebP images
    if conversion_map:
        print(f"[WebP Conversion] Updating HTML references...")
        html_files = list(site_dir.rglob('*.html'))
        updated_files = 0
        total_replacements = 0
        
        for html_path in html_files:
            try:
                content = html_path.read_text(encoding='utf-8')
                original_content = content
                file_updated = False
                
                # Update image references - replace file extensions directly
                for old_path, new_path in conversion_map.items():
                    # Extract just the filename for simpler matching
                    old_filename = Path(old_path).name
                    new_filename = Path(new_path).name
                    
                    # Replace in src attributes
                    if old_filename in content:
                        new_content = content.replace(f'src="{old_path}"', f'src="{new_path}"')
                        
                        # Also handle relative paths - just replace the filename
                        new_content = new_content.replace(old_filename, new_filename)
                        
                        if new_content != content:
                            replacements = content.count(old_filename)
                            total_replacements += replacements
                            content = new_content
                            file_updated = True
                
                # Write back if changed
                if file_updated and content != original_content:
                    html_path.write_text(content, encoding='utf-8')
                    updated_files += 1
                    
            except Exception as e:
                print(f"[WebP Conversion] Failed to update {html_path}: {e}")
        
        print(f"[WebP Conversion] Updated {updated_files} HTML files ({total_replacements} image references)")
    
    # Print summary statistics
    print(f"\n[WebP Conversion] Summary:")
    print(f"  - Images converted: {stats['converted']}")
    print(f"  - Images skipped (already converted): {stats['skipped']}")
    print(f"  - Conversion failures: {stats['failed']}")
    
    if stats['total_original_size'] > 0 or stats['total_webp_size'] > 0:
        original_mb = stats['total_original_size'] / (1024 * 1024)
        webp_mb = stats['total_webp_size'] / (1024 * 1024)
        savings_mb = original_mb - webp_mb
        savings_percent = (savings_mb / original_mb) * 100
        
        print(f"  - Original size: {original_mb:.2f} MB")
        print(f"  - WebP size: {webp_mb:.2f} MB")
        print(f"  - Space saved: {savings_mb:.2f} MB ({savings_percent:.1f}%)")
    
    print("[WebP Conversion] Complete!\n")


def on_post_build(config):
    """
    Hook called after the build completes.
    - Reports TelemFFB settings missing an effects-reference entry
    - Copies .htaccess to site output (MkDocs ignores dotfiles)
    - Converts images to WebP format (skipped in serve mode)
    """
    import sys
    import os
    import shutil

    _report_undocumented_effects()

    # Copy .htaccess if present (MkDocs skips dotfiles)
    docs_dir = Path(config['docs_dir'])
    site_dir = Path(config['site_dir'])
    htaccess_src = docs_dir / '.htaccess'
    htaccess_dst = site_dir / '.htaccess'
    if htaccess_src.is_file():
        # Avoid SameFileError when docs_dir/site_dir paths resolve to the same file.
        same_file = False
        try:
            same_file = htaccess_dst.exists() and htaccess_src.samefile(htaccess_dst)
        except FileNotFoundError:
            same_file = False

        if not same_file:
            shutil.copy2(str(htaccess_src), str(htaccess_dst))

    # Skip WebP conversion in serve/livereload mode for performance
    if 'serve' in sys.argv or os.environ.get('MKDOCS_SKIP_WEBP'):
        print("[WebP Conversion] Skipping conversion in livereload mode (use 'mkdocs build' for WebP conversion)")
        return
    
    convert_images_to_webp(config)


def on_page_content(html, page, config, files):
    """
    Process HTML content:
    - Mark external links with class/target attributes
    - Mark label-style paragraphs (first node is <strong>) with a CSS class
    """
    from bs4 import BeautifulSoup, Tag

    # Configuration (matching plugin settings from mkdocs.yml)
    class_name = 'external'
    target = '_blank'
    rel = []  # Can be set to ['noopener', 'noreferrer'] if needed
    additional_protocols = ['https:']
    default_protocols = ['http://', 'https://', 'ftp://', 'mailto:', 'tel:', 'www']
    all_protocols = default_protocols + additional_protocols

    soup = BeautifulSoup(html, 'html.parser')

    # External links
    for a_tag in soup.find_all('a', href=True):
        # Skip header anchor links
        if 'headerlink' in a_tag.get('class', []):
            continue

        href = a_tag['href']
        if any(href.startswith(protocol) for protocol in all_protocols):
            # Add external class
            if class_name and class_name not in a_tag.get('class', []):
                classes = a_tag.get('class', [])
                if not isinstance(classes, list):
                    classes = []
                a_tag['class'] = classes + [class_name]

            # Set target attribute
            if target:
                a_tag["target"] = target

            # Set rel attribute if configured
            if rel:
                a_tag["rel"] = rel

    # Label paragraphs: first child node (including text) is <strong>
    for p_tag in soup.find_all('p'):
        if p_tag.contents and isinstance(p_tag.contents[0], Tag) and p_tag.contents[0].name == 'strong':
            classes = p_tag.get('class', [])
            if not isinstance(classes, list):
                classes = []
            p_tag['class'] = classes + ['label-paragraph']

    return str(soup)


PLACEHOLDER_IMAGE = '/images/placeholder.svg'


def _img2fig_build_figure(caption, image_link, attr_list, is_index=False):
    """
    Build an HTML <figure> element from parsed image components.
    Prepends '../' to relative image paths for non-index pages (which are
    served from a subdirectory like page-name/index.html).
    Index pages are served directly from their directory, so no prefix is needed.
    """
    # Skip absolute or protocol-relative URLs (https://, http://, //, data:)
    if not re.match(r'^(?:https?://|//|data:)', image_link):
        if not is_index:
            image_link = ('..' / Path(image_link)).as_posix()
    if attr_list:
        attr_list = attr_list.replace('{', '').replace('}', '')
    else:
        attr_list = ''
    return (
        r'<figure class="figure-image">'
        rf'  <img src="{image_link}" alt="{caption}" {attr_list}>'
        rf'  <figcaption>{caption}</figcaption>'
        r'</figure>'
    )


def on_page_markdown(markdown, page, config, files):
    """
    Convert Markdown image syntax to <figure> elements with captions.
    Replaces the img2figv2 plugin (vendored inline to avoid external dependency).
    Missing images are replaced with a placeholder and a warning is printed.
    Linked images [![alt](img)](url) produce a <figure> with <a><img></a> inside.
    """
    if '<!-- telemffb-' in markdown:
        markdown = _expand_telemffb_settings(markdown)

    docs_dir = Path(config['docs_dir'])
    page_dir = (docs_dir / page.file.src_path).parent
    is_index = page.file.src_path.endswith('index.md')

    def _resolve_image(image_link):
        """Check image exists, return resolved link (or placeholder)."""
        if not re.match(r'^(?:https?://|//|data:)', image_link):
            clean_link = image_link.split('?')[0].split('#')[0]
            image_path = (page_dir / clean_link).resolve()
            if not image_path.is_file():
                print(f"[Placeholder] Missing image: {image_link} (in {page.file.src_path})")
                return PLACEHOLDER_IMAGE
        return image_link

    def _adjust_path(image_link):
        """Prepend ../ for non-index pages with relative paths."""
        if not re.match(r'^(?:https?://|//|data:)', image_link):
            if not is_index:
                image_link = ('..' / Path(image_link)).as_posix()
        return image_link

    def _convert_linked_image(match):
        """Handle [![alt](img)](url) — produce <figure> with clickable image."""
        caption = match.group(1)
        image_link = _resolve_image(match.group(2))
        image_link = _adjust_path(image_link)
        href = match.group(3)
        return (
            f'<figure class="figure-image">'
            f'  <a href="{href}"><img src="{image_link}" alt="{caption}"></a>'
            f'  <figcaption>{caption}</figcaption>'
            f'</figure>'
        )

    def _convert_image(match):
        """Handle ![alt](img) — produce <figure> with caption."""
        caption, image_link, attr_list = match.groups()
        image_link = _resolve_image(image_link)
        return _img2fig_build_figure(caption, image_link, attr_list, is_index)

    # First pass: convert linked images [![alt](img)](url)
    linked_pattern = re.compile(
        r'\[!\[(.*?)\]\((.*?)\)\]\((.*?)\)', flags=re.IGNORECASE
    )
    markdown = re.sub(linked_pattern, _convert_linked_image, markdown)

    # Second pass: convert standalone images ![alt](img)
    standalone_pattern = re.compile(
        r'!\[(.*?)\]\((.*?)\)(\{[^\}]*\})?', flags=re.IGNORECASE
    )
    markdown = re.sub(standalone_pattern, _convert_image, markdown)

    return markdown



