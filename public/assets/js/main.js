// Main JavaScript - Responsive Design

document.addEventListener('DOMContentLoaded', function() {
    initNavbar();
});

/**
 * Initialise la navigation responsive
 */
function initNavbar() {
    const navbarToggle = document.querySelector('.navbar__toggle');
    const navbarMenu = document.querySelector('.navbar__menu');

    if (navbarToggle) {
        navbarToggle.addEventListener('click', function() {
            navbarToggle.classList.toggle('active');
            navbarMenu.classList.toggle('active');
        });

        // Fermer le menu en cliquant sur un lien
        const navbarLinks = document.querySelectorAll('.navbar__link');
        navbarLinks.forEach(link => {
            link.addEventListener('click', function() {
                navbarToggle.classList.remove('active');
                navbarMenu.classList.remove('active');
            });
        });
    }
}

/**
 * Gère le redimensionnement de la fenêtre
 */
window.addEventListener('resize', function() {
    const navbarMenu = document.querySelector('.navbar__menu');
    const navbarToggle = document.querySelector('.navbar__toggle');

    // Réinitialiser le menu sur les écrans larges
    if (window.innerWidth > 768) {
        navbarMenu?.classList.remove('active');
        navbarToggle?.classList.remove('active');
    }
});
