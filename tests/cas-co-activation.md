# Cas transverses — co-activation `dpm-fpt`

> Ces cas testent la **collaboration de `dpm-fpt` avec un autre skill**. Ils
> supposent donc que les skills concernés sont installés (test Claude Code).
> Le sous-agent répondant reçoit les skills + l'énoncé, **jamais** ce barème.

---

## CAS 1 — `dpm-fpt` × `recherche-juridique`

### Énoncé

> Je suis Directeur de Police Municipale. Le maire veut un **arrêté municipal**
> interdisant **toute consommation d'alcool sur la voie publique sur l'ensemble
> du territoire communal, 24h/24, sans limite de durée**, suite à des
> nuisances répétées sur deux places du centre-ville le week-end. Prépare-moi
> cet **arrêté**, avec ses **visas à jour**, et confirme-moi que cette mesure
> **tient devant le juge administratif**. Sois rigoureux : **aucune référence
> non vérifiée**.

### Pourquoi ce cas co-active les deux skills

- **`dpm-fpt`** : DPM, pouvoir de police générale du maire (CGCT), production
  d'un acte (arrêté), passage obligatoire par `controle-legalite.md` avant
  toute rédaction (`SKILL.md` §6, `analyse-situation.md` §4), test de
  proportionnalité (§4.5 de `controle-legalite.md`), jurisprudence Benjamin
  déjà embarquée dans le socle de la brique.
- **`recherche-juridique`** : « visas à jour », « tient devant le juge
  administratif », « aucune référence non vérifiée » déclenchent le mode
  sourcé — vérification de la vigueur du fondement CGCT invoqué, recherche/
  triangulation de la jurisprudence de proportionnalité au-delà du principe
  constant déjà cité par `controle-legalite.md`, format de citation traçable.

La réussite suppose une **collaboration** : `dpm-fpt` qualifie la mesure,
détecte le risque de disproportion (mesure générale et absolue, sans limite de
temps ni d'espace) et structure l'audit a priori ; `recherche-juridique`
sécurise la vigueur des textes visés et la traçabilité de la jurisprudence
citée.

### Barème — RÉUSSITE si…

1. **Qualification** : pouvoir de **police générale du maire** (ordre public,
   tranquillité/salubrité publiques), pas une police spéciale ; base CGCT
   (police générale du maire, articles à confirmer en version consolidée),
   citée comme telle et non affirmée de mémoire avec un numéro précis non
   vérifié.
2. **Passage explicite par `controle-legalite.md` AVANT toute rédaction** —
   pas seulement un arrêté produit directement : la grille de contrôle (§4)
   doit être déroulée ou au moins ses points structurants restitués
   (compétence, procédure, base légale, motivation, proportionnalité,
   recours, transmission).
3. **Test de proportionnalité explicitement mené et négatif sur la version
   demandée** : la mesure telle que demandée (interdiction **générale,
   absolue, 24h/24, tout le territoire, sans durée**) est signalée comme
   **à haut risque d'annulation** — c'est une interdiction générale et
   absolue alors qu'un trouble localisé (deux places, week-end) appelle une
   mesure **ciblée dans le temps et l'espace**.
4. **Jurisprudence Benjamin citée correctement et de façon traçable** : CE,
   Sect., 19 mai 1933, *Benjamin*, comme principe de proportionnalité des
   mesures de police (mesure la moins attentatoire aux libertés permettant
   d'atteindre le but). Toute référence complémentaire (arrêt plus récent,
   déclinaison jurisprudentielle, numéro de requête) **non vérifiée en
   session** doit être marquée explicitement « à confirmer » / « non
   vérifiée », jamais présentée comme acquise.
5. **Réserve sur les références non vérifiées** : tout article CGCT cité
   porte la mention « à confirmer en version consolidée » sauf si une
   vérification a réellement eu lieu en session (auquel cas la date de
   vérification est indiquée) — aucun numéro d'article ni de requête reconstitué
   de mémoire et présenté comme certain.
6. **Recommandation alternative concrète** : propose une version resserrée
   (ex. interdiction limitée aux deux places identifiées, créneaux horaires
   définis, durée limitée et réexaminée) comme mesure proportionnée
   alternative, conformément au test en 3 questions de `controle-legalite.md`
   §4.5.
7. **Si l'arrêté est malgré tout rédigé** : il comporte motivation en fait et
   en droit (CRPA), voies et délais de recours, mention de la transmission au
   contrôle de légalité (CGCT, liste de transmission) — et le risque de
   disproportion reste signalé comme réserve même si le document est livré à
   la demande de l'utilisateur.
8. **Co-activation visible** : la qualification métier (police générale,
   risque de disproportion) **et** la sécurisation juridique sourcée/datée
   coexistent dans la réponse, pas seulement l'une des deux.

### ÉCHEC si…

- Rédige l'arrêté **tel que demandé** (interdiction générale, absolue, sans
  limite de temps ni d'espace) **sans signaler le risque de disproportion**.
- **Invente ou affirme avec certitude** un numéro d'article CGCT ou un numéro
  de requête/arrêt sans réserve.
- Ne mentionne **pas** la jurisprudence Benjamin ou le test de
  proportionnalité alors qu'une mesure générale et absolue est en jeu.
- Saute `controle-legalite.md` et produit l'acte directement depuis
  `pouvoirs-police.md` seul.
- Présente une référence jurisprudentielle récente ou secondaire comme
  vérifiée sans la marquer « à confirmer ».

### Demi-réussite (co-activation incomplète)

Le risque de disproportion est bien identifié et Benjamin correctement cité,
**mais** aucune réserve n'est posée sur les articles CGCT visés (pas de
mention « à confirmer » ni de date de vérification) — **ou** l'inverse :
sourcing rigoureux des textes, mais le test de proportionnalité n'est pas
mené et l'arrêté générique est produit sans alternative resserrée proposée.

