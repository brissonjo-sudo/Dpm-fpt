# Générateur interactif — Rapport de mise à disposition (v0.1.0)

> Couche 4 (générateur d'écrit), piloté par `references/ecrits-professionnels.md`
> §4 et §5 (branche de rattachement — lire avant tout usage), et par
> `references/penal-procedure.md` §4.3 à §4.5 (flagrance, art. 73 CPP,
> garde-fou APJA — lire avant tout usage). Structure de dialogue alignée sur
> `SKILL.md` §6. Gabarit de mise en forme inspiré de la discipline de
> `Drh-fpt/assets/decision-modele.md` (champs entre `[ ]`, aucune donnée
> nominative en clair dans le canevas, réserves « à confirmer en version
> consolidée » sur tout visa).
>
> **Ce fichier ne tranche jamais la qualification pénale** (renvoi
> `references/penal-procedure.md` / `references/reglementation-appliquee.md`)
> et **ne formalise jamais un acte réservé à l'OPJ** (audition, garde à vue,
> perquisition, réquisition judiciaire — art. 16 CPP). Il documente
> strictement une **mesure de contrainte ponctuelle** (l'appréhension, art. 73
> CPP) et sa **remise immédiate** à l'officier de police judiciaire.

---

## 0. Quand utiliser ce générateur

Le **rapport de mise à disposition** est l'écrit qui trace qu'un **APJA a
appréhendé l'auteur d'un crime ou d'un délit flagrant puni d'emprisonnement**
(art. 73 CPP) et l'a **remis à l'officier de police judiciaire** — il ne
documente rien d'autre que cette séquence : appréhension → contrainte
strictement limitée au temps nécessaire → remise à l'OPJ.

**Avant d'ouvrir ce générateur**, dérouler le test de
`references/ecrits-professionnels.md` §5.1 et `references/penal-procedure.md`
§4.3 :

1. **Y a-t-il eu appréhension d'une personne (art. 73 CPP) ?**
   Non → ce n'est **pas** le bon écrit. Réorienter vers
   `assets/rapport-information.md` (simple compte rendu, sans appréhension)
   ou `assets/pv-contravention.md` (constatation d'une contravention relevant
   de la compétence de verbalisation de l'agent), selon la logique de
   `references/ecrits-professionnels.md` §5.1.
2. **Le fait est-il bien un crime ou un délit flagrant puni d'une peine
   d'emprisonnement** (régime de la flagrance, art. 53 et s. CPP — périmètre
   exact et seuils à confirmer en version consolidée) ?
   Si l'agent a un doute sérieux sur la flagrance ou la gravité du fait,
   le signaler explicitement comme point à vérifier avant de présenter
   l'appréhension comme régulière — ne jamais trancher ce point de qualification
   dans ce générateur (renvoi `references/penal-procedure.md` §4.3).
3. **Rappel du garde-fou APJA (`SKILL.md` §5.2,
   `references/penal-procedure.md` §4.4-4.5)** : ce générateur **ne sert qu'à
   documenter l'appréhension et la remise à l'OPJ**. Si, à un moment
   quelconque du recueil, il apparaît qu'un acte réservé à l'OPJ a été
   pratiqué ou s'apprête à l'être par l'agent PM lui-même (audition formelle,
   fouille hors cadre de sécurité, garde à vue, perquisition, réquisition
   judiciaire), afficher **immédiatement** le bloc **STOP** ci-dessous, avant
   tout autre contenu, et limiter la suite à l'action APJA conforme.

```
STOP — Cet acte relève de la compétence exclusive de l'OPJ
(Police Nationale / Gendarmerie).
Procéder à la mise à disposition immédiate (art. 73 CPP) et figer les lieux.
```

**Rappel structurant** (`references/ecrits-professionnels.md` §5.4) : ce
générateur reste **le seul** des trois écrits de la branche mobilisable une
fois le garde-fou déclenché — il documente précisément l'action conforme
(appréhension + remise), jamais l'acte réservé lui-même.

Si aucun blocage n'apparaît : le **rapport de mise à disposition** est le bon
écrit. Poursuivre au §1.

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

### Étape 2 — Date et heure des faits à l'origine de l'appréhension
- Date et heure précises du crime ou délit flagrant constaté (distincte, le
  cas échéant, de l'heure d'appréhension elle-même, étape 6).
