# Générateur interactif — Arrêté (modèle) (v0.1.0)

> Couche 4 (`references/templates/`), piloté par `references/ecrits-professionnels.md`
> (§4, §5.1, §6 point 4, §10). Cet écrit n'est **pas** un écrit de
> constatation (PV, rapport) : c'est un **acte administratif de l'autorité
> territoriale**, susceptible de **faire grief**. À ce titre, ce générateur
> est **subordonné** à `references/controle-legalite.md` : la grille de
> contrôle a priori (§4 de ce fichier) doit être déroulée **avant** toute
> rédaction, et chaque réserve qu'elle soulève doit être reportée dans le
> brouillon produit ici.
>
> **Discipline d'écriture** : champs à compléter entre `[ ]`. **Aucune
> donnée nominative** (administré, agent) ne doit apparaître dans ce
> gabarit ni dans un brouillon produit en session — seuls des espaces
> réservés. Tout visa d'article, tout numéro de décision, toute date
> d'entrée en vigueur portent la réserve **« à confirmer en version
> consolidée »** tant qu'ils n'ont pas été vérifiés sur la source
> officielle dans la session en cours (socle-sources, `SKILL.md` §5.3).
> Référence de gabarit générique d'acte faisant grief :
> `Drh-fpt/assets/decision-modele.md` (structure visas / considérants /
> dispositif / voies de recours / check-list — transposée ici au champ
> police municipale et enrichie de la grille `controle-legalite.md`).

---

## 0. Pré-requis avant d'ouvrir le générateur

1. **Nature de l'acte qualifiée** (`controle-legalite.md` §3) : police
   générale (CGCT) ou police spéciale (laquelle) ; acte individuel ou
   réglementaire ; acte faisant grief ou non. Si la question relève en
   réalité d'un acte RH individuel (sanction, refus d'avancement, fin de
   fonctions d'un agent) → **frontière stricte** vers `drh-fpt`
   (`SKILL.md` §5.4) ; ce générateur reste compétent uniquement pour le
   contrôle de légalité de l'acte en tant que tel, en miroir.
2. **Garde-fou APJA testé** (`SKILL.md` §5.2) : un arrêté de police ne
   couvre jamais un acte réservé à l'OPJ. Si le contexte qui motive
   l'arrêté révèle une situation dépassant l'art. 21 CPP, afficher le
   **STOP** avant toute chose, rendre compte à l'OPJ et traiter l'aspect
   pénal séparément. Un rapport de mise à disposition ne se justifie que si
   une route 53/73 ou 78-6 est établie (`penal-procedure.md`).
3. **Conflit de compétence** (maire / préfet / OPJ) écarté ou signalé
   (`analyse-situation.md` §3, `controle-legalite.md` §4.1) : l'autorité
   envisagée comme signataire est-elle bien compétente sur cet objet
   précis (police générale du maire, ou police spéciale dont le titulaire
   réel doit être vérifié) ?
4. **Passage obligatoire par la grille de contrôle a priori**
   (`controle-legalite.md` §4, reprise et restituée au §4 ci-dessous) :
   ce générateur ne rédige **aucun** arrêté sans avoir déroulé cette
   grille dans l'ordre (compétence → procédure → base légale →
   motivation → proportionnalité → voies de recours → transmission).

---

## 1. Séquence de questions — une à une, jamais en bloc

**Règle de conduite** (`SKILL.md` §6, `ecrits-professionnels.md` §6.2) :
poser **un champ à la fois**, attendre la réponse, **confirmer** la valeur
reçue avant de passer au champ suivant. Ne jamais enchaîner plusieurs
questions dans le même tour. Si une réponse manque ou reste vague,
**relancer une fois** sur ce champ précis, puis, si elle reste
indisponible, basculer ce champ en `[INCOMPLET]` (§5) et continuer la
séquence sur les champs suivants plutôt que de bloquer tout l'entretien.

L'ordre ci-dessous suit la trame **qui / quand / où / pourquoi /
qualification / témoins / suites** imposée par `SKILL.md` §6, adaptée à un
acte administratif (pas un écrit de constatation : « témoins » devient
« tiers concernés / contradictoire », « qualification » devient « base
légale »).

