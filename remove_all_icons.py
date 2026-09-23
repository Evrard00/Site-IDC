#!/usr/bin/env python3
"""
Remove all icon references from HTML files.
This removes all <span class="material-symbols-outlined"> elements.
"""

import re
from pathlib import Path

def remove_all_icons():
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Get all HTML files
    html_files = list(workspace_root.glob('src/**/*.html')) + list(workspace_root.glob('public/**/*.html'))
    
    print("🗑️  Removing all icon references from HTML files...\n")
    
    removed_total = 0
    
    for html_file in sorted(html_files):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Pattern 1: Remove entire <span class="material-symbols-outlined ...">...</span> tags
        # This includes multi-line patterns
        content = re.sub(
            r'<span\s+class="material-symbols-outlined[^"]*"[^>]*>.*?</span>\s*',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Pattern 2: Remove emoji icons (any emoji character)
        content = re.sub(
            r'[🀀-🿿]',  # emoji range
            '',
            content
        )
        
        # Pattern 3: Remove icon divs that only contain emojis or are empty
        content = re.sub(
            r'<div class="pourquoi-icon">\s*</div>',
            '',
            content
        )
        
        # Pattern 4: Remove raccourci buttons with icons
        content = re.sub(
            r'<a[^>]*class="raccourci-btn"[^>]*>.*?</a>\s*',
            '',
            content,
            flags=re.DOTALL
        )
        
        if content != original:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            removed = len(re.findall(r'material-symbols-outlined', original))
            removed_total += removed
            print(f"  ✓ {html_file.relative_to(workspace_root)}: removed {removed} icon references")
    
    print(f"\n{'='*50}")
    print(f"✅ Total icon references removed: {removed_total}\n")

if __name__ == '__main__':
    remove_all_icons()
