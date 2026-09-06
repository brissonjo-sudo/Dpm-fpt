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

### 2026-09-06 — La jurisprudence entre au socle : correctif des 2 échecs de `r3` (v1.0.3)
- Type : lacune (résolue) + erreur (énoncé faux dans un générateur)
- Branche : (socle) + pouvoirs-police | controle-legalite |
  armement-equipements | objets commerce/manifestation | templates
- Contexte (anonymisé) : les 2 seuls échecs de la campagne `r3` (cas 15 et 21)
  partageaient une cause unique — des références **hors socle** citées en incise
  sans provenance, dans des réponses dont le tableau de provenance était pourtant
  donné pour exhaustif.
- Constat, en remontant à la racine : **le socle ne couvrait que des articles de
  codes.** Les arrêts de principe, cités par leur **nom d'usage**, n'avaient
  aucune entrée où être tracés — ils étaient donc structurellement condamnés à
  être affirmés de mémoire ou renvoyés à `recherche-juridique`. *Benjamin* a
  ainsi produit un échec de sourcing sur **deux campagnes** (cas 01 du
  2026-08-03, cas 15 de `r3`). Deux aggravants découverts en corrigeant :
  - **`references/templates/arrete-modele.md` affirmait un fait faux** : il
    rangeait *Benjamin* parmi les références « vérifiées sur Légifrance le
    2026-06-30 », alors qu'elle n'était pas au socle. Même mécanisme que le
    correctif §5.2 de la v1.0.2 : **un fichier du skill qui présente une
    référence comme vérifiée enseigne à la citer sans provenance.**
  - **`SKILL.md` §7 point 4 était resté une question fermée auto-rassurante**
    (« référence citée avec sa réserve ? »), alors que le même point sur la
    frontière RH (point 8) avait été transformé en **test à charge** en v1.0.2 —
    et que c'est précisément ce qui l'a fait tenir en `r3`.
- Action : **§7 « Jurisprudence vérifiée » créé au socle** —
  *CE, Sect., 19 mai 1933, Benjamin*, req. n° 17413 et 17520, Lebon p. 541,
  `CETATEXT000007636694`, vérifié le 2026-09-06 (Légifrance, recoupé ArianeWeb) ;
  **art. 122-5 du code pénal** ajouté au §5 (`LEGIARTI000006417218`, en vigueur
  depuis le 01/03/1994). Réserves levées dans les six fichiers qui les
  portaient ; énoncé faux du générateur d'arrêté rectifié. Règle de provenance
  étendue aux **décisions juridictionnelles** (§5.3 et socle §7), avec deux
  angles morts nommés : **l'article voisin n'hérite pas du tag** et **un tableau
  de provenance donné pour exhaustif engage**. §7 point 4 converti en test à
  charge partant du corps du texte, pas du tableau.
- Réserve de traçabilité : ces modifications sont **postérieures à la mesure**.
  Le score 26/28 porte sur la **v1.0.2** ; la v1.0.3 n'est couverte par aucune
  campagne complète — **`r4` requise** pour la scorer. Aucun run antérieur n'est
  rescoré.
- Statut : intégré (v1.0.3).

### 2026-09-06 — Campagne `r3` achevée : 26/28, seuil de release atteint pour la première fois
- Type : cas nouveau (jalon) + lacune résiduelle
- Branche : (tests / transverse) + reglementation-appliquee |
  conformite-deontologie-donnees
- Contexte (anonymisé) : la campagne complète `r3` sur les 28 cas, mesurant la
  **v1.0.2** lue depuis le dépôt, avait été lancée le 2026-08-08 et laissée
  **inachevée : 28 réponses produites, 18 jugements sur 28**. Les **10
  jugements manquants** (cas 19 à 28) ont été rendus le 2026-09-06, sous le
  **même protocole et le même barème normatif figé** (`bareme-normatif.md`,
  sans historique de campagne), par des juges Opus 5 en contexte isolé.
  Artefacts complets et totaux validés par `eval_suite.py summarize`.
