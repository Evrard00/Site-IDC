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


/* ══════════════════════════════════════════════════════════════════
   SESSION
   Ce bloc était recopié dans les treize pages connectées : neuf du
   back-office, quatre de l'espace client. Seize kilo-octets, et treize
   endroits à modifier pour un seul correctif.

   Les deux variantes ne différaient que par le nom de repli et la
   seconde ligne de l'en-tête — l'adresse côté back-office, le mode de
   facturation côté client, comme le fait leur application. L'attribut
   data-espace porté par .app les distingue.
   ══════════════════════════════════════════════════════════════════ */
(function () {
    'use strict';

    var app = document.querySelector('.app');
    if (!app) { return; }
    var admin = app.getAttribute('data-espace') === 'admin';

    var brut = null;
    try { brut = localStorage.getItem('idc-session'); } catch (e) { /* stockage bloqué */ }
    if (!brut) { window.location.replace('login.html'); return; }

    var session = {};
    try { session = JSON.parse(brut) || {}; } catch (e) { session = {}; }

    var PAIEMENT = { CASH: 'Comptant', CREDIT: 'Crédit', ACCOUNT: 'Compte' };
    var nom = session.nom || (admin ? 'Administration IDC' : 'Client IDC');
    var seconde = admin ? (session.email || '')
                        : (PAIEMENT[session.paiement] || 'Comptant');

    var elNom = document.getElementById('whoNom');
    var elMail = document.getElementById('whoMail');
    var elAv = document.getElementById('whoAvatar');
    if (elNom) { elNom.textContent = nom; }
    if (elMail) { elMail.textContent = seconde; }
    if (elAv) {
        elAv.textContent = nom.split(/\s+/).map(function (m) { return m.charAt(0); })
                              .join('').toUpperCase().slice(0, 2);
    }

    var sortie = document.getElementById('deconnexion');
    if (sortie) {
        sortie.addEventListener('click', function () {
            try { localStorage.removeItem('idc-session'); } catch (e) { /* rien */ }
            window.location.replace('login.html');
        });
    }
}());


/* ══════════════════════════════════════════════════════════════════
   FILTRES DE LISTE
   Le filtrage vivait dans un script recopié par page, couplé à des
   identifiants : #f-statut, #f-type, #f-recherche. Deux conséquences.
   Les filtres que j'ai ajoutés à Cartes TPE, nommés #c-…, n'avaient
   aucune logique derrière et ne faisaient rien. Et notifications.html,
   engendrée depuis purchases.html, exécutait ce script sur des éléments
   absents : « Cannot read properties of null ».

   Celui-ci ne connaît aucun identifiant. Il prend les contrôles du bloc
   .filters et les applique au premier tableau qui suit. Sans bloc
   .filters, il ne fait rien — c'est le cas sur les vingt autres pages.
   ══════════════════════════════════════════════════════════════════ */
(function () {
    'use strict';

    var bloc = document.querySelector('.filters');
    if (!bloc) { return; }

    var table = document.querySelector('.panel table.data');
    if (!table) { return; }

    var lignes = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    var listes = Array.prototype.slice.call(bloc.querySelectorAll('select'));
    var cherche = bloc.querySelector('input[type="search"]');
    var compte = document.getElementById('f-compte');

    function appliquer() {
        var criteres = listes
            .filter(function (l) { return l.selectedIndex > 0; })
            .map(function (l) { return l.value.toLowerCase(); });
        var texte = cherche ? cherche.value.trim().toLowerCase() : '';
        var n = 0;

        lignes.forEach(function (tr) {
            var contenu = tr.textContent.toLowerCase();
            var ok = criteres.every(function (c) { return contenu.indexOf(c) !== -1; })
                  && (!texte || contenu.indexOf(texte) !== -1);
            tr.hidden = !ok;
            if (ok) { n += 1; }
        });

        if (compte) {
            compte.textContent = n === 0 ? 'Aucune ligne ne correspond aux filtres'
                               : n === 1 ? '1 ligne affichée'
                               : n + ' lignes affichées';
        }
    }

    listes.forEach(function (l) { l.addEventListener('change', appliquer); });
    if (cherche) { cherche.addEventListener('input', appliquer); }
    appliquer();
}());
