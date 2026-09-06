# Branche — Écrits professionnels (v0.1.0)

> Structure conforme à `_gabarit-branche.md`. Aucune valeur datée ni numéro
> d'article cité de mémoire hors ceux explicitement marqués « vérifié sur
> Légifrance » ci-dessous : pour le reste, seules les **règles** figurent,
> avec consigne de vérifier la version en vigueur à la date des faits.

## Périmètre / Exclusions

- **Périmètre** : **PV de contravention**, **rapport d'information**,
  **rapport de mise à disposition**. Cette branche pilote le **générateur
  interactif de la couche 4** (`references/templates/*.md`) : typologie des écrits,
  mentions obligatoires, valeur probante, et logique d'assemblage du
  document, y compris la règle `[INCOMPLET]`.
- **Exclusions** : le **fond de la qualification pénale** (nature de
  l'infraction, pouvoir APJA mobilisé, garde-fou OPJ) → `penal-procedure.md`
  (lien croisé, pas de duplication) ; le **contenu réglementaire** d'une
  infraction par domaine (route, débits de boissons, salubrité, animaux) →
  `reglementation-appliquee.md` ; le **formalisme d'un acte administratif**
  (arrêté, note au maire) → `references/templates/arrete-modele.md` et
  `references/templates/note-maire-modele.md`, sous contrôle préalable de
  `controle-legalite.md` ; la **jurisprudence de fond** sur la régularité
  d'un écrit contesté → `recherche-juridique`.

---

## 1. Questions couvertes

- Quel écrit produire pour telle situation : PV de contravention, rapport
  d'information, ou rapport de mise à disposition ?
- Quelles sont les mentions obligatoires de chaque écrit ?
- Quelle est la **valeur probante** du PV, et jusqu'à quand peut-elle être
  combattue ?
- Comment piloter le générateur interactif (`references/templates/`) : quelles questions
  poser, dans quel ordre, comment gérer une donnée manquante ?
- Que faire si l'écrit ne peut pas être complété faute de donnée (règle
  `[INCOMPLET]`) ?
- À qui transmettre l'écrit une fois produit (maire, OPJ, procureur) ?

---

## 2. Arbre de traitement

`identifier la situation (constatation seule / mesure sur la personne / fait
porté à connaissance sans constatation directe) → qualifier le pouvoir
mobilisé (renvoi penal-procedure.md : art. 21 / 21-2 / 53 et 73 / 78-6 CPP)
→ déterminer le type d'écrit (§5.1) → ouvrir le générateur references/templates/
correspondant → poser les questions une à une (qui / quand / où / pourquoi /
qualification / témoins / suites) → si donnée manquante : marquer
[INCOMPLET] et la demander explicitement (jamais halluciner) → assembler le
document → vérifier les mentions obligatoires (§5) → vérifier la
transmission requise (§6) → produire le livrable`.

Le test du **garde-fou APJA** (`SKILL.md` §5.2, `penal-procedure.md` §4.5)
précède toujours le choix de l'écrit. Une demande d'acte réservé à l'OPJ
impose le STOP et le compte rendu immédiat à l'OPJ ; elle ne crée, à elle
seule, aucun pouvoir de retenir ou de mettre une personne à disposition.
Le rapport de mise à disposition n'est produit que si l'une des routes
juridiques des articles 53 et 73 ou de l'article 78-6 du CPP est établie.

---

## 3. Variables à lever

- **Nature de l'écrit attendu** — l'utilisateur sait-il déjà lequel produire,
  ou faut-il le déduire de la situation (constatation seule, appréhension,
  simple information sans constatation directe) ?
- **Identité et qualité du rédacteur** — agent PM agréé et assermenté
  (condition de la qualité APJA, `rh-specificites-pm.md`), chef de poste,
  ou DPM.
- **Faits** — qui, quand (date et heure précises), où (localisation précise
  de l'infraction ou du fait, cf. exigence jurisprudentielle de
  localisation pour le PV, §5.2), quoi, comment constaté.
