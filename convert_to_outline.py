#!/usr/bin/env python3
"""
Convert filled SVG icons to outline style by applying CSS modifications.
This script modifies the SVG files to use stroke instead of fill for outline appearance.
"""

from pathlib import Path
import re

def convert_to_outline_style():
    """Convert SVG icons from filled to outline style."""
    
    svg_dir = Path('d:\\Téléchargement\\Site-IDC\\assets\\icons\\svg')
    
    print("🎨 Converting SVG icons to outline style...\n")
    
    converted = 0
    
    for svg_file in svg_dir.glob('*.svg'):
        try:
            with open(svg_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Ensure SVG has style tag for outline effect
            if '<style>' not in content:
                # Add inline style for stroke
                content = content.replace(
                    '<svg ',
                    '<style>path, circle, rect, polygon, polyline { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }</style><svg '
                )
            
            # Also add style attribute if not present to preserve viewBox
            if 'style=' not in content and '<svg' in content:
                content = content.replace(
                    '<svg',
                    '<svg style="fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"',
                    1
                )
            
            if content != original:
                with open(svg_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                converted += 1
                print(f"  ✓ {svg_file.name}: converted to outline")
        
        except Exception as e:
            print(f"  ✗ {svg_file.name}: {str(e)}")
    
    print(f"\n{'='*50}")
    print(f"✅ Converted: {converted} SVG files to outline style\n")

if __name__ == '__main__':
    convert_to_outline_style()
