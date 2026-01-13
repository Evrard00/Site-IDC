# ⚡ Quick Start - Refonte Site IDC

## 🚀 Démarrer en 5 minutes

### 1. Ouvrir le site
**Option A : Navigateur direct**
- Ouvrir : `src/index.html` dans votre navigateur

**Option B : Serveur local (recommandé)**
- VS Code → Extensions → Live Server
- Clic droit sur `src/index.html` → "Open with Live Server"

### 2. Explorer la structure
```
src/
├── index.html          ← Page d'accueil
├── pages/              ← Pages infos
│   ├── qui-sommes-nous.html
│   ├── carriere.html
│   ├── contact.html
│   └── devis.html
├── activites/          ← 5 pages produits
│   ├── carburants.html
│   ├── gaz.html
│   ├── lubrifiants.html
│   ├── carte-tpe.html
│   └── stations.html
└── boutique/           ← E-shop
    └── index.html
```

### 3. Personnaliser rapidement

#### Changer les couleurs
Fichier : `assets/css/variables.css`
```css
:root {
    --primary-color: #0066cc;    ← Changer cette couleur
    --secondary-color: #ff6600;  ← Et celle-ci
}
```

#### Ajouter du contenu
Ouvrir n'importe quelle page et modifier les sections "À compléter"

#### Ajouter une nouvelle page
1. Copier `_template.html`
2. Renommer le fichier
3. Modifier le contenu
4. Ajouter le lien dans le menu navigation

### 4. Vérifier le responsive
- **Desktop** : F12 → Toggle device toolbar → Desktop
- **Mobile** : F12 → Toggle device toolbar → iPhone 12
- **Tablette** : F12 → Toggle device toolbar → iPad

---

## 📋 Fichiers clés à connaître

| Fichier | Rôle |
|---------|------|
| `src/index.html` | Accueil du site |
| `assets/css/variables.css` | Couleurs, espacements, breakpoints |
| `assets/css/styles.css` | Tous les styles responsifs |
| `assets/js/main.js` | Menu hamburger et interactions |
| `docs/SITEMAP.md` | Structure complète du site |
| `docs/CHECKLIST.md` | Plan d'exécution détaillé |

---

## 🎯 Tâches prioritaires

### Première semaine
```
[ ] Remplir contenu accueil
[ ] Ajouter images hero
[ ] Compléter pages activités
[ ] Ajouter chiffres clés réels
[ ] Remplir contacts réels
```

### Deuxième semaine
```
[ ] Créer pages légales
[ ] Intégrer Google Maps
[ ] Configurer formulaires email
[ ] Optimiser images
```

---

## 🐛 Troubleshooting

**Les images n'apparaissent pas ?**
- Vérifier chemins des images (relatif ou absolu)
- Utiliser `/assets/images/nomimage.jpg`

**Le menu hamburger ne fonctionne pas ?**
- Vérifier JavaScript activé
- Vérifier console (F12) pour erreurs

**Responsive ne marche pas ?**
- Vérifier `<meta name="viewport" ...>` présent
- Tester avec F12 Toggle device toolbar

---

## 📚 Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** ← Vous êtes ici
- **[SITEMAP.md](SITEMAP.md)** - Structure détaillée
- **[CHECKLIST.md](CHECKLIST.md)** - Plan complet
- **[README.md](../README.md)** - Guide général

---

## 💬 Questions ?

Voir [docs/](../) pour la documentation complète !

**Bon développement ! 🚀**
