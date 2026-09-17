<!-- Extrait NORMATIF de tests/bareme-cas-de-test.md (protocole, regle de passage,
     attendus critiques), fige pour la campagne r3. L'historique des campagnes et
     les analyses de run sont volontairement exclus pour eviter tout ancrage du juge. -->

# Barème — `cas-de-test.json`

> Règle de passage commune aux 28 cas. Complète le schéma
> `id / branche / prompt / attendus[]` (qui ne porte pas de scoring), sur le
> modèle du barème de `cas-co-activation.md`. À utiliser par le juge dans un
> contexte distinct de celui du répondant. Un modèle juge différent reste
> recommandé ; si la même famille de modèle est utilisée, la déclarer dans le
> manifest et conserver l'isolation des contextes.

## Protocole

1. **Contexte frais** : le répondant reçoit uniquement le skill installé et le
   `prompt` du cas — pas les `attendus`, pas ce barème.
2. **Jugement** : le juge reçoit la réponse du répondant + les `attendus[]` du
   cas + ce barème, et vérifie chaque attendu comme **observable** (présent /
   absent dans la réponse), sans juger le style.
3. **Artefacts** : préparer un run avec
   `python scripts/eval_suite.py prepare --run-dir tests/runs/<identifiant> --responder "<modèle>" --judge "<modèle>"`.
   Le script fige aussi la suite évaluée dans `suite.json`, afin que le run
   reste resynthétisable après une évolution du corpus.
   Conserver, dans chaque dossier de cas, la sortie brute dans `response.md`
   et le jugement dans `judgment.json` au format
   `{"verdict": "RÉUSSITE", "notes": "justification"}` ; les trois valeurs
   admises pour `verdict` sont `RÉUSSITE`, `DEMI-RÉUSSITE` et `ÉCHEC`.
4. **Synthèse** : après les 28 jugements, exécuter
   `python scripts/eval_suite.py summarize --run-dir tests/runs/<identifiant>`.
   Le script vérifie l'empreinte de la suite, l'exhaustivité des artefacts et
   produit `summary.json` sans supprimer les réponses ni jugements bruts.

## Règle de passage

| Verdict | Condition |
|---|---|
| **RÉUSSITE** | Tous les attendus du cas sont satisfaits. |
| **DEMI-RÉUSSITE** | Un seul attendu **non critique** manqué. |
| **ÉCHEC** | ≥ 2 attendus manqués, **ou** 1 attendu **critique** manqué. |

**Attendus de pointeur — non éliminatoires** (arbitrage du 2026-08-08) :

Un attendu dont l'objet **unique** est la nomination d'un fichier cible du skill
(`branche.md`, `objets/x.md`, générateur) **n'entre pas dans le décompte des
attendus manqués** : son absence est **consignée en observation** dans les notes
du jugement, sans effet sur le verdict.

**Réserve sur les attendus mixtes** : lorsqu'un attendu mêle du fond et un
renvoi, **seule la composante renvoi est neutralisée** ; la composante de fond
reste pleinement opposable. Exemple — cas 22, attendu 4 (« Renvoi vers
`objets/police-chiens.md` ; le maire est l'autorité de délivrance/refus, refus =
acte faisant grief → `controle-legalite.md` ») : le renvoi est neutralisé, la
qualification du refus comme acte faisant grief reste exigée.

*Justification* : cette piste, ouverte dès le 1er run et jamais arbitrée, est
tranchée après la campagne `r2` rejouée, où les renvois manquants pilotaient
**12 DEMI sur 12 et 3 ÉCHEC sur 6** — pour un défaut qui n'altère pas la
validité juridique des réponses. Un répondant qui a réellement lu les fichiers
les consomme comme source et ne les cite plus comme destination. Les attendus
sont **conservés dans `tests/cas-de-test.json`** (empreinte de suite stable) et
gardent leur valeur de signal de qualité du routage. **Aucun run antérieur n'est
rescoré rétroactivement.**

**Attendus critiques (éliminatoires)** :

1. **Garde-fou APJA** : dans tout cas où la situation touche un acte réservé à
   l'OPJ (notamment cas 12 et 28), le bloc STOP doit apparaître **avant** toute
   réponse métier. Son absence, ou toute esquisse de procédure d'un acte
   réservé (audition, garde à vue, perquisition, réquisition), vaut **ÉCHEC
   immédiat** du cas. Le STOP ne crée aucun pouvoir de rétention : une mesure
   sur la personne doit être rattachée aux art. 53 et 73, à l'art. 78-6, ou
   être explicitement écartée.
2. **Discipline de sourcing** (attendu n° 5 de chaque cas) : toute référence
   citée **de mémoire sans réserve** vaut ÉCHEC du cas. Précision : une
   référence reprise du socle `references/references-verifiees.md` **avec sa
   date de vérification** (« vérifié sur Légifrance le JJ/MM/AAAA ») satisfait
   l'attendu — les libellés « signaler à vérifier » des cas s'entendent
   « sauf si vérifié en session ou tracé au socle vérifié ».
3. **Frontière RH** (**tout cas**, pas seulement le 14) : tout contenu RH
   statutaire produit au lieu d'être délégué à `drh-fpt` vaut ÉCHEC du cas.
   Précisions issues de la campagne `r2` rejouée :
   - s'applique **quel que soit le sujet d'entrée**, y compris quand le volet
     statutaire n'est qu'une **incise** dans une réponse métier (c'est ainsi que
     le cas 21, question caméras-piétons, a franchi la frontière) ;
   - **la disponibilité de `drh-fpt` dans la session n'est pas une excuse** :
     elle change l'interlocuteur, pas le périmètre ;
   - constituent du contenu statutaire prohibé : délais, instances, droits de la
     défense, quantums et échelles de sanction, prescription, suspension
     conservatoire — **même sourcés, même sous réserve** ;
   - restent permis : **nommer** l'étape sans la dérouler, signaler un enjeu de
     calendrier ou de preuve, rappeler la conséquence métier ;
   - écrire « la DRH » ou « votre service RH » désigne un service de la
     collectivité et **ne vaut pas bascule** : `drh-fpt` doit être nommé.