- **Qualification retenue** — texte d'incrimination précis (renvoi
  obligatoire à `reglementation-appliquee.md` ou `penal-procedure.md` pour
  le fond ; cette branche ne qualifie pas elle-même).
- **Personne(s) concernée(s)** — mis en cause identifié ou non, témoins,
  victime éventuelle.
- **Suites données** — observations recueillies, appréhension ou non, mise
  à disposition ou non, destinataire(s) du compte rendu (maire, OPJ,
  procureur).
- **Existence d'une donnée manquante** bloquant l'assemblage → règle
  `[INCOMPLET]` (§5.5).

---

## 4. Typologie des écrits de la PM (cette branche)

| Écrit | Déclencheur | Nature | Générateur |
|---|---|---|---|
| **PV de contravention** | Constatation directe d'une **contravention** dans le cadre du pouvoir de l'agent (art. 21 CPP) | Acte de constatation à **valeur probante particulière** (§5.2) | `references/templates/pv-contravention.md` |
| **Rapport d'information** | Fait porté à la connaissance du maire / de l'OPJ, sans route 53/73 ou 78-6 établie ni constatation par PV (ex. délit constaté hors compétence de verbalisation, observation, signalement) | Écrit de **compte rendu**, valeur probante ordinaire (simple rapport) | `references/templates/rapport-information.md` |
| **Rapport de mise à disposition** | Route A : appréhension d'un crime flagrant ou d'un délit flagrant puni d'emprisonnement (art. 53 et 73 CPP) ; route B : refus ou impossibilité de justifier son identité après relevé autorisé, puis présentation ou rétention sur ordre de l'OPJ (art. 78-6 CPP) | Écrit de **compte rendu d'une mesure légalement fondée**, avec sa base exacte et sa chronologie | `references/templates/rapport-mise-a-disposition.md` |

**Autres écrits pilotés par cette branche** (actes, hors écrits de
constatation stricto sensu — rappel de cohérence, détail dans `SKILL.md`
§6) :

| Écrit | Nature | Générateur |
|---|---|---|
| **Arrêté (modèle)** | Acte faisant grief le cas échéant → `controle-legalite.md` **avant** production | `references/templates/arrete-modele.md` |
| **Note au maire (modèle)** | Note de pilotage / aide à la décision, pas un acte | `references/templates/note-maire-modele.md` |

> Ne jamais confondre rapport d'information et rapport de mise à
> disposition : le second documente une **mesure de contrainte sur la
> personne** (appréhension), pas une simple transmission d'information.

---

## 5. Règles métier

### 5.1 Choix de l'écrit — logique de décision

1. **Une route légale de mise à disposition est-elle établie ?**
   - **Route A** : crime flagrant ou délit flagrant puni d'emprisonnement,
     qualifié au regard de l'art. 53 CPP, puis appréhension sur l'art. 73.
   - **Route B** : relevé d'identité légalement autorisé, refus ou
     impossibilité de justifier l'identité, compte rendu immédiat à l'OPJ,
     puis présentation ou rétention sur son ordre (art. 78-6).
   - Si oui → **rapport de mise à disposition**, en plus de tout PV éventuel
     sur les faits eux-mêmes.
   - Si aucune route n'est établie → aucune rétention ; passer à 2.
2. **L'agent a-t-il constaté lui-même une contravention dans le cadre de
   son pouvoir de verbalisation (renvoi `reglementation-appliquee.md` pour
   vérifier que la contravention relève bien de sa compétence
   matérielle) ?**
   - Oui → **PV de contravention**.
   - Non → **rapport d'information** (fait porté à connaissance, délit hors
     compétence de constatation directe par PV, observation simple).
3. **La demande comporte-t-elle un acte réservé à l'OPJ ?** → tester le
   garde-fou (§5.4) **avant** de conclure sur l'écrit, quelle que soit la
   réponse aux points 1 et 2. L'art. 16 CPP définit notamment la qualité
   d'OPJ ; la base de chaque acte réservé doit être citée séparément.

