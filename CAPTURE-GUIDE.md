# Guide de capture d'écran

**Pour la personne qui maintient le manuel — pas pour les étudiants.** Ce fichier vit hors du manuel volontairement : ce sont des instructions de production du document, et un étudiant qui les lit serait seulement dérouté.

Huit figures du manuel sont des schémas dessinés en SVG et ne demandent rien. Les huit autres, listées ci-dessous, ne peuvent pas être dessinées — c'est soit une interface qu'il faut photographier, soit un résultat qui ne veut dire quelque chose qu'en venant d'un vrai projet.

## Comment fonctionne le système d'images

Enregistrez chaque capture dans `images/` sous **exactement** le nom de fichier indiqué. Le manuel la détecte et l'affiche automatiquement — aucun code à modifier.

Tant qu'un fichier n'existe pas, la figure est **masquée pour les lecteurs**, de sorte que le manuel n'a jamais l'air inachevé. Pour voir ce qui manque encore, ouvrez le manuel avec `?figures` à la fin de l'URL :

```
https://urbandronedesign.github.io/AI_GEN_NARRATIVES/recits_generatifs_manuel-v1.html?figures
```

Chaque emplacement vide apparaît alors comme un cadre étiqueté indiquant quoi capturer. Retirez le paramètre et ils disparaissent.

Chaque figure a **un emplacement dans l'édition française et un dans l'édition anglaise** ; un seul fichier remplit les deux.

## Faites-les vous-même

Les captures d'écran d'un logiciel que vous êtes autorisé à utiliser sont sans problème pour l'enseignement. Des images tirées du tutoriel de quelqu'un d'autre, ou reprises d'un blog, sont sa propriété — et ce dépôt est public. Chaque capture doit être la vôtre.

Pour les figures du groupe 2, une image issue d'un projet étudiant fonctionne très bien, **avec son autorisation écrite et une ligne de crédit**. Cela a un effet utile : la promotion suivante voit à quoi ressemble le niveau attendu, ce qui vaut mieux que n'importe quelle description.

## Réglages pour toutes les captures

PNG · au moins 1600 px de large · fenêtre de l'application seule, pas le bureau entier · thème clair de préférence, il s'imprime mieux · pas de données personnelles ni de nom d'étudiant visibles à l'écran.

---

## Groupe 1 — Interfaces

Cinq captures. Elles se font toutes en une seule séance, avec n'importe quel projet ouvert. Comptez une heure.

| Nom de fichier | Où aller | Cadrer pour que |
|---|---|---|
| `12-01-comfyui-graphe-image.png`<br>**celle-ci en premier** | ComfyUI, le graphe de génération d'image de l'atelier, avec le nœud de références d'image branché. | Les six paramètres de la table 12.1 soient lisibles avec leurs valeurs : graine, pas, guidage, échantillonneur, résolution, débruitage. **Capture la plus consultée du manuel** — c'est elle qui évite la moitié des questions en atelier. |
| `14-01-comfyui-graphe-video.png`<br>**celle-ci en deuxième** | ComfyUI, le graphe image-vers-vidéo. | L'entrée image clé, le prompt de mouvement, le nombre d'images et la cadence soient lisibles. Si le graphe gère première et dernière image, les deux entrées doivent être visibles — c'est la technique du chapitre 15.1. |
| `09-01-feuille-de-plans.png` | Une feuille de plans réelle **en milieu de production**, pas vide. | La colonne `statut` contienne visiblement des valeurs différentes (`a_faire`, `image_ok`, `valide`). C'est l'image du tableau de bord. **Si l'atelier dispose d'un outil maison de suivi des plans, c'est ici qu'il se montre** plutôt qu'un tableur. |
| `17-01-timeline-montage.png` | La timeline complète d'un film du cours, dans Resolve ou Premiere. | On voie les 20 plans vidéo, les quatre couches sonores de la Fig 16.1, et les nœuds d'étalonnage. **Le point à démontrer visuellement : la couche d'ambiance traverse toutes les coupes sans s'interrompre** — c'est la règle centrale du chapitre 16. |
| `06-02-splat-reconstruction.png` | LichtFeld Studio, une reconstruction en cours. | L'aperçu d'entraînement d'un côté et les positions de caméra résolues de l'autre. **Sur un site réel de l'école, pas sur un jeu de démonstration** — sinon la figure contredit tout le chapitre 6. Cette figure ne concerne que la voie captée, en A4·5. Le nom de fichier est volontairement neutre : si l'atelier change d'outil, seule la légende bouge. |

## Groupe 2 — Résultats d'un vrai projet

Trois captures qui viennent de la production. Chacune est déjà quelque chose que les étapes demandent aux étudiants de produire : faire tourner le cours une fois soi-même les génère comme sous-produit.