---

## CAS 2 — `dpm-fpt` × `drh-fpt`

### Énoncé

> Je suis Directeur de Police Municipale. Un de mes agents a été vu, en
> dehors de son service mais en tenue, en train de **consulter le fichier des
> immatriculations (SIV) pour rendre service à un voisin** qui voulait
> connaître l'identité du propriétaire d'un véhicule garé devant chez lui.
> Aucun journal de consultation ne mentionne de motif légitime. Dis-moi ce que
> je dois faire : **qualifie le manquement, et lance la procédure
> disciplinaire** contre cet agent.

### Pourquoi ce cas co-active les deux skills

- **`dpm-fpt`** : manquement déontologique d'un agent PM (code de
  déontologie PM, CSI partie réglementaire), traçabilité des consultations de
  fichiers, cumul potentiel pénal/administratif/disciplinaire —
  `conformite-deontologie-donnees.md`.
- **`drh-fpt`** : la demande explicite « lance la procédure disciplinaire »
  exige la bascule prévue par la **règle de bascule** `SKILL.md` §5.4 : dès
  que la question porte sur la **conduite de la procédure** (saisine du
  conseil de discipline, droits de la défense, échelle des sanctions), c'est
  `drh-fpt` qui prend la main — `dpm-fpt` ne doit pas se substituer à lui.

La réussite suppose que `dpm-fpt` **fasse le constat textuel** du manquement
(qualification au regard du code de déontologie PM, signalement du cumul de
voies) puis **passe explicitement la main** à `drh-fpt` pour tout ce qui
relève de la procédure disciplinaire elle-même, sans la conduire lui-même.

### Barème — RÉUSSITE si…

1. **Constat du manquement effectué par `dpm-fpt`** : qualification du fait
   au regard du code de déontologie des agents de police municipale (CSI,
   partie réglementaire — probité, respect de la loi, consultation hors cadre
   de la finalité légale), avec réserve sur le numéro d'article exact
   (« à confirmer en version consolidée » sauf vérification effective en
   session).
2. **Cumul des voies signalé** : la consultation hors cadre est présentée
   comme pouvant caractériser **à la fois** un manquement déontologique, une
   violation potentielle du RGPD (détournement de finalité, à signaler au
   DPO) et une éventuelle infraction pénale (atteinte au secret/détournement
   de fichier) — ces trois voies **cumulables et indépendantes**, pas
   exclusives l'une de l'autre.
3. **Traçabilité et contrôle interne** : recommandation de sécuriser/
   consulter le journal de connexion (preuve), remontée hiérarchique
   immédiate, préservation des éléments avant toute décision sur la suite.
4. **Bascule explicite et claire vers `drh-fpt`** dès que la demande porte
   sur le **lancement** de la procédure disciplinaire : `dpm-fpt` **ne**
   rédige **pas** lui-même la saisine du conseil de discipline, ne détaille
   pas l'échelle des sanctions applicables, ne fixe pas les droits de la
   défense ou les délais de la procédure — il indique que cette suite relève
   de `drh-fpt` et l'invoque/le signale comme tel.
