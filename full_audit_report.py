import json
from collections import Counter, defaultdict

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 90)
print(" " * 20 + "RAPPORT COMPLET D'AUDIT DES ICÔNES")
print(" " * 30 + "Site-IDC (08/04/2026)")
print("=" * 90)

# RÉSUMÉ
print("\n RÉSUMÉ EXÉCUTIF:")
print("-" * 90)
summary = data.get("summary", {})
print(f"   Fichiers analysés: {summary.get('total_files_analyzed', 0)} ({summary.get('html_files', 0)} HTML + {summary.get('css_files', 0)} CSS)")
print(f"   Icônes totales détectées: {summary.get('total_icons_found', 0)}")

icon_types = summary.get("icon_types", {})
print(f"\n  Répartition par type:")
for itype, count in icon_types.items():
    print(f"    - {itype.upper()}: {count}")

# 1. EMOJIS ET LOCATIONS
print("\n" + "=" * 90)
print(" 1. EMOJIS DÉTECTÉS ET LEURS LOCATIONS:")
print("-" * 90)
emojis = data.get("emojis", [])
print(f"\nTotal: {len(emojis)} emojis uniques\n")

for idx, emoji_data in enumerate(emojis, 1):
    emoji = emoji_data.get("emoji", "?")
    name = emoji_data.get("name", "Unknown")
    unicode = emoji_data.get("unicode", "")
    locations = emoji_data.get("usage_locations", [])
    
    print(f"  {idx}. {emoji} {name} ({unicode})")
    print(f"     Utilisation: {len(locations)} occurrence(s)")
    
    for loc in locations[:2]:  # Show first 2 locations
        file = loc.get("file", "?")
        line = loc.get("line", "?")
        usage = loc.get("usage", "?")
        print(f"        {file}:{line} - {usage}")
    
    if len(locations) > 2:
        print(f"       ... et {len(locations) - 2} autre(s)")

# 2. MATERIAL SYMBOLS
print("\n" + "=" * 90)
print(" 2. MATERIAL SYMBOLS UTILISÉS:")
print("-" * 90)
symbols = data.get("material_symbols", [])
print(f"\nTotal: {len(symbols)} symboles\n")

for idx, symbol_data in enumerate(symbols, 1):
    symbol = symbol_data.get("symbol", "?")
    name = symbol_data.get("name", "Unknown")
    locations = symbol_data.get("usage_locations", [])
    
    print(f"  {idx}. {name}")
    print(f"     Utilisation: {len(locations)} occurrence(s)")
    
    for loc in locations[:1]:
        file = loc.get("file", "?")
        usage = loc.get("usage", "?")
        print(f"       • {file} - {usage}")

# 3. SVG ICONS
print("\n" + "=" * 90)
print("🎨 3. SVG ICONS UTILISÉES:")
print("-" * 90)
svg_icons = data.get("svg_icons", [])
print(f"\nTotal: {len(svg_icons)} fichiers SVG\n")

for idx, svg_data in enumerate(svg_icons[:10], 1):  # Show first 10
    filename = svg_data.get("filename", "?")
    svg_type = svg_data.get("type", "")
    locations = svg_data.get("usage_locations", [])
    
    print(f"  {idx}. {filename} (Type: {svg_type})")
    print(f"     Utilisation: {len(locations)} occurrence(s)")

if len(svg_icons) > 10:
    print(f"  ... et {len(svg_icons) - 10} autres fichiers SVG")

# 4. PNG ICONS
print("\n" + "=" * 90)
print("🖼️  4. PNG ICONS UTILISÉES:")
print("-" * 90)
png_icons = data.get("png_icons", [])
print(f"\nTotal: {len(png_icons)} fichiers PNG\n")

for idx, png_data in enumerate(png_icons, 1):
    filename = png_data.get("filename", "?")
    png_type = png_data.get("type", "")
    locations = png_data.get("usage_locations", [])
    
    print(f"  {idx}. {filename} (Type: {png_type})")
    print(f"     Utilisation: {len(locations)} occurrence(s)")

# 5. ICON STYLES CSS
print("\n" + "=" * 90)
print("🎯 5. STYLES CSS D'ICÔNES:")
print("-" * 90)
styles = data.get("icon_styles_css", [])
print(f"\nTotal: {len(styles)} classes CSS\n")

# Collecte les tailles et couleurs
sizes_used = Counter()
colors_used = Counter()

for style in styles:
    class_name = style.get("class_name", "")
    properties = style.get("properties", {})
    
    # Extract font-size
    font_size = properties.get("font-size", "")
    if font_size:
        sizes_used[font_size] += 1
    
    # Extract color
    color = properties.get("color", "")
    if color:
        colors_used[color] += 1

# Afficher les tailles
print("  Tailles (font-size) utilisées:")
for size, count in sorted(sizes_used.items(), key=lambda x: x[1], reverse=True):
    print(f"    • {size}: {count} classe(s)")

# Afficher les couleurs
print("\n  Couleurs utilisées:")
unique_colors = list(colors_used.items())
for color, count in sorted(unique_colors, key=lambda x: x[1], reverse=True)[:10]:
    print(f"    • {color}: {count} classe(s)")

if len(unique_colors) > 10:
    print(f"    ... et {len(unique_colors) - 10} autre(s)\n")

# 6. RECOMMENDATIONS
print("=" * 90)
print("✅ 6. RECOMMENDATIONS POUR L'UNIFORMISATION:")
print("-" * 90)

recommendations = data.get("recommendations", {})

if "emoji_issues" in recommendations:
    print("\n  🔴 PROBLÈMES AVEC LES EMOJIS:")
    for issue in recommendations.get("emoji_issues", [])[:5]:
        print(f"     • {issue}")

if "material_symbols" in recommendations:
    print("\n  🔴 MATÉRIEL SYMBOLS:")
    for issue in recommendations.get("material_symbols", [])[:3]:
        print(f"     • {issue}")

if "svg_png_usage" in recommendations:
    print("\n  🔴 SVG/PNG USAGE:")
    for issue in recommendations.get("svg_png_usage", [])[:3]:
        print(f"     • {issue}")

if "accessibility" in recommendations:
    print("\n  🔴 ACCESSIBILITÉ:")
    for issue in recommendations.get("accessibility", [])[:3]:
        print(f"     • {issue}")

# Summary recommendations
print("\n  📋 ACTIONS RECOMMANDÉES:")
print("     1. Standardiser une palette de tailles d'icônes (établir 3-4 tailles max)")
print("     2. Réduire la mixité des types d'icônes (choisir SVG OU Material Symbols)")
print("     3. Créer une nomenclature cohérente et un système de design")
print("     4. Ajouter des labels ARIA pour l'accessibilité sur tous les emojis")
print("     5. Documenter les cas d'usage de chaque type d'icône")
print("     6. Implémenter des tests de cohérence visuelle et d'accessibilité")

print("\n" + "=" * 90)
print(" " * 35 + "FIN DU RAPPORT")
print("=" * 90)
