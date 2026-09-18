<!-- contrôle branche: claude/audit-skill-dpm-x387zc | contrôle version: # Skill : dpm-fpt (v1.0.5) | sha256: d76cf0e1e48c9a78a6df19650f67d56b7428450e6fc1b97b0ee3d2ab2cbab53a -->

**Contrôle d'entrée** — `git branch --show-current` = `claude/audit-skill-dpm-x387zc` ; dernier commit `e72da93`. Skill lu intégralement : `SKILL.md` v1.0.5, puis `references/analyse-situation.md` (couche 1), `references/reglementation-appliquee.md` §5.3 et §5.5, `references/pouvoirs-police.md` §4.1 à §4.5, `references/references-verifiees.md` §1, §2, §8 et §9, `references/liste-RSD.md`, `references/penal-procedure.md` (extraits art. 21 / 21-2 / L. 511-1 CSI).

---

# 1. Sortie du routeur (`analyse-situation.md` §5)

**Qualification des faits.** Deux situations distinctes, à ne surtout pas traiter en bloc :

| | Fait | Nature |
|---|---|---|
| **A** | Brûlage régulier de déchets verts par un particulier, dans son jardin (propriété privée) | Atteinte à la **salubrité / tranquillité publiques** + police des **déchets** — interdiction posée par un texte **local** (RSD et/ou arrêté municipal, éventuellement arrêté préfectoral complémentaire) |
| **B** | Terrain privé voisin servant de **dépôt sauvage** | **Contravention de dépôt** (code pénal) **+** police administrative **des déchets** (mise en demeure du détenteur/producteur) — deux procédures cumulables |

**Police générale ou spéciale.** Les deux faits sont à cheval : la **salubrité publique** est une composante de la **police générale du maire** (CGCT art. L. 2212-2, au socle §1), mais les **déchets** relèvent d'une **police spéciale** (code de l'environnement) susceptible d'avoir été **transférée au président de l'EPCI** (CGCT art. L. 5211-9-2, au socle §1). Le principe de spécialité (`pouvoirs-police.md` §4.3) impose de vérifier ce point **avant** de fonder quoi que ce soit sur la police générale.

**Autorité compétente.** À déterminer, et c'est la première variable à lever : **maire** (police générale + arrêtés municipaux de salubrité), **préfet** (RSD = arrêté préfectoral ; substitution L. 2215-1), **président d'EPCI** (si la police des déchets est transférée).

**Conflit de compétence détecté et signalé (obligation `analyse-situation.md` §3)** : **maire / président d'EPCI** sur le volet déchets, et **maire / préfet** sur le fondement RSD. Il n'est **pas** tranché ici : il conditionne à la fois la légalité de l'arrêté support et **l'habilitation de vos agents à verbaliser**. Voir §4 ci-dessous.

**Pouvoirs exerçables par vos agents.** Constatation par procès-verbal en qualité d'**APJA** (CPP art. 21, 2°), dans les limites de leur **habilitation textuelle** de constatation (CSI R. 511-1) — c'est précisément le point qui coince ici.

**Couple [risque / confiance] (`SKILL.md` §5.1)** : **[risque élevé / confiance à vérifier]**. L'enjeu n'est pas la difficulté de la question, c'est la **validité des PV** (un PV dressé hors habilitation est attaquable et expose le service), l'**exposition contentieuse** de la commune et l'atteinte portée à un administré. Plancher d'exigence imposé par la matrice : **citation de source + réserve explicite « à confirmer »**, abstention motivée sur ce qui n'est pas établi.

**Branches et objets mobilisés** : `reglementation-appliquee.md` §5.3 (salubrité) et §5.5 (environnement / brûlage) · `pouvoirs-police.md` §4.1 et §4.3 (titulaires, spécialité) · `liste-RSD.md` (récupération du texte départemental) · `controle-legalite.md` (si vous produisez un arrêté municipal) · générateurs `references/templates/pv-contravention.md` et `rapport-information.md`.

---

# 2. Garde-fou APJA — la limite est ici la **propriété privée**, pas l'acte d'enquête

La demande telle que formulée **ne dépasse pas** les pouvoirs APJA : je ne déclenche donc pas le STOP en tête de réponse. Mais les deux faits se déroulent **sur des propriétés privées**, et c'est là que la dérive est quasi systématique sur ce type de dossier. Donc, par anticipation :

