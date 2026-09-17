# Contrôle de protocole — partiel `claude-v1.0.5-partiel`

## Nature du run

**Partiel ciblé de 8 cas sur 28**, pas une campagne complète. Non comparable
aux scores `r1`–`r4` (qui portent sur les 28 cas). Voir `manifest.json` pour
la justification de la sélection.

## Copie du skill réellement mesurée

Chaque répondant charge le skill par **lecture directe du dépôt**
(`/home/user/Dpm-fpt/SKILL.md`, branche `claude/audit-skill-dpm-x387zc`,
commit `7c941b4`), l'outil Skill servant toujours une copie de session
figée (v1.0.1 au dernier contrôle).

Empreinte de référence du fichier mesuré :

```
SKILL.md sha256 = d76cf0e1e48c9a78a6df19650f67d56b7428450e6fc1b97b0ee3d2ab2cbab53a
```

Chaque `response.md` ouvre sur une ligne de contrôle rapportant la version
lue (`# Skill : dpm-fpt (v1.0.5)`) et l'empreinte calculée par le répondant.
**Résultat du contrôle : à consigner ci-dessous à l'issue du run.**

## Cloisonnement

- **Répondants** : accès limité au `prompt.md` de leur cas (lecture) et à
  leur `response.md` (écriture) ; toute autre lecture sous `tests/`
  interdite (`cas-de-test.json`, `bareme-cas-de-test.md`, `tests/runs/**`),
  ainsi que `JOURNAL.md`, `CHANGELOG.md`, `README.md` et `docs/`. Un agent
  par cas, contexte frais, aucun partage de contexte entre cas.
  `recherche-juridique` et `drh-fpt` restent invocables.
- **Juges** : reçoivent `response.md`, les `attendus[]` du cas
  (`tests/cas-de-test.json`) et `tests/bareme-cas-de-test.md` (barème
  normatif), sans accès à la réponse ni au jugement d'un autre cas, sans
  historique des campagnes précédentes.
- **Exécution strictement séquentielle** (règle du 2026-09-17) : un agent,
  on attend son retour, on committe, on lance le suivant. Aucun lancement
  groupé.

## Barème

Barème de `tests/bareme-cas-de-test.md`, inchangé depuis `r2`/`r3`/`r4`
(amendement du 2026-08-08 sur les attendus de pointeur non éliminatoires).

## Résultat du contrôle de version (à compléter à l'issue du run)

_À consigner : n/8 répondants ayant rapporté la version et l'empreinte
attendues._
