# Générateur interactif — PV de contravention (v0.1.0)

> Couche 4 (`assets/`), piloté par `references/ecrits-professionnels.md`
> (§4, §5, §6, §10). Avant tout usage de ce générateur, le routeur
> `references/analyse-situation.md` et le test du **garde-fou APJA**
> (`SKILL.md` §5.2) doivent déjà avoir validé que la situation relève bien
> d'un **PV de contravention** au sens de `ecrits-professionnels.md` §5.1
> (constatation directe d'une contravention, dans le champ de compétence
> matérielle de l'agent — art. 21 CPP + texte spécial, ex. art. L. 130-4
> code de la route, à confirmer en version consolidée).
>
> **Discipline d'écriture** : champs à compléter entre `[ ]`. **Aucune
> donnée nominative** ne doit apparaître dans ce gabarit ni dans un
> brouillon produit en session — seuls des espaces réservés
> (`[NOM Prénom]`, `[adresse]`, `[plaque]`…). Tout visa d'article et toute
> référence numérotée portent la réserve **« à confirmer en version
> consolidée »** tant qu'ils n'ont pas été vérifiés sur la source officielle
> dans la session en cours (socle-sources, `SKILL.md` §5.3).

---

## 0. Pré-requis avant d'ouvrir le générateur

1. **Garde-fou APJA testé** (`SKILL.md` §5.2, `penal-procedure.md` §4.4-4.5) :
   le fait constaté reste-t-il dans le périmètre de l'art. 21 CPP (à
   confirmer en version consolidée) ? Si la situation bascule vers un acte
   réservé OPJ (art. 16 CPP), afficher le **STOP** avant toute chose et
   réorienter vers `assets/rapport-mise-a-disposition.md` — ce générateur
   ne produit **pas** de PV dans ce cas.
2. **Choix de l'écrit confirmé** (`ecrits-professionnels.md` §5.1) :
   constatation **directe** d'une **contravention**, dans le champ de
   compétence matérielle de l'agent. En cas de doute sur la compétence de
   constatation, renvoyer à `references/reglementation-appliquee.md` (et,
   pour les contraventions routières, à l'art. L. 130-4 du code de la
   route — vérifié sur Légifrance le 2026-06-30, identifiant
   LEGIARTI000045072417, périmètre exact par catégorie d'agent à confirmer
   en version consolidée) **avant** de poursuivre.
3. Si une appréhension a également eu lieu (art. 73 CPP) : ce PV se cumule
   avec un `assets/rapport-mise-a-disposition.md` distinct — ne pas
   fusionner les deux écrits (`ecrits-professionnels.md` §5.1, point 1).

---

## 1. Séquence de questions — une à une, jamais en bloc

**Règle de conduite** (`SKILL.md` §6, `ecrits-professionnels.md` §6.2) :
poser **un champ à la fois**, attendre la réponse, **confirmer** la valeur
reçue avant de passer au champ suivant. Ne jamais enchaîner plusieurs
questions dans le même tour. Si une réponse manque ou reste vague,
**relancer une fois** sur ce champ précis, puis, si elle reste indisponible,
basculer ce champ en `[INCOMPLET]` (§3) et continuer la séquence sur les
champs suivants plutôt que de bloquer tout l'entretien.

L'ordre ci-dessous suit la trame **qui / quand / où / pourquoi /
qualification / témoins / suites** imposée par `SKILL.md` §6 et
`ecrits-professionnels.md` §5.3.

### Étape 1 — Identité et qualité du rédacteur (« qui » constate)
- Q1.1 : « Quel est votre nom, prénom et qualité (agent de police
  municipale, chef de service de police municipale…) ? »
- Q1.2 : « Quel est votre numéro d'agrément préfectoral / d'assermentation,
  si exigé pour cette catégorie de contravention (à vérifier selon le texte
  applicable) ? »
- Q1.3 : « Dans quelle commune et au titre de quel service exercez-vous ? »

