# Site IDC — Ivoirienne d'Hydrocarbures

Site vitrine et e-shop d'IDC : carburants, gaz butane, lubrifiants, soute maritime,
carte TPE B2B et réseau de onze stations en Côte d'Ivoire.

HTML, CSS et JavaScript natifs. Aucun framework, aucune dépendance npm.

## Démarrer

```bash
npm run dev      # serveur local sur http://127.0.0.1:8000 (Python 3)
npm run build    # génère public/ pour la mise en ligne
```

`npm run dev` sert le dépôt tel quel : `http://127.0.0.1:8000/src/index.html` pour
le site en travail, `/public/index.html` pour la version construite. Le cache est
désactivé, un rafraîchissement suffit après une modification.

## Structure

```
Site-IDC/
├── src/
│   ├── _v2.css             # le système visuel — jetons, composants, interactions
│   ├── _app.css            # coquille de l'espace client (colonne + tableaux)
│   ├── _tete.js            # en-tête, menu mobile, envoi des formulaires
│   ├── _v2-ui.html         # page de composants, référence interne, non publiée
│   ├── index.html          # accueil
│   ├── tpe.html            # carte TPE
│   ├── eshop.html          # catalogue lubrifiants, panier, demande de devis
│   ├── contact.html · jobs.html · actualites.html · client.html
│   ├── login.html          # connexion (démonstration, voir plus bas)
│   ├── dashboard.html · purchases.html · cartes-tpe.html   # espace client
│   ├── cart-devis.html     # vue plein écran du panier de l'e-shop
│   └── 404.html
├── assets/images/          # seules les images référencées sont publiées
├── build.js                # génère public/
├── serve.py                # serveur de développement
├── robots.txt · sitemap.xml · favicon.ico
└── netlify.toml · vercel.json
```

Les fichiers préfixés d'un `_` sont partagés ou internes. `build.js` publie
`_v2.css`, `_app.css` et `_tete.js`, mais ignore tout `_*.html`.

## Le système visuel

Tout vit dans `src/_v2.css`. Les pages n'ont plus qu'un `<style>` pour ce qui leur
est propre — environ 500 lignes au total, contre 8 200 avant la refonte.

**Polices** — Bricolage Grotesque pour le texte et les titres, IBM Plex Mono pour
les micro-libellés en capitales. L'axe optique `opsz` de Bricolage est
indispensable : le retirer économise 35 Ko mais élargit les lettres au point de
faire déborder les titres.

**Couleurs** — déclarées comme variables en tête de `_v2.css`, chacune annotée de
son rapport de contraste. Ne jamais écrire une couleur en dur : les valeurs
d'état (`--ok`, `--err`) ont été extraites de huit pages où elles traînaient.

| Rôle | Variable | Valeur |
|---|---|---|
| Fond, surface | `--ground` `--surface` | `#ECEEE9` `#FFFFFF` |
| Encre | `--ink` `--ink-2` `--ink-3` | `#15171A` `#5A6058` `#656B63` |
| Vert IDC | `--green` `--green-lo` | `#1A7A39` `#6FD08C` |
| Orange IDC | `--orange` `--orange-t` `--orange-lo` | `#BC5810` `#AA500E` `#F0A05A` |
| Fond sombre | `--night` | `#14181B` |

**Points de rupture** — il n'y a pas de grille imposée : chaque composant bascule
là où son contenu l'exige. Les plus fréquents sont 1080, 900, 820 et 560 px.

## Règles tenues partout

Elles ont chacune coûté un défaut avant d'être écrites.

- **0 violation WCAG 2.2 AA + best-practice** sur les 13 pages publiées, mesuré
  avec axe-core. Une seule exception, documentée : les repères de la carte des
  stations passent sous le seuil de 2.5.8, et la liste qui l'accompagne offre la
  même fonction en cibles de 48 px atteignables au clavier.
- **Aucun texte sous 4,5:1.** Le contraste sur photo se mesure en échantillonnant
  le fond réel, pas à l'œil : le titre du héros était à 1,01:1.
- **Rien d'invisible au repos.** Les apparitions au défilement translatent, elles
  ne jouent jamais sur l'opacité.
