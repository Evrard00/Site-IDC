# 🎨 Guide Design IDC - Couleurs et Styles

## 📋 Résumé

Le design du site IDC utilise les couleurs du logo officiel pour une cohérence visuelle totale.

---

## 🎨 Palette de Couleurs

### Couleurs Primaires
| Couleur | Hex | RGB | Utilisation |
|---------|-----|-----|------------|
| **Vert Foncé** | `#0F5629` | 15, 86, 41 | Background footer |
| **Vert IDC** | `#1B7D3A` | 27, 125, 58 | Textes, titres, accents |
| **Vert Clair** | `#2D9F52` | 45, 159, 82 | Hover, effets |

### Couleurs Secondaires
| Couleur | Hex | RGB | Utilisation |
|---------|-----|-----|------------|
| **Orange** | `#FF6600` | 255, 102, 0 | Accents, boutons |
| **Orange Clair** | `#FFCC80` | 255, 200, 128 | Backgrounds légers |

### Couleurs Neutres
| Couleur | Hex | RGB | Utilisation |
|---------|-----|-----|------------|
| Blanc | `#FFFFFF` | 255, 255, 255 | Fond principal |
| Gris Clair | `#F5F5F5` | 245, 245, 245 | Sections alternées |
| Gris | `#666666` | 102, 102, 102 | Texte secondaire |
| Noir | `#1A1A1A` | 26, 26, 26 | Texte principal |

---

## 🎯 Système de Design

### 1. **Header/Navigation**
```css
.navbar {
    background: white;
    box-shadow: 0 2px 12px rgba(27, 125, 58, 0.1);
}

.navbar__brand {
    color: var(--primary-color); /* #1B7D3A */
    font-weight: 700;
}

.navbar__link:hover {
    color: var(--primary-color);
    border-bottom: 2px solid var(--primary-color);
}
```

**Caractéristiques:**
- Fond blanc propre
- Ombre subtile avec la teinte verte
- Marque de navigation au hover

---

### 2. **Hero Section**
```css
.hero {
    background: linear-gradient(135deg, #1b7d3a 0%, #ff6600 100%);
    color: white;
    padding: 120px var(--spacing-md);
}

.hero h1 {
    font-size: clamp(32px, 5vw, 56px);
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}
```

**Caractéristiques:**
- Gradient vert → orange
- Texte blanc avec ombre
- Responsive (clamp pour taille fluide)

---

### 3. **Cards & Sections**
```css
.card {
    background: white;
    border-top: 4px solid var(--secondary-color); /* Orange */
    box-shadow: 0 2px 8px rgba(27, 125, 58, 0.08);
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: 0 8px 24px rgba(27, 125, 58, 0.15);
    transform: translateY(-6px);
}

.card h3 {
    color: var(--primary-color); /* Vert */
    font-weight: 700;
}
```

**Caractéristiques:**
- Bordure supérieure orange
- Ombre subtile avec teinte verte
- Animation au hover (élévation)
- Titres en vert

---

### 4. **Boutons**

#### Bouton Primaire
```css
.btn {
    background-color: var(--primary-color); /* #1B7D3A */
    color: white;
    border: 2px solid var(--primary-color);
    font-weight: 600;
}

.btn:hover {
    background-color: var(--primary-dark); /* #0F5629 */
    box-shadow: 0 4px 12px rgba(27, 125, 58, 0.3);
}
```

#### Bouton Secondaire
```css
.btn-secondary {
    background-color: var(--secondary-color); /* #FF6600 */
    border-color: var(--secondary-color);
}

.btn-secondary:hover {
    background-color: #e55a00;
    box-shadow: 0 4px 12px rgba(255, 102, 0, 0.3);
}
```

#### Bouton Outline
```css
.btn-outline {
    background-color: transparent;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
}

.btn-outline:hover {
    background-color: var(--primary-color);
    color: white;
}
```

---

### 5. **Stat Cards**
```css
.stat-card {
    background: linear-gradient(135deg, white, #f9f9f9);
    border-left: 4px solid var(--secondary-color); /* Orange */
    box-shadow: 0 4px 12px rgba(27, 125, 58, 0.1);
}

.stat-number {
    font-size: clamp(36px, 6vw, 56px);
    color: var(--primary-color); /* Vert */
    font-weight: 900;
}
```

---

### 6. **Testimonials**
```css
.testimonial-card {
    background: white;
    border-left: 4px solid var(--secondary-color); /* Orange */
    box-shadow: 0 4px 12px rgba(27, 125, 58, 0.08);
}

.testimonial-card .quote {
    color: #666;
    font-style: italic;
    line-height: 1.7;
}

.testimonial-card .quote::before {
    content: '"';
    color: var(--secondary-color); /* Orange */
    opacity: 0.3;
}

.testimonial-card .author {
    color: var(--primary-color); /* Vert */
    font-weight: 600;
}
```

---

### 7. **Footer**
```css
.footer {
    background: linear-gradient(135deg, #0f5629 0%, #1b7d3a 100%);
    color: white;
    padding: 32px 0;
}

.footer a {
    color: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
}

.footer a:hover {
    color: white;
}
```

**Caractéristiques:**
- Gradient vert foncé
- Texte blanc avec opacity au hover
- Transitions douces

---

## 🎨 Classes Utilitaires Disponibles

