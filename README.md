# dpm-fpt — Système expert d'aide à la décision pour un Directeur de Police Municipale

Skill Claude destiné à un **Directeur de Police Municipale (DPM)** en
collectivité territoriale. Il cadre le besoin métier, oriente vers la bonne
base légale et le bon écrit, et sécurise les frontières de compétence
(APJA / OPJ, maire / préfet, métier / RH).

## Périmètre

Métier de la police municipale : pouvoirs de police, procédure pénale APJA,
réglementation appliquée, doctrine opérationnelle, continuum de sécurité,
armement, vidéoprotection, déontologie et données, pilotage et budget, écrits
professionnels.

**Hors périmètre** : RH statutaire des agents (→ `drh-fpt`), actes réservés à
l'OPJ (→ garde-fou APJA), droit étranger.

## Posture

**Hybride** : opérationnelle par défaut (rapide, orientée décision et écrit),
**vérifiée sur déclencheur** (matrice métier/juridique du `SKILL.md` §2.2). Toute
règle reposant sur un texte est vérifiée à la source officielle ou marquée « à
confirmer en version consolidée ».

## Architecture (4 couches)

1. **Decision Engine** — `references/analyse-situation.md` (routeur, appelé en premier).
2. **Branches métier** — 11 branches + 3 briques posture dans `references/`.
3. **Objets métier** — 8 fiches système expert dans `objets/`.
4. **Générateurs** — écrits interactifs dans `assets/`.

Dispositifs transverses (`SKILL.md` §5) : double échelle confiance × risque,
garde-fou APJA (« Hard Stop »), socle-sources autonome, délégation `drh-fpt`,
hiérarchie de co-activation.

## Structure

```
dpm-fpt/
├── SKILL.md                 # noyau : posture + dispositifs transverses
├── references/              # couches 1 et 2 (routeur + branches + postures + socle)
├── objets/                  # couche 3 (fiches système expert)
├── assets/                  # couche 4 (générateurs d'écrits)
├── tests/                   # cas de test + cas de co-activation
├── docs/adr/                # décisions d'architecture (ADR)
├── vault/                   # index Obsidian (maillage, non packagé)
├── CHANGELOG.md
├── JOURNAL.md
└── README.md
```

## Dépendances

- **`recherche-juridique`** (recommandé) — validateur de fond : vigueur des
  textes, format de citation traçable, triangulation des sources.
- **`drh-fpt`** (recommandé) — volet RH statutaire des agents PM.

## Apprentissage et versioning

Boucle `JOURNAL.md` (cas) → `CHANGELOG.md` (versions), décisions tracées dans
`docs/adr/`. Revue de rentrée au 1er septembre.

## Version

**v1.0.0 — première release stable.** Complet (4 couches), audité et **testé en
contexte frais** (26 cas + 5 co-activations, 3 runs ; sécurité transverse,
sourcing et bascule drh-fpt validés) : routeur, 11 branches + 3 postures +
socle, 8 objets, 5 générateurs, tests et vault d'index, plus un **socle de
références vérifiées sur Légifrance** (`references/references-verifiees.md`) et
les **liens de récupération du RSD par département** (`references/liste-RSD.md`,
96/101 départements vérifiés au 2026-07-01).
