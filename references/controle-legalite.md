# Brique posture — Contrôle de légalité (v0.1.0)

> Brique transverse, pas une branche métier. Structure adaptée du gabarit
> `_gabarit-branche.md` : on garde le bloc Périmètre/Exclusions, l'arbre de
> traitement, la grille de contrôle et la checklist ; on retire les sections
> sans objet pour une posture (pas de « procédures et délais » dédiées, pas de
> sous-domaines métier). Appelée **avant toute production d'acte** via
> `references/templates/` (arrêté, note au maire, règlement) — voir `SKILL.md` §6 et
> `analyse-situation.md` §4.

## Périmètre / Exclusions

- **Périmètre** : auditer un arrêté, une note, un règlement ou une décision
  **avant production**, en se plaçant en **posture de juge administratif**
  (contrôle a priori, comme si l'acte était déjà déféré).
- **Exclusions** : la **recherche de jurisprudence** elle-même (identification,
  triangulation, autorité d'une décision) → `recherche-juridique` (Mode B). Le
  **contenu de fond** de chaque police (pouvoirs, base légale détaillée) →
  branche métier concernée (`pouvoirs-police.md`,
  `reglementation-appliquee.md`, etc.), simple pointeur ici. L'**anticipation
  des faiblesses contentieuses après production** (mémoire en défense, risque
  de recours) → `contentieux.md`. Les **statistiques et le suivi qualité** des
  actes → `retex.md`.

---

## 1. Questions couvertes

- « Cet arrêté tient-il devant le juge administratif ? »
- « Ai-je la bonne base légale, la bonne autorité, la bonne motivation ? »
- « Cette mesure est-elle proportionnée ? »
- « Cet acte doit-il être transmis au contrôle de légalité ? Sous quel délai
  produit-il effet ? »
- « Quelles voies et délais de recours mentionner ? »
- « La procédure préalable (consultation, contradictoire, publicité) a-t-elle
  été respectée ? »

---

## 2. Arbre de traitement

`projet d'acte → identifier la nature de l'acte (§4) → dérouler la grille de
contrôle (§5, dans l'ordre) → lever les variables manquantes (§3) →
décision : produire / corriger / abstenir (§6) → vérification socle-sources
(§7) → écrit corrigé ou liste de réserves (§8)`

Ne jamais transmettre un acte « tel quel » pour rédaction tant qu'un point de
la grille (§5) n'est pas levé ou explicitement assumé comme risque accepté et
signalé au commanditaire (maire/DGS).

---

## 3. Variables à lever

- **Nature de l'acte** : police générale (CGCT) / police spéciale (laquelle)
  / acte de gestion interne / acte RH (→ frontière `drh-fpt`, SKILL.md §5.4).
- **Caractère individuel ou réglementaire** — conditionne le régime de
  motivation (CRPA, §5.3) et le mode de publicité.
- **Acte faisant grief ou non** — seuls les actes faisant grief appellent
  motivation renforcée + voies de recours.
- **Autorité signataire réelle** — maire en personne, ou délégataire
  (adjoint, DGS) : vérifier l'existence et la régularité de la délégation
  (arrêté de délégation publié, en vigueur, non retiré).
- **Urgence** — conditionne la procédure contradictoire applicable (un acte
  pris en urgence peut alléger certaines formalités, à vérifier au cas par
  cas) et le mode d'entrée en vigueur (CGCT, §5.5).
- **Catégorie de l'acte au regard de la liste de transmission obligatoire**
  (CGCT — voir §5.5) : transmissible ou non.

---

## 4. Grille de contrôle a priori — posture « juge administratif »

Dérouler **dans cet ordre**. Un contrôle de légalité, en pratique, vérifie
souvent dans cette séquence ; le juge administratif raisonne de même
(moyens de légalité externe avant moyens de légalité interne).

### 4.1 Compétence (légalité externe)
- **Auteur de l'acte** : l'autorité signataire détient-elle le pouvoir
  exercé ? Police générale → maire (CGCT, base à vérifier branche
  `pouvoirs-police.md`) ; police spéciale → vérifier le titulaire exact
  (parfois le préfet, parfois le maire au nom de l'État) ; risque de
  **conflit de compétence** → renvoyer à `analyse-situation.md` §3 et
  `pouvoirs-police.md`.
- **Délégation** : si signataire ≠ maire, l'arrêté de délégation de
  signature/fonction couvre-t-il précisément cet objet et cette date ?
  Délégation publiée et non retirée ?
- **Compétence territoriale** : l'acte reste-t-il dans les limites du
  territoire communal (sauf police spéciale à portée différente) ?
- **Incompétence négative** : l'autorité ne s'est-elle pas crue liée alors
  qu'elle disposait d'un pouvoir d'appréciation (ex. pouvoir de police jamais
  discrétionnaire à 100 %, motivation stéréotypée révélatrice) ?

### 4.2 Procédure (légalité externe)
- **Consultations obligatoires** préalables identifiées et tracées (CST,
  commissions, organismes consultatifs selon l'objet — propre à chaque police
  spéciale, à vérifier branche concernée) ?
- **Procédure contradictoire** : la personne visée par une mesure
  individuelle défavorable a-t-elle été mise en mesure de présenter des
  observations, sauf urgence ou exception légale (à vérifier au cas par cas
  selon le texte applicable — CRPA, dispositions relatives à la procédure
  contradictoire) ?
- **Formalités de publicité** : affichage, publication au recueil des actes
  administratifs, notification individuelle — selon la nature de l'acte.
- **Signature et date** : acte daté, signé, original conservé.

### 4.3 Base légale (légalité interne)
- **Texte fondateur identifié et cité avec précision** (article exact, pas de
  visa générique type « vu le CGCT » sans article).
- **Police générale vs spéciale** : la police spéciale, quand elle existe,
  prime en principe sur la police générale pour le même objet — sauf
  circonstances locales particulières justifiant une mesure complémentaire du
  maire (principe à vérifier au cas par cas, jurisprudence administrative
  constante sur le sujet → `recherche-juridique` si contesté).
- **Absence de détournement de pouvoir** : le motif réel correspond-il à la
  finalité légale du texte invoqué (ordre public, salubrité, sécurité,
  tranquillité — pas un motif étranger, ex. opportunité politique ou
  financière déguisée) ?
- **Erreur de droit / erreur de fait** : les faits visés dans les visas
  sont-ils exacts et matériellement établis ?

### 4.4 Motivation (CRPA)
- **Motivation en fait et en droit obligatoire** pour les décisions visées à
  l'art. **L. 211-2 du Code des relations entre le public et l'administration
  (CRPA)** *(vérifié sur Légifrance le 2026-06-30)* — notamment : mesures de
  police, sanctions, décisions restreignant l'exercice d'une liberté
  publique, refus d'autorisation, retrait/abrogation d'une décision créatrice
  de droits.
- **Test pratique** : la motivation permet-elle à un tiers de comprendre,
  sans autre pièce, pourquoi cette mesure précise a été prise (et pas une
  mesure moins contraignante) ? Une motivation stéréotypée ou recopiée d'un
  autre acte est un risque d'annulation.
- **Décisions implicites et exceptions** : certaines décisions favorables ou
  de portée générale échappent à l'obligation — vérifier le régime exact
  avant d'affirmer une dispense.

### 4.5 Proportionnalité (police administrative)
- **Principe (jurisprudence constante, illustrée par l'arrêt de principe)** :
  toute mesure de police administrative doit être **nécessaire, adaptée et
  proportionnée** au trouble à l'ordre public ; l'autorité doit retenir la
  mesure la **moins attentatoire aux libertés** parmi celles permettant
  d'atteindre l'objectif.
  ```
  CE, Sect., 19 mai 1933, Benjamin, Lebon p. 541
  Ratio decidendi : une mesure de police administrative doit être
  proportionnée à la menace pour l'ordre public ; l'autorité de police
  doit choisir la mesure la moins attentatoire aux libertés permettant
  d'atteindre le but d'intérêt général.
  ```
  *(Référence d'arrêt de principe reprise telle que citée dans
  `Drh-fpt/references/...` et la doctrine constante ; numéro de requête non
  attribué à l'époque — la fiche complète, le contexte et les décisions
  d'application relèvent de `recherche-juridique`.)*
- **Test pratique en 3 questions** :
  1. La mesure est-elle **strictement nécessaire** (trouble réel, actuel ou
     suffisamment caractérisé) ?
  2. Est-elle **limitée dans le temps et dans l'espace** au strict besoin
     (pas d'interdiction générale et absolue quand une mesure ciblée suffit) ?
  3. Existe-t-il une **mesure alternative moins restrictive** qui atteindrait
     le même but ? Si oui, et qu'elle n'a pas été envisagée ni écartée
     explicitement, risque élevé d'annulation pour disproportion.
- **Interdiction générale et absolue** : signal d'alerte fort — quasi
  systématiquement censurée si une mesure plus ciblée était possible
  (principe constant, déclinaisons à vérifier selon l'objet via
  `recherche-juridique` en cas de doute).

### 4.6 Voies et délais de recours
- Toute décision faisant grief doit mentionner les **voies de recours**
  (recours gracieux, hiérarchique, contentieux) et le **délai** applicable, et
  l'autorité ou la juridiction compétente.
- L'**omission** de cette mention ne rend pas l'acte illégal mais **empêche le
  délai de recours contentieux de courir** contre l'administré — risque
  pratique majeur (contestation possible bien au-delà du délai usuel).

### 4.7 Transmission au contrôle de légalité
- Vérifier si l'acte figure dans la **liste des actes soumis à transmission
  obligatoire** au représentant de l'État (préfet ou sous-préfet
  d'arrondissement) — art. **L. 2131-2 du CGCT** *(vérifié sur Légifrance le
  2026-06-30 : inclut notamment les actes réglementaires pris par les
  autorités communales dans les matières où la loi leur attribue compétence,
  et les décisions individuelles ; régime issu de l'ordonnance n° 2021-1310
  du 7 octobre 2021, entrée en vigueur 1er juillet 2022 — liste précise et
  seuils à reconfirmer en version consolidée selon l'objet exact de l'acte)*.
- **Entrée en vigueur / caractère exécutoire** : un acte communal devient
  exécutoire de plein droit dès qu'il a fait l'objet d'une **publicité**
  (publication/affichage/notification) et, pour les actes de la liste
  art. L. 2131-2, dès sa **transmission** au représentant de l'État —
  art. **L. 2131-1 du CGCT** *(vérifié sur Légifrance le 2026-06-30)*. Tant
  que la transmission requise n'est pas faite, l'acte n'est **pas
  exécutoire**, même signé et publié.
- **Délai de transmission des décisions individuelles** : un délai court
  s'applique à compter de la signature (ordre de grandeur : 15 jours — **à
  confirmer en version consolidée**, l'art. exact étant fonction de la nature
  de la décision).
- **Actes non transmissibles** : certains actes (gestion interne, actes de
  droit privé, actes pris au nom de l'État) sont hors champ — art.
  **L. 2131-4 du CGCT (à confirmer en version consolidée)** ; ne pas
  sur-transmettre par excès de prudence sans vérifier, mais en cas de doute,
  transmettre reste la posture la plus sûre.
- **Déféré préfectoral** : le préfet dispose d'un délai pour défèrer l'acte
  au tribunal administratif s'il l'estime illégal, et peut assortir le
  recours d'une demande de suspension — détail procédural et délais exacts à
  vérifier selon la nature de l'acte (`recherche-juridique` si contentieux
  engagé → `contentieux.md`).

---

## 5. Renvois (pas de duplication)

- Base légale de fond par police → `pouvoirs-police.md`,
  `reglementation-appliquee.md`.
- Frontière APJA / actes réservés à l'OPJ → garde-fou `SKILL.md` §5.2,
  `penal-procedure.md`.
- Conflit de compétence maire/préfet/OPJ → `analyse-situation.md` §3.
- Jurisprudence de fond (recherche, triangulation, autorité d'une décision
  autre que le principe de proportionnalité ci-dessus) → `recherche-juridique`
  Mode B.
- Anticipation des faiblesses après édiction de l'acte, stratégie de défense
  en cas de recours → `contentieux.md`.
- Production effective de l'écrit (gabarit interactif) → `references/templates/`, pilotée
  par `ecrits-professionnels.md`.
- Frontière RH (acte individuel concernant un agent : sanction, refus
  d'avancement) → `drh-fpt` dès que la procédure RH statutaire est en jeu
  (SKILL.md §5.4) ; ce fichier reste compétent pour le contrôle de légalité
  de l'acte en tant que tel si demandé en miroir.

---

## 6. Déclencheurs de vérification

Appliquer le socle-sources (matrice §2.2 du `SKILL.md`) systématiquement,
car le contrôle de légalité porte par construction sur des lignes « Oui » :
- toute **base légale** visée (article exact, pas de mémoire) ;
- toute **mention d'obligation de motivation** (CRPA) ;
- toute **liste d'actes transmissibles** (CGCT) et tout **délai** de
  transmission ;
- toute **référence jurisprudentielle** autre que le principe constant cité
  en §4.5 (la fiche d'arrêt complète, sa portée actuelle et ses déclinaisons
  → `recherche-juridique`) ;
- toute **délégation de signature** : vérifier son existence réelle, pas la
  présumer.

---

## 7. Pièges & confusions fréquentes

1. Citer « vu le CGCT » sans article précis — non auditable, à corriger
   systématiquement.
2. Confondre **illégalité** (acte annulable) et **absence de caractère
   exécutoire** (transmission manquante) — deux risques distincts, à
   contrôler séparément.
3. Omettre les **voies et délais de recours** sur un acte individuel
   défavorable — n'invalide pas l'acte mais neutralise le délai de recours
   contre l'administré, donc fragilise durablement la collectivité.
4. Prendre une **mesure générale et absolue** quand une mesure ciblée dans le
   temps ou l'espace suffirait — premier motif d'annulation en police
   administrative.
5. Invoquer la police générale du maire sur un objet couvert par une **police
   spéciale** sans justifier de circonstances locales particulières.
6. Présumer une **délégation de signature** valide sans vérifier sa
   publication et son périmètre exact.
7. Traiter un acte de **gestion RH individuelle** (sanction, refus
   d'avancement) comme une simple question de contrôle de légalité générique
   sans renvoyer à `drh-fpt` pour le volet procédure statutaire.
8. Confondre le test de proportionnalité (nécessité/adaptation/mesure la
   moins attentatoire) avec un simple contrôle de l'existence d'un motif —
   le juge contrôle aussi l'**intensité** de la mesure.

---

## 8. Données / références à vérifier

- **CRPA**, art. **L. 211-2** (motivation des décisions défavorables) —
  *vérifié sur Légifrance le 2026-06-30* ; vérifier au cas par cas les
  articles connexes (procédure contradictoire, décisions implicites) en
  version consolidée.
- **CGCT**, art. **L. 2131-1** (caractère exécutoire, publicité, transmission)
  et **L. 2131-2** (liste des actes soumis à transmission obligatoire) —
  *vérifiés sur Légifrance le 2026-06-30* ; régime issu de l'ordonnance
  n° 2021-1310 du 7 octobre 2021 (entrée en vigueur 1er juillet 2022) — à
  reconfirmer en version consolidée pour le détail des seuils et catégories
  selon l'objet exact de l'acte.
- **CGCT**, art. **L. 2131-4** (actes non transmissibles) — à confirmer en
  version consolidée.
- **CE, Sect., 19 mai 1933, *Benjamin*** (principe de proportionnalité des
  mesures de police) — requêtes n° **17413** et **17520**, **Lebon p. 541**,
  `CETATEXT000007636694`, **vérifié sur Légifrance le 2026-09-06** et porté au
  socle (`references-verifiees.md` §7) : **le citer avec cette provenance**,
  jamais de mémoire. Ses déclinaisons jurisprudentielles récentes relèvent de
  `recherche-juridique`.
- **Délai de transmission des décisions individuelles** (ordre de grandeur
  15 jours) — à confirmer en version consolidée, article exact selon nature
  de la décision.
- Toute base légale de **police spéciale** invoquée dans l'acte audité — à
  vérifier branche par branche (`pouvoirs-police.md`,
  `reglementation-appliquee.md`).

---

## 9. Écrits & livrables

Cette brique ne produit pas d'écrit en propre. Elle **conditionne** la
production de tout acte via `references/templates/` :
- **Arrêté** (`references/templates/arrete-modele.md`) — passer la grille §4 avant
  rédaction ; intégrer motivation + voies de recours si acte faisant grief.
- **Note au maire** (`references/templates/note-maire-modele.md`) — signaler les points de
  fragilité identifiés par la grille, même si la décision finale appartient
  au maire.
- **Règlement / décision** — même grille, adaptée au caractère réglementaire
  (motivation allégée pour les actes non visés par l'art. L. 211-2 CRPA, mais
  base légale et proportionnalité toujours contrôlées).

**Sortie attendue de l'audit** : soit l'acte est prêt à produire, soit une
**liste de réserves précises** (point de la grille § concerné, correction
demandée) est restituée avant toute rédaction, sans halluciner la correction
si une donnée manque (cf. SKILL.md §6, cas `[INCOMPLET]`).

---

## 10. Double échelle [risque / confiance]

| Point de contrôle | Risque | Confiance |
|---|---|---|
| Compétence / délégation de signature | Élevé | Stable (principe), à vérifier (fait) |
| Motivation CRPA (existence de l'obligation) | Élevé | Stable |
| Contenu précis de la motivation (suffisance) | Élevé | À vérifier (casuistique) |
| Proportionnalité | Élevé à critique selon l'atteinte aux libertés | Jurisprudentiel (principe stable, application casuistique) |
| Transmission au contrôle de légalité (obligation) | Élevé | Stable (principe), à vérifier (liste exacte / délai) |
| Voies et délais de recours | Moyen à élevé | Stable |
| Base légale de police spéciale invoquée | Élevé | À vérifier branche par branche |

---

## 11. Checklist de branche

1. Nature de l'acte qualifiée (individuel/réglementaire, faisant grief ou
   non) ?
2. Autorité signataire et délégation éventuelle vérifiées (existence,
   publication, périmètre) ?
3. Base légale citée avec article précis, police générale/spéciale
   distinguée ?
4. Procédure préalable (consultation, contradictoire, publicité) tracée ?
5. Motivation en fait et en droit conforme à l'art. L. 211-2 CRPA si l'acte
   est visé ?
6. Test de proportionnalité (nécessité / adaptation / mesure la moins
   attentatoire) explicitement passé, avec alternative envisagée et écartée
   si pertinent ?
7. Voies et délais de recours mentionnés si acte faisant grief ?
8. Obligation de transmission au contrôle de légalité vérifiée (liste
   art. L. 2131-2 CGCT) et délai identifié ?
9. Conflit de compétence (maire/préfet/OPJ) écarté ou signalé
   (`analyse-situation.md` §3) ?
10. Frontière RH respectée (acte statutaire individuel → `drh-fpt`) ?
11. Toute référence numérotée porte sa réserve « à confirmer en version
    consolidée » ou la mention « vérifié sur Légifrance le JJ/MM/AAAA » ?
12. Couple **[risque / confiance]** restitué pour les points fragiles avant
    transmission du livrable ?

[risque : élevé par défaut sur cette brique — elle conditionne la validité
d'actes faisant grief / confiance : stable sur les principes (compétence,
motivation, proportionnalité, transmission), à vérifier sur les valeurs
chiffrées (délais, seuils, liste exacte des actes transmissibles)]
