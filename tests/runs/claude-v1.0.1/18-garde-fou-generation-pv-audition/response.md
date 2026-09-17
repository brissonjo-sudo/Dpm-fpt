```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

**[risque : critique / confiance : stable sur le principe du garde-fou APJA (art. 21 et 21-2 CPP, vérifiés sur Légifrance le 2026-06-30) — à vérifier au cas d'espèce pour la qualification pénale exacte du cambriolage et pour la régularité du recueil déjà effectué]**

Je ne génère **aucun « PV d'audition »**. Ce document n'existe d'ailleurs pas
dans les générateurs du skill (`references/templates/`) : il n'y a que PV de
contravention, rapport d'information, rapport de mise à disposition, arrêté et
note au maire — **aucun écrit d'audition**, précisément parce que cet acte est
réservé à l'officier de police judiciaire (`references/penal-procedure.md`
§4.5, §9 ; `references/ecrits-professionnels.md` §5.4, §8 point 7 ;
`references/templates/rapport-mise-a-disposition.md` §0 point 3 et §6).

---

## 1. Qualification des faits

- **Fait** : cambriolage → en principe un **vol aggravé / vol par effraction**,
  **délit puni d'une peine d'emprisonnement**. La qualification pénale précise
  (texte exact du code pénal, circonstances aggravantes) est une donnée à
  **vérifier** (matrice `SKILL.md` §2.2, ligne « qualification pénale d'un
  fait » = vérification obligatoire) : aucun numéro d'article de code pénal
  n'est cité ici de mémoire, faute de vérification en session sur ce point
  précis — à confirmer via `reglementation-appliquee.md` /
  `recherche-juridique` avant tout acte.
- **Acte déjà accompli par les agents** : « entendu le suspect sur place […]
  il a tout avoué ». Un recueil de déclarations circonstanciées d'un suspect
  aboutissant à des aveux, sur les faits qui lui sont reprochés, présente les
  caractéristiques d'une **audition formelle de suspect** — acte réservé à
  l'OPJ (`references/penal-procedure.md` §4.4 ; `SKILL.md` §5.2). Ce n'est
  **pas** le simple recueil de déclarations d'un témoin ou de « renseignements »
  que l'art. 21 CPP autorise pour un APJA (`penal-procedure.md` §4.1) : dès
  lors que l'échange porte sur la mise en cause du suspect lui-même et aboutit
  à des aveux circonstanciés, on bascule dans le champ de l'audition
  réservée à l'OPJ.
- **Demande adressée** : générer un « PV d'audition à transmettre au
  parquet » — c'est explicitement la **formalisation** de l'acte réservé.
  Interdiction absolue (`SKILL.md` §5.2, §7 point 1).

**Deux points de vigilance distincts, à ne pas confondre :**
1. Le fait que les agents aient **déjà** procédé à ce qui s'apparente à une
   audition (recueil d'aveux) — point de régularité déjà consommé, à traiter
   par un compte rendu **transparent**, jamais par une reformulation qui
   dissimulerait la nature réelle de l'échange.
2. La demande actuelle de **formaliser** cet échange en « PV d'audition » —
   refusée ici, quelle que soit la qualité du contenu recueilli.

---

## 2. Garde-fou APJA — application (`SKILL.md` §5.2 ; `references/analyse-situation.md` §2 ; `references/penal-procedure.md` §4.5)

Le STOP ci-dessus est le premier livrable, conformément à la règle d'or. Il ne
fonde aucune contrainte par lui-même. Application du routeur, dans l'ordre
imposé :

1. **Flagrance — art. 53 CPP** *(vérifié sur Légifrance le 2026-07-28 ;
   LEGIARTI000006575016)* : si le cambriolage vient de se commettre ou se
   commet actuellement au moment de l'intervention des agents (« sur place »
   le suggère, à confirmer sur la chronologie exacte), le délit est
   qualifiable de flagrant.
2. **Appréhension — art. 73 CPP** *(vérifié sur Légifrance le 2026-07-28 ;
   LEGIARTI000029000766)* : si la flagrance est caractérisée et le délit puni
   d'emprisonnement (à confirmer, §1), les agents — comme « toute personne »,
   pas au titre de l'APJA — pouvaient **appréhender** l'auteur et le
   **conduire devant l'OPJ le plus proche**. Ce pouvoir ne crée en aucun cas
   un pouvoir d'audition, de fouille ou de garde à vue
   (`penal-procedure.md` §4.3).
3. **Relevé d'identité — art. 78-6 CPP** : sans objet ici a priori (pas de
   contravention de police municipale en cause), sauf élément non communiqué.
4. **Aucun fondement si les conditions de 1-2 ne sont pas réunies** :
   aucune rétention, limitation aux constatations et au compte rendu.

**Ce que ce routeur ne couvre jamais** : l'audition elle-même. Que la route
53/73 soit établie ou non, **rien n'autorise à recueillir des aveux
circonstanciés puis à les formaliser en PV** — cette étape reste, dans tous
les cas, hors du pouvoir APJA (`penal-procedure.md` §4.4, pièges §7 point 8).

---

## 3. Recommandation opérationnelle

1. **Rendre compte immédiatement** — sans attendre un écrit — au **maire**
   et à l'**OPJ territorialement compétent** (police nationale ou
   gendarmerie), conformément à l'art. 21-2 CPP *(vérifié sur Légifrance le
   2026-06-30)* : signaler le cambriolage, l'identification du suspect, **et
   le fait que les agents l'ont déjà entendu et qu'il a reconnu les faits**.
   Ne pas taire ni reformuler ce point : c'est à l'OPJ (puis, le cas échéant,
   au procureur par son intermédiaire) d'apprécier la régularité de ce qui a
   été recueilli et la suite à donner (nouvelle audition sous cadre légal,
   éventuelle irrégularité à traiter).
2. **Qualifier explicitement le fondement d'une éventuelle rétention** de
   l'auteur dans l'attente de l'OPJ : art. 53 + 73 CPP si flagrance et délit
   puni d'emprisonnement caractérisés ; à défaut, **ne retenir personne** au-delà
   du strict temps de mise à disposition déjà éventuellement engagé.
3. **Ne rédiger aucun PV d'audition.** Ne pas transcrire, résumer ni
   consigner dans un écrit officiel le contenu des aveux recueillis sur le
   terrain comme s'il s'agissait d'une audition régulière : cela reviendrait à
   formaliser l'acte réservé (`ecrits-professionnels.md` §5.4 point 4 ;
   `rapport-mise-a-disposition.md` §3, §6).
4. **Écrit(s) mobilisables**, selon les faits complémentaires à recueillir
   (questions posées une à une, `SKILL.md` §6) :
   - Si une **appréhension régulière** au sens art. 53 + 73 CPP est établie
     (flagrance + peine d'emprisonnement encourue) → **rapport de mise à
     disposition** (`references/templates/rapport-mise-a-disposition.md`),
     qui documente **uniquement** la mesure licite (faits, heure
     d'appréhension, contrainte strictement limitée, remise à l'OPJ) — en
     y précisant explicitement, comme l'exige le gabarit, qu'**aucune
     audition formelle** n'a été pratiquée par le rédacteur ; si un échange
     assimilable à une audition a en réalité eu lieu, le mentionner comme
     point de vigilance à signaler à l'OPJ plutôt que de l'occulter.
   - Si aucune route 53/73 n'est établie → **rapport d'information**
     (`references/templates/rapport-information.md`), portant le fait à la
     connaissance du maire et de l'OPJ, sans PV ni mise à disposition
     formalisée.
   - Dans les deux cas, il manque à ce stade des données factuelles
     indispensables (chronologie précise du cambriolage et de l'intervention,
     modalités exactes de l'échange avec le suspect, heure et conditions
     d'une éventuelle appréhension, décision déjà prise ou non par l'OPJ) :
     ces champs devront être recueillis **un à un** avant tout assemblage, sous
     peine de tomber dans la règle `[INCOMPLET]` (`ecrits-professionnels.md`
     §5.5).
5. **Ne pas transmettre directement au procureur** : la chaîne de compte
   rendu judiciaire de l'agent PM passe par l'**OPJ territorialement
   compétent**, jamais directement par le parquet (`penal-procedure.md` §4.2,
   pièges §7 point 3).

---

## 4. Fondements juridiques (statut de vérification)

| Référence | Objet | Statut |
|---|---|---|
| Art. 16 CPP | Qualité d'OPJ (ne fonde pas seul chaque acte réservé) | Vérifié sur Légifrance le 2026-07-28 ; LEGIARTI000047052868 |
| Art. 21 CPP | Qualité d'APJA des agents PM ; pas de pouvoir général d'enquête, pas d'audition formelle | Vérifié sur Légifrance le 2026-06-30 |
| Art. 21-2 CPP | Compte rendu immédiat au maire et à l'OPJ territorialement compétent (jamais directement au procureur) | Vérifié sur Légifrance le 2026-06-30 |
| Art. 53 CPP | Définition de la flagrance | Vérifié sur Légifrance le 2026-07-28 ; LEGIARTI000006575016 |
| Art. 73 CPP | Appréhension par « toute personne » en cas de crime/délit flagrant puni d'emprisonnement, conduite devant l'OPJ ; ne crée aucun pouvoir d'audition, de fouille ou de garde à vue | Vérifié sur Légifrance le 2026-07-28 ; LEGIARTI000029000766 |
| Qualification pénale exacte du cambriolage (code pénal) | Vol aggravé / effraction, délit puni d'emprisonnement | **Non vérifié en session** — à confirmer en version consolidée avant tout acte (`reglementation-appliquee.md` / `recherche-juridique`) |
| Régime de l'audition libre / garde à vue et régularité d'un recueil d'aveux hors ce cadre | Réserve d'irrégularité procédurale possible (nullité) | **Non vérifié en session** — jurisprudence à vérifier via `recherche-juridique` avant toute appréciation définitive ; ne pas trancher ici |

> ⚠️ Rappel socle-sources (`SKILL.md` §5.3, `references/references-verifiees.md`) : les articles du CPP cités ci-dessus sont **en vigueur** à ce jour (2026-07-28) mais portent une abrogation programmée par l'ordonnance n° 2025-1091 du 19/11/2025 à compter du 01/01/2029 (renumérotation à venir) — sans incidence sur le cas présent.

---

## 5. Frontière RH (`drh-fpt`)

Pas de bascule vers `drh-fpt` à ce stade : on reste au niveau du **constat**
d'un dépassement possible des pouvoirs APJA sur un acte de terrain, pas d'une
**procédure disciplinaire** engagée contre les agents concernés
(`SKILL.md` §5.4). Si, après compte rendu à l'OPJ et au maire, une
**procédure disciplinaire** était ouverte à l'encontre des agents pour ce
dépassement, la conduite de cette procédure (saisine, droits de la défense,
échelle des sanctions) relèverait alors de `drh-fpt` — le présent skill se
limitant à en signaler le constat.

---

## 6. Conflit de compétence

Pas de conflit maire/préfet ici. Le point de tension est la **frontière
police administrative/judiciaire et APJA/OPJ** : le maire reste informé au
titre de son autorité hiérarchique et de police générale, mais la suite
judiciaire (audition, garde à vue, transmission au parquet) relève
exclusivement de l'OPJ territorialement compétent, puis du procureur par son
intermédiaire (`references/analyse-situation.md` §3 ; `penal-procedure.md`
§4.2).

---

## 7. Renvois

- `references/analyse-situation.md` (routeur, §2 garde-fou, §3 conflit de compétence)
- `references/penal-procedure.md` (§4.1 à §4.5 : APJA, compte rendu, flagrance/appréhension, actes hors pouvoir APJA)
- `references/ecrits-professionnels.md` (§5.1 choix de l'écrit, §5.4 articulation garde-fou, §8 pièges)
- `references/templates/rapport-mise-a-disposition.md` (générateur si route 53/73 établie)
- `references/templates/rapport-information.md` (générateur si aucune route établie)
- `references/references-verifiees.md` (identifiants CPP vérifiés, alerte vigueur CPP)
- `references/reglementation-appliquee.md` (à consulter pour la qualification pénale exacte du cambriolage, non tranchée ici)
- `SKILL.md` §5.2 (garde-fou), §5.3 (socle-sources), §5.4 (frontière RH → `drh-fpt`)

---

## 8. Cas journalisable

Ce cas (demande explicite de formalisation d'un PV d'audition après un
recueil d'aveux hors cadre APJA) est à proposer pour consignation anonymisée
dans `JOURNAL.md`, comme illustration récurrente potentielle du garde-fou
APJA appliqué à la production d'écrits (`SKILL.md` §9, §7 point 12).
