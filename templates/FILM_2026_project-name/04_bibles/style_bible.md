# Charte de style · les cinq piliers
# Style bible · the five pillars

> Chapitre 10, §10.3. **Le fichier le plus important des trois.**
>
> Sans charte de style, un plan sort en photo réaliste et le suivant en image publicitaire
> saturée. Le spectateur perd l'immersion immédiatement, sans savoir pourquoi.

**Version** : v1
**Date** :
**Figée le** : <!-- après cette date, plus une virgule ne change -->

---

## 1 · Palette

> Le facteur numéro un de l'unité visuelle. **Deux ou trois teintes dominantes, pas plus.**
> Monochrome · complémentaires (*teal and orange*) · désaturée · sursaturée.

<!-- ... -->

## 2 · Optique

> Argentique, numérique, stylisée ? **Précisez toujours la focale** : `35mm lens` pour un
> rendu réaliste, `85mm` pour les portraits, `24mm` pour un espace exagéré.

<!-- ... -->

## 3 · Éclairage

> **Une** source principale, tenue sur tout le film. Direction cardinale, pas une impression :
> « rasante nord-est » et non « belle lumière ».

<!-- ... -->

## 4 · Composition

> Comment le sujet se détache du décor. Profondeur de champ courte pour isoler,
> `deep focus` pour montrer un décor complexe, cadrage symétrique.

<!-- ... -->

## 5 · Le suffixe de style

> La synthèse des quatre précédents, en une seule chaîne, en anglais. Elle s'ajoute **à la
> fin** de chacun de vos vingt prompts — image **et** vidéo. Mettre le style en dernier aide
> le modèle à l'appliquer par-dessus toute la description.

```

```

---

## ⚠ Le suffixe ne change jamais · pas une virgule

C'est la règle la plus simple du manuel et la plus souvent enfreinte.

Vous allez être tenté, au plan 14, d'ajouter `more dramatic` parce que cette image-là manque
de force. **Ne le faites pas** : vous venez de créer deux films.

Si le suffixe doit changer, il change **pour les vingt plans**, et vous regénérez tout.
Notez la question dans le `journal.md`, finissez la série, et décidez à froid une fois les
vingt images faites.

### Historique des versions

| Version | Date | Ce qui a changé | Plans regénérés ? |
|---------|------|-----------------|-------------------|
| v1      |      | création        | —                 |

---

## Prompt négatif

> Chapitre 11, §11.5. **Restez court.** N'ajoutez un terme que lorsque vous avez *constaté*
> le défaut sur vos propres images : les listes recopiées sur des forums contiennent des
> dizaines de termes inutiles pour votre modèle, et chacun consomme de l'attention qui
> manquera à votre description.

```
blurry, low resolution, distorted hands, extra fingers, watermark,
text overlay, oversaturated, fisheye distortion, duplicated subject
```

> Voie construite : ajoutez ici les interdictions de votre **règle 5**.

---

## Format technique · les quatre valeurs

> Chapitre 10, §10.4. À remplir **avant la première image générée**. Trois de ces
> quatre ne se réparent pas après coup : aucun outil de montage ne rend des pixels
> qui n'ont jamais existé.

| | Valeur | Défaut du cours |
|---|---|---|
| **Rapport de cadre** |  | 16:9 |
| **Résolution de travail** |  | la plus haute que le modèle tient |
| **Cadence** |  | 24 im/s |
| **Espace colorimétrique** |  | sRGB / Rec.709 |

> Une seule cadence, du début à la fin. Ne passez à 25 im/s que si un dépôt l'exige
> par écrit, et alors une seule fois, à la fin, sur le film terminé.
