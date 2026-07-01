# Branche — RH spécificités PM (v0.1.0)

> Structure conforme à `_gabarit-branche.md`. Aucune valeur datée (montants,
> durées, quotas, taux) n'est donnée de mémoire : seules les **règles**
> figurent ici, avec la consigne de vérifier la version en vigueur. Cette
> branche est la **frontière la plus sensible** du skill avec `drh-fpt` : elle
> ne traite que ce que `SKILL.md` §5.4 conserve explicitement dans `dpm-fpt`.

## Périmètre / Exclusions

- **Périmètre** : spécificités RH propres au métier de police municipale
  conservées dans `dpm-fpt` — **agrément préfectoral et assermentation** ;
  **FIA et formation continue armement** (volet métier de la formation) ;
  **cycles atypiques et régime indemnitaire propre (ISFE)** dans leur logique
  opérationnelle ; **constat** du manquement déontologique (avant procédure) ;
  **commandement opérationnel de terrain**.
- **Exclusions** (délégué à `drh-fpt`) : **carrière, paie, avancement,
  positions statutaires** ; **RIFSEEP général** (la PM en est **hors champ** —
  voir §5.3) ; **instances et dialogue social** (CST, F3SCT) ; **PROCÉDURE
  disciplinaire** (saisine du conseil de discipline, droits de la défense,
  échelle des sanctions) ; **santé/QVT, masse salariale, SI RH,
  recrutement/formation général**. Pour le détail de ces sujets : voir
  `Drh-fpt/references/carriere-paie.md` (notamment son §5.7 sur l'ISFE et son
  §5.5 sur l'échelle disciplinaire) et les autres branches de `drh-fpt`.

---

## 1. Questions couvertes

- Un agent peut-il exercer sans agrément préfectoral ou sans assermentation
  préalable ? Que faire en cas de retrait ou de suspension ?
- Quelle est la différence entre la **formation initiale d'application (FIA)**
  et la formation continue obligatoire **armement**, et que couvre `dpm-fpt`
  par rapport à `drh-fpt` sur ce point ?
- Comment qualifier un **cycle horaire atypique** (nuit, week-end, jours
  fériés, brigade canine, ASVP en horaires décalés) du point de vue métier, et
  où s'arrête la compétence de cette branche sur le régime indemnitaire **ISFE**
  qui y est lié ?
- Un agent a un comportement qui pose question au regard du **code de
  déontologie** : à quel moment `dpm-fpt` répond encore, à quel moment la main
  passe-t-elle à `drh-fpt` ?
- Qui exerce le **commandement opérationnel de terrain** lors d'une
  intervention ou d'un dispositif, et comment cette autorité fonctionnelle
  s'articule avec la hiérarchie statutaire ?
- Une question m'arrive sur la **carrière, la paie ou une instance** d'un
  agent PM : dois-je la traiter ici ?

---

## 2. Arbre de traitement

`question → variables à lever (§4) → test frontière dpm-fpt / drh-fpt (§5.0) → décision → vérification (§7) → écrit/livrable (§10)`

**Réflexe imposé avant toute réponse** : tester si la question relève d'une
des **cinq poches conservées** (§0 du tableau ci-dessous) ou si elle bascule
côté `drh-fpt`. Ne jamais traiter sur le fond un sujet de carrière, de paie,
d'instance ou de procédure disciplinaire : renvoyer, sans reformuler le détail
statutaire.

---

## 3. Variables à lever

- **Nature de la question** : métier opérationnel (agrément, FIA armement,
  cycle de service, constat déontologique, commandement) vs statutaire
  (carrière, paie, instance, procédure) — détermine la branche compétente
  avant tout développement.
- **Stade du dossier** : simple **constat** d'un fait au regard du code de
  déontologie, ou **ouverture d'une procédure** (déjà saisine, déjà notification
  de griefs) — la règle de bascule (§5.0) en dépend directement.
- **Statut d'agrément/assermentation de l'agent** : agréé et assermenté en
  cours de validité, en cours d'instruction, suspendu, ou retiré — conditionne
  toute habilitation à agir comme APJA.
- **Cadre d'emplois et fonctions exactes** (chef de service, directeur,
  agent, garde champêtre) : conditionne le régime indemnitaire ISFE et le
  niveau de commandement.
- **Existence d'une convention de coordination** PM/forces de l'État en
  vigueur, et des plages horaires qu'elle fixe (`continuum-partenariats.md`) —
  paramètre souvent imbriqué avec les cycles atypiques.
