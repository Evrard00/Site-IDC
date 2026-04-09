"""
Script pour remplacer les icônes Material Symbols par les SVG du dossier material-icons-master
"""

import os
import re
import json
import shutil
from pathlib import Path

# Chemins
PROJECT_ROOT = Path(__file__).parent
MATERIAL_ICONS_SRC = PROJECT_ROOT / "material-icons-master" / "material-icons-master" / "svg"
ICONS_DEST = PROJECT_ROOT / "assets" / "icons" / "svg"
DATA_FILE = PROJECT_ROOT / "material-icons-master" / "material-icons-master" / "data.json"

# Créer le répertoire de destination s'il n'existe pas
ICONS_DEST.mkdir(parents=True, exist_ok=True)

# Extraire les noms des icônes utilisés dans les fichiers HTML
def extract_icon_names():
    """Extrait tous les noms d'icônes utilisés dans le projet"""
    icon_names = set()
    
    # Chercher les icônes dans les fichiers HTML
    for html_file in PROJECT_ROOT.rglob("*.html"):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Regex pour trouver les icônes Material Symbols
                # Pattern: <span class="material-symbols-outlined ...">ICON_NAME</span>
                matches = re.findall(r'<span\s+class="material-symbols-outlined[^"]*">([^<]+)</span>', content)
                icon_names.update(matches)
        except:
            pass
    
    return sorted(list(icon_names))

# Copier les SVG des icônes utilisées
def copy_svg_icons(icon_names, style="twotone"):
    """Copie les SVG des icônes utilisées vers le dossier de destination"""
    copied = []
    not_found = []
    
    for icon_name in icon_names:
        source_dir = MATERIAL_ICONS_SRC / icon_name
        if source_dir.exists():
            # Chercher le fichier SVG avec le style demandé (twotone par défaut)
            style_file = source_dir / f"{style}.svg"
            if style_file.exists():
                dest_file = ICONS_DEST / f"{icon_name}.svg"
                shutil.copy(style_file, dest_file)
                copied.append(icon_name)
            else:
                # Fallback sur baseline si twotone n'existe pas
                baseline_file = source_dir / "baseline.svg"
                if baseline_file.exists():
                    dest_file = ICONS_DEST / f"{icon_name}.svg"
                    shutil.copy(baseline_file, dest_file)
                    copied.append(icon_name)
        else:
            not_found.append(icon_name)
    
    return copied, not_found

# Créer le mapping CSS pour les icônes
def create_icon_mapping():
    """Crée un fichier CSS pour mapper les icônes et les afficher"""
    css_content = """/* ==========================================
   SVG ICONS MAPPING - IDC
   Remplace les Material Symbols par des SVG locaux
   ========================================== */

.icon-svg {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: auto;
    height: auto;
}

.icon-svg svg {
    height: 1em;
    width: 1em;
    display: inherit;
}

/* Tailles */
.icon-svg.icon-xs { font-size: 12px; }
.icon-svg.icon-s { font-size: 16px; }
.icon-svg.icon-m { font-size: 24px; }
.icon-svg.icon-l { font-size: 32px; }
.icon-svg.icon-xl { font-size: 48px; }

/* Couleurs */
.icon-svg.icon-primary svg { color: #E36A13; }
.icon-svg.icon-secondary svg { color: #0F6B32; }
.icon-svg.icon-dark svg { color: #0B0B0B; }
.icon-svg.icon-light svg { color: #F4F4F4; }
.icon-svg.icon-neutral svg { color: #4F4F4F; }
"""
    
    css_file = PROJECT_ROOT / "assets" / "css" / "icons-svg.css"
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    return css_file

# Créer un fichier JavaScript pour charger les SVG
def create_svg_loader_js():
    """Crée un JavaScript pour charger et afficher les SVG"""
    js_content = """/**
 * Système de chargement des icônes SVG
 * Remplace les Material Symbols par les SVG locaux
 */

class IconLoader {
    constructor() {
        this.svgCache = {};
        this.baseUrl = '/assets/icons/svg/';
        this.init();
    }

    init() {
        // Convertir tous les material-symbols-outlined en SVG
        this.convertMaterialSymbolsToSVG();
    }

    convertMaterialSymbolsToSVG() {
        const icons = document.querySelectorAll('.material-symbols-outlined');
        icons.forEach(el => {
            const iconName = el.textContent.trim();
            this.loadAndReplaceSVG(el, iconName);
        });
    }

    async loadAndReplaceSVG(element, iconName) {
        try {
            const svg = await this.getSVG(iconName);
            if (svg) {
                // Préserver les classes
                const classes = element.getAttribute('class');
                const wrapper = document.createElement('span');
                wrapper.setAttribute('class', classes.replace('material-symbols-outlined', 'icon-svg'));
                wrapper.innerHTML = svg;
                element.replaceWith(wrapper);
            }
        } catch (error) {
            console.warn(`Impossible de charger l'icône: ${iconName}`, error);
        }
    }

    async getSVG(name) {
        if (this.svgCache[name]) {
            return this.svgCache[name];
        }

        try {
            const response = await fetch(`${this.baseUrl}${name}.svg`);
            if (response.ok) {
                const svg = await response.text();
                this.svgCache[name] = svg;
                return svg;
            }
        } catch (error) {
            console.error(`Erreur lors du chargement de ${name}.svg:`, error);
        }
        return null;
    }
}

// Initialiser quand le DOM est prêt
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new IconLoader();
    });
} else {
    new IconLoader();
}
"""
    
    js_file = PROJECT_ROOT / "assets" / "js" / "icon-loader.js"
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    return js_file

# Script principal
if __name__ == "__main__":
    print("🔄 Extraction des icônes utilisées...")
    icon_names = extract_icon_names()
    print(f"✓ {len(icon_names)} icônes trouvées: {', '.join(icon_names[:10])}{'...' if len(icon_names) > 10 else ''}")
    
    print("\n📁 Copie des SVG (style: twotone)...")
    copied, not_found = copy_svg_icons(icon_names, style="twotone")
    print(f"✓ {len(copied)} icônes copiées en style twotone")
    if not_found:
        print(f"⚠ {len(not_found)} icônes non trouvées: {', '.join(not_found)}")
    
    print("\n📝 Création des fichiers de configuration...")
    create_icon_mapping()
    print("✓ Fichier CSS créé: assets/css/icons-svg.css")
    
    create_svg_loader_js()
    print("✓ Fichier JS créé: assets/js/icon-loader.js")
    
    print("\n✅ Configuration terminée!")
    print("\n📌 Prochaines étapes:")
    print("1. Ajouter dans <head> : <link rel=\"stylesheet\" href=\"/assets/css/icons-svg.css\">")
    print("2. Ajouter avant </body> : <script src=\"/assets/js/icon-loader.js\"></script>")
    print("3. Les icônes Material Symbols seront automatiquement remplacées par des SVG")
