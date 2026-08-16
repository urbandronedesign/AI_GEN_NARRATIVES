# Working notes — Récits génératifs

For the maintainer and for Claude Code, which loads this file automatically at the
start of every session in this repo. It records what has been **decided**, so that
neither of us re-litigates it, and how to edit safely, so that neither of us breaks
the thing quietly.

Read this first. Then `python tools/audit.py` before you touch anything, so you know
the baseline is green.

---

## What this repo is

A bilingual (FR/EN) production manual teaching design students, **first to fifth
year**, to produce a short film with generative AI. Distributed as GitHub Pages at
<https://urbandronedesign.github.io/AI_GEN_NARRATIVES/>.

| File | What it is |
|---|---|
| `recits_generatifs_manuel-v1.html` | **The deliverable.** 18 chapters + 3 preamble + 3 reference = 24 sections. ~650 KB. |
| `prompts.html` | Companion: every pipeline prompt copy-ready, the bilingual prompt lexicon, model state |
| `outils.html` | Companion: what is under the ComfyQ form — ComfyUI, the models, the studio workflows, how to judge a new model |
| `index.html` | Meta-refresh redirect to the manual |
| `templates/` | The pre-started project folder + its deterministic ZIP |
| `tools/audit.py` | 7-pass consistency audit. **Must pass 7/7 before any commit.** |
| `CAPTURE-GUIDE.md` | Maintainer-only: the 8 screenshots still to take, and the front/back boundary |

The format is a **single self-contained HTML file** — inline CSS and JS, no external
requests, no build step. It works from a USB key with the network down, which is the
actual requirement. The generalised version of this format is the `coursebook` skill:
<https://github.com/urbandronedesign/coursebook>. Use it when starting a new course;
this file covers only what is specific to *this* one.

---

## Settled decisions — do not reopen

Each of these was decided deliberately and cost something to get right.

| Decision | Why |
|---|---|
| **One HTML file, not MkDocs** | Started as MkDocs Material and abandoned it. Students on lab machines, workshops with broken wifi, a manual that must outlive its toolchain. |
| **Identifiers in English, prose in French** | Folders, files, CSV columns, status values. French students read English fine, and English identifiers survive being pasted into tools and forums. Enforced by audit pass 5. |
| **This is a technical-skills course** | Students finish able to produce a film. Not a theory course. |
| **Hybrid ≠ documentary** | Hybrid means generative + non-generative *material*. The site and references may be real **or entirely invented** — two routes, one pipeline from chapter 7 on. Documenting a real place is never a requirement. |
| **Two routes to a *référentiel*** | Captured (photograph a real place) or constructed (generate research images, then *cull*). Both produce the same `01_references/`. |
| **Students only touch the front apps** | Teachers run ComfyQ server and the LlmOnLan farm. The manual documents only the ComfyQ web UI, the LlmOnLan client and ComfyQ Discovery. Server components go in `CAPTURE-GUIDE.md`, never in the manual — a student who reads about the server tries to install it. |
| **Two level bands, cumulative** | `data-level="p"` = A3+, `data-level="r"` = A4+. Tagged with the *lowest* band that needs it, so nothing is unlearned between years. A third band would be a second manual in disguise. |
| **24 fps, 16:9, sRGB/Rec.709** | §10.4. 24 because that is what the models output; converting to 25 costs a 4 % speed change or judder. Three of the four format values cannot be repaired after generation. |
| **Open calls, not film festivals** | Students submit to design open calls and student competitions. A design call judges the *project*, so Deliverable A is already most of the dossier. §17.7. |
| **Perishable facts are concentrated** | Model names, versions, VRAM figures live in chapter 3 + `prompts.html` + `outils.html`. Everywhere else: roles and methods. The manual says *"where the manual and your installation disagree, believe the software."* |
| **Tool authors are credited** | ComfyQ and LlmOnLan are by **b2renger**, named and linked at every point of use and in every footer. Non-negotiable. |

---

## Facts that must stay consistent everywhere

Change one of these and you must change all of its homes. The audit checks the last two.

- **20 shots × 3 s = 60 s**, in five blocks of **3 · 5 · 4 · 5 · 3** (9/15/12/15/9 s)
- **17 stages**, numbered continuously across the manual, not per chapter
- **Four deliverables** — A production folder · B storyboard · C film · D *(A4·A5)* a reusable asset
- **Four assessment axes** — spécificité, cohérence, intention, méthode
- **Shot-sheet header**, byte-identical in the manual and in the template:
  `shot,block,duration,action,size,angle,movement,place,light,intent,sound,ref_images,seed,status`
  — values `todo` / `image_ok` / `video_ok` / `approved`, movement `static`
