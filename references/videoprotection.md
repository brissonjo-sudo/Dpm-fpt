# Branche — Vidéoprotection (v0.1.0)

> Structure conforme à `_gabarit-branche.md`. Aucune valeur datée (durée de
> conservation, délai d'instruction, composition de la commission
> départementale) n'est donnée de mémoire : seules les **règles** figurent ici,
> avec la consigne de vérifier la version en vigueur.

## Périmètre / Exclusions

- **Périmètre** : cadre du **Code de la sécurité intérieure (CSI), Livre II,
  Titre V** (vidéoprotection sur voie publique et lieux ouverts au public) ;
  **régime d'autorisation préfectorale** ; **exploitation du centre de
  supervision urbain (CSU)** par les agents de police municipale.
- **Exclusions** :
  - **RGPD / conformité données et AIPD générale** → renvoi exprès à
    `references/conformite-deontologie-donnees.md` (le présent fichier ne
    traite que le régime CSI propre à la vidéoprotection ; toute analyse
    d'impact, registre de traitement ou doctrine CNIL transverse relève de
    cette branche) ;
  - **vidéosurveillance intérieure de locaux non ouverts au public** (relève
    du droit du travail / RGPD général, hors CSI Titre V) → hors périmètre ;
  - **caméras individuelles (caméras-piétons)** → hors présent fichier (régime
    CSI distinct, à traiter dans `armement-equipements.md` ou fiche dédiée si
    créée) ;
  - **drones et caméras aéroportées** → régime CSI distinct (articles propres,
    non couverts ici) ;
  - le **fond opérationnel détaillé du CSU** (procédures de poste, doctrine de
    visionnage, fiches réflexes) → objet **`objets/videoprotection.md`**
    (à créer en couche 3 ; à ce stade, ce pointeur est annoncé mais l'objet
    n'existe pas encore dans le dépôt — ne pas l'halluciner avant création) ;
  - la **jurisprudence de fond** (contentieux d'autorisation, contentieux
    d'accès aux images) → `recherche-juridique`.

---

## 1. Questions couvertes

- Mise en place ou extension d'un système de vidéoprotection sur voie publique
  ou dans un lieu ouvert au public.
- Demande, instruction et renouvellement de l'**autorisation préfectorale**.
- Finalités légales mobilisables et leur adéquation au projet.
- Durée de conservation des images et destruction.
- Qui peut **visionner** (agents PM, policiers nationaux, gendarmes, agents
  d'autres services) et sous quelles conditions d'habilitation.
- Fonctionnement du **CSU** : accès, traçabilité, transmission aux forces de
  l'État, réquisitions judiciaires sur images.
- Droits des personnes filmées (information, accès, recours).
- Articulation avec la vidéoprotection commerçants et la transmission vers les
  forces de l'État.

---

## 2. Arbre de traitement

`question → variables à lever (§4) → décision → vérification (§7) → écrit/livrable (§10)`

Réflexe imposé :
1. Identifier si le système relève du **CSI Titre V** (voie publique / lieux
   ouverts au public) ou d'un autre régime (locaux fermés, caméras
   individuelles, drones) → si autre régime, sortir de cette branche.
2. Identifier la **finalité légale** invoquée et l'**autorité compétente**
   (préfet, maire informé, commission départementale).
3. Vérifier l'existence et la validité de l'**autorisation préfectorale**
   (objet, périmètre, durée).
4. Qualifier l'**exploitation** envisagée (qui visionne, qui transmet, durée
   de conservation, traçabilité).
5. Vérifier le socle-sources (§7) avant toute affirmation sur durée, délai ou
   identifiant d'article.
6. Orienter vers l'écrit adapté (dossier de demande, note au maire, fiche de
   procédure CSU) ou vers `conformite-deontologie-donnees.md` pour le volet
   RGPD/AIPD.

---

## 3. Variables à lever

