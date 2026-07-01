# Branche — Conformité, déontologie & données (v0.1.0)

> Structure conforme à `_gabarit-branche.md`. Aucune valeur datée ni numéro
> d'article n'est donné de mémoire : seules les **règles** figurent ici, avec
> la consigne de vérifier la version en vigueur. Branche de **fusion** :
> déontologie professionnelle de l'agent PM + conformité données (RGPD, CRPA,
> AIPD, traçabilité).

## Périmètre / Exclusions

- **Périmètre** : code de déontologie des agents de police municipale (CSI,
  partie réglementaire — à confirmer), proportionnalité de l'usage de la
  force, responsabilité de l'agent et du service (pénale / administrative),
  contrôle interne ; volet données : RGPD, CRPA (accès aux documents
  administratifs), AIPD, traçabilité des consultations de fichiers.
- **Exclusions** : la **procédure disciplinaire** (saisine du conseil de
  discipline, droits de la défense, échelle des sanctions, prescription) →
  `drh-fpt` (`references/carriere-paie.md` §5.5). Cette branche s'arrête au
  **constat** du manquement déontologique ; dès que la **procédure**
  disciplinaire s'engage, passer la main (`SKILL.md` §5.4).

---

## 1. Questions couvertes

- Conformité d'un comportement ou d'un acte d'agent au code de déontologie PM.
- Proportionnalité et légalité de l'usage de la force (contrainte, moyens de
  force intermédiaire, arme).
- Régime de responsabilité applicable à un fait dommageable ou fautif (agent /
  commune / État).
- Organisation du contrôle interne du service (inspection, signalement,
  remontée hiérarchique, IGPM/IGA selon la taille du service).
- Droit d'accès aux documents administratifs détenus par la PM (mains
  courantes, rapports, images vidéoprotection) — articulation CRPA / RGPD.
- Obligations RGPD du service PM en tant que responsable de traitement
  (fichiers, mains courantes numériques, vidéoprotection, applications mobiles).
- Nécessité et conduite d'une analyse d'impact relative à la protection des
  données (AIPD).
- Traçabilité des consultations de fichiers (TAJ, FOVeS, SIV/SNPC, etc.) par
  les agents PM habilités.

---

## 2. Arbre de traitement

`question → variables à lever (§4) → décision → vérification (§7) → écrit/livrable (§10)`

1. Qualifier le fait : **comportement d'agent** (déontologie) ou **traitement
   de données** (RGPD/CRPA) — souvent les deux sont liés (ex. consultation
   irrégulière d'un fichier = manquement déontologique **et** incident RGPD).
2. Situer le niveau : **constat** (cette branche) vs **procédure**
   (`drh-fpt`) vs **pénale** (`penal-procedure.md` si l'agent ou un tiers est
   mis en cause au pénal).
3. Identifier l'autorité et le responsable de traitement compétents.
4. Vérifier la source avant toute affirmation relevant de la matrice §2.2 du
   `SKILL.md`.
5. Orienter vers l'écrit (rapport de manquement, fiche de signalement RGPD,
   registre AIPD, réponse CRPA).

---

## 3. Variables à lever

- **Nature du fait** : manquement déontologique pur, usage de la force,
  incident de traitement de données, ou cumul des trois.
- **Qualité de la personne concernée** : agent PM (titulaire, stagiaire,
  contractuel, garde champêtre), chef de service, ou tiers (administré dont
  les données sont traitées).
- **Stade** : avant tout signalement (constat) / signalement engagé / saisine
  disciplinaire déjà décidée (→ bascule `drh-fpt`).
- **Responsable de traitement** : commune (le plus souvent le maire) ou
  établissement public de coopération ; identifier le **délégué à la
  protection des données (DPO)** désigné, le cas échéant mutualisé au niveau
  intercommunal ou du centre de gestion.
- **Support du traitement** : main courante informatisée, logiciel métier PM,
  vidéoprotection, terminaux mobiles, interconnexions avec des fichiers d'État
  (TAJ, FOVeS, fichier des véhicules volés, etc.).
