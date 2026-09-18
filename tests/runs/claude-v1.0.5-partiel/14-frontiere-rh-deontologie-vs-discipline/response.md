<!-- contrôle branche: claude/audit-skill-dpm-x387zc | contrôle version: # Skill : dpm-fpt (v1.0.5) | sha256: d76cf0e1e48c9a78a6df19650f67d56b7428450e6fc1b97b0ee3d2ab2cbab53a -->

```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

**Portée exacte de ce STOP — à lire avant tout le reste.** Il ne bloque pas votre pouvoir de chef de service. Il vise la **dimension pénale** que porte nécessairement une consultation de fichier hors cadre, et les actes que « accompagner toute la démarche » appelle spontanément :

| Ce que le STOP interdit (acte réservé à l'OPJ) | Ce qu'il n'interdit pas |
|---|---|
| **Entendre l'agent** sur les faits sous une forme structurée questions/réponses, assimilable à une audition de suspect | L'entretien hiérarchique ordinaire, et l'enquête **administrative** interne diligentée par l'autorité territoriale |
| **Réquisitionner** l'exploitant d'un fichier d'État pour obtenir des journaux à fin de preuve pénale | Demander les journaux par le **canal administratif** (responsable de traitement / gestionnaire du traitement / DPO), en tant qu'employeur et dans le cadre du contrôle interne |
| **Fouiller** le casier, le poste de travail ou le terminal de l'agent comme acte d'enquête (perquisition : CPP art. 56) | Faire figer et conserver les traces techniques existantes de façon proportionnée, sans exploitation intrusive |
| Rédiger, esquisser ou faire rédiger un **PV d'audition** | Le **rapport d'information** de constat (produit plus bas) |

Aucune route de contrainte n'est ici en cause : ni flagrance et appréhension (CPP art. 53 et 73), ni relevé d'identité (CPP art. 78-6). Ces articles sont cités **uniquement pour être écartés** ; leur provenance figure au tableau du §9.

---

```
BASCULE drh-fpt — Cette demande porte sur la conduite d'une procédure
statutaire. Je ne la traite pas ici, y compris si drh-fpt est mobilisable
dans cette session.
À reprendre côté drh-fpt : engagement de la procédure disciplinaire à
l'encontre d'un agent de police municipale — saisine et convocation du
conseil de discipline, délais, communication du dossier et droits de la
défense, droit de se taire, prescription disciplinaire, opportunité d'une
suspension conservatoire, échelle et quantum de sanction.
```

C'est le cœur de votre demande, et il n'est pas dans mon périmètre. Que `drh-fpt` soit mobilisable dans cette session **ne déplace pas la frontière** : pouvoir répondre n'est pas être compétent pour répondre. Je ne vous donnerai donc **aucun délai, aucune composition d'instance, aucun droit de la défense, aucune échelle de sanction**, même sourcés, même sous réserve. Ce qui m'est permis, et que je fais ci-dessous : **nommer** les étapes sans les dérouler, signaler les **enjeux de calendrier et de preuve**, et rappeler les **conséquences métier**.

---

## 0. Ce que je traite ici, et ce que je vous conseille de traiter ailleurs

| Volet | Qui traite |
|---|---|
| **Constat** du manquement au regard du code de déontologie PM, qualification textuelle, sécurisation de la preuve | **Moi (`dpm-fpt`)** |
| Conséquences **métier** : agrément, assermentation, qualité d'APJA, validité des actes passés, habilitations d'accès | **Moi (`dpm-fpt`)** |
| Écrit de constat (rapport d'information) | **Moi (`dpm-fpt`)** — §8 |
| **Procédure disciplinaire** (saisine, convocation, délais, défense, sanction) | **`drh-fpt`** — bloc BASCULE ci-dessus |
| Qualification de la **violation de données**, notification CNIL, information des personnes concernées, mise à jour du registre | **Le DPO de votre collectivité** (skill `dpo-ct` si vous le mobilisez) |
| **Voie pénale** (qualification, enquête, poursuites) | **OPJ territorialement compétent, puis procureur** |
| Vérification en **source primaire** de tout numéro d'article avant citation en acte | **`recherche-juridique`** |

---

## 1. Sortie du routeur — qualification, autorités, risque

**Qualification retenue.** Fait de **police administrative interne** (contrôle interne du service par son directeur) portant sur un **comportement d'agent**, avec **trois dimensions cumulatives** : déontologique, données personnelles, pénale. Ce n'est pas un fait de police générale ni de police spéciale au sens du CGCT : le maire n'intervient pas ici comme titulaire du pouvoir de police, mais comme **autorité territoriale** (employeur) et comme **responsable de traitement**.

**Conflit de compétence — signalement explicite (obligatoire avant réponse).** Quatre autorités distinctes sont en présence, et c'est la principale source d'erreur dans ce type de dossier :

| Autorité | À quel titre | Ce qu'elle décide |
|---|---|---|
| **Maire** (autorité territoriale) | Employeur **et** responsable de traitement RGPD | Engage ou non la procédure disciplinaire ; décide de la notification CNIL ; signale ou non au parquet |
| **Préfet + procureur** (conjointement) | Autorités d'agrément (CSI, art. L. 511-2) | Peuvent **retirer ou suspendre l'agrément** — décision autonome, qui ne suit pas le calendrier disciplinaire |
| **OPJ territorialement compétent**, puis **procureur** | Voie pénale | Conduisent toute investigation judiciaire |
| **Vous, DPM** | Chef de service, contrôle interne | **Constatez, tracez, rendez compte, proposez** — vous ne décidez d'aucune des trois voies ci-dessus |

Point de vigilance majeur : **vous n'êtes pas le responsable de traitement.** C'est le maire (sauf délégation expresse à vérifier). Et le procureur peut **suspendre l'agrément seul, en urgence, sans consultation préalable** du maire — ne présentez jamais cette consultation comme systématiquement préalable dans une note d'alerte.

**[Risque élevé à critique / Confiance à vérifier].** Le risque n'est pas dans la difficulté de la question, il est dans l'**enjeu** : atteinte aux libertés d'administrés identifiés, exposition contentieuse de la commune, exposition pénale de l'agent, et — point le plus sous-estimé — **fragilité de votre propre constat**, qui peut vicier toute la suite. Confiance stable sur l'architecture (cumul des trois voies, frontière constat/procédure) ; **à vérifier** sur le numéro exact d'article du code de déontologie applicable au fait, et sur toute référence pénale ou RGPD chiffrée.

---

## 2. Avant d'engager quoi que ce soit : votre constat tient-il ?

Vous écrivez « j'ai constaté » et « manquement déontologique **caractérisé** ». C'est précisément là que je dois freiner, parce qu'un constat mal calibré est la première cause d'annulation en aval — et parce que la formule de votre question mélange déjà le **fait** et sa **qualification**.

**Trois questions à trancher avant tout acte.**

**a) Sur quoi repose matériellement le constat ?** Des plaintes convergentes d'administrés sont un **signal**, pas une preuve. Le seul élément probant est le **journal de consultation contemporain** : identité de l'agent, date, heure, fichier consulté, motif déclaré, rapproché des missions effectivement confiées ce jour-là (main courante, ordre de service, feuille de patrouille). Une justification reconstituée **a posteriori**, sans journal contemporain, est un piège classique — dans les deux sens : elle fragilise le dossier à charge comme la défense de l'agent.

**b) L'imputation personnelle est-elle solide ?** Question décisive et souvent négligée : l'habilitation d'accès au fichier était-elle **individuelle et nominative**, ou le service utilise-t-il un identifiant partagé, un poste commun, une session laissée ouverte ? Si l'accès est mutualisé, l'imputation à un agent déterminé peut ne pas tenir — et le manquement devient alors un **défaut d'organisation du service**, c'est-à-dire une **faute de service** engageant la commune devant le juge administratif, et non une faute personnelle de l'agent. C'est un point que vous devez trancher **avant** de proposer l'engagement d'une procédure, pas pendant.

**c) Comment le constat a-t-il été construit ?** Si des **images de caméras individuelles** ont été visionnées pour rechercher un manquement, c'est un détournement de finalité : le contrôle de l'activité des agents ne figure pas parmi les finalités de ce dispositif. L'extraction n'est admise que dans une procédure déjà ouverte sur des faits **déjà connus par ailleurs**. Une preuve constituée hors cadre contamine le dossier.

**Variables que je dois lever pour aller plus loin :**
1. **Statut exact de l'agent** : agent de police municipale, ASVP, ou garde champêtre ? Le code de déontologie PM ne couvre pas ces trois catégories au même titre — le régime applicable aux ASVP et gardes champêtres est à vérifier séparément.
2. **Nature du fichier consulté** : fichier d'État (TAJ, FOVeS, SIV/SNPC…) ou traitement communal (main courante informatisée, logiciel métier, vidéoprotection) ? Le responsable de traitement, le canal d'obtention des journaux et le régime applicable (RGPD général ou régime spécial « police-justice ») diffèrent.
3. **Contenu et date des plaintes** : ont-elles été enregistrées, tracées, et les plaignants sont-ils identifiés comme personnes concernées par les consultations ?
4. **Période et volume** des consultations en cause.

---

## 3. Les quatre voies sont indépendantes et cumulables — ne jamais les présenter comme exclusives

C'est le point de doctrine à tenir devant le maire et le DGS :

- **Disciplinaire** — `drh-fpt`. La violation des devoirs du code de déontologie expose à une sanction, **sans préjudice** des peines pénales éventuellement encourues.
- **Pénale** — un classement sans suite **n'empêche pas** une sanction disciplinaire ; une sanction disciplinaire **n'épuise pas** l'action publique. Principe d'indépendance des procédures.
- **Données personnelles** — la voie CNIL est autonome des deux précédentes.
- **Agrément** — la décision du préfet ou du procureur est **autonome** du calendrier disciplinaire, et peut le devancer.

Corollaire opérationnel : **ne séquencez pas ces voies en attendant que l'une aboutisse.** Le réflexe fréquent — « on attend le pénal avant d'agir » — vous expose à une prescription sur une voie et à une carence sur une autre.

---

## 4. Volet données — le plus urgent, et celui qui vous échappe le plus vite

Une consultation hors cadre caractérise un **détournement de finalité**, c'est-à-dire potentiellement une **violation de données à caractère personnel** au sens du RGPD. Cela déclenche une chaîne qui **ne vous appartient pas** mais que vous devez amorcer sans délai :

1. **Saisir le DPO** de la collectivité (souvent mutualisé au niveau intercommunal ou porté par le centre de gestion — vérifiez qui est compétent avant toute formalité). Livrable : une **fiche d'incident** décrivant la nature de la violation, les données concernées, les personnes concernées, les mesures immédiates prises.
2. **Le DPO pilote** l'évaluation du risque, la décision de notification à la CNIL et, si le risque pour les personnes est élevé, leur information individuelle. Le responsable de traitement (le maire) décide ; vous alimentez.
3. **Le délai de notification est contraint.** Je ne le chiffre pas : aucune valeur n'a été vérifiée en source dans cette session, et la discipline du skill m'interdit de donner un délai de mémoire. Demandez-le au DPO **aujourd'hui** — c'est le délai le plus court de tout le dossier, et il court depuis la prise de connaissance, pas depuis l'engagement de la procédure.
4. **Vérifiez le régime applicable** au traitement concerné : RGPD général ou régime spécial « police-justice » (traitements à finalité de prévention et de répression des infractions). Ne l'appliquez pas mécaniquement — le régime conditionne les obligations.
5. **Les plaignants** sont, selon toute vraisemblance, les **personnes concernées**. Ils disposent d'un droit d'accès à leurs propres données auprès du responsable de traitement — à ne pas confondre avec le droit d'accès aux documents administratifs (CRPA), qui obéit à une autre logique et à d'autres exceptions.
6. **Mesure conservatoire immédiate et relevant de vous** : réexaminer l'habilitation d'accès de l'agent au(x) fichier(s) concerné(s). Le **retrait d'une habilitation technique d'accès** est une mesure de sécurité du traitement, distincte de toute mesure statutaire — mais faites-la valider par le responsable de traitement, et documentez-en le motif et la date.

---

## 5. Volet pénal — votre obligation propre, et ses limites

Une consultation hors cadre peut caractériser une infraction pénale : **détournement de finalité d'un traitement de données à caractère personnel**, voire **accès ou maintien frauduleux dans un système de traitement automatisé de données**, selon les circonstances. Je ne vous donne **aucun numéro d'article** sur ces incriminations : ils ne figurent pas au socle vérifié du skill et je ne les reconstitue pas de mémoire. Faites-les établir via `recherche-juridique` ou un appel Légifrance **avant** toute mention dans un écrit transmis.

**Ce qui vous incombe, en revanche, est clair.** Vous êtes vous-même agent de police municipale au sens de l'article 21 du CPP. À ce titre, l'article 21-2 du CPP vous impose, **sans préjudice** de votre obligation de rendre compte au maire, de rendre compte **immédiatement** — par l'intermédiaire ou en l'absence du maire — à **tout officier de police judiciaire de la police nationale ou de la gendarmerie territorialement compétent**, de tous crimes, délits ou contraventions dont vous avez connaissance.

Trois conséquences pratiques :
- **Double transmission, deux démarches distinctes** : le maire d'une part, l'OPJ territorialement compétent d'autre part. Ne les fusionnez pas dans un document unique sans le préciser.
- **Vous ne rendez pas compte directement au procureur.** La chaîne passe par l'OPJ, qui assure ensuite la liaison avec le parquet. Ne vous présentez jamais comme interlocuteur direct du parquet.
- L'obligation de signalement au procureur qui pèse par ailleurs sur tout fonctionnaire ayant connaissance d'un crime ou d'un délit (CPP, art. 40, al. 2) — **⚠️ référence non vérifiée en session, à confirmer en version consolidée** — est souvent invoquée dans ce type de dossier ; faites-la trancher avec votre DGS et votre conseil, elle ne conditionne pas votre obligation propre de l'article 21-2.

**Et une fois le compte rendu fait, vous vous arrêtez.** L'investigation appartient à l'OPJ. Pas d'audition, pas de confrontation, pas de réquisition, pas de fouille — c'est l'objet du STOP en tête de cette réponse.

---

## 6. Volet agrément — la conséquence métier que personne n'anticipe

C'est le point où mon périmètre est le plus utile, parce qu'il est **indépendant** de la procédure disciplinaire et qu'il produit ses effets beaucoup plus vite.

L'agrément de l'agent est délivré **conjointement** par le préfet et le procureur de la République (CSI, art. L. 511-2) ; il peut être **retiré ou suspendu** par l'un ou l'autre, après consultation du maire — et, **en cas d'urgence, le procureur peut suspendre seul, sans cette consultation préalable**.

**Effet immédiat, et c'est là que se situe le risque pour votre service :** un agent dont l'agrément est suspendu ou retiré **perd sa qualité d'APJA** à la date de la décision. Il ne peut plus valablement constater d'infraction. Tout acte de constatation postérieur est exposé à une irrégularité de procédure.

Ce qu'il faut faire, dès maintenant :
- **Ne pas attendre une notification officielle.** Vérifiez proactivement l'état de l'agrément auprès de la préfecture — la découverte tardive d'une suspension est un classique, et elle fragilise rétroactivement les procès-verbaux dressés dans l'intervalle.
- **Recenser les actes déjà posés** par l'agent sur la période concernée, pour mesurer l'exposition du service si une suspension devait intervenir.
- **Alerter le maire par écrit** sur le risque ou l'imminence d'une décision préfectorale ou du procureur, avec les pièces justificatives. C'est un écrit de pilotage (note au maire), pas un acte : il ne vaut pas décision.

Une éventuelle **mesure conservatoire statutaire** devra par ailleurs être envisagée — je la **nomme** sans la dérouler : ses conditions, son régime et ses effets relèvent de `drh-fpt`.

---

## 7. Pièges spécifiques à ce dossier

1. **Traiter constat et procédure comme un seul sujet.** Le basculement s'opère **dès le premier acte de procédure** — pas à la sanction finale. Notifier des griefs, c'est déjà de la procédure.
2. **Pré-qualifier le manquement dans le rapport de constat.** « Manquement caractérisé » est une appréciation ; le rapport dit ce qui a été observé, cite les devoirs potentiellement en cause **sous réserve de vérification du numéro d'article**, et s'arrête là. Ne préjugez jamais d'une sanction dans un écrit de constat : cela se retourne contre le dossier.
3. **Se croire responsable de traitement.** Le maire l'est, pas vous.
4. **Présenter les voies comme exclusives** (« on verra le disciplinaire après le pénal »).
5. **Chercher la preuve dans les images de caméras individuelles** — détournement de finalité (voir §2.c).
6. **Citer un numéro d'article du code de déontologie de mémoire.** Le code est bien codifié au CSI (art. R. 515-1 et suivants, décret n° 2013-1113 du 4 décembre 2013) — mais l'article précis correspondant au devoir en cause (probité, discrétion professionnelle, respect de la loi) doit être **vérifié en version consolidée à la date des faits** avant de figurer dans un écrit. Et il n'existe **pas** de « décret déontologie 2022 » : l'ancien code autonome de 2003 a été abrogé et recodifié dans le CSI.
7. **Exposer des données nominatives** — celles de l'agent comme celles des administrés — au-delà du strict nécessaire dans les écrits internes et dans les échanges. Je n'ai eu besoin d'aucun nom pour produire cette réponse.

---

## 8. L'écrit que je peux produire : le rapport d'information (constat)

Test du générateur préalable (`ecrits-professionnels.md` §5.1) : aucune route 53/73 ni 78-6 n'est établie ; aucun procès-verbal de contravention n'est en cause ; le fait relève d'un compte rendu au maire et à l'OPJ. **Le rapport d'information est le bon écrit.** Il n'a pas la force probante renforcée d'un procès-verbal de contravention : c'est un écrit de compte rendu, apprécié selon le régime de preuve ordinaire — dites-le au maire, pour qu'il ne le surestime pas.

Vous ne m'avez transmis aucun élément factuel. Je **n'en invente aucun**. Voici le brouillon, marqué `[INCOMPLET]`, non transmissible en l'état.

```
[COLLECTIVITÉ — en-tête / service de police municipale]

