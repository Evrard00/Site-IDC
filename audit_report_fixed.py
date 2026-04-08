import json
import sys
import io
from collections import Counter

# Fix encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 90)
print(" " * 20 + "RAPPORT COMPLET D'AUDIT DES ICONES")
print(" " * 30 + "Site-IDC (08/04/2026)")
print("=" * 90)

# RÉSUMÉ
print("\nRESUME EXECUTIF:")
print("-" * 90)
summary = data.get("summary", {})
print(f"  * Fichiers analyses: {summary.get('total_files_analyzed', 0)} ({summary.get('html_files', 0)} HTML + {summary.get('css_files', 0)} CSS)")
print(f"  * Icones totales detectees: {summary.get('total_icons_found', 0)}")

icon_types = summary.get("icon_types", {})
print(f"\n  Repartition par type:")
for itype, count in icon_types.items():
    print(f"    - {itype.upper()}: {count}")

# 1. EMOJIS ET LOCATIONS
print("\n" + "=" * 90)
print("1. EMOJIS DETECTES ET LEURS LOCATIONS:")
print("-" * 90)
emojis = data.get("emojis", [])
print(f"\nTotal: {len(emojis)} emojis uniques\n")

emoji_list = []
for idx, emoji_data in enumerate(emojis, 1):
    emoji = emoji_data.get("emoji", "?")
    name = emoji_data.get("name", "Unknown")
    unicode = emoji_data.get("unicode", "")
    locations = emoji_data.get("usage_locations", [])
    
    emoji_list.append((emoji, name))
    print(f"  {idx}. {name}")
    print(f"     Utilisation: {len(locations)} occurrence(s)")
    
    for loc in locations[:1]:
        file = loc.get("file", "?")
        usage = loc.get("usage", "?")
        context = loc.get("context", "")
        print(f"       - {file}: {usage}")

print(f"\n  === RECAPITULATIF EMOJIS ===")
for emoji, name in emoji_list[:15]:
    print(f"  {emoji} -> {name}")
if len(emoji_list) > 15:
    print(f"  ... et {len(emoji_list) - 15} autres")

# 2. TAILLES D'ICONES
print("\n" + "=" * 90)
print("2. TAILLES D'ICONES (font-size) UTILISEES:")
print("-" * 90)

styles = data.get("icon_styles_css", [])
sizes_used = {}
colors_used = {}

for style in styles:
    properties = style.get("properties", {})
    
    font_size = properties.get("font-size", "")
    if font_size:
        sizes_used[font_size] = sizes_used.get(font_size, 0) + 1
    
    color = properties.get("color", "")
    if color:
        colors_used[color] = colors_used.get(color, 0) + 1

print(f"\nTailles detectees: {len(sizes_used)}")
for size, count in sorted(sizes_used.items(), key=lambda x: x[1], reverse=True):
    print(f"  * {size}: {count} classe(s)")

# 3. COULEURS
print("\n" + "=" * 90)
print("3. COULEURS UTILISEES:")
print("-" * 90)
print(f"\nCouleurs uniques detectees: {len(colors_used)}\n")

for color, count in sorted(colors_used.items(), key=lambda x: x[1], reverse=True):
    print(f"  * {color}: {count} fois")

# 4. RECOMMENDATIONS
print("\n" + "=" * 90)
print("4. RECOMMENDATIONS POUR L'UNIFORMISATION:")
print("-" * 90)

print("\n1. STANDARDISATION DES TAILLES:")
print("   - Actuellement {} tailles differentes en utilisation".format(len(sizes_used)))
print("   - RECOMMANDATION: Reduire a 3-4 tailles standard (ex: 16px, 24px, 32px, 48px)")

print("\n2. PALETTE DE COULEURS:")
print("   - Actuellement {} couleurs utilisees".format(len(colors_used)))
print("   - RECOMMANDATION: Limiter a 5-6 couleurs principales + neutres")

print("\n3. COHERENCE DES TYPES D'ICONES:")
emojis_count = len(data.get("emojis", []))
material_count = len(data.get("material_symbols", []))
svg_count = len(data.get("svg_icons", []))
png_count = len(data.get("png_icons", []))
print(f"   - Emojis: {emojis_count}")
print(f"   - Material Symbols: {material_count}")
print(f"   - SVG: {svg_count}")
print(f"   - PNG: {png_count}")
print("   - RECOMMANDATION: Privilégier SVG + Material Symbols plutot que emojis/PNG")

print("\n4. ACCESSIBILITE:")
print("   - RECOMMANDATION: Ajouter des labels ARIA sur tous les emojis")
print("   - RECOMMANDATION: Verifier le contraste des couleurs (WCAG AA minimum)")

print("\n5. DOCUMENTATION:")
print("   - RECOMMANDATION: Creer un design system avec guide des icones")
print("   - RECOMMANDATION: Documenter les cas d'usage de chaque type")

print("\n" + "=" * 90)
print(" " * 35 + "FIN DU RAPPORT")
print("=" * 90)
