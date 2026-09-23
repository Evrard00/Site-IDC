#!/usr/bin/env python3
"""
Sync important corrections from src/ to public/ for key files.
This ensures all HTML files have the fixes applied.
"""

import shutil
from pathlib import Path

def sync_files():
    workspace_root = Path('d:\\Téléchargement\\Site-IDC')
    
    # Files to sync
    files_to_sync = [
        'index.html',
        'login.html',
    ]
    
    print("📋 Syncing corrections from src/ to public/...\n")
    
    for filename in files_to_sync:
        src_file = workspace_root / 'src' / filename
        pub_file = workspace_root / 'public' / filename
        
        if src_file.exists():
            shutil.copy(src_file, pub_file)
            print(f"  ✓ {filename} synced")
        else:
            print(f"  ✗ {filename} not found in src/")
    
    print("\n✅ Sync complete!\n")

if __name__ == '__main__':
    sync_files()
