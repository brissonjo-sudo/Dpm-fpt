# ADR-0001 — Adoption du pattern structurel `drh-fpt`

- **Statut** : accepté
- **Date** : 2026-06-30
- **Contexte** : le skill `dpm-fpt` démarre dans un repo vide. L'écosystème de
  l'auteur comprend déjà `drh-fpt` (v0.4.6, RH territoriale) et
  `droit-francais-skill` / `recherche-juridique` (v2.3.0, recherche juridique),
  qui partagent des conventions éprouvées.

## Décision

Répliquer les conventions de `drh-fpt` pour la **structure** et celles de
`recherche-juridique` pour le **socle-sources** :

- **Frontmatter** : `name`, `description` long-format (déclencheurs explicites +
  exclusions de non-activation), bloc `metadata` (`version` sémantique,
  `statut`, dates de revue/vérification, `perimetre`, `dependances`,
  `compatibilite`, `langue`).
- **Posture hybride** + **matrice métier/juridique** (quand vérifier la source).
- **Gabarits** : `_gabarit-branche.md` (branches `references/`) et
  `_gabarit-objet.md` (fiches `objets/`).
- **Socle-sources** : primarité, règle de provenance des identifiants, date de
  référence, hiérarchie des normes, abstention motivée, format de citation
  normalisé — la **méthode** détaillée restant déléguée à `recherche-juridique`.
- **Journalisation** : `CHANGELOG.md` (semver) + `JOURNAL.md` (cas anonymisés).
- **Tests** : `cas-de-test.json` (schéma `id`/`branche`/`prompt`/`attendus[]`) +
  `cas-co-activation.md` (barème RÉUSSITE/ÉCHEC/demi-réussite).

## Conséquences

- Cohérence d'usage entre les trois skills (mêmes réflexes, même format).
- Maintenance mutualisée (revue de rentrée commune au 1er septembre).
- Coût : reproduction fidèle exigée ; toute divergence justifiée par une ADR.

## Alternatives écartées

- **Structure ad hoc** : rejetée — perte de cohérence et de maintenabilité.
- **Dépendance dure à `recherche-juridique`** : rejetée — le skill doit rester
  fiable de façon autonome (socle-sources embarqué), `recherche-juridique` étant
  appelé pour l'approfondissement (réforme, décret manquant, jurisprudence).
