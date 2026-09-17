# Contrôle de protocole — campagne `claude-v1.0.2-r3`

## Copie du skill réellement mesurée

Chaque répondant a chargé le skill par **lecture directe du dépôt**
(`E:/Claude code/Projects/Dpm-fpt/SKILL.md`), l'outil Skill servant une copie de
session figée en v1.0.1 (cf. `JOURNAL.md`, entrée du 2026-08-08 « L'outil Skill
charge un snapshot de session, pas le dépôt »).

Empreinte de référence du fichier mesuré :

```
SKILL.md sha256 = 88b82428512d9249f600c484fd528ffdfe8f7f999a7bf2c0aed9c2ee6d7d19f2
```

**Résultat du contrôle : 28/28.** Les 28 répondants ont rapporté
`# Skill : dpm-fpt (v1.0.2)` et l'empreinte `88b8242…d19f2`, identique à celle
calculée sur le dépôt avant lancement de la campagne. Aucun répondant n'a lu la
copie de session v1.0.1.

## Cloisonnement

- **Répondants** : accès limité au `prompt.md` de leur cas (lecture) et à leur
  `response.md` (écriture) ; toute autre lecture sous `tests/` interdite
  (`cas-de-test.json`, `bareme-cas-de-test.md`, `tests/runs/**`), ainsi que
  `JOURNAL.md`, `CHANGELOG.md`, `README.md` et `docs/`. Un agent par cas,
  contexte frais, aucun partage de contexte entre cas.
- **Juges** : contexte distinct, un agent par cas. Matériel autorisé :
  `response.md` du cas, l'entrée correspondante de `suite.json` (champ
  `attendus` uniquement), `bareme-normatif.md` (partie normative du barème
  amendé, sans l'historique des campagnes), et — pour le seul contrôle du socle
  de sourcing — `SKILL.md` et `references/references-verifiees.md`.
  `tests/bareme-cas-de-test.md`, `JOURNAL.md` et `CHANGELOG.md` leur sont
  interdits, afin qu'aucun verdict antérieur ne les ancre.

## Skills délégataires

`recherche-juridique` et `drh-fpt` sont restés invocables par les répondants via
l'outil Skill. Leur disponibilité fait partie du dispositif testé : la règle de
non-autorisation de `SKILL.md` §5.4 pose que la disponibilité d'un délégataire
**ne vaut pas autorisation de produire**.

## Écart assumé

Le skill étant chargé par lecture explicite, le **déclenchement automatique par
sa `description`** n'est pas testé par cette voie ; seul son **contenu** l'est.
