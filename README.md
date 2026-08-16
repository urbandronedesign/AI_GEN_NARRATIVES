# Récits génératifs — le manuel de production du court métrage par IA

Manuel de production bilingue (FR/EN) pour produire un **court métrage par IA génératives**, de l'écriture au mixage. Un cours de **compétences techniques**, écrit pour des étudiants en design **de la première à la cinquième année**.

Le film peut se passer dans un **lieu réel que l'étudiant documente** ou dans un **monde entièrement inventé** — anticipation, fable, abstraction. Les deux voies sont traitées, et le pipeline technique est le même à partir du chapitre 7.

### 📖 **[Lire en ligne → urbandronedesign.github.io/AI_GEN_NARRATIVES](https://urbandronedesign.github.io/AI_GEN_NARRATIVES/)**

C'est le lien à donner aux étudiants — aucun téléchargement, aucune installation, fonctionne sur un téléphone.

### ⌨️ **[Prompts & modèles →](https://urbandronedesign.github.io/AI_GEN_NARRATIVES/prompts.html)**

Page compagnon : tous les prompts du pipeline prêts à copier, le lexique bilingue de ce qu'il faut écrire pour obtenir ce que l'on veut (« lumière rasante » → `low raking light, long shadows`), et l'état des modèles. Classée par tâche, avec un filtre en direct.

Pour l'usage hors ligne, téléchargez **[`recits_generatifs_manuel-v1.html`](recits_generatifs_manuel-v1.html)** et ouvrez-le dans n'importe quel navigateur. Un seul fichier autonome, ~540 Ko, aucune dépendance, aucune étape de compilation. Fonctionne depuis une clé USB sans connexion.

