# ADR-0003 — La disponibilité d'un skill délégataire ne vaut pas autorisation de produire

- **Statut** : accepté
- **Date** : 2026-08-08
- **Contexte** : la campagne `claude-v1.0.1-r2`, rejouée les 2026-08-07/08 avec
  un protocole corrigé (répondant disposant **réellement** de `dpm-fpt`,
  `recherche-juridique` et `drh-fpt` invocables), a fait apparaître un mode de
  défaillance que les campagnes antérieures ne pouvaient pas révéler : **rendre
  `drh-fpt` invocable supprime le réflexe de bascule**. Aux cas 14 (critique) et
  21, le répondant a produit lui-même le détail statutaire — échelle des
  sanctions, composition et saisine du conseil de discipline, prescription,
  droits de la défense, droit de se taire, suspension conservatoire — au lieu de
  déléguer. La frontière a été franchie **par capacité, non par ignorance**.

  Ce n'était pas un déficit de documentation. La frontière `dpm-fpt` / `drh-fpt`
  posée par l'[ADR-0002](0002-frontiere-dpm-drh.md) était déjà écrite dans
  `SKILL.md` §5.4, dans le routeur `analyse-situation.md`, et onze fois dans
  `conformite-deontologie-donnees.md` ; `rh-specificites-pm.md` §4.0 interdisait
  même de reformuler le détail procédural « même partiellement ».

  Le diagnostic est une **asymétrie structurelle** avec le garde-fou APJA, qui a
  tenu sur les quatre cas critiques qui le déclenchent (12, 18, 27, 28) : le
  garde-fou dispose d'un **bloc STOP littéral**, d'une **priorité d'émission** et
  d'un **test de sortie binaire** ; la frontière RH n'avait qu'un tableau de
  répartition et une phrase de principe. Sur 28 réponses, **seules 2 nommaient
  `drh-fpt`**.

## Décision

**Règle de non-autorisation.** La disponibilité d'un skill délégataire dans la
session ne vaut pas autorisation de produire. Un skill délégataire mobilisable
**change l'interlocuteur, pas le périmètre** : c'est une raison de **basculer**,
jamais une raison de **traiter**. Pouvoir répondre n'est pas être compétent pour
répondre.

**La bascule est un livrable formaté et prioritaire**, sur le modèle du hard stop
APJA. Le **bloc BASCULE** est émis **avant** tout contenu statutaire :

```
BASCULE drh-fpt — Cette demande porte sur la conduite d'une procédure
statutaire. Je ne la traite pas ici, y compris si drh-fpt est mobilisable
dans cette session.
À reprendre côté drh-fpt : [objet précis].
```

Le skill délégataire est **nommé** : « la DRH », « votre service RH » ou « le
service du personnel » désignent un service de la collectivité et ne valent pas
bascule.

**Déclencheurs (liste fermée)** : échelle ou groupes de sanctions ; conseil de
discipline (composition, saisine, convocation, délais) ; droits de la défense et
communication du dossier ; droit de se taire ; prescription disciplinaire ;
suspension conservatoire ; CAP ; quantum de sanction ; avancement, échelon,
positions statutaires ; RIFSEEP/IFSE général ; instances (CST, F3SCT) ;
instruction d'une protection fonctionnelle.

**Portée transverse.** La règle s'applique **quel que soit le sujet d'entrée**,
y compris quand le volet statutaire n'est qu'une **incise** dans une réponse
métier. Le cas 21 est entré par les caméras-piétons et a dérivé vers les
garanties disciplinaires : une réponse peut être intégralement dans le périmètre
`dpm-fpt` et devoir émettre le bloc pour un seul de ses paragraphes.

**Ligne de partage après la bascule.** Restent permis : **nommer** l'étape sans
la dérouler (« le conseil de discipline devra être saisi »), signaler un enjeu de
calendrier ou de preuve, rappeler la conséquence métier (perte de la qualité
d'APJA, retrait d'habilitation). Restent interdits : délais, instances, droits de
la défense, quantums et échelles — **même sourcés, même sous réserve**.

## Conséquences

- `SKILL.md` §5.4 porte la règle, le bloc, les déclencheurs et la portée ; §7
  point 8 devient un **test à charge** portant sur le texte effectivement produit
  (« contient-il un délai, une instance, un droit de la défense, un quantum ? »)
  et non plus une question fermée auto-rassurante.
- La règle est propagée en couche 1 (`analyse-situation.md`) et en couche 2
  (`rh-specificites-pm.md` §4.0 et §5.2, `conformite-deontologie-donnees.md`
  §4.9 et §7), **sans duplication** : les branches renvoient au format de §5.4.
- `tests/bareme-cas-de-test.md` étend l'attendu critique « frontière RH » à
  **tout cas** (et non au seul cas 14), et précise que la disponibilité de
  `drh-fpt` n'est pas une excuse.
- `scripts/validate_repo.py` fige les nouveaux invariants (bloc BASCULE, règle de
  non-autorisation) au même titre que les snippets du garde-fou APJA.
- La règle est **généralisable** : elle vise tout skill délégataire, pas seulement
  `drh-fpt`. Elle s'appliquerait à l'identique si `dpm-fpt` déléguait un jour un
  autre domaine réservé.

## Alternatives écartées

- **Se reposer sur la description de la frontière** (statu quo de l'ADR-0002) :
  rejetée — c'est précisément le dispositif qui a cédé en `r2`, alors qu'il était
  documenté quatre fois dans le dépôt et qu'il interdisait déjà explicitement la
  reformulation partielle. Décrire une frontière ne suffit pas à la rendre
  opposable ; il faut un format de sortie et un test vérifiable.
- **Ne pas rendre `drh-fpt` invocable pendant les campagnes** pour préserver le
  réflexe de bascule : rejetée — cela reviendrait à tester un dispositif
  différent de celui déployé, et c'est exactement le biais de protocole qui a
  invalidé la première exécution `r2`.
- **Interdire toute mention du statutaire après la bascule** : rejetée — un DPM a
  besoin de savoir qu'une étape existe et quand elle arrive. La ligne de partage
  « nommer sans dérouler » préserve l'utilité opérationnelle sans produire de
  contenu réservé.