### Étape 1 — Autorité et qualité du signataire (« qui » décide)
- Q1.1 : « Quelle est l'autorité signataire envisagée (le maire en
  personne, ou un délégataire — adjoint, conseiller délégué, DGS) ? »
- Q1.2 : « Si délégataire : un arrêté de délégation de signature ou de
  fonction existe-t-il, couvrant précisément cet objet ? Est-il publié et
  non retiré à la date envisagée de signature ? » — si la réponse est
  incertaine, marquer `[INCOMPLET — préciser : existence et périmètre de
  la délégation]` et signaler le risque d'incompétence (`controle-legalite.md`
  §4.1).
- Q1.3 : « Dans quelle commune et au titre de quelle compétence (police
  générale du maire au titre du CGCT, ou police spéciale — laquelle) ? »

### Étape 2 — Date d'effet et urgence (« quand »)
- Q2.1 : « Quelle est la date envisagée de signature de l'arrêté ? »
- Q2.2 : « Quelle doit être la date d'effet / d'entrée en vigueur ? »
  — rappel : pour un acte **défavorable à un administré identifié**, la
  date d'effet est en principe celle de la **notification**, pas de la
  signature (pas de rétroactivité d'un acte faisant grief — cf.
  `Drh-fpt/assets/decision-modele.md`, check-list).
- Q2.3 : « S'agit-il d'une mesure prise en **urgence** ? » — si oui,
  signaler que certaines formalités préalables (contradictoire,
  consultation) peuvent être allégées, **à vérifier au cas par cas**
  selon le texte applicable (`controle-legalite.md` §4.2) ; ne jamais
  présumer la dispense sans cette vérification.

### Étape 3 — Champ d'application géographique et personnel (« où »)
- Q3.1 : « L'arrêté est-il **réglementaire** (portée générale, ex. un
  périmètre, une voie, l'ensemble de la commune) ou **individuel** (vise
  une personne ou une situation déterminée) ? » — conditionne le régime
  de motivation CRPA et le mode de publicité (`controle-legalite.md`
  §3, §4.4).
- Q3.2 : « Quel est le périmètre géographique précis concerné (adresse,
  voie, portion de voie, zone délimitée, ou ensemble du territoire
  communal) ? » — exigence de précision : éviter toute formulation trop
  générale qui exposerait à un grief de mesure disproportionnée
  (`controle-legalite.md` §4.5).
- Q3.3 (si acte individuel) : « La mesure vise-t-elle une personne
  identifiée ? » — ne **jamais** inscrire de donnée nominative réelle
  dans le brouillon ; utiliser `[NOM Prénom]`, `[adresse]` en espace
  réservé.

### Étape 4 — Motifs et base légale (« pourquoi » / qualification)
- Q4.1 : « Quel trouble, risque ou objectif d'intérêt général motive cet
  arrêté (ordre public, sécurité, salubrité, tranquillité, autre police
  spéciale) ? Décrire les faits précis et datés qui le caractérisent. »