- **`prefers-reduced-motion`** coupe les transitions, jamais les comportements.
- **L'élément focalisé n'est jamais masqué** par l'en-tête escamotable (2.4.11).
- **De 320 à 1440 px sans débordement horizontal.** Mesurer sur
  `document.body.scrollWidth`, pas sur `documentElement` : un conteneur qui défile
  gonfle le second sans que la page bouge.
- **Un `<dialog>` pour toute fenêtre modale** : piège de focus, Échap et fond
  inerte viennent gratuitement.

## Build

`node build.js` purge `public/`, réécrit les chemins d'assets relatifs, puis
**ne publie que ce qui sert** : les images jamais référencées et les dossiers
`assets/` orphelins sont écartés. La sortie fait environ 800 Ko pour 13 pages,
contre 17 Mo avant ce tri.

Netlify et Vercel exécutent la même commande. `NODE_VERSION` est fixé à 20 :
`build.js` emploie `fs.readdirSync({ recursive: true })`, apparu en 18.17, qu'une
version antérieure ignorerait en silence.

Pas de redirection attrape-tout : `404.html` est servi par l'hébergeur quand
aucun fichier ne correspond.

## Formulaires

Cinq formulaires passent par **Netlify Forms** — `contact`, `carte-tpe`,
`candidature`, `devis-eshop`, `newsletter`. Chacun déclare `data-netlify`, un
champ caché `form-name` et un pot de miel `bot-field`.

L'envoi est fait à la main par `window.idcEnvoyer()` dans `_tete.js`, la
validation et l'annonce passant déjà par du JavaScript. **En cas d'échec, le
message affiche une erreur exploitable, jamais un faux succès.**

En local, les envois échouent toujours : le serveur de développement ne sait pas
les recevoir. C'est le comportement attendu, testez depuis un déploiement.

Le formulaire de **connexion est volontairement exclu** : y brancher Netlify
Forms stockerait les mots de passe en clair.

## Reste à faire

**Avant la mise en production**

- [ ] Remplacer `https://www.idc.ci` par le domaine réel — `robots.txt`,
      `sitemap.xml`, les `canonical`, les balises `og:` et le JSON-LD.
- [ ] Remplacer l'authentification de démonstration : `login.html` contient deux
      comptes en clair et la session n'est vérifiée par aucun serveur.
- [ ] Activer les notifications Netlify Forms, sinon les demandes arrivent sans
      prévenir personne.
- [ ] Rédiger les pages légales — mentions, confidentialité, CGV — liées mais absentes.

**Contradictions à trancher** — les mêmes chiffres ne s'accordent pas d'une page
à l'autre :

- [ ] **Délai de réponse** : « 24/7 », « sous 48 heures » et « sous 24 heures
      ouvrées » coexistent.
- [ ] **Horaires** : l'accueil annonce « 24/7 » en héros et « lundi au vendredi,
      8 h à 16 h » en pied.
- [ ] **Clients** : 100 000+ sur l'accueil, 10 000+ sur l'espace client.
- [ ] **Réseaux sociaux** : les trois icônes mènent aux accueils de Facebook,
      LinkedIn et Instagram, pas aux comptes IDC.

**Confort**

- [ ] Quatre repères de carte placés sur leur localité, à confirmer : Bayota,
      Tarato, Dianra, Guézon. Les fiches n'ont ni adresse ni horaires.
- [ ] Treize boutons désactivés dans l'espace client (Rapports, Mon entreprise,
      Paramètres, Support) : les brancher ou les retirer.
- [ ] Quatorze fichiers du dépôt ne sont plus référencés — CSS hérité,
      `assets/js/`, `cart-devis.css` et `.js`. Ils ne sont plus publiés, mais
      encombrent encore.

## Outillage hérité

Les scripts Python à la racine (`convert_to_outline.py`, `remove_*.py`,
`sync_corrections.py`…) sont des correctifs ponctuels passés en masse sur
l'ancienne version du code. **Ils ont déjà été appliqués et ne correspondent plus
à la structure actuelle : les relancer casserait le site.** Conservés à titre
d'historique.
