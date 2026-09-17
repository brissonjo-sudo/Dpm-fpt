# Réponse — Excès de vitesse simple constaté au cinémomètre : quel écrit et quelles mentions obligatoires ?

## 0. Cadrage rapide (sortie du routeur `analyse-situation.md`)

- **Qualification des faits** : contravention au code de la route (excès de
  vitesse « simple », donc hors délit de très grand excès / récidive),
  constatée **directement** par l'agent au moyen d'un appareil de contrôle
  homologué (cinémomètre).
- **Police mobilisée** : police spéciale de la circulation routière (pas la
  police générale du maire en tant que telle) — pouvoir de **constatation**
  exercé par l'agent en qualité d'**agent de police judiciaire adjoint
  (APJA)**, art. 21 du Code de procédure pénale (CPP).
- **Autorité compétente / destinataire final** : officier du ministère
  public (OMP) / juridiction de police pour le traitement de la
  contravention — pas le maire à ce stade (le maire n'est destinataire que
  du compte rendu en cas de mesure de contrainte associée, ce qui n'est pas
  le cas ici).
- **Conflit de compétence** : aucun conflit maire/préfet/OPJ identifié dans
  les faits décrits — simple constatation, aucune mesure sur la personne.
- **Garde-fou APJA (§5.2 `SKILL.md`)** : **non déclenché**. Rien dans
  l'énoncé n'indique une garde à vue, une audition formelle, une
  perquisition ou une réquisition judiciaire, ni une appréhension (art. 53 +
  73 CPP) ou un relevé d'identité contraint (art. 78-6 CPP). Pas de STOP à
  afficher. Un excès de vitesse « simple » (hors délit) ne requiert par
  lui-même aucune mesure de contrainte sur la personne.
- **Frontière RH (`drh-fpt`)** : non concernée, aucune question statutaire
  ou disciplinaire.
- **[risque / confiance]** : **élevé / stable sur le principe, à vérifier au
  cas d'espèce** — l'enjeu est la **valeur probante** du PV (art. 537 CPP)
  et la **compétence de constatation** de l'agent PM sur ce type précis
  d'infraction (vitesse par cinémomètre), qui est un point technique
  particulièrement disputé en contentieux routier.

## 1. Écrit à produire

Application de la logique de décision `references/ecrits-professionnels.md`
§5.1 :

1. Aucune route de mise à disposition (art. 53+73 ou 78-6 CPP) n'est
   établie → pas de rapport de mise à disposition.
2. L'agent a **constaté personnellement** une contravention dans le cadre
   de son pouvoir de verbalisation → **PV de contravention**, sous réserve
   de vérifier que le texte d'incrimination attribue bien à l'agent PM le
   pouvoir de constater ce type précis de contravention par PV (point 2 ci-
   dessous).
3. Aucun acte réservé à l'OPJ n'est en cause → pas de garde-fou à opposer.

**→ Générateur à utiliser : `references/templates/pv-contravention.md`**
(piloté par `references/ecrits-professionnels.md` §4, §5, §6, §10).

## 2. Point de vigilance propre à ce cas : la compétence de constatation par cinémomètre

C'est le point le plus sensible de ce dossier, et il conditionne la valeur
probante renforcée de l'art. 537 CPP (matrice §2.2 du `SKILL.md` : « condition
d'exercice » et « étendue d'un pouvoir de police » → vérification
obligatoire).

- **Art. L. 130-4 du code de la route** — vérifié sur Légifrance le
  28/07/2026 (consultation directe de la page, identifiant
  `LEGIARTI000045072417`, en vigueur depuis le 26/01/2022) : cet article
  énumère 15 catégories d'agents habilités, **sans préjudice de la
  compétence générale des OPJ/APJ**, à constater par procès-verbal les
  contraventions de la partie réglementaire du code de la route se
  rattachant à la sécurité et à la circulation routières. Les **agents de
  police judiciaire adjoints** (dont la police municipale, art. 21, 2° CPP)
  figurent au **11e point** de cette énumération.