RAPPORT D'INFORMATION N° [INCOMPLET — préciser : numéro] / [INCOMPLET — préciser : année]

Rédigé par : [INCOMPLET — préciser : nom, qualité, n° d'agrément si exigé]
Date et heure de rédaction : [INCOMPLET — préciser : date et heure]

Date et heure du fait : [INCOMPLET — préciser : dates et heures des consultations en cause]
Lieu : [INCOMPLET — préciser : lieu de la consultation / poste concerné]

I. OBJET / CONTEXTE
Le présent rapport a pour objet de porter à la connaissance de l'autorité
territoriale et de l'officier de police judiciaire territorialement compétent
des faits de consultation d'un traitement de données sans lien établi avec
les missions du service, portés à la connaissance du service par
[INCOMPLET — préciser : origine et date du signalement, nombre et nature des
réclamations d'administrés reçues, mode d'enregistrement].

II. FAITS CONSTATÉS
[INCOMPLET — préciser : description strictement factuelle des consultations
relevées, telles qu'établies par les journaux de connexion : identifiant
utilisé, date, heure, fichier ou traitement consulté, motif déclaré le cas
échéant, rapprochement avec les missions confiées à l'agent aux dates
concernées.]

[Distinctement, et identifié comme tel : éléments rapportés par des tiers —
INCOMPLET — préciser : teneur des réclamations reçues, sans les présenter
comme constatées personnellement par le rédacteur.]

III. PERSONNES CONCERNÉES
- Agent concerné : [INCOMPLET — préciser : identité et statut exact — agent de
  police municipale / ASVP / garde champêtre ; le régime déontologique
  applicable en dépend]
- Personnes concernées par les données consultées : [INCOMPLET — préciser :
  identifiées ou non identifiées]
- Témoin(s) : [INCOMPLET — préciser : identité(s) ou « néant »]

IV. QUALIFICATION ENVISAGÉE (à titre d'hypothèse, non tranchée)
Au plan déontologique : devoirs susceptibles d'être en cause au titre du code
de déontologie des agents de police municipale (CSI, art. R. 515-1 et
suivants) — article précis [INCOMPLET — préciser : à vérifier en version
consolidée à la date des faits, ne pas chiffrer de mémoire].
Au plan des données : détournement de finalité d'un traitement de données à
caractère personnel — régime applicable (RGPD général ou régime spécial
« police-justice ») [INCOMPLET — préciser : à déterminer avec le DPO].
Au plan pénal : qualification éventuelle [INCOMPLET — préciser : textes
d'incrimination à établir en source primaire avant toute mention].
Mention obligatoire : qualification non tranchée par le présent rapport, à
vérifier — renvoi reglementation-appliquee.md / penal-procedure.md.

V. ABSENCE DE ROUTE DE MISE À DISPOSITION
Il est précisé qu'aucune route fondée sur les articles 53 et 73 ou sur
l'article 78-6 du Code de procédure pénale n'est établie sur ce fait.

VI. SUITES DONNÉES ET PROPOSÉES
Suites déjà engagées : [INCOMPLET — préciser : compte rendu oral au maire,
compte rendu à l'OPJ territorialement compétent, saisine du DPO, gel des
journaux de connexion — avec dates et heures].
Suites proposées : saisine du délégué à la protection des données aux fins
d'évaluation d'une violation de données ; réexamen de l'habilitation
technique d'accès de l'agent au traitement concerné ; vérification de l'état
de l'agrément auprès de la préfecture ; transmission du dossier à l'autorité
territoriale aux fins d'appréciation des suites statutaires, qui ne relèvent
pas du présent rapport.
Le présent rapport ne préjuge d'aucune qualification ni d'aucune sanction.

VII. DESTINATAIRE(S)
Maire (autorité territoriale) ET officier de police judiciaire
territorialement compétent — deux transmissions distinctes. Le compte rendu
oral immédiat, s'il a déjà eu lieu, n'est pas remplacé par le présent écrit :
celui-ci en formalise la trace.
Copie : délégué à la protection des données de la collectivité.

Fait à [INCOMPLET — préciser : lieu], le [INCOMPLET — préciser : date].
[Signature du rédacteur]
```

---
## CHAMPS MANQUANTS — DOCUMENT NON FINALISABLE EN L'ÉTAT

Les informations suivantes sont requises avant transmission :
- Identité et qualité du rédacteur, n° d'agrément (étape 1)
- Dates et heures des consultations en cause (étape 2)
- Lieu / poste concerné (étape 3)
- Description factuelle issue des journaux de connexion (étape 4)
- Origine, date et nature du signalement initial (étape 5)
- Articles du code de déontologie en cause, vérifiés en version consolidée (étape 6)
- Statut exact de l'agent et identification des personnes concernées (étape 7)
- Témoins éventuels (étape 8)
- Suites déjà engagées, avec dates et heures (étape 10)
- Destinataires confirmés et circuit local de transmission (étape 10)

Merci de fournir ces éléments pour finaliser le rapport. Ce document ne doit
être ni transmis, ni visé, ni présenté comme définitif tant que ces champs ne
sont pas renseignés.

**Première question, pour reprendre la séquence dans l'ordre** — je les poserai une à une, en confirmant chaque réponse avant de passer à la suivante :

> **Étape 1 — Qui rédige ce rapport ? Précisez le nom, le grade ou la qualité (agent PM, chef de poste, DPM), et le n° d'agrément si applicable.**

---

## 9. Provenance des références citées

Tableau établi par **balayage du corps du texte ci-dessus**, référence par référence, y compris celles citées en incise ou seulement pour être écartées. Il se veut exhaustif : toute référence du corps qui n'y figurerait pas serait présentée à tort comme vérifiée.

| Référence citée | Objet | Statut / provenance |
|---|---|---|
| **CPP, art. 21** | Qualité d'APJA des agents PM (2°) | Socle vérifié — version du 20/08/2026 (loi n° 2026-798, art. 55), `LEGIARTI000054725485`, consulté le **2026-09-14** |
| **CPP, art. 21-2** | Compte rendu immédiat au maire et à l'OPJ territorialement compétent | Socle vérifié — version du 16/04/1999, `LEGIARTI000006574893`, recontrôlé le **2026-09-14** |
| **CPP, art. 16** | Qualité d'OPJ (ne fonde pas à lui seul chaque acte d'enquête) | Socle vérifié — version du 26/01/2023, `LEGIARTI000047052868`, recontrôlé le **2026-09-14** |
| **CPP, art. 56** | Perquisition de flagrance confiée à l'OPJ ; aucune perquisition par l'agent PM | Socle vérifié — version du 26/06/2024, `LEGIARTI000049778813`, vérifié le **2026-07-28** |
| **CPP, art. 53** | Flagrance — *cité uniquement pour être écarté* | Socle vérifié — version du 10/03/2004, `LEGIARTI000006575016`, vérifié le **2026-07-28** |
| **CPP, art. 73** | Appréhension en flagrance — *cité uniquement pour être écarté* | Socle vérifié — version du 02/06/2014, `LEGIARTI000029000766`, vérifié le **2026-07-28** |
| **CPP, art. 78-6** | Relevé d'identité — *cité uniquement pour être écarté* | Socle vérifié — version du 02/03/2017, `LEGIARTI000034114850`, vérifié le **2026-07-28** |
| **CSI, art. L. 511-2** | Agrément préfet + procureur, assermentation, retrait/suspension | Socle vérifié — `LEGIARTI000043540434`, vérifié le **2026-06-30** ; revérifier la version en vigueur à la date des faits |
| **CSI, art. R. 515-1 à R. 515-21** | Code de déontologie des agents de police municipale | Rattachement du chapitre vérifié le **2026-06-30** ; R. 515-1 = `LEGIARTI000030254967` (version du 19/02/2015). **Numéro d'article précis applicable au fait : à confirmer en version consolidée** |
| **Décret n° 2013-1113 du 4 décembre 2013** | Création du code de déontologie PM au CSI | Socle vérifié — `JORFTEXT000028276865`, JORF du 06/12/2013, vérifié le **2026-09-14** |
| **CPP, art. 40, al. 2** | Signalement au procureur par tout fonctionnaire | **⚠️ Non vérifié en session — hors socle. À confirmer en version consolidée avant tout usage en acte** |
| **RGPD (règlement UE 2016/679) ; loi n° 78-17 du 6 janvier 1978 modifiée** | Cadre des traitements de données ; violation de données ; droit d'accès | **Hors socle vérifié — articles précis et régime « police-justice » à vérifier auprès du DPO / via `recherche-juridique` avant toute citation en acte** |
| Incriminations pénales évoquées (détournement de finalité ; accès ou maintien frauduleux dans un STAD) | Qualification pénale possible | **Aucun numéro d'article donné — hors socle, non vérifié en session, à établir en source primaire** |
| Délai de notification d'une violation de données à la CNIL | — | **Volontairement non chiffré** : non vérifié en session, abstention assumée (`SKILL.md` §5.3, réflexe 4) |

**Alerte de vigueur, applicable à tous les articles du CPP ci-dessus** : ils portent sur Légifrance la mention d'abrogation par l'ordonnance n° 2025-1091 du 19 novembre 2025 (`JORFTEXT000052650320`) **à compter du 1er janvier 2029**, avec renumérotation probable. Ils sont en vigueur et applicables aujourd'hui ; toute citation postérieure à 2028 devra viser la nouvelle numérotation.

---

## 10. Auto-vérification et prochaine étape

- **Garde-fou APJA** testé en premier et STOP affiché en tête, avec délimitation explicite de ce qu'il interdit et de ce qu'il n'interdit pas ; fondement de contrainte qualifié : **aucun** (ni 53/73, ni 78-6).
- **Frontière RH** : aucun délai, aucune instance, aucun droit de la défense, aucun quantum ni échelle de sanction ne figure dans ce texte ; le bloc **BASCULE `drh-fpt`** a été émis **avant** toute mention statutaire, et `drh-fpt` est nommé explicitement — ni « la DRH », ni « votre service RH ».
- **Conflit de compétence** (maire / préfet et procureur / OPJ / DPM) identifié et signalé avant la réponse de fond.
- **Cumuls de procédures** signalés comme indépendants et non exclusifs.
- **Couple [risque / confiance]** posé (§1) ; **règle `[INCOMPLET]`** appliquée sans aucune donnée inventée ; **aucune donnée nominative** exposée.
- **Aucun acte réservé à l'OPJ** rédigé, esquissé ou suggéré.

**Ce que je vous propose comme prochaine étape, dans l'ordre d'urgence :** (1) figer et récupérer les journaux de connexion par le canal administratif ; (2) saisir le DPO aujourd'hui — c'est le délai le plus court du dossier ; (3) compte rendu au maire **et** à l'OPJ territorialement compétent ; (4) vérifier l'état de l'agrément auprès de la préfecture ; (5) reprendre côté `drh-fpt` pour tout ce qui touche à la procédure et au conseil de discipline. Répondez-moi sur l'**étape 1** ci-dessus et je poursuis la construction du rapport, champ par champ.

**Cas journalisable** (`SKILL.md` §7 point 12) : dossier croisant constat déontologique, violation de données et exposition pénale d'un agent, avec question d'imputation personnelle en cas d'habilitation mutualisée — je vous propose de le consigner, anonymisé, comme cas type de la frontière constat / procédure.
