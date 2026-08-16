# Gabarits · Templates

## Le dossier de projet

**[⬇ Télécharger `dossier-de-projet.zip`](dossier-de-projet.zip)**

L'arborescence du chapitre 4 du manuel, complète et prête à l'emploi, avec les documents de
travail déjà amorcés. Dézippez, renommez le dossier avec le nom de votre projet, et commencez.

> *The chapter 4 project folder, complete and ready to use, with the working documents already
> started. Unzip, rename the folder after your project, and begin.*

### Ce qu'il y a dedans

| Fichier amorcé | Pour quelle étape | Chapitre |
|---|---|---|
| `journal.md` | dès la mise en place | 4 |
| `00_brief/fiche_problematique.md` | étape 2 | 5 |
| `00_brief/cinq_regles_du_monde.md` | étape 3, **voie construite** | 6 |
| `01_references/INDEX.md` | étape 3 | 6 |
| `01_references/style/SOURCES.md` | dès la première référence externe | 18 |
| `02_ecriture/pitch.md` | étape 4 | 7 |
| `02_ecriture/script.md` | étape 5 | 8 |
| `03_decoupage/feuille_de_plans.csv` | étape 6 — **le document pivot** | 9 |
| `04_chartes/charte_personnage.md` | étape 7 | 10 |
| `04_chartes/charte_lieu.md` | étape 7 | 10 |
| `04_chartes/charte_style.md` | étape 7 | 10 |

Les dossiers vides le sont volontairement. Comme le dit le chapitre 4 : *un dossier vide qui
attend est une consigne ; un dossier créé au moment où on en a besoin devient un débarras.*

La feuille de plans arrive **déjà remplie** avec les vingt identifiants de plan, leur bloc et
une durée de 3 secondes — somme 60 secondes. Il ne reste qu'à écrire.

### Format réduit · années 1 et 2

Trente secondes, dix plans : supprimez les lignes `P11` à `P20` de la feuille de plans et
répartissez les blocs `2·2·2·2·2`. `04_chartes/charte_personnage.md` ne sert pas — le format
A1·A2 se fait sans personnage. Voir *Parcours par année* dans le manuel.

### Une note sur les noms

Les noms de dossiers et de fichiers sont en français dans les deux éditions du manuel, parce
qu'il n'y a **qu'un seul système de fichiers**. L'édition anglaise nomme donc les mêmes
fichiers réels, avec une glose anglaise là où elle aide. Ne les traduisez pas : le manuel, la
feuille de plans et les captures d'écran y font référence tels quels.

---

## Regénérer l'archive

Le dossier `FILM_2026_nom-du-projet/` de ce dépôt est la source ; `dossier-de-projet.zip` en
est l'export. Après modification d'un gabarit :

```bash
python gabarits/build-zip.py
```

Le script exclut les `.gitkeep` : les dossiers vides sont recréés dans l'archive sans eux.
