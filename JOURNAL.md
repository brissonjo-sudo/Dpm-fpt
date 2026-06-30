# Journal des cas — dpm-fpt

> Matière première de l'amélioration du skill. À chaque échange significatif,
> consigner ce qui mérite d'être intégré dans une future version. **Aucune
> donnée nominative** (agent ou administré) : décrire les cas de façon
> anonymisée.

## Comment consigner

Une entrée par cas, au format ci-dessous.

```
### AAAA-MM-JJ — [titre court]
- Type : lacune | erreur | cas nouveau | écrit récurrent
- Branche : pouvoirs-police | penal-procedure | reglementation-appliquee |
  doctrine-operationnelle | continuum-partenariats | armement-equipements |
  videoprotection | rh-specificites-pm | pilotage-budget |
  conformite-deontologie-donnees | ecrits-professionnels | (posture)
- Contexte (anonymisé) : ...
- Constat : ce qui a manqué ou mal fonctionné.
- Action proposée : ce qu'il faudrait ajouter/corriger, et dans quel fichier.
- Statut : à traiter | intégré (vX.Y.Z)
```

## Entrées

### 2026-06-30 — Phase 1 : routeur (Decision Engine)
- Type : cas nouveau
- Branche : analyse-situation (couche 1)
- Contexte : rédaction du gabarit de branche et du routeur.
- Constat : le garde-fou APJA doit être testé **avant** tout routage métier ;
  les conflits de compétence (maire/préfet/OPJ) doivent être signalés et non
  tranchés en silence.
- Action proposée : conserver le garde-fou APJA en tête de routeur et de
  checklist ; relier chaque règle SI…ALORS aux objets de la couche 3.
- Statut : intégré (v0.2.0)

### 2026-06-30 — Phase 0 : pose du socle
- Type : cas nouveau
- Branche : (socle / SKILL)
- Contexte : initialisation du skill `dpm-fpt` dans un repo vide, sur le modèle
  structurel de `drh-fpt` et le socle-sources de `recherche-juridique`.
- Constat : architecture en 4 couches figée par le prompt d'exécution ;
  dispositifs transverses (§5) à encoder dans `SKILL.md` avant de dérouler les
  couches.
- Action proposée : dérouler le routeur `analyse-situation.md` (Phase 1), les 11
  branches + 3 briques posture (Phase 2), les 8 objets (Phase 3), les 5
  générateurs (Phase 4), les tests (Phase 5) et le vault (Phase 6).
- Statut : intégré (v0.1.0)
