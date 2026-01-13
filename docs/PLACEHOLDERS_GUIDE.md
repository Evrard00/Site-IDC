# 📷 Guide des Placeholders d'Images

## 📚 Vue d'ensemble

Le fichier `assets/css/placeholders.css` contient des styles prêts à l'emploi pour afficher des images placeholder (temporaires) en attendant les vraies images.

---

## 🎨 Classes disponibles

### Placeholder Général

```html
<!-- Placeholder simple -->
<div class="placeholder" style="width: 300px; height: 200px;"></div>

<!-- Placeholder avec texte personnalisé -->
<div class="placeholder" data-text="Votre image ici" style="width: 300px; height: 200px;"></div>
```

### Placeholders Spécialisés

#### Hero Image
```html
<!-- Placeholder pour hero section -->
<div class="placeholder-hero">
    Placeholder Hero - 400px
</div>

<!-- Responsive : 250px sur mobile -->
```

#### Card Image
```html
<!-- Placeholder pour card -->
<div class="placeholder-card">
    Image
</div>

<!-- Avec aspect ratio 1:1 -->
```

#### Product Image
```html
<!-- Placeholder pour produit -->
<div class="product-image placeholder">
    Produit Image
</div>

<!-- Hauteur : 250px, responsive -->
```

#### Avatar
```html
<!-- Avatar circulaire -->
<div class="placeholder-avatar">👤</div>

<!-- Tailles disponibles -->
<div class="placeholder-avatar small">👤</div>
<div class="placeholder-avatar">👤</div>
<div class="placeholder-avatar large">👤</div>
```

#### Rectangle
```html
<!-- Format 16:9 (standard) -->
<div class="placeholder-rect">
    Image Rect
</div>

<!-- Format carré -->
<div class="placeholder-rect square">
    Image Carré
</div>

<!-- Format portrait -->
<div class="placeholder-rect tall">
    Image Portrait
</div>

<!-- Format large -->
<div class="placeholder-rect wide">
    Image Large
</div>
```

### Placeholders Colorés

```html
<!-- Bleu primaire -->
<div class="placeholder placeholder-blue" style="width: 200px; height: 200px;">
    Bleu
</div>

<!-- Orange secondaire -->
<div class="placeholder placeholder-orange" style="width: 200px; height: 200px;">
    Orange
</div>

<!-- Autres couleurs -->
<div class="placeholder placeholder-green" style="width: 200px; height: 200px;">
    Vert
</div>

<div class="placeholder placeholder-purple" style="width: 200px; height: 200px;">
    Violet
</div>

<div class="placeholder placeholder-pink" style="width: 200px; height: 200px;">
    Rose
</div>

<div class="placeholder placeholder-cyan" style="width: 200px; height: 200px;">
    Cyan
</div>
```

### Placeholders avec Icônes

```html
<!-- Image générique -->
<div class="placeholder placeholder-icon image" style="width: 300px; height: 300px;">
    Image
</div>

<!-- Vidéo -->
<div class="placeholder placeholder-icon video" style="width: 300px; height: 300px;">
    Vidéo
</div>

<!-- Galerie -->
<div class="placeholder placeholder-icon gallery" style="width: 300px; height: 300px;">
    Galerie
</div>

<!-- Graphique -->
<div class="placeholder placeholder-icon chart" style="width: 300px; height: 300px;">
    Graphique
</div>

<!-- Carte -->
<div class="placeholder placeholder-icon map" style="width: 300px; height: 300px;">
    Carte
</div>

<!-- Profil -->
<div class="placeholder placeholder-icon profile" style="width: 300px; height: 300px;">
    Profil
</div>

<!-- Équipe -->
<div class="placeholder placeholder-icon team" style="width: 300px; height: 300px;">
    Équipe
</div>
```

---

## ⚡ Animations

### Shimmer (Scintillement)

```html
<!-- Animation shimmer -->
<div class="placeholder-section">
    Image avec animation shimmer
</div>
```

### Pulse (Pulsation)

```html
<!-- Animation pulse -->
<div class="placeholder pulse" style="width: 300px; height: 200px;">
    Pulse
</div>
```

### Fade (Fading)

```html
<!-- Animation fade -->
<div class="placeholder fade" style="width: 300px; height: 200px;">
    Fade
</div>
```

---

## 🦴 Skeleton Loaders

Pour les contenus en cours de chargement :

```html
<!-- Petit skeleton -->
<div class="skeleton small"></div>

<!-- Skeleton moyen -->
<div class="skeleton medium"></div>

<!-- Skeleton large -->
<div class="skeleton large"></div>
```

### Texte skeleton

```html
<!-- Lignes de texte en cours de chargement -->
<div class="placeholder-line full"></div>
<div class="placeholder-line full"></div>
<div class="placeholder-line medium"></div>
```

---

## 📦 Exemples complets

### Hero Section avec Placeholder

