# Système d'Icônes SVG - IDC

## 🎯 Vue d'ensemble

Le projet utilise maintenant les icônes SVG du dossier `material-icons-master` au lieu de dépendre de Google Fonts Material Symbols. Cela offre plusieurs avantages :

- ✅ **Indépendance** : Pas de dépendance externe à Google Fonts
- ✅ **Performance** : Icônes locales, chargement plus rapide
- ✅ **Personnalisation** : Possibilité de modifier les SVG si nécessaire
- ✅ **Fiabilité** : Pas de risques de changements d'API externe

## 📁 Structure des fichiers

```
assets/
├── icons/
│   └── svg/               # 31 fichiers SVG des icônes utilisées
│       ├── dashboard.svg
│       ├── settings.svg
│       ├── phone.svg
│       └── ... (29 autres)
├── css/
│   ├── icons.css          # Style de base (conservé)
│   └── icons-svg.css      # Nouveau : styles pour les SVG
└── js/
    └── icon-loader.js     # Nouveau : script de chargement des SVG
```

## 🔧 Comment ça fonctionne

### 1. **Structure HTML (inchangée)**
Les fichiers HTML gardent la même structure avec les Material Symbols :
```html
<span class="material-symbols-outlined icon-primary icon-m">phone</span>
```

### 2. **Chargement automatique (nouveau)**
Quand la page se charge, le script `icon-loader.js` :
- Détecte tous les éléments `.material-symbols-outlined`
- Charge les fichiers SVG correspondants
- Remplace les éléments Material Symbols par les SVG
- Préserve les classes CSS (tailles, couleurs, etc.)

### 3. **Styles CSS**
Le fichier `icons-svg.css` applique les styles aux SVG :
- Tailles : `.icon-xs` (12px), `.icon-s` (16px), `.icon-m` (24px), `.icon-l` (32px), `.icon-xl` (48px)
- Couleurs : `.icon-primary`, `.icon-secondary`, `.icon-dark`, `.icon-light`, `.icon-neutral`

## 📋 Icônes disponibles (31 total)

Les icônes suivantes ont été copiées du dossier `material-icons-master` :

- `build_circle`, `business`, `close`, `credit_card`, `dashboard`
- `delete`, `directions`, `done`, `exit_to_app`, `expand_less`
- `expand_more`, `facebook`, `grid_on`, `help_outline`, `local_shipping`
- `location_on`, `lock`, `mail`, `people`, `phone`
- `photo_camera`, `public`, `receipt_long`, `schedule`, `settings`
- `star`, `store`, `trending_up`, `visibility`, `warning`, `work`

⚠️ **Icônes manquantes** : `package`, `target` (non disponibles dans la source Material Icons)

## 🚀 Intégration HTML

Tous les fichiers HTML ont été automatiquement modifiés pour charger le support SVG :

1. **Dans le `<head>` :**
```html
<link rel="stylesheet" href="../assets/css/icons-svg.css">
```

2. **Avant la fermeture du `</body>` :**
```html
<script src="../assets/js/icon-loader.js"></script>
```

## 🔄 Ajouter une nouvelle icône

Si vous avez besoin d'ajouter une nouvelle icône :

1. **Chercher l'icône** dans le dossier `material-icons-master/material-icons-master/svg/`
2. **Copier le fichier SVG** vers `assets/icons/svg/`
3. **Utiliser dans le HTML** :
```html
<span class="material-symbols-outlined icon-primary">nom_de_l_icone</span>
```
4. Le script `icon-loader.js` la chargera automatiquement

## 📊 Performance

### Avant (Google Fonts)
- Police Material Symbols chargée depuis CDN Google
- ~30KB de données (selon les icônes utilisées)
- Dépendance externe

### Après (SVG local)
- 31 fichiers SVG locaux (~2-5KB chacun, optimisés)
- Aucune dépendance externe
- Chargement asynchrone et cache local

## 🛠️ Maintenance

### Mettre à jour le système Material Icons
```bash
# Mettre à jour le dossier material-icons-master si nécessaire
python setup_icons.py          # Extraire les icônes utilisées
python integrate_svg_icons.py  # Intégrer dans les HTML
```

## ❓ Dépannage

### Les icônes ne s'affichent pas
1. Vérifier que `assets/css/icons-svg.css` existe
2. Vérifier que `assets/js/icon-loader.js` existe
3. Vérifier que `assets/icons/svg/` contient les fichiers SVG
4. Ouvrir la console du navigateur (F12) pour voir les erreurs

### Une icône spécifique manque
1. Vérifier si elle existe dans `material-icons-master/material-icons-master/svg/nom_de_l_icone/`
2. Si elle existe, la copier manuellement vers `assets/icons/svg/`
3. Si elle n'existe pas, chercher une alternative similaire

## 📝 Fichiers modifiés

- ✅ Créé : `assets/icons/svg/*.svg` (31 fichiers)
- ✅ Créé : `assets/css/icons-svg.css`
- ✅ Créé : `assets/js/icon-loader.js`
- ✅ Modifié : Tous les fichiers HTML

## 🔗 Ressources

- Material Icons source : `material-icons-master/`
- Documentation Material Icons : https://github.com/material-icons/material-icons
