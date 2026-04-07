#!/usr/bin/env python3
import os
import re

# Définir les remplacements d'émojis
emoji_replacements = {
    '📊': '<img src="../assets/images/icon-grid.svg" alt="" />',
    '📋': '<img src="../assets/images/icon-list.svg" alt="" />',
    '💳': '<img src="../assets/images/icon-credit-card.svg" alt="" />',
    '📈': '<img src="../assets/images/icon-trending-up.svg" alt="" />',
    '🏢': '<img src="../assets/images/icon-briefcase.svg" alt="" />',
    '⚙️': '<img src="../assets/images/icon-settings.svg" alt="" />',
    '📞': '<img src="../assets/images/icon-phone.svg" alt="" />',
    '🚪': '<img src="../assets/images/icon-door.svg" alt="" />',
    '✓': '<img src="../assets/images/icon-check.svg" alt="" />',
    '📧': '<img src="../assets/images/icon-email.svg" alt="" />',
    '👤': '<img src="../assets/images/icon-users.svg" alt="" />',
    '💬': '<img src="../assets/images/icon-chat.svg" alt="" />',
    '👁️': '<img src="../assets/images/icon-eye.svg" alt="" />',
    '🎯': '<img src="../assets/images/icon-target.svg" alt="" />',
    '⭐': '<img src="../assets/images/icon-star.svg" alt="" />'
}

# Fichiers cibles
files_to_process = [
    'src/dashboard.html',
    'src/purchases.html', 
    'src/cartes-tpe.html',
    'src/tpe.html',
    'src/eshop.html',
    'src/jobs.html',
    'assets/html/footer.html'
]

# Traiter chaque fichier
for filepath in files_to_process:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer chaque émoji
    for emoji, replacement in emoji_replacements.items():
        content = content.replace(emoji, replacement)
    
    # Écrire le fichier si modifié
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Processed: {filepath}")
    else:
        print(f"- No changes: {filepath}")

print("\n✓ All emoji replacements completed!")
