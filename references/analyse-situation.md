# Couche 1 — Decision Engine (`analyse-situation.md`)

> **Branche appelée avant toute autre.** Routeur du skill : il qualifie les
> faits, détecte les conflits de compétence et le garde-fou APJA, puis oriente
> vers la branche métier (couche 2), l'objet métier (couche 3) ou le générateur
> d'écrit (couche 4). Il **ne traite pas le fond** : il aiguille.

## Périmètre / Exclusions

- **Périmètre** : orientation de toute situation un peu composée ; qualification
  préalable, détection de conflit de compétence, déclenchement du garde-fou
  APJA, choix de la branche / objet / écrit.
- **Exclusions** : le fond juridique de chaque sujet → branche concernée ; la
  méthode de recherche et la vigueur des textes → `recherche-juridique`.

---

## 1. Séquence de raisonnement imposée

À appliquer dans cet ordre pour **chaque** routage :

1. **Qualifier les faits** — qui, quand, où, en quelle qualité, contre qui /
   quoi ; nature de l'atteinte (ordre public, validité d'un acte, infraction).
2. **Police générale ou spéciale** — rattacher à la police générale du maire
   (CGCT art. L. 2212-1 et L. 2212-2 — à confirmer) ou à une police spéciale
   (route, débits de boissons, etc.).
3. **Autorité compétente** — maire / préfet / OPJ / autre. Qui détient le
   pouvoir mobilisé ?
4. **Détecter un conflit de compétence** — si plusieurs autorités peuvent
   intervenir, **le signaler explicitement avant de répondre** (voir §3).
5. **Base légale** — identifier le texte fondant le pouvoir, sous réserve de
   vérification (socle-sources, `SKILL.md` §5.3).
6. **Pouvoirs exerçables** — ce que la PM peut faire **en tant qu'APJA** ; si
   l'acte est réservé à l'OPJ → **garde-fou APJA (§2)**.
7. **Niveau de risque** (`SKILL.md` §5.1) — déterminé par l'enjeu, pas par la
   difficulté ; il fixe le plancher d'exigence.
8. **Procédures cumulables** — administrative, pénale, civile : repérer les
   cumuls (ex. fermeture administrative + poursuite pénale).
9. **Hiérarchiser l'urgence** — ce qui doit être fait immédiatement vs ensuite.
10. **Orienter vers l'écrit** — si un écrit est attendu, renvoyer au générateur
    `references/templates/` via `ecrits-professionnels.md`.

---

## 2. Garde-fou APJA — priorité absolue

**Avant tout routage métier**, tester : la situation exige-t-elle un acte
que l'agent PM n'est pas habilité à accomplir (garde à vue, audition formelle
de suspect, perquisition, réquisition judiciaire) ?

Si **oui**, afficher **en premier livrable**, avant tout autre contenu :

```
STOP — Cet acte dépasse les pouvoirs de l'agent de police municipale.
Ne pas l'accomplir ni le formaliser.
Rendre compte immédiatement à l'OPJ territorialement compétent.
```

Ce STOP ne fonde aucune contrainte. Router ensuite vers
`penal-procedure.md` :

1. qualifier la flagrance selon l'art. 53 CPP ;
2. appliquer l'art. 73 seulement en cas de crime flagrant ou de délit flagrant
   puni d'emprisonnement ;
3. appliquer l'art. 78-6 seulement lors d'un relevé d'identité autorisé, avec
   refus ou impossibilité de justification, puis selon la décision de l'OPJ ;
4. à défaut, n'exercer aucune rétention et se limiter aux constatations, au
   compte rendu et à la préservation proportionnée des traces.

---

## 3. Conflit de compétence — signalement obligatoire

Quand plusieurs autorités peuvent intervenir, **ne pas trancher en silence** :
nommer les autorités en présence, la règle de répartition, et le risque.

