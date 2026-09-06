# Générateur interactif — Rapport de mise à disposition (v0.1.0)

> Couche 4 (générateur d'écrit), piloté par `references/ecrits-professionnels.md`
> §4 et §5 (branche de rattachement — lire avant tout usage), et par
> `references/penal-procedure.md` §4.3 à §4.5 (art. 53/73 et 78-6 CPP,
> garde-fou APJA — lire avant tout usage). Structure de dialogue alignée sur
> `SKILL.md` §6. Gabarit de mise en forme inspiré de la discipline de
> `Drh-fpt/assets/decision-modele.md` (champs entre `[ ]`, aucune donnée
> nominative en clair dans le canevas, réserves « à confirmer en version
> consolidée » sur tout visa).
>
> **Ce fichier ne tranche jamais la qualification pénale** (renvoi
> `references/penal-procedure.md` / `references/reglementation-appliquee.md`)
> et **ne formalise jamais un acte réservé à l'OPJ** (audition, garde à vue,
> perquisition, réquisition judiciaire). Il documente strictement une mesure
> ponctuelle fondée soit sur l'**appréhension** des art. 53/73 CPP, soit sur le
> **relevé d'identité** et l'ordre de l'OPJ prévus à l'art. 78-6 CPP.

---

## 0. Quand utiliser ce générateur

Le **rapport de mise à disposition** trace l'une des deux routes suivantes :

- **Route A — art. 53 + 73 CPP** : appréhension de l'auteur d'un crime flagrant
  ou d'un délit flagrant puni d'emprisonnement, puis conduite devant l'OPJ ;
- **Route B — art. 78-6 CPP** : relevé d'identité entrant dans le champ légal,
  refus ou impossibilité de justification, information de l'OPJ, puis
  présentation ou rétention selon son ordre.

Ne jamais fusionner ces fondements ni utiliser ce rapport lorsqu'aucune route
n'est caractérisée.

**Avant d'ouvrir ce générateur**, dérouler le test de
`references/ecrits-professionnels.md` §5.1 et `references/penal-procedure.md`
§4.3 :

1. **Quelle route fonde la mesure : art. 53 + 73, ou art. 78-6 CPP ?**
   Aucune → ce n'est **pas** le bon écrit. Réorienter vers
   `references/templates/rapport-information.md` (simple compte rendu, sans appréhension)
   ou `references/templates/pv-contravention.md` (constatation d'une contravention relevant
   de la compétence de verbalisation de l'agent), selon la logique de
   `references/ecrits-professionnels.md` §5.1.
2. **Les conditions propres à la route sont-elles établies ?**
   - Route A : crime flagrant ou délit flagrant puni d'emprisonnement.
   - Route B : contravention verbalisable, relevé d'identité, refus ou
     impossibilité de justification, information immédiate de l'OPJ et ordre
     explicite pour la présentation ou la rétention au-delà de sa décision.
   En cas de doute, marquer `[INCOMPLET]` et ne pas présenter la mesure comme
   régulière.
3. **Rappel du garde-fou APJA (`SKILL.md` §5.2,
   `references/penal-procedure.md` §4.4-4.5)** : ce générateur **ne sert qu'à
   documenter la mesure licite et la remise à l'OPJ**. Si, à un moment
   quelconque du recueil, il apparaît qu'un acte réservé à l'OPJ a été
   pratiqué ou s'apprête à l'être par l'agent PM lui-même (audition formelle,
   fouille hors cadre de sécurité, garde à vue, perquisition, réquisition
   judiciaire), afficher **immédiatement** le bloc **STOP** ci-dessous, avant
   tout autre contenu, et limiter la suite à l'action APJA conforme.

