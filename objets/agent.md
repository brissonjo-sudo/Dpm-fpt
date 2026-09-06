# Objet métier — Agent de police municipale (v0.1.0)

**Situation type** : Un agent est nommé, doit être agréé et assermenté avant d'exercer ; le DPM suit l'état des agréments, la formation armement, et constate les manquements déontologiques.

**[Risque / Confiance]** — Risque **élevé** (condition d'exercice de la qualité d'APJA ; irrégularité d'agrément fragilise tout acte de constatation). Confiance **stable** sur l'architecture du dispositif (cumul nomination / agrément / assermentation), **à vérifier** sur le numéro exact d'article du code de déontologie applicable en cas de manquement.

---

## 1. Acteurs et autorités compétentes

| Acteur | Rôle | Compétence |
|--------|------|-----------|
| **Maire** (ou président d'EPCI) | Autorité d'emploi | Nomme l'agent ; demande l'agrément au préfet et au procureur ; organise la formation et l'armement ; reste titulaire du pouvoir de police |
| **Préfet** (représentant de l'État) | Autorité d'agrément | Agrée l'agent conjointement avec le procureur ; autorise le port d'armes (condition cumulative à la convention de coordination) ; peut retirer/suspendre l'agrément |
| **Procureur de la République** | Autorité d'agrément | Agrée l'agent conjointement avec le préfet ; peut suspendre l'agrément seul en cas d'urgence |
| **Directeur de police municipale (DPM)** | Chef de service | Assure le commandement opérationnel ; suit l'état des agréments et des formations ; constate les manquements déontologiques |
| **Agent de PM** (titulaire, contractuel, stagiaire) | Opérateur | Exerce ses pouvoirs d'APJA uniquement si agréé, assermenté et autorisé (armement si applicable) |

**Conflit de compétence possible** : un agent dont l'agrément est suspendu ou retiré **perd immédiatement** sa qualité d'APJA et ne peut plus constater d'infractions, même si le maire ou le DPM ignorent la décision. La notification au maire n'est pas toujours instantanée → surveillance proactive auprès du préfet.

---

## 2. Textes applicables

### Agrément et assermentation
- **`../references/rh-specificites-pm.md`** — Frontière `dpm-fpt` / `drh-fpt` ; conditions d'agrément (CSI L. 511-2, *vérifié 2026-06-30*, LEGIARTI000043540434) ; assermentation ; retrait/suspension ; effet sur la qualité d'APJA.

### Armement et port d'armes
- **`../references/armement-equipements.md`** — Autorisation préfectorale individuelle nominative (CSI L. 511-5, *vérifié 2026-06-30*, LEGIARTI000041411486) ; conditions cumulatives (convention de coordination + formation préalable + aptitude) ; maintien de l'autorisation par entraînement obligatoire périodique.

### Conformité, déontologie et données
- **`../references/conformite-deontologie-donnees.md`** — Code de déontologie des agents PM (CSI, partie réglementaire, R. 515-1 et s., *à confirmer en version consolidée*) ; constat du manquement (déontologie, usage proportionné de la force) ; responsabilité personnelle/administrative ; RGPD et traçabilité des consultations de fichiers.

### Autres références transverses utiles
- **`../references/penal-procedure.md`** — En cas de mise en cause pénale de l'agent ou à partir d'un constat déontologique avec dimension pénale (violences, usage disproportionné de la force) → articulation avec le garde-fou APJA.
- **`../references/continuum-partenariats.md`** — Convention de coordination PM / forces de l'État (condition préalable à l'armement).
- **`../references/doctrine-operationnelle.md`** — Commandement opérationnel de terrain (articulation avec la hiérarchie statutaire du service).

---

## 3. Procédures, étapes et délais

### 3.1 Agrément et assermentation (étapes cumulatives)

1. **Nomination** : le maire ou le président d'EPCI nomme l'agent de PM au cadre d'emplois correspondant (titularisation, contractualisation ou stage).
2. **Demande d'agrément** : le maire transmet au préfet et au procureur une demande motivée (identité, fonctions, date de prise de poste attendue).
3. **Instruction** : délai d'instruction **à vérifier au cas par cas** — aucune durée type figée ici.
4. **Agrément conjoint** : le préfet et le procureur délivrent l'agrément, **conjointement et de façon nominative**.
5. **Assermentation** : l'agent doit être assermenté devant le tribunal compétent **avant d'exercer tout pouvoir d'APJA**. Modalités exactes de la prestation → à confirmer en version consolidée.
6. **Suivi de validité** : 
   - L'agrément et l'assermentation **demeurent valables tant que l'agent exerce** — pas de renouvellement automatique périodique ;
   - **En cas de mutation vers une autre collectivité** : la validité du droit de porter le titre d'APJA dépend d'un **nouvel agrément** ; l'agent ne peut pas transférer automatiquement son agrément d'une commune à l'autre.
   - **En cas de changement de collectivité sans nouvel agrément** : l'agent perd sa qualité d'APJA **du jour du changement** → irrégularité de procédure sur tout acte de constatation après cette date.

### 3.2 Retrait ou suspension d'agrément

- **Retrait** : le préfet ou le procureur peut retirer l'agrément **après consultation du maire ou du président d'EPCI** (sauf urgence).
- **Suspension en urgence** : le procureur peut suspendre l'agrément **seul et sans consultation préalable** en cas d'urgence.
- **Notification** : le DPM doit être notifié de la suspension/du retrait. Ne pas attendre une notification officielle formelle avant de vérifier l'état auprès de la préfecture (risque de découverte tardive d'une perte de qualité).
- **Effet immédiat** : dès la suspension/le retrait, l'agent **perd sa qualité d'APJA** ; aucun acte de constatation ne peut être valablement posé après cette date.

### 3.3 Formation préalable au port d'armes

- **Avant tout port effectif** : l'agent doit avoir suivi la formation préalable obligatoire spécifique à l'armement (distincte de la FIA générale du cadre d'emplois).
- **Détail de la formation, durée, contenu** : voir `armement-equipements.md` (§4.7) — ne pas dupliquer ici.
- **Entraînement périodique** : pour maintenir l'autorisation de port, l'agent doit se soumettre à un entraînement (maniement, tir) à une périodicité **fixée par le décret armement et à vérifier en version consolidée** ; le non-respect expose au retrait de l'autorisation préfectorale.

### 3.4 Constat d'un manquement déontologique

1. **Signalement initial** : observation sur le terrain, rapport hiérarchique, demande d'éclaircissement.
2. **Constat factuel et textuel** : le DPM ou un responsable qualifié rédige un rapport de constat, en décrivant les faits observés et en identifiant les articles potentiellement applicables du code de déontologie (sous réserve de vérification).
3. **Remontée hiérarchique** : transmission à la direction générale, au maire, ou au collectif de commandement selon l'organisation locale.
4. **Point de bascule critique** : dès que des **griefs** sont **notifiés à l'agent** ou qu'une **instance disciplinaire** est **saisie** → la main passe **immédiatement** à `drh-fpt` ; cette branche ne produit plus d'écrit procédural.
5. **Dimension pénale** : si le constat touche à des **violences, abus d'autorité, ou usage disproportionné de la force**, tester d'abord le **garde-fou APJA** (l'agent peut être mis en cause pénalement) → articulation avec `penal-procedure.md`.

---

## 4. Écrits associés

### Écrits de constatation et suivi
- **Rapport de constat de manquement déontologique** — `../references/templates/rapport-information.md` (gabarit via `ecrits-professionnels.md`) : description factuelle, identification des articles du code de déontologie potentiellement concernés (sous réserve de vérification du numéro exact), remontée hiérarchique.
- **Note au maire sur l'état des agréments** — `../references/templates/note-maire-modele.md` : agents agréés et assermentés en cours de validité, agréments à surveiller, suspensions/retraits en cours, dates d'expiration attendues (mutations), autorisations de port d'armes à renouveler.
- **Courrier au préfet** (demande d'agrément, signalement d'une situation) : sujet spécifique, identité de l'agent, motif.

### Écrits en cas de dimension pénale
- Dès que l'agent risque une mise en cause pénale (usage de la force contesté, consultation de fichier hors cadre, violences) → activation du **garde-fou APJA** (`SKILL.md` §5.2) et passage à `penal-procedure.md` pour le compte rendu à l'OPJ et au maire.

### Actes faisant grief
- Un éventuel **retrait d'autorisation de port d'armes** par le préfet est un acte de l'État, non produit par cette branche → néanmoins, le DPM peut adresser une **note d'alerte au maire** sur le risque ou l'imminence d'une décision préfectorale, avec pièces justificatives (non-respect de l'entraînement, doute sur l'aptitude).
- Toute décision communale défavorable à l'agent (refus de dotation, suspension des fonctions) : motivation + voies et délais de recours + vérifier le contrôle de légalité → `controle-legalite.md` avant production.

---

## 5. Jurisprudence clé

Voir **`recherche-juridique`** pour :
- **Contrôle de la proportionnalité de l'usage de la force** par les agents PM (standards du juge administratif et pénal).
- **Irrégularité de procédure** sur la qualité d'APJA (absence d'agrément, assermentation non effectuée, absence d'autorisation de port d'armes) — jurisprudence de nullité d'actes de constatation.
- **Faute personnelle détachable du service** vs **faute de service** en matière de responsabilité (usage abusif d'autorité, comportement contraire aux devoirs déontologiques).
- **Indépendance des procédures** (administrative / pénale / disciplinaire) : cumul possible sans exclusion mutuelle.

Thèmes sensibles à signaler en amont :
- Qualification d'un **usage d'arme** (légitime défense vs usage disproportionné).
- **Responsabilité de la commune** en cas de dommage causé par un agent arm&eacute; ; distinction avec la responsabilité personnelle de l'agent.

---

## 6. Check-list opérationnelle

### Avant d'affirmer qu'un agent a la qualité d'APJA
- [ ] **Agrément du préfet ET du procureur** en cours de validité et applicable à la date des faits ?
- [ ] **Assermentation** effectuée et non levée (mutation sans nouvel agrément, retrait) ?
- [ ] Vérifier auprès de la préfecture l'état exact de l'agrément (pas de suspension/retrait récent non notifié) ?
- [ ] Si port d'armes : **autorisation préfectorale nominative** individuelle en cours de validité ?
- [ ] Si port d'armes : **formation préalable** validée et **entraînement périodique** à jour (date et nature à vérifier) ?

### En cas de constat de manquement déontologique
- [ ] **Nature du fait** identifiée (comportement pur vs usage de la force vs consultation de fichier) ?
- [ ] **Code de déontologie** (CSI R. 515-1 et s.) : article(s) potentiellement applicable(s) **à vérifier précisément** avant citation en acte (ne pas chiffrer de mémoire) ?
- [ ] **Dimension pénale** testée (violences, abus, usage disproportionné de la force) → **garde-fou APJA** (l'agent peut être mis en cause) ?
- [ ] Rapport de constat rédigé (faits, articles applicables sous réserve, pas de présomption de sanction) ?
- [ ] **Point de bascule** identifié : dès notification de griefs ou saisine disciplinaire → main à `drh-fpt` ?
- [ ] **Responsable de traitement RGPD** (le maire, pas le DPM) notifié en cas d'incident de données ?

### Avant toute sortie — Garde-fou APJA
- [ ] La situation décrite relève-t-elle **exclusivement des pouvoirs APJA** (art. 21 / 21-2 CPP) ou **dépasse-t-elle** ce cadre (garde à vue, audition formelle, perquisition, réquisition judiciaire) ?
- [ ] Si dépassement détecté → **STOP** affiché **en priorité**, compte rendu immédiat à l'OPJ, puis qualification du seul fondement de contrainte possible : art. 53 + 73, art. 78-6, ou aucun.

### Contrôles transverses
- [ ] Autorités compétentes (maire / préfet / procureur) et leurs rôles respectifs correctement identifiées ?
- [ ] Tout numéro d'article cité assorti de « à confirmer en version consolidée » ou « vérifié sur Légifrance le 2026-06-30 » ?
- [ ] Références vers les branches partenaires (`rh-specificites-pm.md`, `armement-equipements.md`, `conformite-deontologie-donnees.md`, `penal-procedure.md`) effectuées sans duplication de contenu ?
- [ ] Couple [risque / confiance] clairement indiqué si pertinent pour la décision ?
- [ ] Cas journalisable (lacune procédurale, réforme récente, situation atypique) → prévu pour `JOURNAL.md` ?

---

## Références et remontées

**Branche principale de frontière** : Tout sujet de carrière, paie, avancement, position statutaire ou procédure disciplinaire (saisine, notification de griefs, sanction) → `drh-fpt` (`SKILL.md` §5.4) sans reformulation ici.

**Coordination impérative** : Les trois dimensions (agrément, déontologie, armement) d'un agent peuvent être liées — croiser systématiquement avant de conclure.

**Mise à jour requise** : 
- Révision du décret armement (n° 2020-511 du 2 mai 2020) et des suites.
- Code de déontologie PM (CSI R. 515-1 et s.) en cas de refonte.
- Régime de l'agrément et de l'assermentation (CSI L. 511-2) en cas de réforme législative.
