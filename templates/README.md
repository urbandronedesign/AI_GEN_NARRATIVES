# Gabarits · Templates

**English** · [Français](README.fr.md)

## The project folder

**[⬇ Download `project-folder.zip`](project-folder.zip)**

The chapter 4 tree from the manual, complete and ready to use, with the working documents
already started. Unzip, rename the folder after your project, and begin.

### What is inside

| Started file | For which stage | Chapter |
|---|---|---|
| `journal.md` | from setup onwards, then the open calls and the archive | 4 · 17 |
| `00_brief/question_sheet.md` | stage 2 | 5 |
| `00_brief/five_rules.md` | stage 3, **constructed route** | 6 |
| `01_references/INDEX.md` | stage 3 | 6 |
| `01_references/style/SOURCES.md` | from the first external reference onwards | 18 |
| `02_writing/pitch.md` | stage 4 | 7 |
| `02_writing/script.md` | stage 5 | 8 |
| `03_breakdown/shot_sheet.csv` | stage 6 — **the pivot document** | 9 |
| `04_bibles/character_bible.md` | stage 7 | 10 |
| `04_bibles/place_bible.md` | stage 7 | 10 |
| `04_bibles/style_bible.md` | stage 7, plus the technical format | 10 |
| `04_bibles/prompts.md` | stage 8 — the twenty prompts and their seeds | 10 · 11 |
| `00_brief/consent_form.md` | **before** filming or training anything | 18 |
| `00_brief/LICENCES/README.md` | from the first model installed onwards | 18 |

The empty folders are empty on purpose. As chapter 4 puts it: *an empty folder that waits is
an instruction; a folder created at the moment you need it becomes a junk drawer.*

The shot sheet arrives **already filled in** with the twenty shot identifiers, their block and
a duration of 3 seconds — summing to 60 seconds. All that is left is to write.

### Short format · years 1 and 2

Thirty seconds, ten shots: delete rows `P11` to `P20` from the shot sheet and redistribute the
blocks as `2·2·2·2·2`. `04_bibles/character_bible.md` is not used — the A1·A2 format is done
without a character. See *Path by year* in the manual.

### A note on names

Folder, file and column names are **in English**, in both editions of the manual, because there
is **only one filesystem** and students are comfortable in English. Do not translate them: the
manual, the shot sheet and the screenshots refer to them as they are.

The only names you choose are those of your own files — and there too, name them in English:
`PHOTO_014_north-hall_concrete-floor.jpg` rather than `PHOTO_014_halle-nord_sol.jpg`. Sorting
and searching work better for it, and an international jury reads your folder.

---

## Regenerating the archive

The `FILM_2026_project-name/` folder in this repository is the source; `project-folder.zip` is
its export. After modifying a template:

```bash
python templates/build-zip.py
```

The script excludes `.gitkeep` files: the empty folders are recreated in the archive without them.