```html
<section class="hero">
    <div class="placeholder-hero">
        Section Hero à venir
    </div>
</section>
```

### Card avec Placeholder

```html
<div class="card">
    <div class="placeholder-card"></div>
    <h3>Titre du produit</h3>
    <p>Description...</p>
</div>
```

### Produit e-shop

```html
<div class="product-card">
    <div class="product-image placeholder"></div>
    <h3>Produit</h3>
    <p class="product-price">99,99 €</p>
    <button class="btn">Ajouter au panier</button>
</div>
```

### Grid avec Placeholders

```html
<div class="grid">
    <div class="placeholder-card"></div>
    <div class="placeholder-card"></div>
    <div class="placeholder-card"></div>
</div>
```

### Testimonial avec Avatar

```html
<div class="testimonial-card">
    <div class="placeholder-avatar">👤</div>
    <p class="quote">Témoignage en attente...</p>
    <p class="author">Client</p>
</div>
```

---

## 🎯 Bonnes pratiques

### 1. Remplacer les placeholders

```html
<!-- Avant (placeholder) -->
<img class="placeholder-img" src="" alt="Image" style="width: 100%; height: 250px;">

<!-- Après (vraie image) -->
<img src="/assets/images/photo.jpg" alt="Description">
```

### 2. Utiliser le bon placeholder

```html
<!-- Pour un hero : placeholder-hero -->
<div class="placeholder-hero"></div>

<!-- Pour un produit : product-image placeholder -->
<div class="product-image placeholder"></div>

<!-- Pour une card : placeholder-card -->
<div class="placeholder-card"></div>
```

### 3. Ajouter des données réalistes

```html
<!-- Garder la structure HTML identique -->
<div class="product-card">
    <div class="product-image placeholder"></div>
    <!-- Ces éléments resteront inchangés -->
    <h3>Nom du produit</h3>
    <p class="product-price">Prix</p>
</div>
```

---

## 🔄 Remplacer les placeholders

### Méthode simple : Swapper les divs

```html
<!-- Placeholder -->
<div class="product-image placeholder"></div>

<!-- Remplacer par -->
<img src="/assets/images/produit.jpg" alt="Produit" style="width: 100%; height: 250px;">
```

### Méthode avec CSS

```css
/* Cacher le placeholder quand l'image est chargée */
.product-image.placeholder img {
    display: block;
}

.product-image.placeholder::before {
    display: none;
}
```

---

## 📱 Responsive

Tous les placeholders s'adaptent automatiquement aux écrans :

```html
<!-- Placeholder responsif -->
<div class="placeholder-rect">
    S'adapte à tous les écrans
</div>

<!-- Placeholder hero responsif -->
<div class="placeholder-hero">
    400px desktop, 250px mobile
</div>
```

---

## 🎨 Personnalisation

### Créer un placeholder personnalisé

```css
.my-custom-placeholder {
    background: linear-gradient(135deg, #your-color1 0%, #your-color2 100%);
    width: 100%;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba(255, 255, 255, 0.8);
    font-size: 18px;
    border-radius: 4px;
}
```

### Utiliser une couleur du design system

```css
.placeholder-brand {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
}
```

---

## 💡 Conseils

1. **Garder une structure HTML cohérente** - Remplacer seulement le placeholder, pas la structure
2. **Utiliser les bonnes hauteurs** - Product (250px), Hero (400px), Card (aspect-ratio: 1)
3. **Ajouter du texte descriptif** - Aide l'utilisateur à comprendre ce qui va arriver
4. **Utiliser des animations** - Indique que le site est en cours de chargement
5. **Garder la même couleur** - Facilite le remplacement avec de vraies images

---

## 📊 Référence rapide

| Classe | Usage | Hauteur |
|--------|-------|---------|
| `.placeholder-hero` | Hero section | 400px (responsive) |
| `.placeholder-card` | Card image | aspect-ratio: 1 |
| `.product-image.placeholder` | Produit e-shop | 250px |
| `.placeholder-rect` | Rectangle générique | 16:9 |
| `.placeholder-avatar` | Avatar circulaire | 80px |
| `.placeholder-section` | Section image | 300px |
| `.placeholder-[color]` | Couleur spécifique | Flexible |

---

## 🚀 Utilisation dans les pages

### Page produit
```html
<div class="product-card">
    <div class="product-image placeholder"></div>
    <h3>Nom produit</h3>
    <p>Descripton</p>
</div>
```

### Page galerie
```html
<div class="grid">
    <div class="placeholder-card"></div>
    <div class="placeholder-card"></div>
    <div class="placeholder-card"></div>
</div>
```

### Page accueil
```html
<section class="hero">
    <div class="placeholder-hero">Section Hero</div>
</section>
```

---

**Fichier** : `assets/css/placeholders.css`  
**Lignes** : 250+  
**Classes** : 30+  

Tous les styles sont prêts à l'emploi ! 🎉