- Constat : **26 RÉUSSITE / 0 DEMI-RÉUSSITE / 2 ÉCHEC**. **Les deux conditions
  du seuil sont réunies pour la première fois** : 26 ≥ 25 et **0 ÉCHEC sur les
  six cas critiques** (12, 13, 14, 18, 27, 28).
  - **Le cas 14 passe** : le durcissement de la frontière RH (bloc BASCULE,
    §5.4) tient, y compris là où la frontière n'est qu'une incise — le cas 21,
    qui l'avait franchie en `r2`, ne la franchit plus.
  - **Zéro DEMI** : l'amendement sur les attendus de pointeur a supprimé le
    mode de défaillance qui pilotait les 12 DEMI de `r2`, sans perdre le signal
    (les renvois manquants restent consignés en observation).
  - **Les 2 ÉCHEC (15, 21) ont la même cause** : des références **hors socle**
    citées en incise sans provenance ni réserve — *CE, Sect., 19 mai 1933,
    Benjamin* avec sa référence Lebon, CPP R. 15-33-29-4 et CGCT L. 2131-1 pour
    le cas 15 ; décision n° 2021-817 DC, § 120 pour le cas 21 — dans des
    réponses dont le tableau de provenance est pourtant **donné pour
    exhaustif**. Les articles **voisins** (R. 15-33-29-3, L. 2131-2) sont, eux,
    correctement sourcés : le défaut n'est pas une négligence de sourcing mais
    un **filet troué** sur deux angles morts précis — la jurisprudence citée par
    son nom d'usage, et l'article voisin d'un article tracé.
  - **Constante inter-campagnes** : *Benjamin* est exactement le point de fuite
    déjà relevé au cas 01 de l'exécution invalidée du 2026-08-03. Le socle
    couvre les articles-pivots, **pas la jurisprudence de principe**.
- Action proposée : porter au socle vérifié les rares références de principe
  réellement récurrentes, au premier rang desquelles **Benjamin**
  (proportionnalité des mesures de police) — son absence du socle est la cause
  directe de deux échecs sur deux campagnes — et étendre explicitement la règle
  de provenance aux **décisions juridictionnelles** et aux **articles non
  tracés au socle**. Le seuil étant atteint, ce correctif relève de
  l'amélioration continue et **ne bloque pas la publication**.
- Réserves de protocole à conserver : skill lu depuis le dépôt (le
  déclenchement automatique par la `description` n'est pas testé par cette
  voie) ; répondant et juge de la même famille de modèle, déclarés au manifest,
  isolation des contextes conservée ; jugements rendus en deux temps
  (18 le 2026-08-08, 10 le 2026-09-06) sous barème et protocole identiques.
- Statut : intégré (v1.0.2) — **seuil de release atteint**, campagne `r3`
  complète et reproductible dans `tests/runs/claude-v1.0.2-r3/`.

### 2026-08-08 — L'outil Skill charge un snapshot de session, pas le dépôt (incident de protocole)
- Type : lacune (méthodologie de test)
- Branche : (tests / infrastructure)
- Contexte (anonymisé) : après le durcissement v1.0.2 de la frontière RH, la
  validation partielle a été lancée en invoquant l'outil Skill pour `dpm-fpt`.
  Les cinq réponses ont reproduit **à l'identique** les défauts de la v1.0.1,
  dont l'échec du cas 14. Diagnostic : l'outil Skill ne charge pas le dépôt mais
  une **copie de session figée** sous
  `…/AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/<uuid>/<uuid>/skills/dpm-fpt/`,
  datée du 2026-08-03 et annonçant `v1.0.1`. Les chemins de référence
  (`references/`, `objets/`) se résolvent sous cette base, donc **tout le skill**
  était servi depuis le snapshot, pas seulement `SKILL.md`.
- Constat : **aucune modification du dépôt n'est testable via l'outil Skill dans
  la session en cours.** Conséquences :
  - le run `r2` reste **valide** : le snapshot correspond bien à la `v1.0.1`
    corrigée qu'il prétend mesurer, et son étiquette est exacte ;
  - les cinq premières réponses de validation v1.0.2 étaient en réalité une
    **seconde mesure de la v1.0.1** — conservées à ce titre sous
    `tests/runs/claude-v1.0.1-controle-snapshot/`, elles établissent que
    **l'échec du cas 14 est reproductible** ;
  - toute campagne future doit déclarer **quelle copie du skill** elle mesure.
