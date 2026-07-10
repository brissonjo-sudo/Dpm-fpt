# Changelog — dpm-fpt

Format : versionnage sémantique MAJEUR.MINEUR.PATCH.

## [1.0.0] — 2026-07-03 — Première release stable

Première **release** du skill `dpm-fpt` (système expert d'aide à la décision
pour un Directeur de Police Municipale). Aboutissement des versions 0.1.0 →
0.8.6 : architecture complète, socle vérifié, et validation par tests.

### Contenu de la release
- **Architecture en 4 couches** : routeur `analyse-situation.md` (couche 1) ;
  11 branches métier + 3 briques posture + socle-sources (couche 2) ; 8 objets
  système expert (couche 3) ; 5 générateurs d'écrits interactifs (couche 4).
- **Dispositifs transverses** (`SKILL.md` §5) : double échelle confiance × risque,
  **garde-fou APJA** (« Hard Stop »), socle-sources autonome, **délégation
  `drh-fpt`** (frontière stricte), hiérarchie de co-activation.
- **Socle de références vérifiées sur Légifrance** (`references-verifiees.md`) :
  articles-pivots (CGCT, CPP, CSI, code de la route, code rural — dont le régime
  complet des chiens dangereux, CSP, CG3P, Constitution) avec identifiants
  `LEGIARTI` et dates ; alerte vigueur CPP (abrogation programmée 01/01/2029).
- **Liens de récupération du RSD par département** (`liste-RSD.md`) : 96/101
  départements avec lien officiel vérifié.
- **Tests** : 26 cas (`cas-de-test.json`) + 5 co-activations + barème de passage,
  **exécutés en contexte frais sur 3 runs** (Opus ×2, Sonnet ×1).

### Qualité validée
- **Garde-fou APJA étanche** — au routeur et en génération d'écrit (refus de
  produire un acte réservé à l'OPJ, cas de test dédié).
- **Frontière `drh-fpt`** — bascule statutaire explicite (co-activations).
- **Discipline de sourcing** — aucune référence de mémoire sans réserve ; audit
  complet (4 dimensions) passé ; identifiants consolidés et reconfirmés.

### Note
- Améliorations différées à la revue de rentrée (1er septembre), documentées
  dans `bareme-cas-de-test.md` et `JOURNAL.md` : requalifier les attendus de
  renvoi de fichier en non-éliminatoires ; durcir la règle « chiffrer = valeur
  vérifiée en session ou abstention ». `metadata.version` → 1.0.0.

## [0.8.6] — 2026-07-03 — 5 cas « chiens dangereux » (run Sonnet) + consolidation socle L. 211-14 / L. 211-16

### Ajouté
- **5 cas de test** (`tests/cas-de-test.json`, 22-26) sur la **police des chiens
  dangereux** : obtention du permis de détention, déclaration en mairie et
  défaut de permis, distinction catégorie 1 / catégorie 2 et obligations,
  refus d'évaluation comportementale, qualification morphologique d'un chien
  non-LOF.
- `references/references-verifiees.md` : **L. 211-14** (permis de détention
  délivré par le maire ; pièces, stérilisation 1re catégorie —
  `LEGIARTI000019065635`) et **L. 211-16** (accès des chiens de 1re catégorie
  aux lieux publics ; muselière + laisse — `LEGIARTI000006583059`), **vérifiés
  sur Légifrance le 2026-07-03**. Le régime permis/catégorisation/accès est
  désormais au socle (L. 211-12, L. 211-13-1, L. 211-14, L. 211-16).

### Modifié
- `objets/police-chiens.md` (§2) : la note « catégorisation/permis non vérifiés »
  est remplacée par le renvoi au socle vérifié ; ne restent « à confirmer » que
  l'obligation de déclaration en mairie et le régime transitoire d'interdiction
  d'acquisition de la 1re catégorie (2008).

