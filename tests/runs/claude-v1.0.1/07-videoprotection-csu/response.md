# Extension du réseau de vidéoprotection + transmission d'images en direct au commissariat

## 0. Routage (couche 1 — `analyse-situation.md`)

**Qualification des faits** : projet d'extension d'un système de vidéoprotection de voie publique existant, avec ajout d'une fonctionnalité de **transmission d'images en temps réel** vers le commissariat (police nationale) et question sur les **habilitations de visionnage au CSU**.

- **Police générale ou spéciale** : police spéciale de l'État (vidéoprotection, CSI Livre II Titre V), et non police générale du maire.
- **Autorité compétente** : le **préfet de département** (préfet de police à Paris) délivre et modifie l'autorisation ; le **maire** reste porteur du projet/demandeur, pas décideur.
- **Conflit de compétence détecté (maire / préfet)** : à signaler explicitement — une extension mise en œuvre sans autorisation préfectorale préalable, ou hors périmètre autorisé, constitue une **irrégularité opposable**, y compris si le maire l'a décidée seul en conseil municipal. La transmission en direct au commissariat est elle-même soumise à ce même régime : elle doit être **prévue par l'arrêté préfectoral**, pas seulement par un accord informel entre le DPM et le commissariat.
- **Garde-fou APJA (§5.2 SKILL.md)** : **testé, non déclenché**. Aucun acte réservé à l'OPJ (garde à vue, audition formelle, perquisition, réquisition judiciaire) n'est demandé ici — il s'agit d'une procédure administrative d'autorisation et d'organisation du CSU. Point de vigilance à rappeler néanmoins pour la doctrine d'exploitation du CSU (§5 ci-dessous) : dès que l'exploitation des images en direct sort de la simple **constatation/transmission** (rapprochement actif, analyse poussée, tri opérant comme une enquête), le garde-fou s'active et bascule vers `penal-procedure.md`.
- **Branches / objets mobilisés** : `references/videoprotection.md` (branche), `objets/videoprotection.md` (objet système expert), `references/conformite-deontologie-donnees.md` (RGPD/AIPD, transverse), `references/continuum-partenariats.md` (convention de coordination pour la transmission temps réel), `references/controle-legalite.md` (avant tout acte produit).
- **[Risque / Confiance]** : **Risque élevé** (autorisation préfectorale obligatoire, RGPD, durée de conservation encadrée) ; **Confiance stable** sur l'architecture générale de la procédure, **à vérifier** sur les valeurs chiffrées (délais d'instruction, seuil de modification substantielle, composition de la commission départementale).

---

## 1. Recommandation opérationnelle

### A. Sur l'extension du réseau