> *Question posée* : « À quelle date et à quelle heure le fait (crime ou
> délit) s'est-il produit ou a-t-il été constaté en flagrance ? »

### Étape 3 — Lieu
- Localisation précise du fait et, si différent, lieu de l'appréhension.
> *Question posée* : « Où le fait s'est-il produit, et où l'appréhension
> a-t-elle eu lieu (si lieu différent) ? »

### Étape 4 — Faits (quoi / comment), caractérisant la flagrance
- Description **factuelle** des éléments personnellement constatés permettant
  de caractériser la flagrance (fait se commettant ou venant de se commettre),
  sans interprétation ni supposition.
> *Question posée* : « Que s'est-il passé ? Décrivez les faits que vous avez
> personnellement constatés et qui caractérisent, selon vous, un crime ou un
> délit flagrant. »

### Étape 5 — Qualification envisagée (à titre d'hypothèse)
- Le rapport de mise à disposition **n'a pas vocation à trancher** la
  qualification pénale (renvoi `references/penal-procedure.md` et
  `references/reglementation-appliquee.md` pour le fond). Elle doit être
  présentée comme une **hypothèse**, utile pour motiver l'appréhension, jamais
  comme acquise.
> *Question posée* : « Quelle qualification pénale est envisagée pour ce
> fait (à titre d'hypothèse, sans trancher) ? S'agit-il bien d'un crime ou
> d'un délit puni d'une peine d'emprisonnement (condition de l'art. 73
> CPP) ? »

### Étape 6 — Heure exacte de l'appréhension
- Mention **obligatoire**, propre à cet écrit (`ecrits-professionnels.md`
  §5.3) : heure précise à laquelle la personne a été appréhendée (début de la
  contrainte).
> *Question posée* : « À quelle heure exacte la personne a-t-elle été
> appréhendée ? »

### Étape 7 — Description de la contrainte exercée
- Description strictement limitée à ce qui a été nécessaire pour
  l'appréhension et la conduite vers l'OPJ (ex. interpellation, maintien sur
  place, escorte). **Ne jamais** consigner de questions-réponses
  circonstanciées, de fouille hors cadre de sécurité, ni tout élément pouvant
  s'apparenter à une audition ou à un acte d'enquête — cela relève
  exclusivement de l'OPJ (`references/penal-procedure.md` §4.3-4.4).
> *Question posée* : « Quelle contrainte avez-vous exercée sur la personne,
> et seulement celle-là (ex. interpellation, maintien, escorte) ? Confirmez
> qu'aucune audition ni fouille hors cadre de sécurité n'a été pratiquée. »

### Étape 8 — Personne appréhendée
- Identité si connue (jamais de donnée nominative en clair dans le canevas —
  voir §3), à défaut éléments de signalement objectifs.
> *Question posée* : « La personne appréhendée est-elle identifiée ? Si oui,
> précisez son identité (restera anonymisée dans le canevas tant qu'elle
> n'est pas confirmée pour la version consolidée). »

### Étape 9 — Témoins
- Présence de témoins de l'appréhension ou des faits, identifiés ou non.
> *Question posée* : « Y a-t-il des témoins de l'appréhension ou des faits ?
> Si oui, sont-ils identifiés ? »

### Étape 10 — Heure exacte de la mise à disposition de l'OPJ
- Mention **obligatoire** : heure précise à laquelle la personne a été
  effectivement remise à l'OPJ (fin de la contrainte exercée par l'agent PM).
  Si la remise n'a pas encore eu lieu au moment de la rédaction, le signaler
  explicitement (le document ne peut alors être considéré comme finalisé,
  §4).
> *Question posée* : « À quelle heure exacte la personne a-t-elle été remise
> à l'officier de police judiciaire ? Si la remise n'a pas encore eu lieu,
> précisez-le. »

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
> appréhendée », « le témoin 1 ») si la donnée doit rester anonymisée pour
> l'échange avec l'assistant.
>
> ⚠️ **Avant transmission** : vérifier en version consolidée tout texte
> d'incrimination évoqué et le régime exact de la flagrance (art. 53 et s.,
> art. 73 CPP — renvoi `references/penal-procedure.md` §4.3), et confirmer le
> circuit local de transmission (organisation propre à la collectivité,
> convention de coordination — `references/continuum-partenariats.md`).

