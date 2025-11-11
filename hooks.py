"""
MkDocs hooks for post-build image optimization.
Converts PNG, JPG, and JPEG images to WebP format and updates HTML references.
"""

import os
import re
import shutil
from pathlib import Path
from PIL import Image


def on_pre_build(config):
    """Hook called before the build starts."""
    pass


def on_post_build(config):
    """
    Hook called after the build completes.
    Converts all PNG, JPG, and JPEG images to WebP format and updates HTML references.
    Only runs in full build mode, skips during livereload/serve for performance.
    """
    import sys
    import os
    
    # Skip conversion in serve/livereload mode for performance
    # Check if we're running mkdocs serve or if MKDOCS_SKIP_WEBP env var is set
    if 'serve' in sys.argv or os.environ.get('MKDOCS_SKIP_WEBP'):
        print("[WebP Conversion] Skipping conversion in livereload mode (use 'mkdocs build' for WebP conversion)")
        return
    
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


def on_files(files, config):
    """
    Rename files to remove prefix numbers from the final URL paths.
    Keeps the numeric prefix in the source filename for sorting, but removes it from the dest_uri.
    """
    # for file in files:
    #     if file.src_path.endswith('.md') and file.src_path != 'index.md':
    #         # Extract the filename without extension
    #         parts = file.src_path.split('/')
    #         filename = parts[-1].replace('.md', '')
            
    #         # If filename starts with digits followed by a dash, remove them from dest_uri
    #         if filename and filename[0].isdigit() and '-' in filename:
    #             # Remove the prefix number and dash from the destination path
    #             cleaned_filename = re.sub(r'^\d+-', '', filename)
    #             # Update the dest_uri to use the cleaned filename
    #             new_dest_path = '/'.join(parts[:-1] + [cleaned_filename + '/index.html'])
    #             file.dest_uri = new_dest_path
    
    # return files



