/* ══════════════════════════════════════════════════════════════════
   EN-TÊTE — menu mobile et barre escamotable
   Ce script était recopié à l'identique dans neuf pages. Chargé en différé :
   il agit sur des éléments déjà présents et n'a rien à faire avant l'affichage.
   ══════════════════════════════════════════════════════════════════ */
(function () {
    'use strict';
    var burger = document.getElementById('burger');
    var barre  = document.getElementById('barre');
    if (burger && barre) {
        burger.addEventListener('click', function () {
            var ouvert = burger.getAttribute('aria-expanded') === 'true';
            burger.setAttribute('aria-expanded', String(!ouvert));
            burger.setAttribute('aria-label', ouvert ? 'Ouvrir le menu' : 'Fermer le menu');
            if (ouvert) { barre.removeAttribute('data-open'); }
            else { barre.setAttribute('data-open', ''); }
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
                burger.click(); burger.focus();
            }
        });
        barre.querySelectorAll('.mobile-nav a').forEach(function (a) {
            a.addEventListener('click', function () {
                if (burger.getAttribute('aria-expanded') === 'true') { burger.click(); }
            });
        });
    }

    var tete = document.getElementById('tete');
    if (!tete) { return; }

    var racine  = document.documentElement;
    var dernier = window.scrollY;
    var tic     = false;
    var cache   = false;

    var SEUIL_HAUT = 120;   // zone de tête où la barre reste toujours posée
    var SEUIL_MVT  = 6;     // mouvement minimal avant de réagir

    // Hauteur déployée : mesurée une fois barre visible, elle sert de marge
    // aux ancres. --tete-bas suit l'état courant et cale les barres collantes.
    var plein = 92;
    function mesurer() {
        var etait = cache;
        if (etait) { tete.removeAttribute('data-hidden'); }
        plein = Math.round(tete.getBoundingClientRect().bottom);
        racine.style.setProperty('--tete-plein', plein + 'px');
        if (etait) { tete.setAttribute('data-hidden', ''); }
        publier();
    }
    function publier() {
        racine.style.setProperty('--tete-bas', (cache ? 10 : plein) + 'px');
    }

    function montrer() {
        if (!cache) { return; }
        cache = false; tete.removeAttribute('data-hidden'); publier();
    }
    function escamoter() {
        if (cache) { return; }
        // le menu mobile ouvert, ou le focus posé dans la barre, retiennent l'en-tête
        if (barre && barre.hasAttribute('data-open')) { return; }
        if (tete.contains(document.activeElement)) { return; }
        cache = true; tete.setAttribute('data-hidden', ''); publier();
    }

    function majTete() {
        var y = window.scrollY;
        if (y > 24) { tete.setAttribute('data-scrolled', ''); }
        else { tete.removeAttribute('data-scrolled'); }

        var delta = y - dernier;
        if (y <= SEUIL_HAUT) {
            montrer();
        } else if (delta > SEUIL_MVT) {
            escamoter();
        } else if (delta < -SEUIL_MVT) {
            montrer();
        }
        if (Math.abs(delta) > SEUIL_MVT || y <= SEUIL_HAUT) { dernier = y; }
        tic = false;
    }

    window.addEventListener('scroll', function () {
        if (!tic) { window.requestAnimationFrame(majTete); tic = true; }
    }, { passive: true });
    window.addEventListener('resize', mesurer, { passive: true });

    // Clavier. Deux cas opposés :
    //  · le focus entre dans la barre — il faut la montrer, sinon on tabule
    //    vers un lien sorti de l'écran ;
    //  · le focus va sur un élément de la page que la barre recouvrirait —
    //    la remontée du défilement l'avait fait réapparaître par-dessus. On
    //    l'escamote alors, pour que l'élément focalisé reste visible
    //    (WCAG 2.2, critère 2.4.11 « focus non masqué »).
    document.addEventListener('focusin', function (e) {
        var cible = e.target;
        if (tete.contains(cible)) { montrer(); return; }
        if (cache || window.scrollY <= SEUIL_HAUT) { return; }
        if (!cible || typeof cible.getBoundingClientRect !== 'function') { return; }
        var r = cible.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) { return; }
        var t = tete.getBoundingClientRect();
        if (r.top < t.bottom && r.bottom > t.top) { escamoter(); }
    });

    mesurer();
    majTete();
})();

/* ══════════════════════════════════════════════════════════════════
   ENVOI DES FORMULAIRES — Netlify Forms
   Les formulaires du site sont validés et annoncés en JavaScript, donc
   soumis à la main. Netlify attend un POST vers « / » contenant le champ
   form-name. Sans pièce jointe on encode en formulaire URL ; avec, on
   laisse le navigateur composer le multipart.

   La fonction renvoie une promesse et ne masque jamais un échec : si
   l'envoi ne passe pas, l'appelant affiche une erreur au lieu d'un faux
   « message envoyé ».
   ══════════════════════════════════════════════════════════════════ */
window.idcEnvoyer = function (form, extras) {
    var donnees = new FormData(form);
    if (extras) {
        Object.keys(extras).forEach(function (k) { donnees.set(k, extras[k]); });
    }
    if (!donnees.get('form-name')) {
        donnees.set('form-name', form.getAttribute('name') || '');
    }

    var joint = (form.getAttribute('enctype') || '').indexOf('multipart') !== -1;
    var options = { method: 'POST', body: joint ? donnees : new URLSearchParams(donnees).toString() };
    if (!joint) {
        options.headers = { 'Content-Type': 'application/x-www-form-urlencoded' };
    }

    return fetch('/', options).then(function (r) {
        if (!r.ok) { throw new Error('Réponse ' + r.status); }
        return r;
    });
};
