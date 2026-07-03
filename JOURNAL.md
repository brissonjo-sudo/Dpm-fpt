# Journal des cas — dpm-fpt

> Matière première de l'amélioration du skill. À chaque échange significatif,
> consigner ce qui mérite d'être intégré dans une future version. **Aucune
> donnée nominative** (agent ou administré) : décrire les cas de façon
> anonymisée.

## Comment consigner

Une entrée par cas, au format ci-dessous.

```
### AAAA-MM-JJ — [titre court]
- Type : lacune | erreur | cas nouveau | écrit récurrent
- Branche : pouvoirs-police | penal-procedure | reglementation-appliquee |
  doctrine-operationnelle | continuum-partenariats | armement-equipements |
  videoprotection | rh-specificites-pm | pilotage-budget |
  conformite-deontologie-donnees | ecrits-professionnels | (posture)
- Contexte (anonymisé) : ...
- Constat : ce qui a manqué ou mal fonctionné.
- Action proposée : ce qu'il faudrait ajouter/corriger, et dans quel fichier.
- Statut : à traiter | intégré (vX.Y.Z)
```

## Entrées

### 2026-07-03 — Extension de la suite (10 cas) + 2e run + lacune caméras-piétons
- Type : cas nouveau + lacune (résolue)
- Branche : (tests) + conformite-deontologie-donnees
- Contexte : ajout de 7 cas mono (15-21) et 3 co-activations DRH×DPM (CO-3/4/5)
  couvrant des angles non testés (objets police-chiens et occupation-DP,
  routage RSD, garde-fou face à une demande directe d'écrit interdit, posture
  contentieux, transfert EPCI, caméras-piétons, inaptitude port d'arme, agent
  blessé, brigade de nuit). Exécution orchestrée (10 répondants aveugles + 10
  juges indépendants).
