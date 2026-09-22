import React, { useState } from 'react';
import './CartDevis.css';

const CartDevis = () => {
  const [products, setProducts] = useState([
    {
      id: 1,
      name: 'Helix Ultra',
      description: 'Huile moteur essence',
      format: '5L',
      quantity: 1,
      formats: ['1L', '5L', '20L', '60L'],
      image: '../assets/images/products/helix-ultra.png',
      fallbackImage: '🛢️'
    }
  ]);

  const handleFormatChange = (id, newFormat) => {
    setProducts(products.map(product =>
      product.id === id ? { ...product, format: newFormat } : product
    ));
  };

  const handleQuantityChange = (id, delta) => {
    setProducts(products.map(product => {
      if (product.id === id) {
        const newQuantity = Math.max(1, product.quantity + delta);
        return { ...product, quantity: newQuantity };
      }
      return product;
    }));
  };

  const handleAddProduct = () => {
    const newProduct = {
      id: products.length + 1,
      name: 'Shell Helix Plus',
      description: 'Huile moteur diesel premium',
      format: '5L',
      quantity: 1,
      formats: ['1L', '5L', '20L'],
      image: '../assets/images/products/helix-plus.png',
      fallbackImage: '🛢️'
    };
    setProducts([...products, newProduct]);
  };

  const handleRemoveProduct = (id) => {
    setProducts(products.filter(product => product.id !== id));
  };

  const totalQuantity = products.reduce((sum, p) => sum + p.quantity, 0);

  return (
    <div className="cart-devis-container">
      <div className="cart-header">
        <h1>Panier</h1>
        <p className="cart-subtitle">Demande de devis</p>
      </div>

      <div className="cart-content">
        <div className="products-section">
          {products.length === 0 ? (
            <div className="empty-cart">
              <p>Votre panier est vide</p>
              <button className="btn-add-product" onClick={handleAddProduct}>
                Ajouter un produit
              </button>
            </div>
          ) : (
            <>
              {products.map((product) => (
                <div key={product.id} className="product-card">
                  {/* Produit Info */}
                  <div className="product-header">
                    {/* Image */}
                    <div className="product-image-wrapper">
                      <div className="product-image">
                        {product.image ? (
                          <img src={product.image} alt={product.name} />
                        ) : (
                          <span className="image-fallback">{product.fallbackImage}</span>
                        )}
                      </div>
                    </div>

                    {/* Détails produit */}
                    <div className="product-info">
                      <h3 className="product-name">{product.name}</h3>
                      <p className="product-description">{product.description}</p>
                    </div>

                    {/* Bouton supprimer */}
                    <button
                      className="btn-remove"
                      onClick={() => handleRemoveProduct(product.id)}
                      title="Supprimer du panier"
                    >
                      ✕
                    </button>
                  </div>

                  {/* Sélecteurs */}
                  <div className="product-controls">
                    <div className="control-group">
                      <label>Format:</label>
                      <select
                        className="format-select"
                        value={product.format}
                        onChange={(e) => handleFormatChange(product.id, e.target.value)}
                      >
                        {product.formats.map((fmt) => (
                          <option key={fmt} value={fmt}>
                            {fmt}
                          </option>
                        ))}
                      </select>
                    </div>

                    <div className="control-group">
                      <label>Quantité:</label>
                      <div className="quantity-control">
                        <button
                          className="qty-btn"
                          onClick={() => handleQuantityChange(product.id, -1)}
                          disabled={product.quantity <= 1}
                        >
                          −
                        </button>
                        <span className="qty-display">{product.quantity}</span>
                        <button
                          className="qty-btn"
                          onClick={() => handleQuantityChange(product.id, 1)}
                        >
                          +
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Récapitulatif */}
                  <div className="product-summary">
                    <div className="summary-item">
                      <span className="summary-label">Produit:</span>
                      <span className="summary-value">{product.name}</span>
                    </div>
                    <div className="summary-item">
                      <span className="summary-label">Format:</span>
                      <span className="summary-value">{product.format}</span>
                    </div>
                    <div className="summary-item">
                      <span className="summary-label">Quantité:</span>
                      <span className="summary-value">{product.quantity}</span>
                    </div>
                  </div>
                </div>
              ))}

              {/* Ajouter produit */}
              <button className="btn-add-product" onClick={handleAddProduct}>
                + Ajouter un produit
              </button>
            </>
          )}
        </div>

        {/* Sidebar/Résumé */}
        {products.length > 0 && (
          <div className="cart-summary">
            <div className="summary-box">
              <h3>Résumé</h3>
              <div className="summary-detail">
                <span>Nombre de produits:</span>
                <strong>{products.length}</strong>
              </div>
              <div className="summary-detail">
                <span>Quantité totale:</span>
                <strong>{totalQuantity}</strong>
              </div>

              {/* Message prix */}
              <div className="price-message">
                <span className="info-icon">ℹ️</span>
                <p>
                  <strong>Les prix ne sont pas affichés.</strong> Un commercial IDC vous contactera
                  pour définir les tarifs et modalités de paiement.
                </p>
              </div>

              {/* Boutons principaux */}
              <div className="action-buttons">
                <button className="btn-primary">Demander un devis</button>
                <button className="btn-secondary">Commande entreprise</button>
              </div>

              {/* Boutons secondaires */}
              <div className="secondary-buttons">
                <button className="btn-secondary-link">Besoin d'aide ?</button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Message informatif footer */}
      {products.length > 0 && (
        <div className="info-bar">
          <p>
            💼 Vous avez selectionné <strong>{products.length}</strong> produit(s) pour une quantité
            total de <strong>{totalQuantity}</strong> unité(s).
          </p>
        </div>
      )}
    </div>
  );
};

export default CartDevis;