- **Date de référence** des faits ou de l'acte (le cadre RH propre à la PM a
  été modifié récemment, notamment par le décret n° 2024-614 du 26 juin 2024
  sur l'ISFE — à confirmer pour la situation traitée).

---

## 4. Règles métier

### 4.0 Règle de bascule dpm-fpt / drh-fpt — à tester en premier

| Conservé ici (`dpm-fpt`) | Délégué à `drh-fpt` |
|---|---|
| Agrément préfectoral + assermentation | Carrière, paie, avancement, positions statutaires |
| FIA et formation continue **armement** | RIFSEEP général |
| Cycles atypiques + logique métier du régime indemnitaire propre (ISFE) | Instances et dialogue social (CST, F3SCT) |
| **Constat** du manquement déontologique | **Procédure** disciplinaire (saisine conseil, droits de la défense, échelle des sanctions) |
| Commandement opérationnel de terrain | Santé/QVT, masse salariale, SI RH, recrutement/formation général |

**Règle pratique** : tant que la question porte sur le **texte applicable et
le constat des faits au regard de ce texte**, `dpm-fpt` répond. Dès qu'elle
porte sur la **conduite procédurale** (qui notifie, quels délais, quelle
instance, quels droits de la défense, quelle sanction), passer la main à
`drh-fpt` (`Drh-fpt/references/carriere-paie.md`, §5.5) **sans reformuler le
détail procédural ici**, même partiellement.

### 4.1 Agrément préfectoral et assermentation

- **Double condition cumulative et personnelle** : un agent de police
  municipale n'exerce légalement ses pouvoirs (notamment APJA) qu'une fois
  **nommé** par le maire (ou le président de l'EPCI compétent), **agréé** par
  le représentant de l'État dans le département et le procureur de la
  République, **puis assermenté** (CSI, art. **L. 511-2**, *vérifié sur
  Légifrance le 2026-06-30* — LEGIARTI000043540434). L'agrément et
  l'assermentation **demeurent valables** tant que l'agent continue d'exercer
  ses fonctions d'agent de police municipale — ils ne sont **pas** à renouveler
  à échéance fixe, sauf changement de collectivité ou retrait.
- **Autorités compétentes** : le maire (ou président d'EPCI) **nomme** ;
  l'**État** (préfet) et le **procureur de la République** **agréent**,
  conjointement — ce n'est ni un pouvoir municipal seul, ni un pouvoir
  exclusivement étatique.
- **Retrait ou suspension** : l'agrément peut être **retiré ou suspendu** par
  le préfet ou le procureur, **après consultation** du maire ou du président
  de l'EPCI ; **en cas d'urgence**, le procureur peut suspendre **sans cette
  consultation préalable** (CSI, art. L. 511-2, *vérifié sur Légifrance le
  2026-06-30*). Effet immédiat sur l'habilitation à agir : un agent dont
  l'agrément est retiré ou suspendu **perd sa qualité d'APJA** et ne peut plus
  exercer aucun acte qui en dépend.
- **Cas particuliers** : l'agrément peut aussi être délivré à des agents
  communaux habituellement affectés à d'autres fonctions, ou à des agents non
  titulaires, pour assister temporairement les agents de police municipale
  dans les communes touristiques et les stations classées — ces agents ne
  peuvent **porter aucune arme** (CSI, art. L. 511-2 — à confirmer le détail
  exact en version consolidée).
- **Effet sur la qualité d'APJA** : l'agrément et l'assermentation sont une
  **condition d'exercice**, pas une formalité accessoire. Toute absence,
  expiration de fait (changement de collectivité sans nouvel agrément) ou
  retrait expose à une **irrégularité de procédure** sur tout acte de
  constatation pris dans l'intervalle. Croiser systématiquement avec
  `penal-procedure.md` avant de valider un acte APJA.
- **Frontière avec `drh-fpt`** : le **recrutement et la titularisation**
  statutaires de l'agent (stage, intégration, mutation) relèvent de
  `drh-fpt` ; **seule** la condition d'agrément/assermentation propre au
  métier PM reste ici.

### 4.2 FIA et formation continue armement

- La **formation initiale d'application (FIA)**, généraliste, organisée par
  le CNFPT pour le cadre d'emplois, relève de `drh-fpt` (formation générale,
  §5.4 SKILL.md) — **sauf** son **volet armement**, qui reste ici.
- **Spécificité conservée** : la **formation préalable au port d'arme** et
  l'**entraînement périodique obligatoire** (maniement, tir) qui conditionnent
  le **maintien de l'autorisation préfectorale de port d'arme** sont traités
  en détail dans `armement-equipements.md` (§4.7) — **ne pas dupliquer ici**,
  renvoyer systématiquement à cette branche pour le contenu, la périodicité et
  la traçabilité de cette formation.
- **Articulation** : cette branche RH ne fait que **rappeler la frontière** —
  le contenu métier de la formation armement (texte applicable, fréquence,
  conditions de retrait du droit de port en cas de non-respect) est intégralement
  dans `armement-equipements.md`.

### 4.3 Cycles atypiques et régime indemnitaire propre (ISFE)

- **Cycles atypiques** : la police municipale fonctionne souvent en horaires
  décalés (nuit, week-end, jours fériés, services en cycle), notamment pour
  couvrir les plages fixées par une éventuelle **convention de coordination**
  (le service ne peut en principe intervenir qu'entre certaines plages
  horaires sauf exception **gardes statiques** et **manifestations
  organisées par la commune**, sauf stipulation contraire de la convention —
  CSI, art. **L. 512-2 et s.**, *rattachement à confirmer en version
  consolidée*, voir `continuum-partenariats.md` pour le contenu de la
  convention). L'**organisation du cycle de travail** lui-même (durée annuelle
  de référence, régime des heures supplémentaires, astreintes) relève du
  **temps de travail statutaire général** → `drh-fpt`
  (`Drh-fpt/references/carriere-paie.md`, §5.9). **Ce qui reste ici** : la
  **logique métier** du cycle (pourquoi le service est organisé ainsi au
  regard des missions et de la convention), pas le régime juridique du temps
  de travail.