- Q4.2 : « S'agit-il d'un objet couvert par une **police spéciale** ?
  Si oui, laquelle, et qui en est le titulaire (parfois le maire au nom
  de l'État, parfois le préfet) ? » — renvoi obligatoire à
  `references/pouvoirs-police.md` pour trancher le fond ; ce générateur
  ne tranche jamais lui-même la compétence. Rappel : la police spéciale,
  quand elle existe, prime en principe sur la police générale pour le
  même objet, sauf circonstances locales particulières à motiver
  explicitement (`controle-legalite.md` §4.3).
- Q4.3 : « Quel texte fondateur précis souhaitez-vous viser (code,
  article exact) ? » — **ce générateur ne tranche jamais la base légale
  de fond lui-même** ; renvoi obligatoire à `references/pouvoirs-police.md`
  ou `references/reglementation-appliquee.md` selon l'objet. Si le texte
  proposé n'a pas été vérifié dans la session contre une source
  officielle, le marquer `⚠️ non vérifié — à confirmer en version
  consolidée avant signature`. Refuser tout visa générique type « vu le
  CGCT » sans article précis (`controle-legalite.md` §7, piège n° 1).
- Q4.4 : « La mesure envisagée est-elle la **moins attentatoire aux
  libertés** parmi celles permettant d'atteindre l'objectif ? Une mesure
  alternative moins restrictive a-t-elle été envisagée et, le cas
  échéant, pourquoi a-t-elle été écartée ? » — test de proportionnalité
  obligatoire (`controle-legalite.md` §4.5, principe posé par CE, Sect.,
  19 mai 1933, *Benjamin*, req. n° 17413 et 17520, Lebon p. 541,
  `CETATEXT000007636694` — vérifié le 2026-09-06, socle
  `references-verifiees.md` §7 ; déclinaisons récentes à vérifier via
  `recherche-juridique` en cas de doute).
  Si la mesure est générale et absolue dans le temps ou l'espace alors
  qu'une mesure ciblée suffirait, **signaler le risque élevé
  d'annulation** avant de poursuivre.

### Étape 5 — Procédure préalable et tiers concernés (équivalent « témoins »)
- Q5.1 : « Une consultation préalable obligatoire était-elle requise
  (commission, organisme consultatif selon l'objet) ? A-t-elle eu lieu et
  est-elle tracée ? » — propre à chaque police spéciale, à vérifier
  branche concernée (`controle-legalite.md` §4.2).
- Q5.2 (si acte individuel défavorable) : « La personne visée a-t-elle été
  mise en mesure de présenter des observations préalables (procédure
  contradictoire), sauf urgence ou exception légale ? » — si la réponse
  est négative sans justification claire, signaler le risque de vice de
  procédure.
- Q5.3 : « Quelles formalités de publicité sont prévues (affichage,
  publication au recueil des actes administratifs, notification
  individuelle) ? » — selon que l'acte est réglementaire ou individuel.

### Étape 6 — Dispositif et conséquences (suites — partie 1)
- Q6.1 : « Que doit décider précisément le dispositif (article 1er) ?
  Formuler la mesure exacte, datée et délimitée. »
- Q6.2 : « Y a-t-il des conséquences administratives ou financières
  associées (article 2) ? »
- Q6.3 : « Qui est chargé de l'exécution (DGS, chef de service de police
  municipale, autre) ? »

### Étape 7 — Voies de recours et transmission (suites — partie 2)
- Q7.1 : « Cet acte fait-il grief à un administré identifié ou à une
  catégorie d'administrés (mesure individuelle ou réglementaire
  défavorable) ? » — si **oui**, les voies et délais de recours sont
  **obligatoires** dans le dispositif (`controle-legalite.md` §4.6) ; leur
  omission n'invalide pas l'acte mais **empêche le délai de recours
  contentieux de courir** contre l'administré — risque pratique majeur à
  signaler explicitement si la réponse à cette question reste incertaine.
- Q7.2 : « L'acte figure-t-il dans la liste des actes soumis à
  transmission obligatoire au représentant de l'État (art. L. 2131-2
  CGCT, vérifié sur Légifrance le 2026-06-30 — liste précise et seuils à
  reconfirmer en version consolidée selon l'objet exact) ? » — en cas de
  doute, rappeler que la posture la plus sûre reste de transmettre
  (`controle-legalite.md` §4.7), sans pour autant affirmer l'obligation
  comme acquise si elle n'a pas été vérifiée.
