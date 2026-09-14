# dpm-fpt — Système expert d'aide à la décision pour un Directeur de Police Municipale

Skill Codex/Claude destiné à un **Directeur de Police Municipale (DPM)** en
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
4. **Générateurs** — modèles Markdown interactifs dans
   `references/templates/`.

Dispositifs transverses (`SKILL.md` §5) : double échelle confiance × risque,
garde-fou APJA (« Hard Stop »), socle-sources autonome, délégation `drh-fpt`,
hiérarchie de co-activation.

## Structure

```
dpm-fpt/
├── SKILL.md                 # noyau : posture + dispositifs transverses
├── agents/openai.yaml       # métadonnées d'interface Codex
├── references/              # couches 1 et 2 (routeur + branches + postures + socle)
│   └── templates/           # couche 4 (modèles d'écrits)
├── objets/                  # couche 3 (fiches système expert)
├── scripts/                 # validation et packaging reproductibles
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

**v1.0.4 — revue de rentrée 2026 et audit complet (2026-09-14).** Rapport :
`docs/audit/2026-09-14-audit-v1.0.3.md`. Ce que la version change :

- **Socle recontrôlé** identifiant par identifiant (62/62 sur Légifrance) ;
  deux versions nouvelles depuis la date consignée, toutes deux issues de la
  **loi n° 2026-798 du 18 août 2026** : art. 21 CPP (le recueil de
  déclarations par PV est étendu aux APJA des 1° à 1° ter, **sans les agents
  de police municipale**) et CSP L. 3332-15 (fermeture des débits de boissons
  pour atteinte à l'ordre public : 3 mois, 6 en réitération). **17 références**
  citées dans les branches sans figurer au socle y sont portées (§8), dont
  R. 325-14 du code de la route, les référés du CJA et l'art. 803 CPP.
- **Garde-fou APJA** : trois fissures refermées — rétention sur simple
  soupçon et « mise à disposition automatique » dans l'objet accident,
  exception « fouille de sécurité » jamais définie (désormais bornée à l'art.
  L. 511-1 CSI, palpation consentie), menottage sans fondement de rétention
  (art. 803 CPP).
- **Fourrière** : le skill affirmait que la PM « ne décide jamais » la mise en
  fourrière ; l'art. R. 325-14 la fait prescrire par l'OPJ **ou par le chef de
  la police municipale** (sauf véhicule volé, non identifié ou faussement
  immatriculé). Branche et objet corrigés.
- **Frontière RH** étendue aux couches 3 et 4 (objet agent, protection
  fonctionnelle), description du skill rendue discriminante vis-à-vis de
  `drh-fpt` et `dpo-ct`, gabarits et pointeurs remis d'équerre.

**Dernier score de suite — campagne complète `claude-v1.0.2-r3`** (achevée le
2026-09-06, 28 cas, skill lu depuis le dépôt) : **26 RÉUSSITE / 0 DEMI /
2 ÉCHEC**, seuil de release atteint (≥ 25/28 et 0 échec sur les six cas
critiques). Les deux échecs (15, 21) tenaient à des références hors socle,
corrigées en v1.0.3. La v1.0.4 est mesurée par la campagne `r4`
(`tests/runs/claude-v1.0.4-r4/`, protocole `r3` reconduit) ; son score est
consigné dans `tests/bareme-cas-de-test.md` et dans le `CHANGELOG.md`.

Historique complet des campagnes et des versions : `CHANGELOG.md`,
`tests/bareme-cas-de-test.md`. Le package d'exécution est limité aux fichiers
nécessaires (`SKILL.md`, `agents/openai.yaml`, `references/`, `objets/`).
