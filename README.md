```
████  █████  ████ █████ █████  ████
█   █ █     █       █     █   █
████  ████  █       █     █    ███
█  █  █     █       █     █       █
█   █ █████  ████ █████   █   ████

 ████ █████ █   █ █████ ████   ███  █████ █████ █████  ████
█     █     ██  █ █     █   █ █   █   █     █   █     █
█  ██ ████  █ █ █ ████  ████  █████   █     █   ████   ███
█   █ █     █  ██ █     █  █  █   █   █     █   █         █
 ████ █████ █   █ █████ █   █ █   █   █   █████ █     ████

the production manual for the AI-generated short film
FR · EN   ·   L'École de Design Nantes Atlantique   ·   Edition 2026.1

  référentiel → writing → bibles → image → movement → sound → delivery
       ▲                                                          │
       └──────  the defect noticed here was committed there  ─────┘
```

**English** · [Français](README.fr.md)

# Récits génératifs — the production manual for the AI-generated short film

A bilingual (FR/EN) production manual for making a **short film with generative AI**, from writing to the mix. A course in **technical skills**, written for design students **from first to fifth year**.

The film can take place in a **real location the student documents** or in a **wholly invented world** — speculative fiction, fable, abstraction. Both routes are covered, and from chapter 7 on the technical pipeline is the same.

### 📖 **[Read online → urbandronedesign.github.io/AI_GEN_NARRATIVES](https://urbandronedesign.github.io/AI_GEN_NARRATIVES/)**

This is the link to give students — nothing to download, nothing to install, works on a phone.

### ⌨️ **[Prompts & models →](https://urbandronedesign.github.io/AI_GEN_NARRATIVES/prompts.html)**

Companion page: every prompt in the pipeline ready to copy, the bilingual lexicon of what to write to get what you want (« lumière rasante » → `low raking light, long shadows`), and the state of the models. Sorted by task, with a live filter.

### 🔧 **[Under the hood →](https://urbandronedesign.github.io/AI_GEN_NARRATIVES/outils.html)**

Second companion page: what sits behind the form. **ComfyUI** and how to read a graph, the models and the projects they came from, and the catalogue of studio workflows — including the three the manual does not cover (**masked inpainting**, **SAM3**, **LivePortrait**), with the caveat that goes with them. It ends with a protocol for judging a model you have never met — the only part of the page that will not go stale.

For offline use, download **[`recits_generatifs_manuel-v1.html`](recits_generatifs_manuel-v1.html)** and open it in any browser. One self-contained file, ~650 KB, no dependencies, no build step. It works from a USB key with the network down — take [`prompts.html`](prompts.html) and [`outils.html`](outils.html) along too, they are self-contained the same way.

