# Branche — Doctrine opérationnelle

> Structure conforme à `_gabarit-branche.md`. Branche **organisationnelle** :
> elle traite le **comment commander, organiser et déployer le service**, pas
> le contenu réglementaire de fond ni les partenariats institutionnels.

## 1. Périmètre / Exclusions

**Périmètre** : organisation du service (cycles, effectifs, doctrine
d'emploi), patrouilles (modes d'action, secteurs), dispositifs événementiels
(sécurisation de manifestations, gabarits de dispositif), gestion de crise
(alerte, plan communal de sauvegarde, maincourante de crise, retour à la
normale), articulation avec les zones de sécurité prioritaires (ZSP) et
dispositifs territoriaux analogues.

**Exclusions** :
- **Contenu réglementaire de fond** (pouvoirs de police mobilisés, régime
  juridique d'un attroupement, d'un débit de boissons temporaire, du
  stationnement lors d'un événement) → `reglementation-appliquee.md` et
  `pouvoirs-police.md`.
- **Partenariats institutionnels** (convention de coordination, CLSPD/CISPD,
  coopération avec les forces de l'État) → `continuum-partenariats.md`.
- **Procédure pénale** (constatation d'infraction pendant un dispositif,
  relations OPJ) → `penal-procedure.md`.
- **RH statutaire** des agents (cycles de travail en tant que régime
  statutaire, heures supplémentaires, astreintes en tant que droits) →
  `drh-fpt` (§5.4 `SKILL.md`) ; ce qui reste ici, c'est l'**organisation
  opérationnelle** du cycle, pas son régime indemnitaire ou statutaire.
- **Armement et équipements** (dotation, FIA) → `armement-equipements.md`.
- **Vidéoprotection / CSU** en tant qu'outil de surveillance fixe →
  `videoprotection.md` ; reste ici son **articulation avec le dispositif de
  patrouille ou d'événement** (renvoi, pas de doctrine vidéo).
- **Budget et marchés** liés aux dispositifs (location de matériel,
  prestataires) → `pilotage-budget.md`.

---

## 2. Questions couvertes

- Construction d'un cycle de travail opérationnel (horaires, effectifs,
  présence terrain vs astreinte fonctionnelle).
- Doctrine de patrouille (pédestre, VTT, véhiculée, mixte ; secteurs ;
  binômes vs solo).
- Conception d'un dispositif événementiel (manifestation sportive, culturelle,
  marché, brocante, feu d'artifice, fan-zone).
- Gestion de crise communale (intempérie, accident majeur, attentat, événement
  d'ordre public) : déclenchement, commandement, articulation avec le préfet.
- Plan communal de sauvegarde (PCS) : rôle de la PM dans son activation.
- Zones de sécurité prioritaires (ZSP) et dispositifs territoriaux analogues :
  articulation du service PM avec un classement ZSP existant.
- Continuité de service (jours fériés, période estivale, pics
  saisonniers).

---

## 3. Arbre de traitement

`question → variables à lever (§4) → décision → vérification (§7) → écrit/livrable (§10)`

Ne jamais figer un dispositif (cycle, patrouille, événement, crise) sans avoir
levé les variables de risque, d'effectif et de compétence engagée.

---

## 4. Variables à lever

- **Nature du service** : effectifs disponibles, amplitude horaire actuelle,
  existence d'une convention de coordination (conditionne les plages
  horaires d'intervention de la PM hors convention — voir
  `continuum-partenariats.md`).
- **Qualification de l'événement** : manifestation revendicative (régime
  déclaratif/préfectoral spécifique) vs événement organisé par la commune
  (kermesse, marché) vs événement privé sur domaine public (autorisation
  d'occupation).
- **Niveau de risque de l'événement** : affluence attendue, configuration des
  lieux, antécédents, contexte de menace (plan Vigipirate ou équivalent en
  vigueur — à vérifier).
- **Autorité organisatrice et autorité de police** : qui organise (mairie,
  association, privé) n'est pas toujours qui exerce la police (maire, et le
  cas échéant préfet pour une police spéciale ou un classement particulier).
- **Classement ZSP ou dispositif territorial équivalent** : existe-t-il sur le
  ressort de la commune ? Quelle gouvernance (état-major de sécurité,
  copilotage préfet/procureur/maire) ?