1. Ne pas traiter l'extension comme un ajout technique mineur : une extension de périmètre / ajout significatif de caméras est en principe une **modification substantielle** de l'autorisation existante, ce qui impose une **nouvelle demande ou une demande de modification** auprès de la préfecture — ne jamais présumer qu'un simple courrier d'information suffit (seuil précis de « modification substantielle » **à vérifier en version consolidée**).
2. Reprendre le dossier depuis l'origine sur les points suivants avant tout dépôt :
   - **finalité(s) légale(s)** invoquée(s) pour les nouvelles caméras — doit correspondre à l'une des finalités **limitativement énumérées** (art. L. 251-2 CSI) ; une finalité de « surveillance générale » sans risque identifié fragilise le dossier ;
   - **périmètre exact** (plan de situation, nombre et emplacement des caméras) ;
   - **durée de conservation envisagée**, sous le plafond légal (art. L. 252-5 CSI, plafond d'**un mois**, hors procédure judiciaire en cours) ;
   - **habilitations de visionnage envisagées**, y compris pour les nouveaux destinataires (police nationale) — voir point B.
3. Déposer le dossier auprès du **préfet de département** (préfet de police à Paris), qui statue **après avis de la commission départementale de vidéoprotection** (avis consultatif). Pièces exactes du dossier réglementaire, délai d'instruction et délai de saisine de la commission : **à vérifier en version consolidée** (partie réglementaire du CSI), ne jamais les indiquer de mémoire dans un courrier ou une note.
4. Le **maire n'autorise pas** l'extension : il est porteur du projet (demandeur), le pouvoir de décision reste au préfet. Éviter toute formulation qui laisserait entendre qu'une délibération municipale suffit à elle seule.

### B. Sur la transmission en direct au commissariat et le visionnage au CSU

1. La transmission d'images en temps réel vers les forces de l'État **n'est pas de droit** : elle n'est possible que **si l'arrêté préfectoral la prévoit expressément**, avec ses modalités (art. L. 252-2 CSI). Il faut donc que la demande de modification d'autorisation **mentionne explicitement** cette destination et ces modalités — ne pas la mettre en œuvre techniquement avant que l'arrêté modifié ne le permette.
2. **Qui peut visionner** — principe d'habilitation individuelle et nominative :
   - au CSU : uniquement des **agents de police municipale individuellement désignés et habilités**, selon les conditions fixées par l'arrêté — jamais une habilitation générique « service CSU » ;
   - côté commissariat : les **policiers nationaux** (ou gendarmes le cas échéant) ne peuvent visionner que s'ils sont eux aussi **individuellement désignés et habilités** dans les conditions prévues par l'arrêté (art. L. 252-2 CSI). Un accès « ouvert » au commissariat sans liste nominative d'agents habilités est une irrégularité.
   - un agent PM non habilité ne visionne pas, même en présence d'un collègue habilité, sauf disposition contraire expresse de l'arrêté.
3. **Formaliser la coordination** : au-delà de l'autorisation CSI elle-même, les modalités opérationnelles de la transmission temps réel (horaires, protocole d'alerte, désignation croisée des agents habilités, traçabilité partagée) doivent être inscrites dans la **convention de coordination** police municipale / police nationale (ou un avenant si elle existe déjà) — `references/continuum-partenariats.md`. La convention **ne crée aucun pouvoir nouveau** : elle organise l'exercice de ce que l'arrêté préfectoral autorise déjà.
4. **Traçabilité** : mettre en place ou vérifier le journal des accès et des extractions (identité, date, heure, action) pour l'ensemble des agents habilités, PM et police nationale, dès l'ouverture de la transmission en direct.
5. **Volet RGPD/AIPD** (transverse, non traité dans la branche vidéoprotection elle-même) : l'extension du système et l'ajout d'un nouveau destinataire (police nationale) constituent un changement de traitement à documenter — mise à jour du **registre des traitements**, examen de la nécessité d'une **AIPD** (probable au vu de l'extension + nouveau flux de transmission), information du **DPO/délégué à la protection des données** avant mise en service → `references/conformite-deontologie-donnees.md`.
6. **Réquisition judiciaire en cours** : si des images sont extraites pour une procédure, la destruction est **suspendue** — coordination avec `references/penal-procedure.md` ; l'extraction et la remise sur réquisition relèvent de la procédure pénale, toute exploitation active allant au-delà de la simple transmission bascule vers le garde-fou APJA (§5.2 SKILL.md).

### C. Écrits à produire

- **Note au maire** — opportunité et calendrier de l'extension, choix de la finalité, articulation avec la convention de coordination, impact RGPD/coût → gabarit `references/templates/note-maire-modele.md`. Passer par `references/controle-legalite.md` avant rédaction.
- **Dossier de demande de modification d'autorisation préfectorale** — brouillon `[INCOMPLET]` tant que finalité, plan, durée de conservation et habilitations envisagées ne sont pas toutes levées (ne jamais halluciner une pièce manquante).
- **Avenant à la convention de coordination** (ou convention si elle n'existe pas / est obsolète) — modalités de transmission temps réel et d'habilitation croisée.
- **Fiche de procédure CSU** — mise à jour des habilitations nominatives, de la traçabilité et des modalités de transmission.
- Le cas échéant, **registre de traitement / AIPD** — via `conformite-deontologie-donnees.md`.

---

## 2. Fondements juridiques

> Discipline de sourçage appliquée : les identifiants suivants sont soit repris du socle **`references/references-verifiees.md`** (vérification Légifrance du **30/06/2026**, complément du **01/07/2026**), soit **vérifiés directement sur Légifrance dans la présente session le 28/07/2026**. Toute autre valeur (délais, seuils, composition de commission) reste marquée « à confirmer en version consolidée », conformément au socle-sources (`SKILL.md` §5.3).

- **Art. L. 252-1, Code de la sécurité intérieure** — installation d'un système de vidéoprotection subordonnée à l'autorisation du préfet (préfet de police à Paris), après avis de la commission départementale de vidéoprotection. **Vérifié sur Légifrance le 28/07/2026** (identifiant **LEGIARTI000037825998**, version en vigueur depuis le **21/05/2023**, loi n° 2023-380 du 19/05/2023) — cet identifiant précise et actualise la mention générique « à relever à nouveau au moment de l'usage » figurant dans `references/videoprotection.md` §4.1/§9.
- **Art. L. 251-2, CSI** — liste limitative des finalités légales pouvant fonder l'autorisation ; cas particulier « commerçants » (information du maire, non-assimilable à une autorisation municipale). Identifiant **LEGIARTI000041599395**, en vigueur depuis le 21/05/2023 (`references-verifiees.md`, vérifié 01/07/2026).
- **Art. L. 252-2, CSI** — l'autorisation fixe elle-même les conditions opérationnelles : qualité et habilitation individuelle des personnes chargées de l'exploitation et du visionnage (agents PM, et le cas échéant policiers nationaux/gendarmes désignés et habilités dans les mêmes conditions) ; fondement direct de la règle « qui peut visionner » et de la transmission vers les forces de l'État. Identifiant **LEGIARTI000047569434**, en vigueur depuis le 21/05/2023 (`references-verifiees.md`, vérifié 01/07/2026).
- **Art. L. 252-3, CSI** — accès et transmission des enregistrements. Identifiant **LEGIARTI000043540807**, en vigueur depuis le 27/05/2021 (`references-verifiees.md`, vérifié 01/07/2026).
- **Art. L. 252-5, CSI** — destruction des enregistrements dans un délai maximum fixé par l'autorisation, **plafonné à un mois**, hors enquête de flagrance/préliminaire ou information judiciaire. Identifiant **LEGIARTI000025505435**, en vigueur depuis le 01/05/2012 (`references-verifiees.md`, vérifié 01/07/2026).
- **Art. R. 252-3, CSI** — le dossier de demande doit **mentionner** la durée de conservation retenue ; ne fixe pas lui-même le plafond (celui-ci relève de l'art. L. 252-5). Identifiant **LEGIARTI000048480362**, en vigueur depuis le 30/11/2023 (`references-verifiees.md`, vérifié 01/07/2026).
- **Art. L. 253-5, CSI** — droit d'accès des personnes filmées aux enregistrements les concernant, sous réserve de motifs de refus limitatifs. Identifiant **LEGIARTI000038791144**, en vigueur depuis le 21/05/2023 (`references-verifiees.md`, vérifié 01/07/2026) — non directement en cause dans la présente question, mais à rappeler si des administrés s'interrogent sur les nouvelles caméras.
- **Art. L. 512-4, CSI et s.** — convention de coordination police municipale / forces de sécurité de l'État, cadre de formalisation des modalités de transmission en temps réel. Identifiant **LEGIARTI000043540466**, vérifié sur Légifrance le 30/06/2026 (`references-verifiees.md`) — **seuil d'effectif rendant la convention obligatoire et durée de validité : à confirmer en version consolidée**, ce seuil ayant déjà évolué par réforme.

**Non vérifié dans cette session — à confirmer en version consolidée avant tout acte** :
- pièces réglementaires exactes du dossier de demande (partie réglementaire du CSI, art. R. 251 et s.) ;
- délai d'instruction et délai de saisine de la commission départementale ;
- composition exacte de la commission départementale de vidéoprotection ;
- seuil précis déclenchant l'obligation d'une nouvelle demande vs simple modification de l'autorisation existante ;
- seuil d'effectif rendant la convention de coordination obligatoire et sa durée de validité.

---

## 3. Points de vigilance (pièges fréquents signalés par la branche)

1. Le **maire n'autorise pas** l'extension : il ne fait que porter la demande — piège de confusion fréquent avec le régime « commerçants » (simple information du maire).
2. La **transmission temps réel** vers le commissariat n'est légale que si l'**arrêté préfectoral la prévoit** — un accord opérationnel informel entre DPM et commissariat, sans base dans l'arrêté, est irrégulier.
3. Habilitation de visionnage **strictement nominative**, jamais générique au service, y compris côté police nationale.
4. Ne jamais affirmer une durée de conservation chiffrée pour les nouvelles caméras sans vérifier l'arrêté applicable et son plafond légal (1 mois, art. L. 252-5, sous réserve d'une réquisition judiciaire en cours).
5. Ne pas traiter le volet RGPD/AIPD dans la branche vidéoprotection : renvoyer systématiquement à `conformite-deontologie-donnees.md`.
6. Garde-fou APJA à rappeler pour la doctrine d'exploitation du CSU une fois la transmission en direct ouverte : la simple **constatation et transmission** reste dans le cadre APJA ; toute exploitation active (rapprochement, analyse) au-delà de ce cadre bascule vers `penal-procedure.md`.

---

## 4. Renvois des fichiers du skill mobilisés

- `references/analyse-situation.md` — routeur, garde-fou APJA testé, conflit de compétence maire/préfet signalé.
- `references/videoprotection.md` — branche de fond : régime d'autorisation préfectorale, finalités, durée de conservation, habilitation de visionnage.
- `objets/videoprotection.md` — objet système expert : acteurs, procédure détaillée (phases 1 à 7), check-lists opérationnelles CSU.
- `references/conformite-deontologie-donnees.md` — RGPD/AIPD, registre de traitement, DPO (à mobiliser pour le volet données de l'extension et du nouveau flux vers le commissariat).
- `references/continuum-partenariats.md` — convention de coordination PM / police nationale, cadre de formalisation de la transmission temps réel.
- `references/penal-procedure.md` — coordination en cas de réquisition judiciaire sur les images ou d'exploitation dépassant le cadre APJA.
- `references/controle-legalite.md` — à dérouler avant toute production d'acte (note au maire, éventuel arrêté municipal connexe).
- `references/templates/note-maire-modele.md` — gabarit pour la note au maire sur l'opportunité et le calendrier du projet.
- `references/references-verifiees.md` — socle des identifiants Légifrance vérifiés (§3, vidéoprotection) mobilisés ci-dessus.

**[Risque / Confiance] de synthèse** : élevé sur le principe d'autorisation, la transmission temps réel et les habilitations de visionnage / stable sur l'architecture générale de la procédure, à vérifier sur les délais, seuils et pièces réglementaires avant tout dépôt de dossier ou tout acte engageant la commune.
