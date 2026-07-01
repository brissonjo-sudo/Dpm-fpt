# Objet métier — Vidéoprotection / Centre de supervision urbain (v0.1.0)

**Situation type** : Installation, exploitation et renouvellement d'un système de vidéoprotection sur voie publique ou dans un lieu ouvert au public ; autorisation préfectorale ; accès et transmission des images ; droits des personnes filmées.

**[Risque / Confiance]** — Risque **élevé** (autorisation préfectorale obligatoire, conformité RGPD, durée de conservation encadrée, droit d'accès des personnes). Confiance **stable** sur le cadre général d'autorisation (architecture CSI), **à vérifier** sur les valeurs chiffrées (délais, durée de conservation, délai de saisine), les finalités légales (liste modifiable) et la composition de la commission départementale.

---

## 1. Acteurs et autorités compétentes

| Acteur | Rôle | Compétence |
|--------|------|-----------|
| **Maire** (ou président d'EPCI) | Autorité de demande | Porteur du projet de vidéoprotection ; demande l'autorisation préfectorale ; assure la conformité d'exploitation ; reste titulaire du pouvoir de police générale |
| **Préfet** (ou préfet de police à Paris) | Autorité d'autorisation | Délivre l'autorisation après avis de la commission départementale ; fixe les conditions opérationnelles (périmètre, durée, habilitations) dans l'arrêté |
| **Commission départementale de vidéoprotection** | Organe consultatif | Rend un avis préalable sur la demande ; composée d'un magistrat (président), de représentants de l'État, de collectivités et de la société civile (composition réglementaire à vérifier) |
| **Directeur de police municipale (DPM)** | Chef de service | Organise le centre de supervision urbain (CSU) ; supervise les habilitations des agents ; assure la traçabilité des accès et des extractions ; détermine les responsables de traitement données |
| **Agents de police municipale** (CSU) | Opérateurs | Visionnent les images dans le cadre strict de l'autorisation ; doivent être **individuellement habilités et désignés** ; traçabilité de chaque accès obligatoire |
| **CNIL** | Autorité de contrôle | Contrôle la conformité RGPD, l'AIPD, la traçabilité des consultations ; reçoit les plaintes sur violation de droits d'accès |
| **Commerçants** (cas particulier) | Porteurs de projet alternatifs | Peuvent installer un système sur les abords immédiats de leur établissement **après information du maire** (pas une autorisation municipale) ; reste soumis à l'autorisation préfectorale |

**Conflit de compétence possible** : Un maire qui installe sans autorisation préfectorale ou hors du périmètre autorisé commet une irrégularité opposable. Ne jamais présumer que l'information d'une commission interne (police, sécurité) vaut autorisation officielle.

---

## 2. Textes applicables

### Régime d'autorisation et cadre général
- **`../references/videoprotection.md`** — Code de la sécurité intérieure (CSI), **Livre II, Titre V**, articles L. 251-1 à L. 253-5 (*vérifié Légifrance 30/06/2026*, identifiants LEGIARTI relevés pour les articles clés : L. 252-1 LEGIARTI000047569469 ; L. 251-2 LEGIARTI000041599395 ; L. 252-2 LEGIARTI000047569434 ; L. 252-3 LEGIARTI000043540807 ; L. 252-5 LEGIARTI000025505435 (**plafond de conservation d'un mois**) ; L. 253-5 LEGIARTI000038791144 — **à recontrôler en version consolidée** avant tout usage en acte). Autorisation préfectorale obligatoire ; finalités limitativement énumérées ; commission départementale d'avis ; **durée de conservation plafonnée à un mois (art. L. 252-5 CSI)**.

### Conformité données, RGPD, AIPD et traçabilité
- **`../references/conformite-deontologie-donnees.md`** — Régime RGPD (règlement UE 2016/679, loi Informatique et Libertés, directive police-justice le cas échéant) ; AIPD obligatoire avant déploiement ; traçabilité des consultations et des extractions ; accès des personnes concernées (CRPA / droit d'accès RGPD) ; incident de violation de données (notification CNIL, délai à vérifier).

### Articulation avec la procédure pénale
- **`../references/penal-procedure.md`** — Extraction d'images sur réquisition judiciaire (ordonnance du juge d'instruction ou du procureur) ; suspension de la destruction en cas de procédure en cours ; transmission des images aux forces de l'État ; garde-fou APJA en cas d'exploitation active (rapprochements, analyses poussées) dépassant la simple transmission.

### Continuum de sécurité et convention de coordination
- **`../references/continuum-partenariats.md`** — Convention de coordination PM / forces de l'État (police nationale, gendarmerie) ; transmission en temps réel des images du CSU ; modalités de partage et d'habilitations croisées ; points de contact permanents.

---

## 3. Procédures, étapes et délais

### 3.1 Demande d'autorisation préfectorale (première installation ou extension)

| Étape | Acteur | Action | Point de contrôle |
|-------|--------|--------|-------------------|
| **Phase 1 — Élaboration du projet** | Maire / DPM | Définir le périmètre (lieux filmés, plan de situation), identifier la ou les **finalités légales** (à choisir parmi la liste CSI L. 251-2) | Finalité parmi la liste fermée ; cohérence avec le risque identifié |
| **Phase 2 — Dossier de demande** | Maire | Constituer le dossier selon les pièces réglementaires (à vérifier : partie réglementaire CSI articles R. 251 et s.) ; prévoir la durée de conservation envisagée, les habilitations, les mesures de sécurité du CSU | Pièces complètes ; absence de pièce = demande rejetée ou suspendue |
| **Phase 3 — Dépôt à la préfecture** | Maire (ou DPM en qualité de responsable local) | Transmettre le dossier au préfet | Date de dépôt ; accusé de réception |
| **Phase 4 — Saisine de la commission départementale** | Préfet | Le préfet saisit la commission pour avis | Avis rendu dans un délai (à vérifier ; ordre de grandeur : 2-3 mois, jamais affirmer de mémoire) |
| **Phase 5 — Décision de l'autorisation** | Préfet | Arrêté préfectoral fixant : périmètre, finalité(s), durée de validité (à vérifier), durée de conservation des images (en jours, plafonné légalement), habilitations des agents, mesures de sécurité | Arrêté reçu par la commune ; constitue le document de référence unique |
| **Phase 6 — Mise en service** | DPM | Organisation du CSU selon l'arrêté ; habilitations individuelles nominatives ; mise en place de la traçabilité | Conformité stricte avec l'arrêté |
| **Phase 7 — Suivi opérationnel** | DPM | Journal des accès, des extractions, des destructions ; respect des durées de conservation | Aucune exploitation hors périmètre autorisé |

**Hypothèses à annoncer** :
- Délai exact de saisine de la commission : **à vérifier en version consolidée**.
- Délai exact d'instruction par la commission : **à vérifier en version consolidée**.
- Délai de validité de l'autorisation : **à vérifier en version consolidée** (durée type fixée par décret, jamais de mémoire).
- Pièces exactes du dossier de demande : **à vérifier en version consolidée** (partie réglementaire R. 251 et s., ne pas les lister de mémoire).

### 3.2 Renouvellement avant expiration

1. **Anticipation** : consulter l'arrêté actuel ; identifier la date d'expiration ; anticiper le dépôt (délai de instruction à vérifier, potentiellement plusieurs mois) pour éviter une interruption de service.
2. **Dossier de renouvellement** : actualiser le dossier si le projet n'a pas changé substantiellement (même périmètre, même finalité, même durée de conservation) ; ajouter un bilan opérationnel (incidents, améliorations) si utile.
3. **Transmission et décision** : même processus qu'une première demande (saisine commission, avis, arrêté de renouvellement).

### 3.3 Modification substantielle de l'autorisation

- **Extension de périmètre** (ajout de caméras, nouvelle zone) : nouvelle demande ou demande de modification selon le seuil (à vérifier) → traiter comme une extension, ne pas présumer que la modification est mineure.
- **Changement de finalité** : nouvelle demande obligatoire ; ne jamais exploiter en dehors des finalités autorisées.
- **Réduction de durée de conservation** : demande de modification simplifiée possible (vérifier le régime).
- **Augmentation de la durée de conservation** : nouvelle demande (plus restrictive que la réduction).

### 3.4 Exploitation du CSU — accès et traçabilité

1. **Habilitations nominatives** : chaque agent autorisé à visionner doit être **individuellement désigné** dans une liste tracée (pas d'habilitation générique au service) ; habilitation donnée par écrit, mentionnant l'identité, la fonction, la date de début/fin éventuelle.
2. **Journal des accès** : enregistrement de chaque connexion au système (identité de l'agent, date, heure, durée, actions effectuées — consultation, extraction, téléchargement) ; conservation du journal selon un délai (à vérifier, en général plus long que celui des images).
3. **Accès des forces de l'État** : selon la convention de coordination et l'arrêté préfectoral, les agents de police nationale ou de gendarmerie peuvent accéder en temps réel ou sur demande — modalités à formaliser.
4. **Extraction pour une procédure judiciaire** : sur réquisition (ordonnance du juge d'instruction ou demande du procureur), extraction des images concernées, transmission sous enveloppe fermée, accusé de réception ; la réquisition **suspend la destruction** des images extractées jusqu'à fin de la procédure.
5. **Destruction des images** : à l'échéance fixée par l'autorisation, **sauf réquisition en cours** ; destruction documentée (date, modalités) ; attestation de destruction conservée.

### 3.5 Accès des personnes filmées

- **Droit de droit** : une personne intéressée peut demander l'accès aux images la concernant ou vérifier leur destruction → réponse dans un délai (à vérifier, potentiellement 1-2 mois).
- **Motifs de refus limitatifs** : sûreté de l'État, défense nationale, sécurité publique, procédure judiciaire en cours, droits des tiers (autres personnes filmées) → tout refus doit être motivé sur l'un de ces motifs.
- **Recours** : la personne peut saisir la **commission départementale de vidéoprotection** ou la **CNIL**, ou le juge (recours gracieux, puis en référé).

---

## 4. Écrits associés

### Écrits de demande et de projet
- **Dossier de demande d'autorisation préfectorale** : à constituer selon les pièces réglementaires (parties réglementaires CSI) ; brouillon `[INCOMPLET]` si une pièce manque (plan de situation, note de présentation, estimation de durée de conservation, calendrier, budget, sécurité du CSU).
- **Note au maire** — `../assets/note-maire-modele.md` : opportunité du projet, choix de la finalité (avec justification du risque identifié), articulation avec la convention de coordination existante, impacts RGPD, coût d'exploitation, calendrier de demande d'autorisation.

### Écrits opérationnels du CSU
- **Fiche de procédure CSU** : organisation du centre (locaux, accès physiques, droits informatiques), habilitations individuelles (liste nominative tracée), traçabilité des accès (journal, modalités, conservation), modalités de transmission aux forces de l'État, procédure d'extraction sur réquisition, destruction programée des images.
- **Registre de traitement (RGPD)** : partie du registre des traitements de la commune, détaillant le traitement « vidéoprotection » (finalités, données, destinataires, durée, mesures de sécurité, DPO).
- **Analyse d'impact (AIPD)** — si obligatoire : description du système, évaluation des risques pour les droits et libertés, mesures pour les mitiger, validation avant mise en service → renvoi à `../references/conformite-deontologie-donnees.md` pour la méthodologie CNIL.

### Écrits de réponse aux demandes d'accès et recours
- **Réponse à une demande d'accès aux images** (art. L. 253-5 CSI) : accès de droit si aucun motif de refus limitatif ne s'applique ; sinon, courrier de refus **motivé** sur l'un des motifs légaux ; information des voies de recours (commission départementale, CNIL, juge).
- **Réponse à une demande d'accès CRPA** : distinction entre demandeur (administré tiers, ou personne intéressée cherchant accès à ses propres données) ; application de la grille CRPA (exceptions sécurité publique, procédure judiciaire) + droit d'accès RGPD.
- **Signalement RGPD au DPO** : en cas d'incident (accès non autorisé, extraction hors cadre, destruction hors délai), fiche d'incident adressée au délégué à la protection des données (DPO).

### Actes faisant grief (le cas échéant)
- Un éventuel **arrêté municipal limitant l'accès au CSU** ou fixant des modalités restrictives : motivation + voies et délais de recours + vérification du contrôle de légalité → `controle-legalite.md` avant production.

---

## 5. Jurisprudence clé

Voir **`recherche-juridique`** pour :
- **Contrôle de la légalité d'une autorisation préfectorale** : défaut de motivation, incompatibilité de la finalité invoquée avec le projet réel, périmètre disproportionné au risque identifié.
- **Contentieux du droit d'accès** : refus de communication d'images jugé infondé (motif de refus non applicable), délai de réponse dépassé.
- **Responsabilité du service** en cas de fuite ou d'utilisation abusive des images : violation du RGPD, exploitation à titre personnel, transmission non autorisée.
- **Proportionnalité du système** : un système excessivement intrusif par rapport à la finalité pourrait être annulé (jurisprudence administrative sur les atteintes aux libertés).
- **Exploitation algorithmique** (reconnaissance faciale, LAPI) : fondement distinct et plus restrictif que la vidéoprotection seule → ne pas présumer la légalité d'un algorithme du seul fait de l'autorisation vidéoprotection.

Thèmes sensibles à signaler en amont :
- **Articulation avec la présomption d'innocence** : un système de vidéoprotection ne crée pas de culpabilité ; les images restent des éléments de preuve dont l'interprétation relève de l'autorité judiciaire.
- **Protection des données sensibles** : les images peuvent révéler des données sensibles (santé, identité religieuse, etc.) → exigence de sécurité renforcée du CSU.

---

## 6. Check-list opérationnelle

### Avant de demander l'autorisation préfectorale
- [ ] **Finalité légale** identifiée parmi la liste fermée (CSI L. 251-2) et justifiée par un risque réel et proportionné ?
- [ ] **Autorité compétente** : préfet du département (ou préfet de police à Paris) — pas le maire seul ?
- [ ] **Périmètre** (lieux filmés) délimité avec précision sur un plan (voie publique ? lieu ouvert au public ? combien de caméras ?) ?
- [ ] **Dossier de demande** complet selon la partie réglementaire CSI (à vérifier pièces exactes : ne pas affirmer de mémoire) ?
- [ ] **Durée de conservation** envisagée cohérente avec la finalité et inférieure au plafond légal (à vérifier le plafond, jamais affirmer de mémoire) ?
- [ ] **CSU et sécurité du système** : accès physiques sécurisés, droits informatiques restreints, sauvegarde des journaux de traçabilité ?
- [ ] **Convention de coordination** avec les forces de l'État existante ou en cours de négociation (si transmission en temps réel prévue) ?
- [ ] **AIPD** envisagée ou en cours de conduite si le système présente un risque élevé (vidéoprotection étendue, reconnaissance faciale) ?

### En cours d'exploitation
- [ ] **Habilitations nominatives** de chaque agent du CSU mises à jour et tracées (liste signée, dates de début/fin) ?
- [ ] **Journal des accès** conservé et audité régulièrement (identité, date, action, durée) ?
- [ ] **Arrêté préfectoral** consulté avant chaque action (périmètre, finalités autorisées, destinataires, durée de conservation) ?
- [ ] **Modification substantielle** de périmètre, finalité ou durée : nouvelle demande d'autorisation demandée **avant** mise en œuvre, jamais après ?
- [ ] **Réquisitions judiciaires** reçues et exécutées : copie des images transmise sous enveloppe fermée, accusé de réception, durée de conservation suspendue jusqu'à fin de procédure ?
- [ ] **Destruction des images** effectuée à l'échéance, documentée (date, preuve de destruction technique), sauf procédure en cours ?

### En cas de demande d'accès d'une personne filmée
- [ ] **Demandeur** identifié : personne intéressée par les images ou tiers cherchant accès à un document administratif ?
- [ ] **Motif de refus** (si applicable) parmi la liste fermée (sûreté de l'État, défense, sécurité publique, procédure judiciaire, droits des tiers) et bien motivé ?
- [ ] **Délai de réponse** respecté (à vérifier le délai exact réglementaire, ne pas le donner de mémoire) ?
- [ ] **Information** sur les voies de recours (commission départementale, CNIL, juge) fournie en cas de refus ?

### En cas d'incident RGPD ou manquement
- [ ] **Incident qualifié** : accès non autorisé ? extraction hors cadre ? destruction prématurée ? visionnage sans habilitation ?
- [ ] **DPO notifié** immédiatement (violation potentielle de données, délai de notification à vérifier : ordre de grandeur 72 heures) ?
- [ ] **Journal des accès** et **dossier système** conservés pour enquête interne ?
- [ ] **Garde-fou APJA** testé si l'exploitation active du CSU dépasse la simple constatation/transmission (rapprochement de plaques, analyses biométriques) ?

### Avant toute sortie — Garde-fou APJA
- [ ] L'exploitation du CSU relève-t-elle **uniquement de la constatation et de la transmission** (rôle APJA) ou franchit-elle ce cadre (analyse poussée, rapprochement actif, demande à l'OPJ d'effectuer des actes réservés) ?
- [ ] Si **dépassement détecté** (exploitation pénale active hors cadre APJA) → **STOP** affiché **en priorité** : « Cet acte relève de la compétence exclusive de l'OPJ (Police Nationale / Gendarmerie). Mise à disposition immédiate et figement des lieux. »

### Contrôles transverses
- [ ] **Commission départementale de vidéoprotection** : composition et modalités de saisine vérifiées à la préfecture (ne pas inventer de mémoire) ?
- [ ] **Tout numéro d'article cité** assorti de « à confirmer en version consolidée » ou « vérifié sur Légifrance le 30/06/2026 » (identifiants LEGIARTI cités) ?
- [ ] **Références vers les branches partenaires** (`videoprotection.md`, `conformite-deontologie-donnees.md`, `continuum-partenariats.md`, `penal-procedure.md`) effectuées sans duplication ?
- [ ] **Couple [risque / confiance]** clairement indiqué dans les conclusions ?
- [ ] **Cas journalisable** (lacune dans les délais, extension non autorisée détectée, incident de destruction prématurée) → identifié pour `JOURNAL.md` ?

---

## Références et remontées

**Branche principale** : La vidéoprotection repose sur trois socles indissociables :
1. **Cadre d'autorisation** (CSI, branche `videoprotection.md`) — c'est l'ossature.
2. **Conformité données** (RGPD, AIPD, CRPA, branche `conformite-deontologie-donnees.md`) — c'est le contrôle interne.
3. **Procédure judiciaire** (extraction sur réquisition, suspension de destruction, branche `penal-procedure.md`) — c'est le basculement vers l'OPJ.

Ne jamais traiter un de ces trois volets en isolation.

**Coordination impérative** :
- Avant chaque **modification substantielle** du système : passer par la demande préfectorale complète (ne pas présumer que l'extension est mineure).
- En cas de **demande d'accès** : croiser CRPA + droit d'accès RGPD + régime CSI spécifique (trois grilles, une seule réponse).
- En cas d'**incident RGPD** : notification immédiate du DPO et évaluation de la nécessité d'informer la CNIL (délai à vérifier).
- En cas de **réquisition judiciaire** : transmission immédiate, suspension de destruction, archivage de la réquisition comme justificatif de conservation.

**Mise à jour requise** :
- **Régime d'autorisation CSI** (articles L. 251 à L. 253) : révision lors de réformes législatives (évolutions fréquentes sur ce titre).
- **Partie réglementaire** (articles R. 251 et s., R. 252 et s., R. 253 et s.) : composition de la commission, pièces du dossier, délais — à vérifier chaque année.
- **AIPD et méthodologie CNIL** : mise à jour des référentiels CNIL en cas d'évolution des critères de risque.
- **Convention de coordination PM / forces de l'État** : renouvellement au minimum tous les 2-3 ans ; articulation avec le CSU à clarifier à chaque révision.