- **Nature du lieu filmé** : voie publique, abords d'un bâtiment public,
  établissement recevant du public, commerce (régime « commerçants »
  spécifique, sous condition d'information du maire).
- **Finalité poursuivie** : protection de bâtiments publics, prévention
  d'atteintes aux personnes et aux biens, prévention du trafic de stupéfiants,
  prévention d'actes de terrorisme, régulation du trafic routier, etc. — la
  finalité **conditionne** la légalité de l'autorisation.
- **Porteur du projet** : commune (maire demandeur le plus fréquent), EPCI,
  exploitant privé d'un lieu ouvert au public, commerçant.
- **Autorité compétente pour délivrer l'autorisation** : préfet de
  département ; **préfet de police à Paris** ; cas particulier d'un système
  s'étendant sur plusieurs départements → préfet du département du siège du
  demandeur.
- **Composition et rôle de la commission départementale de vidéoprotection**
  (avis préalable obligatoire) — à vérifier (composition réglementaire).
- **Qui visionne** : agents de police municipale du CSU, policiers nationaux,
  gendarmes, agents d'autres services mentionnés par les textes (douanes,
  services d'incendie et de secours) — chacun sous condition d'être
  **individuellement désigné et habilité**.
- **Durée de conservation envisagée** et **destination** des enregistrements
  (vidéoprotection courante vs réquisition judiciaire en cours).
- **Existence d'une convention de coordination ou d'un protocole CSU /
  forces de l'État** régissant la transmission d'images en temps réel →
  `continuum-partenariats.md`.

---

## 4. Règles métier

### 4.1 Régime d'autorisation préfectorale — principe

Police spéciale de l'État. L'installation d'un système de vidéoprotection sur
la voie publique ou dans un lieu ouvert au public **est soumise à
autorisation** du représentant de l'État dans le département (préfet) et, à
Paris, du préfet de police, donnée **après avis de la commission
départementale de vidéoprotection** :

> Art. L. 252-1, Code de la sécurité intérieure (vérifié sur Légifrance le
> 30/06/2026, identifiant LEGIARTI relevé pour les articles cités au §9).

Ce n'est **pas** un pouvoir du maire : le maire n'autorise pas le dispositif
(sauf le cas particulier de l'information préalable pour le dispositif
« commerçants », §4.2). Le maire est porteur de projet possible (demandeur),
mais l'autorité de décision reste le préfet. Si la commune installe sans
autorisation ou hors périmètre autorisé, c'est une irrégularité opposable.

### 4.2 Finalités légales — liste fermée, à vérifier

Le système ne peut être autorisé que pour l'une des **finalités limitativement
énumérées** par le texte (assurer la sécurité des personnes, prévention des
atteintes aux biens, régulation du trafic routier, protection des bâtiments
publics, prévention d'actes de terrorisme, prévention du trafic de
stupéfiants, etc.) :

> Art. L. 251-2, Code de la sécurité intérieure (vérifié sur Légifrance le
> 30/06/2026).

Cas particulier **commerçants** : un commerçant peut installer un système sur
la voie publique pour la protection des abords immédiats de son
établissement, **après information du maire** de la commune concernée et sous
autorisation de l'autorité publique compétente (préfet). L'information du
maire **n'est pas une autorisation municipale** — ne pas confondre les deux
rôles.

**Piège de qualification** : si la finalité réelle du projet ne correspond
à aucune des finalités listées (ex. surveillance générale sans lien avec un
risque identifié), le dossier est fragile au contentieux → signaler avant
rédaction de la demande.

### 4.3 Procédure d'instruction et avis de la commission départementale

L'autorisation est délivrée après avis (consultatif) de la **commission
départementale de vidéoprotection**, présidée par un magistrat. Sa
composition et ses modalités de saisine sont fixées par la partie
réglementaire du CSI — **à vérifier en version consolidée**, ne pas citer de
mémoire la composition exacte.

L'arrêté d'autorisation **fixe lui-même** les conditions opérationnelles :
qualité et habilitation des personnes en charge de l'exploitation et du
visionnage, mesures assurant le respect des règles du titre :

> Art. L. 252-2, al. 1, Code de la sécurité intérieure (vérifié sur
> Légifrance le 30/06/2026).

→ Conséquence pratique : **lire l'arrêté préfectoral lui-même** avant toute
décision d'exploitation. Le CSI fixe le cadre, l'arrêté individualise les
conditions (zones filmées, durée, accès).

### 4.4 Durée de l'autorisation et renouvellement

L'autorisation est délivrée pour une **durée déterminée, renouvelable** —
durée à vérifier en version consolidée (régime fixé par décret d'application,
ne pas citer de chiffre de mémoire). Toute modification substantielle du
système (extension de périmètre, changement de finalité, ajout de caméras
significatif) impose en principe une nouvelle demande ou une modification de
l'autorisation existante — vérifier le seuil de modification déclenchant une
nouvelle instruction.

### 4.5 Durée de conservation des images

L'autorisation **fixe elle-même** les modalités de transmission des images,
d'accès aux enregistrements, et la **durée de conservation**, dans la limite
d'un plafond légal :

> Art. L. 252-3, Code de la sécurité intérieure (vérifié sur Légifrance le
> 30/06/2026) : durée de conservation plafonnée, fixée par l'autorisation,
> **sans préjudice des nécessités de conservation pour une procédure
> pénale**.

Règles à retenir :
- la durée précise (plafond légal en jours) est une **valeur réglementaire à
  vérifier** — ne jamais l'affirmer de mémoire (§9) ;
- **hors réquisition judiciaire**, l'enregistrement doit être **détruit** au
  terme du délai fixé par l'autorisation ;
- une **réquisition judiciaire** (sur le fondement du CPP, hors présente
  branche) suspend la destruction pour les images concernées — coordonner
  avec `penal-procedure.md` si une exploitation judiciaire est en cours.

### 4.6 Qui peut visionner — habilitation individuelle

Principe : seuls des **agents individuellement désignés et habilités** par
l'autorité compétente peuvent visionner les images, dans les conditions
fixées par l'autorisation :

> Art. L. 252-2, Code de la sécurité intérieure (vérifié sur Légifrance le
> 30/06/2026) : pour les systèmes relevant du dernier alinéa de l'art.
> L. 251-2 (cas spécifique), le visionnage est réservé aux agents de police
> nationale et de gendarmerie individuellement désignés et habilités ; pour
> les autres cas, l'autorisation peut prévoir des destinataires
> supplémentaires (police municipale, douanes, services d'incendie et de
> secours), désignés et habilités dans les mêmes conditions.

Conséquence pour le CSU :
- vérifier que **chaque agent affecté au CSU** dispose d'une habilitation
  individuelle traçable, conforme à ce que prévoit l'arrêté préfectoral ;
- un agent PM non habilité ne visionne pas, même en présence d'un agent
  habilité, sauf disposition contraire expressément prévue ;
- la **transmission en temps réel vers les forces de l'État** (police
  nationale, gendarmerie) est possible si l'autorisation le prévoit et selon
  les modalités qu'elle fixe ; formaliser ce point dans la convention de
  coordination → `continuum-partenariats.md`.