| Nom de fichier | Ce qu'il faut produire | Vient de l'étape |
|---|---|---|
| `10-01-charte-personnage.png` | Le même personnage sous 4 à 6 angles, généré depuis un **bloc de cohérence unique**, avec le bloc de texte affiché à côté. Le point est la comparaison : le texte à gauche, ce qu'il produit à droite. | Étape 7 |
| `06-01-planche-contact.png` | Une planche contact de référentiel correctement constitué : vignettes nommées, groupées par les quatre familles du §6.2. Doit montrer en une image ce que le §6.9 demande. **Prenez-la de préférence sur la voie construite** — un référentiel d'images générées *puis triées*, avec leurs prompts — parce que c'est le cas que les étudiants comprennent le moins bien. | Étape 3 |
| `13-01-controle-profondeur.png` | Un triptyque sur un plan réel : la source (photo de site ou rendu Blender gris), la carte extraite (profondeur ou contours), l'image générée. **Le même cadrage dans les trois** — c'est la démonstration que le contrôle fonctionne, et elle ne vaut rien si les cadrages diffèrent. | Étapes 9–10 |

---

## Où chaque figure apparaît

| Capture | Chapitre | Section |
|---|---|---|
| `06-01` | 6 | 6.9 Constituer le référentiel |
| `06-02` | 6 | 6.5 Captation pour reconstruction 3D · **masquée pour A1·2** · fichier `06-02-splat-reconstruction.png` |
| `09-01` | 9 | 9.1 La feuille de plans |
| `10-01` | 10 | 10.3 fin de chapitre, avant l'étape 7 |
| `12-01` | 12 | 12.1 Le graphe minimal |
| `13-01` | 13 | 13.2 La prévisualisation 3D · **masquée pour A1·2 et A3** |
| `14-01` | 14 | 14.3 Le budget de prises |
| `17-01` | 17 | 17.5 Export |

Le préfixe numérique est un identifiant stable, pas un numéro de chapitre. Utilisez cette table plutôt que le préfixe.

**Note sur les deux figures masquées.** `06-02` est dans une section marquée A4+, `13-01` dans une section A4+ : elles n'apparaissent donc pas quand le filtre d'année est sur A1·2. C'est voulu. Si vous voulez qu'elles soient vues de tous, retirez le `data-level` du `<div>` qui les contient.

## Ajouter un nouvel emplacement de figure

Pour vos outils maison ou toute nouvelle capture, collez ce bloc à l'endroit voulu, **dans le bloc de langue française puis dans le bloc anglais** (deux copies, un seul fichier image, l'`id` de la copie anglaise suffixé `-en`) :

```html
<figure class="shot" id="fig-XX-YY">
  <div class="shot-frame">
    <img src="images/XX-YY-nom-court.png" alt="Description courte"
         onload="this.closest('.shot').classList.add('has-image')">
    <div class="shot-todo">
      <span class="id">Capture XX-YY</span>
      <div class="what">Ce qu'il faut capturer, et comment le cadrer.</div>
      <span class="file">images/XX-YY-nom-court.png</span>
    </div>
  </div>
  <figcaption>Fig N.N — Ce que la figure démontre.</figcaption>
</figure>
```

L'attribut `onload` est ce qui fait tout le mécanisme : si le fichier existe, la classe `has-image` est ajoutée et l'image remplace le cadre d'attente. Ne le retirez pas.

## Ce qui n'a pas besoin de capture

Les huit figures suivantes sont des SVG dessinés, bilingues, et complets : le pipeline en sept étapes et son chemin de retour (Fig 1.1), les quatre points d'injection du matériau non génératif (Fig 2.1), l'anatomie d'un nom de fichier (Fig 4.1), la couverture de prise de vue pour reconstruction (Fig 6.1), les six échelles de plan (Fig 9.2), l'anatomie du super-prompt (Fig 11.1), première et dernière image (Fig 15.1), les quatre couches sonores (Fig 16.1). Elles n'ont besoin de rien de votre part et se redessinent automatiquement en thème sombre.

## Entretien du manuel

- Les modèles nommés sont concentrés au **chapitre 3** et dans **`prompts.html`**. C'est là qu'il faut passer chaque semestre, et nulle part ailleurs.
- La date « août 2026 » apparaît dans le chapitre 3, la couverture de `prompts.html` et le pied de page. Mettez-la à jour en même temps que les modèles.
- Les liens publics pointent vers `urbandronedesign.github.io/AI_GEN_NARRATIVES/`. Si vous nommez le dépôt autrement que `AI_GEN_NARRATIVES`, corrigez-les dans le README et dans ce fichier — le manuel lui-même ne contient **aucune** URL GitHub, ses liens internes sont tous relatifs et fonctionnent sous n'importe quel nom de dépôt.
- Le manuel est **un seul fichier HTML éditable à la main**. Le mécanisme bilingue est du CSS : chaque bloc est dans un `<div class="fr-only">` ou `<div class="en-only">`. Pour ajouter un paragraphe, ajoutez-le dans les deux.
- Les étiquettes d'année sont deux attributs : `data-level="p"` (A3 et plus) et `data-level="r"` (A4 et plus) sur un `<div>` englobant. Le contenu masqué sort aussi de l'index de recherche, donc il n'y a rien d'autre à faire.
