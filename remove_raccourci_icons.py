#!/usr/bin/env python3
"""
Supprime les boutons icônes de la section raccourcis et ajoute du texte simple
"""

from pathlib import Path
import re

def remove_raccourci_icons():
    """Supprime les icônes de la section raccourcis"""
    
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    html_files = [
        workspace_root / 'src' / 'index.html',
        workspace_root / 'public' / 'index.html',
    ]
    
    for file_path in html_files:
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vider la div raccourcis-grid
        original_content = content
        content = re.sub(
            r'<div class="raccourcis-grid">\s*</div>',
            '<div class="raccourcis-grid">\n                        </div>',
            content,
            flags=re.MULTILINE
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {file_path.name}: raccourcis-grid emptied")
        else:
            print(f"ℹ️  {file_path.name}: No changes needed")

if __name__ == '__main__':
    print("🗑️  Removing raccourci icons...")
    remove_raccourci_icons()
    print("✅ Done!")
