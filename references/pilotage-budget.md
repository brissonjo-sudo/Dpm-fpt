# Branche — Pilotage & budget (v0.1.0)

> Structure conforme à `_gabarit-branche.md`. Les valeurs datées (seuils,
> montants, taux) ne sont jamais données de mémoire : seules les **règles**
> figurent ici, avec la consigne de vérifier la valeur en vigueur.

## 1. Périmètre / Exclusions

**Périmètre** : projet de service de police municipale ; construction et
exécution du budget du service ; marchés publics du service (équipements,
véhicules, armement) ; indicateurs d'activité et reporting au maire.

**Exclusions** :
- **Masse salariale** (traitement, régime indemnitaire, effectifs au sens RH,
  GVT) → `drh-fpt` (carrière-paie). La présente branche traite la masse
  salariale **uniquement comme une ligne du budget global du service**, sans
  jamais en détailler le calcul (renvoi systématique).
- **Armement et équipements** : le **choix doctrinal et l'autorisation
  préfectorale** relèvent de `references/armement-equipements.md` ; cette
  branche traite l'**achat** (procédure de marché) une fois la doctrine fixée.
- **Vidéoprotection** : l'**autorisation préfectorale et le régime CNIL**
  relèvent de `references/videoprotection.md` ; cette branche traite
  l'**achat et le financement** de l'équipement.
- **Légalité de l'acte** (délibération, marché) avant signature →
  `references/controle-legalite.md`.

## 2. Questions couvertes

Élaboration d'un projet de service pluriannuel ; construction budgétaire
(BP, DM, CA) ; débat d'orientation budgétaire ; choix de la procédure de
marché public selon le montant ; computation des seuils (achat de
véhicules, gilets pare-balles, armement, uniformes, radio, vidéoprotection,
logiciels métier) ; allotissement ; subventions et cofinancements (FIPD,
dotations) ; tableau de bord d'activité (PV, interventions, taux
d'élucidation locale) ; reporting au maire et au conseil municipal.

## 3. Arbre de traitement

`question → variables à lever (§4) → décision → vérification (§7) → écrit/livrable (§10)`

Ne pas chiffrer ni qualifier une procédure de marché tant que le **montant
estimé du besoin** et la **nature de l'achat** (fournitures/services vs
travaux) ne sont pas connus.

## 4. Variables à lever

- **Taille de la commune / EPCI** (seuils CGCT déclenchant des obligations :
  rapport d'orientation budgétaire, débat, présentation des effectifs —
  à vérifier selon strate démographique).
- **Montant estimé du besoin HT**, sur la durée totale envisagée du contrat
  (et non le seul exercice annuel) — détermine le régime de publicité et de
  mise en concurrence.
- **Nature de l'achat** : fournitures/services ou travaux (seuils distincts).
- **Allotissement envisagé** : lot par lot ou marché global (computation du
  seuil par lot vs valeur totale estimée du besoin).
- **Source de financement** : budget propre, subvention fléchée (FIPD,
  dotation armement, fonds européens), cofinancement EPCI.
- **Régime budgétaire de la collectivité** : nomenclature comptable
  applicable (M57 généralisée ou autre selon strate — à vérifier),
  autorisations de programme / crédits de paiement si pluriannuel.
- **Existence d'un projet de service formalisé** (référentiel
  stratégique préalable) conditionnant la cohérence des achats et des
  indicateurs avec les priorités affichées au maire.

## 5. Règles métier

### 5.1 Projet de service de police municipale