- **The project tree** (both editions must list the same directories):
  `00_brief/ 01_references/{photo,video,sound,docs,style}/ 02_writing/ 03_breakdown/ 04_bibles/ 05_storyboard/APPROVED/ 06_shots/APPROVED/ 07_sound/{ambience,voice,music,sfx}/ 08_edit/ 09_export/ journal.md`

---

## Editing the manual

The single file is **canonical**. Any `parts/` in a scratch directory is stale the
moment the file is edited directly — do not resurrect them.

Edit with a script, never by hand:

```python
import io
p = "recits_generatifs_manuel-v1.html"
t = io.open(p, encoding="utf-8").read()
old = "…distinctive prose, not tag soup…"
assert t.count(old) == 1, "count=%d" % t.count(old)     # never skip
t = t.replace(old, new)
io.open(p, "w", encoding="utf-8", newline="").write(t)   # newline="" keeps line endings
```

**Both editions in the same script.** Write the FR block and its EN twin together;
never write one language and translate later. Section numbers, identifiers, table
rows and stage numbers must match — the audit compares them.

Four traps, all of which have actually bitten:

- **`count == 1` is not enough.** It guards against a multi-replace, not against
  matching the *wrong* single place. A glossary row for C2PA landed in chapter 17's
  export table because `<tr><td>Cadence</td>` had just been added there. Anchor on
  text distinctive to the *section* you mean, and check what you matched.
- **`PYTHONIOENCODING=utf-8`** before printing anything containing `│ · —` or an
  accent, or the script dies in `cp1252` at the print and you debug the wrong thing.
- **Never mutate the repo to test a hypothesis.** A line-ending experiment ran
  `shutil.rmtree` on the template tree and the deletion got committed. Copy to the
  scratch directory first.
- **A shared word occurs twice.** "Export" is the same in both editions, so
  `<h3>17.5 Export</h3>` matched twice. Pass the expected count explicitly.

For a long insertion, write the FR and EN blocks to scratch files and splice them in.
Do not compose 400 lines inside a shell heredoc.

---

## Before every commit

```bash
python tools/audit.py            # 7/7, exit code = failing passes
python templates/build-zip.py    # only if templates/ changed — CI checks the hash
```

Then, when the change warrants it:

- **Every new external link HTTP-checked.** All of them, every time.
  `grep -oh 'href="https\?://[^"]*"' *.html | sed 's/.*href="//;s/"$//' | sort -u`
  then `curl -s -o /dev/null -w '%{http_code}'` each one.
- **Both editions read** for the section you touched, with no leftover text from the
  other language. English *prompts* inside the French edition are correct by design.
- **README figures re-derived** — size, word count, section count, symptom rows, FAQ
  entries, glossary terms. These go stale silently after every substantial edit and
  nothing catches them.
- Level filter at the lowest band: the manual still reads, nothing dangles.
- `?figures` reviewed if you added a figure slot, and it is listed in `CAPTURE-GUIDE.md`.

Commit in full prose: what changed, why, what was verified, and what you deliberately
did **not** do. The log is the only record of *why*, and it has repaid that already.

Git identity is set locally in this repo: `urbandronedesign
<7166404+urbandronedesign@users.noreply.github.com>`. There is no global config.
Do not use a personal email address in commits.

Push, then check CI **and** the live URL — a push can succeed, CI can pass, and the
page still 404.

---

## State, as of August 2026

Everything below is done and live. The two open items are the only ones outstanding
from a 30-finding specialist audit of the course.

**Recently added** — the tool-explainer companion (`outils.html`), the three
ComfyQ workflows the manual had never mentioned (masked inpainting, SAM3,
LivePortrait) with the caveat that they do not excuse a bad breakdown, `§10.4` the
technical format, `§17.4` undoing the AI look, `§17.6–17.8` delivery / open calls /
archiving, C2PA in `§18.2`, and three template files the manual referenced but the
archive never shipped (`04_bibles/prompts.md`, `00_brief/LICENCES/`,
`00_brief/consent_form.md`).

**Open**

1. **A worked end-to-end example** — one shot carried from question to export, with
   the real prompts, seeds and rejects. Undecided: a companion page, or woven
   through the chapters. Best built from a film that actually exists, not invented.
2. **The assessment rubric with per-level criteria** — deliberately left to the
   teacher. The four axes exist; the grading scale is not Claude's to invent.

**Known asymmetries that are correct** — do not "fix" these:

- The glossary is one shared table, both languages in the same rows. That is the
  point of a glossary.
- `LICENCES/` is spelled the British way and is intentionally not in the sweep's
  banned list.
- Chapter 3 and the two companion pages are *expected* to go stale. That is their job.
