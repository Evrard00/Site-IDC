#!/usr/bin/env python3
"""
Fix all spans where CSS text appears as content instead of icon names.

Analyze each file and replace CSS content with appropriate icon names.
"""

import re
from pathlib import Path

def get_context_icon(line_text):
    """Determine the appropriate icon based on surrounding text."""
    text_lower = line_text.lower()
    
    if 'mail' in text_lower or 'email' in text_lower or 'contact@' in text_lower:
        return 'mail'
    elif 'phone' in text_lower or '+225' in text_lower or 'tel:' in text_lower:
        return 'phone'
    elif 'en attente' in text_lower:
        return 'schedule'
    elif 'en cours' in text_lower:
        return 'schedule'
    elif 'négociation' in text_lower:
        return 'schedule'
    elif 'livrée' in text_lower or 'delivered' in text_lower:
        return 'done'
    elif 'active' in text_lower or 'activé' in text_lower:
        return 'check_circle'
    elif 'panier' in text_lower or 'cart' in text_lower:
        return 'shopping_cart'
    elif 'besoin' in text_lower or 'help' in text_lower:
        return 'help_outline'
    elif 'prix' in text_lower or 'tarif' in text_lower:
        return 'attach_money'
    elif 'this' in text_lower or 'cette liste' in text_lower or 'profils' in text_lower:
        return 'info'
    elif 'abidjan' in text_lower or 'location' in text_lower:
        return 'location_on'
    else:
        return 'info'  # default

def fix_file(file_path):
    """Fix CSS spans in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    
    # Pattern to detect CSS in span content
    css_pattern = r'(vertical-align:\s*[^;]*;?\s*(?:margin-right:[^;]*;?)?(?:font-size:[^;]*;?)?)'
    
    for i, line in enumerate(lines):
        # Check if this line has the problematic pattern
        if 'material-symbols-outlined' in line and css_pattern in line:
            # Extract the full line for context
            context = ''.join(lines[max(0, i-2):min(len(lines), i+3)])
            
            # Determine the appropriate icon
            icon_name = get_context_icon(context)
            
            # Replace CSS content with icon name
            # Pattern: style="...">CSS_TEXT</span>
            new_line = re.sub(
                r'(material-symbols-outlined[^>]*style="[^"]*">)(?:vertical-align:[^<]*;?\s*(?:margin-right:[^<]*;?)?(?:font-size:[^<]*;?)?)</span>',
                rf'\1{icon_name}</span>',
                line
            )
            
            if new_line != line:
                lines[i] = new_line
                modified = True
                print(f"  Line {i+1}: {line.strip()[:60]}... → {icon_name}")
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    return False

def main():
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Files with issues (from grep search)
    files_with_issues = [
        'src/cartes-tpe.html',
        'src/client.html',
        'src/contact.html',
        'src/dashboard.html',
        'src/eshop.html',
        'src/index.html',
        'src/jobs.html',
        'src/purchases.html',
    ]
    
    print("🔧 Fixing CSS text in span content...\n")
    
    fixed_count = 0
    for file_rel in files_with_issues:
        file_path = workspace_root / file_rel
        if file_path.exists():
            print(f"\n📄 {file_rel}")
            if fix_file(file_path):
                fixed_count += 1
        else:
            print(f"  ✗ Not found")
    
    print(f"\n{'='*50}")
    print(f"✅ Fixed {fixed_count} files\n")

if __name__ == '__main__':
    main()