- Document de **pilotage stratégique**, non un acte juridique formel : pas de
  base légale imposant son contenu en tant que tel pour la PM (à la différence
  d'autres administrations). Sa **légitimité** vient de sa validation par le
  maire (autorité hiérarchique du service) et, le cas échéant, de sa
  présentation au conseil municipal.
- Structure recommandée : diagnostic de sécurité locale, priorités
  opérationnelles, organisation cible (effectifs, équipements, doctrine —
  renvoi `doctrine-operationnelle.md`), trajectoire budgétaire pluriannuelle,
  indicateurs de suivi (§5.4).
- Le projet de service **n'emporte pas par lui-même** d'engagement budgétaire :
  il oriente le **vote annuel du budget** par le conseil municipal, seul acte
  juridiquement engageant.
- Cohérence à vérifier avec la **convention de coordination** (renvoi
  `continuum-partenariats.md`) et les éventuelles **LDG RH** du volet
  recrutement (renvoi `drh-fpt`).

### 5.2 Construction et exécution budgétaire

- **Cadre général** : budget communal régi par le CGCT (Livre III, finances
  communales). Principes budgétaires (annualité, universalité, unité,
  équilibre réel, spécialité) — règles stables dans leur architecture,
  modalités d'application à vérifier au cas par cas.
- **Rapport et débat d'orientation budgétaire (DOB)** : dans les communes
  dont la population atteint le seuil fixé par la loi, le maire présente au
  conseil municipal, dans le délai précédant l'examen du budget, un rapport
  sur les orientations budgétaires, les engagements pluriannuels envisagés
  et la structure/gestion de la dette ; ce rapport donne lieu à un **débat**,
  dont **acte est pris par une délibération spécifique**
  (Art. L. 2312-1 CGCT — *vérifié sur Légifrance le 2026-06-30*,
  identifiant `LEGIARTI000051731867`). Dans les communes dépassant un second
  seuil démographique, le rapport intègre en outre une présentation de la
  structure des effectifs et de l'évolution des dépenses de personnel — point
  de **jonction obligatoire avec `drh-fpt`** pour le chiffrage RH, le DPM ne
  fournissant que les éléments de doctrine et d'organisation du service.
  > **Point de vigilance daté** : une réforme de la nomenclature budgétaire
  et comptable locale (ordonnance n° 2025-526 du 12 juin 2025) modifie ce
  cadre **à compter de l'exercice 2026** — vérifier la version consolidée
  applicable à l'exercice budgétaire concerné avant toute présentation au
  conseil municipal.
- **Cycle budgétaire annuel** : DOB (si seuil atteint) → vote du budget
  primitif (BP) → décisions modificatives (DM) en cours d'exercice → compte
  administratif (CA) en clôture. Le budget du service PM (fonctionnement et
  investissement) s'inscrit dans le budget général de la commune ; il n'a pas
  d'autonomie juridique propre (sauf régie ou budget annexe, cas rare pour la
  PM).
- **Pluriannualité** : pour les investissements lourds (flotte de véhicules,
  centre de supervision urbain, armement), recourir aux **autorisations de
  programme / crédits de paiement (AP/CP)** si la nomenclature applicable le
  permet — vérifier l'éligibilité selon la strate et le référentiel comptable
  en vigueur.