```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

**Rappel structurant** (`references/ecrits-professionnels.md` §5.4) : le STOP
ne rend pas ce rapport automatiquement mobilisable. Après le compte rendu à
l'OPJ, qualifier séparément la route A ou B. Si elle est établie, ce
générateur documente uniquement la mesure conforme et sa chronologie, jamais
l'acte réservé. Si aucune route n'est établie, ne retenir personne et produire
seulement le rapport d'information ou le PV adapté.

Si aucun blocage n'apparaît **et qu'une route A ou B est établie**, le rapport
de mise à disposition est le bon écrit. Poursuivre au §1.

---

## 1. Séquence interactive obligatoire

**Principe directeur** (`SKILL.md` §6, `ecrits-professionnels.md` §6.2) : les
questions sont posées **une à une**, jamais en bloc. Confirmer chaque réponse
avant de passer au champ suivant. Ne jamais pré-remplir un champ non fourni :
appliquer la règle `[INCOMPLET]` (§4).

Ordre imposé des questions :

### Étape 1 — Identification du rédacteur (qui rapporte)
- Nom, qualité (agent PM / chef de poste / DPM), n° d'agrément si exigé par
  le texte applicable (à vérifier).
> *Question posée* : « Qui rédige ce rapport ? Précisez nom, grade/qualité,
> et n° d'agrément si applicable. »

### Étape 2 — Fondement et date des faits
- Route A : date et heure du crime ou délit flagrant.
- Route B : contravention verbalisée, date et heure du relevé d'identité.
> *Question posée* : « La mesure relève-t-elle des art. 53/73 ou de l'art.
> 78-6 CPP ? Quels faits datés établissent les conditions de cette route ? »

### Étape 3 — Lieu
- Localisation précise du fait et, si différent, lieu du relevé d'identité ou
  de l'appréhension.
> *Question posée* : « Où le fait s'est-il produit, et où la mesure a-t-elle
> débuté si le lieu est différent ? »

### Étape 4 — Faits caractérisant la route
- Route A : éléments personnellement constatés caractérisant la flagrance.
- Route B : contravention verbalisable, relevé d'identité, refus ou
  impossibilité de justification, heure du compte rendu à l'OPJ et teneur de
  sa décision.
> *Question posée* : « Quels faits établissent chacune des conditions du
> fondement retenu, sans interprétation ni supposition ? »

### Étape 5 — Qualification et base légale
- Le rapport de mise à disposition **n'a pas vocation à trancher** la
  qualification pénale (renvoi `references/penal-procedure.md` et
  `references/reglementation-appliquee.md` pour le fond). Elle doit être
  présentée comme une **hypothèse**, utile pour motiver l'appréhension, jamais
  comme acquise.
> *Question posée* : « Quelle qualification est envisagée et quel fondement
> exact autorise la mesure : art. 53 + 73 ou art. 78-6 CPP ? »

### Étape 6 — Heure exacte du début de la mesure
- Route A : heure de l'appréhension.
- Route B : heure du refus ou de l'impossibilité, heure de l'information de
  l'OPJ et heure de son ordre éventuel.
> *Question posée* : « À quelles heures exactes la mesure a-t-elle commencé,
> l'OPJ a-t-il été informé et a-t-il donné sa décision ? »

### Étape 7 — Description de la contrainte exercée
- Description strictement limitée à ce que permet le fondement retenu.
  Pour l'art. 78-6, distinguer le temps nécessaire à l'information et à la
  décision de l'OPJ de la présentation ou rétention ordonnée. **Ne jamais**
  consigner de questions-réponses
  circonstanciées, de fouille hors cadre de sécurité, ni tout élément pouvant
  s'apparenter à une audition ou à un acte d'enquête — cela relève
  exclusivement de l'OPJ (`references/penal-procedure.md` §4.3-4.4).
> *Question posée* : « Quelle contrainte avez-vous exercée sur la personne,
> et seulement celle-là (ex. interpellation, maintien, escorte) ? Confirmez
> qu'aucune audition ni fouille hors cadre de sécurité n'a été pratiquée. »

### Étape 8 — Personne concernée
- Identité si connue (jamais de donnée nominative en clair dans le canevas —
  voir §3), à défaut éléments de signalement objectifs.
> *Question posée* : « La personne concernée est-elle identifiée ? Si oui,
> précisez son identité (restera anonymisée dans le canevas tant qu'elle
> n'est pas confirmée pour la version consolidée). »

### Étape 9 — Témoins
- Présence de témoins de la mesure ou des faits, identifiés ou non.
> *Question posée* : « Y a-t-il des témoins de la mesure ou des faits ?
> Si oui, sont-ils identifiés ? »

### Étape 10 — Issue de la mesure et heure exacte
- **Route A** : heure précise à laquelle la personne a été conduite devant ou
  remise à l'OPJ.
- **Route B** : heure et contenu de la décision de l'OPJ ; selon son ordre,
  heure de la présentation, du début et de la fin de la rétention, ou heure à
  laquelle la personne a été laissée libre de partir.
- Si l'issue n'est pas encore connue au moment de la rédaction, le signaler
  explicitement : le document ne peut pas être considéré comme finalisé.
> *Question posée* : « Quelle décision l'OPJ a-t-il prise, à quelle heure, et
> quelle a été l'issue exacte de la mesure ? »

### Étape 11 — Identité ou qualité de l'OPJ destinataire
- Identité ou, à défaut, qualité/service de l'OPJ destinataire (police
  nationale ou gendarmerie territorialement compétente), et lieu de remise
  (commissariat, brigade).
> *Question posée* : « À quel OPJ (nom et/ou service) et à quel lieu la
> personne a-t-elle été remise ? »

### Étape 12 — Suites données et destinataires du présent rapport
- Suites déjà engagées (compte rendu oral immédiat à l'OPJ, information du
  maire) et destinataire(s) du présent écrit : maire **et** OPJ
  territorialement compétent — double transmission à distinguer
  explicitement (`references/penal-procedure.md` §4.2).
> *Question posée* : « Le compte rendu oral immédiat a-t-il déjà été fait à
> l'OPJ et au maire ? À qui ce rapport écrit doit-il être transmis (maire,
> OPJ, les deux) ? »

**À l'issue de l'étape 12** : si toutes les réponses nécessaires ont été
recueillies, passer à l'assemblage (§2). Sinon, appliquer la règle
`[INCOMPLET]` (§4).

---

## 2. Gabarit d'assemblage

> Champs à compléter entre `[ ]`. **Aucune donnée nominative** ne doit
> figurer en clair dans ce canevas tant qu'elle n'a pas été expressément
> fournie et confirmée par l'utilisateur pour la version consolidée finale ;
> dans le canevas de travail, préférer un identifiant neutre (« la personne
> concernée », « le témoin 1 ») si la donnée doit rester anonymisée pour
> l'échange avec l'assistant.
>
> ⚠️ **Avant transmission** : vérifier en version consolidée tout texte
> d'incrimination évoqué et le régime exact retenu (art. 53/73 ou 78-6 CPP —
> renvoi `references/penal-procedure.md` §4.3), et confirmer le
> circuit local de transmission (organisation propre à la collectivité,
> convention de coordination — `references/continuum-partenariats.md`).

```
[COLLECTIVITÉ — en-tête / service de police municipale]