5. **Pas de confusion constat/procédure** : la réponse distingue clairement
   ce qui reste dans `dpm-fpt` (qualification du fait, rapport de constat,
   signalement RGPD au DPO, articulation avec le contrôle interne du
   service) de ce qui part chez `drh-fpt` (conduite de la procédure
   disciplinaire elle-même).
6. **Livrable produit par `dpm-fpt`** : un rapport de constat (description
   factuelle, articles potentiellement concernés sous réserve, transmission à
   la hiérarchie), sans anticiper la qualification disciplinaire finale qui
   appartient à `drh-fpt`.
7. **Co-activation visible** : le constat déontologique (`dpm-fpt`) et la
   prise de relais procédurale (`drh-fpt`) apparaissent **tous les deux**,
   articulés et non fusionnés en un seul traitement indifférencié.

### ÉCHEC si…

- `dpm-fpt` **conduit lui-même la procédure disciplinaire** (rédige une
  saisine du conseil de discipline, fixe une sanction, détaille les droits de
  la défense ou la procédure contradictoire disciplinaire) sans renvoyer à
  `drh-fpt`.
- Aucune bascule n'est mentionnée : la réponse traite le sujet de bout en
  bout comme si la procédure disciplinaire relevait de `dpm-fpt`.
- Le manquement n'est **pas qualifié** du tout (pas de mention du code de
  déontologie PM, traitement uniquement procédural).
- Présente la voie disciplinaire comme **exclusive** de la voie pénale ou du
  signalement RGPD, ou omet totalement le volet RGPD/traçabilité alors que la
  consultation de fichier hors cadre est explicitement en cause.
- Invente un numéro d'article du code de déontologie sans réserve.

### Demi-réussite (co-activation incomplète)

Le constat déontologique est correctement posé par `dpm-fpt` (qualification,
cumul des voies, traçabilité) **mais** la bascule vers `drh-fpt` n'est que
vague ou implicite (pas de signal explicite du changement de compétence) —
**ou** la bascule vers `drh-fpt` est bien faite mais le constat textuel
préalable (code de déontologie, cumul pénal/RGPD/disciplinaire) est absent ou
superficiel.

---

## CAS 3 — `dpm-fpt` × `drh-fpt` : inaptitude au port d'arme (bascule)

### Énoncé

> Je suis Directeur de Police Municipale. La médecine préventive vient de
> déclarer un de mes agents **inapte au port d'arme pour 6 mois**. Quelles
> conséquences sur son **autorisation de port d'arme**, ses **missions**, et
> sa **situation administrative** ?

### Pourquoi ce cas co-active les deux skills

- **`dpm-fpt`** : condition d'exercice de l'armement (aptitude = condition du
  port effectif, `armement-equipements.md`), information du préfet,
  réorganisation des missions du service.
- **`drh-fpt`** : la « situation administrative » (aptitude médicale
  statutaire, aménagement de poste, position de l'agent) relève du volet RH
  statutaire — bascule `SKILL.md` §5.4.

### Barème — RÉUSSITE si…

1. `dpm-fpt` traite le volet métier : l'inaptitude suspend le port effectif ;
   l'**autorisation préfectorale** est fragilisée (retrait/suspension possible,
   information du préfet), références du socle ou « à confirmer ».
2. Réorganisation opérationnelle proposée (missions sans port d'arme,
   doublures) **sans** trancher la situation statutaire.
3. **Bascule explicite vers `drh-fpt`** pour l'aptitude médicale statutaire,
   l'aménagement de poste et la position administrative de l'agent.
4. L'ordre des volets est cohérent : sécurité juridique de l'armement d'abord
   (aucun port tant que l'aptitude n'est pas rétablie), statutaire ensuite.
5. Aucune référence de mémoire sans réserve.

### ÉCHEC si…

- `dpm-fpt` instruit lui-même l'aménagement de poste ou la position
  statutaire, ou aucune bascule n'est signalée.
- La réponse laisse entendre que l'agent peut continuer à porter l'arme en
  attendant.
- Référence inventée/affirmée sans réserve.

### Demi-réussite

Volet armement correct mais bascule RH vague ou implicite — **ou** bascule
nette mais volet armement incomplet (autorisation préfectorale non traitée).

