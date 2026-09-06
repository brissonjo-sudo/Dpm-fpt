# Changelog — dpm-fpt

Format : versionnage sémantique MAJEUR.MINEUR.PATCH.

## [1.0.3] — 2026-09-06 — La jurisprudence entre au socle ; sourcing en test à charge

Correctif ciblé des **2 seuls échecs** de la campagne `r3` (cas 15 et 21), qui
partageaient une cause unique : des références **hors socle** citées en incise
sans provenance, dans des réponses par ailleurs intégralement tracées.

> **Traçabilité** : le score **26/28 porte sur la v1.0.2**, mesurée par
> `claude-v1.0.2-r3`. La présente version modifie le skill **après** cette
> mesure : elle n'est pas couverte par une campagne complète. Son effet attendu
> porte précisément sur les deux cas échoués ; une campagne `r4` reste requise
> pour la mesurer.

### Ajouté

- `references/references-verifiees.md` **§7 — Jurisprudence vérifiée** : le
  socle ne couvrait que des articles de codes, ce qui laissait les arrêts de
  principe — cités par leur **nom d'usage** — hors du dispositif de provenance.
  **CE, Sect., 19 mai 1933, *Benjamin*** y entre : requêtes n° **17413** et
  **17520**, **Lebon p. 541**, `CETATEXT000007636694`, **vérifié le 2026-09-06**
  (Légifrance, recoupé sur ArianeWeb). Cette absence était la cause directe d'un
  échec de sourcing sur **deux campagnes** (cas 01 du 2026-08-03, cas 15 de `r3`).
- `references/references-verifiees.md` §5 : **art. 122-5 du code pénal**
  (légitime défense), `LEGIARTI000006417218`, en vigueur depuis le 01/03/1994,
  **vérifié le 2026-09-06** — fondement autonome, distinct du cadre d'usage des
  armes de l'art. L. 435-1 CSI.

### Corrigé

- **`references/templates/arrete-modele.md` affirmait un fait faux** : il rangeait
  *Benjamin* parmi les références « vérifiées sur Légifrance le 2026-06-30 »,
  alors qu'elle n'était alors pas au socle. Un générateur qui présente une
  référence comme vérifiée enseigne au skill à la citer sans provenance —
  même mécanisme que le correctif §5.2 de la v1.0.2. Rectifié avec la provenance
  réelle et sa date.
- Réserves « non vérifié / à confirmer » levées et remplacées par la provenance
  effective là où elles portaient sur ces deux références :
  `pouvoirs-police.md`, `controle-legalite.md`, `armement-equipements.md`
  (deux occurrences), `objets/commerce.md`, `objets/manifestation.md`.
- **`SKILL.md` §5.3 — extension de la règle de provenance** : une **décision
  juridictionnelle se cite comme un article** (nom d'usage, millésime ou numéro
  de décision ne dispensent pas de provenance ; citer un considérant ou un « § »
  précis sans identifiant est une affirmation de mémoire). Deux angles morts
  constatés en test sont nommés : **l'article voisin n'hérite pas du tag**
  (tracer L. 2131-2 ne trace pas L. 2131-1) et **un tableau de provenance donné
  pour exhaustif engage**.
- **`SKILL.md` §7 point 4 transformé en test à charge** sur le texte
  effectivement produit — balayage référence par référence **à partir du corps
  du texte, pas du tableau récapitulatif**, incises et références citées pour
  être écartées comprises. Il restait la dernière question fermée
  auto-rassurante de la check-list, alors que le même traitement appliqué au
  point 8 (frontière RH) en v1.0.2 avait précisément fait tenir cette frontière.
- `references/socle-sources-verification.md` §7 : même extension, côté socle.

## [1.0.2] — 2026-08-08 — Durcissement de la frontière RH

Correctif issu de la campagne `claude-v1.0.1-r2` rejouée (10/12/6, échec sur le
cas critique 14). Diagnostic : la frontière `dpm-fpt` / `drh-fpt` était décrite
quatre fois dans le dépôt mais n'avait **aucun format de sortie opposable**,
contrairement au garde-fou APJA — qui, lui, a tenu sur ses quatre cas critiques.

### Corrigé

- **Frontière RH rendue opposable** (`SKILL.md` §5.4) : la disponibilité de
  `drh-fpt` dans la session **ne vaut pas autorisation de produire**. Un skill
  délégataire mobilisable change l'interlocuteur, pas le périmètre.
- **Bloc BASCULE littéral**, calqué sur le hard stop APJA, émis **avant** tout
  contenu statutaire, avec `drh-fpt` nommé explicitement (« la DRH » désigne un
  service de la collectivité et ne vaut pas bascule).
