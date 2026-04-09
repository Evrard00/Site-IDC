"""
Script pour corriger TOUS les styles inline des icônes en une seule passe
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
HTML_FILES = list(PROJECT_ROOT.glob("src/*.html"))

total_fixed = 0

for html_file in HTML_FILES:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        
        # Regex universelle pour toutes les icônes avec styles inline
        # Détecte: <span class="material-symbols-outlined" ... style="..." ...>ICONNAME</span>
        def replace_inline_style(match):
            class_str = match.group(1)
            icon_name = match.group(2)
            
            # Construire les nouvelles classes basées sur le style inline
            new_classes = "material-symbols-outlined"
            style_inline = ""
            
            # Extraire seulement vertical-align et margin pour les conserver
            style_attr = match.group(0)
            if 'vertical-align' in style_attr:
                style_inline += " vertical-align: "
                v_match = re.search(r'vertical-align:\s*(-?[\d.]+)px', style_attr)
                if v_match:
                    style_inline += v_match.group(1) + "px;"
            
            if 'margin-right' in style_attr:
                if style_inline and not style_inline.endswith(";"):
                    style_inline += ";"
                style_inline += " margin-right: "
                m_match = re.search(r'margin-right:\s*(-?[\d.]+)px', style_attr)
                if m_match:
                    style_inline += m_match.group(1) + "px;"
            
            # Déterminer les classes basées sur la couleur et taille
            if '#0F6B32' in style_attr:
                new_classes += " icon-success"
            elif '#E36A13' in style_attr:
                new_classes += " icon-primary"
            else:
                new_classes += " icon-neutral"
            
            # Déterminer la taille
            if 'font-size: 64px' in style_attr:
                new_classes += " icon-xl"
            elif 'font-size: 28px' in style_attr:
                new_classes += " icon-l"
            elif 'font-size: 20px' in style_attr:
                pass  # pas de classe de taille standard pour 20px
            elif 'font-size: 16px' in style_attr:
                new_classes += " icon-s"
            
            # Préserver les autres styles si nécessaire
            if 'display: flex' in style_attr or 'width: 100%' in style_attr:
                preserve_style = ""
                if 'display: flex' in style_attr:
                    preserve_style += "display: flex; "
                if 'align-items: center' in style_attr:
                    preserve_style += "align-items: center; "
                if 'justify-content: center' in style_attr:
                    preserve_style += "justify-content: center; "
                if 'width: 100%' in style_attr:
                    preserve_style += "width: 100%; "
                if 'height: 100%' in style_attr:
                    preserve_style += "height: 100%;"
                if preserve_style:
                    return f'<span class="{new_classes}" style="{preserve_style}">{icon_name}</span>'
            
            if style_inline:
                return f'<span class="{new_classes}" style="{style_inline}">{icon_name}</span>'
            else:
                return f'<span class="{new_classes}">{icon_name}</span>'
        
        # Pattern regex pour capturer les spans avec styles
        pattern = r'<span\s+class="([^"]*material-symbols-outlined[^"]*)"[^>]*style="([^"]*)"[^>]*>([^<]+)</span>'
        
        # Faire le remplacement
        matches = re.finditer(pattern, content)
        original_len = len(re.findall(pattern, content))
        
        content = re.sub(pattern, replace_inline_style, content)
        
        if original_len > 0:
            total_fixed += original_len
            print(f"✓ {html_file.name}: {original_len} styles inline corrigés")
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    except Exception as e:
        print(f"❌ Erreur pour {html_file.name}: {e}")

print(f"\n✅ Correction terminée!")
print(f"   Total de styles inline corrigés: {total_fixed}")
