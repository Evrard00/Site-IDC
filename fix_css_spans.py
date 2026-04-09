#!/usr/bin/env python3
"""
Fix spans where CSS text appears as content instead of icon names.

Finds patterns like:
  <span ... style="...">vertical-align: -2px; margin-right: 4px;</span>

And replaces with proper icon names like:
  <span ... style="...">mail</span>
"""

import re
from pathlib import Path

def fix_all_files():
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Get all HTML files
    html_files = list(workspace_root.glob('src/**/*.html')) + list(workspace_root.glob('public/**/*.html'))
    
    print("🔧 Fixing spans with CSS content...\n")
    
    total_fixed = 0
    
    for file_path in sorted(html_files):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern: <span ... >vertical-align: ...; margin-right: ...;</span>
        # Replace with icon name based on context
        
        # 1. Mail icon - followed by email address
        content = re.sub(
            r'<span class="material-symbols-outlined icon-neutral"[^>]*style="[^"]*vertical-align:[^"]*margin-right:[^"]*"[^>]*>vertical-align:[^<]*margin-right:[^<]*</span>\s*(contact@|adama\.)',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">mail</span> \1',
            content
        )
        
        # 2. Phone icon - followed by phone number
        content = re.sub(
            r'<span class="material-symbols-outlined icon-neutral"[^>]*style="[^"]*vertical-align:[^"]*margin-right:[^"]*(?:font-size:[^"]*)?[^"]*"[^>]*>vertical-align:[^<]*margin-right:[^<]*(?:font-size:[^<]*)?</span>\s*\+225',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">phone</span> +225',
            content
        )
        
        # 3. Status badge icons - various statuses
        statuses = ['En attente', 'En cours', 'Négociation', 'Livrée', 'Active', 'Besoin d\'aide', 
                    'Cette liste est non exhaustive', 'Les prix ne sont pas', 'un commercial']
        
        content = re.sub(
            r'<span class="material-symbols-outlined icon-neutral"[^>]*style="[^"]*vertical-align:[^"]*margin-right:[^"]*(?:font-size:[^"]*)?[^"]*"[^>]*>vertical-align:[^<]*margin-right:[^<]*(?:font-size:[^<]*)?</span>\s+(En attente|En cours|Négociation|Livrée|Active)',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">schedule</span> \1',
            content
        )
        
        # 4. Help icon
        content = re.sub(
            r'<span class="material-symbols-outlined icon-neutral"[^>]*style="[^"]*vertical-align:[^"]*margin-right:[^"]*(?:font-size:[^"]*)?[^"]*"[^>]*>vertical-align:[^<]*margin-right:[^<]*(?:font-size:[^<]*)?</span>\s*Besoin',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">help_outline</span> Besoin',
            content
        )
        
        # 5. Generic fallback - replace any remaining CSS-as-content with "visibility"
        content = re.sub(
            r'<span class="material-symbols-outlined icon-neutral"[^>]*style="[^"]*vertical-align:[^"]*margin-right:[^"]*[^"]*"[^>]*>vertical-align:[^<]*margin-right:[^<]*</span>',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">info</span>',
            content
        )
        
        # 6. Similar patterns with different wording that also contain CSS
        content = re.sub(
            r'<span class="material-symbols-outlined[^>]*style="[^"]*vertical-align:[^"]*[^"]*"[^>]*>margin-right:[^<]*(?:vertical-align:[^<]*)?(?:font-size:[^<]*)?</span>',
            r'<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">info</span>',
            content
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Count changes
            changes = len(re.findall(r'semantic class=', original_content)) - len(re.findall(r'semantic class=', content))
            print(f"  ✓ {file_path.relative_to(workspace_root)}")
            total_fixed += 1
    
    print(f"\n✅ Fixed {total_fixed} files")

if __name__ == '__main__':
    fix_all_files()