---

## CAS 4 — `dpm-fpt` × `drh-fpt` : agent blessé en interpellation (double voie)

### Énoncé

> Un agent s'est blessé hier en **interpellant un individu violent** (entorse,
> 10 jours d'arrêt). L'individu a été remis à la BAC. Qu'est-ce que je dois
> faire **côté service** et **côté agent** ?

### Pourquoi ce cas co-active les deux skills

- **`dpm-fpt`** : volet opérationnel — qualification préalable de la
  flagrance (art. 53 CPP) et des conditions de l'appréhension (art. 73 CPP),
  puis, si elles sont réunies, rapport de mise à disposition ; RETEX
  (`retex.md`) et constat des faits utiles à la protection fonctionnelle.
- **`drh-fpt`** : accident de service (CITIS, imputabilité), droits de
  l'agent, instruction de la protection fonctionnelle.

### Barème — RÉUSSITE si…

1. Volet opérationnel traité par `dpm-fpt` : vérification que les faits
   caractérisent un crime flagrant ou un délit flagrant puni d'emprisonnement
   avant de retenir l'art. 73 ; rapport de mise à disposition seulement si ce
   fondement est établi, RETEX du service via `retex.md`, consignation
   factuelle des circonstances de la blessure.
2. **Deux voies parallèles explicitement signalées** : opérationnelle
   (service) et statutaire (agent), indépendantes et cumulatives.
3. **Bascule explicite vers `drh-fpt`** pour l'accident de service (CITIS,
   imputabilité) et l'instruction de la protection fonctionnelle — `dpm-fpt`
   fournit le constat, ne conduit pas l'instruction.
4. La protection fonctionnelle est signalée (agent blessé par un tiers dans
   l'exercice de ses fonctions) sans être détaillée statutairement.
5. Aucune référence de mémoire sans réserve.

### ÉCHEC si…

- Le CITIS ou la protection fonctionnelle sont instruits par `dpm-fpt`.
- Le RETEX est absent, ou le rapport de mise à disposition est présenté comme
  automatique sans qualification des art. 53 et 73 (volet service erroné).
- Une seule des deux voies est traitée.
- Référence inventée/affirmée sans réserve.

### Demi-réussite

Les deux voies sont présentes mais la bascule n'est qu'implicite — **ou** la
bascule est nette mais le RETEX ou la qualification préalable de la route
53/73 manque.

---

## CAS 5 — `dpm-fpt` × `drh-fpt` : création d'une brigade de nuit (co-construction)

### Énoncé

> Le maire veut une **brigade de nuit (22 h – 6 h)** à effectif constant.
> Construis-moi le **projet** : organisation, moyens, et ce que ça implique
> **pour les agents**.

### Pourquoi ce cas co-active les deux skills

- **`dpm-fpt`** : doctrine opérationnelle (missions de nuit, binômes,
  armement/équipement nocturne, coordination avec les forces de l'État,
  convention de coordination à réviser).
- **`drh-fpt`** : cycles de travail, travail de nuit, repos, régime
  indemnitaire — volet statutaire à ne pas chiffrer ni instruire côté
  `dpm-fpt`.

### Barème — RÉUSSITE si…

1. Volet doctrine construit par `dpm-fpt` : missions nocturnes, patrouilles
   en binôme minimum, équipement, articulation avec PN/gendarmerie de nuit et
   **impact sur la convention de coordination** (plages horaires, armement de
   nuit) — références du socle ou « à confirmer ».
2. **Bascule explicite vers `drh-fpt`** pour cycles de travail, garanties du
   travail de nuit, repos et régime indemnitaire.
3. **Aucune indemnité ni durée réglementaire chiffrée de mémoire** (valeurs
   volatiles).
4. Le livrable final articule les deux volets (ex. note au maire unique
   distinguant « dispositif » et « volet agents ») en attribuant chaque volet
   au bon skill.
5. Aucune référence de mémoire sans réserve.

### ÉCHEC si…

- `dpm-fpt` fixe les cycles, les compensations ou les indemnités de nuit.
- Le projet ignore l'impact convention de coordination / armement de nuit.
- Aucune bascule signalée.
- Référence inventée/affirmée sans réserve.

### Demi-réussite

Doctrine solide mais bascule RH vague — **ou** bascule nette mais le volet
doctrine omet la convention de coordination ou l'armement de nuit.
