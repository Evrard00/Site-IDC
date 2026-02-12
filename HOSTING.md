# Configuration pour différents hébergeurs

## Netlify
- Créé : `netlify.toml` ✓
- Configure automatiquement le build et le dossier public

## Vercel  
- Créé : `vercel.json` ✓
- Configure le dossier public comme output

## GitHub Pages
- Créé : `.github/workflows/deploy.yml` (optionnel)

## Général (tous les hébergeurs statiques)
1. Assurez-vous que le build s'exécute avec : `node build.js`
2. Le site est servi depuis le dossier `public/`
3. Les fichiers HTML avec les assets corrigés y sont contenus