```
[COLLECTIVITÉ — en-tête / service de police municipale]

RAPPORT DE MISE À DISPOSITION N° [numéro] / [année]
(établi en application de l'article 73 du Code de procédure pénale)

Rédigé par : [nom, qualité, n° d'agrément si exigé]
Date et heure de rédaction : [date] à [heure]

I. FAITS À L'ORIGINE DE L'APPRÉHENSION
Date et heure des faits : [date] à [heure] — étape 2
Lieu des faits : [adresse ou localisation précise] — étape 3
[Description strictement factuelle des éléments personnellement constatés
caractérisant un crime ou un délit flagrant puni d'une peine
d'emprisonnement — étape 4. Pas d'interprétation, pas de supposition.]

II. QUALIFICATION ENVISAGÉE (à titre d'hypothèse, non tranchée par ce rapport)
[Texte d'incrimination évoqué — étape 5. Mention obligatoire : « qualification
non tranchée par le présent rapport, à vérifier — renvoi
reglementation-appliquee.md / penal-procedure.md ». Préciser explicitement si
la condition de peine d'emprisonnement (art. 73 CPP) est remplie ou à
vérifier.]

III. APPRÉHENSION (ART. 73 CPP)
Lieu de l'appréhension (si différent du lieu des faits) : [adresse ou
« identique au lieu des faits »] — étape 3
Heure exacte de l'appréhension : [heure] — étape 6
Personne appréhendée : [identité ou « non identifiée » / éléments de
signalement objectifs] — étape 8
Description de la contrainte exercée, strictement limitée à ce qui a été
nécessaire : [interpellation / maintien sur place / escorte — étape 7]
Il est précisé qu'aucune audition formelle, fouille hors cadre de sécurité,
ni mesure assimilable à un acte réservé à l'officier de police judiciaire
(art. 16 CPP) n'a été pratiquée par le rédacteur.

IV. TÉMOINS
[Identité(s) ou « néant » ; précisions le cas échéant — étape 9]

V. MISE À DISPOSITION DE L'OFFICIER DE POLICE JUDICIAIRE
Heure exacte de la mise à disposition : [heure, ou « remise non encore
effectuée à l'heure de rédaction du présent rapport — voir section
CHAMPS MANQUANTS »] — étape 10
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
- **Objectivité stricte** sur les faits à l'origine de l'appréhension :
  description des éléments personnellement constatés, pas de jugement de
  valeur ni de supposition sur les intentions.
- **Toute référence de texte** (incrimination, régime de flagrance) porte la
  réserve « à confirmer en version consolidée » sauf identifiant déjà
  vérifié dans la session courante (règle de provenance, `SKILL.md` §5.3).
- **Pas de qualification pénale tranchée** dans ce document : renvoi
  systématique aux branches compétentes (§0, §1 étape 5).
- **Deux heures distinctes et obligatoires** : heure d'appréhension (étape 6)
  et heure de mise à disposition (étape 10). Ne jamais les fusionner ni en
  approximer une à partir de l'autre.
- **Contrainte strictement limitée** : la section III ne décrit que ce qui a
  été nécessaire à l'appréhension et à la conduite vers l'OPJ. **Aucune
  trace d'audition, de questions-réponses circonstanciées, de fouille hors
  cadre de sécurité, ni de toute autre mesure relevant de l'art. 16 CPP** ne
  doit apparaître dans ce rapport — c'est le cœur du **garde-fou APJA**
  appliqué à cet écrit (`references/ecrits-professionnels.md` §5.4, §8 point
  7).
- **L'acte d'enquête reste à l'OPJ** : ce rapport documente la **remise**, il
  ne préjuge ni ne décrit aucune suite procédurale (garde à vue, audition,
  classement) qui relève de la seule décision de l'OPJ et, le cas échéant, du
  procureur de la République. Ne jamais anticiper ni suggérer cette suite
  dans le corps du rapport.

---

## 4. Règle `[INCOMPLET]` — application stricte

**Interdiction absolue d'halluciner une donnée manquante** (date, heure,
lieu, identité, texte d'incrimination, heure d'appréhension, heure de mise à
disposition, identité/qualité de l'OPJ).

Si une information nécessaire à une étape du §1 n'a pas été fournie, et **en
particulier** si l'heure exacte d'appréhension (étape 6) ou l'heure exacte de
mise à disposition (étape 10) manque :

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

Point de vigilance particulier : l'heure d'appréhension et l'heure de mise à
disposition sont des mentions obligatoires de cet écrit
(`references/ecrits-professionnels.md` §5.3) ; leur absence empêche de
documenter la durée de la contrainte exercée et fragilise la conformité de
l'appréhension au regard de l'art. 73 CPP (contrainte strictement
proportionnée au temps nécessaire — `references/penal-procedure.md` §4.3).

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
- Le **compte rendu oral immédiat** à l'OPJ (au moment ou immédiatement après
  la mise à disposition) **précède** la rédaction de cet écrit et n'est pas
  remplacé par lui : l'écrit **formalise** la trace après coup, il ne s'y
  substitue pas. Ne jamais présenter la rédaction du rapport écrit comme la
  première information donnée à l'OPJ.
- **Aucun délai chiffré** n'est donné de mémoire pour la rédaction de ce
  rapport : la **mise à disposition elle-même** (l'acte matériel de remise)
  doit intervenir « dans le délai le plus court possible »
  (`references/penal-procedure.md` §5 point 4) ; l'écrit qui la formalise
  suit dès que possible, sans retarder la transmission du compte rendu oral.
- **Archivage** : conserver une trace de la version transmise
  (`references/ecrits-professionnels.md` §6.6), utile en cas de contestation
  ultérieure de la régularité de l'appréhension ou de reconstitution
  chronologique exacte des heures (appréhension / mise à disposition).

---

## 6. Articulation avec le garde-fou APJA (rappel)

Ce générateur est, par construction, **l'écrit du garde-fou APJA**
(`references/ecrits-professionnels.md` §5.4, `references/penal-procedure.md`
§4.5) : il documente précisément l'action conforme — appréhender, contraindre
au strict nécessaire, remettre à l'OPJ — quand la situation dépasse ou
s'apprête à dépasser le pouvoir APJA.

Si, à n'importe quelle étape du recueil (§1), il apparaît que l'agent PM a
pratiqué ou s'apprête à pratiquer un acte réservé à l'OPJ (audition formelle,
fouille hors cadre de sécurité, garde à vue, perquisition hors flagrance
stricte, réquisition judiciaire — art. 16 CPP,
`references/penal-procedure.md` §4.4), interrompre la séquence de questions
et afficher immédiatement le bloc **STOP** (§0) **avant** de poursuivre quoi
que ce soit d'autre. La suite se limite alors à :
1. l'affichage du STOP en premier ;
2. la consignation, dans ce même rapport, des seules informations relevant
   de l'appréhension et de la remise (sections I à III et V du gabarit, §2) ;
3. la **non-rédaction** de toute section qui décrirait un acte réservé —
   préférer `[INCOMPLET — hors champ APJA, acte réservé OPJ, ne pas
   formaliser]` plutôt que de décrire l'acte ;
4. le compte rendu à l'OPJ et au maire, sans attendre la rédaction définitive
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
| Caractérisation de la flagrance et de la gravité (crime/délit puni d'emprisonnement) | Élevé | À vérifier au cas par cas — jamais tranchée ici, renvoi `penal-procedure.md` §4.3 |
| Heure d'appréhension / heure de mise à disposition | Élevé | `[INCOMPLET]` obligatoire si absente — mentions structurantes de l'écrit |
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
3. Appréhension (art. 73 CPP) explicitement confirmée comme déclencheur de
   cet écrit — sinon, redirection vers `assets/rapport-information.md` ou
   `assets/pv-contravention.md` selon le cas (§0).
4. **Heure exacte de l'appréhension** et **heure exacte de la mise à
   disposition** toutes deux renseignées, ou marquées `[INCOMPLET]` avec
   demande explicite (§4) — jamais l'une déduite de l'autre.
5. **Identité ou qualité de l'OPJ destinataire** renseignée, ou marquée
   `[INCOMPLET]`.
6. **Description de la contrainte exercée** strictement limitée à
   l'appréhension et à la conduite vers l'OPJ : aucune trace d'audition, de
   fouille hors cadre de sécurité, ni d'acte d'enquête.
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