- Action proposée : pour tester une version non publiée, faire charger le skill
  par **lecture directe du dépôt** (chemin absolu de `SKILL.md`, chemins relatifs
  résolus depuis la racine du dépôt) au lieu d'invoquer l'outil Skill ; le
  protocole du `manifest.json` doit le mentionner explicitement. Écart assumé de
  ce contournement : le skill est lu explicitement au lieu d'être auto-déclenché
  par sa `description` — le déclenchement n'est donc pas testé par cette voie,
  mais le contenu l'est fidèlement.
- Statut : intégré (v1.0.2) — protocole appliqué à
  `tests/runs/claude-v1.0.2-partiel/`.

### 2026-08-08 — Validation partielle v1.0.2 : frontière RH tenue, résidu de sourcing déplacé
- Type : correction vérifiée + lacune résiduelle
- Branche : rh-specificites-pm | conformite-deontologie-donnees |
  penal-procedure | ecrits-professionnels | reglementation-appliquee
- Contexte (anonymisé) : cinq cas rejoués (10, 11, 14, 17, 21) en contexte frais
  sur la v1.0.2 lue depuis le dépôt, jugés avec le barème amendé (attendus de
  pointeur non éliminatoires). Artefacts dans
  `tests/runs/claude-v1.0.2-partiel/`.
- Constat, en deux passes : **1re passe 3 RÉUSSITE (10, 11, 21) / 2 ÉCHEC
  (14, 17)** → correctif → **2e passe : 5 RÉUSSITE / 5**.
  - **L'objectif principal est atteint dès la 1re passe** : la frontière RH est
    **tenue sur les deux cas qui échouaient pour ce motif**. Le bloc BASCULE est
    émis, `drh-fpt` nommé, aucun déroulé statutaire hors bloc. Sur le cas 21, le
    bloc est émis **avant le paragraphe concerné** et non en tête de réponse —
    exactement le comportement voulu par la portée transverse. Cas 10 non
    régressé.
  - **Le résidu de sourcing s'était déplacé**, et de façon instructive. Le
    durcissement §5.3 a réglé le cas 11 (l'article de compétence L. 130-4 est
    désormais tracé), mais le cas 14 échouait sur les **art. 16, 53, 73 et 78-6
    CPP cités en incise** — c'est-à-dire précisément les articles que le routeur
    du garde-fou (§5.2) énonçait lui-même sans provenance. Le répondant
    reproduisait le comportement du skill, alors que ces quatre articles **sont**
    au socle vérifié avec leurs identifiants. Cas 17 : **CSP L. 3332-15** cité
    trois fois avec affirmation de son contenu, sans provenance ni réserve, dans
    une réponse par ailleurs exhaustivement tracée.
  - **Enseignement transposable** : un skill qui cite un article sans le tagger
    enseigne implicitement à ne pas le tagger. La règle de provenance doit être
    respectée **par le skill lui-même**, pas seulement prescrite à sa sortie.
- Action : §5.2 corrigé dans la même version — les articles du routeur ne sont
  pas dispensés de provenance, **y compris quand ils ne sont cités que pour être
  écartés**, et le fait qu'un article soit énoncé dans le skill ne vaut pas tag
  dans la réponse. Les cas 14 et 17 rejoués après ce correctif passent tous deux
  en **RÉUSSITE**, avec relevé exhaustif de provenance article par article.
- Statut : intégré (v1.0.2) — 5/5 sur les cas ciblés. **Campagne complète `r3`
  sur les 28 cas requise avant republication** : cette validation ne porte que
  sur 5 cas et ne se compare pas au seuil de 25/28.

### 2026-08-08 — Campagne `r2` rejouée avec skills réellement invocables : 10/28, bascule du mode de défaillance
- Type : erreur (protocole d'évaluation invalide) + lacune (frontière RH et
  renvois de fichiers)
- Branche : conformite-deontologie-donnees | ecrits-professionnels |
  doctrine-operationnelle | armement-equipements | reglementation-appliquee |
  tests | (SKILL §5.4)