- Q7.3 : « Quel circuit de transmission et de notification est applicable
  localement (transmission dématérialisée au contrôle de légalité,
  notification LRAR ou décharge à l'administré) ? » — si la donnée
  manque, marquer `[INCOMPLET — préciser : circuit de transmission /
  notification]` plutôt que de la deviner.

---

## 2. Garde-fous transverses pendant la séquence

- Si, à l'**Étape 1** ou à l'**Étape 4**, il apparaît un **conflit de
  compétence** (objet relevant en réalité du préfet, ou d'une police
  spéciale dont le maire n'est pas titulaire) : suspendre l'assemblage,
  signaler le conflit, renvoyer à `analyse-situation.md` §3 et
  `pouvoirs-police.md` avant de poursuivre.
- Si, à l'**Étape 1**, il apparaît que l'acte est en réalité une **mesure
  RH individuelle** concernant un agent (sanction, refus d'avancement,
  fin de fonctions) : ce générateur reste compétent pour le contrôle de
  légalité de l'acte en tant que tel, mais la **conduite de la
  procédure** statutaire relève de `drh-fpt` (`SKILL.md` §5.4) — le
  signaler explicitement et orienter l'utilisateur.
- Si, à l'**Étape 4**, le contexte motivant l'arrêté révèle une situation
  dépassant le pouvoir APJA (acte réservé à l'OPJ ; l'art. 16 CPP définit
  notamment la qualité d'OPJ, mais le texte propre à l'acte doit être cité) :
  afficher le
  **STOP** (`SKILL.md` §5.2) avant toute chose ; l'arrêté de police ne
  peut pas se substituer à l'action pénale requise.

---

## 3. Grille de contrôle a priori — à dérouler avant rédaction

Reprise opérationnelle de `controle-legalite.md` §4, **dans cet ordre**,
posture « juge administratif » (légalité externe avant légalité interne).
Aucune ligne ne peut être cochée par défaut : chacune doit être levée par
une réponse explicite obtenue en §1, ou listée comme réserve.

1. **Compétence** (§4.1) — autorité signataire détentrice du pouvoir
   exercé ? Délégation vérifiée (existence, publication, périmètre,
   non-retrait) si signataire ≠ maire ? Compétence territoriale
   respectée ? Pas d'incompétence négative (l'autorité ne s'est pas crue
   liée alors qu'elle disposait d'un pouvoir d'appréciation) ?
2. **Procédure** (§4.2) — consultations obligatoires tracées ?
   Procédure contradictoire respectée pour une mesure individuelle
   défavorable, sauf urgence/exception justifiée ? Formalités de
   publicité identifiées ? Acte daté et signé ?
3. **Base légale** (§4.3) — texte fondateur cité avec article exact (pas
   de visa générique) ? Police générale/spéciale correctement
   distinguées, primauté de la spéciale respectée ou circonstances
   locales particulières motivées ? Absence de détournement de pouvoir
   (motif réel = finalité légale du texte) ? Faits visés exacts et
   matériellement établis ?
4. **Motivation CRPA** (§4.4) — si la décision relève de l'art. L. 211-2
   du CRPA *(vérifié sur Légifrance le 2026-06-30)* (mesure de police,
   décision restreignant une liberté publique, refus d'autorisation,
   retrait/abrogation d'une décision créatrice de droits) : motivation
   en fait **et** en droit complète, non stéréotypée, permettant à un
   tiers de comprendre pourquoi cette mesure précise — et pas une mesure
   moins contraignante — a été prise.
5. **Proportionnalité** (§4.5) — mesure strictement nécessaire, limitée
   dans le temps et l'espace, alternative moins restrictive envisagée et
   écartée si pertinent ? Signal d'alerte si interdiction générale et
   absolue.
6. **Voies et délais de recours** (§4.6) — mentionnés si l'acte fait
   grief : recours gracieux, hiérarchique, contentieux, délai, autorité
   ou juridiction compétente.
7. **Transmission au contrôle de légalité** (§4.7) — acte inclus dans la
   liste de l'art. L. 2131-2 CGCT ? Caractère exécutoire conditionné à la
   publicité et, le cas échéant, à la transmission (art. L. 2131-1 CGCT,
   vérifiés sur Légifrance le 2026-06-30) ? Délai de transmission
   identifié (ordre de grandeur 15 jours pour une décision individuelle —
   à confirmer en version consolidée) ?

**Décision à l'issue de la grille** : produire / corriger / abstenir
(`controle-legalite.md` §2). Si un point reste non levé, ne **jamais**
le combler par supposition : le reporter en réserve explicite dans le
brouillon (§5) et, si la décision finale appartient au maire, le
signaler clairement comme un risque accepté à assumer en connaissance de
cause.

---

## 4. Mentions obligatoires — grille de vérification avant assemblage

Avant d'assembler le document final, vérifier que chacune des mentions
suivantes est renseignée ou explicitement marquée `[INCOMPLET]` :

**Visas et procédure :**
- [ ] Autorité signataire identifiée, délégation vérifiée si applicable
- [ ] Visas précis (texte + article exact), pas de visa générique
- [ ] Consultations préalables obligatoires tracées, le cas échéant
- [ ] Procédure contradictoire tracée pour une mesure individuelle
      défavorable, sauf urgence/exception justifiée

**Considérants (motivation en fait et en droit) :**
- [ ] Exposé des faits précis et datés
- [ ] Motif de droit rattaché au texte visé
- [ ] Test de proportionnalité explicitement passé (nécessité,
      adaptation, mesure la moins attentatoire, alternative envisagée)

**Dispositif :**
- [ ] Mesure décidée formulée précisément, datée, délimitée dans le temps
      et l'espace
- [ ] Date d'effet = notification pour un acte défavorable (pas de
      rétroactivité)
- [ ] Conséquences administratives/financières le cas échéant
- [ ] Voies et délais de recours mentionnés si l'acte fait grief (§Q7.1)
- [ ] Autorité chargée de l'exécution identifiée
- [ ] Mention de la transmission au contrôle de légalité si applicable
      (§Q7.2) et du circuit de notification (§Q7.3)

---

## 5. Règle `[INCOMPLET]` — application stricte

Conformément à `SKILL.md` §6 et `ecrits-professionnels.md` §5.5 :
**interdiction absolue d'halluciner une donnée manquante** (autorité
signataire, délégation, base légale précise, faits motivant la mesure,
date d'effet, voies de recours, circuit de transmission).

Si une information nécessaire n'a pas été fournie à l'issue de la
séquence de questions (§1) ou de la grille de contrôle (§3) :
1. Produire le brouillon avec les champs disponibles.
2. Marquer chaque champ manquant par
   `[INCOMPLET — préciser : <nom du champ>]` directement dans le corps du
   document, à l'endroit où l'information devrait figurer.
3. Lister ces champs en fin de document, section **« Champs manquants à
   compléter »**, en distinguant les champs **factuels** (date, lieu,
   identité) des **réserves de contrôle de légalité** (compétence non
   vérifiée, délégation non confirmée, proportionnalité non testée,
   obligation de transmission incertaine).
4. **Demander explicitement** ces données à l'utilisateur avant de
   considérer l'arrêté comme finalisé.
5. **Ne jamais transmettre, viser, signer, ni présenter comme définitif**
   un arrêté portant une mention `[INCOMPLET]` non résolue — *a fortiori*
   un acte faisant grief, dont l'irrégularité expose la collectivité à
   une annulation contentieuse.

---

## 6. Gabarit d'assemblage

> Champs entre `[ ]`. Aucune donnée nominative réelle dans ce gabarit.
> Tout numéro d'article, toute référence de décision, porte sa réserve
> tant qu'elle n'a pas été vérifiée dans la session en cours. Structure
> reprise de `Drh-fpt/assets/decision-modele.md`, adaptée au champ police
> municipale (police générale/spéciale du maire) et enrichie de la
> grille `controle-legalite.md`.

```
[COLLECTIVITÉ — en-tête]

ARRÊTÉ N° [numéro] / [année]
portant [objet précis de la mesure de police : réglementation de …,
interdiction de …, mesure individuelle de … — formulation exacte issue
de Q6.1]

[L'AUTORITÉ TERRITORIALE — Le Maire / le délégataire identifié en Q1.1,
qualité précise],

VU le Code général des collectivités territoriales, notamment son
   article [L. … relatif au pouvoir de police mobilisé — à confirmer en
   version consolidée] ;
VU [le code ou texte spécial fondant la police spéciale invoquée, le cas
   échéant — article exact, renvoi pouvoirs-police.md / reglementation-
   appliquee.md — ⚠️ à confirmer en version consolidée si non vérifié
   dans la session] ;
VU le Code des relations entre le public et l'administration, notamment
   son article L. 211-2 (motivation des décisions défavorables) [si
   l'acte relève de ce régime — Étape 4, grille §3 point 4] ;
VU [l'arrêté de délégation de signature/fonction du [date], publié le
   [date], si le signataire n'est pas le maire en personne — référence
   exacte [INCOMPLET] si non fournie] ;
VU [les actes de la procédure préalable : avis, consultation,
   notification du contradictoire — référence et date] ;

CONSIDÉRANT [exposé des faits précis et datés justifiant la mesure —
Étape 4, Q4.1] ;
CONSIDÉRANT [le motif de droit, rattaché au texte visé — Étape 4,
Q4.2-Q4.3] ;
CONSIDÉRANT que la mesure envisagée est strictement nécessaire,
   limitée dans le temps et dans l'espace au strict besoin, et constitue
   la mesure la moins attentatoire aux libertés permettant d'atteindre
   l'objectif poursuivi [détailler le test de proportionnalité et
   l'alternative écartée le cas échéant — Étape 4, Q4.4] ;
[CONSIDÉRANT la procédure suivie : consultation, contradictoire, délai,
   avis — Étape 5, si applicable] ;

ARRÊTE :

Article 1er — [dispositif : mesure décidée, précise, datée et délimitée
   dans le temps et l'espace — Étape 6, Q6.1], à compter de [date
   d'effet — en principe la NOTIFICATION pour un acte défavorable ; pas
   de rétroactivité].
Article 2 — [conséquences administratives / financières le cas échéant —
   Q6.2, ou « Sans objet »].
Article 3 — [Si l'acte fait grief — Q7.1 positif] Le présent arrêté peut
   faire l'objet, dans un délai de DEUX MOIS à compter de sa
   notification [ou de sa publication, selon la nature de l'acte] :
   - d'un recours gracieux auprès de [l'autorité signataire] ;
   - d'un recours hiérarchique [si applicable] ;
   - d'un recours contentieux devant le tribunal administratif de
     [ville].
   Le recours administratif préalable proroge le délai de recours
   contentieux.
   [Si l'acte ne fait pas grief : « Article 3 — Sans objet (acte non
   créateur de grief au sens de controle-legalite.md §3) », et signaler
   ce choix comme un point à confirmer plutôt qu'une certitude définitive
   si un doute subsiste.]
Article 4 — [Le DGS / le chef de service de police municipale / autre,
   identifié en Q6.3] est chargé(e) de l'exécution du présent arrêté, qui
   sera [notifié à l'intéressé(e) par voie traçable (LRAR / décharge) /
   publié et affiché] et [transmis au contrôle de légalité — si
   applicable selon Q7.2, circuit précisé en Q7.3, ou « non soumis à
   transmission obligatoire — à confirmer en version consolidée selon
   l'art. L. 2131-2 CGCT »].

Fait à [lieu], le [date].
[Signature de l'autorité territoriale identifiée en Q1.1]
```

---

## 7. Exécution et transmission

- **Caractère exécutoire** : l'arrêté ne devient exécutoire de plein
  droit qu'après **publicité** (publication/affichage/notification) et,
  pour les actes figurant à l'art. **L. 2131-2 du CGCT**, après sa
  **transmission** au représentant de l'État — art. **L. 2131-1 du CGCT**
  *(vérifié sur Légifrance le 2026-06-30)*. Tant que la transmission
  requise n'est pas faite, l'acte **n'est pas exécutoire**, même signé et
  publié — distinguer cette **absence de caractère exécutoire** de
  l'**illégalité** proprement dite (deux risques distincts,
  `controle-legalite.md` §7 piège n° 2).
- **Délai de transmission** des décisions individuelles : ordre de
  grandeur **15 jours** à compter de la signature — **à confirmer en
  version consolidée**, l'article exact étant fonction de la nature de
  la décision (`controle-legalite.md` §4.7, §8).
- **Actes non transmissibles** (gestion interne, actes de droit privé,
  actes pris au nom de l'État) : art. **L. 2131-4 du CGCT (à confirmer en
  version consolidée)** ; en cas de doute, transmettre reste la posture
  la plus sûre plutôt que de présumer une dispense.
- **Notification** à l'administré concerné (acte individuel) par voie
  traçable (LRAR / décharge), distincte de la transmission au contrôle de
  légalité.
- **Archivage** : conserver une trace de la version signée, de la date et
  du mode de publicité, ainsi que de la date et de l'accusé de
  transmission au contrôle de légalité, en vue d'une éventuelle
  contestation (`contentieux.md` pour l'anticipation des faiblesses
  après édiction, hors périmètre de ce générateur).
- Avant toute signature ou transmission, vérifier que l'arrêté ne porte
  **aucune mention `[INCOMPLET]`** non résolue (§5) — un acte faisant
  grief incomplet ne doit jamais être présenté comme définitif.

---

## 8. Checklist finale avant restitution de l'arrêté

1. Garde-fous transverses testés (§2) : pas de conflit de compétence non
   signalé, pas de bascule RH non renvoyée à `drh-fpt`, pas d'acte
   réservé OPJ confondu avec une mesure de police administrative.
2. Grille de contrôle a priori (§3) déroulée **dans l'ordre** : compétence
   → procédure → base légale → motivation → proportionnalité → voies de
   recours → transmission ; aucun point coché par défaut.
3. Séquence de questions déroulée **une à une**, confirmation obtenue à
   chaque étape (§1).
4. **Compétence et délégation** vérifiées (existence, publication,
   périmètre, non-retrait) si signataire ≠ maire.
5. **Base légale** citée avec article précis, police générale/spéciale
   correctement distinguées, primauté de la spéciale respectée ou
   circonstances locales motivées.
6. **Motivation en fait et en droit** complète si l'acte relève de
   l'art. L. 211-2 CRPA — non stéréotypée.
7. **Test de proportionnalité** explicitement passé, alternative moins
   restrictive envisagée et écartée si pertinent.
8. **Voies et délais de recours** mentionnés si l'acte fait grief (Q7.1) ;
   signalé comme risque pratique majeur si la réponse à Q7.1 reste
   incertaine.
9. **Obligation de transmission au contrôle de légalité** vérifiée
   (art. L. 2131-2 CGCT) et circuit/délai identifiés ou `[INCOMPLET]`.
10. Toutes les mentions de §4 renseignées ou explicitement `[INCOMPLET]`.
11. Aucune donnée nominative réelle insérée dans un gabarit ou un
    brouillon de travail — uniquement des espaces réservés.
12. Section **« Champs manquants à compléter »** présente si au moins un
    `[INCOMPLET]` subsiste, distinguant champs factuels et réserves de
    contrôle de légalité, et demande explicite formulée à l'utilisateur.
13. Toute référence numérotée porte sa réserve « à confirmer en version
    consolidée » ou la mention « vérifié sur Légifrance le JJ/MM/AAAA »
    (règle de provenance, `SKILL.md` §5.3).
14. Arrêté **non signé, non transmis, non visé comme définitif** tant
    qu'un `[INCOMPLET]` ou une réserve de la grille §3 subsiste.

[risque : critique — acte faisant grief, exposition contentieuse directe
sur la collectivité en cas d'irrégularité (compétence, motivation,
proportionnalité, transmission) / confiance : stable sur les principes
de `controle-legalite.md` (compétence, motivation CRPA, art. L. 2131-1 et
L. 2131-2 CGCT — vérifiés sur Légifrance le 2026-06-30 ; proportionnalité
*Benjamin*, req. n° 17413 et 17520, Lebon p. 541, `CETATEXT000007636694` —
vérifié le 2026-09-06), à vérifier systématiquement sur la base légale de fond
propre à chaque police (générale ou spéciale), sur l'existence et le
périmètre exact d'une délégation de signature, et sur les seuils/délais
chiffrés de transmission (à confirmer en version consolidée)]
