import json
import sys
import io

# Fix encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("\n" + "=" * 90)
print("DETAILS ADDITIONNELS - MATERIAL SYMBOLS & SVG")
print("=" * 90)

# MATERIAL SYMBOLS
print("\n[MATERIAL SYMBOLS - 15 SYMBOLES]")
print("-" * 90)
symbols = data.get("material_symbols", [])
for idx, sym in enumerate(symbols, 1):
    name = sym.get("name", "Unknown")
    locations = sym.get("usage_locations", [])
    loc_files = list(set([loc.get("file", "?") for loc in locations]))
    print(f"  {idx}. {name} - utilise dans: {', '.join(loc_files[:2])}")

# SVG ICONS
print("\n[SVG ICONS - 17 FICHIERS]")
print("-" * 90)
svg_icons = data.get("svg_icons", [])
for idx, svg in enumerate(svg_icons, 1):
    filename = svg.get("filename", "?")
    svg_type = svg.get("type", "")
    locations = svg.get("usage_locations", [])
    usage_count = len(locations)
    print(f"  {idx}. {filename} (Type: {svg_type}) - {usage_count} utilisation(s)")

# PNG ICONS
print("\n[PNG ICONS - 2 FICHIERS]")
print("-" * 90)
png_icons = data.get("png_icons", [])
for idx, png in enumerate(png_icons, 1):
    filename = png.get("filename", "?")
    png_type = png.get("type", "")
    locations = png.get("usage_locations", [])
    usage_count = len(locations)
    print(f"  {idx}. {filename} (Type: {png_type}) - {usage_count} utilisation(s)")

# CSS STYLES - DETAILS
print("\n[CLASSES CSS D'ICONES - 20 CLASSES]")
print("-" * 90)
styles = data.get("icon_styles_css", [])
all_properties = {}

for style in styles:
    class_name = style.get("class_name", "")
    properties = style.get("properties", {})
    files_using = style.get("files_using", [])
    
    print(f"\n  .{class_name}")
    
    # Afficher les proprietes
    if properties:
        for prop_name, prop_value in properties.items():
            if prop_value:
                print(f"    {prop_name}: {prop_value}")
    
    # Afficher les fichiers utilisant cette classe
    if files_using:
        print(f"    Fichiers: {', '.join(files_using[:2])}")

print("\n" + "=" * 90)
