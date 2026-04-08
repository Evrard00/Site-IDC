import json
import sys
import io

# Fix encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("\n" + "=" * 100)
print(" " * 30 + "RESUME COMPLET - AUDIT DES ICONES")
print(" " * 35 + "Site-IDC 2026")
print("=" * 100)

# ===== SECTION 1: EMOJIS =====
print("\n1. EMOJIS UTILISES (28 total)")
print("-" * 100)
emojis = data.get("emojis", [])
emoji_summary = []
for emoji_data in emojis:
    emoji = emoji_data.get("emoji", "?")
    name = emoji_data.get("name", "")
    locations = emoji_data.get("usage_locations", [])
    emoji_summary.append(f"{emoji} {name} ({len(locations)} x)")

# Afficher en colonnes
col_width = 30
for i in range(0, len(emoji_summary), 3):
    line = ""
    for j in range(3):
        if i + j < len(emoji_summary):
            line += emoji_summary[i+j].ljust(col_width)
    print("  " + line)

# ===== SECTION 2: TAILLES =====
print("\n" + "=" * 100)
print("2. TAILLES D'ICONES UTILISEES")
print("-" * 100)
styles = data.get("icon_styles_css", [])
sizes_dict = {}
for style in styles:
    props = style.get("properties", {})
    font_size = props.get("font_size", props.get("font-size", ""))
    if font_size:
        sizes_dict[font_size] = sizes_dict.get(font_size, 0) + 1

if sizes_dict:
    print("\n  Tailles detectees:")
    for size in sorted(sizes_dict.keys()):
        count = sizes_dict[size]
        bar = "*" * count
        print(f"    {size:15} | {bar} ({count})")
else:
    print("\n  Pas de tailles specifiques trouvees dans les CSS")
    print("  Les tailles sont souvent heritees du contexte ou definies inline")

# ===== SECTION 3: COULEURS =====
print("\n" + "=" * 100)
print("3. COULEURS UTILISEES")
print("-" * 100)
colors_dict = {}
for style in styles:
    props = style.get("properties", {})
    color = props.get("color", "")
    if color:
        colors_dict[color] = colors_dict.get(color, 0) + 1

if colors_dict:
    print("\n  Couleurs detectees:")
    for color, count in sorted(colors_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"    {color:15} | Utilisation: {count} classe(s)")
else:
    print("\n  Pas de couleurs specifiques trouvees dans les CSS des icones")

# ===== SECTION 4: REPARTITION DES TYPES =====
print("\n" + "=" * 100)
print("4. REPARTITION PAR TYPE D'ICONE")
print("-" * 100)
summary = data.get("summary", {})
icon_types = summary.get("icon_types", {})

total = sum(icon_types.values())
print(f"\n  Total icones: {total}")
print()

for itype, count in sorted(icon_types.items(), key=lambda x: x[1], reverse=True):
    percent = (count / total) * 100
    bar = "#" * int(percent / 2)
    print(f"  {itype.upper():20} | {count:3} icones ({percent:5.1f}%) | {bar}")

# ===== SECTION 5: RECOMMENDATIONS =====
print("\n" + "=" * 100)
print("5. RECOMMENDATIONS CLES POUR L'UNIFORMISATION")
print("-" * 100)

recommendations = """
PROBLEME 1: MIXITE DES TYPES D'ICONES
  - Situation: 28 emojis + 15 Material Symbols + 17 SVG + 2 PNG
  - Risque: Coherence visuelle faible, maintenance difficile
  - Solution: Adopter un systeme unifie (SVG ou Material Design)
  
PROBLEME 2: ABSENCE DE STANDARDISATION DES TAILLES
  - Situation: Tailles definies de maniere ad-hoc (48px, 28px, 24px, 18px)
  - Risque: Incoherence visuelle
  - Solution: 
    * Definir 4 tailles: S(16px), M(24px), L(32px), XL(48px)
    * Appliquer systematiquement dans les CSS

PROBLEME 3: PALETTE DE COULEURS REDUITE
  - Situation: Une seule couleur detectee (#E36A13 orange)
  - Risque: Limitation semantique (pas de variation pour etats, etc.)
  - Solution: Definir 5-6 couleurs principales + variantes

PROBLEME 4: ACCESSIBILITE AUX EMOJIS
  - Situation: 28 emojis sans labels ARIA
  - Risque: Inaccessible aux lecteurs d'ecran
  - Solution:
    * Ajouter aria-label ou aria-hidden="true" sur tous les emojis
    * Verifier les ratios de contraste (WCAG AA minimum)

PROBLEME 5: DOCUMENTATION INSUFFISANTE
  - Situation: Pas de guide des icones ou design system
  - Risque: Incoherence lors des futures evolutions
  - Solution:
    * Creer un guide des icones avec regles et cas d'usage
    * Documenter les conventions de nommage et styles

ACTIONS A COURT TERME:
  1. Choisir entre SVG et Material Symbols (recommande: SVG pour cohesion)
  2. Migrer les emojis importants vers SVG
  3. Creer une palette de couleurs homogene
  4. Standardiser les 4 tailles principales

ACTIONS A LONG TERME:
  1. Developper un design system complet
  2. Creer une librairie d'icones reutilisables
  3. Implémenter des tests d'accessibilite
  4. Maintenir la documentation à jour
"""

print(recommendations)

print("\n" + "=" * 100)
print(" " * 40 + "FIN DU RAPPORT")
print("=" * 100 + "\n")