### Étape 2 — Date et heure de la constatation (« quand »)
- Q2.1 : « À quelle date avez-vous constaté les faits ? »
- Q2.2 : « À quelle heure précise (heure de constatation, pas une
  estimation) ? »
- Si l'infraction dépend d'un **appareil de contrôle homologué** (radar,
  cinémomètre, horodateur) : Q2.3 : « L'heure provient-elle directement de
  l'appareil, ou d'une observation distincte de l'agent ? Préciser le type
  d'appareil et, si connu, sa référence d'homologation. »

### Étape 3 — Lieu précis de l'infraction (« où »)
- Q3.1 : « Quelle est l'adresse ou la localisation exacte des faits (voie,
  numéro ou portion de voie, point kilométrique, commune) ? »
- **Rappel impératif** (`ecrits-professionnels.md` §5.2) : une localisation
  imprécise fait perdre au PV sa force probante renforcée (art. 537 CPP).
  Si la réponse reste vague (« dans le centre-ville », « vers la place »),
  **relancer explicitement** pour obtenir une localisation exploitable
  avant de continuer.

### Étape 4 — Faits matériellement constatés (« pourquoi » / quoi)
- Q4.1 : « Que avez-vous personnellement constaté, en décrivant uniquement
  les éléments matériels observés (pas d'interprétation, pas de
  supposition) ? »
- Q4.2 : « Avez-vous constaté ces faits par observation directe, ou
  via un appareil de contrôle ? Si appareil, le lien avec Q2.3 est-il
  cohérent ? »
- **Garde-fou rédactionnel** : si la réponse contient des éléments qui ne
  relèvent pas de l'observation directe de l'agent (rapporté par un tiers,
  déduction), les signaler et les isoler explicitement — la force probante
  de l'art. 537 CPP ne couvre que la matérialité constatée personnellement
  (`ecrits-professionnels.md` §5.2).

### Étape 5 — Qualification retenue
- Q5.1 : « Quel texte d'incrimination souhaitez-vous viser (code, article) ? »
- **Ce générateur ne tranche jamais la qualification lui-même** — renvoi
  obligatoire :
  - contenu de l'infraction par domaine → `references/reglementation-appliquee.md` ;
  - pouvoir de constatation mobilisé (art. 21 CPP et texte spécial) →
    `references/penal-procedure.md`.
  Si la qualification proposée par l'utilisateur n'a pas été confirmée dans
  la session contre une source officielle, la marquer `⚠️ non vérifié —
  qualification à confirmer en version consolidée avant transmission`
  plutôt que de l'affirmer comme acquise.
- Q5.2 (le cas échéant) : « Cette contravention est-elle prévue par un
  texte qui attribue explicitement aux agents de police municipale le
  pouvoir de la constater par procès-verbal (ex. art. L. 130-4 du code de
  la route pour le domaine routier) ? » — si la réponse est négative ou
  incertaine, signaler que la force probante renforcée de l'art. 537 CPP
  n'est pas acquise (`ecrits-professionnels.md` §5.2) et que l'écrit
  pertinent pourrait être un rapport d'information.

### Étape 6 — Personne(s) concernée(s) et témoins
- Q6.1 : « L'identité du contrevenant est-elle connue ? Si oui, sur quel
  fondement (pièce d'identité présentée, immatriculation, déclaration) ? »
  — ne **jamais** inscrire de donnée nominative réelle dans un brouillon de
  travail ; utiliser `[NOM Prénom]`, `[date de naissance]`, `[adresse]` en
  espace réservé.
- Q6.2 : « Y a-t-il eu des témoins ? Si oui, combien et selon quelle
  qualité (autre agent, tiers présent) ? » — mêmes réserves nominatives.
- Q6.3 : « Le contrevenant a-t-il formulé des observations au moment de la
  constatation ? » — rappel : leur recueil est une **faculté**, pas une
  obligation, dans le cadre de l'art. 21 CPP (`ecrits-professionnels.md`
  §5.3).