> **Manuel compagnon** — [3DVIZ · SketchUp & Rhino vers Twinmotion 2026](https://github.com/urbandronedesign/3DVIZ), même format, même conventions. Les deux se lisent de la même façon : bascule FR/EN, recherche, filtre de niveau, index par symptôme.

---

## Ce qu'il contient

**18 chapitres** suivant l'ordre réel de la production — comprendre, réunir le référentiel, écrire, verrouiller, générer l'image, animer, sonoriser, monter — plus une section de référence.

| Partie | Chapitres |
|---|---|
| **Préambule** | Comment utiliser ce manuel · Le projet & ce que vous rendez · **Parcours par année** |
| **I — Fondations** | Le pipeline de bout en bout · Le principe hybride · Le laboratoire · **Le dossier de projet** |
| **II — Le référentiel** | Problématique & brief · **Construire le référentiel** (voie captée / voie construite) |
| **III — L'écriture** | Du brief au pitch · Piloter le LLM · Découpage & feuille de plans |
| **IV — La cohérence** | Les chartes de cohérence · Super-prompt & ancrage |
| **V — L'image** | Générer le storyboard · Contrôle hybride & validation |
| **VI — Le mouvement** | De l'image au plan animé · Contrôle avancé & finition |
| **VII — Son & livraison** | Conception sonore · Montage, étalonnage, export · Droit, éthique & crédits |
| **Référence** | Index Dérive → Correction (36 symptômes) · FAQ Étudiants (30 questions) · Glossaire bilingue (46 termes) |

Soit **21 sections** au total, dont trois de préambule et trois de référence.

Environ **61 500 mots** sur les deux langues.

Le chapitre 1 s'ouvre sur un schéma pleine page de tout le pipeline — sept étapes, les décisions qui appartiennent à chacune, et le **chemin de retour** montrant qu'un défaut constaté en aval a été commis en amont. Le dossier de projet est dessiné comme le contenant de l'ensemble, parce qu'un projet qui n'est pas portable n'est pas vraiment un projet.

## Fonctionnalités

- **Bilingue** — bascule FR/EN, mémorisée entre les visites
- **Recherche côté client** dans les chapitres, la FAQ, l'index des dérives et les blocs de prompt — avec index séparé par langue
- **Filtre par année A1·2 / A3 / A4·5** — les étiquettes sont cumulatives, et le contenu masqué sort aussi de l'index de recherche
- **Blocs de prompt avec bouton Copier** — les étudiants copient des prompts en permanence
- **Index Dérive → Correction** organisé par ce qu'on voit à l'écran, pas par chapitre
- **Feuille de style d'impression** — s'imprime et s'exporte proprement en PDF, avec des sauts de page raisonnables
- **Responsive** — lisible sur un téléphone à 1 h du matin la veille d'un jury
- **Thème clair / sombre**, suit le système par défaut
- Raccourcis : <kbd>/</kbd> pour la recherche, <kbd>Échap</kbd> pour l'effacer

## La structure du cours

Le manuel repose sur **un seul film**, mené à travers **14 étapes**. Trois rendus, quatre en fin de cycle :

| | Livrable |
|---|---|
| **A** | **Le dossier de production** — le référentiel (capté ou construit), feuille de plans, chartes de cohérence, journal de projet |
| **B** | **Le storyboard** — images clés validées, chacune avec son prompt exact et sa graine |
| **C** | **Le film** — son mixé, générique déclarant les outils |
| **D** | *(A4·A5 seulement)* **Un actif réutilisable documenté** légué à l'atelier : un graphe ComfyUI, une LoRA avec son jeu d'images, une reconstruction de site, ou une fiche de technique |

Parce que le dossier de production est rendu, les chapitres de méthode sont **évalués directement** plutôt que d'être une préparation à autre chose. Quatre axes d'évaluation, annoncés dès le préambule : spécificité, cohérence, intention, méthode.

### Deux voies vers le même artefact

Un modèle génératif produit la moyenne de ce qu'il a vu. Pour qu'un film soit le vôtre et non cette moyenne, il faut un **référentiel** : un ensemble d'images et de sons spécifiques, triés et nommés, injectés dans le modèle et dont on tire les chartes de cohérence. Le chapitre 6 en décrit les deux constructions.

| | Voie captée | Voie construite |
|---|---|---|
| **Le monde est** | réel, visitable | inventé — anticipation, fable, abstraction |
| **Le référentiel vient de** | photographies, vidéos et sons pris sur site | images de recherche générées **puis triées**, dessins, maquettes et objets photographiés, textures, références sous licence |
| **Le risque propre** | rester descriptif | rester flottant : un monde sans règles écrites |
| **La discipline propre** | aller chercher la bonne matière | trancher — générer est facile, éliminer est le travail |
| **Produit** | `01_references/` trié, nommé, indexé | *le même* `01_references/` |

Les deux se mélangent, et c'est souvent le plus fort : un monde inventé dont les matières viennent de photographies réelles. À partir du chapitre 7, le manuel ne fait plus la différence.

**Hybride ne veut pas dire documentaire.** Un film de science-fiction dont les décors viennent de maquettes photographiées, dont les bruitages sont enregistrés sur un bureau et dont les mouvements de caméra sortent d'une prévisualisation Blender est *plus* hybride qu'un documentaire produit entièrement au prompt. Ce qui compte n'est pas que le monde soit réel, mais que le matériau qui l'ancre soit celui de l'étudiant.

### Un pipeline, cinq années

Le **pipeline ne change pas** d'un niveau à l'autre — c'est tout l'intérêt d'un seul document : ce qui est appris en première année reste vrai en cinquième, et il n'y a rien à désapprendre. Ce qui change est le format, la profondeur technique et l'exigence d'argumentation. Un première année ne fait pas « un morceau du cours » : il fait *tout le cours, en plus petit*.

| Année | Format | Chartes | Axes hybrides exigés |
|---|---|---|---|
| **A1 · A2** | 30 s · 10 plans | lieu + style, pas de personnage | 1 référentiel · 4 métier |
| **A3** *(format de référence)* | 60 s · 20 plans | les trois | 1 · 3 matière · 4 |
| **A4 · A5** | 60–90 s, 20 plans min. | les trois, versionnées | les quatre, dont 2 contrôle démontré |

Le corps du manuel est écrit pour le format de référence — 60 secondes, vingt plans. La section **Parcours par année** donne, pour chaque niveau, le format, les livrables et un tableau de lecture chapitre par chapitre. Le filtre de la barre d'outils masque directement ce qui n'est pas encore pour le lecteur : un première année voit 92 % du manuel, un troisième année 97 %.

### Pourquoi 3 secondes par plan

C'est la durée qu'un modèle vidéo génère nativement et bien ; au-delà, la dérive s'installe. Vingt plans est assez pour qu'une *méthode* de cohérence soit nécessaire (à cinq plans on s'en sort à l'œil) et assez peu pour qu'un échec reste réparable dans le temps du module.

## Figures

**Huit figures sont des schémas dessinés** — SVG en ligne, bilingues, sans aucune dépendance. Elles couvrent ce qu'une capture d'écran explique mal : le chemin de retour du pipeline, les quatre points d'injection du matériau non génératif dans la chaîne, l'anatomie d'un nom de fichier, la couverture de prise de vue pour une reconstruction 3D, les six échelles de plan, l'anatomie du super-prompt, l'effet de la contrainte par première et dernière image, l'architecture des quatre couches sonores.

**Huit sont des captures d'écran** qui ne peuvent pas être dessinées — les graphes ComfyUI de l'atelier, une planche de charte personnage, une timeline de montage, la feuille de plans en production. Voir **[CAPTURE-GUIDE.md](CAPTURE-GUIDE.md)** pour les instructions de prise.

Tant qu'un fichier n'existe pas, la figure est **masquée pour les lecteurs**, de sorte que le manuel n'a jamais l'air inachevé. Pour voir ce qui manque encore, ajoutez `?figures` à l'URL :

```
https://urbandronedesign.github.io/AI_GEN_NARRATIVES/recits_generatifs_manuel-v1.html?figures
```

Chaque emplacement vide apparaît alors comme un cadre étiqueté indiquant quoi capturer. Retirez le paramètre et ils disparaissent.

## Une note sur l'écriture

Le manuel est écrit **pour les étudiants, pas à leur sujet**. Il s'adresse au lecteur à la deuxième personne et ne contient aucune consigne destinée à un encadrant, aucun conseil de conception d'évaluation, aucun commentaire de notation — les étudiants ont accès à ce document, donc tout ce qui n'a de sens que pour la personne qui enseigne vit à l'extérieur, dans [CAPTURE-GUIDE.md](CAPTURE-GUIDE.md).

Deux conventions portent la différence entre le fait et l'opinion :

- **Documenté** — vérifié dans la documentation officielle d'un modèle, d'un outil ou d'un texte réglementaire
- **Pratique d'atelier** — du métier et du jugement, avec quoi un étudiant est invité à discuter

## Le dossier de projet, prêt à l'emploi

**[⬇ `gabarits/dossier-de-projet.zip`](gabarits/dossier-de-projet.zip)** — l'arborescence du chapitre 4, complète, avec **onze documents de travail déjà amorcés** : fiche de problématique, cinq règles du monde, index du référentiel, les trois chartes, pitch, script, journal, et la feuille de plans déjà remplie avec les vingt identifiants de plan et leurs blocs (somme des durées : 60 s).

Les étudiants dézippent, renomment le dossier, et commencent. Les dossiers vides le sont volontairement — voir [gabarits/README.md](gabarits/README.md). La source browsable est [`gabarits/FILM_2026_project-name/`](gabarits/FILM_2026_project-name/) ; `python gabarits/build-zip.py` regénère l'archive après modification d'un gabarit.

**Les noms de dossiers, de fichiers et de colonnes sont en anglais** dans les deux éditions, parce qu'il n'y a qu'un seul système de fichiers et que les étudiants sont à l'aise en anglais. Le manuel français nomme donc les mêmes fichiers réels, sans les traduire.

## Les outils de l'atelier

Le pipeline décrit ici ne suppose pas que chaque étudiant installe et administre sa propre chaîne. Il repose sur **deux outils développés à l'École de Design Nantes Atlantique par [b2renger](https://github.com/b2renger)**, sans lesquels ce cours ne serait pas tenable à l'échelle d'une promotion :

| Outil | Rôle dans le cours | Chapitres |
|---|---|---|
| **[ComfyQ](https://github.com/b2renger/ComfyQ)** | Réservation de créneaux et file d'attente devant ComfyUI sur les GPU de l'atelier. Frise de réservation, estimation de durée calibrée par flux, historique partagé, export CSV, réutilisation d'un travail passé avec ses paramètres et ses médias. | 3 · 12 · 14 · 15 |
| **[LlmOnLan](https://github.com/b2renger/LlmOnLan)** *(MIT)* | Client de conversation adossé aux GPU de l'école, servant Gemma 4. Connexion automatique, aucune configuration. Multimodal (images, voix), recherche web, OCR de documents, et pilotage de Blender via MCP. Les conversations et les documents restent sur la machine de l'étudiant. | 3 · 5 · 6 · 8 · 13 |

**Le manuel ne décrit que les surfaces étudiantes** : l'interface web de ComfyQ (rien à installer, un navigateur suffit) et le client LlmOnLan (un installeur par système). Les composants d'administration — serveur ComfyQ, ferme LlmOnLan, ComfyQ Discovery — sont utilisés par les enseignants et les mainteneurs, et documentés dans [CAPTURE-GUIDE.md](CAPTURE-GUIDE.md), pas dans un document que les étudiants lisent.

Ces deux outils expliquent plusieurs choix du manuel. La discipline de graine du chapitre 12 suit le comportement de ComfyQ (champ randomisé à l'ouverture, verrouillage par saisie manuelle) ; le budget de calcul du chapitre 14 se lit dans son estimation calibrée plutôt qu'au chronomètre ; et l'argument de confidentialité des chapitres 3 et 18 tient parce que LlmOnLan garde les données en local.

## Ce qui se périme, et ce qui ne se périme pas

Ce champ change tous les deux mois. Tout ce qui est **nommé** — modèles, versions, chiffres de VRAM — est concentré dans le **chapitre 3** et dans **[prompts.html](prompts.html)**, pour que le reste du manuel reste juste. La *méthode* est faite pour survivre aux noms.

État des modèles : **août 2026**. Quand le manuel et votre installation ne sont pas d'accord sur un nom de nœud ou un réglage, croyez le logiciel.

## Mise à jour du manuel

C'est **un seul fichier HTML**, éditable directement — pas de compilation, pas de dépendances, pas de `npm install`. Ouvrez `recits_generatifs_manuel-v1.html` dans un éditeur de texte et modifiez-le.

Le mécanisme bilingue est du CSS : chaque bloc de texte est dans un `<div class="fr-only">` ou `<div class="en-only">`, et la bascule ne fait qu'appliquer une classe sur `<body>`. Pour ajouter un paragraphe, ajoutez-le dans les deux.

## Sources documentaires

Le manuel a été enrichi à partir de l'état de l'art d'août 2026 sur les techniques hybrides : cohérence par références multiples, prévisualisation 3D comme guide de mouvement, contrainte par première et dernière image, transfert de mouvement, reconstruction de site en splats gaussiens, et les obligations de transparence entrées en application le 2 août 2026. Les affirmations vérifiables portent la mention **Documenté** dans le texte.

Sources principales :

- [ComfyUI — documentation](https://docs.comfy.org/)
- [Gemma 4 — Google AI for Developers](https://ai.google.dev/gemma)
- [Règlement européen sur l'IA, article 50 — obligations de transparence](https://artificialintelligenceact.eu/article/50/)
- [Commission européenne — application des règles de transparence au 2 août 2026](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [LichtFeld Studio — entraînement de splats gaussiens, open source](https://lichtfeld.io/) · [dépôt](https://github.com/MrNeRF/LichtFeld-Studio)
- [Hugging Face — poids de modèles](https://huggingface.co/models)

## Documents d'origine

Ce manuel développe deux documents de travail internes, **non versionnés** ici (`.pdf` et `.docx` sont exclus par le `.gitignore`) :

- `Methodologie Creation de film AI.pdf` — le schéma initial du pipeline en six phases
- `STORYBOARDING assisté par IA génératives et LLM.docx` — la méthode initiale en trois phases et les chartes de cohérence

Les chapitres 8, 10 et 11 en sont l'élaboration directe : la déconstruction en trois phases, les chartes de cohérence et le super-prompt en trois blocs viennent de là. Le manuel les remplace — ils restent en local comme trace de la genèse du cours.

## Licence

Aucune licence n'a encore été choisie. En l'absence de licence, le droit d'auteur s'applique par défaut : le matériel est consultable ici mais n'est pas licencié pour réutilisation.
