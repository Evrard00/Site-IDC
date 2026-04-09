#!/usr/bin/env python3
"""
Fix CSS content property issue: Replace HTML in CSS ::before with actual DOM elements.

Problem: CSS content property cannot render HTML markup. Lines showing:
    .service-details ul li:before { content: '<span class="material-symbols-outlined icon-success icon-s">done</span>'; }
    .request-card li:before { content: '<span class="material-symbols-outlined icon-success icon-s">done</span>'; }

Solution: Add the icon spans directly to the HTML list items and clean up the problematic CSS.
"""

import re
from pathlib import Path

def fix_css_content_property(file_path):
    """Fix CSS ::before with HTML content and add icons to list items."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modifications = 0
    
    # Extract the icon markup from CSS content property
    # Pattern: content: '<span class="material-symbols-outlined icon-success icon-s">done</span>';
    icon_pattern = r"content:\s*'<span[^>]*class=\"([^\"]*material-symbols-outlined[^\"]*)\"[^>]*>([^<]*)<\/span>';"
    
    icon_matches = list(re.finditer(icon_pattern, content))
    
    if not icon_matches:
        print(f"  ✓ No CSS content property issues found in {file_path.name}")
        return 0
    
    # Find which CSS rule contains this (service-details or request-card)
    # We need to fix TWO things:
    # 1. Remove the ::before { content: ... } CSS
    # 2. Add <span> icons directly to <li> elements
    
    # First, let's remove the problematic ::before CSS rules
    
    # Pattern 1: .service-details ul li:before { ... }
    service_details_pattern = r"\.service-details\s+ul\s+li:before\s*\{[^}]*content:\s*'<span[^>]*>done<\/span>'[^}]*\}"
    if re.search(service_details_pattern, content):
        # Replace with a simple CSS rule that hides the default bullet
        content = re.sub(
            r"\.service-details\s+ul\s+li:before\s*\{[^}]*content:\s*'<span[^>]*>done<\/span>'[^}]*\}",
            ".service-details ul li:before {\n            display: none;\n        }",
            content,
            flags=re.MULTILINE
        )
        modifications += 1
        print(f"  ✓ Fixed .service-details ul li:before CSS in {file_path.name}")
    
    # Pattern 2: .request-card li:before { ... }
    request_card_pattern = r"\.request-card\s+li:before\s*\{[^}]*content:\s*'<span[^>]*>done<\/span>'[^}]*\}"
    if re.search(request_card_pattern, content):
        content = re.sub(
            r"\.request-card\s+li:before\s*\{[^}]*content:\s*'<span[^>]*>done<\/span>'[^}]*\}",
            ".request-card li:before {\n            display: none;\n        }",
            content,
            flags=re.MULTILINE
        )
        modifications += 1
        print(f"  ✓ Fixed .request-card li:before CSS in {file_path.name}")
    
    # Now add icons to list items directly
    # For .service-details ul li items
    content = re.sub(
        r'(<div class="service-details"[^>]*>.*?)<li>([^<])',
        r'\1<li><span class="material-symbols-outlined icon-success icon-s">done</span> \2',
        content,
        flags=re.DOTALL
    )
    
    # For .request-card li items - simpler approach
    # Look for <ul> within .request-card and add icons to each <li>
    def add_icons_to_request_card_lists(match):
        ul_content = match.group(0)
        # Add icon to each <li> that doesn't already have one
        ul_content = re.sub(
            r'<li>([^<])',
            r'<li><span class="material-symbols-outlined icon-success icon-s">done</span> \1',
            ul_content
        )
        return ul_content
    
    # Find all <ul> within .request-card sections
    content = re.sub(
        r'(<div class="request-card[^>]*>.*?)<ul>(.*?)<\/ul>',
        lambda m: m.group(1) + '<ul>' + re.sub(
            r'<li>([^<])',
            r'<li><span class="material-symbols-outlined icon-success icon-s">done</span> \1',
            m.group(2)
        ) + '</ul>',
        content,
        flags=re.DOTALL
    )
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {file_path.name}")
        return modifications
    
    return 0

def main():
    """Main function to fix all HTML files."""
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Files to fix
    files_to_fix = [
        'src\\index.html',
        'src\\login.html',
        'public\\index.html',
        'public\\login.html'
    ]
    
    print("🔧 Fixing CSS content property issues...")
    print("-" * 50)
    
    total_fixes = 0
    for file_path in files_to_fix:
        full_path = workspace_root / file_path
        if full_path.exists():
            fixes = fix_css_content_property(full_path)
            total_fixes += fixes
        else:
            print(f"  ✗ File not found: {file_path}")
    
    print("-" * 50)
    print(f"✅ Completed! Fixed {total_fixes} CSS issues.")

if __name__ == '__main__':
    main()
