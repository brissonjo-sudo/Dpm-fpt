# Brique posture — Contentieux (anticipation adversariale)

> Structure adaptée de `_gabarit-branche.md` (brique posture transverse, pas une
> branche métier complète). Les valeurs datées et identifiants non vérifiés ne
> sont jamais donnés de mémoire : seules les **règles** figurent ici, avec la
> consigne de vérifier la version en vigueur.

## Périmètre / Exclusions

- **Périmètre** : anticiper les **faiblesses d'une décision** (arrêté, mesure
  de police, acte individuel) selon trois angles adversariaux — **l'avocat**
  du requérant, **le juge administratif**, **le préfet** (déféré). Objectif :
  identifier les points de fragilité **avant** la production de l'acte ou
  avant un contentieux déclaré, et proposer des consolidations.
- **Exclusions** : la **recherche de jurisprudence** elle-même (identification,
  triangulation, fond d'un arrêt) → `recherche-juridique` (Mode B). Le
  **contrôle de légalité préalable** d'un acte avant sa production (posture
  « relecture interne ») → `controle-legalite.md`. Le **retour d'expérience**
  post-intervention (hors contentieux) → `retex.md`. Le fond des pouvoirs de
  police mobilisés → `pouvoirs-police.md`. La procédure pénale et le garde-fou
  APJA → `penal-procedure.md` (`SKILL.md` §5.2).

> **Articulation avec `controle-legalite.md`** : `controle-legalite.md` relit
> l'acte **avant** sa signature avec la grille du contrôle préfectoral
> (compétence, procédure, motivation, base légale). `contentieux.md` se
> positionne **après** — ou en simulation préventive — sur l'acte déjà pris ou
> sur le point d'être pris, en élargissant l'angle à l'avocat requérant et à
> l'office du juge. Les deux briques sont complémentaires, pas redondantes :
> utiliser `controle-legalite.md` pour fabriquer l'acte, `contentieux.md` pour
> le stress-tester.

---

## 1. Questions couvertes

- « Cette décision (arrêté, mesure de police, refus, sanction) tient-elle si
  elle est attaquée ? »
- « Quels moyens un avocat soulèverait-il contre cet acte ? »
- « Le préfet peut-il déférer cet acte ? Sur quel fondement, dans quel délai ? »
- « Quel est l'office du juge administratif sur ce type de mesure
  (contrôle normal, restreint, entier) ? »
- « Faut-il craindre un référé (suspension, liberté) ? »
- « Comment consolider l'acte avant ou après contestation ? »

---

## 2. Arbre de traitement

`acte ou décision identifié → qualifier sa nature (réglementaire / individuel,
faisant grief ou non) → dérouler les trois angles (§5) → identifier les
points de fragilité (§6) → vérifier les références mobilisées (§7) →
proposer les consolidations (§8) → livrable (§9)`

Ne pas conclure « l'acte est solide » sans avoir testé explicitement les trois
angles. Une décision qui « semble correcte » peut être fragile sur un seul
moyen suffisant à l'annulation.

---

## 3. Variables à lever

- **Nature de l'acte** : réglementaire (arrêté de portée générale) ou
  individuel (faisant grief à une personne identifiée). Conditionne les
  délais, les voies de recours, et l'intérêt à agir des tiers.
- **Auteur et compétence** : qui a signé (maire, président d'EPCI,
  délégataire) ? Délégation de signature/fonction régulière et publiée ?
- **Date de l'acte et formalités de publicité** : transmission au contrôle de
  légalité, affichage, notification — point de départ des délais de recours.
- **Base légale invoquée** : police générale (CGCT) ou police spéciale
  (texte propre) ? Norme correctement visée dans les visas ?
- **Existence d'un précédent comparable** (jurisprudence locale ou nationale
  connue) → si recherche de fond nécessaire, renvoyer à
  `recherche-juridique` (Mode B), ne pas l'improviser ici.