- **Niveau de crise** : événement courant (gérable par le service seul) vs
  crise nécessitant l'activation du PCS et/ou la montée en commandement du
  maire vs crise dépassant la compétence communale (bascule préfectorale,
  ORSEC).
- **Disponibilité d'un PCS** : existant, à jour, testé ou non (l'existence et
  l'actualisation du PCS sont elles-mêmes des obligations à vérifier selon le
  classement de risque de la commune — art. L. 731-3 CSI, vérifié sur
  Légifrance le 2026-06-30).

---

## 5. Règles métier

### 5.1 Doctrine d'emploi et organisation du service

- L'organisation du service relève du pouvoir d'organisation du maire
  (autorité territoriale) et du directeur de police municipale par
  délégation/subdélégation. Le **cycle de travail** est d'abord un acte
  d'organisation du service ; sa **conformité statutaire** (durée annuelle de
  référence, régimes dérogatoires, cycles atypiques propres à la PM) relève
  du volet RH → voir `rh-specificites-pm.md` (cycles atypiques) et `drh-fpt`
  pour le régime général du temps de travail.
- Principe à retenir : **dimensionner le service sur la doctrine d'emploi
  avant le cycle**, pas l'inverse. Une doctrine d'emploi formalise : les
  missions prioritaires du service (proximité, tranquillité publique,
  circulation, événementiel), les plages de présence terrain attendues, le
  niveau d'engagement en flagrance, et l'articulation avec les forces de
  l'État (renvoi `continuum-partenariats.md`).
- **Continuité de service** : le maire est responsable de l'ordre public en
  continu sur sa commune (police générale, art. L. 2212-2 CGCT, vérifié sur
  Légifrance le 2026-06-30) ; le dimensionnement du service PM est un choix
  d'organisation locale, pas une obligation de couverture 24h/24 — distinguer
  l'**obligation de résultat sur l'ordre public** (qui peut être assurée par
  d'autres moyens : forces de l'État, astreinte, escalade) de l'**obligation
  de moyens du service PM**, qui n'existe pas en tant que telle.

### 5.2 Patrouilles

- Le mode de patrouille (pédestre, VTT, véhiculée, mixte) est un choix
  opérationnel, à motiver par : la doctrine de proximité retenue, la
  configuration urbaine, le niveau de risque du secteur, et la sécurité des
  agents (doctrine de binôme à privilégier en zone à risque ou de nuit —
  point d'organisation interne, pas une obligation légale générale ; vérifier
  toute consigne locale ou instruction propre avant de la présenter comme une
  règle).
- Le **sectorisé** est un outil de doctrine (zones de patrouille dédiées) à
  distinguer du **classement ZSP** (§5.4), qui est un dispositif piloté par
  l'État, pas un découpage interne du service PM.
- Patrouille et **constatation d'infraction** : les pouvoirs exercés en
  patrouille restent ceux de l'APJA (art. 21 et 21-2 CPP — à confirmer en
  version consolidée). Toute situation dépassant ce cadre déclenche le
  garde-fou APJA → `penal-procedure.md`.

### 5.3 Dispositifs événementiels

- **Première question à trancher** : qui organise, qui autorise, qui exerce
  la police. Un événement communal (kermesse, marché) relève en principe de
  la police générale du maire (art. L. 2212-2 CGCT) ; un rassemblement
  revendicatif relève d'un régime spécifique de déclaration/encadrement
  préfectoral distinct → qualification à vérifier dans `pouvoirs-police.md`
  avant tout dispositif.
- Construction du dispositif (méthode, pas règle juridique) :
  1. qualifier l'événement (nature, organisateur, affluence) ;
  2. identifier l'autorité de police compétente et les autorisations
     préalables requises (occupation du domaine public, débit de boissons
     temporaire — renvoi `reglementation-appliquee.md`) ;
  3. évaluer le risque (affluence, configuration des lieux, antécédents,
     niveau de menace) ;
  4. dimensionner les effectifs et les missions (filtrage, régulation
     circulation, présence dissuasive, point de regroupement) ;
  5. prévoir l'articulation avec les forces de l'État et les services de
     secours (SDIS, SAMU) si le format l'exige → `continuum-partenariats.md` ;
  6. prévoir une procédure dégradée (évacuation, alerte, repli) proportionnée
     au risque identifié à l'étape 3.
- Un dispositif événementiel n'emporte **aucune extension** des pouvoirs APJA
  des agents présents : présence renforcée ne signifie pas pouvoir
  d'investigation renforcé.

