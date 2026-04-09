"""
Générer une liste complète de tous les icônes disponibles et utilisés
"""

import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent
SVG_DIR = PROJECT_ROOT / "assets" / "icons" / "svg"

# Récupérer les icônes SVG disponibles
available_icons = sorted([f.stem for f in SVG_DIR.glob("*.svg")])

# Récupérer les icônes utilisées dans le HTML
used_icons = set()
for html_file in PROJECT_ROOT.glob("src/*.html"):
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        # Chercher les icônes dentro des class="material-symbols-outlined"
        matches = re.findall(r'>([a-z_]+)<\/span><\/span>', content)
        used_icons.update(matches)
    except:
        pass

# Fusionner et dédupliquer
all_icons = sorted(set(available_icons + list(used_icons)))
missing_icons = sorted(set(used_icons) - set(available_icons))

print("=" * 80)
print("📊 LISTE COMPLÈTE DES ICÔNES - SITE IDC")
print("=" * 80)

print(f"\n✅ ICÔNES DISPONIBLES ({len(available_icons)} total):\n")
print("┌─ NAVIGATIONS & CONTRÔLE")
nav_icons = ['dashboard', 'expand_more', 'expand_less', 'close', 'exit_to_app', 'help_outline']
for icon in nav_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

print("\n┌─ STATUT & VALIDATION")
status_icons = ['done', 'warning', 'visibility', 'schedule', 'delete']
for icon in status_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

print("\n┌─ FINANCIER & PAIEMENT")
financial_icons = ['credit_card', 'receipt_long', 'trending_up']
for icon in financial_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

print("\n┌─ SOCIAL & COMMUNICATION")
social_icons = ['phone', 'mail', 'facebook', 'photo_camera']
for icon in social_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

print("\n┌─ MÉTIER & AFFAIRES")
business_icons = ['business', 'work', 'store', 'local_shipping', 'directions', 'build_circle', 'grid_on', 'lock', 'public', 'people']
for icon in business_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

print("\n┌─ AUTRES")
other_icons = ['star', 'settings']
for icon in other_icons:
    if icon in available_icons:
        print(f"  ✓ {icon}")

if missing_icons:
    print(f"\n\n⚠️  ICÔNES MANQUANTES ({len(missing_icons)} total):")
    print("Ces icônes sont utilisées dans le HTML mais pas encore intégrées:\n")
    for icon in missing_icons:
        print(f"  ✗ {icon}")

print("\n\n" + "=" * 80)
print(f"📈 RÉSUMÉ:")
print(f"   • Icônes disponibles: {len(available_icons)}")
print(f"   • Icônes utilisées: {len(used_icons)}")
print(f"   • Icônes manquantes: {len(missing_icons)}")
print("=" * 80)