### Étape 7 — Suites données
- Q7.1 : « Une notification ou un avis a-t-il été remis au contrevenant
  (PV papier remis sur place, avis de contravention différé, verbalisation
  électronique) ? Selon quelle procédure locale ? »
- Q7.2 : « Y a-t-il eu appréhension de la personne (art. 73 CPP) en plus de
  la constatation ? » — si oui, ne pas documenter la mesure de contrainte
  dans ce PV : orienter vers `assets/rapport-mise-a-disposition.md` en
  écrit distinct et complémentaire (`ecrits-professionnels.md` §5.1).
- Q7.3 : « Quel circuit de transmission est applicable localement
  (officier du ministère public via verbalisation électronique, transmission
  papier au tribunal de police, autre circuit propre à la collectivité) ? »
  — si la donnée manque, **ne pas la deviner** : la marquer `[INCOMPLET —
  préciser : circuit de transmission OMP]` et noter qu'aucun délai chiffré
  n'est avancé de mémoire (`ecrits-professionnels.md` §6, point 5).

---

## 2. Mentions obligatoires — grille de vérification avant assemblage

Avant d'assembler le document final, vérifier que chacune des mentions
suivantes (`ecrits-professionnels.md` §5.3) est renseignée ou explicitement
marquée `[INCOMPLET]` :

**Socle commun :**
- [ ] Identité et qualité du rédacteur (+ n° d'agrément si exigé)
- [ ] Date et heure précises de la constatation
- [ ] Lieu précis (exigence renforcée — §1 Étape 3)
- [ ] Faits matériellement constatés, sans interprétation
- [ ] Qualification retenue avec texte d'incrimination précis
- [ ] Identité du mis en cause si connue / témoins le cas échéant
- [ ] Observations recueillies du contrevenant, le cas échéant
- [ ] Suites données et destinataire(s)

**Propres au PV de contravention :**
- [ ] Texte exact de l'incrimination (visa précis, pas générique)
- [ ] Référence à l'appareil de contrôle homologué, si la contravention en
      dépend (modalités de preuve spécifiques à vérifier selon le texte)
- [ ] Mention de la notification/avis au contrevenant selon la procédure
      applicable (circuit à vérifier localement)
- [ ] Confirmation explicite que le texte d'incrimination attribue le
      pouvoir de constatation par PV à l'agent PM (sinon : force probante
      renforcée non acquise, §5.2 `ecrits-professionnels.md`)

---

## 3. Règle `[INCOMPLET]` — application stricte

Conformément à `SKILL.md` §6 et `ecrits-professionnels.md` §5.5 :
**interdiction absolue d'halluciner une donnée manquante** (date, lieu,
identité, texte d'incrimination, heure, circuit de transmission).

Si une information nécessaire n'a pas été fournie à l'issue de la séquence
de questions (§1) :
1. Produire le brouillon avec les champs disponibles.
2. Marquer chaque champ manquant par
   `[INCOMPLET — préciser : <nom du champ>]` directement dans le corps du
   document, à l'endroit où l'information devrait figurer.
3. Lister ces champs en fin de document, section **« Champs manquants à
   compléter »**.
4. Demander explicitement ces données à l'utilisateur avant de considérer
   le PV comme finalisé.
5. **Ne jamais transmettre, viser, ni présenter comme définitif** un PV
   portant une mention `[INCOMPLET]` non résolue.

---

## 4. Valeur probante — rappel à restituer avec le PV produit

Toujours accompagner le PV produit du rappel suivant
(`ecrits-professionnels.md` §5.2) :

