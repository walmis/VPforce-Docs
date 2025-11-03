"""
MkDocs hook to handle image path rewriting.
This allows images from ../media/Pictures/ to be properly served.
"""

import os
import shutil
from pathlib import Path


def on_pre_build(config):
    """
    Copy media files to docs directory before build.
    This ensures images are accessible during the build process.
    """
    # Get the project root directory
    docs_dir = Path(config['docs_dir'])
    project_root = docs_dir.parent
    
    # Source and destination paths
    media_source = project_root / 'media'
    media_dest = docs_dir / 'media'
    
    # Copy media directory if it exists
    if media_source.exists():
        print(f"Copying media files from {media_source} to {media_dest}")
        
        # Remove existing media directory in docs if it exists
        if media_dest.exists():
            shutil.rmtree(media_dest)
        
        # Copy the media directory
        shutil.copytree(media_source, media_dest)
        print(f"Media files copied successfully")
    else:
        print(f"Warning: Media source directory {media_source} not found")


def on_post_build(config):
    """
    Optional: Clean up copied media files after build if desired.
    Comment out if you want to keep media in docs directory.
    """
    pass
    # Uncomment below to clean up after build:
    # docs_dir = Path(config['docs_dir'])
    # media_dest = docs_dir / 'media'
    # if media_dest.exists():
    #     shutil.rmtree(media_dest)
    #     print("Cleaned up temporary media files")