### 4.7 Exploitation du CSU — points de vigilance opérationnels

- **Traçabilité des accès** : journal des connexions, des extractions, des
  visionnages — exigence de fond du régime, modalités précises à vérifier
  dans l'arrêté et la réglementation applicable.
- **Extraction d'images pour une procédure** : l'extraction et la remise à
  l'autorité judiciaire (réquisition, sur PV) relèvent de la procédure pénale
  — coordonner avec `penal-procedure.md` ; au-delà de la simple remise sur
  réquisition, toute exploitation active (analyse poussée, rapprochement)
  dépassant le cadre APJA bascule vers le **garde-fou §5.2 du SKILL.md**.
- **Lecture de plaque (LAPI), reconnaissance faciale ou tout traitement
  algorithmique additionnel** : régime distinct, hors présent périmètre —
  ne pas présumer la légalité d'un dispositif algorithmique du seul fait que
  l'autorisation vidéoprotection existe ; vérifier un fondement spécifique
  avant tout déploiement (point de risque élevé, §11).
- **Sécurité du système** (accès physique au CSU, droits informatiques,
  habilitations techniques) : volet sécurité des systèmes d'information, à
  croiser avec `conformite-deontologie-donnees.md`.

### 4.8 Droits des personnes filmées

Toute personne intéressée peut s'adresser au responsable du système pour
obtenir l'**accès aux enregistrements la concernant**, ou vérifier leur
destruction dans le délai prescrit. Ce droit est **de droit**, sous réserve de
motifs de refus limitativement prévus (sûreté de l'État, défense, sécurité
publique, procédure judiciaire en cours, droits des tiers) :