- **Urgence du contexte** (mesure restrictive de liberté en cours
  d'exécution) → déclenche l'hypothèse référé (§5.2).

---

## 4. Règles métier — cadrage des trois angles

### 4.1 Distinction structurante : légalité externe / légalité interne
Tout moyen contentieux contre un acte administratif se classe en deux
familles. Tester systématiquement les deux, dans cet ordre (le juge examine
souvent l'externe en premier) :

- **Légalité externe** : compétence de l'auteur, procédure suivie (consultation
  préalable obligatoire, avis requis, contradictoire), forme de l'acte
  (motivation écrite quand exigée, visas).
- **Légalité interne** : existence et exactitude matérielle des faits, base
  légale, exacte qualification juridique des faits, erreur de droit,
  détournement de pouvoir, proportionnalité de la mesure au but poursuivi
  (police administrative).

### 4.2 Office du juge administratif — intensité du contrôle
L'intensité varie selon la nature de la mesure. Ne jamais traiter tous les
actes de police avec le même niveau d'exigence :

- **Contrôle normal** : régime de droit commun pour la plupart des mesures de
  police administrative générale (légalité, exactitude matérielle des faits,
  qualification juridique, proportionnalité).
- **Contrôle restreint** (erreur manifeste d'appréciation) : certaines
  décisions où le juge laisse une marge d'appréciation à l'autorité
  administrative — champ à vérifier au cas par cas, ne pas présumer.
- **Contrôle entier de proportionnalité** : mesures de police restrictives de
  libertés fondamentales (réunion, manifestation, circulation, couvre-feu
  local) — le juge vérifie que la mesure est nécessaire, adaptée et
  proportionnée, et qu'aucune mesure moins attentatoire ne permettait
  d'atteindre le même but d'intérêt général (logique du contrôle de
  proportionnalité des mesures de police, jurisprudence constante — fond à
  vérifier via `recherche-juridique`).

> Ne jamais affirmer le niveau de contrôle applicable à une mesure précise
> sans vérification : c'est une ligne « Oui » de la matrice §2.2 du
> `SKILL.md` (étendue d'un pouvoir / jurisprudence).

### 4.3 Angle de l'avocat requérant
Logique adversariale : chercher activement la faille, pas seulement
constater la conformité apparente.
- Examiner d'abord la **légalité externe** (souvent le terrain le plus
  rentable pour un requérant : vice de procédure ou de compétence emporte
  l'annulation sans débat sur le fond).
- Tester l'**intérêt à agir** du requérant potentiel (administré visé,
  voisin, association agréée, contribuable local selon l'acte).
- Tester le **moyen de fond le plus probable** compte tenu de la nature de la
  mesure (proportionnalité pour une mesure de police restrictive, erreur de
  qualification pour une sanction, défaut de base légale pour un acte
  innovant).
- Identifier si un **référé** est probable en parallèle du recours au fond
  (§4.4) — accroît la pression temporelle sur l'administration.

### 4.4 Angle du juge administratif
- Qualifier le **recours pour excès de pouvoir** (légalité) par opposition au
  plein contentieux (indemnitaire, contractuel) — la nature du recours
  conditionne les pouvoirs du juge.
- Délai de recours contentieux de droit commun : **deux mois** à compter de
  la notification ou de la publication de la décision attaquée (art.
  **R. 421-1** du code de justice administrative — *vérifié sur Légifrance le
  2026-06-30*). Vérifier le point de départ exact (notification individuelle
  vs publication/affichage) et les éventuelles prorogations.
- **Référé-suspension** (art. **L. 521-1** CJA — *vérifié sur Légifrance le
  2026-06-30*) : suspension de l'exécution de l'acte si la requête au fond est
  recevable, l'**urgence** est caractérisée, et il existe un moyen propre à
  créer, en l'état de l'instruction, un **doute sérieux** sur la légalité de
  l'acte. Toujours associé à un recours principal en annulation.
- **Référé-liberté** (art. **L. 521-2** CJA — *vérifié sur Légifrance le
  2026-06-30*) : mesure utile en cas d'**atteinte grave et manifestement
  illégale** à une liberté fondamentale dans l'exercice d'un pouvoir de
  l'administration ; juge statuant en **48 heures** ; appel devant le Conseil
  d'État dans un délai resserré (à confirmer en version consolidée). Hypothèse
  pertinente pour une mesure de police restrictive de liberté en cours
  d'exécution (manifestation interdite, fermeture administrative, mesure
  individuelle privative).
- Le juge peut **annuler**, ou substituer/réformer selon la nature du
  contentieux ; l'administration peut être condamnée aux frais irrépétibles —
  champ exact à vérifier.

### 4.5 Angle du préfet (déféré préfectoral)
- Le préfet **n'est pas une partie comme une autre** : son pouvoir de déféré
  est un contrôle de légalité a posteriori, distinct du recours d'un tiers.
- **Fondement et délai** : le préfet défère au tribunal administratif les
  actes mentionnés à l'article **L. 2131-2** du CGCT qu'il estime contraires à
  la légalité, dans un délai de **deux mois** suivant leur **transmission**
  (art. **L. 2131-6** CGCT — *vérifié sur Légifrance le 2026-06-30*). Ce délai
  court à compter de la **transmission au contrôle de légalité**, pas
  nécessairement de la publication ou de la notification — distinction à ne
  jamais confondre avec le délai de droit commun (§4.4).
- Le préfet **informe sans délai** l'autorité communale de son déféré et lui
  communique les illégalités invoquées (art. L. 2131-6 CGCT).
- Le préfet peut assortir son déféré d'une **demande de suspension** ;
  celle-ci est accordée si un moyen paraît, en l'état de l'instruction,
  propre à créer un **doute sérieux** quant à la légalité de l'acte attaqué
  (art. L. 2131-6 CGCT — même texte, régime spécifique au déféré, à ne pas
  confondre avec le référé-suspension de droit commun de l'art. L. 521-1 CJA,
  même si le standard du « doute sérieux » est commun aux deux mécanismes).
- Pour les actes mentionnés à l'article **L. 2131-3** CGCT (catégorie
  spécifique — à confirmer en version consolidée), le préfet peut être saisi
  par un **tiers lésé** et déférer l'acte dans les deux mois suivant cette
  saisine — voie indirecte à connaître : un administré sans intérêt à agir
  direct, ou hors délai de droit commun, peut tenter de faire déférer l'acte
  par ce canal.
- Vérifier systématiquement si l'acte entre dans la **liste des actes soumis
  à transmission obligatoire** (art. L. 2131-2 CGCT — à confirmer en version
  consolidée) : un acte non soumis à transmission n'ouvre pas le délai de
  déféré de la même manière et expose différemment.

---

## 5. Procédure d'anticipation (méthode des trois angles)

Pour toute décision testée, dérouler dans l'ordre :

1. **Angle avocat (§4.3)** — lister les moyens externes puis internes les
   plus probables ; noter celui qui présente le risque d'annulation le plus
   élevé.
2. **Angle juge administratif (§4.4)** — qualifier le contrôle applicable
   (§4.2), le délai de recours, et l'hypothèse référé.
3. **Angle préfet (§4.5)** — vérifier si l'acte est soumis à transmission
   obligatoire, le délai de déféré, et le risque de demande de suspension
   préfectorale (le standard du doute sérieux étant moins exigeant pour le
   préfet qu'une démonstration au fond).
4. **Synthèse des points de fragilité** (§6) — croiser les trois angles ;
   un même vice (ex. défaut de motivation) peut être exploité par les trois
   acteurs simultanément.
5. **Consolidations proposées** (§8).

---

## 6. Pièges & confusions fréquentes

1. Confondre le **délai de droit commun** (deux mois à notification/publication,
   art. R. 421-1 CJA) et le **délai de déféré préfectoral** (deux mois à
   **transmission**, art. L. 2131-6 CGCT) : deux points de départ différents,
   deux acteurs différents.
2. Traiter le **référé-suspension** (art. L. 521-1 CJA, urgence + doute
   sérieux, toujours accessoire à un recours au fond) comme équivalent au
   **référé-liberté** (art. L. 521-2 CJA, atteinte grave et manifestement
   illégale à une liberté fondamentale, autonome, jugé en 48 heures) : régimes,
   conditions et délais distincts.
3. Oublier que le **préfet peut suspendre via le déféré** assorti d'une
   demande de suspension (art. L. 2131-6 CGCT), avec un effet souvent plus
   rapide et plus dissuasif qu'un recours de tiers.
4. Limiter l'analyse à la **légalité interne** (le fond, la proportionnalité)
   en oubliant la **légalité externe** (compétence, procédure, forme) qui est
   statistiquement le terrain le plus fréquent d'annulation.
5. Affirmer le **niveau de contrôle du juge** (normal / restreint / entier)
   sans vérification pour le type de mesure en cause : c'est une ligne « Oui »
   de la matrice §2.2 (étendue d'un pouvoir, jurisprudence).
6. Confondre **acte réglementaire** et **acte individuel** : régime de
   recours, d'intérêt à agir et de retrait/abrogation différents.
7. Ignorer qu'un acte **non transmis** au contrôle de légalité, alors qu'il
   devait l'être, reste fragile sans que le délai de déféré n'ait pu courir
   normalement — situation à signaler, pas à ignorer.
8. Confondre cette brique avec une **recherche de jurisprudence de fond** :
   tout précédent jurisprudentiel précis à mobiliser dans une argumentation
   relève de `recherche-juridique` (Mode B), pas d'une reconstitution de
   mémoire ici.

---

## 7. Déclencheurs de vérification

Appliquer le socle-sources (`SKILL.md` §5.3, `socle-sources-verification.md`)
dès que :
- un **délai de recours ou de déféré** est annoncé pour une décision réelle ;
- le **niveau de contrôle du juge** applicable à une mesure précise est
  affirmé ;
- la **liste des actes soumis à transmission obligatoire** (art. L. 2131-2
  CGCT) conditionne la réponse ;
- un **précédent jurisprudentiel** est invoqué pour étayer un moyen → renvoyer
  à `recherche-juridique` (Mode B) plutôt que de le citer de mémoire ;
- une **réforme récente** du contentieux administratif ou du contrôle de
  légalité est en cause.

---

## 8. Consolidations type (à adapter, jamais génériques sans contexte)

- **Vice de compétence** : vérifier et joindre la délégation de
  signature/fonction publiée et en vigueur à la date de l'acte.
- **Vice de procédure** : vérifier la consultation préalable obligatoire
  (avis, commission) et en conserver la trace écrite.
- **Défaut de motivation** (acte faisant grief) : motivation en fait et en
  droit, explicite, propre à l'espèce — jamais une formule type sans
  rattachement aux faits.
- **Défaut de proportionnalité** : documenter pourquoi une mesure moins
  attentatoire aux libertés n'aurait pas suffi à atteindre le but d'intérêt
  général poursuivi.
- **Défaut de base légale** : vérifier le visa exact (police générale vs
  police spéciale, texte applicable au moment des faits) avant signature.
- **Risque de déféré** : anticiper la transmission diligente au contrôle de
  légalité et, pour un acte sensible, solliciter un échange préalable avec
  les services préfectoraux plutôt que de découvrir le déféré après coup.

Pour la fabrication de l'acte en amont avec cette grille → `controle-legalite.md`.

---

## 9. Écrits & livrables

- **Note d'analyse contentieuse** (interne, avant ou après contestation) :
  synthèse des trois angles, points de fragilité hiérarchisés, consolidations
  proposées, délais en cours.
- **Mémoire en défense** (élément de cadrage uniquement) : ce skill prépare le
  diagnostic et les éléments factuels ; la rédaction du mémoire relève de
  l'avocat de la collectivité — ne pas se substituer à lui sur la stratégie
  contentieuse.
- Pas de générateur dédié dans `references/templates/` à ce stade : produire la note
  d'analyse au format libre, en respectant la structure de cette brique.

---

## 10. Double échelle [risque / confiance]

- **Risque** : par défaut **élevé** dès qu'une décision réelle est testée
  (exposition contentieuse, validité de l'acte) ; **critique** si l'acte est
  déjà en cours d'exécution et restrictif de liberté (hypothèse référé-liberté).
- **Confiance** :
  - **Stable** : distinction légalité externe/interne, existence des trois
    voies (recours de tiers, déféré, référés), logique du doute sérieux.
  - **À vérifier** : délais exacts, liste des actes soumis à transmission,
    niveau de contrôle applicable à une mesure précise, tout numéro d'article
    non vérifié dans la session.
  - **Jurisprudentiel** : application concrète de la proportionnalité à une
    mesure donnée → `recherche-juridique` (Mode B) avant toute affirmation
    ferme.

---

## 11. Checklist de branche

1. Les **trois angles** (avocat, juge, préfet) ont-ils été déroulés, pas
   seulement un ou deux ?
2. **Légalité externe** testée avant/à côté de la légalité interne ?
3. **Niveau de contrôle du juge** identifié sans présomption non vérifiée ?
4. **Délai de droit commun** (R. 421-1 CJA) et **délai de déféré**
   (L. 2131-6 CGCT) distingués, avec leurs points de départ respectifs ?
5. Hypothèse **référé** (suspension art. L. 521-1 CJA / liberté art. L. 521-2
   CJA) testée si la mesure est restrictive de liberté ou en cours
   d'exécution ?
6. Acte vérifié au regard de la **liste de transmission obligatoire**
   (art. L. 2131-2 CGCT) ?
7. Toute référence numérotée porte la réserve « à confirmer en version
   consolidée » ou la mention « vérifié sur Légifrance le JJ/MM/AAAA » ?
8. Aucun précédent jurisprudentiel de fond invoqué sans renvoi à
   `recherche-juridique` ?
9. Consolidations proposées **rattachées aux faits**, pas génériques ?
10. Couple **[risque / confiance]** indiqué ?

[risque / confiance] : risque élevé à critique selon le contexte (§10) —
confiance mixte : architecture stable, valeurs et précédents à vérifier
systématiquement avant usage en acte ou en mémoire.