| Conflit fréquent | Réflexe |
|---|---|
| **Maire / préfet** (police générale vs police spéciale de l'État, substitution) | Identifier le titulaire du pouvoir spécial ; signaler le pouvoir de substitution du préfet → `pouvoirs-police.md` |
| **Maire / OPJ** (police administrative vs judiciaire) | Distinguer la finalité (préventive vs répressive) ; basculer en garde-fou APJA si judiciaire → `penal-procedure.md` |
| **PM / forces de l'État** (sur le terrain) | Renvoyer à la convention de coordination → `continuum-partenariats.md` |

---

## 4. Règles de routage explicites (`SI … ALORS …`)

Liste **non exhaustive** — point de départ obligatoire, à compléter par le
rédacteur. Le garde-fou APJA (§2) est testé **avant** toute règle ci-dessous.

```
SI fait relevant d'une infraction pénale constatable par APJA
   ALORS → branche penal-procedure.md (+ vérifier garde-fou §2)

SI fait dépassant les pouvoirs APJA (art. 21 CPP)
   ALORS → STOP immédiat (§2), pas de poursuite de branche

SI question sur un commerce / débit de boisson / fermeture administrative
   ALORS → objet commerce.md (qui pointe vers
   reglementation-appliquee.md + pouvoirs-police.md)

SI question sur un événement / rassemblement public
   ALORS → objet manifestation.md (+ doctrine-operationnelle.md)

SI rédaction d'un acte (arrêté, note, règlement, décision)
   ALORS → controle-legalite.md AVANT toute production via references/templates/

SI question RH statutaire (carrière, paie, instances, procédure disciplinaire)
   ALORS → bloc BASCULE drh-fpt émis AVANT tout contenu statutaire
   (SKILL.md §5.4) ; la disponibilité de drh-fpt n'autorise pas à traiter ici

SI manquement déontologique d'un agent PM (constat, pas procédure)
   ALORS → conformite-deontologie-donnees.md
   (dès que la PROCÉDURE disciplinaire débute → bloc BASCULE drh-fpt)

SI un volet statutaire n'apparaît qu'en incise d'une réponse métier
   (usage des images, accès fichier, organisation du service)
   ALORS → bloc BASCULE quand même, pour ce paragraphe (SKILL.md §5.4)

SI demande de production d'écrit (PV, rapport, note)
   ALORS → générateur interactif correspondant (couche 4 / assets)

SI doute sur une réforme récente, jurisprudence complexe ou décret manquant
   ALORS → appel recherche-juridique (hors socle autonome)

SI conflit de compétence entre autorités (maire / préfet / OPJ)
   ALORS → pouvoirs-police.md + signalement explicite du conflit avant réponse
```

### Compléments de routage (extensions)

```
SI stationnement gênant / abusif, enlèvement, mise en fourrière
   ALORS → objet fourriere.md (+ reglementation-appliquee.md)

SI occupation du domaine public (terrasse, marché, chantier, manifestation)
   ALORS → objet occupation-domaine-public.md (+ pouvoirs-police.md)

SI accident de la circulation / sur la voie publique
   ALORS → objet accident.md (+ penal-procedure.md pour la constatation)

SI chien dangereux / divagation / morsure
   ALORS → objet police-chiens.md (+ reglementation-appliquee.md)

SI installation, exploitation ou contrôle de la vidéoprotection / CSU
   ALORS → objet videoprotection.md + branche videoprotection.md
   (RGPD/CNIL transverse → conformite-deontologie-donnees.md)

SI armement, dotation, autorisation préfectorale, formation préalable
   ALORS → armement-equipements.md

SI doctrine de service, patrouilles, dispositif événementiel, gestion de crise
   ALORS → doctrine-operationnelle.md

SI convention de coordination, CLSPD/CISPD, prévention de la délinquance
   ALORS → continuum-partenariats.md

SI projet de service, budget, marché public, indicateurs, reporting
   ALORS → pilotage-budget.md (masse salariale → drh-fpt)

SI contrôle d'un acte AVANT production (arrêté/note/règlement)
   ALORS → controle-legalite.md (posture « juge administratif »)

SI anticipation des faiblesses contentieuses d'une décision
   ALORS → contentieux.md

SI retour d'expérience post-intervention
   ALORS → retex.md

SI agent PM (agrément, assermentation, FIA, commandement de terrain)
   ALORS → objet agent.md + rh-specificites-pm.md
   (carrière/paie/discipline statutaire → drh-fpt, SKILL.md §5.4)
```

---

## 5. Sortie du routeur

Après aiguillage, restituer brièvement :
- la **qualification** retenue et l'**autorité compétente** ;
- le **garde-fou APJA** s'il s'applique (STOP en tête) ;
- tout **conflit de compétence** détecté ;
- le couple **[risque / confiance]** (`SKILL.md` §5.1) ;
- la (les) **branche(s) / objet(s) / écrit(s)** vers lesquels on oriente.

---

## 6. Checklist du routeur

- [ ] Garde-fou APJA testé **en premier** ?
- [ ] Police générale / spéciale et autorité compétente identifiées ?
- [ ] Conflit de compétence détecté et signalé le cas échéant ?
- [ ] Niveau de risque (enjeu) posé avant de calibrer la réponse ?
- [ ] Cumuls de procédures repérés ?
- [ ] Orientation explicite vers branche / objet / écrit ?
- [ ] Renvoi à `recherche-juridique` si réforme / jurisprudence complexe ?