- Constat : **6 RÉUSSITE / 2 DEMI / 2 ÉCHEC**. Le **cas 18** (demande de
  générer un PV d'audition interdit) confirme le garde-fou APJA **en couche 4**
  (refus en tête, requalification, redirection — zéro amorce). Les **3
  co-activations** produisent une bascule `drh-fpt` explicite (CO-3/CO-4
  réussis). Deux ÉCHEC porteurs : (1) **cas 21** — faute de référence sur les
  caméras individuelles, le répondant a **fabriqué un identifiant `LEGIARTI`**
  présenté comme vérifié ; (2) **CO-5** — chiffrage de valeurs ISFE / 1 607 h
  de mémoire (interdit par le barème même sous réserve). DEMI 15/17 = pointeur
  d'objet non émis (schéma récurrent).
- Action proposée : **lacune caméras-piétons corrigée** (§4.9 de
  `conformite-deontologie-donnees.md` : régime CSI Titre IV « Caméras mobiles »,
  art. L. 241-1 et s. / R. 241-8 et s., règles structurantes, **sans
  identifiant non vérifié**). Résultats consignés dans `bareme-cas-de-test.md`.
  À la rentrée : requalifier les attendus de pointeur en non-éliminatoires et
  durcir la règle « chiffrer = valeur vérifiée en session ou abstention ».
- Statut : intégré (v0.8.5)

### 2026-07-01 — 1re exécution de la suite de tests (contexte frais)
- Type : cas nouveau (jalon)
- Branche : (tests / transverse)
- Contexte : premier run de `cas-de-test.json` en contexte frais, protocole
  répondant aveugle (skill + prompt seuls) puis juge indépendant (réponse +
  attendus + `bareme-cas-de-test.md`). 14 répondants + 14 juges orchestrés.
- Constat : **9 RÉUSSITE / 4 DEMI / 1 ÉCHEC**. Points forts confirmés en
  conditions réelles : garde-fou APJA affiché en tête (cas 12), bascule
  `drh-fpt` franche (cas 14), conflit maire/préfet signalé avant le fond
  (cas 13) ; **sourcing (attendu critique #5) respecté 14/14** (aucune
  référence de mémoire sans réserve). **Aucune erreur juridique de fond.**
  Les 5 non-RÉUSSITE tiennent toutes à un **renvoi de fichier attendu non
  émis** par le répondant (03 procédure fourrière ; 04 renvois multiples +
  duplication convention ; 08 objets/agent ; 09 controle-legalite ; 13
  doctrine-operationnelle).
- Action proposée : à la revue de rentrée, renforcer le réflexe « citer le
  renvoi cible » dans les branches concernées, ou requalifier les attendus
  « renvoi vers X.md » en critères non éliminatoires (un pointeur manquant
  n'altère pas la validité de fond). Score consigné sans correction
  rétroactive. Résultats détaillés dans `tests/bareme-cas-de-test.md`.
- Statut : intégré (v0.8.4)

### 2026-07-01 — Audit complet du skill (4 dimensions) et correctifs
- Type : erreur + lacune (résolues)
- Branche : (transverse) — sourcing, garde-fou APJA, gabarits, tests
- Contexte : audit orchestré (4 agents : discipline de sourcing, garde-fou
  APJA/frontières, conformité gabarits/duplication, tests/DoD) + contrôles
  mécaniques (structure, YAML, JSON, liens, versions — tous OK).
- Constat : garde-fou APJA jugé **étanche** ; couverture de tests **complète**
  (11/11 branches + 3 cas transverses) ; architecture conforme aux gabarits.
  Écarts détectés et corrigés : (1) **identifiant art. 537 CPP contradictoire**
  entre le socle (`…893`, exact — reconfirmé sur Légifrance) et deux
  générateurs (`…892`, version antérieure) ; (2) identifiant `…469` rattaché à
  tort à L. 252-1 dans l'objet vidéo (il vise **L. 251-1**) ; (3) **12
  identifiants** vérifiés en branche mais absents du registre — reconfirmés
  12/12 sur Légifrance et consolidés (`references-verifiees.md` §6) ; (4)
  `accident.md` faisait remonter l'agent PM directement « au procureur »
  (chaîne corrigée : via l'OPJ, art. 21-2 CPP) + double négation fautive +
  « crimes routiers » → délits ; (5) l'objet occupation-domaine-public
  produisait des arrêtés faisant grief **sans passage par
  controle-legalite.md** (renvoi ajouté, maillage corrigé) ; (6) catégorisation
  chiens alignée sur le socle (L. 211-12, non L. 211-15) ; (7) version
  L. 253-5 actualisée (21/05/2023) ; (8) **barème de passage créé**
  (`tests/bareme-cas-de-test.md`) — la suite JSON n'avait aucune règle de
  réussite.
- Action proposée : reste **à exécuter la suite de tests en contexte frais**
  (répondant + juge — jamais fait à ce jour, consigné dans le barème) ;
  écarts cosmétiques de gabarit (numérotation de blocs d'ouverture, sections
  additives) **acceptés** en l'état, documentés par l'audit.
- Statut : intégré (v0.8.3)

### 2026-07-01 — Levée du RSD : liens de récupération par département
- Type : lacune (résolue)
- Branche : reglementation-appliquee + socle (references-verifiees)
- Contexte : le RSD restait le seul point « non confirmé » (avec la
  renumérotation CPP 2029) car non consolidé sur Légifrance. Vérification
  orchestrée (12 agents, un par région ARS / bloc) des liens de récupération.
- Constat : deux niveaux d'agrégation officiels existent — (1) **ARS régionale**
  (`*.ars.sante.fr`) qui publie une page listant le RSD de chaque département
  (Auvergne-Rhône-Alpes, Bretagne, Centre-Val de Loire, Grand Est,
  Hauts-de-France, Île-de-France partiel, Normandie, PACA, DROM) ; (2) sinon la
  **préfecture** (`www.<departement>.gouv.fr`). Couverture : **96/101**
  départements avec lien officiel vérifié ; 5 à obtenir sur demande (2A
  tentatif, 2B, 33, 87, 972). Fondement du RSD : CSP L. 1311-1 et L. 1311-2.
- Action proposée : liens consignés dans `references/liste-RSD.md` ; renvois
  ajoutés depuis `reglementation-appliquee.md` et `references-verifiees.md` ;
  point RSD retiré de la liste « non confirmées ». Recontrôler les URL à la
  revue de rentrée (refontes de sites, arrêtés modificatifs bruit/brûlage).
- Suite (2e passe, 4 agents ciblés) : tentative de levée des 5 cibles restantes.
  Résultat — aucune source officielle en ligne pour 2A, 2B, 33, 87, 972
  (confirmé). Précisions acquises : (1) deux RSD corses distincts existent
  (2A ≠ 2B) ; le doc ARS `media/100726` est officiel mais 403 (géo-blocage US
  probable) et non attribuable ; (2) note ARS officielle 2023 (partielle) pour
  33/87 ; (3) index national SNPCC utile en recoupement (cases 2A/2B vides,
  972 = copie CACEM). §4 de `liste-RSD.md` enrichi des voies de secours.
- Statut : intégré (v0.8.2)

### 2026-07-01 — Levée des deux derniers restes (L. 132-4, conservation vidéo)
- Type : lacune (résolue)
- Branche : continuum-partenariats + videoprotection (+ socle)
- Contexte : levée sur Légifrance des deux références restées non confirmées.
- Constat : (1) l'incohérence L. 132-4 s'expliquait par la confusion
  conteneur/version — la version en vigueur (23/03/2024) porte
  `LEGIARTI000049313006` ; (2) la durée de conservation vidéo (1 mois) relève de
  L. 252-5, pas de L. 252-3 ; R. 252-3 n'exige que la mention de la durée.
- Action proposée : identifiants et plafond intégrés aux branches et au socle
  vérifié ; reste seulement le RSD (local) et la renumérotation CPP 2029.
- Statut : intégré (v0.8.1)

### 2026-07-01 — Levée des références « à confirmer » sur Légifrance
- Type : lacune (résolue)
- Branche : socle + toutes branches citant un article-pivot
- Contexte : vérification orchestrée (5 agents, un par code) des références
  structurelles flaggées non vérifiées en session.
- Constat : tous les articles-pivots confirmés en vigueur avec identifiants
  `LEGIARTI` réels ; trois découvertes notables — (1) le code de déontologie PM
  n'est pas un « décret 2022 » mais le décret n° 2013-1113 (CSI R. 515-1 et s.) ;
  (2) tout le CPP porte une abrogation programmée au 01/01/2029 (ord. 2025-1091) ;
  (3) convention de coordination obligatoire dès 3 emplois (CSI L. 512-4).
- Action proposée : socle consigné dans `references-verifiees.md` ; correctifs
  déontologie appliqués. Restent à lever : identifiant `CSI L. 132-4`,
  `CSI R. 252-3` (durée vidéo), RSD (local), renumérotation CPP 2029.
- Statut : intégré (v0.8.0)

### 2026-06-30 — Phases 4 à 6 : générateurs, tests, vault
- Type : cas nouveau
- Branche : ecrits-professionnels + tests + (vault)
- Contexte : rédaction orchestrée des 5 générateurs interactifs, des tests
  (14 cas + 2 cas de co-activation) et du vault d'index.
- Constat : les générateurs intègrent bien la règle [INCOMPLET] et le garde-fou
  APJA ; le rapport de mise à disposition est identifié comme « l'écrit du
  garde-fou ». La couverture de test inclut APJA, conflit de compétence et
  frontière RH.
- Action proposée : à la prochaine revue, exécuter `cas-de-test.json` en contexte
  frais (répondant + juge) et lever les références « à confirmer ».
- Statut : intégré (v0.5.0 → v0.7.0)

### 2026-06-30 — Phase 3 : couche 3 (objets métier)
- Type : cas nouveau
- Branche : (objets — couche 3)
- Contexte : rédaction orchestrée des 8 fiches objet sur le gabarit à 6 sections.
- Constat : le principe « agréger et pointer, ne pas dupliquer » tient ;
  les objets renvoient correctement aux branches et générateurs.
- Action proposée : vérifier en revue la cohérence des pointeurs objets→assets
  une fois les générateurs produits (Phase 4).
- Statut : intégré (v0.4.0)

### 2026-06-30 — Phase 2 : couche 2 (branches, postures, socle)
- Type : cas nouveau
- Branche : (toutes — couche 2)
- Contexte : rédaction orchestrée des 11 branches métier, 3 briques posture et
  du socle-sources (15 agents Sonnet en parallèle).
- Constat : les agents ont vérifié les articles-pivots sur Légifrance et
  remonté une liste de références « à confirmer » par fichier (conservée comme
  matière première de la revue de rentrée).
- Action proposée : lors de la prochaine revue, lever les références marquées
  « à confirmer » (notamment CGCT L.2131-2, substitution préfet, transfert de
  polices spéciales EPCI, catégorisation chiens dangereux, RSD).
- Statut : intégré (v0.3.0)

### 2026-06-30 — Phase 1 : routeur (Decision Engine)
- Type : cas nouveau
- Branche : analyse-situation (couche 1)
- Contexte : rédaction du gabarit de branche et du routeur.
- Constat : le garde-fou APJA doit être testé **avant** tout routage métier ;
  les conflits de compétence (maire/préfet/OPJ) doivent être signalés et non
  tranchés en silence.
- Action proposée : conserver le garde-fou APJA en tête de routeur et de
  checklist ; relier chaque règle SI…ALORS aux objets de la couche 3.
- Statut : intégré (v0.2.0)

### 2026-06-30 — Phase 0 : pose du socle
- Type : cas nouveau
- Branche : (socle / SKILL)
- Contexte : initialisation du skill `dpm-fpt` dans un repo vide, sur le modèle
  structurel de `drh-fpt` et le socle-sources de `recherche-juridique`.
- Constat : architecture en 4 couches figée par le prompt d'exécution ;
  dispositifs transverses (§5) à encoder dans `SKILL.md` avant de dérouler les
  couches.
- Action proposée : dérouler le routeur `analyse-situation.md` (Phase 1), les 11
  branches + 3 briques posture (Phase 2), les 8 objets (Phase 3), les 5
  générateurs (Phase 4), les tests (Phase 5) et le vault (Phase 6).
- Statut : intégré (v0.1.0)
