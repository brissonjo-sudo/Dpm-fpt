# Gabarit des objets métier (`objets/`)

> Méta-document (instructions de conception, pas de contenu métier). Les huit
> fiches « objet » de `objets/` suivent **exactement** cette structure, dans cet
> ordre. Un objet est une **fiche système expert** qui agrège, pour une
> situation type récurrente, ce dont le DPM a besoin pour décider et agir vite.
>
> Principe directeur : l'objet **agrège et pointe**, il ne **duplique pas**. Le
> fond juridique reste dans les branches (`references/`) ; la jurisprudence
> reste renvoyée à `recherche-juridique`.

## Structure imposée d'un objet (6 sections)

1. **Acteurs et autorités compétentes** — qui intervient (maire, préfet, OPJ,
   PM, tiers), qui décide quoi. Signaler tout conflit de compétence possible.
2. **Textes applicables** — **pointeurs** vers les branches concernées
   (chemins relatifs), avec la mention des codes/textes clés et la réserve « à
   confirmer en version consolidée ». **Pas de recopie** du fond des branches.
3. **Procédures (étapes, délais)** — le déroulé opérationnel pas à pas, avec les
   délais et points de contrôle ; distinguer voie administrative et voie pénale
   si elles se cumulent.
4. **Écrits associés** — **pointeur** vers le(s) générateur(s) `references/templates/`
   pertinents (PV, rapport, arrêté, note au maire).
5. **Jurisprudence clé** — **pointeur** vers `recherche-juridique` (ne pas
   recopier le fond) ; signaler seulement les thèmes jurisprudentiels sensibles.
6. **Check-list opérationnelle** — contrôles concrets de terrain et de procédure
   avant d'agir / de clôturer, dont le **garde-fou APJA** si l'objet peut le
   déclencher.

## Règles d'écriture

- Impératif, phrases courtes, orienté action et décision.
- En-tête : un bloc rappelant en une phrase la **situation type** couverte et le
  couple **[risque / confiance]** dominant (`SKILL.md` §5.1).
- Aucune référence numérotée ou valeur datée **de mémoire** : réserve « à
  confirmer en version consolidée » ou identifiant vérifié en session.
- Renvois par **pointeur** uniquement (branches, générateurs, objets liés).
- Si l'objet peut déclencher le garde-fou APJA (§5.2), le rappeler en section 6.
