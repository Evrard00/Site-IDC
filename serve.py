#!/usr/bin/env python3
"""
Serveur de développement pour le site IDC avec cache désactivé
"""

import http.server
import socketserver
import os

PORT = 8001
BIND_ADDRESS = '127.0.0.1'

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Gestionnaire HTTP sans cache"""
    
    def end_headers(self):
        """Ajouter les headers pour désactiver le cache"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        """Gérer les requêtes GET"""
        if self.path == '/':
            self.path = '/src/index.html'
        return super().do_GET()

# Créer le serveur
with socketserver.TCPServer((BIND_ADDRESS, PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"✅ Serveur lancé sur http://{BIND_ADDRESS}:{PORT}")
    print(f"📂 Répertoire racine: {os.getcwd()}")
    print(f"🚀 Accédez au site: http://{BIND_ADDRESS}:{PORT}")
    print(f"🔄 Cache désactivé (rechargement automatique)")
    print(f"⏹️  Appuyez sur Ctrl+C pour arrêter le serveur\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ Serveur arrêté.")