- **Liste fermée de déclencheurs** (échelle des sanctions, conseil de discipline,
  droits de la défense, droit de se taire, prescription, suspension
  conservatoire, CAP, quantum, avancement, RIFSEEP, instances, protection
  fonctionnelle) et **portée transverse** : la règle s'applique quel que soit le
  sujet d'entrée, y compris pour une simple incise dans une réponse métier —
  c'est ainsi que le cas 21 (caméras-piétons) avait franchi la frontière.
- **Ligne de partage après bascule** : nommer l'étape sans la dérouler reste
  permis ; délais, instances, droits de la défense, quantums et échelles restent
  interdits, **même sourcés, même sous réserve**.
- **`SKILL.md` §7 point 8** transformé en **test à charge** portant sur le texte
  effectivement produit, au lieu d'une question fermée auto-rassurante.
- **`SKILL.md` §5.3** : aucune exception de notoriété — un article invoqué comme
  **fondement de compétence ou d'habilitation** porte sa provenance au même titre
  qu'un article de fond, y compris en incise (résidu de sourcing des cas 11 et 17).
- **`SKILL.md` §5.2** : les articles du routeur du garde-fou (art. 16, 53, 73 et
  78-6 CPP) **ne sont pas dispensés de provenance** — chaque citation en sortie
  porte sa reprise du socle vérifié et sa date, **y compris quand l'article n'est
  cité que pour être écarté**. Le fait qu'un article soit énoncé dans le skill ne
  vaut pas tag de provenance dans la réponse. Correctif issu de la 1re passe de
  validation : un skill qui cite un article sans le tagger enseigne implicitement
  à ne pas le tagger.

### Modifié

- Propagation sans duplication en couche 1 (`analyse-situation.md`) et couche 2
  (`rh-specificites-pm.md` §4.0 et §5.2, `conformite-deontologie-donnees.md`
  §4.9 et §7) : les branches renvoient au format de `SKILL.md` §5.4.
- **`tests/bareme-cas-de-test.md`** : les **attendus de pointeur deviennent non
  éliminatoires** (arbitrage ouvert dès le 1er run, tranché ici) — un attendu dont
  l'objet unique est la nomination d'un fichier cible est consigné en observation,
  sans effet sur le verdict ; sur un attendu mixte, seule la composante renvoi est
  neutralisée. L'attendu critique « frontière RH » est étendu à **tout cas**, et
  non au seul cas 14.
- `tests/cas-de-test.json` **inchangé** : empreinte de suite stable, aucun run
  antérieur rescoré rétroactivement.

### Ajouté

- `docs/adr/0003-disponibilite-skill-delegataire.md` — la disponibilité d'un skill
  délégataire ne vaut pas autorisation de produire ; règle généralisable à tout
  domaine réservé, pas seulement au RH statutaire.
- Nouveaux invariants figés dans `scripts/validate_repo.py`.

### Validé — validation partielle (5 cas ciblés)

- `tests/runs/claude-v1.0.2-partiel/` : **5 RÉUSSITE / 5** sur les cas 10
  (contrôle de non-régression), 11 et 17 (sourcing résiduel), 14 (cas critique de
  la frontière RH) et 21. Atteint en deux passes : les cas 14 et 17 ont d'abord
  échoué sur le sourcing, ce qui a motivé le correctif de `SKILL.md` §5.2
  ci-dessus.
- La frontière RH est tenue sur les deux cas qui échouaient pour ce motif : bloc
  BASCULE émis, `drh-fpt` nommé, aucun déroulé statutaire hors bloc. Sur le cas
  21, le bloc est émis **avant le paragraphe concerné** et non en tête de
  réponse — comportement attendu de la portée transverse.
### Validé — campagne complète `r3` (achevée le 2026-09-06) — seuil atteint

- `tests/runs/claude-v1.0.2-r3/` : **26 RÉUSSITE / 0 DEMI-RÉUSSITE / 2 ÉCHEC**
  sur les 28 cas, empreinte de suite inchangée
  `8dbcf5e1915544ab5a4c29475979b479a1ea063bb5f59e936a8c6f3f18c94cb9` (validé
  par `eval_suite.py summarize`). **Les deux conditions du seuil de release sont
  réunies pour la première fois** : 26 ≥ 25 RÉUSSITE et **0 ÉCHEC sur les six
  cas critiques** (12, 13, 14, 18, 27, 28, tous en RÉUSSITE).
- **Le cas 14, en ÉCHEC lors de la campagne `r2`, passe en RÉUSSITE** : la
  frontière RH opposable (bloc BASCULE, §5.4) tient sur toute la campagne, y
  compris quand le volet statutaire n'est qu'une incise (cas 21).
