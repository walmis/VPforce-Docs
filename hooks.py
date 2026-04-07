"""
MkDocs hooks for post-build processing.
- WebP image conversion and HTML reference updates
- External link marking and label paragraph styling
- Markdown image-to-figure conversion
"""

import re
from pathlib import Path
from PIL import Image


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
    - Copies .htaccess to site output (MkDocs ignores dotfiles)
    - Converts images to WebP format (skipped in serve mode)
    """
    import sys
    import os
    import shutil

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



