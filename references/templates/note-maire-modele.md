# Générateur interactif — Note au maire (modèle) (v0.1.0)

> Couche 4 (générateur d'écrit), piloté par `references/ecrits-professionnels.md`
> §4 et §10 (branche de rattachement — lire avant tout usage). Structure de
> dialogue alignée sur `SKILL.md` §6. Gabarit de mise en forme inspiré de la
> discipline de `Drh-fpt/assets/decision-modele.md` (champs entre `[ ]`,
> aucune donnée nominative en clair dans le canevas, réserves « à confirmer en
> version consolidée » sur tout visa).
>
> **Nature de l'écrit** : la note au maire est une **note de pilotage / aide
> à la décision** — **pas un acte administratif**. Elle ne produit aucun
> effet de droit par elle-même, ne fait pas grief, et n'est donc **ni motivée
> au sens du CRPA, ni assortie de voies et délais de recours, ni soumise à
> transmission au contrôle de légalité** en tant que telle
> (`references/controle-legalite.md` §9). En revanche, si la note recommande
> une **décision** du maire qui prendra ensuite la forme d'un arrêté ou d'une
> autre décision faisant grief, la **base légale citée dans la note doit être
> rigoureuse** dès ce stade, car elle conditionne la suite : passage
> obligatoire par `references/controle-legalite.md` avant toute production
> de l'acte qui en découlerait (`references/templates/arrete-modele.md`).
>
> **Ce fichier ne tranche jamais seul** la qualification pénale ou
> réglementaire d'un fait (renvoi `references/penal-procedure.md` /
> `references/reglementation-appliquee.md`), ni la légalité d'un projet
> d'acte (renvoi `references/controle-legalite.md`) : il **signale** les
> points de fragilité identifiés par la grille de contrôle, la décision
> finale appartenant au maire.

---

## 0. Quand utiliser ce générateur

La **note au maire** sert à éclairer une décision du maire : elle expose un
**contexte**, une **analyse**, des **options** chiffrées/qualifiées avec
leurs **risques**, et une **recommandation** du DPM (ou du rédacteur
habilité), sans décider à sa place.

**Avant d'ouvrir ce générateur**, vérifier que l'écrit demandé est bien une
note de pilotage et non un autre type de document :

1. **S'agit-il de constater un fait avec valeur probante (contravention) ?**
   Oui → `references/templates/pv-contravention.md`, pas ce générateur.
2. **S'agit-il de rendre compte d'une intervention ou d'une appréhension ?**
   Oui → `references/templates/rapport-information.md` ou
   `references/templates/rapport-mise-a-disposition.md` selon le cas
   (`references/ecrits-professionnels.md` §5.1), pas ce générateur.
3. **S'agit-il de rédiger directement l'acte décisionnel (arrêté) ?**
   Oui → `references/templates/arrete-modele.md`, après passage par
   `references/controle-legalite.md`. La note au maire peut **précéder**
   cette rédaction (note d'aide à la décision en amont de l'arrêté), mais
   ne s'y substitue jamais.
4. **Le fait sous-jacent comporte-t-il une demande d'acte hors pouvoir APJA
   (`SKILL.md` §5.2 ; l'art. 16 CPP définit notamment la qualité d'OPJ) ?**
   Oui → afficher le **STOP** (bloc ci-dessous) **avant tout autre
   contenu**. La note au maire, si elle est néanmoins produite, se limite
   alors à rendre compte de l'action APJA conforme et, si un fondement a été
   qualifié, de la présentation réalisée au titre des art. 53/73 ou 78-6 —
   jamais à présenter des options sur un acte réservé à l'OPJ.

