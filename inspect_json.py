import json

# Lire le fichier JSON
with open(r"d:\Téléchargement\Site-IDC\AUDIT_ICONS_REPORT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Afficher les clés principales
print("Structure JSON principale:")
if isinstance(data, dict):
    print(f"  Clés principales: {list(data.keys())}")
    
    # Vérifier la structure des données
    for key in data.keys():
        if isinstance(data[key], list):
            print(f"\n  {key}: {len(data[key])} éléments")
            if data[key]:
                print(f"    Clés du premier élément: {list(data[key][0].keys()) if isinstance(data[key][0], dict) else 'N/A'}")
        elif isinstance(data[key], dict):
            print(f"\n  {key}: {list(data[key].keys())}")
        else:
            print(f"\n  {key}: {type(data[key]).__name__} - {str(data[key])[:100]}")

# Afficher un aperçu du contenu
print("\n\n" + "="*80)
print("APERÇU DU CONTENU:")
print("="*80)
print(json.dumps(data, indent=2, ensure_ascii=False)[:3000])