- **Régime indemnitaire propre — ISFE** : la filière police municipale et les
  gardes champêtres sont **hors RIFSEEP**. Le régime indemnitaire propre,
  l'**Indemnité Spéciale de Fonction et d'Engagement (ISFE)**, est fondé sur
  l'art. **L. 714-13 du CGFP** et institué par le **décret n° 2024-614 du 26
  juin 2024** (deux parts : fixe + variable liée à l'engagement) — détail
  intégral, plafonds, procédure d'institution, clause de sauvegarde, et
  abrogation des anciens régimes (décrets n° 97-702, 2000-45, 2006-1397) dans
  `Drh-fpt/references/carriere-paie.md` (§5.7). **Ne pas redévelopper ce
  détail ici** : seule la **logique métier** du lien entre sujétions de
  service (nuit, dimanche, jours fériés, astreintes, engagement
  opérationnel) et part variable de l'ISFE relève de cette branche, comme
  élément de pilotage du service (organisation des roulements, valorisation
  de l'engagement) ; le **calcul, la délibération et les arrêtés individuels**
  relèvent de `drh-fpt`.
- **Frontière pratique** : si la question est « combien », « selon quel
  plafond », « quelle procédure d'institution », « quel arrêté individuel » →
  `drh-fpt`. Si la question est « comment organiser le service compte tenu
  des contraintes horaires et de l'engagement attendu » → cette branche
  (`doctrine-operationnelle.md` pour le détail des dispositifs).

### 4.4 Constat du manquement déontologique

- Le **code de déontologie des agents de police municipale** (CSI, partie
  réglementaire, Livre V — rattachement général **vérifié sur Légifrance le
  2026-06-30** dans `socle-sources-verification.md` ; numéro précis d'article
  applicable à confirmer en version consolidée) fixe les devoirs
  professionnels : dignité, probité, impartialité, discrétion, usage
  proportionné de la force, rapports avec le public et la hiérarchie.
- **Ce que `dpm-fpt` traite** : le **constat textuel** — qualifier un fait
  rapporté au regard du code de déontologie (quel devoir est en cause, quel
  texte le fonde), à l'occasion d'un **rapport d'information**, d'un
  **compte rendu hiérarchique**, ou d'une **observation de terrain** — voir
  `conformite-deontologie-donnees.md` pour le détail de la grille de constat
  et `ecrits-professionnels.md` pour le rapport correspondant.
- **Ce que `dpm-fpt` ne traite jamais** : dès que le dossier **bascule en
  procédure** — notification de griefs, communication du dossier, saisine du
  conseil de discipline, mesures conservatoires (suspension), échelle des
  sanctions, droits de la défense — la main passe **immédiatement** à
  `drh-fpt` (`Drh-fpt/references/carriere-paie.md`, §5.5). Ce basculement
  s'opère **dès le premier acte de procédure**, pas seulement à la sanction
  finale.
- **Cas particulier — manquement avec dimension pénale** (usage disproportionné
  de la force, violences) : tester **prioritairement** le garde-fou APJA
  (`SKILL.md` §5.2) — l'agent peut lui-même devenir mis en cause pénalement,
  ce qui prime sur le traitement déontologique interne. Voir
  `armement-equipements.md` (§4.4 et §7) pour l'articulation usage de la
  force / garde-fou APJA.

### 4.5 Commandement opérationnel de terrain

- **Double hiérarchie à distinguer** :
  - **hiérarchie statutaire** : grade, cadre d'emplois, position dans
    l'organigramme — relève de `drh-fpt` (carrière, positions) ;
  - **hiérarchie fonctionnelle/opérationnelle** : autorité de commandement
    exercée **sur le terrain**, pendant une intervention ou un dispositif,
    indépendamment du grade statutaire dans certains schémas d'organisation
    (chef de poste, coordinateur d'un dispositif événementiel, officier de
    garde) — relève de **cette branche**.
- Les agents de police municipale agissent **sous l'autorité du maire**
  (CGCT, art. **L. 2212-5**, *vérifié sur Légifrance le 2026-06-30* —
  rattachement confirmé : les agents exécutent, dans la limite de leurs
  attributions et sous l'autorité du maire, les tâches relevant de la
  compétence de celui-ci en matière de prévention et de surveillance du bon
  ordre, de la tranquillité, de la sécurité et de la salubrité publiques).
  Le **maire** reste le **titulaire du pouvoir de police** ; le
  **commandement opérationnel** (organisation des patrouilles, répartition
  des moyens, direction d'un dispositif) est **délégué en pratique** au
  directeur ou chef de service, dans le cadre fixé par le maire — sans que
  cela transfère le pouvoir de police lui-même (`pouvoirs-police.md`).
- **Le commandement opérationnel de terrain conservé ici** couvre : la
  **doctrine de commandement** (qui dirige une intervention, une patrouille,
  un dispositif), la **chaîne de remontée d'information** vers le directeur
  et le maire, et l'**articulation avec les forces de l'État** sur le terrain
  (`continuum-partenariats.md`). Le **contenu opérationnel détaillé**
  (organisation des patrouilles, doctrine d'engagement, gestion de crise)
  relève de `doctrine-operationnelle.md` — cette branche **ne fait que
  poser le repère RH** : qui commande, à quel titre, et où s'arrête ce
  commandement par rapport à la hiérarchie statutaire.
- **Piège à éviter** : présenter le commandement opérationnel comme une
  **délégation de pouvoir de police** au sens juridique (acte formalisé,
  publié, qui engagerait la responsabilité du maire pour la décision
  elle-même) sans vérifier s'il s'agit d'une simple **organisation interne du
  service** (pas d'acte formalisé requis) ou d'une véritable **délégation de
  signature/fonction** — distinction à trancher au cas par cas via
  `pouvoirs-police.md` et `controle-legalite.md`.

---

## 5. Procédures et délais

Cette branche **ne décrit pas de procédure complète** sur les sujets délégués
(carrière, discipline) : se reporter à `drh-fpt`. Sur les sujets conservés :

### 5.1 Agrément — étapes côté `dpm-fpt`
1. **Nomination** par le maire ou le président de l'EPCI.
2. **Demande d'agrément** transmise au préfet et au procureur de la
   République.
3. **Agrément** délivré conjointement (délai d'instruction à vérifier au cas
   par cas, non figé ici).
4. **Assermentation** devant le tribunal compétent (modalités à vérifier en
   version consolidée).
5. **Suivi de la validité** : pas de renouvellement périodique automatique,
   mais vigilance en cas de mutation, de changement de collectivité, ou de
   procédure de retrait/suspension en cours.

### 5.2 Constat déontologique — points de bascule à surveiller
- Observation/rapport initial → **constat** (cette branche).
- Dès **notification de griefs** ou **saisine d'une instance** → bascule
  immédiate `drh-fpt`, sans rédiger d'élément de procédure ici.
- Si dimension pénale → garde-fou APJA **avant** tout, puis
  `penal-procedure.md`.

---

## 6. Déclencheurs de vérification

Appliquer le socle-sources (`SKILL.md` §2.2 et §5.3) avant de conclure dès
que :
- le **statut d'agrément ou d'assermentation** d'un agent conditionne la
  validité d'un acte APJA ;
- une question porte sur le **contenu précis du code de déontologie** PM
  (numéro d'article exact) ;
- une question touche au **régime indemnitaire ISFE** au-delà de sa logique
  métier (taux, plafonds, procédure) → orienter vers `drh-fpt` plutôt que de
  vérifier ici ;
- un doute existe sur le **point de bascule** constat / procédure
  disciplinaire dans un dossier concret ;
- une **réforme récente** touche l'agrément, l'assermentation, ou l'ISFE
  (décret n° 2024-614 du 26 juin 2024 et ses suites).

---

## 7. Pièges & confusions fréquentes

1. Traiter une question de **carrière, paie, avancement ou instance** sur
   cette branche au lieu de renvoyer immédiatement à `drh-fpt`.
2. Confondre **constat** déontologique (ici) et **procédure** disciplinaire
   (`drh-fpt`) : le basculement intervient **dès le premier acte de
   procédure**, pas seulement à la sanction.
3. Croire l'agrément/l'assermentation **renouvelables périodiquement** :
   ils sont valables **tant que l'agent exerce**, sauf retrait, suspension ou
   changement de collectivité.
4. Oublier que le **procureur peut suspendre seul, en urgence**, sans
   consultation préalable du maire — ne pas présenter la consultation comme
   systématiquement préalable.
5. Traiter l'**ISFE en détail** (plafonds, calcul, procédure d'institution)
   ici au lieu de renvoyer à `drh-fpt` (`carriere-paie.md` §5.7) — cette
   branche n'en garde que la **logique métier** des cycles et sujétions.
6. Confondre **hiérarchie statutaire** (grade) et **commandement
   opérationnel de terrain** (autorité fonctionnelle) : un agent gradé
   inférieur peut, selon l'organisation, diriger un dispositif ponctuel sans
   que cela modifie sa position statutaire.
7. Présenter le commandement opérationnel comme une **délégation de pouvoir
   de police** formalisée sans vérifier s'il s'agit d'une simple
   organisation interne.
8. Redévelopper le contenu de la **formation armement** ici plutôt que de
   renvoyer à `armement-equipements.md` (§4.7), qui en a la charge complète.
9. Ignorer le **garde-fou APJA** lorsqu'un manquement déontologique a une
   dimension pénale (usage de la force).

---

## 8. Données / références à vérifier

- **CSI, art. L. 511-2** (nomination, agrément préfectoral et du procureur,
  assermentation, retrait/suspension) — *vérifié sur Légifrance le
  2026-06-30*, identifiant LEGIARTI000043540434 ; revérifier la version en
  vigueur à la date des faits (l'article a été modifié, notamment par la loi
  n° 2021-646 du 25 mai 2021 — à confirmer en version consolidée).
- **CGCT, art. L. 2212-5** (agents PM agissant sous l'autorité du maire,
  exécution des arrêtés de police, constatation par procès-verbal) — *vérifié
  sur Légifrance le 2026-06-30* ; revérifier la version en vigueur à la date
  des faits.
- **CSI, art. L. 512-2 et s.** (plages horaires d'intervention, convention
  de coordination, exceptions gardes statiques/manifestations) —
  *rattachement identifié via recherche Légifrance le 2026-06-30* (article
  L. 512-5, LEGIARTI000041411429, notamment) ; numéro précis applicable à la
  question des cycles à reconfirmer en version consolidée. Voir
  `continuum-partenariats.md` pour le contenu de la convention.
- **CGFP, art. L. 714-13**, fondement de l'ISFE — *référence reprise de
  `Drh-fpt/references/carriere-paie.md` §5.7, non revérifiée dans cette
  session* — à confirmer en version consolidée avant toute citation en acte ;
  pour le détail (plafonds, procédure), se reporter à `drh-fpt`.
- **Décret n° 2024-614 du 26 juin 2024** relatif à l'ISFE des agents de
  police municipale et gardes champêtres — *référence reprise de
  `Drh-fpt/references/carriere-paie.md` §5.7, non revérifiée dans cette
  session* — à confirmer en version consolidée ; détail intégral dans
  `drh-fpt`.
- **Code de déontologie des agents de police municipale** (CSI, partie
  réglementaire, Livre V) — rattachement général repris de
  `socle-sources-verification.md` ; numéro précis d'article applicable à un
  manquement donné — **à confirmer en version consolidée**, jamais de
  mémoire.
- **Décret armement PM** (formation préalable, entraînement périodique) —
  voir `armement-equipements.md` (§8) pour les références déjà vérifiées,
  ne pas dupliquer ici.

---

## 9. Écrits & livrables

1. **Écrit de constatation / rapport** : **rapport d'information** ou
   **compte rendu hiérarchique** documentant un constat déontologique —
   `assets/rapport-information.md` (`ecrits-professionnels.md` pour le
   choix du gabarit). Rester sur le **constat factuel et textuel**, ne pas
   préjuger d'une sanction.
2. **Note** : **note au maire** sur l'état des agréments du service
   (agents agréés, agréments à surveiller, suspensions en cours), ou sur
   l'organisation du commandement opérationnel — `assets/note-maire-modele.md`.
3. **Transmission** : dès bascule en procédure disciplinaire ou en dimension
   pénale, **transmettre le dossier** à `drh-fpt` ou activer le garde-fou
   APJA — ne pas produire d'écrit de procédure ici.
4. **Acte faisant grief** : un éventuel **retrait/suspension d'agrément**
   relève de l'autorité préfectorale/du procureur, pas d'un acte produit par
   cette branche ; le **suivi administratif local** (note d'alerte au maire)
   reste possible. Pour tout acte communal faisant grief en matière RH
   (sanction, refus), voir `drh-fpt`.

---

## 10. Double échelle [risque / confiance]

- **Existence et conditions de l'agrément/assermentation** (CSI L. 511-2) :
  confiance **stable**, risque **élevé** (condition d'exercice de la qualité
  d'APJA — toute irrégularité expose l'acte à la nullité).
- **Frontière constat / procédure disciplinaire** : confiance **stable** sur
  le principe de répartition, risque **moyen à élevé** sur le tri d'un cas
  limite (un constat mal calibré peut vicier une procédure ultérieure ou, à
  l'inverse, priver l'agent de garanties).
- **Logique métier des cycles atypiques** : confiance **stable**, risque
  **faible à moyen** (organisationnel, sauf si la question dérive vers le
  régime juridique du temps de travail → `drh-fpt`).
- **ISFE — volet métier (cette branche)** : confiance **stable** sur le
  principe (hors RIFSEEP, régime propre) ; **toute valeur chiffrée ou
  procédure d'institution** → renvoyer à `drh-fpt`, ne pas trancher ici.
- **Commandement opérationnel de terrain** : confiance **à vérifier** au cas
  par cas (dépend de l'organisation locale du service, pas d'un texte unique
  et stable), risque **moyen** (organisationnel) à **élevé** si la question
  touche à une délégation formalisée de pouvoir.

---

## 11. Checklist de branche

1. La question a-t-elle été **testée contre le tableau de bascule (§4.0)**
   avant toute réponse sur le fond ?
2. Si la question est **statutaire** (carrière, paie, instance, procédure
   disciplinaire) : a-t-elle été **renvoyée à `drh-fpt`** sans en
   redévelopper le détail ?
3. **Agrément et assermentation** vérifiés avant d'affirmer la validité d'un
   acte APJA de l'agent concerné ?
4. **Constat vs procédure** déontologique : le point de bascule a-t-il été
   identifié, et la main passée à `drh-fpt` dès le premier acte procédural ?
5. Dimension **pénale** d'un manquement testée en priorité via le
   **garde-fou APJA** (`SKILL.md` §5.2) ?
6. **Formation armement** renvoyée à `armement-equipements.md` sans
   duplication de contenu ?
7. **ISFE** : seule la logique métier traitée ici, le détail chiffré et
   procédural renvoyé à `drh-fpt` ?
8. **Commandement opérationnel** distingué de la **hiérarchie statutaire** ?
9. Tout identifiant `LEGIARTI`/`JORFTEXT` cité provient-il d'un appel d'outil
   de la session, et non de la mémoire (règle de provenance, `SKILL.md`
   §5.3) ?

[risque / confiance] — Risque **élevé** sur l'agrément/assermentation
(condition d'exercice de la qualité d'APJA) et sur le tri constat/procédure
disciplinaire (vice de procédure possible des deux côtés) ; risque **moyen**
sur les cycles atypiques et le commandement opérationnel (organisationnel,
sauf dérive vers un acte formalisé). Confiance **stable** sur l'architecture
de la frontière `dpm-fpt`/`drh-fpt` elle-même (posée par `SKILL.md` §5.4) et
sur le principe de l'agrément CSI L. 511-2 ; **à vérifier systématiquement**
sur le numéro exact d'article du code de déontologie applicable à un cas
donné et sur toute valeur chiffrée ISFE (renvoyée à `drh-fpt`).
