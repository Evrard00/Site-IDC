#!/bin/bash

# Script de build pour Vercel
# Copie tous les fichiers du dossier src/ vers la racine pour servir en static

echo "Building for production..."

# Créer les répertoires
mkdir -p public

# Copier les fichiers HTML du dossier src vers la racine
cp src/*.html ./
cp src/*.html public/

# Vérifier la structure
echo "✓ Build completed"
echo "Files in root:"
ls -la *.html

exit 0
