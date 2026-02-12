// Load and inject footer on all pages
document.addEventListener('DOMContentLoaded', function() {
    // Determine the correct path based on current page location
    const currentPath = window.location.pathname;
    const isDashboard = currentPath.includes('dashboard.html') || 
                        currentPath.includes('purchases.html') || 
                        currentPath.includes('cartes-tpe.html');
    
    let footerPath;
    if (isDashboard) {
        footerPath = '../../assets/html/footer.html';
    } else if (currentPath.includes('src/')) {
        footerPath = '../assets/html/footer.html';
    } else {
        footerPath = './assets/html/footer.html';
    }
    
    // Fetch and insert footer
    fetch(footerPath)
        .then(response => response.text())
        .then(html => {
            // Find or create a footer container
            let footerContainer = document.querySelector('footer');
            
            if (footerContainer) {
                // Replace existing footer
                footerContainer.outerHTML = html;
            } else {
                // Insert before closing body tag
                document.body.insertAdjacentHTML('beforeend', html);
            }
        })
        .catch(error => console.log('Footer not loaded:', error));
});
