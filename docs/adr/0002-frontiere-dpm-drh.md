# ADR-0002 — Frontière `dpm-fpt` / `drh-fpt` et garde-fou APJA

- **Statut** : accepté
- **Date** : 2026-06-30
- **Contexte** : deux frontières de compétence structurent le métier de DPM et
  doivent être codées sans ambiguïté pour éviter les chevauchements et les
  dépassements de pouvoir : (1) métier PM vs RH statutaire ; (2) pouvoirs APJA
  vs actes réservés à l'OPJ.

## Décision

### Frontière `dpm-fpt` / `drh-fpt` (RH des agents PM)

Règle de bascule **constat vs procédure** :

- `dpm-fpt` **conserve** : agrément préfectoral + assermentation ; FIA et
  formation continue armement ; cycles atypiques + régime indemnitaire propre
  (ISF) ; **constat** textuel du manquement déontologique ; commandement
  opérationnel de terrain.
- `drh-fpt` **prend la main** sur : carrière, paie, avancement, positions
  statutaires ; RIFSEEP général ; instances et dialogue social ; **procédure**
  disciplinaire (saisine du conseil, droits de la défense, échelle des
  sanctions) ; santé/QVT, masse salariale, SI RH, recrutement/formation général.

Tant qu'on reste au **constat** d'un manquement (au regard du code de
déontologie PM), `dpm-fpt` répond. Dès la **conduite de la procédure**
disciplinaire, passer la main à `drh-fpt`.

### Garde-fou APJA (« Hard Stop »)

La police municipale agit comme **APJA** (art. 21 / 21-2 CPP — à confirmer en
version consolidée). Tout acte réservé à l'**OPJ** (art. 16 CPP) — garde à vue,
audition de suspect, perquisition hors flagrance, réquisition judiciaire — est
**hors périmètre d'action**. Sa détection déclenche un **STOP affiché en premier
livrable**, avant tout autre contenu, orientant vers la mise à disposition
immédiate (art. 73 CPP) et la préservation des lieux.

## Conséquences

- La frontière RH est matérialisée par la branche `rh-specificites-pm.md` et le
  tableau du `SKILL.md` §5.4 ; testée par un cas de co-activation
  `dpm-fpt` × `drh-fpt`.
- Le garde-fou APJA est prioritaire sur toute sortie métier ; testé par un cas
  dédié dans `tests/`.

## Alternatives écartées

- **Tout traiter dans `dpm-fpt`** (y compris la procédure disciplinaire) :
  rejetée — duplication avec `drh-fpt` et risque d'incohérence statutaire.
- **Garde-fou en simple avertissement** plutôt que hard stop prioritaire :
  rejetée — l'enjeu (dépassement de pouvoir, nullité de procédure) impose un
  blocage explicite et prioritaire.