> **Art. 537 du CPP** *(contenu confirmé sur Légifrance le 2026-06-30,
> identifiant LEGIARTI000006576892 — à reconfirmer en version consolidée à
> la date d'usage)* : les contraventions sont prouvées soit par
> procès-verbaux ou rapports, soit par témoins à défaut. Le présent PV, sous
> réserve qu'il émane d'un agent auquel le texte d'incrimination attribue le
> pouvoir de constater par procès-verbal, **fait foi jusqu'à preuve
> contraire**, laquelle ne peut être rapportée que par écrit ou par témoins.
> Cette force probante renforcée porte uniquement sur la **matérialité des
> faits constatés personnellement** par l'agent, et suppose une
> **localisation précise** (exigence jurisprudentielle constante sur l'art.
> 537 CPP, *à vérifier au cas par cas via `recherche-juridique` avant
> citation en acte*). Un PV imprécis retombe au régime de preuve ordinaire.

---

## 5. Gabarit d'assemblage

> Champs entre `[ ]`. Aucune donnée nominative réelle dans ce gabarit.
> Tout numéro d'article porte sa réserve tant qu'il n'a pas été vérifié
> dans la session en cours.

```
[COLLECTIVITÉ — en-tête / cachet du service de police municipale]

PROCÈS-VERBAL DE CONTRAVENTION N° [numéro]

Je soussigné(e), [NOM Prénom], [qualité : agent / chef de service de police
municipale], agréé(e) et assermenté(e) sous le n° [n° d'agrément —
[INCOMPLET] si non fourni], en fonction au service de police municipale de
la commune de [commune],

CERTIFIE avoir personnellement constaté, le [date] à [heure précise], à
[lieu exact — voie, numéro ou portion de voie, commune], les faits
suivants :

[description des faits matériellement constatés, sans interprétation ni
supposition — Étape 4]

Ces faits sont constitutifs de la contravention prévue et réprimée par
[texte d'incrimination précis — article exact, code concerné — visa
⚠️ à confirmer en version consolidée si non vérifié dans la session],
texte qui attribue aux agents de police municipale le pouvoir de
constatation par procès-verbal au titre de [renvoi : art. L. 130-4 du code
de la route et art. 21 CPP pour le domaine routier — vérifié sur Légifrance
le 2026-06-30, identifiant LEGIARTI000045072417 ; ou autre texte spécial
applicable — à confirmer selon le domaine].

[Le cas échéant : élément constaté au moyen de l'appareil de contrôle
homologué [type d'appareil], référence d'homologation [référence —
[INCOMPLET] si non fournie].]

Mis en cause : [identité si connue : [NOM Prénom], [date de naissance],
[adresse] — ou : « non identifié »].

Témoins : [identité(s) et qualité(s) — ou : « néant »].

Observations recueillies du contrevenant : [contenu, si recueillies — ou :
« aucune observation recueillie »].

Notification : [modalités — PV remis sur place / avis différé /
verbalisation électronique — circuit local [INCOMPLET] si non précisé].

[Le cas échéant, en écrit distinct : une appréhension a été réalisée au
titre de l'art. 73 CPP — voir rapport de mise à disposition n° [référence],
non détaillée dans le présent PV.]

Le présent procès-verbal est transmis à [officier du ministère public /
circuit de verbalisation électronique / tribunal de police compétent —
[INCOMPLET — préciser : circuit de transmission OMP] si non précisé],
conformément à la procédure applicable localement.

Fait à [lieu], le [date].
[Signature de l'agent verbalisateur]
```

---

## 6. Transmission — officier du ministère public (OMP)

- Le PV de contravention est transmis selon le circuit applicable à la
  contravention concernée : **verbalisation électronique** (flux dédié vers
  l'OMP / le centre de traitement compétent) ou **circuit papier** vers le
  **tribunal de police** / l'**officier du ministère public**
  territorialement compétent — modalités et délais exacts **à confirmer en
  version consolidée et selon l'organisation locale**
  (`ecrits-professionnels.md` §6, point 5) ; aucun délai chiffré n'est
  avancé de mémoire dans ce générateur.
- Si une appréhension a eu lieu en parallèle (art. 73 CPP), la transmission
  du PV reste **distincte** du circuit de mise à disposition de l'OPJ pour
  le rapport de mise à disposition — ne pas confondre les deux flux
  (`ecrits-professionnels.md` §5.1).
- **Archivage** : conserver une trace de la version transmise (date, mode
  d'envoi, accusé de réception le cas échéant), notamment en vue d'une
  éventuelle contestation ultérieure mettant en jeu la valeur probante de
  l'art. 537 CPP (`ecrits-professionnels.md` §6, point 6).
- Avant transmission, vérifier que le PV ne porte **aucune mention
  `[INCOMPLET]`** non résolue (§3) — un PV incomplet ne doit pas être
  présenté comme définitif ni transmis en l'état.

---

## 7. Articulation avec le garde-fou APJA et le contrôle de légalité

- Le **PV de contravention n'est pas un acte administratif faisant grief**
  au sens de `references/controle-legalite.md` (ce n'est pas une décision
  de l'autorité territoriale) : il ne requiert donc **ni motivation CRPA,
  ni voies et délais de recours administratifs, ni transmission au contrôle
  de légalité** au sens de l'art. L. 2131-2 CGCT. Ne pas confondre avec
  l'**arrêté** (`assets/arrete-modele.md`), qui lui reste soumis à
  `controle-legalite.md` avant toute production.
- Si, en cours de séquence de questions, il apparaît que les faits
  dépassent le périmètre de l'art. 21 CPP (acte réservé à l'OPJ, art. 16
  CPP), interrompre l'assemblage du PV, afficher le **STOP**
  (`SKILL.md` §5.2) en premier livrable, et limiter la suite à l'action
  APJA conforme : constatation, préservation des traces, compte rendu au
  maire et à l'OPJ (`penal-procedure.md` §4.2, §4.5).

---

## 8. Checklist finale avant restitution du PV

1. Garde-fou APJA testé, situation dans le périmètre art. 21 CPP — sinon
   STOP affiché en premier (§7).
2. Choix de l'écrit confirmé : constatation directe d'une contravention
   dans la compétence matérielle de l'agent (§0).
3. Séquence de questions déroulée **une à une**, confirmation obtenue à
   chaque étape (§1).
4. Toutes les mentions obligatoires de §2 renseignées ou explicitement
   `[INCOMPLET]`.
5. Qualification retenue **renvoyée** à `reglementation-appliquee.md` /
   `penal-procedure.md`, jamais tranchée ici ; mention `⚠️ non vérifié` si
   non confirmée en session.
6. Localisation suffisamment précise pour préserver la force probante de
   l'art. 537 CPP (§4) — sinon signalé comme risque de perte de force
   probante renforcée.
7. Aucune donnée nominative réelle insérée dans un gabarit ou un brouillon
   de travail — uniquement des espaces réservés.
8. Section **« Champs manquants à compléter »** présente si au moins un
   `[INCOMPLET]` subsiste, et demande explicite formulée à l'utilisateur.
9. Circuit de transmission OMP identifié ou marqué `[INCOMPLET]` — pas de
   délai chiffré inventé.
10. Rappel de la valeur probante (§4) joint au PV produit.
11. Si appréhension associée (art. 73 CPP) : signalée comme écrit distinct
    (`assets/rapport-mise-a-disposition.md`), non fusionnée dans ce PV.
12. PV non transmis, non visé comme définitif tant qu'un `[INCOMPLET]`
    subsiste (§3, §6).

[risque : élevé sur la valeur probante (art. 537 CPP) et la compétence de
constatation, le PV n'étant cependant pas un acte faisant grief au sens de
`controle-legalite.md` / confiance : stable sur le principe de l'art. 537
CPP et de l'art. L. 130-4 du code de la route (vérifiés sur Légifrance le
2026-06-30), à confirmer en version consolidée pour le détail des
compétences par catégorie d'agent, la qualification retenue au cas
d'espèce, et le circuit local de transmission à l'OMP]
