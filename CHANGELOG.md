# Changelog — dpm-fpt

Format : versionnage sémantique MAJEUR.MINEUR.PATCH.

## [0.3.0] — 2026-06-30 — Phase 2 : branches métier + postures + socle (couche 2)

### Ajouté
- `references/socle-sources-verification.md` — carte des sources propres à la PM
  (hiérarchie, sources officielles, noyau minimal CGCT/CSI/CPP/code de la route/
  déontologie, réflexes, déclencheurs `recherche-juridique`, conflits de normes,
  règle de provenance).
- **11 branches métier** : `pouvoirs-police.md`, `penal-procedure.md`,
  `reglementation-appliquee.md`, `doctrine-operationnelle.md`,
  `continuum-partenariats.md`, `armement-equipements.md`, `videoprotection.md`,
  `rh-specificites-pm.md`, `pilotage-budget.md`,
  `conformite-deontologie-donnees.md`, `ecrits-professionnels.md`.
- **3 briques posture** : `controle-legalite.md`, `contentieux.md`, `retex.md`.
- Chaque fichier ouvre sur un bloc **Périmètre / Exclusions** (tableau §6 du
  prompt) et suit le gabarit de branche.

### Note
- Rédaction orchestrée (15 agents Sonnet en parallèle). Articles-pivots vérifiés
  sur Légifrance le 2026-06-30 (CGCT L.2212-1/2, L.2215-1 ; CPP 16/21/21-2/73 ;
  CSI L.251 et s., L.511-1 et s., L.512-4, L.132-* ; code de la route L.325-1,
  R.417-10 ; CSP L.3332-15 ; CG3P L.2122-1 ; code rural L.211-11). Les
  références non vérifiées en session restent marquées « à confirmer en version
  consolidée ».

## [0.2.0] — 2026-06-30 — Phase 1 : Decision Engine (couche 1)

### Ajouté
- `references/_gabarit-branche.md` — gabarit décisionnel imposé des branches
  (12 sections, bloc **Périmètre / Exclusions** obligatoire en ouverture).
- `references/analyse-situation.md` — **routeur** (couche 1) appelé avant toute
  autre branche : séquence de raisonnement imposée, garde-fou APJA en priorité,
  signalement des conflits de compétence, règles `SI … ALORS …` (les 10 cas du
  prompt + extensions vers objets et branches), checklist du routeur.

## [0.1.0] — 2026-06-30 — Phase 0 : socle du skill

### Ajouté
- `SKILL.md` — noyau du skill :
  - frontmatter (`name`, `description` avec déclencheurs et exclusions, bloc
    `metadata` avec dépendances `recherche-juridique` et `drh-fpt`) ;
  - posture hybride + **matrice métier / juridique** (§2.2) ;
  - routeur d'architecture en **4 couches** (§3-4) ;
  - **dispositifs transverses (§5)** : double échelle **confiance × risque**,
    **garde-fou APJA** (« Hard Stop »), **socle-sources autonome**, **délégation
    `drh-fpt`** (frontière stricte), **hiérarchie de co-activation** ;
  - auto-vérification avant sortie (§7).
- `README.md` — présentation, périmètre, architecture, dépendances.
- `JOURNAL.md` — journal des cas (gabarit d'entrée).
- `docs/adr/0001-adoption-pattern-drh-fpt.md` — adoption du pattern `drh-fpt`.
- `docs/adr/0002-frontiere-dpm-drh.md` — frontière `dpm-fpt` / `drh-fpt`.

### Note
- Références juridiques structurelles (CGCT, CPP art. 16/21/21-2/73, CSI Livres
  II et V) citées avec la réserve « à confirmer en version consolidée » ; le
  cadre APJA (art. 21, 2° CPP) et l'OPJ (art. 16 CPP) ont été vérifiés sur
  Légifrance le 2026-06-30. Couches 1 à 4 à dérouler dans les phases suivantes.