Ces trois écrits ne sont **pas exclusifs** : une même situation peut
cumuler PV (sur l'infraction constatée) et rapport de mise à disposition
(sur la mesure fondée selon la route retenue), avec une double transmission
(`penal-procedure.md` §4.2).

### 5.2 Valeur probante du PV de contravention

**Art. 537 du CPP** *(contenu confirmé sur Légifrance le 2026-06-30,
identifiant LEGIARTI000006576893)* : les contraventions sont prouvées soit
par procès-verbaux ou rapports, soit par témoins à défaut de
procès-verbaux ou rapports, ou à leur appui.

Sauf disposition contraire, les procès-verbaux ou rapports établis par les
officiers ou agents de police judiciaire, les agents de police judiciaire
adjoints, ou les fonctionnaires ou agents chargés de certaines fonctions de
police judiciaire **auxquels la loi a attribué le pouvoir de constater les
contraventions par procès-verbal**, font **foi jusqu'à preuve contraire**.
**La preuve contraire ne peut être rapportée que par écrit ou par témoins.**

**Conséquences pratiques pour l'agent PM** :
- Le PV de contravention de l'agent PM agréé et assermenté (art. 21 CPP)
  bénéficie de cette **force probante renforcée**, à la différence d'un
  simple rapport.
- Cette force probante n'est **pas automatique** : elle suppose que le
  texte d'incrimination concerné **attribue bien** à l'agent PM le pouvoir
  de constater par procès-verbal (vérifier dans `reglementation-appliquee.md`
  ou le texte spécial applicable — ex. code de la route, art. L. 130-4,
  §5.3).
- **Exigence de précision** (jurisprudence constante de la Cour de
  cassation sur l'art. 537 CPP, *à vérifier au cas par cas via
  `recherche-juridique` avant citation en acte*) : pour valoir jusqu'à
  preuve contraire, le PV doit **localiser précisément** l'infraction
  (lieu exact, le cas échéant portion de voie) et énoncer les éléments
  matériels constatés avec une précision suffisante pour permettre au
  contrevenant et au juge de vérifier les faits. Un PV imprécis perd sa
  force probante renforcée et retombe au régime de preuve ordinaire.
- La force probante porte sur la **matérialité des faits constatés
  personnellement par l'agent** — pas sur la qualification juridique
  retenue, ni sur des éléments rapportés de tiers.

Le **rapport d'information** et le **rapport de mise à disposition**
n'ont **pas** ce régime de preuve renforcée : ce sont des écrits de compte
rendu, appréciés selon le régime de preuve ordinaire.

### 5.3 Mentions obligatoires — principes communs

Avant tout détail propre à chaque écrit, **toujours** consigner :
- **identité du rédacteur** (nom, qualité, n° d'agrément si exigé par le
  texte applicable — à vérifier) ;
- **date et heure** précises de la constatation ou du fait (et, le cas
  échéant, heure d'appréhension / heure de mise à disposition distinctes,
  §5.4) ;
- **lieu précis** — exigence renforcée pour le PV (§5.2) ;
- **faits matériellement constatés**, formulés au plus près de
  l'observation directe, sans interprétation ni supposition ;
- **qualification retenue**, avec le texte d'incrimination précis (renvoi
  `reglementation-appliquee.md` / `penal-procedure.md` pour le fond — cette
  branche ne tranche pas la qualification elle-même) ;
- **identité du mis en cause** si connue, et des **témoins** le cas
  échéant ;
- **observations recueillies** du contrevenant, si l'agent les a
  recueillies dans le cadre de l'art. 21 CPP (faculté, pas obligation) ;
- **suites données** et **destinataire(s)** du document.

**Mentions propres au PV de contravention** — en sus de ce qui précède :
- texte exact de l'incrimination (visa précis) ;
- éventuelle référence à un appareil de contrôle homologué (radar,
  cinémomètre, horodateur) si la contravention en dépend — modalités de
  preuve spécifiques à vérifier selon le texte applicable ;