### Classes d'Accent
```html
<!-- Couleur du texte -->
<p class="accent-primary">Texte vert</p>
<p class="accent-secondary">Texte orange</p>

<!-- Backgrounds -->
<div class="bg-primary">Fond vert</div>
<div class="bg-secondary">Fond orange</div>
<div class="bg-primary-light">Fond vert très clair</div>

<!-- Borders -->
<div class="border-primary">Bordure verte</div>
<div class="border-secondary">Bordure orange</div>
<div class="border-top-secondary">Bordure supérieure orange</div>
```

### Gradients
```html
<!-- Gradient principal -->
<section class="gradient-idc">
    Contenu avec gradient vert→orange
</section>

<!-- Gradient foncé -->
<div class="gradient-idc-dark">
    Gradient vert foncé
</div>

<!-- Gradient léger -->
<div class="gradient-idc-light">
    Gradient subtil
</div>
```

### Badges
```html
<span class="badge">Important</span>
<span class="badge badge-secondary">Nouveau</span>
<span class="badge badge-outline">Info</span>
```

### Section Titles
```html
<h2 class="section-title">Mon Titre</h2>
<!-- Ajoute automatiquement une barre de couleur en-dessous -->
```

### Feature Boxes
```html
<div class="feature-box">
    <div class="feature-box__icon">💡</div>
    <h3>Titre</h3>
    <p>Description</p>
</div>
```

### CTA Banner
```html
<section class="cta-banner">
    <h2>Appel à l'Action</h2>
    <p>Message important</p>
    <button class="btn btn-secondary">Cliquez ici</button>
</section>
```

---

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 576px
- **Tablet**: 576px - 768px
- **Small Desktop**: 768px - 992px
- **Desktop**: 992px - 1200px
- **Large Desktop**: > 1200px

### Utilisation
```css
/* Mobile first */
.my-element {
    font-size: 14px;
    grid-template-columns: 1fr;
}

/* Tablet et plus */
@media (min-width: 768px) {
    .my-element {
        font-size: 16px;
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop et plus */
@media (min-width: 992px) {
    .my-element {
        font-size: 18px;
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 🎯 Bonnes Pratiques

### 1. **Cohérence des Couleurs**
- Utilisez toujours `var(--primary-color)` pour le vert
- Utilisez `var(--secondary-color)` pour l'orange
- Evitez les couleurs en dur (hardcoded)

### 2. **Espacement**
```css
/* Utilisez les variables d'espacement */
margin: var(--spacing-md);    /* 16px */
padding: var(--spacing-lg);   /* 24px */
gap: var(--spacing-md);       /* 16px */
```

### 3. **Typographie**
```css
/* Utilisez les classes font-size */
.heading { font-size: var(--font-size-2xl); font-weight: 700; }
.body { font-size: var(--font-size-base); line-height: 1.6; }
.small { font-size: var(--font-size-sm); }
```

### 4. **Transitions**
```css
/* Utilisez la transition standard */
transition: var(--transition); /* all 0.3s ease */
```

### 5. **Shadows**
```css
/* Ombre subtile pour cards */
box-shadow: 0 2px 8px rgba(27, 125, 58, 0.08);

/* Ombre au hover */
box-shadow: 0 8px 24px rgba(27, 125, 58, 0.15);
```

---

## 🔧 Fichiers CSS Utilisés

| Fichier | Purpose | Taille |
|---------|---------|--------|
| `reset.css` | Normalisation cross-browser | 32 lines |
| `variables.css` | Variables CSS (couleurs, espacement) | 50 lines |
| `styles.css` | Styles principaux et responsive | 640 lines |
| `placeholders.css` | Placeholders images | 396 lines |
| **`theme-idc.css`** | **Thème IDC (nouveau)** | **250 lines** |

---

## 📊 Exemple Complet

### HTML
```html
<section class="section">
    <div class="container">
        <h2 class="section-title">Nos Services</h2>
        
        <div class="grid">
            <div class="card">
                <h3>Service 1</h3>
                <p>Description du service</p>
                <button class="btn">En savoir plus</button>
            </div>
            
            <div class="card">
                <h3>Service 2</h3>
                <p>Description du service</p>
                <button class="btn">En savoir plus</button>
            </div>
        </div>
    </div>
</section>
```

### Résultat
- Titre avec barre colorée
- Cards avec bordure orange et ombre verte
- Boutons verts avec hover ombré

---

## ✅ Checklist de Qualité Design

- [ ] Toutes les couleurs du logo IDC sont utilisées
- [ ] Les hover effects sont fluides et subtils
- [ ] Le design est responsive sur tous les breakpoints
- [ ] Les transitions utilisent `var(--transition)`
- [ ] L'espacement utilise `var(--spacing-*)`
- [ ] Les shadows évoquent la palette verte
- [ ] Les boutons ont suffisamment de contraste
- [ ] La typographie est cohérente
- [ ] Les sections alternent couleurs/blancs pour clarté

---

## 🚀 Démarrage Rapide

```html
<!-- Inclure les CSS dans ce ordre -->
<link rel="stylesheet" href="./assets/css/reset.css">
<link rel="stylesheet" href="./assets/css/variables.css">
<link rel="stylesheet" href="./assets/css/styles.css">
<link rel="stylesheet" href="./assets/css/placeholders.css">
<link rel="stylesheet" href="./assets/css/theme-idc.css">
```

**Prêt à utiliser !** 🎉
