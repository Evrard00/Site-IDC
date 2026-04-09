"""
Script pour corriger les erreurs de normalisation et remplacer les emojis
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
HTML_FILES = list(PROJECT_ROOT.glob("src/*.html"))

for html_file in HTML_FILES:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        
        # Corriger les classes doublées icon-icon-*
        content = re.sub(r'icon-icon-', 'icon-', content)
        
        # Remplacer les emojis par des icônes appropriées
        replacements = {
            '📝': '<span class="material-symbols-outlined icon-neutral icon-m">receipt</span>',
            '👤': '<span class="material-symbols-outlined icon-neutral icon-m">person</span>',
            '📧': '<span class="material-symbols-outlined icon-neutral icon-xs" style="vertical-align: -2px; margin-right: 4px;">mail</span>',
            '⏱️': '<span class="material-symbols-outlined icon-warning icon-s" style="vertical-align: -2px; margin-right: 4px;">schedule</span>',
            '🔄': '<span class="material-symbols-outlined icon-warning icon-s" style="vertical-align: -2px; margin-right: 4px;">refresh</span>',
        }
        
        for emoji, icon_html in replacements.items():
            content = content.replace(emoji, icon_html)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Corrigé: {html_file.name}")
        else:
            print(f"- Aucun changement: {html_file.name}")
    except Exception as e:
        print(f"❌ Erreur pour {html_file.name}: {e}")

print("\n✅ Corrections terminées!")