- **Exécution** : engagement → liquidation → ordonnancement → paiement
  (séparation ordonnateur/comptable). Le DPM, en tant que service prescripteur,
  engage la dépense dans la limite des crédits votés et de sa délégation de
  signature (vérifier l'arrêté de délégation du maire).

### 5.3 Marchés publics (équipements, véhicules, armement)

- **Code de la commande publique (CCP)** : texte de référence. Distinguer
  toujours le **seuil de dispense de procédure** (marché passé sans
  publicité ni mise en concurrence préalables) du **seuil de procédure
  adaptée (MAPA)** et du **seuil de procédure formalisée** (appel d'offres) —
  ces trois seuils sont **périodiquement révisés** (révision biennale liée
  aux seuils européens) : ne jamais les citer de mémoire, vérifier la valeur
  en vigueur à la date de lancement de la consultation.
  - **Gré à gré sans publicité ni mise en concurrence** : possible pour un
    besoin dont la valeur estimée est inférieure à un seuil fixé par voie
    réglementaire, ou dans les cas limitativement énumérés (urgence,
    infructuosité, exclusivité — liste fermée) (Art. L. 2122-1 CCP —
    *vérifié sur Légifrance le 2026-06-30*, identifiant
    `LEGIARTI000042657232` ; cas détaillés aux art. R. 2122-1 et s. CCP, à
    confirmer en version consolidée pour le seuil chiffré).
  - **Procédure adaptée (MAPA)** : entre le seuil de dispense et le seuil de
    procédure formalisée ; librement organisée par l'acheteur dans le respect
    des principes de la commande publique (Art. L. 2123-1 et R. 2123-1 CCP —
    *vérifié sur Légifrance le 2026-06-30*, identifiant `LEGIARTI000043316424`
    pour R. 2123-1).
  - **Procédure formalisée** (appel d'offres ouvert/restreint) : au-delà du
    seuil européen applicable à la catégorie d'acheteur et d'achat —
    **toujours vérifier le seuil en vigueur**, distinct pour fournitures/
    services et pour travaux.
- **Computation du besoin** : la valeur s'apprécie sur la **totalité du
  besoin**, pas marché par marché ni année par année (interdiction du
  saucissonnage). Pour un allotissement, vérifier la règle de computation
  par lot (seuil dérogatoire possible pour certains lots sous conditions
  cumulatives — montant du lot et part du lot dans le total — à confirmer en
  version consolidée).
- **Spécificités armement et équipements de protection** : achat soumis au
  droit commun de la commande publique ; la **doctrine d'équipement**
  (type d'arme, calibre, dotation) relève de `armement-equipements.md` et de
  l'autorisation préfectorale **préalable** à tout engagement d'achat
  significatif — vérifier l'articulation calendaire (autorisation avant
  commande, ou clause suspensive).
- **Véhicules** : marché de fournitures (achat) ou parfois marché global
  incluant équipement/sérigraphie ; vérifier si un accord-cadre mutualisé
  (centrale d'achat, UGAP ou groupement de commandes avec l'EPCI) est
  mobilisable — dispense alors de remise en concurrence par la commune sous
  conditions à vérifier.
- **Mise en concurrence et transparence** : obligations de publicité (BOAMP,
  JOUE selon seuil), critères de sélection et d'attribution objectifs, et
  **traçabilité** des échanges avec les candidats — point de vigilance
  contentieuse (référé précontractuel, voir `contentieux.md`).

### 5.4 Indicateurs d'activité et reporting au maire

- **Finalité** : objectiver l'activité du service pour éclairer la décision
  du maire (autorité hiérarchique) et nourrir le DOB / le projet de service ;
  ce n'est pas une obligation légale formalisée pour la PM en tant que telle
  (à la différence, par exemple, des polices nationale/gendarmerie) — c'est un
  **outil de pilotage**, sa fréquence et son contenu relèvent de
  l'organisation interne du service et des attentes du maire.
- **Indicateurs typiques** : volume et nature des interventions, PV dressés
  par catégorie d'infraction, rapports transmis à l'OPJ/au procureur, activité
  de verbalisation (stationnement, circulation), fourrières, mains courantes,
  délais de réponse, taux de disponibilité de la flotte et des équipements,
  incidents avec usage de la force ou de l'armement (renvoi
  `armement-equipements.md` pour le régime de compte rendu obligatoire),
  sollicitations de la vidéoprotection (renvoi `videoprotection.md`).
- **Prudence méthodologique** : ne jamais présenter un indicateur d'activité
  comme une mesure de **délinquance constatée** (statistique relevant de
  l'État, SSMSI) ni comme un indicateur de **performance individuelle** d'un
  agent sans cadre RH validé (renvoi `drh-fpt` pour tout lien avec
  l'évaluation professionnelle) — distinguer pilotage de service et
  évaluation d'agent.
- **Protection des données** : les indicateurs nominatifs ou ré-identifiants
  (zones à faible effectif, données issues de la vidéoprotection) suivent le
  régime RGPD/CNIL → `conformite-deontologie-donnees.md`.

## 6. Procédures et délais

- **DOB** : délai de présentation du rapport avant l'examen du budget fixé
  par le CGCT — **à vérifier** selon la version consolidée et la strate de
  population (§5.2).
- **Vote du budget primitif** : délai légal annuel de vote — à vérifier
  (CGCT, disposition générale sur l'adoption du budget).
- **Computation et choix de procédure de marché** : vérifier le seuil
  applicable **à la date de lancement** de la consultation (les seuils
  évoluent par paliers réglementaires périodiques) avant tout engagement.
- **Délais de recours contentieux** sur un marché (référé précontractuel,
  référé contractuel, recours Tarn-et-Garonne) : à vérifier au cas par cas →
  `contentieux.md`.
- **Demandes de subvention** (FIPD, dotations équipement) : calendrier annuel
  fixé par l'autorité gestionnaire (préfecture/État) — à vérifier auprès de
  la source officielle de l'appel à projets, jamais de mémoire.

## 7. Déclencheurs de vérification

Appliquer le socle-sources (matrice §2.2 du `SKILL.md`) dès que :
- un **seuil de marché public** (dispense, MAPA, procédure formalisée) est
  cité pour qualifier une procédure ;
- un **délai ou un seuil démographique CGCT** (DOB, présentation des
  effectifs) conditionne une obligation de la commune ;
- une **référence d'article ou de décret** est utilisée pour fonder une
  délibération ou un marché ;
- une **réforme récente** de la nomenclature budgétaire ou des seuils de la
  commande publique est susceptible de s'appliquer à l'exercice concerné.

## 8. Pièges & confusions fréquentes

1. Confondre le **budget du service** (ligne de fonctionnement/investissement
   intégrée au budget communal) avec un **budget autonome** — la PM n'a, en
   règle générale, pas de personnalité budgétaire propre.
2. **Saucissonner** un achat (fractionnement artificiel) pour rester sous un
   seuil de dispense ou de MAPA — irrégularité sanctionnée.
3. Traiter la **masse salariale** comme une donnée à chiffrer dans cette
   branche : toujours renvoyer le calcul à `drh-fpt`, ne garder ici que la
   ligne budgétaire globale.
4. Engager une **commande d'armement** avant l'**autorisation préfectorale**
   requise (renvoi `armement-equipements.md`) — vérifier l'articulation
   calendaire avant tout bon de commande.
5. Présenter des **indicateurs d'activité PM** comme une statistique
   officielle de délinquance (confusion avec les données SSMSI/État).
6. Oublier le **débat** (et la délibération actant le débat) du DOB en se
   contentant de la présentation du rapport.
7. Citer un **seuil de commande publique** sans en vérifier la date de
   révision en vigueur — ces seuils ne sont **pas figés**.

## 9. Données / références à vérifier

- **Jamais de mémoire** : montants exacts des seuils de dispense de
  procédure, de MAPA et de procédure formalisée (CCP) ; seuils démographiques
  CGCT déclarant les obligations de DOB et de présentation des effectifs ;
  délais légaux de vote du budget ; taux et plafonds de subventions
  (FIPD, dotations armement).
- **Vérifiées sur Légifrance le 2026-06-30** (structure stable, citables sous
  réserve de la version consolidée à la date d'usage) :
  - Art. L. 2312-1 CGCT (rapport et débat d'orientation budgétaire),
    identifiant `LEGIARTI000051731867` — **point de vigilance** : régime
    modifié par l'ordonnance n° 2025-526 du 12 juin 2025, applicable à
    compter de l'exercice budgétaire 2026 ; revérifier la version en vigueur
    à la date du DOB concerné.
  - Art. L. 2122-1 CCP (conditions du marché sans publicité ni mise en
    concurrence préalables), identifiant `LEGIARTI000042657232`.
  - Art. L. 2123-1 et R. 2123-1 CCP (conditions de recours à la procédure
    adaptée), identifiant `LEGIARTI000043316424` pour R. 2123-1.
  - Ces identifiants sont vérifiés **dans leur existence et leur objet** ; les
    **seuils chiffrés** qu'ils renvoient à des textes réglementaires distincts
    (avis de seuils périodiquement publiés) restent **à confirmer en version
    consolidée** à la date d'usage — ne jamais les reporter de mémoire dans un
    acte.
- **Architecture stable mais détail à confirmer** : nomenclature comptable
  M57 (généralisation et modalités selon strate — à vérifier), principes
  budgétaires (CGCT, Livre III finances communales).

## 10. Écrits & livrables

1. **Pilotage stratégique** — projet de service pluriannuel (note de
   doctrine + trajectoire budgétaire) ; rapport d'orientation budgétaire
   (volet PM) pour alimenter le DOB du maire.
2. **Acte budgétaire** — le DPM **n'élabore pas seul** l'acte (délibération
   de budget), il fournit les éléments du service ; vérifier la procédure de
   consolidation avec les finances de la collectivité.
3. **Marché public** — pièces de la consultation (CCTP technique relevant du
   DPM, RC et CCAP relevant souvent du service achats/finances) ; **acte
   d'engagement et choix de procédure** : motivation du choix de procédure
   selon le seuil retenu, à documenter pour traçabilité contentieuse (renvoi
   `contentieux.md`).
4. **Reporting** — tableau de bord d'indicateurs d'activité (périodicité à
   définir avec le maire) ; note de synthèse annuelle au maire et, si
   présentée, au conseil municipal.

Gabarits → `assets/` (note au maire : `assets/note-maire-modele.md`).

## 11. Double échelle [risque / confiance]

- **Stable** : architecture du cycle budgétaire (DOB → BP → DM → CA),
  distinction des trois régimes de procédure de marché (dispense / adaptée /
  formalisée), principe d'interdiction du saucissonnage.
- **À vérifier (risque moyen à élevé selon enjeu)** : tout seuil chiffré
  (commande publique, démographique CGCT), tout délai légal, la nomenclature
  comptable applicable à la strate, le calendrier d'une réforme en cours
  (ordonnance 2025-526).
- **Risque élevé** : choix de procédure de marché sur achat sensible
  (armement) sans articulation vérifiée avec l'autorisation préfectorale —
  citation de source obligatoire avant engagement (§5.1 du `SKILL.md`).

## 12. Checklist de branche

1. Masse salariale exclue du chiffrage détaillé et renvoyée à `drh-fpt` ?
2. Montant estimé du besoin (HT, sur la durée totale) et nature de l'achat
   (fournitures/services vs travaux) levés avant de qualifier la procédure ?
3. Seuil de procédure (dispense / MAPA / formalisée) vérifié en version
   consolidée à la date de lancement, pas cité de mémoire ?
4. Absence de saucissonnage du besoin vérifiée ?
5. Pour un achat d'armement : articulation avec l'autorisation préfectorale
   (`armement-equipements.md`) vérifiée avant engagement ?
6. DOB : seuil démographique, délai et contenu (effectifs si seuil atteint)
   vérifiés, jonction `drh-fpt` faite pour le volet RH ?
7. Indicateurs distingués d'une statistique officielle de délinquance et
   d'une évaluation individuelle d'agent ?
8. Si acte faisant grief ou marché contesté : renvoi `controle-legalite.md` /
   `contentieux.md` effectué ?
