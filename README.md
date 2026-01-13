# Refonte du Site IDC

## 📋 Description
Projet de refonte complète du site internet IDC avec un design responsive, optimisé pour tous les types d'écrans et orienté vers la conversion B2B.

## 🎯 Objectifs
- ✅ Responsive design (mobile-first)
- ✅ Site corporate + e-shop intégré
- ✅ Optimisé pour la conversion B2B (demandes de devis, carte TPE)
- ✅ SEO-friendly (pages dédiées par activité/produit)
- ✅ Performance et accessibilité

## 📁 Structure du projet

```
Site-IDC/
├── src/                              # Code source du site
│   ├── index.html                   # Accueil
│   ├── pages/                       # Pages informatives
│   │   ├── qui-sommes-nous.html
│   │   ├── carriere.html
│   │   ├── contact.html
│   │   └── devis.html
│   ├── activites/                   # Pages des activités
│   │   ├── index.html
│   │   ├── carburants.html
│   │   ├── gaz.html
│   │   ├── lubrifiants.html
│   │   ├── carte-tpe.html
│   │   └── stations.html
│   └── boutique/                    # E-shop
│       ├── index.html
│       ├── categories/
│       └── produits/
├── assets/                          # Ressources
│   ├── css/
│   │   ├── reset.css               # Normalisation
│   │   ├── variables.css           # Variables CSS
│   │   └── styles.css              # Styles principaux
│   ├── js/
│   │   └── main.js                 # JavaScript interactif
│   └── images/                      # Images du site
├── docs/                            # Documentation
│   ├── SITEMAP.md                  # Sitemap détaillé
│   ├── SPECIFICATIONS.md           # Spécifications
│   └── CHANGELOG.md                # Changelog
├── README.md                        # Ce fichier
├── package.json                     # Dépendances
└── .gitignore                      # Fichiers à ignorer
```

## 🚀 Responsive Design

### Breakpoints
- **Mobile** : < 576px
- **Tablette** : 576px - 768px  
- **Petit écran** : 768px - 992px
- **Standard** : 992px - 1200px
- **Grand écran** : > 1200px

### Approche
- Mobile-first
- CSS Grid et Flexbox pour les layouts
- Variables CSS pour la cohérence
- Menu hamburger adaptatif

## 🎨 Technologies

- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **Responsive** : Media queries, CSS Grid, Flexbox
- **Variables** : CSS custom properties
- **Outils** : VS Code avec Prettier

## 📱 Pages créées

### Pages principales ✅
- Accueil (hero, activités, chiffres, témoignages)
- Qui sommes-nous (présentation, histoire, valeurs)
- Nos activités (index + 5 pages détaillées)
  - Carburants
  - Gaz Butane
  - Lubrifiants
  - Carte TPE B2B
  - Stations & Services
- Boutique (accueil e-shop)
- Carrière (offres d'emploi, candidature)
- Contact (formulaires, infos, carte)
- Demande de devis (formulaire B2B)

### Pages à créer 📝
- Mentions légales
- Politique de confidentialité
- CGV
- Catégories e-shop (Lubrifiants, Accessoires, Gaz)
- Fiches produits
- Panier et paiement

## 🎯 Points clés UX/SEO

### CTA Visibles
- Chaque page a un appel à l'action clair
- Priorité conversion B2B (demande de devis, carte TPE)
- Boutons primaires et secondaires bien différenciés

### Navigation
- ✅ Menu responsive (hamburger sur mobile)
- ✅ Header sticky
- ✅ Footer global avec liens vers toutes les pages

### SEO
- ✅ Chaque activité/produit = page dédiée
- ✅ Meta descriptions pour chaque page
- ✅ Hiérarchie de titres correcte (H1, H2, H3)
- ✅ URLs SEO-friendly

## 🎨 Design System

### Couleurs
- **Primaire** : #0066cc (bleu)
- **Secondaire** : #ff6600 (orange)
- **Texte** : #333333
- **Fond clair** : #f5f5f5
- **Bordures** : #e0e0e0

### Typographie
- **Police** : System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, etc.)
- **Tailles** : Fluides (clamp) du mobile au desktop

### Espacement
- Système cohérent en variables CSS (spacing-xs à spacing-2xl)
- Basé sur 8px unit

## 📦 Installation & Utilisation

### Prérequis
- Navigateur moderne
- Éditeur de code (VS Code recommandé)

### Lancer le site
1. Ouvrir `src/index.html` dans un navigateur
2. Ou utiliser un serveur local (Live Server VS Code)

## 📝 À compléter

- [ ] Ajouter les contenus spécifiques (textes, images)
- [ ] Intégrer Google Maps (cartes interactives)
- [ ] Développer l'e-commerce (panier, paiement)
- [ ] Créer les pages légales
- [ ] Optimiser les images
- [ ] Ajouter Google Analytics
- [ ] Créer sitemap XML et robots.txt

## 📚 Documentation

Voir `/docs/` pour plus de détails :
- [SITEMAP.md](docs/SITEMAP.md) - Structure complète du site
- [SPECIFICATIONS.md](docs/SPECIFICATIONS.md) - Spécifications détaillées
- [CHANGELOG.md](docs/CHANGELOG.md) - Historique des versions

## 👥 Équipe

_À compléter avec les informations de l'équipe_

## 📞 Support

Pour toute question, contactez [email ou contact]

---

**Dernière mise à jour** : 13 janvier 2026  
**Version** : 2.0.0 (En cours)
