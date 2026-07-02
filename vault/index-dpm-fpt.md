---
tags: [skill/dpm-fpt, index]
version: 0.7.0
---

# Index — skill dpm-fpt

> Ce vault **indexe** le skill `dpm-fpt` (Directeur de Police Municipale). Il ne
> duplique aucun contenu métier : chaque ligne pointe vers le fichier source du
> repo (chemins relatifs depuis `vault/`). Pour le maillage des liens entre
> objets, branches et générateurs → [[maillage]].

## Navigation rapide (1 besoin = 1 fichier)

### Couche 1 — Routeur

| Besoin | Fichier repo |
|--------|--------------|
| Point d'entrée du skill, déclenchement, posture hybride, garde-fou APJA, frontière drh-fpt | `../SKILL.md` |
| Qualifier une situation composée (Decision Engine, séquence de raisonnement) | `../references/analyse-situation.md` |
| Carte des sources propres PM (CGCT, CSI, CPP, code de la route, déontologie) + conflit de normes | `../references/socle-sources-verification.md` |
| Références vérifiées Légifrance (identifiants LEGIARTI, versions, alerte CPP 2029) | `../references/references-verifiees.md` |
| Liens de récupération du RSD par département (ARS régionale / préfecture) | `../references/liste-RSD.md` |

### Couche 2 — Branches métier (11) + 3 briques posture

| Besoin | Fichier repo |
|--------|--------------|
| Gabarit imposé d'une branche (structure de référence) | `../references/_gabarit-branche.md` |
| Pouvoirs de police du maire (police générale / spéciale, autorité compétente) | `../references/pouvoirs-police.md` |
| Procédure pénale applicable à la PM, pouvoirs APJA, garde-fou OPJ | `../references/penal-procedure.md` |
| Réglementation appliquée (route, stationnement/fourrière, débits de boissons, salubrité, domaine public, animaux) | `../references/reglementation-appliquee.md` |
| Doctrine opérationnelle (organisation, patrouilles, dispositifs événementiels, gestion de crise) | `../references/doctrine-operationnelle.md` |
| Continuum de sécurité et partenariats (convention de coordination, CLSPD/CISPD) | `../references/continuum-partenariats.md` |
| Armement et équipements (agrément, FIA, formation continue) | `../references/armement-equipements.md` |
| Vidéoprotection (autorisation, exploitation, conservation) | `../references/videoprotection.md` |
| RH spécificités PM (cycles atypiques, ISF — hors statutaire général) | `../references/rh-specificites-pm.md` |
| Pilotage et budget du service | `../references/pilotage-budget.md` |
| Conformité, déontologie et données (RGPD, code de déontologie PM) | `../references/conformite-deontologie-donnees.md` |
| Écrits professionnels — pilote la couche 4 (typologie, mentions obligatoires, valeur probante) | `../references/ecrits-professionnels.md` |
| **Posture** — Contrôle de légalité (relecture a priori, avant production d'acte) | `../references/controle-legalite.md` |
| **Posture** — Contentieux (anticipation adversariale après / pendant production) | `../references/contentieux.md` |
| **Posture** — RETEX (retour d'expérience post-intervention, pilotage/apprentissage) | `../references/retex.md` |

### Couche 3 — Objets métier (fiches système expert)

| Besoin | Fichier repo |
|--------|--------------|
| Gabarit imposé d'un objet (6 sections, agrège et pointe) | `../objets/_gabarit-objet.md` |
| Débits de boissons et commerces réglementés | `../objets/commerce.md` |
| Manifestation / événement sur la voie publique | `../objets/manifestation.md` |
| Occupation du domaine public | `../objets/occupation-domaine-public.md` |
| Agent PM (pouvoirs, équipement, conduite à tenir) | `../objets/agent.md` |
| Accident (constatation, conséquences) | `../objets/accident.md` |
| Fourrière (mise en fourrière de véhicule) | `../objets/fourriere.md` |
| Vidéoprotection — cas d'usage opérationnel | `../objets/videoprotection.md` |
| Police des chiens dangereux | `../objets/police-chiens.md` |

### Couche 4 — Générateurs interactifs d'écrits

| Besoin | Fichier repo |
|--------|--------------|
| PV de contravention | `../assets/pv-contravention.md` |
| Rapport d'information | `../assets/rapport-information.md` |
| Rapport de mise à disposition (art. 73 CPP) | `../assets/rapport-mise-a-disposition.md` |
| Arrêté (modèle) — acte faisant grief | `../assets/arrete-modele.md` |
| Note au maire (modèle) | `../assets/note-maire-modele.md` |

### Hors couches — gouvernance et tests

| Besoin | Fichier repo |
|--------|--------------|
| Cas de co-activation (dpm-fpt / drh-fpt / recherche-juridique) | `../tests/cas-co-activation.md` |
| Jeu de cas de test structuré | `../tests/cas-de-test.json` |
| Barème de passage des 14 cas (attendus critiques, score de suite) | `../tests/bareme-cas-de-test.md` |
| Historique des versions (semver) | `../CHANGELOG.md` |
| Journal des cas significatifs (apprentissage, anonymisé) | `../JOURNAL.md` |
| ADR — adoption du pattern drh-fpt | `../docs/adr/0001-adoption-pattern-drh-fpt.md` |
| ADR — frontière dpm-fpt / drh-fpt | `../docs/adr/0002-frontiere-dpm-drh.md` |
| Présentation générale du repo | `../README.md` |

## Voir aussi

- [[maillage]] — carte des liens objets ↔ branches ↔ générateurs, nœuds transverses (garde-fou APJA, frontière drh-fpt).
