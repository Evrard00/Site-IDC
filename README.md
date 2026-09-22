# Site IDC — Ivoirienne d'Hydrocarbures

Site vitrine et e-shop d'IDC : carburants, gaz butane, lubrifiants, carte TPE B2B
et réseau de stations-service en Côte d'Ivoire.

HTML / CSS / JavaScript natifs, sans framework ni dépendance npm.

## Démarrer

```bash
npm run dev      # serveur local sur http://127.0.0.1:8000 (Python 3)
npm run build    # génère public/ pour la mise en ligne
```

`npm run dev` sert le dépôt tel quel : la racine redirige vers `/src/index.html`.
Le cache est désactivé, un simple rafraîchissement suffit après une modification.

## Structure

```
Site-IDC/
├── src/                    # les 12 pages du site
│   ├── index.html          # accueil
│   ├── tpe.html            # carte TPE (présentation + demande)
│   ├── eshop.html          # boutique lubrifiants
│   ├── contact.html        # formulaire de contact
│   ├── jobs.html           # offres et candidatures
│   ├── actualites.html     # actualités
│   ├── login.html          # connexion espace client
│   ├── client.html         # accueil espace client
│   ├── dashboard.html      # tableau de bord client
│   ├── purchases.html      # historique d'achats
│   ├── cartes-tpe.html     # gestion des cartes TPE
│   ├── cart-devis.html     # panier / demande de devis
│   └── components/         # variante React du panier (non intégrée)
├── assets/
│   ├── css/                # feuilles partagées (voir ci-dessous)
│   ├── js/                 # footer-loader.js, main.js, icon-loader.js
│   ├── html/footer.html    # pied de page commun, injecté en JS
│   ├── images/             # visuels et icônes SVG
│   ├── icons/svg/          # 35 icônes SVG (non utilisées actuellement)
│   └── pdfs/
├── public/                 # sortie du build — régénéré, jamais édité à la main
├── build.js                # script de build
├── serve.py                # serveur de développement
├── robots.txt / sitemap.xml / favicon.ico
└── netlify.toml / vercel.json
```

### Feuilles de style

| Fichier | Rôle |
|---|---|
| `shared.css` | en-tête, pied de page, lien d'évitement, dimensionnement des icônes — chargé par 11 pages sur 12 |
| `reset.css`, `variables.css`, `styles.css` | socle, chargé par `index.html` |
| `theme-idc.css`, `placeholders.css` | thème et blocs de remplacement |
| `icons.css`, `icons-svg.css` | **inutilisées** — plus aucune classe employée, plus chargées |

L'essentiel du CSS vit encore dans des balises `<style>` au sein de chaque page.
Extraire l'en-tête et le pied de page vers `shared.css` reste le principal
chantier de maintenabilité.

## Déploiement

Les deux hébergeurs exécutent `node build.js` et publient `public/` :

- **Netlify** — `netlify.toml`
- **Vercel** — `vercel.json`

Le build purge `public/` à chaque exécution, réécrit les chemins d'assets
relatifs et copie `robots.txt`, `sitemap.xml` et `favicon.ico` à la racine.

## À faire avant la mise en production

- [ ] **Remplacer `https://www.idc.ci`** par le domaine réel dans `robots.txt`,
      `sitemap.xml` et les balises `canonical` / `og:` des 12 pages.
- [ ] **Relier les formulaires à un back-end.** Devis TPE, contact et
      candidatures sont aujourd'hui enregistrés dans le `localStorage` du
      visiteur : aucune demande n'est transmise à IDC.
- [ ] **Remplacer l'authentification de démonstration.** `login.html` contient
      des identifiants en clair et la session n'est pas vérifiée côté serveur.
- [ ] Vérifier les coordonnées de contact, aujourd'hui fictives.
- [ ] Rédiger les pages légales (mentions, confidentialité, CGV), liées mais absentes.

## Repères techniques

- **Points de rupture** : 480, 768, 1024, 1200 px.
- **Couleurs** : vert `#1b7d3a`, orange `#E36A13`, texte `#4F4F4F`, fond `#E8E8E5`.
- **Polices** : Poppins (titres), Inter (texte).
- **Images** : dimensionnées à leur taille d'affichage, JPEG progressif ;
  `loading="lazy"` hors du premier écran.

## Outillage

Les scripts Python à la racine (`fix_*.py`, `audit_*.py`, `remove_*.py`…) sont des
correctifs ponctuels passés en masse sur le code. **Ils ont déjà été appliqués :
les relancer recasserait le site.** Ils sont conservés à titre d'historique.
