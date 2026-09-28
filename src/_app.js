/* ══════════════════════════════════════════════════════════════════
   COQUILLE DE L'ESPACE CONNECTÉ — colonne de navigation réductible

   Les douze pages de l'espace client et du back-office partageaient une
   feuille de style mais aucun script : chaque comportement aurait dû
   être recopié douze fois. Ce fichier est leur script commun.

   La colonne se réduit à ses icônes pour rendre la largeur au contenu.
   Trois précautions :

   · l'état est retenu dans localStorage, sinon il se perdrait à chaque
     changement de page — une bascule qu'il faut refaire à chaque clic ne
     sert à rien ;
   · les libellés restent dans le document, seulement masqués à l'œil
     par la technique de .sr-only. Un lecteur d'écran continue d'annoncer
     « Tableau de bord », et un attribut title donne l'infobulle à la
     souris ;
   · la bascule ne vaut qu'au-dessus de 900 px. En dessous, la colonne
     est déjà une barre horizontale : la réduire n'aurait pas de sens, et
     le bouton disparaît.
   ══════════════════════════════════════════════════════════════════ */
(function () {
    'use strict';

    var CLE = 'idc-menu-reduit';
    var racine = document.documentElement;
    var bouton = document.getElementById('basculeMenu');
    if (!bouton) { return; }

    function lire() {
        try { return localStorage.getItem(CLE) === '1'; } catch (e) { return false; }
    }

    function poser(reduit) {
        if (reduit) { racine.setAttribute('data-menu-reduit', ''); }
        else { racine.removeAttribute('data-menu-reduit'); }
        bouton.setAttribute('aria-expanded', String(!reduit));
        bouton.setAttribute('aria-label',
            reduit ? 'Déployer le menu de navigation' : 'Réduire le menu de navigation');
        try { localStorage.setItem(CLE, reduit ? '1' : '0'); } catch (e) { /* mode privé */ }
    }

    // L'état initial est déjà posé par le fragment en tête de page, avant le
    // premier rendu : sans lui la colonne s'afficherait déployée puis se
    // replierait sous les yeux du visiteur. Ici on ne fait que l'annoncer.
    poser(lire());

    bouton.addEventListener('click', function () {
        poser(!racine.hasAttribute('data-menu-reduit'));
    });

    // Un title par entrée : réduite, la colonne ne montre que des icônes, et
    // la souris n'a plus rien à lire. Le libellé vient du <span> déjà présent.
    var entrees = document.querySelectorAll('.side-nav a, .side-nav button');
    Array.prototype.forEach.call(entrees, function (e) {
        if (e.getAttribute('title')) { return; }
        var etiquette = e.querySelector('span:not(.sr-only):not(.tag)');
        if (etiquette) { e.setAttribute('title', etiquette.textContent.trim()); }
    });
}());