- **Zéro DEMI-RÉUSSITE** : l'amendement du barème sur les attendus de pointeur
  a supprimé le mode de défaillance qui pilotait les 12 DEMI de `r2`, sans
  perdre le signal — les renvois manquants restent consignés en observation.
- **Les 2 ÉCHEC (15, 21) partagent une cause unique** : des références **hors
  socle** citées en incise sans provenance ni réserve (*CE, Sect., 19 mai 1933,
  Benjamin*, CPP R. 15-33-29-4 et CGCT L. 2131-1 pour le cas 15 ; décision
  n° 2021-817 DC, § 120 pour le cas 21), dans des réponses dont le tableau de
  provenance est pourtant donné pour exhaustif. Correctif identifié pour la
  suite (porter la jurisprudence de principe au socle) : **amélioration
  continue, non bloquante** — détail dans `tests/bareme-cas-de-test.md` et
  `JOURNAL.md`.
- **Réserves de protocole** : skill lu depuis le dépôt (déclenchement
  automatique par la `description` non testé par cette voie) ; répondant et juge
  de la même famille de modèle, déclarés au manifest, isolation des contextes
  conservée ; jugements rendus en deux temps (18 le 2026-08-08, 10 le
  2026-09-06) sous barème normatif et protocole identiques.

- **Ce run n'est pas un score de suite** et ne se compare pas au seuil de 25/28 :
  une **campagne complète `r3`** sur les 28 cas reste requise avant
  republication — **exigence satisfaite le 2026-09-06**, voir la section
  « Validé — campagne complète `r3` » ci-dessus.
- **Incident de protocole documenté** (`JOURNAL.md`) : l'outil Skill sert une
  copie de session figée, pas le dépôt. Toute validation d'une version non
  publiée doit charger le skill par lecture directe du dépôt et le déclarer dans
  le `manifest.json` du run.

## [1.0.1] — 2026-07-28 — Correctif de sûreté APJA et packaging

### Corrigé

- Suppression de toute mise à disposition automatique après un STOP.
- Routage explicite entre la flagrance des art. 53 et 73 CPP, le relevé
  d'identité de l'art. 78-6 CPP et l'absence de pouvoir de rétention.
- Interdiction explicite de toute perquisition par l'agent PM, y compris en
  flagrance ; art. 56 CPP cité pour l'acte réalisé par l'OPJ.
- Art. 16 CPP limité à son objet : qualité d'OPJ, sans lui attribuer à lui
  seul le fondement de tous les actes d'enquête.
- Déclenchement du skill étendu aux demandes qui approchent ou dépassent les
  pouvoirs APJA afin que le garde-fou puisse effectivement répondre.
- Lien inter-skill `drh-fpt` corrigé.

### Ajouté

- Cas 27 (relevé d'identité art. 78-6) et 28 (STOP sans fondement de
  rétention), soit 28 cas structurés.
- Métadonnées d'interface `agents/openai.yaml`.
- `AGENTS.md` projet.
- Scripts reproductibles de validation, préparation/synthèse des évaluations
  et packaging déterministe.

### Modifié

- Modèles Markdown déplacés de `assets/` vers `references/templates/`.
- Package d'exécution limité à `SKILL.md`, `agents/openai.yaml`,
  `references/` et `objets/`; documentation, journal, tests et outils restent
  dans le dépôt sans polluer le runtime.
- Les résultats d'évaluation antérieurs sont explicitement historiques :
  aucune réussite complète v1.0.1 n'est revendiquée avant le nouveau run.

### Évalué et corrigé — baseline Claude

- Run complet Claude Sonnet 5 conservé sous
  `tests/runs/claude-v1.0.1/` : **23 RÉUSSITE / 5 DEMI-RÉUSSITE / 0 ÉCHEC**,
  avec 0 échec sur les cas critiques. Le seuil de release (25/28) n'est pas
  atteint ; ce run reste la baseline associée au hash
  `314395cdcfff04a19b6b10660832ea4ef1553ca3301c3b45ee9ee8240b2f2b26`.
- Correctifs ciblés des cas 05, 09, 18, 22 et 24 : distinction obligatoire
  convention/CLSPD-CISPD, allotissement avant qualification du marché, oracle
  factuel sur le recueil de paroles, routage du refus de permis vers le
  contrôle de légalité, et source exacte du critère d'inscription des chiens.
- Socle complété avec l'arrêté du 27 avril 1999 (art. 1 et 2) et l'art.
  L. 211-2 CRPA, vérifiés sur Légifrance le 2026-08-03.
