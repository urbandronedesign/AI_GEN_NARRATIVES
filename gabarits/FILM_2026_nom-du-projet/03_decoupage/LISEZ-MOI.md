# La feuille de plans · The shot sheet

`feuille_de_plans.csv` est **le document pivot du projet**. Une ligne par plan, vingt lignes.
C'est le seul document que vous ouvrirez tous les jours pendant six semaines, et le cœur du
livrable A.

Ouvrez-le dans un tableur (Excel, LibreOffice, Numbers, Google Sheets). Il est déjà rempli
avec les vingt identifiants de plan, leur bloc et une durée de 3 secondes par défaut —
somme : 60 secondes.

## Les quatorze colonnes

| Colonne | Contenu | Sert au chapitre |
|---------|---------|------------------|
| `plan` | `P01` à `P20`. **Ne change jamais**, même si l'ordre au montage change. | partout |
| `bloc` | I à V, la structure du chapitre 7. Déjà rempli. | 17 |
| `duree` | En secondes. 3 par défaut ; 2 ou 4 si le rythme l'exige. **La somme doit faire 60 (± 2).** | 17 |
| `action` | L'action visible, une phrase. Ce que fait le plan. | 12 · 14 |
| `echelle` | `TL` `PL` `PM` `PA` `PR` `GP` — voir Fig 9.2 du manuel. | 12 |
| `angle` | Hauteur et axe de caméra. | 12 |
| `mouvement` | Ce qui bouge. `fixe` est une réponse valide et souvent la bonne. | 14 · 15 |
| `lieu` | La zone. Doit correspondre à une zone de votre `INDEX.md`. | 10 |
| `lumiere` | Direction et qualité, en direction cardinale. **Constante sur tout le film** sauf ellipse écrite. | 10 · 12 |
| `intention` | Ce que le plan doit faire ressentir. La colonne qu'on saute et qu'il faut garder : c'est elle qui vous sert à choisir entre trois prises au chapitre 15. | 13 · 17 |
| `son` | Ce qu'on entend : ambiance, événement, voix, silence. | 16 |
| `ref_images` | Les références de votre référentiel à injecter, séparées par `;`. **Une cellule vide signifie que ce plan sera inventé par le modèle.** | 12 |
| `seed` | La graine de l'image validée. Sans elle, le livrable B n'est pas reproductible. | 12 |
| `statut` | `a_faire` · `image_ok` · `video_ok` · `valide` | 13 · 15 |

## Pourquoi un CSV et pas un joli document

Parce qu'il est **triable et filtrable**. À trois jours du rendu, la question n'est pas
« à quoi ressemble mon film » mais « quels plans ne sont pas finis » : vous filtrez la
colonne `statut` et vous avez la réponse en deux secondes. Un storyboard mis en page, aussi
beau qu'il soit, ne répond pas à cette question.

## Format réduit · A1 · A2

Trente secondes, dix plans. Supprimez les lignes P11 à P20 et répartissez les blocs
`2·2·2·2·2` : P01–P02 en I, P03–P04 en II, P05–P06 en III, P07–P08 en IV, P09–P10 en V.
Les proportions de la structure restent les mêmes.

## Attention à votre tableur

Certains tableurs réécrivent le fichier en changeant le séparateur ou l'encodage.
Enregistrez en **CSV UTF-8, séparateur virgule**. Si vos accents deviennent illisibles ou
si tout se retrouve dans une seule colonne, c'est cela.