### 5.4 Gestion de crise

- **Distinguer trois niveaux** :
  1. **Incident courant** géré par le service seul (moyens normaux, pas
     d'activation de plan).
  2. **Crise communale** nécessitant la mobilisation du maire en tant
     qu'autorité de police générale et, le cas échéant, l'activation du
     **plan communal de sauvegarde (PCS)** lorsque la commune y est tenue ou
     en dispose (art. L. 731-3 CSI, vérifié sur Légifrance le 2026-06-30 —
     le PCS prépare la réponse aux situations de crise, organise l'alerte et
     l'information préventive, et recense les moyens disponibles ; son
     caractère obligatoire dépend du classement de la commune au regard des
     risques recensés, à vérifier au cas par cas).
  3. **Crise dépassant la compétence communale**, appelant la bascule vers le
     dispositif **ORSEC** sous l'autorité du préfet — la PM reste alors un
     **moyen mis à disposition**, pas un pilote du dispositif.
- **Rôle de la PM en gestion de crise** : exécution des missions de sécurité
  et de protection de la population fixées par le maire (ou, en phase
  ORSEC, par le COS/préfet via le dispositif), remontée d'information
  continue, tenue d'une maincourante de crise. La PM **n'élabore pas** seule
  le PCS (document de la commune, porté par les services concernés sous
  l'autorité du maire) mais y contribue pour le volet sécurité.
- **Police générale vs préfectorale en crise** : tant que la crise reste
  communale, le maire conserve la direction des opérations de secours
  (sous réserve du rôle du DOS au sens du droit de la sécurité civile, à
  vérifier) ; au-delà, le préfet devient directeur des opérations de
  secours. Ne jamais présenter la PM comme autorité de commandement de la
  crise : elle est un service exécutant sous l'autorité du maire ou, en
  phase préfectorale, intégrée au dispositif.
- **Retour à la normale** : prévoir la phase de désengagement progressif et
  le retour d'expérience → `retex.md`.

### 5.5 Zones de sécurité prioritaires (ZSP) et dispositifs territoriaux analogues

- Les **ZSP** sont un dispositif **non codifié**, créé par voie de
  circulaire ministérielle (instruction du ministère de l'Intérieur de
  2012, à confirmer en version consolidée — il ne s'agit pas d'un texte de
  loi ou de décret, mais d'un acte de pilotage administratif). Ne jamais
  présenter une ZSP comme fondée sur un article de code : son fondement est
  une **politique publique pilotée par l'État** (préfet/procureur),
  matérialisée par une gouvernance locale (état-major de sécurité).
- **Conséquence pour la doctrine PM** : un classement ZSP **ne modifie pas**
  les pouvoirs de police du maire ni les pouvoirs APJA des agents PM. Il crée
  une **priorité d'action territoriale concertée** : la PM y participe
  comme partenaire, dans le cadre de sa convention de coordination
  → `continuum-partenariats.md`, pas comme autorité pilote.
- D'autres dispositifs territoriaux ont pu succéder ou coexister avec les ZSP
  selon les politiques publiques en vigueur (ex. dispositifs de police de
  sécurité du quotidien, quartiers de reconquête républicaine). **Vérifier
  le dispositif en vigueur localement** avant toute doctrine : ces
  qualifications évoluent au gré des circulaires et ne sont pas stabilisées
  dans un texte de niveau législatif.
- Pour la commune, l'enjeu opérationnel est l'**articulation du cycle de
  patrouille et des dispositifs événementiels avec les priorités définies par
  l'état-major de sécurité local**, sans confusion de compétence.

---

## 6. Procédures et délais

Cette branche est principalement organisationnelle ; peu de délais
légaux stricts lui sont propres. Points de procédure à retenir :

- **Activation du PCS** : déclenchée par le maire (ou son représentant) dès
  qu'un événement répond aux critères du plan ; pas de délai légal de
  déclenchement, mais l'**absence de plan à jour ou non exercé** sur une
  commune qui y est tenue est un point de vigilance contentieuse en cas de
  carence avérée (exercice périodique requis — périodicité à vérifier en
  version consolidée).
- **Dispositif événementiel à enjeu** : prévoir les délais d'instruction des
  autorisations administratives sous-jacentes (occupation du domaine
  public, débit de boissons temporaire) en amont du dispositif sécurité →
  délais propres à `reglementation-appliquee.md`, à anticiper dans le
  rétroplanning du dispositif.
- **Conventions et concertations ZSP/territoriales** : pas de délai propre à
  la doctrine ; le rythme est fixé par la gouvernance locale (état-major de
  sécurité), à documenter au cas par cas.

---

## 7. Déclencheurs de vérification

Appliquer le socle-sources (matrice §2.2 `SKILL.md`) dès que :
- la **compétence à activer un PCS ou un dispositif ORSEC** est en jeu
  (répartition maire/préfet) ;
- le **caractère obligatoire du PCS** pour la commune concernée est invoqué
  (classement de risque à vérifier au cas par cas) ;
- une **doctrine d'emploi ou un cycle** est présenté comme imposé par un
  texte précis (vérifier s'il s'agit d'une règle statutaire réelle ou d'un
  choix d'organisation locale) ;
- le **fondement d'un dispositif événementiel** (police générale vs régime
  spécifique de rassemblement) conditionne le périmètre d'action de la PM ;
- une référence à un **dispositif territorial type ZSP** est utilisée pour
  justifier une priorité d'action : vérifier le dispositif réellement en
  vigueur localement (les circulaires se succèdent, le nom et le cadre
  évoluent).

---

## 8. Pièges & confusions fréquentes

1. Présenter la **ZSP** comme un texte de loi ou de décret : c'est un
   dispositif de circulaire, piloté par l'État, sans effet sur les pouvoirs
   de police municipale.
2. Confondre **sectorisation interne** de patrouille (outil de doctrine du
   service) et **classement ZSP** (dispositif piloté par l'État).
3. Croire qu'un **dispositif événementiel renforcé** étend les pouvoirs
   APJA des agents présents — faux, le cadre légal reste identique.
4. Présenter la PM comme **autorité de commandement** d'une gestion de crise
   communale : elle est un service exécutant sous l'autorité du maire (ou,
   en phase ORSEC, intégrée au dispositif préfectoral).
5. Oublier de distinguer **crise communale** (maire) et **crise dépassant la
   compétence communale** (bascule préfectorale, ORSEC) — risque de
   présenter une intervention de la PM hors de son niveau de compétence.
6. Traiter le **cycle de travail** comme une question purement
   organisationnelle sans vérifier sa conformité statutaire (renvoi
   `rh-specificites-pm.md` / `drh-fpt`) — ou inversement, traiter toute la
   doctrine d'emploi comme une question RH alors qu'elle reste d'abord un
   choix de commandement opérationnel.
7. Construire un dispositif événementiel sans avoir vérifié au préalable les
   autorisations administratives sous-jacentes (occupation du domaine
   public, débit de boissons) → `reglementation-appliquee.md`.
8. Confondre l'**élaboration du PCS** (document communal porté sous
   l'autorité du maire, par les services concernés) et la **seule
   contribution sécurité** de la PM à ce document.

---

## 9. Données / références à vérifier

- **Plan communal de sauvegarde** : art. **L. 731-3 du Code de la sécurité
  intérieure** (vérifié sur Légifrance le 2026-06-30 ; identifiant
  LEGIARTI000044375292) — vérifier en plus, au cas par cas, le **caractère
  obligatoire** pour la commune concernée (classement de risque, articles
  réglementaires R. 731-1 et suivants — à confirmer en version consolidée) et
  la **périodicité d'exercice** du plan.
- **Police générale du maire** : art. **L. 2212-1 et L. 2212-2 du CGCT**
  (L. 2212-2 vérifié sur Légifrance le 2026-06-30 ; identifiant
  LEGIARTI000029946370) — fondement de l'intervention du maire en gestion de
  crise communale et en dispositif événementiel communal ; pour le détail des
  pouvoirs, renvoyer à `pouvoirs-police.md`.
- **ZSP** : circulaire du ministère de l'Intérieur de 2012 (intitulé et
  référence exacts — à confirmer en version consolidée ; ce n'est pas un
  texte codifié, ne jamais lui attribuer un numéro LEGIARTI). Vérifier le
  dispositif territorial réellement actif localement à la date des faits, les
  ZSP ayant pu être remplacées ou complétées par d'autres priorités
  ministérielles depuis 2012.
- **Dispositif ORSEC** : cadre légal et réglementaire propre à la sécurité
  civile (code de la sécurité intérieure, Livre VII) — numéros d'articles
  précis à vérifier au cas par cas selon le point traité (déclenchement,
  rôle du DOS, articulation préfet/maire).
- **Cycles de travail PM** : régime statutaire et éventuelles dérogations
  propres à la filière → renvoi `rh-specificites-pm.md` ; ne pas citer de
  décret de mémoire ici.

---

## 10. Écrits & livrables

1. **Organisation** — note de doctrine d'emploi (missions prioritaires,
   modes de patrouille, sectorisation), fiche de cycle de service (en lien
   avec `rh-specificites-pm.md` pour la conformité statutaire).
2. **Dispositif événementiel** — ordre d'opération / fiche de dispositif
   (effectifs, missions, points de regroupement, procédure dégradée) ;
   distinct des **autorisations administratives** sous-jacentes, à produire
   via `assets/arrete-modele.md` le cas échéant.
3. **Gestion de crise** — maincourante de crise, fiche réflexe par type de
   risque, contribution PM au PCS communal.
4. **Pilotage** — note au maire/DGS sur le dimensionnement du service ou sur
   l'articulation avec un dispositif territorial (ZSP ou équivalent) →
   `assets/note-maire-modele.md`.
5. **Retour d'expérience** — après tout dispositif événementiel à enjeu ou
   toute gestion de crise → `retex.md`.

Aucun de ces écrits ne constitue, par lui-même, un acte faisant grief ; si un
dispositif débouche sur un **arrêté** (réglementation temporaire de
circulation, fermeture de voie), basculer vers `controle-legalite.md` avant
production.

---

## 11. Double échelle [risque / confiance]

- **Doctrine d'emploi, sectorisation de patrouille** : organisation interne —
  [risque faible / confiance stable] tant qu'aucun texte n'est invoqué comme
  contraignant.
- **Dispositif événementiel courant** (kermesse, marché) : [risque moyen /
  confiance stable] sur le fondement (police générale du maire) ; vérifier
  l'autorisation sous-jacente si occupation du domaine public ou débit de
  boissons.
- **Dispositif événementiel à forte affluence ou contexte de menace** :
  [risque élevé / à vérifier] — vérification obligatoire de la répartition
  des compétences et de l'articulation avec les forces de l'État.
- **Gestion de crise communale (PCS)** : [risque élevé / à vérifier] —
  vérifier le caractère obligatoire du plan et la chaîne de commandement
  (maire / préfet).
- **Bascule ORSEC / crise dépassant la compétence communale** : [risque
  critique / à vérifier] — abstention sur toute description précise de la
  chaîne de commandement sans vérification, renvoyer vers les autorités
  compétentes (préfecture, SDIS).
- **ZSP et dispositifs territoriaux analogues** : [risque moyen / à
  vérifier] — le dispositif change de nom et de cadre au fil des politiques
  publiques ; ne jamais présenter une doctrine ZSP comme stable dans le
  temps.

---

## 12. Checklist de branche

1. Qualification de la situation posée : organisation courante / événement /
   crise communale / crise dépassant la compétence communale ?
2. Autorité compétente identifiée (maire, et le cas échéant préfet) et rôle
   de la PM positionné comme **exécutant**, pas comme pilote ?
3. Garde-fou APJA rappelé si la situation peut déraper vers un acte
   judiciaire réservé à l'OPJ (`penal-procedure.md`) ?
4. Autorisations administratives sous-jacentes d'un dispositif événementiel
   vérifiées (renvoi `reglementation-appliquee.md`) avant de figer le
   dispositif sécurité ?
5. PCS : caractère obligatoire et actualisation vérifiés avant toute
   affirmation sur la commune concernée ?
6. ZSP ou dispositif territorial cité avec sa nature réelle (circulaire,
   non codifiée) et vérifié comme actif à la date des faits ?
7. Frontière RH respectée : cycle de travail traité comme organisation
   opérationnelle ici, renvoyé à `rh-specificites-pm.md`/`drh-fpt` pour sa
   conformité statutaire ?
8. Aucune référence d'article citée sans réserve « à confirmer en version
   consolidée », sauf les trois mentions vérifiées sur Légifrance le
   2026-06-30 (§9) ?
9. Couple [risque / confiance] indiqué selon le sous-domaine concerné (§11) ?
10. Si écrit produit : type identifié (organisation / dispositif / crise /
    pilotage / RETEX) et, si acte faisant grief, passage par
    `controle-legalite.md` ?