> **Companion manual** — [3DVIZ · SketchUp & Rhino to Twinmotion 2026](https://github.com/urbandronedesign/3DVIZ), same format, same conventions. Both read the same way: FR/EN toggle, search, level filter, symptom index.

---

## What is in it

**18 chapters** following the real order of production — understand, gather the *référentiel*, write, lock, generate the image, animate, add sound, edit — plus a reference section.

| Part | Chapters |
|---|---|
| **Preamble** | How to use this manual · The project & what you hand in · **Path by year** |
| **I — Foundations** | The end-to-end pipeline · The hybrid principle · The lab · **The project folder** |
| **II — The *référentiel*** | Research question & brief · **Building the *référentiel*** (captured route / constructed route) |
| **III — Writing** | From brief to pitch · Steering the LLM · Breakdown & shot sheet |
| **IV — Consistency** | The consistency bibles · Super-prompt & anchoring |
| **V — The image** | Generating the storyboard · Hybrid control & validation |
| **VI — Movement** | From still to animated shot · Advanced control & finishing |
| **VII — Sound & delivery** | Sound design · **Edit, grade, deliver** (the AI look, open calls, archiving) · Law, ethics & credits |
| **Reference** | Symptom → Fix index (46 symptoms) · Student FAQ (38 questions) · Bilingual glossary (55 terms) |

That is **24 sections** in all, three of them preamble and three reference.

Roughly **70,300 words** across the two languages.

Chapter 1 opens on a full-page diagram of the whole pipeline — seven stages, the decisions that belong to each, and the **return path** showing that a defect noticed downstream was committed upstream. The project folder is drawn as the container for all of it, because a project that is not portable is not really a project.

## Features

- **Bilingual** — FR/EN toggle, remembered between visits
- **Client-side search** across chapters, FAQ, symptom index and prompt blocks — with a separate index per language
- **Year filter A1·2 / A3 / A4·5** — the labels are cumulative, and hidden content drops out of the search index too
- **Prompt blocks with a Copy button** — students copy prompts constantly
- **Symptom → Fix index** organised by what you see on screen, not by chapter
- **Print stylesheet** — prints and exports to PDF cleanly, with sensible page breaks
- **Responsive** — readable on a phone at 1 a.m. the night before a jury
- **Light / dark theme**, following the system by default
- Shortcuts: <kbd>/</kbd> for search, <kbd>Esc</kbd> to clear it

## How the course is built

The manual rests on **a single film**, carried through **14 stages**. Three deliverables, four in the final years:

| | Deliverable |
|---|---|
| **A** | **The production folder** — the *référentiel* (captured or constructed), shot sheet, consistency bibles, project journal |
| **B** | **The storyboard** — approved key images, each with its exact prompt and seed |
| **C** | **The film** — mixed sound, credits declaring the tools used |
| **D** | *(A4·A5 only)* **A documented reusable asset** left to the studio: a ComfyUI graph, a LoRA with its image set, a site reconstruction, or a technique sheet |

Because the production folder is handed in, the method chapters are **assessed directly** rather than being preparation for something else. Four assessment axes, announced from the preamble on: specificity, consistency, intent, method.

### Two routes to the same artefact

A generative model produces the average of what it has seen. For a film to be yours and not that average, you need a ***référentiel***: a set of specific images and sounds, sorted and named, fed into the model and used to derive the consistency bibles. Chapter 6 describes its two constructions.

| | Captured route | Constructed route |
|---|---|---|
| **The world is** | real, visitable | invented — speculative, fable, abstraction |
| **The *référentiel* comes from** | photographs, video and sound taken on site | generated research images **then culled**, drawings, models and objects photographed, textures, licensed references |
| **Its own risk** | staying merely descriptive | staying vague: a world with no written rules |
| **Its own discipline** | going out to get the right material | deciding — generating is easy, eliminating is the work |
| **Produces** | a sorted, named, indexed `01_references/` | *the same* `01_references/` |

The two mix, and that is often the strongest option: an invented world whose materials come from real photographs. From chapter 7 on, the manual no longer distinguishes between them.

**Hybrid does not mean documentary.** A science-fiction film whose sets come from photographed models, whose foley is recorded on a desk and whose camera moves come out of a Blender previz is *more* hybrid than a documentary produced entirely by prompt. What matters is not that the world be real, but that the material anchoring it be the student's own.

### One pipeline, five years

The **pipeline does not change** from one level to the next — that is the whole point of a single document: what is learned in first year stays true in fifth, and there is nothing to unlearn. What changes is the format, the technical depth and how much argument is expected. A first-year student does not do "part of the course": they do *the whole course, smaller*.

| Year | Format | Bibles | Hybrid axes required |
|---|---|---|---|
| **A1 · A2** | 30 s · 10 shots | place + style, no character | 1 *référentiel* · 4 craft |
| **A3** *(reference format)* | 60 s · 20 shots | all three | 1 · 3 material · 4 |
| **A4 · A5** | 60–90 s, 20 shots min. | all three, versioned | all four, including 2 demonstrated control |

The body of the manual is written for the reference format — 60 seconds, twenty shots. The **Path by year** section gives, for each level, the format, the deliverables and a chapter-by-chapter reading table. The toolbar filter simply hides what is not yet for the reader: a first-year sees 92 % of the manual, a third-year 97 %.

### Why three seconds a shot

That is the duration a video model generates natively and well; beyond it, drift sets in. Twenty shots is enough that a *method* for consistency becomes necessary (at five shots you can wing it by eye) and few enough that a failure stays repairable within the time of the module.

## Figures

**Eight figures are drawn diagrams** — inline SVG, bilingual, with no dependency at all. They cover what a screenshot explains badly: the pipeline's return path, the four injection points for non-generative material in the chain, the anatomy of a filename, the shooting coverage for a 3D reconstruction, the six shot sizes, the anatomy of the super-prompt, the effect of first-and-last-frame constraint, the architecture of the four sound layers.

**Eight are screenshots** that cannot be drawn — the studio's ComfyUI graphs, a character bible board, an edit timeline, the shot sheet in production. See **[CAPTURE-GUIDE.md](CAPTURE-GUIDE.md)** for how to take them.

As long as a file does not exist, the figure is **hidden from readers**, so that the manual never looks unfinished. To see what is still missing, add `?figures` to the URL:

```
https://urbandronedesign.github.io/AI_GEN_NARRATIVES/recits_generatifs_manuel-v1.html?figures
```

Each empty slot then appears as a labelled frame saying what to capture. Remove the parameter and they disappear.

## A note on the writing

The manual is written **for students, not about them**. It addresses the reader in the second person and contains no instructions aimed at a teacher, no assessment-design advice, no grading commentary — students have access to this document, so anything that only makes sense to the person teaching lives outside it, in [CAPTURE-GUIDE.md](CAPTURE-GUIDE.md).

Two conventions carry the difference between fact and opinion:

- **Documenté** *(Documented)* — verified in the official documentation of a model, a tool or a regulatory text
- **Pratique d'atelier** *(Studio practice)* — craft and judgement, which a student is invited to argue with

## The project folder, ready to use

**[⬇ `templates/project-folder.zip`](templates/project-folder.zip)** — the chapter 4 tree, complete, with **eleven working documents already started**: research-question sheet, five rules of the world, *référentiel* index, the three bibles, pitch, script, journal, and the shot sheet already filled in with the twenty shot identifiers and their blocks (durations summing to 60 s).

Students unzip, rename the folder, and start. The empty folders are empty on purpose — see [templates/README.md](templates/README.md). The browsable source is [`templates/FILM_2026_project-name/`](templates/FILM_2026_project-name/); `python templates/build-zip.py` regenerates the archive after a template is modified.

**Folder, file and column names are in English** in both editions, because there is only one filesystem and students are comfortable in English. The French manual therefore names the same real files, without translating them.

## The studio tools

The pipeline described here does not assume every student installs and administers their own chain. It rests on **two tools developed at L'École de Design Nantes Atlantique by [b2renger](https://github.com/b2renger)**, without which this course would not be workable at the scale of a whole year group:

| Tool | Role in the course | Chapters |
|---|---|---|
| **[ComfyQ](https://github.com/b2renger/ComfyQ)** | Slot booking and a queue in front of ComfyUI on the studio GPUs. Booking timeline, per-workflow calibrated duration estimates, shared history, CSV export, reuse of a past job with its parameters and media. | 3 · 12 · 14 · 15 |
| **[LlmOnLan](https://github.com/b2renger/LlmOnLan)** *(MIT)* | Chat client backed by the school's GPUs, serving Gemma 4. Automatic connection, no configuration. Multimodal (images, voice), web search, document OCR, and Blender control via MCP. Conversations and documents stay on the student's machine. | 3 · 5 · 6 · 8 · 13 |

**The manual documents only the student-facing surfaces**: the ComfyQ web interface (nothing to install, a browser is enough) and the LlmOnLan client (one installer per system). The administration components — ComfyQ server, LlmOnLan farm, ComfyQ Discovery — are used by teachers and maintainers, and documented in [CAPTURE-GUIDE.md](CAPTURE-GUIDE.md), not in a document students read.

These two tools explain several of the manual's choices. The seed discipline of chapter 12 follows ComfyQ's behaviour (field randomised on open, locked by typing a value manually); the compute budget of chapter 14 is read off its calibrated estimate rather than off a stopwatch; and the privacy argument of chapters 3 and 18 holds because LlmOnLan keeps data local.

## Checking the manual for consistency

```bash
python tools/audit.py
```

Seven passes, no dependencies: HTML validity, internal link resolution, **parity of facts between the two editions** (section numbers, identifiers, cross-references, year labels, stage and figure numbers), **structural parity** (an edition with five table rows where the other has four has lost content), absence of French file or column names, agreement between the manual and the downloadable template, and symmetry of the year bands.

Run it after every change to the manual. The exit code is the number of failing passes, so it works as-is in CI — which is what [`.github/workflows/audit.yml`](.github/workflows/audit.yml) does, and it also checks that `project-folder.zip` is not stale with respect to the template.

This script exists because this document describes **one single reality in two languages**, and the way the two editions drift apart is not the way you notice while reading. On its first run it found a validation criterion that had vanished from the English edition of chapter 6, the complete absence of a CSV example in the English edition of chapter 9, and four smaller inconsistencies. Details in [tools/README.md](tools/README.md).

## What goes stale, and what does not

This field changes every couple of months. Everything **named** — models, versions, VRAM figures — is concentrated in **chapter 3**, in **[prompts.html](prompts.html)** and in **[outils.html](outils.html)**, so that the rest of the manual stays true. The *method* is built to outlive the names.

Model state: **August 2026**. When the manual and your installation disagree on a node name or a setting, believe the software.

## Updating the manual

> **Before making any change, read [`CLAUDE.md`](CLAUDE.md).** That is the maintenance
> document: the decisions already settled and why, the facts that must stay consistent
> from one file to the next, how to edit a 650 KB file without breaking it quietly, and
> what is still open. It is also loaded automatically by Claude Code at the start of
> every session in this repository.

It is **a single HTML file**, editable directly — no build, no dependencies, no `npm install`. Open `recits_generatifs_manuel-v1.html` in a text editor and change it.

The bilingual mechanism is CSS: every block of text sits in a `<div class="fr-only">` or an `<div class="en-only">`, and the toggle only applies a class to `<body>`. To add a paragraph, add it to both.

## Documentary sources

The manual was developed from the August 2026 state of the art on hybrid techniques: consistency through multiple references, 3D previz as a movement guide, first-and-last-frame constraint, motion transfer, site reconstruction as Gaussian splats, and the transparency obligations that came into force on 2 August 2026. Verifiable claims carry the mention **Documenté** in the text.

Main sources:

- [ComfyUI — documentation](https://docs.comfy.org/)
- [Gemma 4 — Google AI for Developers](https://ai.google.dev/gemma)
- [EU AI Act, article 50 — transparency obligations](https://artificialintelligenceact.eu/article/50/)
- [European Commission — enforcement of the transparency rules from 2 August 2026](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [LichtFeld Studio — Gaussian splat training, open source](https://lichtfeld.io/) · [repository](https://github.com/MrNeRF/LichtFeld-Studio)
- [Hugging Face — model weights](https://huggingface.co/models)

## Source documents

This manual develops two internal working documents, **not versioned** here (`.pdf` and `.docx` are excluded by `.gitignore`):

- `Methodologie Creation de film AI.pdf` — the initial six-phase pipeline diagram
- `STORYBOARDING assisté par IA génératives et LLM.docx` — the initial three-phase method and the consistency bibles

Chapters 8, 10 and 11 are their direct elaboration: the three-phase deconstruction, the consistency bibles and the three-block super-prompt come from there. The manual replaces them — they stay local as a trace of how the course came about.

## Licence

No licence has been chosen yet. In the absence of a licence, copyright applies by default: the material can be read here but is not licensed for reuse.
