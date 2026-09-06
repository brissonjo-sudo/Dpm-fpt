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

**v1.0.3 — la jurisprudence entre au socle.** Le garde-fou APJA distingue trois
issues : appréhension sous les conditions cumulatives des articles 53 et 73 du
CPP, relevé d'identité selon l'article 78-6, ou absence de pouvoir de rétention.
Aucune perquisition n'est attribuée à l'agent PM, même en flagrance.

**Dernier score de suite — la campagne complète `claude-v1.0.2-r3`**, achevée le
2026-09-06 sur les 28 cas, **mesure la v1.0.2** et donne **26 RÉUSSITE /
0 DEMI-RÉUSSITE / 2 ÉCHEC** : le seuil de release est atteint pour la première
fois (≥ 25/28 et **0 échec sur les six cas critiques**, dont le cas 14 qui
échouait auparavant).

Les deux échecs (15 et 21) tenaient à des références **hors socle** —
jurisprudence citée par son nom d'usage, article voisin d'un article tracé —
citées sans réserve dans des réponses par ailleurs intégralement sourcées. La
**v1.0.3 corrige cette cause à la racine** : l'arrêt *Benjamin* et l'art. 122-5
du code pénal sont portés au socle vérifié, la règle de provenance couvre
explicitement les décisions de justice, et l'auto-vérification du sourcing
devient un **test à charge** sur le texte produit. Cette version étant
postérieure à la mesure, une campagne `r4` reste requise pour la scorer.

La campagne `claude-v1.0.1-r2` a été **rejouée les 2026-08-07/08** : sa première
exécution avait été conduite sans que le répondant dispose réellement des skills
invocables, et mesurait donc le modèle nu, pas le skill. Résultat de la
ré-exécution : **10 RÉUSSITE / 12 DEMI-RÉUSSITE / 6 ÉCHEC**, dont un échec sur
un cas critique (14). Le sourcing, cause des échecs précédents, est désormais
tenu sur 26/28 ; la cause dominante devient le renvoi de fichier non nommé
(12 DEMI sur 12), désormais **requalifié en critère non éliminatoire**.

Enseignement central, traité par cette version : **rendre `drh-fpt` invocable
supprimait le réflexe de bascule** — le skill produisait le détail statutaire au
lieu de déléguer. La disponibilité d'un skill délégataire ne vaut plus
autorisation de produire, et la bascule devient un livrable formaté et
prioritaire (voir `docs/adr/0003-disponibilite-skill-delegataire.md`). Validation
partielle requise sur les cas 10, 11, 14, 17 et 21 avant toute campagne
complète. Détail dans `tests/bareme-cas-de-test.md`. Le package d'exécution est
limité aux fichiers nécessaires.