> Art. L. 253-5, Code de la sécurité intérieure (vérifié sur Légifrance le
> 30/06/2026).

En cas de difficulté, la personne peut saisir la **commission départementale
de vidéoprotection** ou la **CNIL**, sans préjudice du recours juridictionnel
(y compris en référé).

> Information générale du public (panneaux, mentions d'information, registre
> des traitements, AIPD) → régime RGPD/CNIL transverse, **non traité ici** →
> `references/conformite-deontologie-donnees.md`.

---

## 5. Procédures et délais

| Étape | Acteur | Point de contrôle |
|---|---|---|
| Élaboration du projet (lieux, finalité, périmètre) | Porteur de projet (commune/maire le plus souvent) | Finalité parmi la liste légale (§4.2) |
| Dépôt du dossier de demande d'autorisation | Porteur de projet → préfecture | Pièces du dossier réglementaire — à vérifier (partie réglementaire CSI) |
| Avis de la commission départementale | Commission départementale de vidéoprotection | Avis consultatif ; délai d'instruction à vérifier |
| Décision (arrêté préfectoral) | Préfet (préfet de police à Paris) | Fixe finalité, périmètre, durée de conservation, habilitations |
| Mise en service | Porteur de projet / CSU | Conformité stricte au périmètre et aux conditions de l'arrêté |
| Renouvellement avant échéance | Porteur de projet | Anticiper le délai de dépôt avant expiration — à vérifier |
| Modification substantielle | Porteur de projet | Nouvelle demande ou modification d'autorisation selon seuil — à vérifier |
| Contrôle | Commission départementale / CNIL | Pouvoir de contrôle sur place, recommandations |
| Destruction des images | Responsable du système / CSU | À l'échéance fixée par l'autorisation, sauf procédure en cours |

**Hypothèses à annoncer** : tout délai d'instruction, tout délai de dépôt de
renouvellement, et toute composition de commission cités dans un écrit
doivent être vérifiés en version consolidée avant envoi — ne jamais les
donner de mémoire dans un acte.

---

## 6. Déclencheurs de vérification

Appliquer le socle-sources (matrice §2.2 du `SKILL.md`) dès que :
- une **durée de conservation** ou un **délai de procédure** est annoncé à un
  tiers ou inséré dans un acte ;