RAPPORT DE MISE À DISPOSITION N° [numéro] / [année]
(fondement : [art. 53 + 73 / art. 78-6 du Code de procédure pénale])

Rédigé par : [nom, qualité, n° d'agrément si exigé]
Date et heure de rédaction : [date] à [heure]

I. FAITS À L'ORIGINE DE LA MESURE
Date et heure des faits : [date] à [heure] — étape 2
Lieu des faits : [adresse ou localisation précise] — étape 3
[Description strictement factuelle des éléments personnellement constatés
caractérisant chacune des conditions du fondement retenu — étape 4.
Pas d'interprétation, pas de supposition.]

II. QUALIFICATION ET FONDEMENT
[Texte d'incrimination évoqué — étape 5. Mention obligatoire : « qualification
non tranchée par le présent rapport, à vérifier — renvoi
reglementation-appliquee.md / penal-procedure.md ».]
Fondement de la mesure : [Route A — art. 53 + 73 / Route B — art. 78-6]
Conditions vérifiées : [liste factuelle / `[INCOMPLET]`]

III. MESURE
Lieu de la mesure : [adresse ou « identique au lieu des faits »] — étape 3
Heure exacte du début : [heure] — étape 6
Personne concernée : [identité ou « non identifiée » / éléments de
signalement objectifs] — étape 8

[ROUTE A — ART. 53 + 73]
Heure de l'appréhension : [heure]

[ROUTE B — ART. 78-6]
Contravention verbalisée : [nature et texte habilitant]
Refus ou impossibilité de justifier l'identité : [faits]
Information de l'OPJ : [date/heure]
Décision et ordre de l'OPJ : [teneur, date/heure, identité/service]

Description de la contrainte exercée, strictement limitée à ce qui a été
autorisé par le fondement retenu : [description — étape 7]
Il est précisé qu'aucune audition formelle, fouille hors cadre de sécurité,
ni mesure assimilable à un acte réservé à l'officier de police judiciaire
n'a été pratiquée par le rédacteur.

IV. TÉMOINS
[Identité(s) ou « néant » ; précisions le cas échéant — étape 9]

V. ISSUE DE LA MESURE ET DÉCISION DE L'OFFICIER DE POLICE JUDICIAIRE
Décision de l'OPJ, si route 78-6 : [contenu et heure / sans objet] — étape 10
Issue exacte : [conduite ou remise devant l'OPJ / présentation / rétention
ordonnée / personne laissée libre de partir / issue non encore connue —
voir section CHAMPS MANQUANTS] — étape 10
Heure(s) correspondante(s) : [heure(s)] — étape 10
OPJ destinataire (identité et/ou service) : [nom / qualité / service —
étape 11]
Lieu de remise : [commissariat / brigade — étape 11]

VI. COMPTE RENDU ET DESTINATAIRES
Compte rendu oral immédiat effectué : [oui / non, précisions] — étape 12
Destinataire(s) du présent rapport écrit : [maire / OPJ territorialement
compétent / les deux — étape 12]. Si double destinataire : la transmission
au maire et la transmission à l'OPJ sont deux démarches distinctes
(`references/penal-procedure.md` §4.2) ; le présent écrit formalise la
trace du compte rendu oral immédiat déjà effectué, le cas échéant, sur le
terrain.

Fait à [lieu], le [date].
[Signature du rédacteur]
```

---

## 3. Discipline de rédaction (rappel, non négociable)

- **Champs entre `[ ]`** tant qu'ils ne sont pas confirmés par l'utilisateur.
- **Aucune donnée nominative** générée ou supposée par l'assistant : toute
  identité doit être fournie explicitement par l'utilisateur ; en son
  absence, laisser `[INCOMPLET — préciser : identité de …]`.
- **Objectivité stricte** sur les faits à l'origine de la mesure :
  description des éléments personnellement constatés, pas de jugement de
  valeur ni de supposition sur les intentions.
- **Toute référence de texte** (incrimination, régime de flagrance) porte la
  réserve « à confirmer en version consolidée » sauf identifiant déjà
  vérifié dans la session courante (règle de provenance, `SKILL.md` §5.3).
- **Pas de qualification pénale tranchée** dans ce document : renvoi
  systématique aux branches compétentes (§0, §1 étape 5).
- **Chronologie distincte et obligatoire** : début de la mesure, information
  et décision de l'OPJ pour la route B, puis issue horodatée.
  Ne jamais fusionner ni approximer ces heures.
- **Contrainte strictement limitée** : la section III ne décrit que ce qui a
  été autorisé par la route A ou B et nécessaire à la conduite ou présentation
  devant l'OPJ. **Aucune
  trace d'audition, de questions-réponses circonstanciées, de fouille hors
  cadre de sécurité, ni de toute autre mesure hors pouvoir APJA** ne
  doit apparaître dans ce rapport — c'est le cœur du **garde-fou APJA**
  appliqué à cet écrit (`references/ecrits-professionnels.md` §5.4, §8 point
  7).
- **L'acte d'enquête reste à l'OPJ** : ce rapport documente la **mesure et la
  remise**, il
  ne préjuge ni ne décrit aucune suite procédurale (garde à vue, audition,
  classement) qui relève de la seule décision de l'OPJ et, le cas échéant, du
  procureur de la République. Ne jamais anticiper ni suggérer cette suite
  dans le corps du rapport.

---

## 4. Règle `[INCOMPLET]` — application stricte

**Interdiction absolue d'halluciner une donnée manquante** (date, heure,
lieu, identité, texte d'incrimination, heure de début de la mesure, décision
de l'OPJ, issue et heure correspondante, identité/qualité de l'OPJ).

Si une information nécessaire à une étape du §1 n'a pas été fournie, et **en
particulier** si l'heure exacte de début de la mesure (étape 6), la décision
de l'OPJ requise pour la route B ou l'heure de l'issue (étape 10) manque :

1. Ne **pas** combler le champ par une supposition, même plausible.
2. Marquer le champ correspondant dans le gabarit `[INCOMPLET — préciser :
   <nom du champ>]`.
3. Poursuivre l'assemblage avec les champs disponibles (un champ manquant ne
   bloque pas la rédaction des autres sections).
4. En fin de document, ajouter la section suivante, systématiquement si au
   moins un champ est marqué `[INCOMPLET]` :

```
---
## CHAMPS MANQUANTS — DOCUMENT NON FINALISABLE EN L'ÉTAT

Les informations suivantes sont requises avant transmission :
- [champ manquant 1 — étape correspondante]
- [champ manquant 2 — étape correspondante]
- [...]

Point de vigilance particulier : le début de la mesure, la décision de l'OPJ
lorsqu'elle est requise et l'issue horodatée sont des mentions structurantes
de cet écrit (`references/ecrits-professionnels.md` §5.3). Leur absence
empêche de documenter la conformité de la route 53/73 ou 78-6
(`references/penal-procedure.md` §4.3).

Merci de fournir ces éléments pour finaliser le rapport. Ce document ne doit
être ni transmis, ni visé, ni présenté comme définitif tant que ces champs
ne sont pas renseignés.
```

5. **Demander explicitement** ces données à l'utilisateur dans la réponse,
   en reprenant la formulation de la question d'étape correspondante (§1).
6. Ne jamais marquer le document comme « final » ou « prêt à transmettre »
   tant qu'une mention `[INCOMPLET]` subsiste — **a fortiori** si la mise à
   disposition elle-même n'a pas encore eu lieu (étape 10) : dans ce cas, le
   document reste un brouillon de compte rendu en cours, jamais un rapport
   clos.

---

## 5. Transmission

- **Destinataires** : maire **et** OPJ territorialement compétent, sans
  exception, conformément à la double transmission de
  `references/penal-procedure.md` §4.2 — ce n'est pas une option laissée au
  choix du rédacteur, à la différence du rapport d'information.
- Le **compte rendu oral immédiat** à l'OPJ intervient sans attendre la
  rédaction : dès l'appréhension pour la route A et dès le refus ou
  l'impossibilité de justifier l'identité pour la route B. L'écrit formalise
  la trace après coup et ne s'y substitue pas.
- **Aucun délai chiffré** n'est donné de mémoire pour la rédaction de ce
  rapport. Route A : conduire devant l'OPJ sans délai indu. Route B : respecter
  strictement la chronologie de l'art. 78-6, notamment l'information et la
  décision de l'OPJ puis son ordre éventuel. L'écrit suit dès que possible,
  sans retarder le compte rendu oral.
- **Archivage** : conserver une trace de la version transmise
  (`references/ecrits-professionnels.md` §6.6), utile en cas de contestation
  ultérieure de la régularité de la mesure ou de reconstitution chronologique
  exacte des faits, de l'information, de la décision de l'OPJ et de l'issue.

---

## 6. Articulation avec le garde-fou APJA (rappel)

Ce générateur est, par construction, **l'écrit de la mesure licite**
(`references/ecrits-professionnels.md` §5.4, `references/penal-procedure.md`
§4.5) : il documente précisément la route A ou B et la remise à l'OPJ. Le
déclenchement du garde-fou ne suffit jamais, à lui seul, à ouvrir ce générateur.

Si, à n'importe quelle étape du recueil (§1), il apparaît que l'agent PM a
pratiqué ou s'apprête à pratiquer un acte hors de ses pouvoirs (audition
formelle, fouille hors cadre de sécurité, garde à vue, perquisition,
réquisition judiciaire —
`references/penal-procedure.md` §4.4), interrompre la séquence de questions
et afficher immédiatement le bloc **STOP** (§0) **avant** de poursuivre quoi
que ce soit d'autre. La suite se limite alors à :
1. l'affichage du STOP en premier ;
2. la qualification de la route A, de la route B, ou de l'absence de fondement ;
3. seulement si une route est établie, la consignation des informations
   relevant de la mesure et de la remise (sections I à III et V du gabarit) ;
4. la **non-rédaction** de toute section qui décrirait un acte réservé —
   préférer `[INCOMPLET — hors champ APJA, acte réservé OPJ, ne pas
   formaliser]` plutôt que de décrire l'acte ;
5. le compte rendu à l'OPJ et au maire, sans attendre la rédaction définitive
   de l'écrit.

**Rappel de cohérence avec `references/ecrits-professionnels.md` §8 point
7** : ne jamais esquisser, dans ce rapport, des éléments relevant d'une
audition formelle (questions-réponses circonstanciées) — c'est le piège le
plus fréquent identifié pour cet écrit.

---

## 7. Double échelle [risque / confiance]

| Point | Risque | Confiance |
|---|---|---|
| Choix de l'écrit (vs rapport d'information / PV) | Moyen | Vérification ponctuelle si situation mixte (§0) |
| Qualification de la route 53/73 ou 78-6 | Critique | Toutes les conditions doivent être vérifiées ; sinon aucune rétention |
| Chronologie de la mesure / décision OPJ / mise à disposition | Élevé | `[INCOMPLET]` obligatoire si absente — mentions structurantes de l'écrit |
| Description de la contrainte exercée (limitée au strict nécessaire) | Critique | Vigilance rédactionnelle constante — bascule vers garde-fou si dépassement |
| Qualification évoquée à titre d'hypothèse | Élevé | À vérifier — jamais tranchée ici |
| Donnée manquante (tout champ) | Élevé | N/A — `[INCOMPLET]` obligatoire |
| Double transmission maire / OPJ | Élevé | Obligatoire, non optionnelle pour cet écrit (à la différence du rapport d'information) |

---

## 8. Checklist avant de considérer le rapport comme finalisé

1. Garde-fou APJA testé en premier et à chaque étape (§0, §6) : aucun acte
   réservé OPJ reconstitué ou décrit comme s'il relevait de l'APJA.
2. Toutes les étapes du §1 parcourues **une à une**, avec confirmation à
   chaque étape.
3. Route 53/73 ou 78-6 explicitement confirmée comme déclencheur de cet écrit
   — sinon, aucune rétention et redirection vers
   `references/templates/rapport-information.md` ou
   `references/templates/pv-contravention.md` selon le cas (§0).
4. **Heure exacte de début**, **information et décision de l'OPJ** lorsque
   requises, et **issue horodatée** renseignées ou marquées `[INCOMPLET]`
   avec demande explicite (§4).
5. **Identité ou qualité de l'OPJ destinataire** renseignée, ou marquée
   `[INCOMPLET]`.
6. **Description de la contrainte exercée** strictement limitée à la route
   établie et, pour la route 78-6, à la décision de l'OPJ : aucune trace
   d'audition, de fouille hors cadre de sécurité, ni d'acte d'enquête.
7. Qualification, si évoquée, présentée comme hypothèse non tranchée, avec
   renvoi aux branches compétentes (`penal-procedure.md`,
   `reglementation-appliquee.md`).
8. Aucune donnée manquante comblée par supposition — règle `[INCOMPLET]`
   (§4) appliquée et champs listés explicitement si nécessaire.
9. **Double transmission maire + OPJ territorialement compétent**
   correctement distinguée et toutes deux mentionnées (`penal-procedure.md`
   §4.2) — non optionnelle pour cet écrit.
10. Aucune donnée nominative exposée inutilement (`SKILL.md` §7 point 11).
11. Mention finale claire : document **prêt à transmettre** ou marqué
    `[INCOMPLET]` avec demande explicite des champs manquants — jamais d'état
    intermédiaire ambigu, et jamais « prêt à transmettre » si la mise à
    disposition elle-même n'a pas encore eu lieu.
