# Sources préparées depuis main — 13 octobre 2026

Statut : préparation locale uniquement. Base : origin/main 2376270f, runtime DPM1.0.5 conservé. Aucune poussée, campagne, nouvelle preuve métier ou publication.

## Sources retenues

Deux modules génériques sont repris du travail local ancien : scripts/eval_suite.py et scripts/package_skill.py. Les autres 114scripts restent dans les archives et le checkout original : 74outils de maintenance du connecteur juridique ou diagnostics ponctuels, 40harnais et pilotes historiques. Le classement complet par chemin, empreinte, imports et références est conservé dans le dossier de récupération du chantier.

L’évaluateur garde les suites figées, sélection de cas, empreintes du barème, provenance déclarée et métadonnées de rôles distincts. Ces métadonnées ne prouvent pas une isolation réelle ni une identité fournisseur. Les formats1/2 restent synthétisables sans devenir une autorisation de release : la barrière exige des valeurs True pour protocole et modèle, une valeur inconnue ne passe pas.

Les formats natifs ≥3 sont explicitement refusés par ce candidat générique ; leur harnais historique et leur protocole restent dans l’archive. Aucun import du runner historique ni dépendance au sous-module dans ce candidat. Ne pas convertir les preuves existantes ni requalifier leurs scores avec ce changement.

Le packager accepte une source explicite dans le dépôt, vérifie les fichiers requis et refuse un lien runtime sortant. Le nom de l’archive vient de la version du SKILL sélectionné. La valeur de repli reste1.0.5, pas la1.0.3du checkout ancien. Aucun package généré dans cette préparation.

## Préparation d’une évaluation

La nouvelle interface exige des paramètres explicites. Exemple à adapter, non exécuté :

```powershell
python scripts/eval_suite.py prepare --run-dir tests/runs/NOUVEAU_RUN --responder MODELE_REPONDANT --judge MODELE_JUGE --skill-version 1.0.5 --responder-reasoning EFFORT_REPONDANT --judge-reasoning EFFORT_JUGE --source-commit COMMIT_SOURCE --skill-source dpm-fpt=SKILL.md --bareme tests/bareme-cas-de-test.md
```

Un format2 nécessite ensuite orchestration.json et les fichiers de contexte des rôles. Réponses/jugements réels, cohérence des déclarations, traces et avis humains restent des contrôles distincts. Ce script ne lance aucun modèle.

## Contenus conservés sans reprise

- SKILL, références, objets, agents, suite et barème sont ceux de main, inchangés.
- CHANGELOG, JOURNAL et résultats locaux anciens ne remplacent pas les versions plus récentes de main. Leurs octets et couches d’index sont archivés.
- Pas de sous-module, de .gitmodules, de nouvelle archive de campagne ou d’outil de publication GitHub ajouté à ce candidat.
- README/ADR locaux de sous-modules et run_sol_campaign.py attendent la décisionT47 ; rien n’est retiré dans le checkout original.
- Les scripts de diagnostics juridiques ont des contextes, versions de protocole, pins ou dossiers fixes ; ils ne sont pas présentés comme sources génériques DPM prêtes à livrer.

## Contrôles et limites

Comparaison des sources avec les 65commits supplémentaires de main, analyse de syntaxe Python et comparaison des arbres Git. Aucun test logiciel ajouté ni exécuté, aucun service/API/CLI de modèle appelé. Les tests et les commandes validate_repo.py/package_skill.py prescrits avant livraison restent à exécuter dans un chantier de validation du candidat ; aucune livraison ni demande de poussée n’est incluse ici.

Avant une future poussée : revoir le diff et la compatibilité de la nouvelle CLI, exécuter les contrôles autorisés du candidat exact, puis validation ciblée Jo. Tous les résultats historiques restent liés à leur runtime/protocole.
