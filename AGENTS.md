# Instructions projet — dpm-fpt

Les règles globales de `C:\Users\Krn\Documents\ClaudeMemory\AGENTS.md`
s'appliquent à ce dépôt.

## Mémoire projet

Avant toute modification non triviale, consulter :

- `C:\Users\Krn\Documents\ClaudeMemory\02-Projects\Dpm-fpt\overview.md`
- `C:\Users\Krn\Documents\ClaudeMemory\02-Projects\Dpm-fpt\conventions.md`
- `C:\Users\Krn\Documents\ClaudeMemory\02-Projects\Dpm-fpt\decisions.md`
  si ce fichier existe
- `C:\Users\Krn\Documents\ClaudeMemory\02-Projects\Dpm-fpt\journal.md`
  si ce fichier existe

## Contraintes du skill

- Communiquer et rédiger en français.
- Traiter le skill comme une aide à la décision, jamais comme une source
  autonome de droit positif.
- Vérifier les références juridiques à la source officielle avant toute
  conclusion ou les marquer explicitement comme non vérifiées.
- Maintenir le garde-fou APJA : STOP avant tout contenu lorsqu'un acte réservé
  à l'OPJ est demandé ; ce STOP ne crée aucun pouvoir de rétention.
- Distinguer les routes des articles 53 et 73, de l'article 78-6 du CPP, et
  l'absence de fondement de contrainte.
- Ne pas déplacer la frontière RH statutaire : activer `drh-fpt`.
- Ne pas réécrire l'historique des décisions ; ajouter une entrée qui
  supersède la précédente.

## Validation

Avant livraison, exécuter :

```powershell
python scripts/validate_repo.py
python scripts/package_skill.py
```

Le package d'exécution ne contient que `SKILL.md`, `agents/openai.yaml`,
`references/` (modèles inclus dans `references/templates/`) et `objets/`.