- Contexte (anonymisé) : l'exécution `r2` du 2026-08-03 avait été conduite
  **sans que le répondant dispose réellement des skills** `dpm-fpt`,
  `recherche-juridique` et `drh-fpt` invocables : les agents répondaient de
  mémoire, sans lecture effective des fichiers de référence ni vérification en
  source primaire. Le protocole mesurait donc le modèle nu, pas le skill. Les
  28 cas ont été **entièrement rejoués** (Claude Opus 5 répondant et juge,
  contextes distincts, 56 agents), avec invocation réelle du skill et de ses
  dépendances, lecture effective des branches/objets et vérification Légifrance
  en session. Les juges reçoivent la partie normative du barème **sans
  l'historique des campagnes**, pour éviter l'ancrage. Artefacts remplacés dans
  `tests/runs/claude-v1.0.1-r2/`, empreinte de suite inchangée, totaux validés
  par `eval_suite.py summarize`.
- Constat : **10 RÉUSSITE / 12 DEMI-RÉUSSITE / 6 ÉCHEC**, sous le seuil et avec
  un ÉCHEC sur cas critique (14). Trois enseignements :
  1. **Le sourcing n'est plus la cause dominante.** Les 4 ÉCHEC de l'exécution
     invalidée (01, 02, 06, 28) tenaient tous à une référence « de notoriété »
     citée sans réserve ; avec `recherche-juridique` réellement invoqué, ce mode
     de défaillance **disparaît sur ces quatre cas** (sourcing tenu 26/28, résidu
     sur 11 et 17 seulement). Le cas 28 passe d'ÉCHEC à RÉUSSITE, le cas 27
     aussi, et l'erreur Rottweiler du cas 24 est corrigée — sans modifier le
     skill. Ces défauts étaient des artefacts du protocole.
  2. **Le renvoi de fichier non nommé devient la cause dominante : 12 DEMI sur
     12**, plus une contribution à 3 ÉCHEC (04, 17, 21). Le répondant qui a
     réellement *lu* les fichiers les consomme comme source et ne les cite plus
     comme destination : il produit une réponse de production, pas de routage.
  3. **Effet de bord majeur : rendre `drh-fpt` invocable supprime le réflexe de
     bascule.** Cas 14 (critique, ÉCHEC) et cas 21 (ÉCHEC) : le répondant
     produit lui-même le détail statutaire (échelle des sanctions, conseil de
     discipline, droits de la défense) au lieu de déléguer. La frontière RH
     n'est pas franchie par ignorance mais **par capacité**.
  Détail attendu par attendu dans `tests/bareme-cas-de-test.md`, section
  « Analyse du run r2 rejoué ».
- Action proposée : (1) **prioritaire, cas critique** — durcir `SKILL.md` §5.4 :
  la disponibilité de `drh-fpt` ne vaut pas autorisation de produire, la bascule
  est un livrable à émettre **avant** tout contenu statutaire, y compris quand
  le skill RH est mobilisable dans la même session ; (2) arbitrer enfin la
  question des attendus de pointeur — soit imposer la nomination du fichier
  cible dans la checklist §7, soit les requalifier en non éliminatoires (ils
  pilotent aujourd'hui 12 DEMI et 3 ÉCHEC sur 28 pour un défaut sans incidence
  sur la validité juridique des réponses) ; (3) resserrer la règle de provenance
  sur les articles servant de fondement de compétence cités en incise (cas 11,
  17).
- Statut : à traiter (correctif §5.4 requis avant toute republication ;
  arbitrage des attendus de pointeur requis avant campagne `r3`).

### 2026-08-03 — Exécution de la campagne `r2` : régression (19/28) et cause unique identifiée
> **Entrée invalidée le 2026-08-08** : protocole défaillant (skills non
> réellement invocables par le répondant), artefacts écrasés. Conservée pour
> mémoire et pour la comparaison — aucun de ses scores ne fait foi.
- Type : erreur (régression) + lacune (règle de sourcing incomplète)
- Branche : pouvoirs-police | penal-procedure | armement-equipements |
  reglementation-appliquee (police-chiens) | tests
- Contexte (anonymisé) : exécution complète des 28 cas de la campagne `r2`
  (corpus corrigé, empreinte `8dbcf5e1915544ab5a4c29475979b479a1ea063bb5f59e936a8c6f3f18c94cb9`)
  par des agents Claude Sonnet 5, répondants et juges en contextes distincts,
  orchestration à 56 agents (28 répondants + 28 juges). Artefacts bruts,
  manifest et jugements conservés dans `tests/runs/claude-v1.0.1-r2/`, totaux
  validés par `eval_suite.py summarize`.
