# Contrôle de protocole — campagne `claude-v1.0.4-r4`

## Copie du skill réellement mesurée

Chaque répondant charge le skill par **lecture directe du dépôt**
(`/home/user/Dpm-fpt/SKILL.md`, branche `claude/audit-skill-dpm-x387zc`,
HEAD postérieur aux correctifs de l'audit du 2026-09-14), l'outil Skill
servant toujours une copie de session figée en v1.0.1 (constat renouvelé le
2026-09-14 : `diff` du skill synchronisé contre le dépôt).

Empreinte de référence du fichier mesuré :

```
SKILL.md sha256 = 8a461746c0867c7c33adb531f1ffeff3da97c024d09aa70e1523a04e0f3c74a4
```

Chaque `response.md` ouvre sur une ligne de contrôle (commentaire HTML)
rapportant la version lue (`# Skill : dpm-fpt (v1.0.4)`) et l'empreinte
calculée par le répondant. **Résultat du contrôle : 28/28.** Les 28 répondants
ont rapporté `# Skill : dpm-fpt (v1.0.4)` et l'empreinte `8a461746…c74a4`,
identique à celle calculée sur le dépôt avant lancement. Aucun répondant n'a lu
la copie de session v1.0.1.

## Empreinte de suite

`suite.json` = `91d794d08e5555d69eb3c6738b834b3efca9d9b09f63075963d0793d451873a4`.
Cette empreinte diffère de celle de `r2`/`r3` (`8dbcf5e1…`) **uniquement par
les fins de ligne** : le commit `bcd488b` du 2026-09-06 (`.gitattributes`) a
normalisé `tests/cas-de-test.json` en LF ; `eval_suite.py` hache les octets
bruts. Contenu vérifié identique hors `\r` (`diff` de `suite.json` r3 et du
corpus courant). **Aucun cas n'est modifié** ; `r4` se compare à `r3`.

## Cloisonnement

- **Répondants** : accès limité au `prompt.md` de leur cas (lecture) et à
  leur `response.md` (écriture) ; toute autre lecture sous `tests/` interdite
  (`cas-de-test.json`, `bareme-cas-de-test.md`, `tests/runs/**`), ainsi que
  `JOURNAL.md`, `CHANGELOG.md`, `README.md` et `docs/`. Un agent par cas,
  contexte frais, aucun partage de contexte entre cas. Accès à Légifrance par
  `WebFetch`/`WebSearch` autorisé (voie de repli de `recherche-juridique`,
  aucune clé PISTE dans l'environnement).
- **Juges** : contexte distinct, un agent par cas. Matériel autorisé :
  `response.md` du cas, l'entrée correspondante de `suite.json` (champ
  `attendus` uniquement), `bareme-normatif.md` (extrait normatif figé en `r3`,
  reconduit sans changement — il omet la section « Score de suite », sans
  incidence : le juge note cas par cas), et — pour le seul contrôle du socle
  de sourcing — `SKILL.md` et `references/references-verifiees.md`.
  `tests/bareme-cas-de-test.md`, `JOURNAL.md`, `CHANGELOG.md` et `docs/` leur
  sont interdits.

## Skills délégataires

`recherche-juridique` et `drh-fpt` restent invocables par les répondants via
l'outil Skill. Leur disponibilité fait partie du dispositif testé (règle de
non-autorisation, `SKILL.md` §5.4).

## Coût

Nouveauté `r4` : tokens et durée de chaque répondant et de chaque juge, tels
que rapportés par l'orchestrateur, sont consignés dans `manifest.json`
(champ `cost`). Ordre de grandeur mesuré : **≈ 121 000 tokens par répondant**
et **≈ 72 500 par juge**, soit **≈ 5,4 M tokens** pour la campagne.

## Écart d'exécution assumé — parallélisme

Contrairement à `r3`, la campagne n'a **pas** été exécutée en vagues parallèles :
la limite de forfait a interrompu trois vagues successives (12, 12 puis 10
agents). À partir du 2026-09-17 l'exécution est passée à **un agent à la fois**,
avec commit après chaque retour. Cet écart porte sur le **calendrier**, pas sur
le dispositif : chaque agent conserve un contexte frais et isolé, et le
cloisonnement décrit ci-dessus est inchangé. Les agents interrompus avant
d'écrire leur fichier ont été **relancés depuis zéro**, jamais repris.

## Écart assumé

Le skill étant chargé par lecture explicite, le **déclenchement automatique
par sa `description`** n'est pas testé par cette voie ; seul son **contenu**
l'est.
