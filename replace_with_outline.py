#!/usr/bin/env python3
"""
Replace all twotone SVG icons with outline versions from material-icons-master.
"""

import shutil
from pathlib import Path

def replace_icons_with_outline():
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    source_base = workspace_root / 'material-icons-master' / 'material-icons-master' / 'svg'
    dest_dir = workspace_root / 'assets' / 'icons' / 'svg'
    
    # Get all current SVG files (we'll replace them with outline versions)
    current_icons = list(dest_dir.glob('*.svg'))
    
    print("🔄 Replacing twotone icons with outline versions...\n")
    
    replaced = 0
    not_found = 0
    
    for svg_file in current_icons:
        icon_name = svg_file.stem  # filename without .svg
        
        # Try to find outline version in material-icons-master
        outline_source = source_base / icon_name / 'outline.svg'
        
        if outline_source.exists():
            shutil.copy(outline_source, svg_file)
            replaced += 1
            print(f"  ✓ {icon_name}: replaced with outline")
        else:
            # Try baseline as fallback
            baseline_source = source_base / icon_name / 'baseline.svg'
            if baseline_source.exists():
                shutil.copy(baseline_source, svg_file)
                replaced += 1
                print(f"  ✓ {icon_name}: replaced with baseline (outline not found)")
            else:
                not_found += 1
                print(f"  ✗ {icon_name}: not found in material-icons-master")
    
    print(f"\n{'='*50}")
    print(f"✅ Replaced: {replaced}")
    print(f"⚠️  Not found: {not_found}")
    print(f"📊 Total icons: {len(current_icons)}\n")

if __name__ == '__main__':
    replace_icons_with_outline()