- **Réserve légale intégrée à l'article** : « *La liste des contraventions
  que chaque catégorie d'agents mentionnée ci-dessus est habilitée à
  constater est fixée par décret en Conseil d'État* ». Autrement dit,
  l'appartenance de principe des APJA/PM à L. 130-4 **ne suffit pas** : il
  faut que le **décret d'application** inclue bien l'excès de vitesse par
  cinémomètre dans la liste des contraventions constatables par les APJA/PM
  — ce décret et son contenu précis **n'ont pas été vérifiés dans cette
  session** et doivent l'être avant de considérer le PV comme
  définitivement recevable (⚠️ à confirmer en version consolidée,
  `reglementation-appliquee.md` n'aborde pas ce point de détail).
- Si ce texte d'application ne confère pas cette compétence précise à
  l'agent, la conséquence pratique (§5.2 `ecrits-professionnels.md`) est
  que la force probante renforcée de l'art. 537 CPP **n'est pas acquise**,
  et l'écrit pertinent pourrait basculer vers un simple **rapport
  d'information** au lieu d'un PV.
- Recommandation opérationnelle : avant transmission, faire confirmer par
  le service (ou `recherche-juridique`) que (a) l'agent est habilité pour
  cette catégorie précise de contravention, et (b) que le **cinémomètre
  utilisé est homologué et a fait l'objet des vérifications périodiques
  requises** (contrôle métrologique annuel par organisme indépendant),
  point de preuve technique distinct de la compétence juridique, à faire
  figurer explicitement dans le PV.

## 3. Mentions obligatoires pour que le PV soit recevable

D'après `references/templates/pv-contravention.md` §2 (grille de
vérification) et `ecrits-professionnels.md` §5.3, à consigner **toutes**,
ou à défaut marquer `[INCOMPLET]` :

**Socle commun**
- Identité et qualité du rédacteur (+ n° d'agrément préfectoral /
  assermentation si exigé).
- Date et heure précises de la constatation.
- **Lieu précis** de l'infraction (voie, portion de voie exacte, sens de
  circulation, commune) — exigence renforcée : une localisation imprécise
  fait perdre au PV sa force probante renforcée.
- Faits matériellement constatés, formulés au plus près de l'observation
  directe (vitesse relevée, sans interprétation).
- Qualification retenue avec le texte d'incrimination précis (renvoi à
  `reglementation-appliquee.md` pour le fond — cette branche ne tranche pas
  elle-même la qualification exacte, ex. classe de contravention selon le
  dépassement constaté).
- Identité du mis en cause si connue (conducteur identifié ou
  identification par immatriculation), témoins le cas échéant.
- Observations recueillies du contrevenant, si l'agent les a recueillies
  (faculté, pas obligation, art. 21 CPP).
- Suites données et destinataire(s) du document.

**Mentions propres au PV de contravention avec appareil de contrôle**
- **Texte exact de l'incrimination** (visa précis, pas générique).
- **Référence à l'appareil de contrôle homologué** (type de cinémomètre,
  n° de série, référence d'homologation, **date de la dernière vérification
  périodique** et organisme vérificateur indépendant) — point de preuve
  technique indispensable en cas de contestation, distinct de la question
  de compétence traitée au §2 ci-dessus.
- Préciser si l'heure et la vitesse relevées proviennent **directement de
  l'appareil** ou d'une observation distincte de l'agent, et la cohérence
  entre les deux.
- **Mention de la notification/de l'avis** au contrevenant selon la
  procédure applicable localement (PV remis sur place, avis différé,
  verbalisation électronique).
- **Confirmation explicite** que le texte d'incrimination (et son décret
  d'application, §2) attribue bien à l'agent PM le pouvoir de constatation
  par PV pour ce type de contravention — sinon, signaler que la force
  probante renforcée n'est pas acquise.

**Rappel de valeur probante à joindre au PV** (`ecrits-professionnels.md`
§5.2, art. 537 CPP — *vérifié sur Légifrance le 30/06/2026, réaligné le
01/07/2026, identifiant `LEGIARTI000006576893`, en vigueur depuis le
01/04/2005* ; **abrogation programmée au 01/01/2029 par l'ordonnance
n° 2025-1091 du 19/11/2025**, sans effet à la date des faits actuelle) : le
PV, sous réserve qu'il émane d'un agent auquel le texte d'incrimination
attribue le pouvoir de constater par procès-verbal, **fait foi jusqu'à
preuve contraire**, laquelle ne peut être rapportée que par écrit ou par
témoins ; cette force probante ne porte que sur la **matérialité des faits
constatés personnellement**, et suppose une **localisation précise**
(exigence jurisprudentielle constante sur l'art. 537 CPP, à vérifier au cas
par cas via `recherche-juridique` avant citation en acte).

