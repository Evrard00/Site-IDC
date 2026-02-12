const fs = require('fs');
const path = require('path');

// Script de build pour copier les fichiers vers le dossier public
console.log('Building for Vercel...');

const srcDir = path.join(__dirname, 'src');
const assetsDir = path.join(__dirname, 'assets');
const publicDir = path.join(__dirname, 'public');

// Créer le dossier public s'il n'existe pas
if (!fs.existsSync(publicDir)) {
    fs.mkdirSync(publicDir, { recursive: true });
}

// Fonction récursive pour copier les répertoires
function copyDirRecursive(src, dest) {
    if (!fs.existsSync(dest)) {
        fs.mkdirSync(dest, { recursive: true });
    }
    
    const files = fs.readdirSync(src);
    files.forEach(file => {
        const srcPath = path.join(src, file);
        const destPath = path.join(dest, file);
        const stat = fs.statSync(srcPath);
        
        if (stat.isDirectory()) {
            copyDirRecursive(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
            console.log(`✓ Copied ${file}`);
        }
    });
}

// Copier et corriger les fichiers HTML de src/
const files = fs.readdirSync(srcDir);
files.forEach(file => {
    if (file.endsWith('.html')) {
        let content = fs.readFileSync(path.join(srcDir, file), 'utf8');
        
        // Remplacer les chemins relatifs des assets
        // ../assets/ → assets/
        content = content.replace(/\.\.\/assets\//g, 'assets/');
        
        // Écrire dans le dossier public
        fs.writeFileSync(path.join(publicDir, file), content);
        console.log(`✓ Processed HTML: ${file}`);
    }
});

// Copier les assets/
if (fs.existsSync(assetsDir)) {
    const publicAssetsDir = path.join(publicDir, 'assets');
    copyDirRecursive(assetsDir, publicAssetsDir);
    console.log('✓ Copied assets directory');
}

console.log('✓ Build completed!');


