const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// Script de build : génère le dossier public/ servi par Vercel / Netlify
console.log('Building for production...');

const rootDir = __dirname;
const srcDir = path.join(rootDir, 'src');
const assetsDir = path.join(rootDir, 'assets');
const publicDir = path.join(rootDir, 'public');

// Fichiers statiques présents à la racine du dépôt et attendus à la racine du site
const ROOT_FILES = ['robots.txt', 'sitemap.xml', 'favicon.ico'];

// Purge du dossier de sortie.
// Sans cette étape, une page supprimée de src/ restait en ligne indéfiniment
// (about.html, services.html et news.html ont ainsi survécu à plusieurs déploiements).
if (fs.existsSync(publicDir)) {
    fs.rmSync(publicDir, { recursive: true, force: true });
    console.log('✓ Cleaned public/');
}
fs.mkdirSync(publicDir, { recursive: true });

// Copie récursive d'un répertoire
function copyDirRecursive(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        if (entry.isDirectory()) {
            copyDirRecursive(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

// Pages HTML : src/*.html → public/*.html, chemins d'assets réécrits
let pageCount = 0;
const sorties = [];   // ce qui est publié, pour savoir ensuite quelles images servent
const pages = [];     // écrites en dernier : elles doivent porter les noms empreints
const empreintes = new Map();   // nom d'origine -> nom empreint
for (const file of fs.readdirSync(srcDir)) {
    const srcPath = path.join(srcDir, file);
    if (!fs.statSync(srcPath).isFile()) continue;

    // Les fichiers préfixés d'un « _ » sont des références internes
    // (page de composants du design system) : pas des pages du site.
    if (file.startsWith('_') && file.endsWith('.html')) continue;

    if (file.endsWith('.html')) {
        let content = fs.readFileSync(srcPath, 'utf8');

        // En production les pages sont à la racine : ../assets/ et ../../assets/
        // doivent tous deux devenir assets/.
        content = content.replace(/\.\.\/\.\.\/assets\//g, 'assets/');
        content = content.replace(/\.\.\/assets\//g, 'assets/');

        pages.push({ file, content });
        sorties.push(content);
        pageCount++;
    } else {
        // CSS/JS propres à une page (ex. _v2.css, _app.css)
        fs.copyFileSync(srcPath, path.join(publicDir, file));
        if (/\.(css|js)$/.test(file)) sorties.push(fs.readFileSync(srcPath, 'utf8'));
    }
}
console.log(`✓ ${pageCount} pages HTML traitées`);

// Ressources partagées.
// assets/images/ pèse 16 Mo dont 15 que plus aucune page ne charge : les
// grandes photos de héros écartées et les icônes matricielles remplacées par
// des tracés SVG en ligne. On ne publie que ce qui est réellement référencé ;
// les fichiers restent dans le dépôt, ils ne partent simplement plus en ligne.
if (fs.existsSync(assetsDir)) {
    const imagesDir = path.join(assetsDir, 'images');
    const referencees = new Set();
    for (const texte of sorties) {
        for (const m of texte.matchAll(/assets\/images\/([\w.\-]+)/g)) referencees.add(m[1]);
    }

    // Les feuilles et scripts hérités (assets/css, assets/js, assets/html) ne
    // sont plus chargés par aucune page depuis la refonte : le style vit dans
    // src/_v2.css et src/_app.css. On les laisse dans le dépôt sans les publier.
    const ecartes = [];
    for (const entry of fs.readdirSync(assetsDir, { withFileTypes: true })) {
        const from = path.join(assetsDir, entry.name);
        const to = path.join(publicDir, 'assets', entry.name);
        if (entry.name === 'images' && entry.isDirectory()) continue;

        if (entry.isDirectory()) {
            const fichiers = fs.readdirSync(from, { recursive: true, withFileTypes: true })
                .filter((f) => f.isFile()).map((f) => f.name);
            const sert = fichiers.some((nom) => sorties.some((t) => t.includes(nom)));
            if (fichiers.length && !sert) { ecartes.push(entry.name); continue; }
            copyDirRecursive(from, to);
        } else {
            fs.mkdirSync(path.dirname(to), { recursive: true });
            fs.copyFileSync(from, to);
        }
    }
    if (ecartes.length) console.log(`  · dossiers non référencés écartés : ${ecartes.join(', ')}`);

    if (fs.existsSync(imagesDir)) {
        const dest = path.join(publicDir, 'assets', 'images');
        fs.mkdirSync(dest, { recursive: true });
        let gardees = 0, ecartees = 0, octetsEcartes = 0;
        for (const entry of fs.readdirSync(imagesDir, { withFileTypes: true })) {
            const from = path.join(imagesDir, entry.name);
            if (entry.isDirectory()) { copyDirRecursive(from, path.join(dest, entry.name)); continue; }
            if (referencees.has(entry.name)) {
                // Empreinte de contenu. Sans elle, une image remplacée sous le
                // même nom garde son adresse : le cache d'un an déclaré dans
                // netlify.toml la sert encore un an. Un nom qui change à chaque
                // modification rend ce cache sûr — et immédiat.
                const donnees = fs.readFileSync(from);
                const ext = path.extname(entry.name);
                const nom = path.basename(entry.name, ext) + '.'
                          + crypto.createHash('sha256').update(donnees).digest('hex').slice(0, 8) + ext;
                fs.writeFileSync(path.join(dest, nom), donnees);
                empreintes.set(entry.name, nom);
                gardees++;
            } else {
                octetsEcartes += fs.statSync(from).size;
                ecartees++;
            }
        }
        console.log(`✓ assets/ copié — ${gardees} images publiées, ` +
                    `${ecartees} non référencées écartées (${(octetsEcartes / 1048576).toFixed(1)} Mo)`);
    } else {
        console.log('✓ assets/ copié');
    }
}

// Les pages partent maintenant, avec les adresses d'images empreintes.
// Remplacement littéral plutôt qu'expression régulière : pas d'échappement à
// tenir. Les noms les plus longs d'abord, au cas où l'un serait le préfixe
// d'un autre (« hero.webp » dans « hero.webp.map »).
const parLongueur = [...empreintes].sort((a, b) => b[0].length - a[0].length);
for (const { file, content } of pages) {
    let sortie = content;
    for (const [avant, apres] of parLongueur) {
        sortie = sortie.split('assets/images/' + avant).join('assets/images/' + apres);
    }
    fs.writeFileSync(path.join(publicDir, file), sortie);
}
if (empreintes.size) console.log(`\u2713 ${empreintes.size} images empreintes`);

// Fichiers racine (référencement, favicon)
for (const file of ROOT_FILES) {
    const from = path.join(rootDir, file);
    if (fs.existsSync(from)) {
        fs.copyFileSync(from, path.join(publicDir, file));
        console.log(`✓ ${file}`);
    } else {
        console.warn(`! ${file} absent — ignoré`);
    }
}

console.log('✓ Build terminé.');