- **Demandeur CRPA** : administré lui-même (droit d'accès aux données
  personnelles, RGPD) ou tiers (accès à un document administratif, sous
  réserve d'occultation des données personnelles).

---

## 4. Règles métier

### 4.1 Code de déontologie des agents de police municipale

- Source : partie réglementaire du CSI, **art. R. 515-1 à R. 515-21**
  (*vérifié sur Légifrance le 2026-06-30*), créés par le **décret
  n° 2013-1113 du 4 décembre 2013** (en vigueur au 01/01/2014) ; ce chapitre
  constitue le code de déontologie des agents de police municipale et
  s'applique aux agents, chefs de service et directeurs de police municipale.
  L'ancien code autonome (décret n° 2003-735 du 1er août 2003) a été **abrogé
  et recodifié** dans le CSI. ➜ Il n'existe **pas** de « décret déontologie
  2022 ». Identifiants et versions consolidés → `references-verifiees.md` §3 ;
  recontrôler l'article applicable au fait examiné avant citation en acte.
- Contenu structurant (à vérifier article par article avant citation en
  acte) : respect de la loi et des libertés publiques, impartialité, probité,
  dignité en service et hors service, discrétion professionnelle, obéissance
  hiérarchique sauf ordre manifestement illégal, rapport à la hiérarchie,
  port de la tenue et des éléments d'identification, droits et devoirs
  respectifs des agents et des autorités de commandement.
- **Champ d'application** : tous les agents de police municipale, y compris
  chefs de service et directeurs ; ne couvre pas les ASVP ni les gardes
  champêtres au même titre (à vérifier le régime exact applicable à ces
  derniers) → si la question porte sur le statut de l'agent plutôt que sur le
  manquement, voir `rh-specificites-pm.md`.
- **Sanction d'un manquement** : la violation des devoirs définis par ce
  chapitre expose l'agent à une **sanction disciplinaire**, sans préjudice des
  **peines pénales** éventuellement encourues — **double voie cumulative**, à
  ne jamais présenter comme exclusive l'une de l'autre.

### 4.2 Usage de la force — principes de proportionnalité

- Distinguer deux fondements, à ne pas confondre :
  - **légitime défense** (droit commun, code pénal — à confirmer en version
    consolidée), ouverte à tout individu, agent ou non, dans les conditions
    de nécessité, simultanéité et proportionnalité ;
  - **usage de moyens de force dans le cadre des pouvoirs de police**
    (maintien/rétablissement de l'ordre, dispersion d'attroupement après
    sommations — CSI, livre II, ordre et sécurité publics — à confirmer),
    réservé en principe aux représentants de la force publique selon des
    conditions de nécessité absolue et de proportionnalité au trouble à faire
    cesser, avec cessation de l'usage de la force dès le trouble disparu.
- **Armement et moyens de force intermédiaire** des agents PM : autorisation
  préfectorale, conditions de port et d'usage, formation préalable obligatoire
  (FIA) → renvoi systématique à `armement-equipements.md` ; ne pas dupliquer
  ici le régime d'armement.
- **Principe de proportionnalité** : tout usage de la force doit être
  **nécessaire** (absence d'alternative moins coercitive), **adapté** (moyen
  proportionné à la menace) et **gradué** (cessation dès que le trouble
  cesse). C'est le standard de contrôle du juge (administratif et pénal) sur
  l'action de l'agent — jurisprudence de fond → `recherche-juridique`.
- **Vidéoprotection / caméras-piétons** comme élément de preuve et de
  contrôle de la proportionnalité de l'usage de la force : régime propre →
  `videoprotection.md` (transverse avec RGPD, §4.5 ci-dessous).

### 4.3 Responsabilité — pénale et administrative

- **Responsabilité pénale personnelle de l'agent** : engagée pour toute
  infraction commise (violences, abus d'autorité, atteinte aux libertés,
  manquement au devoir de probité) ; ne disparaît pas du fait de l'exercice
  des fonctions. La **faute personnelle détachable du service** reste
  imputable à l'agent seul.
- **Responsabilité administrative de la commune** : régime de la
  **faute de service**, engagée devant le juge administratif lorsque le
  dommage trouve son origine dans l'organisation ou le fonctionnement du
  service (faute simple en principe pour la PM, hors régimes spéciaux à
  vérifier). Distinguer faute de service (commune répond) et faute personnelle
  détachable (agent répond, la commune peut néanmoins indemniser la victime
  puis exercer une action récursoire contre l'agent — mécanisme à vérifier).
- **Cumul de fautes** : possible (faute personnelle commise à l'occasion du
  service et non dépourvue de tout lien avec lui) → la victime peut engager la
  responsabilité de l'administration, qui peut ensuite agir contre l'agent.
- **Protection fonctionnelle** : l'agent mis en cause (pénalement ou
  civilement) pour des faits commis dans l'exercice de ses fonctions peut
  solliciter la **protection fonctionnelle** de la collectivité (prise en
  charge des frais de défense, sauf faute personnelle détachable) — régime
  statutaire, conditions et exclusions à vérifier → volet procédural et
  instruction de la demande → `drh-fpt`.
- **Cumul procédures administrative / pénale / disciplinaire** : ces trois
  voies sont **indépendantes** (principe d'indépendance des procédures) et
  **cumulables** ; un classement sans suite pénal n'empêche pas une sanction
  disciplinaire, et inversement.

### 4.4 Contrôle interne

- Le contrôle interne du service relève du **directeur de police municipale**
  et de la chaîne hiérarchique : remontée systématique des incidents,
  signalement des manquements suspectés, traçabilité des décisions
  d'engagement de la force.
- Selon la taille et l'organisation du service : inspection interne, référent
  déontologie, ou saisine d'instances externes (IGA, déontologue de la
  collectivité) — modalités à vérifier au cas par cas, pas de cadre légal
  uniforme imposant une structure type pour la PM (à la différence de l'IGPN
  pour la police nationale).
- Le contrôle interne est le point d'entrée du **constat** du manquement
  (cette branche) avant toute éventuelle ouverture de **procédure
  disciplinaire** (`drh-fpt`).
- Articuler avec le déontologue compétent (si la collectivité en a désigné un
  au titre du droit de la fonction publique — référent déontologue, dispositif
  distinct du code de déontologie PM lui-même) — à vérifier.

### 4.5 RGPD — le service PM comme responsable de traitement

- Le RGPD (règlement UE 2016/679) et la loi Informatique et Libertés
  s'appliquent à tout traitement de données à caractère personnel opéré par le
  service PM (main courante informatisée, logiciel métier, vidéoprotection,
  applications de verbalisation mobile, fichiers locaux).
- **Responsable de traitement** : en principe le **maire** (ou le président de
  l'EPCI en cas de mutualisation), pas le directeur de police municipale à
  titre personnel — à vérifier selon l'organisation et les actes de
  délégation.
- **DPO** : désignation obligatoire pour les autorités publiques ; souvent
  mutualisée au niveau intercommunal ou via le centre de gestion. Vérifier
  l'identité du DPO compétent avant toute formalité.
- **Principes structurants à appliquer systématiquement** : finalité
  déterminée et légitime, minimisation des données collectées, durée de
  conservation limitée et documentée, sécurisation des accès, information des
  personnes concernées, droits d'accès/rectification/opposition (sous réserve
  des exceptions tenant à la sécurité publique et aux missions de police).
- **Régime spécifique « directive police-justice »** (traitements à finalité
  de prévention et de répression des infractions) : un sous-régime distinct du
  RGPD général peut s'appliquer aux traitements de la PM lorsqu'ils
  poursuivent une finalité de police judiciaire (ex. main courante alimentant
  des éléments transmis au parquet) — **vérifier le régime exact applicable
  par traitement avant toute conclusion**, ne pas appliquer mécaniquement le
  RGPD général sans examiner cette distinction.
- Articulation avec la vidéoprotection : régime d'autorisation propre
  (CSI) + RGPD/police-justice pour le traitement des images → ne pas dupliquer
  ici, voir `videoprotection.md`.

### 4.6 CRPA — accès aux documents administratifs

- Le **droit d'accès aux documents administratifs** (mains courantes,
  rapports, PV, images de vidéoprotection en tant que documents) relève du
  **Code des relations entre le public et l'administration (CRPA), titre Ier**
  (droit d'accès aux documents administratifs — articles L311-1 et suivants —
  *vérifié sur Légifrance le 2026-06-30* quant à la localisation du titre ;
  numéro d'article précis à confirmer en version consolidée selon la date des
  faits).
