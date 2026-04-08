import json
import re
from collections import defaultdict, Counter

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Structures pour collecter les données
emojis_locations = defaultdict(list)
font_sizes = Counter()
colors = Counter()

# Parcourir toutes les sections du rapport
if isinstance(data, dict):
    sections = data.get("sections", [])
    issues = data.get("issues", [])
    
    # Traiter les sections
    for section in sections:
        icons = section.get("icons", [])
        for icon in icons:
            # Emojis
            text = str(icon.get("character", "")) + str(icon.get("name", ""))
            location = section.get("location", "Unknown")
            
            # Tailles
            size = icon.get("fontSize", "")
            if size:
                font_sizes[str(size)] += 1
            
            # Couleurs
            color = icon.get("color", "")
            if color:
                colors[str(color)] += 1

print("=" * 80)
print("RAPPORT D'AUDIT DES ICÔNES - RÉSUMÉ DÉTAILLÉ")
print("=" * 80)

# Afficher les statistics brutes
print(f"\nTotal de sections: {len(sections)}")
print(f"Total d'issues: {len(issues)}")

# 1. TAILLES UTILISÉES
print("\n" + "=" * 80)
print(" TAILLES D'ICÔNES (font-size) UTILISÉES:")
print("-" * 80)
if font_sizes:
    for size, count in sorted(font_sizes.items(), key=lambda x: x[1], reverse=True):
        print(f"  {size}: {count} utilisation(s)")
else:
    print("  Vérification en cours...")

# 2. COULEURS
print("\n" + "=" * 80)
print(" COULEURS UTILISÉES:")
print("-" * 80)
if colors:
    unique_colors = list(colors.items())
    for color, count in unique_colors[:20]:
        print(f"  {color}: {count} utilisation(s)")
    if len(unique_colors) > 20:
        print(f"  ... et {len(unique_colors) - 20} autres couleurs")
else:
    print("  Vérification en cours...")

# 3. ISSUES FROM REPORT
print("\n" + "=" * 80)
print("  PROBLÈMES IDENTIFIÉS:")
print("-" * 80)
if issues:
    categories = defaultdict(list)
    for issue in issues:
        category = issue.get("category", "Other")
        severity = issue.get("severity", "")
        message = issue.get("message", "")
        categories[category].append((severity, message))
    
    for cat in sorted(categories.keys()):
        print(f"\n  {cat}:")
        for severity, msg in categories[cat][:5]:
            prefix = "🔴" if severity == "error" else "🟡" if severity == "warning" else "🔵"
            print(f"    {prefix} {msg}")

# 4. RECOMMENDATIONS
print("\n" + "=" * 80)
print("✅ RECOMMENDATIONS POUR L'UNIFORMISATION:")
print("-" * 80)

recommendations = [
    "  • Standardiser les tailles d'icônes actives",
    "  • Définir une palette de couleurs cohérente",
    "  • Utiliser une nomenclature homogène pour nommer les icônes",
    "  • Documenter les standards visuels et techniques",
    "  • Créer une librairie d'icônes réutilisables",
    "  • Implémenter des tests visuels de régression"
]

for rec in recommendations:
    print(rec)

print("\n" + "=" * 80)
print("FIN DU RAPPORT")
print("=" * 80)
