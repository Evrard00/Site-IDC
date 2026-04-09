"""
Script pour corriger les styles inline des icônes
Remplacer les styles inline par les classes CSS appropriées
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
HTML_FILES = list(PROJECT_ROOT.glob("src/*.html"))

# Mappings de correction
corrections = [
    # Style inline avec color et font-size
    {
        'pattern': r'<span class="material-symbols-outlined"[^>]*style="color: #0F6B32; font-size: 16px;"[^>]*>([^<]+)</span>',
        'replacement': r'<span class="material-symbols-outlined icon-success icon-s">\1</span>',
        'description': 'Color #0F6B32 + font-size 16px'
    },
    # Style inline avec font-size, vertical-align, margin-right et color (E36A13)
    {
        'pattern': r'<span class="material-symbols-outlined"[^>]*style="font-size: 16px; vertical-align: -2px; margin-right: 4px; color: #E36A13;"[^>]*>([^<]+)</span>',
        'replacement': r'<span class="material-symbols-outlined icon-primary icon-s" style="vertical-align: -2px; margin-right: 4px;">\1</span>',
        'description': 'Font-size 16px + color orange'
    },
    # Style inline avec font-size, vertical-align, margin-right (20px)
    {
        'pattern': r'<span class="material-symbols-outlined"[^>]*style="font-size: 20px; vertical-align: -4px; margin-right: 8px;"[^>]*>([^<]+)</span>',
        'replacement': r'<span class="material-symbols-outlined icon-neutral" style="vertical-align: -4px; margin-right: 8px; font-size: 20px;">\1</span>',
        'description': 'Font-size 20px'
    },
    # Style inline avec font-size 28px
    {
        'pattern': r'<span class="material-symbols-outlined"[^>]*style="font-size: 28px; margin-right: 8px; vertical-align: -2px;"[^>]*>([^<]+)</span>',
        'replacement': r'<span class="material-symbols-outlined icon-l" style="margin-right: 8px; vertical-align: -2px;">\1</span>',
        'description': 'Font-size 28px'
    },
    # Style inline avec font-size 64px et color orange
    {
        'pattern': r'<span class="material-symbols-outlined"[^>]*style="font-size: 64px; color: #E36A13; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;"[^>]*>([^<]+)</span>',
        'replacement': r'<span class="material-symbols-outlined icon-primary icon-xl" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">\1</span>',
        'description': 'Font-size 64px + color orange + flex'
    },
]

total_fixed = 0
files_modified = set()

for html_file in HTML_FILES:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        
        for i, correction in enumerate(corrections):
            pattern = correction['pattern']
            replacement = correction['replacement']
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                files_modified.add(html_file.name)
                total_fixed += len(matches)
                print(f"  {html_file.name}: {len(matches)} corrections ({correction['description']})")
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f"❌ Erreur pour {html_file.name}: {e}")

print(f"\n✅ Correction terminée!")
print(f"   • Fichiers modifiés: {len(files_modified)}")
print(f"   • Styles inline corrigés: {total_fixed}")
print(f"   • Fichiers: {', '.join(sorted(files_modified))}")