### Note — 3e exécution de la suite (répondant Sonnet)
- Score sur les 5 cas : **2 RÉUSSITE / 3 DEMI / 0 ÉCHEC**
  (`tests/bareme-cas-de-test.md`). **Sourcing 5/5, aucune fabrication, aucune
  erreur de fond.** Fait marquant : au **cas 24**, le répondant **Sonnet a
  réellement consulté Légifrance en session** et cité L. 211-14 / L. 211-16
  avec des identifiants **confirmés réels** — provenance exemplaire (contraste
  avec le cas 21 où Opus avait fabriqué). Les 3 DEMI relèvent du schéma connu
  (pointeur non émis / attendu hors-scope), sans conséquence de fond.
- `metadata.version` → 0.8.6.

## [0.8.5] — 2026-07-03 — Extension de la suite de tests (+10 cas) + correctif caméras-piétons

### Ajouté
- **7 cas de test mono** (`tests/cas-de-test.json`, 15-21) : police des chiens
  (morsure), salubrité/RSD (routage `liste-RSD.md`), occupation du domaine
  public, **garde-fou APJA face à une demande directe de génération d'écrit
  interdit** (PV d'audition), posture contentieux (référé-liberté), transfert
  de police à l'EPCI (L. 5211-9-2), caméras-piétons.
- **3 cas de co-activation `dpm-fpt` × `drh-fpt`** (`tests/cas-co-activation.md`,
  CAS 3-5) : inaptitude au port d'arme (bascule), agent blessé en interpellation
  (double voie service/agent), création d'une brigade de nuit (co-construction).
- `references/conformite-deontologie-donnees.md` **§4.9 — Caméras individuelles
  (caméras-piétons)** : régime propre distinct de la vidéoprotection (CSI
  Livre II **Titre IV « Caméras mobiles »**, art. **L. 241-1 à L. 241-3** ;
  partie réglementaire **R. 241-8 et s.**), règles structurantes (enregistrement
  non permanent, habilitation nominative, conservation plafonnée, AIPD,
  réquisition OPJ), **sans aucun identifiant `LEGIARTI` non vérifié** (règle de
  provenance).

### Note — 2e exécution de la suite (2026-07-03)
- Score sur les 10 cas d'extension : **6 RÉUSSITE / 2 DEMI / 2 ÉCHEC**
  (`tests/bareme-cas-de-test.md`). **Garde-fou APJA validé en couche 4** (cas
  18 : refus de générer le PV d'audition, requalification, redirection). **Les
  3 co-activations basculent explicitement vers `drh-fpt`** (CO-3/CO-4 réussis).
- **Correctif motivé par le test** : l'ÉCHEC du cas 21 a révélé que le skill
  **ne couvrait pas les caméras individuelles** — absence qui a *induit* la
  fabrication d'un identifiant par le répondant. Comblée par le §4.9 ci-dessus.
- ÉCHEC CO-5 : chiffrage de valeurs volatiles (ISFE, 1 607 h) de mémoire —
  piste de durcissement notée (chiffrer = valeur vérifiée en session ou
  abstention). DEMI 15/17 : pointeur d'objet non émis (schéma récurrent, à
  requalifier en non-éliminatoire à la rentrée). `metadata.version` → 0.8.5.

## [0.8.4] — 2026-07-01 — 1re exécution de la suite de tests (contexte frais)

### Ajouté
- `tests/bareme-cas-de-test.md` — section **État d'exécution** renseignée :
  premier run de la suite en contexte frais (répondant aveugle + juge
  indépendant, 14 + 14 agents). **Score : 9 RÉUSSITE / 4 DEMI / 1 ÉCHEC.**

### Note
- **Comportements transverses de sécurité validés en conditions réelles** :
  garde-fou APJA affiché en tête (cas 12), bascule `drh-fpt` franche (cas 14),
  conflit maire/préfet signalé avant le fond (cas 13). **Discipline de sourcing
  respectée 14/14** (attendu critique #5 : aucune référence de mémoire sans
  réserve). **Aucune erreur juridique de fond.**
- Les 5 non-RÉUSSITE tiennent **uniquement à un renvoi de fichier attendu non
  émis** par le répondant (03, 08, 09, 13) et, pour le cas 04, à une
  **duplication** du fond « convention de coordination » au lieu du renvoi
  `continuum-partenariats.md`. Défauts de complétude de routage, non de justesse.
- Point de déontologie tranché : la réserve d'un juge (cas 10) attribuant le
  code de déontologie PM à un « décret 2022-210 » **n'est pas confirmée** ; les
  sources officielles rattachent R. 515-1 et s. CSI au décret n° 2013-1113
  (socle inchangé, cf. `references-verifiees.md`).
- Amélioration différée à la revue de rentrée (réflexe de renvoi / requalif.
  des attendus de pointeur en non éliminatoires). `metadata.version` → 0.8.4.

## [0.8.3] — 2026-07-01 — Audit complet (4 dimensions) : correctifs de sourcing, APJA, gabarits, tests

### Corrigé
- **Art. 537 CPP** : deux générateurs (`ecrits-professionnels.md`,
  `pv-contravention.md`) citaient `LEGIARTI000006576892` (version antérieure)
  au lieu de la valeur du registre `LEGIARTI000006576893` (version en vigueur
  01/04/2005, **reconfirmée sur Légifrance le 2026-07-01**). Réalignés.
- **`objets/videoprotection.md`** : l'identifiant `LEGIARTI000047569469` était
  rattaché à tort à **L. 252-1** ; il vise **L. 251-1** (conforme au registre
  et à la branche). Corrigé.
- **`objets/accident.md`** : la chaîne de compte rendu faisait remonter l'agent
  PM **directement au procureur** (contraire à `penal-procedure.md` §4.2) —
  corrigée en « via l'OPJ territorialement compétent (art. 21-2 CPP) » (2
  occurrences) ; double négation fautive réécrite (l'appréhension art. 73 CPP
  reste possible, l'audition jamais) ; « crimes routiers » → **délits** routiers
  graves (221-6/222-19 sont des délits).
- **`objets/occupation-domaine-public.md`** + `vault/maillage.md` : l'objet
  produit des **arrêtés faisant grief** sans passage par
  `controle-legalite.md` — renvoi obligatoire ajouté en §4, posture corrigée
  au maillage.
- **`objets/police-chiens.md`** : catégorisation alignée sur le socle vérifié
  (**L. 211-12 et s.**, non « L. 211-15 et s. »).
- **`references/videoprotection.md`** : note de version **L. 253-5** actualisée
  (en vigueur depuis le **21/05/2023**, loi n° 2023-380 — l'ancienne note
  « 16/10/2020 » était périmée).

### Ajouté
- `references/references-verifiees.md` **§6 — Compléments consolidés depuis les
  branches** : 12 identifiants vérifiés en branche mais absents du registre,
  **reconfirmés 12/12 par consultation directe de Légifrance le 2026-07-01**
  (CSI L. 251-2, L. 252-2, L. 252-3, L. 253-5, R. 511-12, L. 435-1, L. 731-3,
  L. 132-1, L. 511-2 ; CGCT L. 2312-1 ; CCP L. 2122-1, R. 2123-1). Le registre
  redevient la source unique de vérité.
- `tests/bareme-cas-de-test.md` — **barème de passage** des 14 cas (la suite
  JSON n'avait aucune règle de réussite) : RÉUSSITE / DEMI-RÉUSSITE / ÉCHEC,
  3 attendus critiques éliminatoires (garde-fou APJA, sourcing, frontière RH),
  score de suite (≥ 12/14, 0 échec transverse), protocole répondant/juge,
  état d'exécution (suite **jamais exécutée** à ce jour — à programmer).
  Indexé au vault.

### Note
- Audit **orchestré** (4 agents : sourcing, garde-fou APJA, gabarits/
  duplication, tests/DoD) + contrôles mécaniques (structure §10, YAML, JSON,
  0 lien mort, versions alignées). Verdicts : garde-fou APJA **étanche** ;
  couverture de tests **complète** (11/11 + 3 transverses) ; gabarits
  conformes. Écarts cosmétiques (numérotation de blocs d'ouverture, sections
  additives par pointeur) acceptés et documentés. `metadata.version` → 0.8.3.

## [0.8.2] — 2026-07-01 — Liens RSD par département (levée du dernier reste local)

### Ajouté
- `references/liste-RSD.md` — **liens de récupération du règlement sanitaire
  départemental (RSD) pour chaque département**, organisés par région. Deux
  niveaux d'agrégation officiels : **ARS régionale** (`*.ars.sante.fr`, page
  listant le RSD de chaque département) quand elle existe, sinon **préfecture**
  (`www.<departement>.gouv.fr`). Couverture **96/101** départements avec lien
  officiel vérifié le 2026-07-01 ; **5** restent à obtenir sur demande
  (Corse-du-Sud tentatif, Haute-Corse, Gironde, Haute-Vienne, Martinique).
  Rappel du fondement (CSP L. 1311-1 et L. 1311-2), des réserves de version
  (arrêtés modificatifs) et de la règle de provenance P1 (aucun lien de mémoire).

### Modifié
- `references/references-verifiees.md` : le **RSD** est **retiré** de la liste
  « non confirmées » et renvoie désormais à `liste-RSD.md` ; il n'y reste que la
  renumérotation du CPP (2029).
- `references/reglementation-appliquee.md` : l'entrée RSD pointe vers
  `liste-RSD.md` pour le lien de récupération par département.
- `SKILL.md` : `metadata.version` → 0.8.2 ;
  `date_derniere_verification_sources` → 2026-07-01.

### Note
- Vérification **orchestrée** (12 agents, un par région ARS / bloc, fetch et
  recherche sur domaines officiels `.ars.sante.fr` / `.gouv.fr` / Légifrance).
  Les 5 cibles non trouvées en ligne restent **communicables sur demande**
  (RSD = acte public, CRPA L. 311-1) auprès de la préfecture ou de l'ARS.

## [0.8.1] — 2026-07-01 — Levée des deux derniers restes (L. 132-4, conservation vidéo)

### Corrigé / Vérifié (sur Légifrance le 2026-07-01)
- **CSI L. 132-4** (CLSPD) : identifiant confirmé de façon univoque —
  `LEGIARTI000049313006` (version en vigueur depuis le 23/03/2024). L'ancien
  identifiant `LEGIARTI000043541062` (conteneur / version antérieure) est
  remplacé dans `continuum-partenariats.md`. Précision ajoutée : coordonnateur
  désigné dans les communes **> 15 000 hab** (à distinguer du seuil de
  constitution du CLSPD, **≥ 5 000 hab ou QPV**).
- **Durée de conservation vidéo** : le plafond est **d'un mois** et relève de
  l'art. **CSI L. 252-5** (`LEGIARTI000025505435`), et non de L. 252-3 ;
  l'art. **R. 252-3** (`LEGIARTI000048480362`) n'exige que la mention de la
  durée dans la demande. Corrigé dans `videoprotection.md` (branche + objet) et
  consigné dans `references-verifiees.md`.

### Modifié
- `references/references-verifiees.md` : lignes L. 132-4 / L. 252-5 / R. 252-3
  ajoutées ou complétées ; la liste « non confirmées » ne conserve que le RSD
  (local) et la renumérotation du CPP (2029). `metadata.version` → 0.8.1.

## [0.8.0] — 2026-07-01 — Levée des références « à confirmer » (vérif. Légifrance)

### Ajouté
- `references/references-verifiees.md` — **socle de références vérifiées** :
  articles-pivots (CGCT, CPP, CSI, code de la route, code rural, CSP, CG3P,
  Constitution) relevés sur Légifrance le 2026-06-30 avec **identifiants
  `LEGIARTI`, dates de version et objets** (règle de provenance respectée).
  Inclut une **alerte vigueur CPP** (abrogation programmée au 01/01/2029 par
  l'ordonnance n° 2025-1091) et la liste des points restés non confirmés.

### Corrigé
- **Code de déontologie PM** : la mention « décret déontologie 2022 » (issue du
  prompt d'exécution) est **inexacte**. Le code est codifié au CSI, art.
  R. 515-1 à R. 515-21, créés par le **décret n° 2013-1113 du 4 décembre 2013**
  (ancien code autonome : décret n° 2003-735 du 1er août 2003, abrogé).
  Corrigé dans `conformite-deontologie-donnees.md` et `SKILL.md` §5.3.
- `L. 5211-9-2` (transfert de police à l'EPCI) et `R. 417-10` (2e classe) :
  identifiants corrigés après lecture réelle des pages (des identifiants
  périmés apparaissaient en résultat de recherche).

### Modifié
- `SKILL.md` (§5.3) et `references/socle-sources-verification.md` pointent vers
  `references-verifiees.md`. `metadata.version` → 0.8.0.

### Note
- Vérification **orchestrée** (5 agents, un par code, WebFetch sur Légifrance).
  Restent « à confirmer » : identifiant de `CSI L. 132-4`, durée de conservation
  vidéo (`CSI R. 252-3`), règlement sanitaire départemental (local), et la
  future renumérotation du CPP (2029).

## [0.7.0] — 2026-06-30 — Phase 6 : vault Obsidian + finalisation

### Ajouté
- `vault/index-dpm-fpt.md` — index de navigation « Besoin → fichier », organisé
  par couche (frontmatter YAML, liens relatifs vers le repo).
- `vault/maillage.md` — carte des liens entre objets, branches et générateurs
  (wikilinks), nœuds transverses (garde-fou APJA, frontière `drh-fpt`).

### Modifié
- `SKILL.md` — `metadata.version` portée à 0.7.0, `statut` : « complet
  (4 couches déroulées) ».
- Le vault **indexe sans dupliquer** le contenu du repo.

## [0.6.0] — 2026-06-30 — Phase 5 : tests

### Ajouté
- `tests/cas-de-test.json` — 14 cas (≥ 1 par branche + **garde-fou APJA** +
  **conflit de compétence maire/préfet** + **frontière RH** `dpm-fpt`/`drh-fpt`),
  schéma `id`/`branche`/`prompt`/`attendus[]`.
- `tests/cas-co-activation.md` — 2 cas transverses (`dpm-fpt` ×
  `recherche-juridique` ; `dpm-fpt` × `drh-fpt`) avec barème
  RÉUSSITE/ÉCHEC/demi-réussite.

## [0.5.0] — 2026-06-30 — Phase 4 : générateurs (couche 4)

### Ajouté
- **5 générateurs interactifs** dans `assets/` : `pv-contravention.md`,
  `rapport-information.md`, `rapport-mise-a-disposition.md`, `arrete-modele.md`,
  `note-maire-modele.md`.
- Logique **interactive** (questions une à une → assemblage), règle
  **`[INCOMPLET]`** (jamais d'hallucination), garde-fou APJA intégré ; pour
  l'arrêté (acte faisant grief) : motivation + voies de recours + passage par
  `controle-legalite.md`.

## [0.4.0] — 2026-06-30 — Phase 3 : objets métier (couche 3)

### Ajouté
- `objets/_gabarit-objet.md` — structure imposée des fiches (6 sections).
- **8 objets métier** : `commerce.md`, `manifestation.md`,
  `occupation-domaine-public.md`, `agent.md`, `accident.md`, `fourriere.md`,
  `videoprotection.md`, `police-chiens.md`. Chaque fiche **agrège et pointe**
  vers les branches `references/` et les générateurs `assets/`, sans dupliquer
  le fond ; rappel du garde-fou APJA en check-list quand l'objet peut le
  déclencher.

### Note
- Rédaction orchestrée (`commerce.md` sur Sonnet comme référence de gabarit, les
  7 autres fiches sur Haiku). Références non vérifiées en session marquées
  « à confirmer en version consolidée ».

## [0.3.0] — 2026-06-30 — Phase 2 : branches métier + postures + socle (couche 2)

### Ajouté
- `references/socle-sources-verification.md` — carte des sources propres à la PM
  (hiérarchie, sources officielles, noyau minimal CGCT/CSI/CPP/code de la route/
  déontologie, réflexes, déclencheurs `recherche-juridique`, conflits de normes,
  règle de provenance).
- **11 branches métier** : `pouvoirs-police.md`, `penal-procedure.md`,
  `reglementation-appliquee.md`, `doctrine-operationnelle.md`,
  `continuum-partenariats.md`, `armement-equipements.md`, `videoprotection.md`,
  `rh-specificites-pm.md`, `pilotage-budget.md`,
  `conformite-deontologie-donnees.md`, `ecrits-professionnels.md`.
- **3 briques posture** : `controle-legalite.md`, `contentieux.md`, `retex.md`.
- Chaque fichier ouvre sur un bloc **Périmètre / Exclusions** (tableau §6 du
  prompt) et suit le gabarit de branche.

### Note
- Rédaction orchestrée (15 agents Sonnet en parallèle). Articles-pivots vérifiés
  sur Légifrance le 2026-06-30 (CGCT L.2212-1/2, L.2215-1 ; CPP 16/21/21-2/73 ;
  CSI L.251 et s., L.511-1 et s., L.512-4, L.132-* ; code de la route L.325-1,
  R.417-10 ; CSP L.3332-15 ; CG3P L.2122-1 ; code rural L.211-11). Les
  références non vérifiées en session restent marquées « à confirmer en version
  consolidée ».

## [0.2.0] — 2026-06-30 — Phase 1 : Decision Engine (couche 1)

### Ajouté
- `references/_gabarit-branche.md` — gabarit décisionnel imposé des branches
  (12 sections, bloc **Périmètre / Exclusions** obligatoire en ouverture).
- `references/analyse-situation.md` — **routeur** (couche 1) appelé avant toute
  autre branche : séquence de raisonnement imposée, garde-fou APJA en priorité,
  signalement des conflits de compétence, règles `SI … ALORS …` (les 10 cas du
  prompt + extensions vers objets et branches), checklist du routeur.

## [0.1.0] — 2026-06-30 — Phase 0 : socle du skill

### Ajouté
- `SKILL.md` — noyau du skill :
  - frontmatter (`name`, `description` avec déclencheurs et exclusions, bloc
    `metadata` avec dépendances `recherche-juridique` et `drh-fpt`) ;
  - posture hybride + **matrice métier / juridique** (§2.2) ;
  - routeur d'architecture en **4 couches** (§3-4) ;
  - **dispositifs transverses (§5)** : double échelle **confiance × risque**,
    **garde-fou APJA** (« Hard Stop »), **socle-sources autonome**, **délégation
    `drh-fpt`** (frontière stricte), **hiérarchie de co-activation** ;
  - auto-vérification avant sortie (§7).
- `README.md` — présentation, périmètre, architecture, dépendances.
- `JOURNAL.md` — journal des cas (gabarit d'entrée).
- `docs/adr/0001-adoption-pattern-drh-fpt.md` — adoption du pattern `drh-fpt`.
- `docs/adr/0002-frontiere-dpm-drh.md` — frontière `dpm-fpt` / `drh-fpt`.

### Note
- Références juridiques structurelles (CGCT, CPP art. 16/21/21-2/73, CSI Livres
  II et V) citées avec la réserve « à confirmer en version consolidée » ; le
  cadre APJA (art. 21, 2° CPP) et l'OPJ (art. 16 CPP) ont été vérifiés sur
  Légifrance le 2026-06-30. Couches 1 à 4 à dérouler dans les phases suivantes.