```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

Si aucun de ces quatre cas ne redirige ailleurs : la **note au maire** est
le bon écrit. Poursuivre au §1.

---

## 1. Séquence interactive obligatoire

**Principe directeur** (`SKILL.md` §6, `ecrits-professionnels.md` §6.2) : les
questions sont posées **une à une**, jamais en bloc. Confirmer chaque
réponse avant de passer au champ suivant. Ne jamais pré-remplir un champ non
fourni : appliquer la règle `[INCOMPLET]` (§4).

Ordre imposé des questions :

### Étape 1 — Identification du rédacteur et destinataire (qui)
- Nom, qualité du rédacteur (DPM / chef de service / agent habilité) ;
  confirmation que le destinataire est bien le maire (ou, le cas échéant,
  un adjoint délégué — préciser la délégation).
> *Question posée* : « Qui rédige cette note, et à qui est-elle adressée
> (le maire, ou un adjoint délégué — dans ce cas, sur quelle délégation) ? »

### Étape 2 — Date de la note et échéance de la décision (quand)
- Date de rédaction de la note ; échéance à laquelle une décision est
  attendue, si elle existe (urgence, échéance réglementaire, événement
  programmé).
> *Question posée* : « À quelle date rédigez-vous cette note, et existe-t-il
> une échéance à laquelle une décision est attendue ? »

### Étape 3 — Périmètre et localisation (où)
- Périmètre concerné par la question traitée (ensemble de la commune,
  quartier, voie, établissement, événement précis — selon l'objet).
> *Question posée* : « Quel est le périmètre concerné (toute la commune, un
> secteur précis, un établissement, un événement) ? »

### Étape 4 — Contexte et faits motivant la note (pourquoi)
- Exposé des faits ou de la situation à l'origine de la note, formulé de
  façon factuelle (statistiques, signalements, incidents, évolution
  réglementaire, demande d'un tiers).
> *Question posée* : « Quel est le contexte ou quels sont les faits qui
> motivent cette note (situation observée, signalements, évolution
> réglementaire, demande reçue) ? »

### Étape 5 — Base légale ou réglementaire mobilisée (qualification)
- Texte(s) susceptible(s) de fonder une décision du maire sur ce sujet
  (police générale CGCT, police spéciale identifiée — renvoi
  `references/pouvoirs-police.md` pour le fond ; ce générateur **ne
  tranche pas** lui-même la qualification).
> *Question posée* : « Quelle base légale ou réglementaire envisagez-vous
> pour une éventuelle décision (police générale du maire, police spéciale
> — laquelle) ? Si vous ne savez pas, indiquez-le : ce point sera signalé
> comme à vérifier. »

### Étape 6 — Options envisageables
- Recenser les **options** réalistes ouvertes au maire, y compris l'option
  « ne rien faire » ou « différer », avec pour chacune : description
  succincte, avantages, inconvénients, coût/moyens nécessaires si connus.
> *Question posée* : « Quelles sont les options envisageables (au moins
> deux, y compris l'absence d'action si pertinente) ? Pour chacune, quels
> avantages et inconvénients identifiez-vous ? »

### Étape 7 — Personnes ou tiers concernés / témoins ou avis recueillis
- Tiers dont la situation serait affectée par une décision (administrés,
  professionnels, riverains), et avis déjà recueillis (services, partenaires
  du continuum de sécurité, instances consultatives) — jamais de donnée
  nominative en clair dans le canevas (§3).
> *Question posée* : « Des tiers sont-ils directement concernés par une
> décision sur ce sujet ? Des avis ont-ils déjà été recueillis (services,
> partenaires, instances) ? »

### Étape 8 — Risques par option
- Pour chaque option retenue à l'étape 6, identifier le ou les risques
  (juridique/contentieux, opérationnel, sécuritaire, financier, image) et
  qualifier le couple **[risque / confiance]** (`SKILL.md` §5.1).
> *Question posée* : « Pour chaque option, quels risques identifiez-vous
> (contentieux, opérationnel, sécuritaire, financier, image), et avec quel
> niveau de confiance dans l'analyse ? »

### Étape 9 — Recommandation du rédacteur
- Option recommandée par le DPM/rédacteur, avec justification synthétique ;
  préciser que la décision finale appartient au maire.
> *Question posée* : « Quelle option recommandez-vous, et pourquoi,
> succinctement ? »

### Étape 10 — Suites et calendrier proposé
- Étapes suivantes si la recommandation est suivie (ex. instruction d'un
  projet d'arrêté, consultation complémentaire, communication), et
  calendrier indicatif.
> *Question posée* : « Si la recommandation est suivie, quelles sont les
> prochaines étapes et un calendrier indicatif (ex. projet d'arrêté à
> instruire, consultation à mener, communication à prévoir) ? »

**À l'issue de l'étape 10** : si toutes les réponses nécessaires ont été
recueillies, passer à l'assemblage (§2). Sinon, appliquer la règle
`[INCOMPLET]` (§4).

---

## 2. Gabarit d'assemblage

> Champs à compléter entre `[ ]`. **Aucune donnée nominative** ne doit
> figurer en clair dans ce canevas tant qu'elle n'a pas été expressément
> fournie et confirmée par l'utilisateur pour la version consolidée finale ;
> dans le canevas de travail, préférer un identifiant neutre (« le riverain
> A », « le partenaire B ») si la donnée doit rester anonymisée pour
> l'échange avec l'assistant.
>
> ⚠️ **Avant transmission au maire** : si la note évoque une base légale ou
> réglementaire conditionnant une décision, vérifier en version consolidée
> ce visa (renvoi `references/pouvoirs-police.md` /
> `references/reglementation-appliquee.md`) et signaler tout point de
> fragilité identifié par `references/controle-legalite.md` (§4 de cette
> brique), notamment compétence, base légale précise et proportionnalité —
> même si cette note elle-même n'est pas un acte faisant grief.

```
[COLLECTIVITÉ — en-tête / service de police municipale]

