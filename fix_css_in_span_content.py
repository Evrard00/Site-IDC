#!/usr/bin/env python3
"""
Fix spans where CSS appears as literal text instead of icon names.

Problem: <span class="material-symbols-outlined" style="...">vertical-align: -2px; margin-right: 4px;</span>
The span contains CSS text instead of an icon name.

Solution: Replace CSS content with proper icon names (from the style attributes or use defaults)
"""

import re
from pathlib import Path

def fix_css_span_content(file_path):
    """Fix spans where CSS text appears as content instead of icon names."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modifications = 0
    
    # Pattern: <span class="material-symbols-outlined ... style=" ... ">vertical-align: ...; margin-right: ...;</span>
    # The content is CSS text instead of icon name
    
    # Find all problematic spans where content is CSS text
    pattern = r'<span([^>]*class="material-symbols-outlined[^"]*"[^>]*style="[^"]*"[^>]*)>vertical-align:[^<]*margin-right:[^<]*</span>'
    
    matches = list(re.finditer(pattern, content))
    
    if matches:
        print(f"\n  ✓ Found {len(matches)} spans with CSS as content in {file_path.name}")
        
        # Common icon name mappings based on context
        # Since we need to preserve the icon meaning, we'll use common defaults
        # or extract from class attributes
        
        # Replace these with generic icon placeholders
        # The actual icon will be loaded by JavaScript
        content = re.sub(
            pattern,
            r'<span\1>visibility</span>',  # Use visibility as default icon for status/data placeholders
            content
        )
        modifications += len(matches)
    
    # More specific patterns for footer contact info
    # Pattern: style attribute with specific properties
    
    # Email icon pattern
    content = re.sub(
        r'<span class="material-symbols-outlined icon-neutral" style="[^"]*">vertical-align:[^<]*margin-right:[^<]*</span>\s+contact@idc\.ci',
        r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -2px; margin-right: 4px;">mail</span> contact@idc.ci',
        content
    )
    if content != original_content:
        modifications += 1
    
    # Phone icon pattern
    content = re.sub(
        r'<span class="material-symbols-outlined icon-neutral" style="[^"]*">vertical-align:[^<]*margin-right:[^<]*(?:font-size:[^"]*)?</span>\s+\+225',
        r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -2px; margin-right: 4px;">phone</span> +225',
        content
    )
    if content != original_content:
        modifications += 1
    
    # Generic status badge pattern - En attente, En cours, Négociation, Livrée, Active
    content = re.sub(
        r'<span class="material-symbols-outlined icon-neutral" style="[^"]*">vertical-align:[^<]*margin-right:[^<]*</span>\s+(En attente|En cours|Négociation|Livrée|Active)',
        r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -2px; margin-right: 4px;">schedule</span> \1',
        content
    )
    if content != original_content:
        modifications += 1
    
    # Email in contact section
    content = re.sub(
        r'<span class="material-symbols-outlined icon-neutral" style="[^"]*">vertical-align:[^<]*margin-right:[^<]*</span>\s+contact@idc\.ci',
        r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -2px; margin-right: 4px;">mail</span> contact@idc.ci',
        content
    )
    if content != original_content:
        modifications += 1
    
    # Help text pattern
    content = re.sub(
        r'<span class="material-symbols-outlined icon-neutral" style="[^"]*">vertical-align:[^<]*margin-right:[^<]*</span>\s+Besoin',
        r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -2px; margin-right: 4px;">help_outline</span> Besoin',
        content
    )
    if content != original_content:
        modifications += 1
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {file_path.name}")
        return modifications
    
    return 0

def main():
    """Main function to fix all HTML files."""
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Search for all HTML files with the problematic pattern
    html_files = list(workspace_root.glob('src/**/*.html')) + list(workspace_root.glob('public/**/*.html'))
    
    print("🔧 Fixing CSS-as-content spans...")
    print("-" * 50)
    
    total_fixes = 0
    for file_path in sorted(html_files):
        fixes = fix_css_span_content(file_path)
        total_fixes += fixes
    
    print("-" * 50)
    print(f"✅ Completed! Fixed {total_fixes} span content issues.")

if __name__ == '__main__':
    main()
