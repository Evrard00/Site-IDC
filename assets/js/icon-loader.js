/**
 * Système de chargement des icônes SVG
 * Remplace les Material Symbols par les SVG locaux
 */

class IconLoader {
    constructor() {
        this.svgCache = {};
        this.baseUrl = '/assets/icons/svg/';
        this.init();
    }

    init() {
        // Convertir tous les material-symbols-outlined en SVG
        this.convertMaterialSymbolsToSVG();
    }

    convertMaterialSymbolsToSVG() {
        const icons = document.querySelectorAll('.material-symbols-outlined');
        icons.forEach(el => {
            const iconName = el.textContent.trim();
            this.loadAndReplaceSVG(el, iconName);
        });
    }

    async loadAndReplaceSVG(element, iconName) {
        try {
            const svg = await this.getSVG(iconName);
            if (svg) {
                // Préserver les classes
                const classes = element.getAttribute('class');
                const wrapper = document.createElement('span');
                wrapper.setAttribute('class', classes.replace('material-symbols-outlined', 'icon-svg'));
                wrapper.innerHTML = svg;
                element.replaceWith(wrapper);
            }
        } catch (error) {
            console.warn(`Impossible de charger l'icône: ${iconName}`, error);
        }
    }

    async getSVG(name) {
        if (this.svgCache[name]) {
            return this.svgCache[name];
        }

        try {
            const response = await fetch(`${this.baseUrl}${name}.svg`);
            if (response.ok) {
                const svg = await response.text();
                this.svgCache[name] = svg;
                return svg;
            }
        } catch (error) {
            console.error(`Erreur lors du chargement de ${name}.svg:`, error);
        }
        return null;
    }
}

// Initialiser quand le DOM est prêt
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new IconLoader();
    });
} else {
    new IconLoader();
}