NOTE AU MAIRE N° [numéro] / [année]
[Mention facultative : destinataire précis si adjoint délégué — préciser la
délégation]

Rédigée par : [nom, qualité]
Date : [date]
Objet : [intitulé synthétique de la question traitée]
Échéance de décision : [date ou « sans échéance fixée » — étape 2]

I. CONTEXTE
[Périmètre concerné (étape 3) et faits ou situation motivant la note,
exposés de façon factuelle — étape 4. Citer les éléments objectifs
disponibles (signalements, statistiques, antécédents) sans
interprétation excessive.]

II. ANALYSE
[Base légale ou réglementaire envisageable pour une éventuelle décision
(étape 5), avec la réserve obligatoire : « qualification non tranchée par
la présente note, à vérifier — renvoi pouvoirs-police.md /
reglementation-appliquee.md ». Préciser si la police mobilisée est générale
ou spéciale et signaler tout risque de conflit de compétence
(maire/préfet) identifié.

Avis déjà recueillis et tiers concernés, le cas échéant (étape 7), sans
donnée nominative en clair.]

III. OPTIONS
[Pour chaque option recensée à l'étape 6 :]

Option [n°] — [intitulé]
- Description : [...]
- Avantages : [...]
- Inconvénients : [...]
- Moyens / coût estimé : [si connu, sinon « [INCOMPLET — préciser : coût
  estimé de l'option n° ... ]» ou « non chiffré à ce stade »]
- Risque(s) identifié(s) : [étape 8]
- [risque : Faible / Moyen / Élevé / Critique — confiance : Stable / À
  vérifier / Jurisprudentiel / Abstention] (`SKILL.md` §5.1)

[Répéter pour chaque option, y compris l'option « ne rien faire » ou
« différer » si elle a été envisagée.]

IV. POINTS DE VIGILANCE — CONTRÔLE DE LÉGALITÉ (le cas échéant)
[Si une option recommandée est susceptible de déboucher sur un acte
faisant grief : reprendre ici les points de fragilité identifiés via
references/controle-legalite.md §4 — compétence et délégation, procédure
préalable, base légale précise, proportionnalité, obligation de
motivation et de transmission au contrôle de légalité de l'acte à venir.
Cette note elle-même n'est pas un acte et n'est pas soumise à ces
obligations, mais les anticiper ici sécurise la décision du maire.
Si aucune option n'aboutit à un acte faisant grief : « sans objet à ce
stade ».]

V. RECOMMANDATION
[Option recommandée et justification synthétique — étape 9. Rappel
explicite : « Cette recommandation n'engage pas le maire ; la décision lui
appartient. »]

VI. SUITES ET CALENDRIER PROPOSÉ
[Étapes suivantes si la recommandation est suivie, calendrier indicatif —
étape 10. Si une option implique la rédaction d'un arrêté : rappel que ce
projet d'acte devra être instruit séparément via references/templates/arrete-modele.md,
après passage obligatoire par references/controle-legalite.md.]

Fait à [lieu], le [date].
[Signature du rédacteur]
```

---

## 3. Discipline de rédaction (rappel, non négociable)

- **Champs entre `[ ]`** tant qu'ils ne sont pas confirmés par
  l'utilisateur.
- **Aucune donnée nominative** générée ou supposée par l'assistant : toute
  identité doit être fournie explicitement par l'utilisateur ; en son
  absence, laisser `[INCOMPLET — préciser : identité de …]`.
- **Pas de décision déguisée** : la note **ne décide pas** ; elle
  **recommande**. La formulation doit toujours laisser explicite que la
  décision appartient au maire (étape 9, section V du gabarit).
- **Toute référence de texte** (base légale envisagée pour une décision)
  porte la réserve « à confirmer en version consolidée » sauf identifiant
  déjà vérifié dans la session courante (règle de provenance, `SKILL.md`
  §5.3).
- **Pas de qualification pénale ou réglementaire tranchée** dans ce
  document : renvoi systématique aux branches compétentes (§0, §1 étape 5).
- **Au moins deux options** présentées, y compris l'option de ne pas agir
  ou de différer si elle est pertinente : une note à option unique masque
  l'aide à la décision attendue par le maire.
- **Risque par option** explicitement qualifié (§1 étape 8, couple
  [risque/confiance] `SKILL.md` §5.1), pas seulement pour l'option
  recommandée.

---

## 4. Règle `[INCOMPLET]` — application stricte

**Interdiction absolue d'halluciner une donnée manquante** (contexte, base
légale envisagée, option, risque, recommandation, destinataire).

Si une information nécessaire à une étape du §1 n'a pas été fournie :

1. Ne **pas** combler le champ par une supposition, même plausible.
2. Marquer le champ correspondant dans le gabarit `[INCOMPLET — préciser :
   <nom du champ>]`.
3. Poursuivre l'assemblage avec les champs disponibles (un champ manquant
   ne bloque pas la rédaction des autres sections ; en particulier, des
   options déjà recueillies peuvent être assemblées même si une autre
   reste à préciser).
4. En fin de document, ajouter la section suivante, systématiquement si au
   moins un champ est marqué `[INCOMPLET]` :

```
---
## CHAMPS MANQUANTS — DOCUMENT NON FINALISABLE EN L'ÉTAT

Les informations suivantes sont requises avant transmission au maire :
- [champ manquant 1 — étape correspondante]
- [champ manquant 2 — étape correspondante]
- [...]

Merci de fournir ces éléments pour finaliser la note. Ce document ne doit
être ni transmis, ni présenté comme définitif tant que ces champs ne sont
pas renseignés.
```

5. **Demander explicitement** ces données à l'utilisateur dans la réponse,
   en reprenant la formulation de la question d'étape correspondante (§1).
6. Ne jamais marquer le document comme « final » ou « prêt à transmettre »
   tant qu'une mention `[INCOMPLET]` subsiste.
7. **Cas particulier — base légale incertaine (étape 5)** : si le
   rédacteur ne sait pas quelle base légale envisager, ne **jamais**
   l'inventer ; marquer `[INCOMPLET — préciser : base légale envisagée, ou
   indiquer "à déterminer via pouvoirs-police.md / reglementation-appliquee.md"]`
   et signaler que ce point devra être levé avant toute instruction d'un
   éventuel acte.

---

## 5. Transmission et articulation avec l'acte éventuel

- **Destinataire** : le maire (ou l'adjoint délégué identifié à l'étape 1,
  délégation précisée).
- La note au maire **n'est pas un acte** : elle n'est ni motivée au sens du
  CRPA, ni assortie de voies et délais de recours, ni soumise par
  elle-même à l'obligation de transmission au contrôle de légalité
  (`references/controle-legalite.md` §9). Ne jamais présenter cette note
  comme tenant lieu d'un arrêté ou d'une décision.
- Si la **recommandation retenue** par le maire implique la rédaction d'un
  acte (typiquement un arrêté) : ce projet d'acte doit être instruit
  **séparément** via `references/templates/arrete-modele.md`, **après passage
  obligatoire** par `references/controle-legalite.md` (grille de contrôle
  a priori §4 : compétence et délégation, procédure préalable, base
  légale précise, motivation en fait et en droit si l'acte fait grief,
  proportionnalité, voies et délais de recours, vérification de la
  transmission au contrôle de légalité — CGCT, art. L. 2131-2, à confirmer
  en version consolidée).
- **Archivage** : conserver une trace de la version transmise au maire
  (`references/ecrits-professionnels.md` §6.6), utile pour la traçabilité
  de la décision et en cas de contestation ultérieure de l'acte qui en
  découlerait.

---

## 6. Articulation avec le garde-fou APJA (rappel)

Si, à n'importe quelle étape du recueil (§1), il apparaît que la situation
sous-jacente **dépasse le pouvoir APJA**, interrompre la
séquence de questions et afficher immédiatement le bloc **STOP** (§0)
**avant** de poursuivre quoi que ce soit d'autre. La suite se limite alors
à :
1. l'affichage du STOP en premier ;
2. le rappel que la note au maire, si elle est néanmoins utile, se borne à
   rendre compte de l'action APJA conforme (constatation, préservation,
   compte rendu et, seulement sur fondement qualifié, présentation à l'OPJ) —
   jamais à présenter des « options » sur un acte réservé à l'OPJ ;
3. le renvoi au compte rendu déjà transmis à l'OPJ : rapport de mise à
   disposition uniquement si une route 53/73 ou 78-6 est établie, sinon
   rapport d'information. La note au maire n'ajoute qu'un éclairage de
   pilotage en aval (ex. communication, mesures complémentaires relevant du
   maire).

---

## 7. Double échelle [risque / confiance]

| Point | Risque | Confiance |
|---|---|---|
| Choix de l'écrit (note vs acte vs rapport) | Moyen | Vérification ponctuelle si la situation appelle déjà une décision formalisée |
| Base légale envisagée pour une éventuelle décision (étape 5) | Élevé | À vérifier — jamais tranchée ici, renvoi `pouvoirs-police.md` / `reglementation-appliquee.md` |
| Pertinence et exhaustivité des options présentées | Moyen | Stable sur le principe (au moins deux options), vigilance rédactionnelle constante |
| Qualification du risque par option (étape 8) | Élevé | À vérifier au cas par cas selon l'option |
| Donnée manquante | Élevé | N/A — `[INCOMPLET]` obligatoire |
| Recommandation présentée comme engageant le maire (au lieu de rester une proposition) | Élevé | Stable sur le principe — formulation à corriger systématiquement si ambiguë |
| Option recommandée débouchant sur un acte faisant grief | Critique | Passage obligatoire par `controle-legalite.md` avant toute production de cet acte |

---

## 8. Checklist avant de considérer la note comme finalisée

1. Garde-fou APJA testé en premier (§0, §6) : aucune « option » présentée
   sur un fait réservé à l'OPJ.
2. Toutes les étapes du §1 parcourues **une à une**, avec confirmation à
   chaque étape.
3. Au moins deux options présentées (§3), avec avantages, inconvénients et
   risque qualifié pour chacune (§1 étape 8).
4. Aucune donnée manquante comblée par supposition — règle `[INCOMPLET]`
   (§4) appliquée et champs listés explicitement si nécessaire, y compris
   le cas particulier de la base légale incertaine (§4 point 7).
5. Base légale envisagée présentée comme **hypothèse à vérifier**, jamais
   comme acquise ; renvoi explicite aux branches compétentes (§0, §1
   étape 5).
6. Recommandation clairement distinguée d'une décision : formulation
   rappelant que la décision finale appartient au maire (§1 étape 9,
   section V du gabarit, §3).
7. Si une option aboutit à un acte faisant grief : section IV du gabarit
   renseignée avec les points de fragilité identifiés via
   `references/controle-legalite.md`, et rappel explicite que cette note
   ne se substitue pas à l'instruction séparée de l'acte
   (`references/templates/arrete-modele.md`).
8. Aucune donnée nominative exposée inutilement (`SKILL.md` §7 point 11).
9. Couple **[risque / confiance]** indiqué pour chaque option (§7), pas
   seulement pour l'option recommandée.
10. Mention finale claire : document **prêt à transmettre** ou **marqué
    `[INCOMPLET]`** avec demande explicite des champs manquants — jamais
    d'état intermédiaire ambigu.