## 4. Statut de l'écrit

Ce cas n'ayant pas encore de données concrètes fournies (dates, lieu,
identité, référence de l'appareil), aucun brouillon nominatif n'est produit
ici : la recommandation opérationnelle est d'ouvrir le générateur
interactif `references/templates/pv-contravention.md` et de dérouler ses
questions **une à une** (qui / quand / où / pourquoi / qualification /
témoins / suites), en marquant `[INCOMPLET — préciser : <champ>]` tout champ
manquant plutôt que de le supposer, notamment le n° d'homologation et la
date de vérification périodique du cinémomètre, et le circuit local de
transmission à l'OMP.

## 5. Transmission

PV de contravention → circuit applicable localement : verbalisation
électronique (flux dédié OMP) ou circuit papier vers le tribunal de police
/ OMP territorialement compétent — modalités et délais exacts **à confirmer
en version consolidée et selon l'organisation locale**, aucun délai chiffré
avancé de mémoire. Le PV n'est **pas** un acte administratif faisant grief :
il ne requiert ni motivation CRPA, ni voies et délais de recours, ni
transmission au contrôle de légalité (art. L. 2131-2 CGCT) —
`references/templates/pv-contravention.md` §7.

## 6. Renvois de fichiers du skill mobilisés

- Routeur : `references/analyse-situation.md`
- Branche pilote : `references/ecrits-professionnels.md` (§4, §5.1, §5.2,
  §5.3, §9, §10)
- Fond du pouvoir APJA : `references/penal-procedure.md` §4.1 (art. 21 CPP)
- Fond réglementaire routier : `references/reglementation-appliquee.md`
  §5.1 (ne détaille pas la compétence spécifique « cinémomètre » — point à
  compléter/vérifier)
- Socle de sources : `references/references-verifiees.md` (§2 CPP, §4 code
  de la route) et `references/socle-sources-verification.md` (méthode, non
  reproduite ici)
- Générateur d'écrit : `references/templates/pv-contravention.md`
- Non mobilisé : `references/controle-legalite.md` (PV = pas un acte
  administratif faisant grief), `drh-fpt` (aucun sujet RH statutaire)

## 7. Auto-vérification (`SKILL.md` §7)

1. Garde-fou APJA testé → non déclenché, pas de STOP.
2. Conflit de compétence → aucun détecté, rien à signaler.
3. Lignes « Oui » de la matrice §2.2 vérifiées : étendue du pouvoir de
   constatation (L. 130-4, vérifié le 28/07/2026) et valeur probante
   (art. 537 CPP, vérifié le 30/06/2026/réaligné le 01/07/2026) ; **reste à
   vérifier** : le décret en Conseil d'État précisant si l'excès de vitesse
   par cinémomètre figure dans la liste des contraventions constatables par
   les APJA/PM (non vérifié dans cette session).
4. Références datées avec leur statut de vérification exact — aucun
   identifiant inventé.
5. Police spéciale (circulation routière) et autorité compétente (OMP/
   juridiction de police) correctement identifiées.
6. [risque / confiance] indiqué (§0).
7. Acte faisant grief : non applicable (PV, pas un arrêté).
8. Frontière RH : non concernée.
9. Conflit de normes : aucun détecté.
10. Écrit demandé : orientation donnée vers le générateur interactif,
    aucun brouillon nominatif halluciné en l'absence de données.
11. Aucune donnée personnelle exposée.
12. Cas journalisable : **oui, proposé** — la compétence exacte de
    constatation de l'excès de vitesse par cinémomètre par les agents PM
    (décret d'application de l'art. L. 130-4 non vérifié dans cette
    session) mériterait une entrée `JOURNAL.md` pour consolidation lors de
    la prochaine revue de rentrée.