```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

Ce bloc s'applique **dès que** la constatation suppose :
- de **pénétrer dans une propriété privée close, un jardin clos ou un domicile** sans le consentement libre de l'occupant : l'agent PM **ne réalise aucune perquisition, y compris en flagrance** (`SKILL.md` §5.2 ; CPP art. 56 : la perquisition de flagrance est réalisée par l'OPJ — au socle §2, `LEGIARTI000049778813`, en vigueur depuis le 26/06/2024, consulté le 2026-06-30) ;
- de **fouiller** un véhicule ou un contenant sur le dépôt, de **saisir** des pièces (courriers, factures) trouvées dans les déchets pour identifier l'auteur, ou d'**auditionner** formellement l'administré ou le propriétaire du terrain. La loi n° 2026-798 du 18/08/2026 a ouvert le recueil de déclarations par PV à certains APJA, mais **les agents de police municipale en sont expressément exclus** (CPP art. 21, version du 20/08/2026, au socle §2, `LEGIARTI000054725485`, consulté le 2026-09-14) : l'extension ne se transpose pas à la PM par analogie.

**Ce que vos agents font légitimement** : constater **depuis la voie publique** ou depuis un point où ils se trouvent régulièrement, décrire matériellement (dates, heures, récurrence, nature et volume des déchets, fumées, visibilité depuis l'espace public), photographier depuis l'extérieur, recueillir les **observations** du contrevenant lors du PV, et **rendre compte immédiatement** à l'OPJ ainsi qu'au maire (CPP art. 21-2, au socle §2, `LEGIARTI000006574893`, en vigueur depuis le 16/04/1999, consulté le 2026-06-30). Entrer sur le terrain avec l'**accord exprès de l'occupant** est possible, mais cet accord doit être tracé au PV : il ne se présume pas, et il ne transforme pas la visite en acte d'enquête.

**Relevé d'identité (CPP art. 78-6, au socle §2, `LEGIARTI000034114850`, en vigueur depuis le 02/03/2017, consulté le 2026-06-30)** — cité ici **pour être borné, pas pour être utilisé à l'aveugle** : il n'est ouvert que **pour une contravention que l'agent est habilité à verbaliser**. Tant que l'habilitation sur le fondement retenu n'est pas établie (§4 ci-dessous), **le relevé d'identité n'a pas de support** : dans ce cas, pas de rétention, constatations et compte rendu à l'OPJ, point final.

> ⚠️ **Alerte de vigueur portée au socle** : tous les articles du CPP cités ci-dessus portent sur Légifrance la mention d'abrogation par l'**ordonnance n° 2025-1091 du 19 novembre 2025** (`JORFTEXT000052650320`, consultée le 2026-09-14) **à compter du 01/01/2029**, avec renumérotation probable. Ils sont en vigueur aujourd'hui ; toute citation postérieure à 2028 devra viser la nouvelle numérotation.

---

# 3. Fait A — brûlage de déchets verts : sur quoi vos agents s'appuient

## 3.1 Le texte support est **local**, jamais national

Il n'existe **pas** d'article de code national que je puisse vous donner comme base de verbalisation directe du brûlage de déchets verts par un particulier. La prohibition est portée, selon les départements, par :

1. le **règlement sanitaire départemental (RSD)** — **arrêté du préfet**, acte réglementaire **local**, **non consolidé sur Légifrance** (sauf cas particulier de Paris, cf. §5). Fondement du pouvoir réglementaire sanitaire : **CSP art. L. 1311-1 et L. 1311-2**, modèle du **RSD type** de la circulaire du 9 août 1978 modifiée (*références citées par `liste-RSD.md`, sans identifiant Légifrance relevé au socle — **à confirmer en version consolidée***) ;
2. le cas échéant, un **arrêté du maire** pris au titre de la police générale de salubrité et de sécurité (CGCT art. L. 2212-2, au socle §1, `LEGIARTI000029946370`, en vigueur depuis le 22/12/2014, consulté le 2026-06-30) ;
3. le cas échéant, des **arrêtés préfectoraux complémentaires** (épisodes de pollution atmosphérique, sécheresse, risque incendie) qui ajoutent ou durcissent l'interdiction sur une période donnée — **non vérifiés dans cette session, à identifier département par département**.

**Ne jamais citer un numéro d'article du RSD de mémoire.** La numérotation et le contenu diffèrent d'un département à l'autre, et `reglementation-appliquee.md` §8 en fait explicitement un piège recensé : le RSD est un acte réglementaire **local**, pas un texte de niveau législatif. La même règle vaut pour la classe de contravention et le montant de l'amende : je ne les chiffre pas ici.

## 3.2 Le maillon qui décide de la validité du PV : **CSI R. 511-1**

C'est le point de fond corrigé en v1.0.5, et il est contre-intuitif.

> **CSI art. R. 511-1** (`LEGIARTI000028285997`, en vigueur depuis le 01/01/2014, **vérifié le 2026-09-17**, socle §9) habilite les agents de police municipale à constater par procès-verbal, notamment, les contraventions de **CP art. R. 610-5** relatives aux **arrêtés de police municipale pris par le maire ou par le préfet** (CGCT art. L. 2215-1, 1° à 3°).
>
> *Réserve de provenance* : **CP art. R. 610-5** n'a **pas** d'entrée propre au socle — il n'y figure que comme objet de l'entrée R. 511-1. Conformément à la règle « l'article voisin n'hérite pas du tag » (`SKILL.md` §5.3), je le cite **sous réserve, à confirmer en version consolidée**, et je ne donne **ni sa classe de contravention ni le montant de l'amende**.
> **CGCT art. L. 2215-1** est au socle §1 (`LEGIARTI000006390227`, en vigueur depuis le 07/03/2007, consulté le 2026-06-30).

Conséquences concrètes, dans l'ordre de solidité décroissante :

- **Base la plus sûre : un arrêté du maire.** Un arrêté municipal interdisant ou encadrant le brûlage à l'air libre sur le territoire communal entre **frontalement** dans le champ de R. 511-1 (« arrêtés de police municipale pris par le maire »). C'est la base que je vous recommande de sécuriser en priorité, et la seule sur laquelle je verbaliserais sans réserve préalable.
- **Base à vérifier : le RSD seul.** Le RSD est bien un **arrêté du préfet**, mais il est pris sur le fondement sanitaire du CSP, **et non** au titre des 1° à 3° de l'art. L. 2215-1 CGCT auxquels R. 511-1 renvoie. `reglementation-appliquee.md` §5.3 est explicite : **« ne pas présumer la constatation directe "sur le RSD" [...] sans vérification préalable »**. Je ne tranche pas ce point ici — **abstention motivée** (`SKILL.md` §5.3, réflexe 4) : à faire lever via `recherche-juridique` avant de bâtir une campagne de verbalisation sur ce seul fondement.
- **Base exclue en l'état : un arrêté du président d'EPCI.** L'habilitation générale de R. 511-1 ne vise **que** les arrêtés du maire ou du préfet ; elle **ne se transpose pas d'elle-même** à un arrêté du président d'EPCI (`pouvoirs-police.md` §4.1, **question ouverte non tranchée par cette version du skill**).

## 3.3 Ce que je vous recommande, concrètement

1. **Vérifiez d'abord si un arrêté municipal existe déjà** sur le brûlage / les feux à l'air libre. S'il existe : c'est votre base de verbalisation, sous réserve qu'il soit toujours en vigueur et régulièrement publié.
2. **S'il n'existe pas**, ne le faites pas signer en réflexe : contrôlez d'abord que la **police spéciale des déchets n'a pas été transférée** à l'EPCI (§4). Si elle l'a été, un arrêté du maire sur ce champ est **exposé à l'illégalité** (incompétence), et un PV fondé dessus tombe avec lui. Passage obligé par `controle-legalite.md` **avant** production, puis `references/templates/arrete-modele.md`.
3. **En parallèle**, récupérez le RSD de votre département **et ses arrêtés modificatifs** (§5) : le brûlage est justement l'un des sujets les plus souvent repris par arrêté modificatif.

---

# 4. Fait B — dépôt sauvage sur terrain privé : le point sensible

## 4.1 Volet pénal : **CP art. R. 633-6**, et l'habilitation n'est **pas** acquise

> **Code pénal art. R. 633-6** (`LEGIARTI000054196263`, en vigueur depuis le **05/06/2026**, **vérifié le 2026-09-17**, socle §9) sanctionne le **dépôt d'ordures ou de déchets hors des conditions fixées par l'autorité compétente**, contravention de **3ᵉ classe**.

C'est la qualification qui correspond matériellement à votre dépôt sauvage. **Mais** — et c'est le correctif de fond à retenir :

> **R. 633-6 ne figure pas dans la liste des contraventions que l'agent de police municipale peut constater au titre de CSI R. 511-1.** Sa constatation par vos agents **n'est pas présumée** : elle est **à vérifier au cas par cas** via `recherche-juridique` avant tout acte (`reglementation-appliquee.md` §5.3 et `references-verifiees.md` §9).

Traduction opérationnelle, sans détour :

- **Je ne vous confirme pas** que vos agents peuvent verbaliser directement sur R. 633-6. Tant que ce point n'est pas levé sur source officielle (texte d'habilitation, éventuelle habilitation spéciale prévue par le code de l'environnement), un PV dressé sur ce seul fondement est un **risque de nullité et d'exposition contentieuse**.
- **Corollaire immédiat** : pas d'habilitation établie ⇒ **pas de relevé d'identité** sur ce fondement (CPP art. 78-6, cité supra) ⇒ si l'auteur du dépôt est pris sur le fait et refuse de justifier son identité, vos agents **constatent et rendent compte à l'OPJ** (CPP art. 21-2), ils ne retiennent pas.
- **Ce qui reste solide dans tous les cas** : le **constat matériel circonstancié** et le **rapport au maire et à l'OPJ**. Un constat bien fait sert à la fois la voie pénale (transmise à l'OPJ/au parquet) et la voie administrative (§4.2), même si le PV de contravention n'est pas dressé par vos agents.

**À faire lever en priorité, avant toute campagne de verbalisation sur les dépôts sauvages** : l'habilitation exacte des agents PM en matière de dépôt de déchets — via `recherche-juridique`, en balise `[complet]` ou `[sourcé]`.

## 4.2 Volet administratif : la vraie voie efficace sur un terrain privé

Sur un **terrain privé**, la réponse la plus opérante n'est pas le PV, c'est la **police administrative des déchets** : mise en demeure du **producteur ou détenteur** de déchets de les éliminer, avec le régime de sanctions administratives attaché. Le texte support est **C. env. art. L. 541-3** (*cité par le socle §9 et par `pouvoirs-police.md` §4.1 uniquement comme objet du I.B de l'art. L. 5211-9-2 CGCT, **sans identifiant Légifrance propre relevé** — **à confirmer en version consolidée***, de même que la procédure exacte, les délais et les montants, que je **ne chiffre pas**).

Ce que cela change pour vous :
- **Ce n'est pas l'agent qui agit**, c'est l'**autorité de police** (`reglementation-appliquee.md` §5.3 : « les mesures de fond relèvent de l'autorité de police, pas de l'agent »). Vos agents **constatent et signalent** ; l'autorité met en demeure.
- **Quelle autorité ?** Le **maire**… **ou le président de l'EPCI** si les prérogatives de L. 541-3 lui ont été transférées. C'est le conflit de compétence à trancher **avant** d'engager la procédure : une mise en demeure signée par une autorité incompétente est annulable, et vous perdez des mois.
- **Cumul de procédures** : la voie administrative (mise en demeure, exécution d'office, sanctions administratives) et la voie pénale **se cumulent** sur les mêmes faits. `analyse-situation.md` §1, point 8 impose de le signaler : je le signale.
- Selon la **nature, le volume et les circonstances** du dépôt (déchets dangereux, usage d'un véhicule, caractère organisé), une **qualification pénale plus lourde** que la contravention peut exister en droit de l'environnement. Je **ne la cite pas** : elle n'est pas au socle, elle n'a pas été vérifiée dans cette session. Si les indices vont dans ce sens, la bascule est simple : **compte rendu à l'OPJ**, et pas de PV de contravention.

## 4.3 Conflit de compétence maire / président d'EPCI — à lever en premier

> **CGCT art. L. 5211-9-2** (`LEGIARTI000048850168`, version du 31/12/2023, socle §1, vérifié le 2026-06-30, recontrôlé les 2026-09-14 et **2026-09-17**) distingue **deux régimes qu'il ne faut pas traiter en bloc** :
>
> - **I.A — transfert de plein droit**, dont la **réglementation de la collecte des déchets ménagers** (si l'EPCI détient la compétence) : chaque maire peut **s'y opposer dans un délai de six mois** (III de l'article) ;
> - **I.B — transfert facultatif**, dont les **prérogatives de C. env. L. 541-3** en matière de déchets : décidé par **arrêté du représentant de l'État**, après **accord de tous les maires des communes membres et du président de l'EPCI** (IV) — pas d'automaticité, pas d'opposition à six mois.

Les trois questions à poser à votre DGS / au service juridique **cette semaine** :

1. L'EPCI détient-il la compétence **collecte/traitement des déchets** ? Si oui, la **réglementation de la collecte** a-t-elle basculé de plein droit au président (I.A), et **votre maire s'y est-il opposé** dans les six mois ?
2. Un **arrêté préfectoral** a-t-il transféré les prérogatives de **L. 541-3** au président (I.B) ?
3. Si la réponse est oui à l'une des deux : **sur quel arrêté vos agents verbaliseraient-ils ?** Si c'est un **arrêté du président d'EPCI**, l'habilitation de R. 511-1 **ne couvre pas ce cas** — question ouverte, non tranchée par le skill, à faire lever via `recherche-juridique` **avant tout acte fondé sur un tel arrêté**. **Ne jamais présumer l'habilitation.**

Rappel de fond (`pouvoirs-police.md` §4.1) : vos agents ne détiennent **aucun pouvoir de police propre**. Ils sont les exécutants des pouvoirs de police de l'autorité compétente — maire, préfet **ou** EPCI selon le cas. Identifier cette autorité n'est pas une formalité : c'est ce qui donne ou retire sa base à chaque PV.

---

# 5. Où trouver le texte exact applicable **dans votre département**

Le skill embarque un fichier dédié : **`references/liste-RSD.md`**, qui donne pour **96 des 101 départements** (métropole + DROM) un **lien de récupération officiel vérifié** — liens récupérés par appel d'outil le **2026-07-01**, aucun reconstitué de mémoire.

## 5.1 La méthode, en trois temps

**1. Deux niveaux d'agrégation officiels, dans cet ordre :**
- **ARS régionale** (`*.ars.sante.fr`) quand elle publie une page d'agrégation listant le RSD de chaque département de la région — **source à privilégier**. C'est le cas pour : Auvergne-Rhône-Alpes (12/12), Bretagne (4/4), Centre-Val de Loire (6/6), Grand Est (10/10), Hauts-de-France (5/5), Île-de-France (partiel), Normandie (5/5), PACA (6/6), et les ARS des DROM.
- **Préfecture** (`www.<departement>.gouv.fr`) lorsque l'ARS n'agrège pas : Bourgogne-Franche-Comté (8/8), Nouvelle-Aquitaine (10/12), Occitanie (13/13), Pays de la Loire (5/5).

**2. Vérifier la version et les modificatifs — c'est le point critique pour votre cas.** Un RSD peut avoir été **modifié par arrêtés successifs**, et `liste-RSD.md` signale nommément que **le bruit et le brûlage à l'air libre** sont les sujets les plus fréquemment repris par arrêté modificatif. Certains départements diffusent leur RSD **en plusieurs titres/fichiers** (Drôme en 9 titres, Puy-de-Dôme, Pas-de-Calais et Somme en 2 parties, Isère, Haute-Saône, Aveyron, Lot, Maine-et-Loire, Vendée, Pyrénées-Atlantiques par pages HTML) : un PDF unique peut ne pas contenir le titre qui vous intéresse.

**3. Cas particulier utile** : le **RSD de Paris (75)** est, lui, publié sur **Légifrance** — arrêté du 20 novembre 1979, `LEGITEXT000006070308` (*provenance : `liste-RSD.md`, lien vérifié le 2026-07-01*), avec une page de reprise sur `paris.fr`. C'est l'exception, pas la règle.

## 5.2 Les cinq cibles sans lien officiel en ligne

Au 2026-07-01, après recherche approfondie (archives, portails ARS, data.gouv, index national), **aucune source officielle en ligne** ne couvre : **2A (Corse-du-Sud)**, **2B (Haute-Corse)**, **33 (Gironde)**, **87 (Haute-Vienne)**, **972 (Martinique)**.
- Pour la Corse, un document RSD officiel existe sur l'ARS Corse (`/media/100726`) mais son **attribution 2A/2B reste indéterminée**, et l'accès automatisé renvoie 403 (probable géo-blocage — lisible depuis une IP française).
- **Voie de récupération pour ces cinq cibles** : **demande directe** à l'ARS (délégation départementale) ou à la préfecture. Le RSD est un acte public communicable au titre du **CRPA art. L. 311-1** (*référence citée par `liste-RSD.md` §4, sans identifiant Légifrance relevé au socle — **à confirmer en version consolidée***).
- **Règle d'usage DPM, non négociable** : pour ces cinq cibles, **ne jamais citer un RSD à partir d'une copie non officielle** (site associatif, docplayer, EPCI). Fonder l'acte sur la **version obtenue de la préfecture ou de l'ARS**, date et arrêtés modificatifs vérifiés. L'index national du **SNPCC** peut servir de point de départ pour retrouver une source, **jamais de source citable en acte**.

## 5.3 Ce qu'il me manque pour vous donner le lien exact

**Dites-moi votre département** (numéro suffit) et je vous donne en retour : le **lien de récupération officiel exact** (ARS ou préfecture), la **mention « en plusieurs titres »** s'il y a lieu, et la version signalée dans le fichier quand elle l'est (ex. Doubs : version modifiée 2022 ; Yonne : version 2002 ; Landes : 1985 ; Mayenne : actualisé 2005 ; Vienne : MAJ 2017 ; La Réunion : RSD 1992 + AP Bruit).

**Réserve de fraîcheur** : ces liens ont été vérifiés le **2026-07-01** et les URL ARS/préfecture changent lors des refontes de sites. En cas de lien mort, repartir de la page d'agrégation régionale ou d'une recherche « règlement sanitaire départemental <département> gouv.fr ».

---

# 6. Plan d'action opérationnel

**Avant toute verbalisation systématisée** (ordre impératif) :

| # | Action | Qui | Pourquoi |
|---|---|---|---|
| 1 | Récupérer le **RSD du département + ses arrêtés modificatifs** (§5) et isoler les articles brûlage / déchets | Vous / secrétariat | C'est le texte de fond, et il est local |
| 2 | Vérifier l'existence et la validité d'un **arrêté municipal** sur le brûlage à l'air libre | Vous / service juridique | Base de verbalisation la plus sûre au regard de R. 511-1 |
| 3 | Trancher le **transfert EPCI** de la police des déchets (L. 5211-9-2, I.A et I.B — §4.3) | DGS / juridique / préfecture | Conditionne la compétence de l'autorité **et** l'habilitation de vos agents |
| 4 | Faire lever par `recherche-juridique` : (a) la constatation par la PM de **CP R. 633-6** ; (b) la verbalisation **sur le seul RSD** au titre de R. 511-1 ; (c) le cas de l'arrêté du **président d'EPCI** | Vous, en balise `[complet]` | Trois points **non tranchés** par le socle — abstention motivée en l'état |
| 5 | **Seulement ensuite** : note de service fixant le fondement retenu et la conduite à tenir | Vous | Ne pas laisser chaque agent choisir sa base légale |

**Dès maintenant, sans attendre** : faire produire par les patrouilles des **constats circonstanciés** (dates, heures, récurrence, nature et volume, fumées, visibilité depuis l'espace public, identité du propriétaire du terrain si connue du cadastre), **depuis la voie publique**. Ce matériau sert les deux voies — pénale et administrative — quel que soit le fondement finalement retenu, et il est le socle de la mise en demeure du §4.2. Rappel : un PV de contravention régulier fait foi jusqu'à preuve contraire (**CPP art. 537**, au socle §2, `LEGIARTI000006576893`, en vigueur depuis le 01/04/2005, consulté le 2026-06-30) — raison de plus pour ne pas le fonder sur une habilitation incertaine.

---

# 7. Écrits mobilisables

Aucun écrit n'a été demandé explicitement : je ne produis donc pas de document, mais voici ce que je peux générer **dès que vous me donnez les éléments** (les générateurs du skill sont interactifs : je pose les questions **une à une**, et je ne comble **jamais** une donnée manquante — un document incomplet sortirait marqué `[INCOMPLET]` avec la liste précise des champs à fournir).

1. **Rapport d'information au maire** (`references/templates/rapport-information.md`) — le livrable le plus utile ici : signalement du dépôt sauvage pour déclencher la **mise en demeure** du détenteur (§4.2) et le signalement du brûlage récurrent. Champs à préparer : localisation exacte et références cadastrales, identité du propriétaire/occupant si connue, dates et heures des constats, nature et volume estimé des déchets, récurrence, suites déjà données, agents constatants.
2. **PV de contravention** (`references/templates/pv-contravention.md`) — **uniquement** une fois le fondement et l'habilitation sécurisés (§3.2 et §4.1). Je ne le génère pas sur une base incertaine.
3. **Arrêté municipal** interdisant/encadrant le brûlage (`references/templates/arrete-modele.md`) — **passage obligatoire par `controle-legalite.md` avant production** : vérification de la compétence (au regard du transfert EPCI), motivation en fait et en droit, publication, et vérification de l'obligation de transmission au contrôle de légalité. Acte réglementaire de police faisant grief : **voies et délais de recours** à mentionner (délai de droit commun de **deux mois**, **CJA art. R. 421-1**, au socle §8, `LEGIARTI000039807005`, en vigueur depuis le 01/01/2020, consulté le 2026-09-14).
4. **Note au maire** (`references/templates/note-maire-modele.md`) — pour arbitrer le conflit de compétence maire / président d'EPCI et acter la stratégie (pénal vs administratif). Recommandée si l'EPCI détient la compétence déchets.

---

# 8. Tableau de provenance

**Ce tableau n'est pas donné pour exhaustif au sens du §5.3** : le balayage part du corps du texte, et toute référence citée ci-dessus sans identifiant y figure explicitement comme **réservée**.

| Référence | Objet retenu | Version / vigueur | Identifiant | Provenance |
|---|---|---|---|---|
| **CSI R. 511-1** | Habilitation des agents PM à constater par PV les contraventions de CP R. 610-5 relatives aux arrêtés de police **du maire ou du préfet** (L. 2215-1, 1° à 3°) | depuis le 01/01/2014 | `LEGIARTI000028285997` | socle §9, **vérifié le 2026-09-17** |
| **CP R. 633-6** | Dépôt d'ordures/déchets hors conditions fixées par l'autorité compétente — 3ᵉ classe ; **non listé** par R. 511-1 | depuis le 05/06/2026 | `LEGIARTI000054196263` | socle §9, **vérifié le 2026-09-17** |
| **CP R. 610-5** | Contraventions aux arrêtés de police | — | **aucun identifiant propre au socle** | ⚠️ **réserve — à confirmer en version consolidée** (cité uniquement dans l'entrée R. 511-1 ; l'article voisin n'hérite pas du tag) |
| **CGCT L. 2212-2** | Objets de la police municipale, dont la **salubrité publique** | depuis le 22/12/2014 | `LEGIARTI000029946370` | socle §1, consulté le 2026-06-30 |
| **CGCT L. 2215-1** | Pouvoirs du préfet / substitution ; renvoi de R. 511-1 (1° à 3°) | depuis le 07/03/2007 | `LEGIARTI000006390227` | socle §1, consulté le 2026-06-30 |
| **CGCT L. 5211-9-2** | Transfert des polices spéciales au président d'EPCI : **I.A de plein droit** (collecte des déchets ménagers, opposition du maire à 6 mois) vs **I.B facultatif** (dont C. env. L. 541-3, arrêté préfectoral + accord de tous les maires) | version du 31/12/2023 | `LEGIARTI000048850168` | socle §1, vérifié le 2026-06-30, recontrôlé les 2026-09-14 et **2026-09-17** |
| **C. env. L. 541-3** | Police administrative des déchets (mise en demeure du producteur/détenteur) | — | **aucun identifiant propre au socle** | ⚠️ **réserve — à confirmer en version consolidée** (cité seulement comme objet du I.B de L. 5211-9-2) |
| **CSP L. 1311-1 et L. 1311-2** | Fondement du pouvoir réglementaire sanitaire du préfet (RSD) | — | **aucun identifiant relevé** | ⚠️ **réserve — à confirmer en version consolidée** (`liste-RSD.md`, vérifié le 2026-07-01) |
| **Circulaire du 9 août 1978 modifiée (RSD type)** | Modèle du RSD | — | **aucun identifiant relevé** | ⚠️ **réserve — à confirmer** (`liste-RSD.md`) |
| **RSD départemental** | Interdiction/encadrement du brûlage, dépôts, salubrité | **propre à chaque département** | **non consolidé sur Légifrance** | `liste-RSD.md` — liens officiels ARS/préfecture vérifiés le **2026-07-01** (96/101 départements) |
| **RSD de Paris (75)** | Arrêté du 20 novembre 1979 | — | `LEGITEXT000006070308` | `liste-RSD.md`, lien vérifié le 2026-07-01 |
| **CRPA L. 311-1** | Communicabilité du RSD sur demande | — | **aucun identifiant relevé** | ⚠️ **réserve — à confirmer** (`liste-RSD.md` §4) |
| **CPP art. 21 (2°)** | Qualité d'APJA des agents PM ; **PM exclue** de l'extension « recueil de déclarations » de la loi n° 2026-798 | version du 20/08/2026 | `LEGIARTI000054725485` | socle §2, consulté le 2026-09-14 — ⚠️ abrogation programmée au 01/01/2029 |
| **CPP art. 21-2** | Compte rendu immédiat à l'OPJ, information du maire | depuis le 16/04/1999 | `LEGIARTI000006574893` | socle §2, consulté le 2026-06-30 — ⚠️ abrogation 01/01/2029 |
| **CPP art. 78-6** | Relevé d'identité, **limité aux contraventions que l'agent est habilité à verbaliser** (cité ici pour être borné) | depuis le 02/03/2017 | `LEGIARTI000034114850` | socle §2, consulté le 2026-06-30 — ⚠️ abrogation 01/01/2029 |
| **CPP art. 56** | Perquisition de flagrance réalisée par l'**OPJ** ; aucun pouvoir de perquisition de l'agent PM (cité pour écarter) | depuis le 26/06/2024 | `LEGIARTI000049778813` | socle §2, consulté le 2026-06-30 — ⚠️ abrogation 01/01/2029 |
| **CPP art. 537** | Force probante du PV de contravention | depuis le 01/04/2005 | `LEGIARTI000006576893` | socle §2, consulté le 2026-06-30 — ⚠️ abrogation 01/01/2029 |
| **CJA R. 421-1** | Délai de recours contentieux de deux mois | depuis le 01/01/2020 | `LEGIARTI000039807005` | socle §8, consulté le 2026-09-14 |
| **Loi n° 2026-798 du 18/08/2026 (« Ripost »)** | Extension du recueil de déclarations aux APJA 1° à 1° ter, **hors PM** | en vigueur au 20/08/2026 | `JORFTEXT000054707332` | socle, alerte de vigueur, consultée le 2026-09-14 |
| **Ordonnance n° 2025-1091 du 19/11/2025** | Réécriture du CPP, abrogation différée au 01/01/2029 (report possible au 01/09/2030 par décret) | — | `JORFTEXT000052650320` | socle, alerte de vigueur, consultée le 2026-09-14 |

---

# 9. Abstentions motivées et points à faire lever

Je ne tranche pas, et je vous le dis franchement plutôt que de vous donner une réponse lisse :

1. **Vos agents peuvent-ils verbaliser CP R. 633-6 ?** → **Non établi.** R. 633-6 ne figure pas dans la liste de CSI R. 511-1. **Ne pas présumer.** À lever via `recherche-juridique` avant toute verbalisation sur ce fondement.
2. **Vos agents peuvent-ils verbaliser sur le seul RSD ?** → **Non établi non plus.** R. 511-1 vise les arrêtés de police du maire ou du préfet au titre de L. 2215-1, 1° à 3° ; le RSD relève d'un fondement sanitaire distinct. Vérification préalable requise (`reglementation-appliquee.md` §5.3).
3. **Et si l'arrêté support émane du président d'EPCI ?** → **Question ouverte, non tranchée par cette version du skill.** L'habilitation de R. 511-1 ne s'y transpose pas d'elle-même.
4. **Classe de contravention, montant d'amende, délais de mise en demeure, numéro d'article du RSD** → **non chiffrés ici**, conformément au socle : jamais de mémoire, toujours en version consolidée / sur le texte départemental à la date des faits.
5. **Qualifications pénales plus lourdes en droit de l'environnement** (nature/volume/circonstances du dépôt) → **hors socle, non vérifiées**. Si les indices vont dans ce sens : constat + compte rendu à l'OPJ, pas de PV.

**Cas journalisable (`SKILL.md` §7, point 12)** : oui. Ce dossier croise trois lacunes structurelles (habilitation R. 633-6, verbalisation sur RSD, arrêté de président d'EPCI) et mérite une entrée anonymisée au `JOURNAL.md` — je vous la rédige si vous le souhaitez, sans nommer ni agent ni administré.

---

**[risque élevé / confiance à vérifier]** — risque élevé en raison de la validité des PV et de l'exposition contentieuse de la commune ; confiance « à vérifier » parce que le maillon décisif (l'habilitation de constatation) n'est établi ni pour R. 633-6, ni pour la verbalisation sur le seul RSD. Plancher d'exigence appliqué : **citation de source + réserve explicite**, abstention sur ce qui n'est pas tranché.

**En une phrase** : le texte de fond est **local** (RSD départemental, à récupérer via `liste-RSD.md` — donnez-moi votre département et je vous sors le lien officiel exact), la base de verbalisation **la plus sûre est un arrêté du maire** couvert par CSI R. 511-1, le **dépôt sauvage se traite d'abord par la voie administrative** (mise en demeure du détenteur par l'autorité compétente), et **avant toute campagne de PV il faut lever trois points d'habilitation** — R. 633-6, RSD seul, arrêté de président d'EPCI.
