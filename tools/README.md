# tools

## `audit.py`

```bash
python tools/audit.py            # full report
python tools/audit.py --quiet    # only failures — what CI prints
```

Standard library only, no dependencies. Exit code is the number of failing passes, so
it works unchanged in CI.

**Run it after every edit to the manual.** It exists because this document has two
editions of the same reality, and the ways they drift apart are not the ways you notice
by reading.

### The seven passes

| | Pass | Catches |
|---|---|---|
| 1 | HTML validity | unclosed or mismatched tags in any page — a 6 000-line hand-edited file makes this easy to do and hard to see |
| 2 | Anchors | an `href="#ch12"` pointing at a section that was renamed |
| 3 | **Fact parity** | the two editions disagreeing on a section number, an identifier, a cross-reference, a year tag, a stage number or a figure number |
| 4 | **Structural parity** | one edition having five table rows where the other has four — i.e. content silently missing from a translation |
| 5 | Identifier sweep | a French folder, file, column or value name surviving a rename |
| 6 | Cross-file | the shot-sheet header in the manual drifting from the one in the downloadable template; the two trees listing different directories; the template's durations no longer summing to 60 s |
| 7 | Year bands | a `data-level` block present in one language and not the other, which would hide different content per edition |

### What it found the first time it ran

Not hypothetical failures — these were live in the published manual:

- the **English chapter 6 had lost a sign-off criterion** (`INDEX.md exists and someone
  else could use it`), dropped while rewriting that exercise for two routes;
- the **English chapter 9 had no CSV example at all** — the filled shot sheet, the most
  concrete artefact in the chapter, existed only in French;
- a stray `class="pr"` span left over from an earlier hack;
- example filenames that differed between editions (`PHOTO_014_halle-nord…` vs
  `…north-hall…`), so the two editions taught different naming;
- `denoise 0,3` — a French decimal comma inside a value the reader types into software;
- and on its very first run after the English rename, a leftover `personnage · lieu ·
  style` in the `prompts.html` folder tree.

### Reading a failure

Passes 3 and 4 print the section id and the field, with what is present in one edition
and absent from the other:

```
FAIL  [ch6] code  FR-only ['INDEX.md']  EN-only -
```

That means the French edition names `INDEX.md` in that chapter and the English does not.
Usually the fix is to add the missing thing, not to remove the extra one.

### Deliberate asymmetries

Two are expected and are **not** reported, because the passes are scoped to avoid them:

- **French prose is not swept.** `ambiances`, `plan`, `son` and `lieu` are ordinary French
  words used constantly in the text. Pass 5 only inspects identifiers: single-token code
  spans, backticked single tokens, file-tree lines and CSV rows.
- **Prompt blocks contain French sentences by design.** The `<pre>` inside a `.pr` block is
  a prompt to be copied, not a path, so it is excluded from the identifier sweep.

If you add a genuine asymmetry on purpose, scope it the same way rather than loosening a
pass — an audit that reports noise stops being read.