- mention de la notification ou de l'avis au contrevenant selon la
  procédure applicable (verbalisation électronique ou PV papier — circuit
  à vérifier localement).

**Mentions propres au rapport de mise à disposition** — en sus du socle
commun :
- **route juridique exacte** : art. 53 et 73 CPP, ou art. 78-6 CPP ;
- **faits établissant toutes les conditions** de la route retenue ;
- **heure exacte de l'appréhension** (route 53/73), ou du refus / de
  l'impossibilité de justifier l'identité et du compte rendu à l'OPJ
  (route 78-6) ;
- **heure exacte de la présentation, de la rétention ordonnée ou de la
  remise** à l'OPJ ;
- pour la route 78-6, **ordre ou décision de l'OPJ** et heure de réception ;
- **identité ou qualité de l'OPJ destinataire**, si connue ;
- description de la **contrainte exercée**, strictement limitée à ce qui
  a été nécessaire (`penal-procedure.md` §4.3) — ne jamais laisser entendre
  une mesure d'audition ou de fouille relevant de l'OPJ.

**Mentions propres au rapport d'information** — en sus du socle commun :
- préciser explicitement qu'**aucune route 53/73 ou 78-6** n'est établie
  (pour distinguer sans ambiguïté du rapport de mise à disposition) ;
