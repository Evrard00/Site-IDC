/**
 * Cart Devis - Gestion du panier B2B
 * Lubrifiants automobiles
 */

class CartDevis {
  constructor() {
    this.products = [
      {
        id: 1,
        name: 'Helix Ultra',
        description: 'Huile moteur essence',
        format: '5L',
        quantity: 1,
        formats: ['1L', '5L', '20L', '60L']
      }
    ];
    this.init();
  }

  init() {
    this.attachEventListeners();
    this.updateUI();
  }

  attachEventListeners() {
    // Quantity buttons
    document.querySelectorAll('.qty-plus').forEach((btn, index) => {
      btn.addEventListener('click', () => this.changeQuantity(index, 1));
    });

    document.querySelectorAll('.qty-minus').forEach((btn, index) => {
      btn.addEventListener('click', () => this.changeQuantity(index, -1));
    });

    // Format selection
    document.querySelectorAll('.format-select').forEach((select, index) => {
      select.addEventListener('change', (e) => {
        this.products[index].format = e.target.value;
        this.updateUI();
      });
    });

    // Remove buttons
    document.querySelectorAll('.btn-remove').forEach((btn, index) => {
      btn.addEventListener('click', () => this.removeProduct(index));
    });

    // Add product button
    const addBtn = document.querySelector('.btn-add-product');
    if (addBtn) {
      addBtn.addEventListener('click', () => this.addProduct());
    }

    // Main buttons
    const devisBtn = document.querySelector('.btn-primary');
    if (devisBtn) {
      devisBtn.addEventListener('click', () => this.submitDevis());
    }

    const commandeEntrepriseBtn = document.querySelectorAll('.btn-secondary')[0];
    if (commandeEntrepriseBtn) {
      commandeEntrepriseBtn.addEventListener('click', () => this.submitCommandeEntreprise());
    }

    // Help button
    const aidBtn = document.querySelector('.btn-secondary-link');
    if (aidBtn) {
      aidBtn.addEventListener('click', () => this.showHelp());
    }
  }

  changeQuantity(index, delta) {
    if (this.products[index]) {
      const newQty = Math.max(1, this.products[index].quantity + delta);
      this.products[index].quantity = newQty;
      this.updateUI();
    }
  }

  removeProduct(index) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce produit ?')) {
      this.products.splice(index, 1);
      this.updateUI();
    }
  }

  addProduct() {
    const newProduct = {
      id: Math.max(...this.products.map(p => p.id)) + 1,
      name: 'Shell Helix Plus',
      description: 'Huile moteur diesel premium',
      format: '5L',
      quantity: 1,
      formats: ['1L', '5L', '20L']
    };
    this.products.push(newProduct);
    this.updateUI();
  }

  submitDevis() {
    const summary = this.products.map(p => 
      `${p.name} - ${p.format} x ${p.quantity}`
    ).join('\n');
    
    const message = `Demande de devis:\n\n${summary}\n\nMerci de nous contacter pour les tarifs.`;
    
    // In real application, send to server
    alert(message);
    console.log('Devis soumis:', this.products);
  }

  submitCommandeEntreprise() {
    alert('Redirection vers le formulaire commande entreprise...');
    // window.location.href = '/commande-entreprise';
  }

  showHelp() {
    alert('Contactez notre équipe support:\nTél: +225 20 21 00 00\nEmail: support@idc.ci');
  }

  updateUI() {
    const container = document.querySelector('.products-section');
    if (!container) return;

    if (this.products.length === 0) {
      container.innerHTML = `
        <div class="empty-cart">
          <p>Votre panier est vide</p>
          <button class="btn-add-product">Ajouter un produit</button>
        </div>
      `;
      this.attachEventListeners();
      this.updateSummary();
      return;
    }

    // Render products
    const productsHTML = this.products.map((product, index) => `
      <div class="product-card">
        <div class="product-header">
          <div class="product-image-wrapper">
            <div class="product-image">
              <span class="image-fallback">🛢️</span>
            </div>
          </div>
          <div class="product-info">
            <h3 class="product-name">${product.name}</h3>
            <p class="product-description">${product.description}</p>
          </div>
          <button class="btn-remove" title="Supprimer du panier">✕</button>
        </div>

        <div class="product-controls">
          <div class="control-group">
            <label>Format:</label>
            <select class="format-select" aria-label="Format du produit">
              ${product.formats.map(fmt => 
                `<option value="${fmt}" ${fmt === product.format ? 'selected' : ''}>${fmt}</option>`
              ).join('')}
            </select>
          </div>

          <div class="control-group">
            <label>Quantité:</label>
            <div class="quantity-control">
              <button class="qty-btn qty-minus" ${product.quantity <= 1 ? 'disabled' : ''}>−</button>
              <span class="qty-display">${product.quantity}</span>
              <button class="qty-btn qty-plus">+</button>
            </div>
          </div>
        </div>

        <div class="product-summary">
          <div class="summary-item">
            <span class="summary-label">Produit:</span>
            <span class="summary-value">${product.name}</span>
          </div>
          <div class="summary-item">
            <span class="summary-label">Format:</span>
            <span class="summary-value">${product.format}</span>
          </div>
          <div class="summary-item">
            <span class="summary-label">Quantité:</span>
            <span class="summary-value">${product.quantity}</span>
          </div>
        </div>
      </div>
    `).join('');

    const addButtonHTML = `
      <button class="btn-add-product">+ Ajouter un produit</button>
    `;

    container.innerHTML = productsHTML + addButtonHTML;
    this.attachEventListeners();
    this.updateSummary();
  }

  updateSummary() {
    const totalProducts = this.products.length;
    const totalQuantity = this.products.reduce((sum, p) => sum + p.quantity, 0);

    // Update summary box
    const summaryBox = document.querySelector('.summary-box');
    if (summaryBox) {
      const productDetailEl = summaryBox.querySelector('.summary-detail:nth-child(2) strong');
      const quantityDetailEl = summaryBox.querySelector('.summary-detail:nth-child(3) strong');
      
      if (productDetailEl) productDetailEl.textContent = totalProducts;
      if (quantityDetailEl) quantityDetailEl.textContent = totalQuantity;
    }

    // Update info bar
    const infoBar = document.querySelector('.info-bar');
    if (infoBar && this.products.length > 0) {
      infoBar.innerHTML = `
        <p>
          💼 Vous avez sélectionné <strong>${totalProducts}</strong> produit(s) pour une quantité
          totale de <strong>${totalQuantity}</strong> unité(s).
        </p>
      `;
    } else if (infoBar) {
      infoBar.innerHTML = '';
    }

    // Show/hide sidebar based on cart content
    const cartSummary = document.querySelector('.cart-summary');
    if (cartSummary) {
      cartSummary.style.display = this.products.length > 0 ? 'block' : 'none';
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new CartDevis();
});
