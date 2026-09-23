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
├── index.html              # redirection de confort vers src/, jamais publiée
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
- **De 320 à 2560 px sans défilement horizontal**, vérifié par un saut réel :
  `window.scrollTo({ left: 9999, behavior: 'instant' })` puis lecture de
  `scrollX`. Le `scroll-behavior: smooth` posé sur `html` rend `scrollTo()`
  animé — lire `scrollX` juste après renvoie l'ancienne valeur et fait conclure
  à tort qu'aucune page ne déborde. C'est ainsi qu'un pied de page débordant
  sur les treize pages est passé inaperçu.
- **Aucune grille en `1fr` qui puisse tomber sous son contenu.** Une colonne
  `1fr` ne descend pas sous sa largeur de min-content : les quatre colonnes du
  pied restaient à 531 px et sortaient de l'écran entre 431 et 530 px. Soit
  `minmax(0, 1fr)`, soit un palier qui réduit le nombre de colonnes.
- **Un `<dialog>` pour toute fenêtre modale** : piège de focus, Échap et fond
  inerte viennent gratuitement. **Ne jamais poser `display` en dehors de l'état
  ouvert** : cela annule la règle `dialog:not([open]) { display: none }` du
  navigateur. Le panneau reste alors dans le flux — garé hors écran, ou masqué
  par le seul `opacity: 0` d'une requête de mouvement, donc pleinement visible
  sous `prefers-reduced-motion` — et ses commandes restent dans l'ordre de
  tabulation. L'e-shop en comptait seize, invisibles et pourtant atteignables.

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

### Empreinte et cache

Chaque image publiée reçoit une **empreinte de son contenu** dans son nom —
`hero.webp` devient `hero.4943194d.webp`, et les pages sont écrites en dernier
pour porter la nouvelle adresse. Une image modifiée change donc d'adresse.

C'est la condition de la politique de cache :

| Ce qui est servi | Cache-Control | Pourquoi |
|---|---|---|
| `/assets/*` | `max-age=31536000, immutable` | le nom change avec le contenu |
| tout le reste | `max-age=0, must-revalidate` | servi après un 304, jamais sans demander |

**Ne jamais déclarer un cache long sans empreinte.** C'est exactement ce qui
était en place : un an sur `/assets/*` avec des noms fixes, et une heure sèche
sur `/*.html`. Une image remplacée sous le même nom restait un an chez qui
l'avait déjà vue, une page une heure — tandis que le CSS, lui, n'avait aucune
règle et se mettait à jour aussitôt. Les déploiements paraissaient n'arriver
qu'à moitié.

La règle `/*.html` avait un second défaut : elle ne s'appliquait qu'aux
adresses finissant par `.html`. Avec les URL propres, `/eshop` y échappait et
`/eshop.html` non : deux visiteurs de la même page pouvaient voir deux
versions.

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

## Ce qui a été retiré

Le dépôt portait **11 059 fichiers sans emploi**, dont `material-icons-master/`
— une bibliothèque d'icônes extraite en double, 10 960 fichiers, que plus aucune
page ne chargeait. Sont partis avec elle les feuilles de style héritées
(`assets/css/`), les icônes en fichiers remplacées par des tracés SVG en ligne
(`assets/icons/`), les scripts de l'ancien site (`assets/js/`), deux composants
React dans un site sans framework (`src/components/`), une vingtaine de
correctifs Python passés une fois en masse, les rapports d'un audit d'icônes
sans objet, et `build.sh` — un script d'avant `build.js` qui copiait `src/*.html`
à la racine du dépôt.

`cart-devis.css` et `cart-devis.js` sont partis aussi : la page ne les chargeait
plus depuis la refonte, mais `build.js` les publiait encore.

Tout cela reste dans l'historique git et se récupère par `git show`.

**Ce qui a été gardé** : les originaux des images publiées — `gaz.png`,
`station.jpg`, `tpe.jpg`, `cab.jpg`, `lub.jpg`, `soute.jpg`, `logo.png`. Ce sont
les fichiers sources à réexporter quand il faut une autre taille ou un autre
cadrage. `build.js` ne les publie pas.

Quelques scripts Python non suivis par git subsistent à la racine
(`convert_to_outline.py`, `remove_*.py`, `replace_with_outline.py`,
`sync_corrections.py`) ainsi que `CART_DEVIS_README.md`. Ce sont des correctifs
ponctuels déjà appliqués à l'ancienne structure : **les relancer casserait le
site.** N'étant pas dans git, ils ne sont récupérables nulle part — d'où leur
maintien en place.