- **Distinguer deux logiques** à ne jamais confondre :
  - **CRPA** : droit d'accès du public/de l'administré à un document
    administratif détenu par la PM, sous réserve des exceptions (sécurité
    publique, procédure judiciaire en cours, protection des données
    personnelles de tiers) et de l'**occultation** des données personnelles
    avant communication à un tiers ;
  - **RGPD** : droit d'accès de la **personne concernée** à ses **propres**
    données personnelles, exercé directement auprès du responsable de
    traitement (procédure distincte de la saisine CRPA/CADA).
- **CADA** : commission compétente en cas de refus de communication d'un
  document administratif — saisine préalable obligatoire avant tout recours
  contentieux (à vérifier le délai et les modalités exactes).
- **Cas fréquent en PM** : demande d'images de vidéoprotection par un
  administré impliqué dans un événement. Articulation CRPA (accès au document)
  / RGPD (droit d'accès aux données le concernant) / régime spécial CSI de la
  vidéoprotection (délai de conservation, destinataires autorisés) → traiter
  les trois grilles ensemble, ne pas répondre sur un seul fondement → voir
  aussi `videoprotection.md`.

### 4.7 AIPD — analyse d'impact relative à la protection des données

- L'**AIPD** est **obligatoire** lorsque le traitement est susceptible
  d'engendrer un risque élevé pour les droits et libertés des personnes —
  critères et liste de traitements concernés fixés par la CNIL, **à vérifier**
  au cas par cas (la vidéoprotection étendue, la reconnaissance faciale ou
  tout dispositif de captation systématique sont des candidats typiques à
  examiner en priorité).
- Conduite de l'AIPD : description du traitement et de ses finalités,
  évaluation de la nécessité et de la proportionnalité, identification des
  risques pour les personnes concernées, mesures pour traiter ces risques —
  méthodologie CNIL, à mobiliser sans la reconstituer de mémoire.
- **Avant tout déploiement** d'un nouveau dispositif de captation ou de
  traitement de données par le service PM (extension de vidéoprotection,
  nouveau logiciel métier, caméra-piéton, lecture automatisée de plaques
  d'immatriculation) : vérifier si l'AIPD est requise **avant** la mise en
  service, pas après.
- Articulation avec le contrôle de légalité et l'autorisation préfectorale de
  vidéoprotection : l'AIPD ne se substitue pas à l'autorisation CSI, elle s'y
  ajoute → `videoprotection.md`.

### 4.8 Traçabilité des consultations de fichiers

- Tout agent PM habilité à consulter un fichier d'État (TAJ, FOVeS, fichier
  des véhicules volés, SIV, etc., selon les habilitations effectivement
  accordées au service) doit le faire dans le **cadre strict de sa
  finalité légale** et de ses **habilitations personnelles** — pas de
  consultation de confort ou hors cadre de mission.
- **Traçabilité obligatoire** : chaque consultation doit être journalisée
  (identité de l'agent, date, motif, fichier consulté) — exigence
  structurante tant pour le RGPD que pour la déontologie professionnelle. Une
  consultation hors cadre constitue un **manquement déontologique**
  (probité, respect de la loi) **et** une **violation potentielle du RGPD**
  (détournement de finalité), pouvant aussi caractériser une infraction
  pénale (atteinte au secret, détournement de fichier informatique) → cumul
  des trois voies (§4.3).
- **Contrôle interne** (§4.4) : audit régulier des journaux de consultation,
  point de vigilance prioritaire pour le directeur de police municipale.
- **Constat d'une consultation suspecte** : cette branche traite le constat
  (qualification du manquement, déclenchement du contrôle interne, signalement
  RGPD le cas échéant) ; dès que la voie disciplinaire est engagée → bascule
  `drh-fpt` ; dès qu'une voie pénale est caractérisée → `penal-procedure.md`
  et garde-fou APJA (`SKILL.md` §5.2) si les actes à accomplir dépassent les
  pouvoirs APJA.

---

## 5. Procédures et délais

- **Signalement d'un manquement déontologique** : remontée hiérarchique
  immédiate, rapport circonstancié, préservation des éléments de preuve
  (images, journaux de connexion, témoignages) avant toute décision sur la
  suite — annoncer les hypothèses, demander les données manquantes (date,
  agent concerné, nature exacte du fait).
- **Violation de données (incident RGPD)** : obligation de notification à la
  CNIL en cas de violation de données à caractère personnel susceptible
  d'engendrer un risque pour les personnes concernées, dans un **délai
  contraint** (délai exact à vérifier, de l'ordre de 72 heures à compter de la
  prise de connaissance) ; information des personnes concernées si le risque
  est élevé. Le DPO pilote cette procédure.
- **Réponse à une demande CRPA** : délai de réponse de l'administration et
  délai de saisine de la CADA en cas de refus ou de silence — **à vérifier**,
  ne pas donner de délai de mémoire.
- **AIPD** : à conduire **en amont** de la mise en œuvre du traitement, et à
  réviser en cas de changement substantiel du traitement.
- Pour toute échéance, signaler le délai comme **à vérifier** plutôt que de le
  chiffrer de mémoire (matrice §2.2 du `SKILL.md`).

---

## 6. Déclencheurs de vérification

Appliquer le socle-sources (`SKILL.md` §5.3 +
`references/socle-sources-verification.md`) dès que :
- un **numéro d'article précis** du code de déontologie PM est cité en acte
  (rapport de manquement, courrier) ;
- la **qualification pénale** d'un usage de la force ou d'une consultation de
  fichier est en jeu ;
- l'**étendue d'un pouvoir** (usage de la force, accès à un fichier) est
  discutée ;
- un **délai** (notification CNIL, réponse CRPA, saisine CADA, prescription)
  conditionne la réponse ;
- une **réforme récente** (RGPD, directive police-justice, refonte du code de
  déontologie PM) est en cause ;
- une **jurisprudence** (faute personnelle/faute de service, proportionnalité
  de l'usage de la force) est invoquée.

---

## 7. Pièges & confusions fréquentes

1. Confondre **légitime défense** (droit commun) et **usage de la force dans
   le cadre des pouvoirs de police** (régime propre, conditions de nécessité
   et proportionnalité distinctes) — §4.2.
2. Traiter un manquement déontologique et la procédure disciplinaire comme un
   seul et même sujet : cette branche s'arrête au **constat** ; la
   **procédure** est `drh-fpt` (§5.4 du `SKILL.md`).
3. Croire que la voie disciplinaire **exclut** la voie pénale, ou
   inversement : elles sont **cumulables et indépendantes** (§4.3).
4. Confondre **CRPA** (accès d'un tiers à un document) et **droit d'accès
   RGPD** (la personne concernée accède à ses propres données) — §4.6.
5. Appliquer le RGPD « général » sans examiner si le traitement relève en
   réalité du régime spécial **police-justice** — §4.5.
6. Oublier l'**AIPD préalable** avant déploiement d'un nouveau dispositif de
   captation (vidéoprotection étendue, caméra-piéton, LAPI) — §4.7.
7. Ne pas tracer une consultation de fichier, ou la justifier a posteriori
   sans journal contemporain — §4.8.
8. Présumer la **faute personnelle** de l'agent en cas de dommage, sans
   distinguer faute de service / faute personnelle détachable — §4.3.
9. Identifier le **directeur de police municipale** comme responsable de
   traitement RGPD au lieu du **maire** (sauf délégation expresse à vérifier).
10. Dupliquer ici le régime d'armement ou de vidéoprotection au lieu de
    renvoyer vers `armement-equipements.md` / `videoprotection.md`.

---

## 8. Données / références à vérifier

- **Code de déontologie des agents de police municipale** : CSI, partie
  réglementaire, articles **R515-1 et suivants** (*vérifié sur Légifrance le
  2026-06-30* pour la localisation du chapitre ; origine décret n° 2003-735 du
  1er août 2003, depuis codifiée — numéro exact d'article applicable au fait
  examiné et version en vigueur à la date des faits **à confirmer**).
- **Usage de la force / dispersion d'attroupements** : CSI, livre II (ordre et
  sécurité publics), notamment les dispositions relatives aux sommations et à
  l'usage de la force par la force publique (*vérifié sur Légifrance le
  2026-06-30* pour l'existence et la localisation de ce régime) — articulation
  exacte avec le statut de l'agent PM et son armement **à confirmer en version
  consolidée** avant tout acte.
- **Légitime défense** : code pénal, dispositions générales — numéro d'article
  à confirmer en version consolidée.
- **Responsabilité administrative / faute de service** : construction
  essentiellement jurisprudentielle (CE) — toute référence d'arrêt à vérifier
  via `recherche-juridique`, ne jamais citer un numéro de requête de mémoire.
- **Protection fonctionnelle** : régime statutaire (CGFP) — article à
  confirmer en version consolidée, articulation avec `drh-fpt` pour
  l'instruction de la demande.
- **RGPD** : règlement (UE) 2016/679 + loi n° 78-17 du 6 janvier 1978 modifiée
  (« Informatique et Libertés ») — articles précis et régime police-justice à
  vérifier sur Légifrance/CNIL avant toute citation en acte.
- **CRPA, droit d'accès aux documents administratifs** : titre Ier, articles
  **L311-1 et suivants** (*vérifié sur Légifrance le 2026-06-30* pour la
  localisation du titre ; numéro précis selon le point traité **à confirmer en
  version consolidée**). Ne pas confondre avec le chapitre diffusion
  (articles L312-1 et s., open data), distinct du droit d'accès.
- **AIPD** : méthodologie et liste des traitements concernés — référentiels
  CNIL, à consulter à jour, jamais reconstitués de mémoire.
- **Notification de violation de données** : délai réglementaire (RGPD) — à
  vérifier, ne pas chiffrer de mémoire.

---

## 9. Écrits & livrables

1. **Constat** — rapport de manquement déontologique (description factuelle
   des faits, articles du code de déontologie potentiellement concernés sous
   réserve de vérification, transmission à la hiérarchie). Ne pas anticiper la
   qualification disciplinaire finale, qui appartient à `drh-fpt`.
2. **Signalement RGPD** — fiche d'incident à destination du DPO (nature de la
   violation, données concernées, mesures immédiates, proposition de
   notification CNIL).
3. **Registre / fiche AIPD** — document préalable au déploiement d'un
   traitement à risque, à associer au registre des traitements.
4. **Réponse CRPA** — courrier de communication ou de refus motivé d'un
   document administratif (occultation des données personnelles de tiers le
   cas échéant, mention des voies de recours CADA).
5. **Note au maire/DGS** — sur une situation de contrôle interne, un incident
   de données, ou un usage de la force contesté, en vue d'arbitrage ou de
   saisine d'instances externes.

Acte faisant grief éventuel (ex. refus de communication CRPA) : motivation +
voies et délais de recours + vérifier la transmission au contrôle de légalité
le cas échéant → `controle-legalite.md` avant production.

---

## 10. Double échelle [risque / confiance]

- **Manquement déontologique léger, sans incidence sur un tiers** :
  [risque faible / confiance stable] — réponse directe sur le principe,
  rapport de constat sans citation d'article précis si non nécessaire.
- **Usage de la force contesté, dommage corporel ou matériel** :
  [risque élevé / confiance à vérifier] — citation de source obligatoire,
  réserve « à confirmer », orientation vers `recherche-juridique` pour la
  jurisprudence de proportionnalité.
- **Violation de données à caractère personnel (consultation hors cadre,
  fuite, incident technique)** : [risque élevé à critique / confiance à
  vérifier] — citation obligatoire, vérification du délai de notification
  CNIL, abstention sur le chiffrage du délai si non vérifié en session.
- **Refus de communication CRPA contesté** : [risque moyen / confiance à
  vérifier] — vérification ponctuelle obligatoire avant réponse motivée.
- **AIPD préalable à un nouveau dispositif** : [risque moyen à élevé selon le
  dispositif / confiance à vérifier] — ne jamais affirmer qu'une AIPD n'est
  pas requise sans vérification du référentiel CNIL à jour.

---

## 11. Checklist de branche

1. Distinction posée entre **constat** (cette branche) et **procédure**
   disciplinaire (`drh-fpt`) ?
2. Cumul **pénal / administratif / disciplinaire** signalé comme
   indépendant et cumulable, pas exclusif ?
3. Usage de la force qualifié sous le bon fondement (**légitime défense** vs
   **pouvoir de police**), proportionnalité examinée ?
4. Faute **personnelle détachable** vs faute **de service** distinguée avant
   toute conclusion sur la responsabilité ?
5. **Responsable de traitement** RGPD correctement identifié (maire / DPO),
   pas le directeur PM par défaut ?
6. Régime **police-justice** envisagé avant application mécanique du RGPD
   général ?
7. **CRPA** (accès document) et **droit d'accès RGPD** (données personnelles)
   non confondus dans la réponse ?
8. **AIPD** envisagée avant tout déploiement de nouveau dispositif de
   captation/traitement ?
9. **Traçabilité des consultations de fichiers** rappelée comme exigence
   transverse (déontologie + RGPD + pénal potentiel) ?
10. Toute référence d'article portée par la réserve « à confirmer en version
    consolidée », sauf mention « vérifié sur Légifrance le 2026-06-30 » ?
11. Renvois faits vers `armement-equipements.md`, `videoprotection.md`,
    `controle-legalite.md`, `penal-procedure.md` et `drh-fpt` plutôt que
    duplication de leur contenu ?
12. Garde-fou APJA testé si la consultation/le fait dérive vers un acte
    réservé à l'OPJ (`SKILL.md` §5.2) ?

**[risque variable selon sous-domaine / confiance à vérifier]** — voir §10
pour le détail par type de situation. Branche à forte sensibilité
contentieuse (libertés publiques, données personnelles) : ne jamais conclure
sur un numéro d'article sans vérification quand l'acte en dépend.