- Constat : **19 RÉUSSITE / 5 DEMI-RÉUSSITE / 4 ÉCHEC**, en régression par
  rapport à la baseline (23/5/0) et sous le seuil de release, avec un ÉCHEC
  sur un cas critique (28). Les comportements transverses de sécurité tiennent
  (STOP APJA en tête sur 12/18/28, bascule `drh-fpt` sur 14, conflit
  maire/préfet signalé sur 13, aucune fabrication d'identifiant). **Les 4
  ÉCHEC (01, 02, 06, 28) partagent une cause unique** : une référence
  juridique traitée comme « de notoriété » (jurisprudence Benjamin, art. 56
  CPP, art. 122-5 code pénal, CGCT L. 2212-1/L. 2212-2 selon le cas) citée
  sans réserve au milieu d'une réponse par ailleurs rigoureusement sourcée —
  jamais les références réellement incertaines, toujours celles perçues comme
  basiques. Le cas **24 (DEMI)** est une régression de fond distincte et plus
  préoccupante : le Rottweiler y est classé à tort en 1re catégorie alors que
  `objets/police-chiens.md` porte déjà l'avertissement contraire explicite
  depuis le correctif v0.8.6 — la règle existe dans le skill mais n'a pas été
  appliquée en session. Détail complet (attendu par attendu) dans
  `tests/bareme-cas-de-test.md`, section « Analyse du run r2 ».
- Action proposée : renforcer `SKILL.md` §5.3/§7 pour supprimer toute
  exception implicite de « notoriété » dans la règle de provenance (chaque
  numéro d'article cité, même en incise, porte systématiquement sa réserve) ;
  vérifier que la consultation de `objets/police-chiens.md` est effective
  avant toute qualification d'espèce/race (pas seulement sa présence dans le
  skill). Ne pas republier tant que ces deux points n'ont pas été retestés au
  moins sur les cas 01, 02, 06, 24 et 28.
- Statut : à traiter (nouveau correctif requis avant campagne `r3`).

### 2026-08-03 — Baseline Claude v1.0.1 et correction des cinq demi-réussites
- Type : lacune + correction d'oracle + vérification juridique
- Branche : continuum-partenariats | pilotage-budget | penal-procedure |
  ecrits-professionnels | reglementation-appliquee | tests
- Contexte (anonymisé) : exécution complète des 28 cas par des agents Claude
  Sonnet 5, avec répondants et juges en contextes distincts ; artefacts bruts,
  manifest et jugements conservés.
- Constat : **23 RÉUSSITE / 5 DEMI-RÉUSSITE / 0 ÉCHEC**. Les cas critiques
  tiennent, ainsi que le sourcing et les frontières APJA/OPJ/RH, mais la
  baseline reste sous le seuil de 25 réussites. Les écarts sont les cas 05
  (distinction CLSPD/CISPD), 09 (allotissement), 18 (oracle trop catégorique),
  22 (refus faisant grief) et 24 (critère d'inscription et source exacte).
- Action : renforcer les quatre routages ; remplacer l'oracle du cas 18 par une
  qualification factuelle exigeant les circonstances de l'échange ; corriger
  la synthèse de l'art. 21 CPP ; ajouter au socle l'arrêté du 27 avril 1999,
  art. 1 et 2, et CRPA L. 211-2. Conserver la baseline sous son ancien hash et
  préparer `claude-v1.0.1-r2` sur la nouvelle empreinte.
- Statut : correctifs intégrés (v1.0.1) ; campagne `r2` à exécuter.

### 2026-07-28 — Mise à disposition : routes 53/73, 78-6 ou aucune (v1.0.1)
- Type : erreur juridique + lacune de packaging et de preuve de régression
- Branche : penal-procedure | ecrits-professionnels | packaging
- Contexte (anonymisé) : audit du garde-fou APJA et des modèles de mise à
  disposition.
- Constat : le corpus associait trop automatiquement un dépassement APJA à
  l'art. 73 et à une mise à disposition, omettait la route distincte de
  l'art. 78-6 et présentait la perquisition comme seulement interdite hors
  flagrance. Les anciens scores n'étaient pas reproductibles à partir
  d'artefacts bruts conservés.
- Action : routage 53/73, 78-6 ou aucune rétention ; interdiction de
  perquisition même en flagrance ; deux cas de non-régression ; scripts de
  validation, protocole d'artefacts et packaging runtime minimal.
- Statut : intégré (v1.0.1) ; suite complète de 28 cas à rejouer en contextes
  frais.

### 2026-07-10 — Conformité frontmatter aux règles Agent Skills (v1.0.0)
- Type : erreur (non-conformité de packaging, pas de fond)
- Branche : (SKILL / packaging)
- Contexte : l'upload du skill sur claude.ai a été refusé — le `SKILL.md`
  ne respectait pas les règles de validation des Agent Skills.
- Constat : `description` de 1 319 caractères (limite : 1 024) et bloc
  `metadata:` non standard dans le frontmatter (la spec ne garantit que
  `name` et `description`). Titre du corps resté à « v0.1.0 ».
- Action proposée : description réécrite à 1 013 caractères (déclencheurs et
  exclusions conservés), métadonnées déplacées dans un encadré du corps,
  titre réaligné. Zip de release reconstruit (contenu à la racine). La
  release v1.0.0 n'étant pas encore publiée, correction intégrée **sans
  incrément de version** (décision de l'auteur).
- Statut : intégré (v1.0.0)

### 2026-07-03 — Release v1.0.0 (première release stable)
- Type : cas nouveau (jalon)
- Branche : (release / SKILL)
- Contexte : matérialisation de la **première release** du skill, non encore
  effectuée. Le skill est complet (4 couches), audité (4 dimensions) et testé
  en contexte frais sur 3 runs (26 cas + 5 co-activations).
- Constat : la version faisait foi via `SKILL.md`/`CHANGELOG` mais **aucun tag
  de release** n'existait (ni ici, ni dans les skills voisins). Choix de
  l'auteur : promouvoir en **v1.0.0** (release stable) plutôt que taguer 0.8.6.
- Action proposée : bump `SKILL.md`/`README`/`CHANGELOG` en 1.0.0, entrée
  CHANGELOG de release récapitulant contenu et qualité validée, **tag git
  `v1.0.0`** + GitHub Release.
- Statut : intégré (v1.0.0)

### 2026-07-03 — 5 cas « chiens dangereux » (répondant Sonnet) + consolidation socle
- Type : cas nouveau + lacune (résolue)
- Branche : (tests) + reglementation-appliquee / objets police-chiens / socle
- Contexte : à la demande de l'auteur, lot de 5 cas ciblant le **permis de
  détention** et la **déclaration** des chiens catégorisés (22-26), exécuté avec
  **répondant Sonnet** (aveugle) et juge Opus indépendant.
- Constat : **2 RÉUSSITE / 3 DEMI / 0 ÉCHEC**. **Sourcing 5/5, aucune
  fabrication, aucune erreur de fond.** Fait marquant : au **cas 24**, Sonnet a
  **réellement consulté Légifrance en session** et cité **L. 211-14**
  (`LEGIARTI000019065635`) et **L. 211-16** (`LEGIARTI000006583059`),
  identifiants **confirmés réels** par recontrôle — provenance exemplaire, à
  l'opposé du cas 21 (Opus avait fabriqué un identifiant faute de référence).
  Le **cas 23** a correctement flaggé l'obligation de **déclaration en mairie**
  « à confirmer » au lieu d'inventer L. 211-14. Les 3 DEMI = pointeur non émis
  (25 : `penal-procedure.md`), attendu hors-scope (22 : refus de permis) ou
  fondement définitionnel non ré-explicité (24).
- Action proposée : **consolidation du socle** — **L. 211-14** (permis délivré
  par le maire, stérilisation 1re cat.) et **L. 211-16** (accès des chiens de
  1re cat. aux lieux publics) ajoutés à `references-verifiees.md` (vérifiés le
  2026-07-03) ; note de l'objet `police-chiens.md` mise à jour en conséquence.
  Restent « à confirmer » : obligation de déclaration en mairie et régime
  transitoire d'interdiction d'acquisition de la 1re catégorie (2008).
- Statut : intégré (v0.8.6)

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
