# Composant Panier / Demande de Devis B2B

Composant de panier avancé pour l'application B2B de vente de lubrifiants automobiles (Shell Helix, etc.)

## 📋 Fichiers fournis

### Version React
- `components/CartDevis.jsx` - Composant React principal
- `components/CartDevis.css` - Styles du composant

### Version HTML/CSS/JS pure
- `cart-devis.html` - Page HTML complète
- `cart-devis.css` - Feuille de styles
- `cart-devis.js` - Logique JavaScript

## ✨ Fonctionnalités

### Obligatoires (comme spécifié)
✅ Bouton principal "Demander un devis" (pas "Commander")
✅ Contrôle de quantité avec boutons − et + fonctionnels (min=1)
✅ Emplacement pour image produit avec fallback emoji 🛢️
✅ Récapitulatif complet (nom, format, quantité)
✅ Sélecteur de format via dropdown (1L, 5L, 20L, 60L)
✅ Message "Les prix ne sont pas affichés. Un commercial vous contactera..."
✅ Boutons secondaires "Besoin d'aide ?" et "Commande entreprise"
✅ Design mobile-first, responsif
✅ Couleur orange #E8500A

### Supplémentaires
✅ Ajout/suppression de produits dynamique
✅ Récapitulatif en sidebar sticky
✅ Barre info avec résumé final
✅ Gestion d'état complète
✅ UX fluide avec animations

## 🚀 Intégration React

```jsx
import CartDevis from '@/components/CartDevis';

function App() {
  return (
    <div>
      <CartDevis />
    </div>
  );
}
```

## 🚀 Intégration HTML pure

Incluez simplement les fichiers dans votre page:

```html
<link rel="stylesheet" href="./cart-devis.css">
<script src="./cart-devis.js"></script>
```

Ou ouvrez directement `cart-devis.html` dans le navigateur.

## 🎨 Couleurs principales

- **Orange (Primary)**: `#E8500A`
- **Fond clair**: `#FAFAFA`
- **Blanc**: `#FFFFFF`
- **Texte sombre**: `#0B0B0B`
- **Texte gris**: `#777`, `#666`
- **Bordure légère**: `#E8E8E8`

## 📱 Breakpoints responsifs

- **Desktop**: > 768px (grid 2 colonnes)
- **Tablet**: 480px - 768px
- **Mobile**: < 480px (colonne unique)

## 🛠️ Personnalisation

### Ajouter des produits

**React:**
```javascript
const [products, setProducts] = useState([
  {
    id: 1,
    name: 'Shell Helix Ultra',
    description: 'Huile moteur haute performance',
    format: '5L',
    quantity: 1,
    formats: ['1L', '5L', '20L', '60L'],
    image: 'url-vers-image.png',
    fallbackImage: '🛢️'
  }
]);
```

**HTML/JS:**
```javascript
addProduct() {
  const newProduct = {
    id: Math.max(...this.products.map(p => p.id)) + 1,
    name: 'Your Product',
    description: 'Description',
    format: '5L',
    quantity: 1,
    formats: ['1L', '5L', '20L']
  };
  this.products.push(newProduct);
  this.updateUI();
}
```

### Personnaliser les boutons

Modifiez les textes dans le JSX/HTML:
- "Demander un devis"
- "Commande entreprise"
- "Besoin d'aide ?"

### Intégration API

Pour soumettre réellement le devis:

```javascript
submitDevis() {
  // Envoyer vers votre API
  fetch('/api/devis', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ products: this.products })
  })
  .then(res => res.json())
  .then(data => console.log('Devis créé:', data));
}
```

## 📦 Dépendances

### React
- React 16+ (ou tout framework moderne)
- CSS Modules (optionnel, utilise CSS global par défaut)

### HTML/JS pure
- Aucune dépendance
- JavaScript vanilla nécessaire
- CSS3 support (flexbox, grid)

## 🔧 Fonctionnalités avancées

### Gestion du panier
- Ajout/suppression dynamique
- Modification formats et quantités
- Validation quantité minimum (1)
- Calcul totaux automatique

### Messages informatifs
- Message prix non affichés
- Barre résumé sticky
- Info bar basée

### Accessibilité
- Labels correctement associés
- Boutons disabled prévisualisés
- Navigation au clavier possible

## 📄 Structure des données produit

```javascript
{
  id: number,                    // ID unique
  name: string,                  // Nom produit
  description: string,           // Description courte
  format: string,                // Format sélectionné (ex: "5L")
  quantity: number,              // Quantité (min 1)
  formats: string[],             // Options disponibles
  image?: string,                // URL image (optionnel)
  fallbackImage: string          // Emoji fallback
}
```

## 🎯 Cas d'usage

- Plateforme B2B de vente de lubrifiants
- Demande de devis en ligne
- Panier pré-devis (sans prix affiché)
- Intégration CRM
- Suivi commercial

## 📞 Support et contact

Pour intégrer avec votre système:
- Modifiez `submitDevis()` pour appeler votre API
- Personnalisez les textes et images produits
- Adaptez les styles à votre branding

## 📋 Checklist d'intégration

- [ ] Copier les fichiers appropriés (React ou HTML)
- [ ] Intégrer dans votre projet
- [ ] Personnaliser les produits
- [ ] Connecter les boutons à vos endpoints API
- [ ] Tester responsivité mobile
- [ ] Tester interaction quantité/format
- [ ] Configurer messages success/error
- [ ] Vérifier accessibilité

---

**Version**: 1.0.0
**Dernière mise à jour**: Avril 2026
**Compatible**: IDC Lubrifiants B2B Application