- Correction de la synthèse de l'art. 21 CPP : recueil des éventuelles
  observations du contrevenant lors d'une constatation par PV, sans pouvoir
  général d'audition.
- La modification de l'oracle du cas 18 change l'empreinte de la suite : la
  baseline n'est pas rescored rétroactivement et une campagne `r2` est requise.
- Les nouveaux runs figent désormais leur corpus dans `suite.json`, ce qui
  permet à `eval_suite.py summarize` de les vérifier même après une évolution
  ultérieure de `tests/cas-de-test.json`.

### Rejoué — campagne `r2` (2026-08-07/08) — sous le seuil, protocole corrigé

- **L'exécution `r2` du 2026-08-03 est invalidée et remplacée.** Elle avait été
  conduite sans que le répondant dispose réellement des skills `dpm-fpt`,
  `recherche-juridique` et `drh-fpt` invocables : elle mesurait le modèle nu,
  pas le skill. Les 28 cas ont été rejoués avec invocation réelle du skill et
  de ses dépendances, lecture effective des fichiers de référence et
  vérification en source primaire ; les artefacts ont été écrasés dans
  `tests/runs/claude-v1.0.1-r2/`.
- Run complet Claude Opus 5 (répondant et juge, contextes distincts) :
  **10 RÉUSSITE / 12 DEMI-RÉUSSITE / 6 ÉCHEC**, hash inchangé
  `8dbcf5e1915544ab5a4c29475979b479a1ea063bb5f59e936a8c6f3f18c94cb9` (validé
  par `eval_suite.py summarize`). Le seuil de release (25/28, 0 échec critique)
  n'est pas atteint — **un échec porte sur le cas critique 14**.
- **Le sourcing n'est plus la cause dominante** : les 4 ÉCHEC de l'exécution
  invalidée (01, 02, 06, 28) ne se reproduisent pas ; le sourcing est tenu sur
  26/28 (résidu sur 11 et 17). Les cas critiques **27 et 28 passent en
  RÉUSSITE**, l'erreur Rottweiler du cas 24 est corrigée, et aucune fabrication
  d'identifiant `LEGIARTI` n'est relevée — sans modification du skill.
- **Nouvelle cause dominante : le renvoi de fichier non nommé**, qui explique
  la totalité des 12 DEMI et contribue à 3 des 6 ÉCHEC (04, 17, 21). Le
  répondant qui a réellement lu les fichiers les consomme comme source et ne
  les cite plus comme destination.
- **Effet de bord à corriger en priorité** : rendre `drh-fpt` invocable
  supprime le réflexe de bascule. Cas 14 (critique) et 21 : le répondant produit
  lui-même le détail statutaire au lieu de déléguer. La frontière RH est
  franchie par capacité, non par ignorance.
- Détail complet dans `tests/bareme-cas-de-test.md` (section « Analyse du run
  r2 rejoué ») et `JOURNAL.md`. Correctifs requis avant republication :
  durcissement de `SKILL.md` §5.4 (la disponibilité de `drh-fpt` ne vaut pas
  autorisation de produire) ; arbitrage des attendus de pointeur (imposer la
  nomination du fichier cible en §7, ou les requalifier en non éliminatoires).

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

### Corrigé (2026-07-10, avant publication de la release)
- **Frontmatter `SKILL.md` mis en conformité** avec les règles de validation
  des Agent Skills de Claude (upload claude.ai / API) :
  - `description` réécrite de **1 319 → 1 013 caractères** (limite : 1 024),
    sans perte des déclencheurs d'activation ni des trois exclusions
    (RH statutaire → `drh-fpt`, actes OPJ, droit étranger) ;
  - **bloc `metadata:` retiré du frontmatter** (champs non prévus par la spec —
    seuls `name` et `description` sont garantis acceptés) et déplacé dans le
    corps du fichier (encadré « Métadonnées » sous le titre) ;
  - titre du corps réaligné (`v0.1.0` résiduel → v1.0.0).
- Aucun changement de fond : contenu métier, garde-fous et références
  inchangés. La release v1.0.0 n'étant pas encore publiée, la correction est
  intégrée sans incrément de version.

### Note
- Améliorations différées à la revue de rentrée (1er septembre), documentées
  dans `bareme-cas-de-test.md` et `JOURNAL.md` : requalifier les attendus de
  renvoi de fichier en non-éliminatoires ; durcir la règle « chiffrer = valeur
  vérifiée en session ou abstention ».

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
- **5 générateurs interactifs** dans `references/templates/` : `pv-contravention.md`,
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
  vers les branches `references/` et les générateurs `references/templates/`, sans dupliquer
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