- préciser le **canal de transmission** retenu (maire, OPJ territorialement
  compétent, procureur via l'OPJ — `penal-procedure.md` §4.2).

### 5.4 Articulation avec le garde-fou APJA

Si, au cours du recueil des informations pour l'écrit, il apparaît que la
situation **dépasse le pouvoir APJA** par une demande d'acte réservé à l'OPJ, le
**garde-fou** (`SKILL.md` §5.2, `penal-procedure.md` §4.5) prime sur la
production de l'écrit :
1. Afficher le **STOP** en premier livrable.
2. Rendre compte immédiatement à l'OPJ et limiter la suite à l'action APJA
   conforme.
3. Qualifier séparément une éventuelle route 53/73 ou 78-6. Si aucune route
   n'est établie, ne retenir personne et produire seulement l'écrit de
   constatation ou d'information adapté.
4. Produire un **rapport de mise à disposition** uniquement lorsqu'une route
   est établie — **aucun** écrit d'audition ou assimilé à un acte réservé OPJ.

Le vocabulaire de la demande ne suffit pas à qualifier l'échange : « entendu »
ou « a avoué » peut désigner des propos spontanés, des observations recueillies
lors d'une constatation ou un questionnement structuré. Avant toute
requalification, demander l'initiative des propos, les questions posées, la
contrainte éventuelle, la forme questions-réponses et les droits notifiés. Le
rapport licite décrit seulement les circonstances et les propos effectivement
perçus ; il ne reconstruit jamais un PV d'audition et ne qualifie pas
catégoriquement l'échange en l'absence de faits suffisants.

### 5.5 Règle `[INCOMPLET]` — donnée manquante

**Interdiction absolue d'halluciner une donnée manquante** (date, lieu,
identité, texte d'incrimination, heure). Si une information nécessaire
n'est pas fournie :
1. Produire le brouillon avec les champs disponibles.
2. Marquer explicitement chaque champ manquant par `[INCOMPLET — préciser :
   <nom du champ>]`.
3. **Lister** ces champs en fin de document, dans une section dédiée.
4. **Demander explicitement** les données manquantes avant de considérer
   l'écrit comme finalisé.

Ne jamais transmettre, viser, ni présenter comme définitif un document
portant une mention `[INCOMPLET]` non résolue.

---

## 6. Procédures et délais

1. **Détection du type d'écrit** (§5.1) — avant toute question de détail.
2. **Recueil interactif** — questions posées **une à une** : qui / quand /
   où / pourquoi / qualification / témoins / suites (cf. `SKILL.md` §6).
   Ne pas enchaîner plusieurs questions en bloc : un champ à la fois,
   confirmation avant de passer au suivant.
3. **Vérification des mentions obligatoires** (§5.3) avant assemblage
   final.
4. **Vérification de la qualification** — renvoi à
   `reglementation-appliquee.md` (contenu de l'infraction) et
   `penal-procedure.md` (pouvoir mobilisé) ; cette branche **n'invente
   jamais** une qualification.
5. **Transmission** — selon le type d'écrit :
   - PV de contravention : circuit de transmission au juge/officier du
     ministère public selon la procédure applicable (verbalisation
     électronique ou circuit papier) — *modalités et délais à vérifier
     localement, pas de délai chiffré donné de mémoire* ;
   - rapport d'information / rapport de mise à disposition : maire **et**
     OPJ territorialement compétent (`penal-procedure.md` §4.2), sans
     attendre la rédaction définitive pour le **compte rendu oral
     immédiat**, l'écrit formalisant ensuite la trace.
6. **Archivage et traçabilité** — conserver une trace de la version
   transmise, en particulier en cas de contestation ultérieure (preuve
   contraire au PV, §5.2).

> Annoncer toute hypothèse retenue sur le circuit de transmission local et
> demander confirmation si la donnée manque (organisation propre à la
> collectivité, convention de coordination).

---

## 7. Déclencheurs de vérification

Appliquer la matrice §2.2 du `SKILL.md` — vérification **obligatoire**
avant de conclure dès que :
- le **contenu exact d'un acte** (PV, rapport) doit être produit ou
  finalisé pour transmission ;
- la **qualification pénale** visée dans l'écrit est en jeu → renvoyer à
  `penal-procedure.md` / `reglementation-appliquee.md`, ne pas trancher
  ici ;
- la **valeur probante** du PV est contestée ou questionnée pour un cas
  précis (jurisprudence sur l'art. 537 CPP, exigence de précision) ;
- un **délai de transmission** ou un **circuit procédural** (verbalisation
  électronique, OMP) conditionne la réponse ;
- un **identifiant LEGIARTI/JORFTEXT/NOR** doit figurer dans l'écrit
  produit (règle de provenance, `SKILL.md` §5.3).

---

## 8. Pièges & confusions fréquentes

1. Produire un **PV** pour un fait que l'agent n'a pas constaté
   personnellement, ou hors du champ de sa compétence matérielle de
   verbalisation (vérifier `reglementation-appliquee.md` avant).
2. Confondre **rapport d'information** et **rapport de mise à
   disposition** : seul le second documente une **appréhension**.
3. Croire que tout écrit de l'agent PM a la **force probante** de
   l'art. 537 CPP : seul le **PV de contravention** régulièrement établi
   en bénéficie ; un simple rapport est apprécié selon le régime de preuve
   ordinaire.
4. Omettre la **localisation précise** dans un PV : risque de perte de la
   force probante renforcée (exigence jurisprudentielle, à vérifier au cas
   par cas).
5. Rédiger ou compléter un champ manquant **par supposition** plutôt que
   de marquer `[INCOMPLET]` et de le demander.
6. Fusionner le **compte rendu au maire** et le **compte rendu à l'OPJ**
   sans préciser la double transmission (`penal-procedure.md` §4.2).
7. Esquisser, dans un rapport de mise à disposition, des éléments relevant
   d'une **audition formelle** (questions-réponses circonstanciées) :
   bascule vers un acte réservé OPJ, interdit (§5.4).
8. Oublier de vérifier, pour un **arrêté** ou une **note au maire**, le
   passage préalable par `controle-legalite.md` (acte faisant grief).

---

## 9. Données / références à vérifier

| Référence | Statut dans cette session |
|---|---|
| **Art. 537 CPP** (force probante des PV et rapports de contravention jusqu'à preuve contraire) | **Vérifié sur Légifrance le 2026-06-30**, identifiant LEGIARTI000006576893 ; version en vigueur à la date des faits à reconfirmer au cas d'usage |
| **Art. 21 et 21-2 CPP** (qualité APJA, compte rendu maire/OPJ) | Vérifiés sur Légifrance le 2026-06-30 — détail complet dans `penal-procedure.md` §4.1–4.2, pas de duplication ici |
| **Art. 53 et 73 CPP** (qualification de la flagrance et appréhension) | Vérifiés sur Légifrance le 2026-07-28 ; identifiants LEGIARTI000006575016 et LEGIARTI000029000766 — détail dans `penal-procedure.md` §4.3 |
| **Art. 78-6 CPP** (relevé d'identité, compte rendu à l'OPJ, présentation ou rétention sur ordre) | Vérifié sur Légifrance le 2026-07-28 ; identifiant LEGIARTI000034114850 — détail dans `penal-procedure.md` §4.3 |
| **Art. 16 CPP** (qualité d'OPJ) | Vérifié sur Légifrance le 2026-07-28 ; identifiant LEGIARTI000047052868. Cet article ne fonde pas à lui seul tous les actes réservés ; citer le texte propre à l'acte concerné |
| **Art. 56 CPP** (perquisition de flagrance par l'OPJ) | Vérifié sur Légifrance le 2026-07-28 ; identifiant LEGIARTI000049778813 — aucune perquisition par l'agent de police municipale, y compris en flagrance |
| **Art. L. 130-4 du code de la route** (catégories d'agents habilités à constater les contraventions routières par PV, renvoi aux art. L. 511-1 et L. 512-2 CSI pour les agents PM) | **Vérifié sur Légifrance le 2026-06-30**, identifiant LEGIARTI000045072417 ; contraventions précises constatables par catégorie d'agent **à confirmer en version consolidée** et selon le texte réglementaire d'application |
| **Art. L. 511-1 et L. 512-2 CSI** (régime des agents de police municipale, compétences de constatation) | À confirmer en version consolidée — non revérifié dans cette session, voir `socle-sources-verification.md` |
| Jurisprudence sur l'exigence de précision (localisation) conditionnant la force probante du PV (art. 537 CPP) | À vérifier au cas par cas via `recherche-juridique` avant citation en acte — aucune décision nommément citée de mémoire dans cette branche |
| Modalités et délais exacts de transmission (verbalisation électronique, OMP) | À confirmer en version consolidée et selon l'organisation locale |

---

## 10. Écrits & livrables — pilotage des générateurs `references/templates/`

Cette branche **pilote** les générateurs interactifs de la couche 4. Elle
ne contient pas elle-même les gabarits de document : ceux-ci vivent dans
`references/templates/`, qui n'est pas encore peuplé à ce stade du skill (couche 4,
phase ultérieure). Quand `references/templates/` sera produit, chaque générateur devra
respecter :

1. **PV de contravention** — `references/templates/pv-contravention.md`.
   Vérifier au préalable la base légale de l'infraction
   (`reglementation-appliquee.md`) et la compétence de constatation de
   l'agent (art. 21 CPP + texte spécial, ex. art. L. 130-4 code de la
   route, §5.3, §9). Respecter les mentions de §5.3 et l'exigence de
   précision conditionnant l'art. 537 CPP (§5.2).
2. **Rapport d'information** — `references/templates/rapport-information.md`. Préciser
   l'absence de route 53/73 ou 78-6 ; double destinataire maire/OPJ
   (`penal-procedure.md` §4.2).
3. **Rapport de mise à disposition** — `references/templates/rapport-mise-a-disposition.md`.
   Mentionner systématiquement la route 53/73 ou 78-6, les faits qui en
   établissent les conditions, la chronologie complète, la décision de l'OPJ
   lorsque l'art. 78-6 est mobilisé, et le destinataire ; articulation
   garde-fou §5.4.
4. **Arrêté (modèle)** — `references/templates/arrete-modele.md`. Acte faisant grief le
   cas échéant : motivation en fait et en droit + voies et délais de
   recours + vérification de la transmission au contrôle de légalité
   (CGCT — à confirmer) ; passage **obligatoire** par
   `controle-legalite.md` avant production.
5. **Note au maire (modèle)** — `references/templates/note-maire-modele.md`. Note de
   pilotage, pas un acte ; pas de voies de recours, mais rigueur sur la
   base légale citée si elle conditionne une décision du maire.

**Logique interactive obligatoire** (rappel `SKILL.md` §6) : détecter le
type d'écrit → poser les questions une à une → assembler le document.
**Cas incomplets** : jamais d'hallucination, brouillon `[INCOMPLET]` listant
les champs manquants (§5.5).

---

## 11. Double échelle [risque / confiance]

| Sous-domaine | Risque | Confiance | Repère |
|---|---|---|---|
| Choix du bon type d'écrit | Moyen | Stable | Vérification ponctuelle si situation mixte (PV + appréhension) |
| Valeur probante du PV (art. 537 CPP) | Élevé | Stable sur le principe (vérifié), à vérifier sur l'exigence de précision au cas d'espèce | Citation obligatoire + réserve « à confirmer » sur la jurisprudence |
| Mentions obligatoires d'un écrit transmis | Élevé | À vérifier selon le texte d'incrimination et le circuit local | Citation + vérification ponctuelle obligatoire avant transmission |
| Compétence de constatation (texte spécial, ex. L. 130-4 code de la route) | Élevé | Stable sur le principe (vérifié), à confirmer sur le détail par catégorie d'agent | Citation obligatoire + réserve « à confirmer en version consolidée » |
| Production d'un acte faisant grief (arrêté) | Critique | À vérifier systématiquement | Citation + motivation + voies de recours + contrôle de légalité obligatoires |
| Donnée manquante dans un écrit | Élevé | N/A | `[INCOMPLET]` obligatoire, jamais d'hallucination |

---

## 12. Checklist de branche

1. **Garde-fou APJA testé** : la demande comporte-t-elle un acte réservé à
   l'OPJ ? Si oui, STOP affiché avant toute production d'écrit et compte rendu
   immédiat à l'OPJ. Le rapport de mise à disposition ne reste mobilisable
   que si une route 53/73 ou 78-6 est établie (§5.4).
2. **Type d'écrit correctement choisi** selon la logique de décision (§5.1) :
   PV / rapport d'information / rapport de mise à disposition, non
   exclusifs les uns des autres.
3. **Qualification pénale renvoyée à `penal-procedure.md` /
   `reglementation-appliquee.md`**, jamais tranchée dans cette branche.
4. **Mentions obligatoires** du type d'écrit concerné toutes présentes
   (§5.3), y compris l'exigence de localisation précise pour le PV.
5. **Valeur probante** correctement qualifiée (force probante renforcée du
   PV vs régime ordinaire des rapports, §5.2) — ne pas la présenter comme
   acquise sans vérifier que le texte d'incrimination attribue bien le
   pouvoir de constatation par PV à l'agent.
6. **Aucune donnée manquante comblée par supposition** : règle
   `[INCOMPLET]` appliquée et champs listés explicitement (§5.5).
7. **Double transmission** maire + OPJ territorialement compétent
   correctement distinguée pour les rapports (`penal-procedure.md` §4.2).
8. Si **acte faisant grief** (arrêté) : passage par `controle-legalite.md`
   vérifié avant toute production.
9. Références citées avec leur statut de vérification exact (§9), jamais
   un identifiant inventé.
10. Couple **[risque / confiance]** (§11) indiqué quand utile à la
    décision.

[risque : élevé sur la valeur probante du PV et la compétence de
constatation, critique si acte faisant grief associé / confiance : stable
sur l'art. 537 CPP et l'art. L. 130-4 du code de la route (vérifiés sur
Légifrance le 2026-06-30), à confirmer en version consolidée pour le détail
des compétences par catégorie d'agent et pour la jurisprudence d'espèce sur
l'exigence de précision]
