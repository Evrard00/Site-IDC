"""
Script pour normaliser les fichiers SVG et le HTML
- Ajouter les attributs de stroke pour les icônes outline
- Normaliser les classes dans le HTML
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SVG_DIR = PROJECT_ROOT / "assets" / "icons" / "svg"

def normalize_svgs():
    """Ajouter les propriétés nécessaires aux SVG outline"""
    for svg_file in SVG_DIR.glob("*.svg"):
        try:
            with open(svg_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ajouter viewBox si absent
            if 'viewBox=' not in content:
                content = content.replace('<svg', '<svg viewBox="0 0 24 24"', 1)
            
            # Traiter les paths pour les icônes outline
            # Ajouter stroke-width, stroke-linecap, stroke-linejoin si pas de fill significatif
            if 'stroke=' not in content or 'stroke-width=' not in content:
                # Remplacer les paths pour ajouter les propriétés stroke
                content = re.sub(
                    r'<path\s+d="([^"]*)"',
                    r'<path d="\1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"',
                    content
                )
            
            with open(svg_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Normalisé: {svg_file.name}")
        except Exception as e:
            print(f"❌ Erreur pour {svg_file.name}: {e}")

def normalize_html():
    """Normaliser les classes d'icônes dans le HTML"""
    html_files = list(PROJECT_ROOT.glob("src/*.html"))
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            # Remplacer les classes combinées comme icon-secondary-m par icon-secondary icon-m
            content = re.sub(
                r'class="([^"]*)(icon-(?:primary|secondary|dark|neutral|light))-([xslm])(.*?)"',
                r'class="\1icon-\2 icon-\3\4"',
                content
            )
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Normalisé HTML: {html_file.name}")
        except Exception as e:
            print(f"❌ Erreur pour {html_file.name}: {e}")

if __name__ == "__main__":
    print("🔧 Normalisation des SVG...")
    normalize_svgs()
    print("\n🔧 Normalisation du HTML...")
    normalize_html()
    print("\n✅ Normalisation terminée!")