- une **finalité** est qualifiée pour fonder une demande d'autorisation
  (risque de rejet ou d'annulation si finalité mal qualifiée) ;
- une **habilitation de visionnage** est attribuée ou retirée à un agent ;
- un **refus d'accès** aux images est opposé à une personne intéressée
  (vérifier que le motif invoqué figure bien dans la liste légale) ;
- un **dispositif algorithmique additionnel** (LAPI, etc.) est envisagé ;
- une **réforme récente** du régime CSI vidéoprotection est suspectée
  (évolutions fréquentes de ce titre) → orientation possible vers
  `recherche-juridique`.

---

## 7. Pièges & confusions fréquentes

1. Croire que le **maire autorise** l'installation : c'est le **préfet**, sauf
   confusion avec la simple **information du maire** dans le cas
   « commerçants » (§4.2).
2. Confondre le **régime CSI Titre V** (voie publique, lieux ouverts au
   public) avec la vidéosurveillance de **locaux fermés non ouverts au
   public**, qui relève d'un autre régime.
3. Laisser visionner les images par un agent **non individuellement
   habilité** : l'habilitation est strictement nominative, pas générique au
   service.
4. Affirmer une **durée de conservation chiffrée** sans vérifier l'arrêté
   préfectoral applicable et la version en vigueur du plafond légal.
5. Oublier que la **réquisition judiciaire** suspend la destruction : une
   destruction automatique sur images sous procédure expose à un risque
   pénal/disciplinaire — coordonner avec `penal-procedure.md`.
6. Présumer la légalité d'un **traitement algorithmique additionnel**
   (reconnaissance faciale, LAPI) du seul fait de l'autorisation
   vidéoprotection existante : fondement distinct à vérifier.
7. Traiter le sujet **RGPD/AIPD** dans cette branche au lieu de renvoyer à
   `conformite-deontologie-donnees.md`.
8. Oublier le **droit d'accès** des personnes filmées et ses motifs de refus
   limitatifs (§4.8) lors d'une demande administrée.
9. Exploiter le CSU au-delà de la simple **constatation et transmission**
   (analyse, rapprochement actif) sans en mesurer la portée au regard du
   garde-fou APJA (§5.2 SKILL.md).

---

## 8. Données / références à vérifier

**Vérifiées sur Légifrance le 30/06/2026** (à recontrôler en version
consolidée avant tout acte, car ce titre évolue fréquemment) :
- **Art. L. 251-1 CSI** — disposition générale, identifiant Légifrance
  LEGIARTI000047569469.
- **Art. L. 251-2 CSI** — finalités légales et cas « commerçants »,
  identifiant Légifrance LEGIARTI000041599395 (version relevée ; vérifier la
  version applicable à la date des faits).
- **Art. L. 252-1 CSI** — autorisation préfectorale et commission
  départementale (référence de section confirmée ; identifiant LEGIARTI
  précis de la version en vigueur à relever à nouveau au moment de l'usage).
- **Art. L. 252-2 CSI** — conditions de visionnage et d'habilitation,
  identifiant Légifrance LEGIARTI000047569434.
- **Art. L. 252-3 CSI** — durée de conservation et transmission,
  identifiant Légifrance LEGIARTI000043540807.
- **Art. L. 253-5 CSI** — droit d'accès des personnes filmées, identifiant
  Légifrance LEGIARTI000038791144 (version relevée le 16/10/2020 ; **revérifier
  la version en vigueur** avant citation dans un acte).

**Non vérifiées dans cette session — à confirmer en version consolidée avant
usage** :
- Partie réglementaire (articles R. 251 et s., R. 252 et s., R. 253 et s.) :
  composition de la commission départementale, pièces du dossier de demande,
  délais d'instruction.
- Décret d'application le plus récent du régime (vu en résultat de recherche :
  un décret de 2023 modifiant le régime vidéoprotection et caméras
  aéroportées — **ne pas citer son numéro ou sa date de mémoire**, le
  revérifier et le viser explicitement s'il est mobilisé dans un acte).
- Durée précise du plafond légal de conservation et durée de validité de
  l'autorisation (chiffres non confirmés dans cette session).
- Régime des caméras individuelles et des drones (hors périmètre, fondement
  distinct à vérifier séparément si la question se pose).

---

## 9. Écrits & livrables

1. **Dossier de demande d'autorisation préfectorale** — pièces réglementaires
   à vérifier ; produire un brouillon `[INCOMPLET]` si une pièce manque
   (finalité, plan, périmètre, durée de conservation envisagée).
2. **Note au maire** — opportunité d'un projet de vidéoprotection, choix de
   la finalité, articulation avec le CSU existant → gabarit
   `assets/note-maire-modele.md`.
3. **Arrêté municipal connexe** (le cas échéant : réglementation d'usage
   interne, organisation du CSU) — **acte faisant grief** seulement s'il
   affecte des droits individuels ; sinon acte d'organisation interne.
   Vérifier dans tous les cas via `controle-legalite.md` avant production.
4. **Fiche de procédure CSU** (habilitations, traçabilité, modalités de
   transmission aux forces de l'État) — articuler avec la convention de
   coordination → `continuum-partenariats.md`.
5. **Réponse à une demande d'accès aux images** (art. L. 253-5) — motiver tout
   refus par l'un des motifs légaux limitatifs ; sinon accès de droit.
6. **Volet RGPD/AIPD du projet** (registre, analyse d'impact, mentions
   d'information) → ne pas produire ici, renvoyer à
   `conformite-deontologie-donnees.md`.

---

## 10. Double échelle [risque / confiance]

| Sous-domaine | Risque | Confiance | Repère |
|---|---|---|---|
| Existence du régime d'autorisation préfectorale | Élevé | Stable | Principe constant (§4.1) |
| Liste des finalités légales | Élevé | À vérifier | Modifications législatives fréquentes (§4.2) |
| Durée précise de conservation (chiffre) | Élevé | À vérifier | Valeur réglementaire, jamais de mémoire (§4.5, §9) |
| Habilitation individuelle de visionnage | Élevé | Stable dans le principe | Modalités précises selon arrêté (§4.6) |
| Droit d'accès des personnes filmées | Moyen | Stable | Motifs de refus limitatifs (§4.8) |
| Dispositifs algorithmiques additionnels (LAPI, reconnaissance faciale) | Critique | À vérifier / débattu | Fondement distinct, contentieux sensible |
| Articulation avec procédure judiciaire en cours | Critique | Stable dans le principe | Coordination obligatoire avec `penal-procedure.md` |

---

## 11. Checklist de branche

1. Le système relève-t-il bien du **CSI Titre V** (voie publique / lieu
   ouvert au public), et non d'un autre régime (locaux fermés, caméra
   individuelle, drone) ?
2. **Autorité compétente** correctement identifiée : préfet (préfet de police
   à Paris), pas le maire — sauf cas « commerçants » (information du maire) ?
3. **Finalité légale** précisément qualifiée et cohérente avec le projet ?
4. **Durée de conservation** et **modalités de visionnage** renvoyées à
   l'arrêté préfectoral applicable, jamais affirmées de mémoire ?
5. **Habilitations individuelles** des agents du CSU vérifiées et tracées ?
6. **Réquisition judiciaire en cours** détectée avant toute destruction
   d'images → coordination `penal-procedure.md` ?
7. **Garde-fou APJA (§5.2 SKILL.md)** testé si l'exploitation du CSU dépasse
   la simple constatation/transmission ?
8. **Volet RGPD/AIPD** renvoyé à `conformite-deontologie-donnees.md`, pas
   traité ici ?
9. **Droit d'accès** d'une personne filmée traité avec un motif de refus
   limitatif si refus opposé ?
10. Si **acte produit** (arrêté, note) : passage par `controle-legalite.md`,
    motivation et voies de recours si acte faisant grief ?
11. Toute référence d'article assortie de sa réserve « à confirmer en version
    consolidée » sauf vérification explicite de cette session (§9) ?

[risque : élevé sur le principe d'autorisation et les durées de conservation /
confiance : stable sur l'architecture générale, à vérifier sur les valeurs
chiffrées et les évolutions réglementaires récentes]
