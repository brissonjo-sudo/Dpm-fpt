# Changelog — dpm-fpt

Format : versionnage sémantique MAJEUR.MINEUR.PATCH.

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
