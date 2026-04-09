"""
Script pour intégrer les icônes SVG dans tous les fichiers HTML
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

def add_svg_support_to_html(html_file):
    """Ajoute le support SVG à un fichier HTML"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Chemin relatif depuis le fichier HTML jusqu'à la racine du projet
        depth = len(html_file.relative_to(PROJECT_ROOT).parts) - 1
        relative_prefix = '../' * depth if depth > 0 else ''
        
        # Ajouter le CSS des icônes SVG avant la fermeture du </head>
        if '<link rel="stylesheet" href="/assets/css/icons-svg.css">' not in content and \
           '<!-- SVG Icons CSS -->' not in content:
            # Remplacer </head> par le CSS + </head>
            css_link = f'    <link rel="stylesheet" href="{relative_prefix}assets/css/icons-svg.css">\n    <!-- SVG Icons CSS loaded -->\n</head>'
            content = content.replace('</head>', css_link)
            modified = True
        
        # Ajouter le script des icônes SVG avant la fermeture du </body>
        if '<script src="/assets/js/icon-loader.js"></script>' not in content and \
           '<!-- SVG Icon Loader -->' not in content:
            # Remplacer </body> par le script + </body>
            script_tag = f'\n    <script src="{relative_prefix}assets/js/icon-loader.js"></script>\n    <!-- SVG Icon Loader loaded -->\n</body>'
            content = content.replace('</body>', script_tag)
            modified = True
        
        if modified:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    
    except Exception as e:
        print(f"❌ Erreur pour {html_file}: {e}")
        return False

# Modifier tous les fichiers HTML
html_files = PROJECT_ROOT.rglob('*.html')
modified_count = 0
total_count = 0

for html_file in html_files:
    # Ignorer le footer.html qui est un fragment
    if 'footer.html' not in str(html_file):
        total_count += 1
        if add_svg_support_to_html(html_file):
            modified_count += 1
            print(f"✓ {html_file.relative_to(PROJECT_ROOT)}")

print(f"\n✅ {modified_count}/{total_count} fichiers HTML modifiés")
