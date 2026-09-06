---
tags: [skill/dpm-fpt, maillage]
---

# Maillage — skill dpm-fpt

> Carte des liens entre couches. Aucune recopie de contenu métier : uniquement
> les renvois (qui mobilise quoi). Navigation par besoin → [[index-dpm-fpt]].

## Nœuds transverses (traversent toutes les couches)

- **[[index-dpm-fpt#Couche 1 — Routeur|Garde-fou APJA]]** (`SKILL.md` §5.2,
  détaillé dans `references/penal-procedure.md` §4.5) — dès qu'un objet ou un
  générateur touche un acte hors pouvoir PM (garde à vue, audition formelle,
  perquisition, réquisition judiciaire), le **STOP** s'affiche avant tout autre
  contenu, puis le fondement d'une éventuelle contrainte est qualifié
  (53/73, 78-6, ou aucun). Objets concernés : [[#objet-accident|accident]],
  [[#objet-agent|agent]], [[#objet-commerce|commerce]],
  [[#objet-fourriere|fourrière]], [[#objet-manifestation|manifestation]],
  [[#objet-occupation-domaine-public|occupation domaine public]],
  [[#objet-police-chiens|police-chiens]], [[#objet-videoprotection|vidéoprotection]]
  (8/8 — seul `objets/_gabarit-objet.md` n'est pas concerné, c'est un
  méta-document). Articulation avec l'écrit : `references/ecrits-professionnels.md`
  §2 (le test du garde-fou précède toujours le choix de l'écrit).
- **Frontière `drh-fpt`** (`SKILL.md` §5.4) — bascule du **constat** (gardé
  dans `dpm-fpt`, via `references/conformite-deontologie-donnees.md` et
  `references/rh-specificites-pm.md`) vers la **procédure** disciplinaire ou
  statutaire (déléguée à `drh-fpt`). Explicitement mobilisée par
  [[#objet-agent|objets/agent.md]] ; règle de bascule rappelée transversalement
  par `references/retex.md` (constat déontologique individuel → bascule dès
  ouverture de procédure).
- **Socle-sources / matrice métier-juridique** (`SKILL.md` §2.2,
  `references/socle-sources-verification.md`) — conditionne, pour chaque
  branche et chaque objet, l'obligation de vérification de source avant
  conclusion. S'applique uniformément, non répété ci-dessous par objet.

## Objets → branches mobilisées → générateurs appelés

### <a id="objet-commerce"></a>`objets/commerce.md` — Débits de boissons et commerces réglementés

- Branches : [[index-dpm-fpt#Couche 2 — Branches métier (11) + 3 briques posture|pouvoirs-police]], [[index-dpm-fpt#Couche 2 — Branches métier (11) + 3 briques posture|penal-procedure]], [[index-dpm-fpt#Couche 2 — Branches métier (11) + 3 briques posture|reglementation-appliquee]]
- Posture : [[index-dpm-fpt#Couche 2 — Branches métier (11) + 3 briques posture|controle-legalite]] (fermeture administrative = acte faisant grief)
- Générateurs : `pv-contravention`, `rapport-information`, `rapport-mise-a-disposition`, `arrete-modele`, `note-maire-modele`

### <a id="objet-manifestation"></a>`objets/manifestation.md` — Manifestation / événement

- Branches : pouvoirs-police, penal-procedure, reglementation-appliquee, doctrine-operationnelle, continuum-partenariats, armement-equipements
- Posture : controle-legalite
- Générateurs : pv-contravention, rapport-information, arrete-modele, note-maire-modele

### <a id="objet-occupation-domaine-public"></a>`objets/occupation-domaine-public.md` — Occupation du domaine public

- Branches : pouvoirs-police, reglementation-appliquee
- Posture : controle-legalite (arrêtés de mise en demeure / retrait = actes faisant grief)
- Générateurs : rapport-information, arrete-modele, note-maire-modele

### <a id="objet-agent"></a>`objets/agent.md` — Agent PM

- Branches : penal-procedure, doctrine-operationnelle, armement-equipements, continuum-partenariats, conformite-deontologie-donnees, rh-specificites-pm
- Transverse : frontière drh-fpt (constat déontologique → bascule procédure)
- Générateurs : rapport-information, note-maire-modele

### <a id="objet-accident"></a>`objets/accident.md` — Accident

- Branches : penal-procedure, reglementation-appliquee, continuum-partenariats, conformite-deontologie-donnees
- Générateurs : pv-contravention, rapport-information, rapport-mise-a-disposition, note-maire-modele

### <a id="objet-fourriere"></a>`objets/fourriere.md` — Fourrière

- Branches : pouvoirs-police, penal-procedure, reglementation-appliquee
- Posture : controle-legalite
- Générateurs : pv-contravention, rapport-information, note-maire-modele

### <a id="objet-videoprotection"></a>`objets/videoprotection.md` — Vidéoprotection (cas d'usage)

- Branches : penal-procedure, continuum-partenariats, conformite-deontologie-donnees, **videoprotection** (branche dédiée couche 2, même thématique que l'objet — l'objet est le cas d'usage opérationnel, la branche est le fond réglementaire)
- Générateurs : note-maire-modele

### <a id="objet-police-chiens"></a>`objets/police-chiens.md` — Police des chiens dangereux

- Branches : pouvoirs-police, penal-procedure, reglementation-appliquee
- Posture : controle-legalite
- Générateurs : pv-contravention, rapport-information, rapport-mise-a-disposition, arrete-modele, note-maire-modele

## Générateurs → branche pilote → posture de contrôle

Les 5 générateurs de la couche 4 (`references/templates/*.md`) sont **tous** pilotés par la
même branche et soumis à la même posture pour les actes faisant grief :

| Générateur | Branche pilote | Posture (avant production si acte faisant grief) |
|---|---|---|
| `references/templates/pv-contravention.md` | `references/ecrits-professionnels.md` | garde-fou APJA (`penal-procedure.md`) en amont du choix d'écrit |
| `references/templates/rapport-information.md` | `references/ecrits-professionnels.md` | garde-fou APJA en amont |
| `references/templates/rapport-mise-a-disposition.md` | `references/ecrits-professionnels.md` | uniquement si une route 53/73 ou 78-6 est établie ; jamais par le seul effet du STOP |
| `references/templates/arrete-modele.md` | `references/ecrits-professionnels.md` | `references/controle-legalite.md` obligatoire (acte faisant grief : motivation, voies de recours, contrôle de légalité) |
| `references/templates/note-maire-modele.md` | `references/ecrits-professionnels.md` | `references/controle-legalite.md` si la note porte une décision défavorable |

Articulation posture après production / en anticipation contentieuse :
`references/contentieux.md` (stress-test adversarial avocat / juge / préfet,
complémentaire de `controle-legalite.md`, pas redondant). Suivi qualité et
apprentissage post-intervention : `references/retex.md` (n'intervient jamais
en amont de la production, pas de base légale propre).

## Briques posture — articulation entre elles

- `controle-legalite.md` → relit **avant** signature (grille du contrôle
  préfectoral : compétence, procédure, motivation, base légale).
- `contentieux.md` → stress-test **après** ou en simulation préventive, angle
  élargi (avocat requérant, juge administratif, préfet déféré).
- `retex.md` → analyse **post-intervention**, pilotage et apprentissage, sans
  fondement de pouvoir propre ; renvoie toujours à la branche métier mobilisée
  au moment des faits pour le fond légal.

## Couverture du maillage

8 objets sur 8 mobilisent au moins une branche métier et au moins un
générateur ; 7 sur 8 mobilisent une posture explicite (seul
`occupation-domaine-public` n'en appelle aucune dans son fil type). Tous les 5
générateurs convergent vers la même branche pilote (`ecrits-professionnels.md`)
et vers le même nœud transverse de garde-fou APJA en amont.
