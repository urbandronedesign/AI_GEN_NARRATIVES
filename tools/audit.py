#!/usr/bin/env python3
"""Audit the manual for internal consistency.

    python tools/audit.py            # audit the repo, print a report
    python tools/audit.py --quiet    # only print failures

Seven passes, in order of how expensive the mistake is to discover late:

  1  HTML validity      unclosed or mismatched tags in any page
  2  Anchors            every href="#…" resolves to an id that exists
  3  Fact parity        the two language editions agree on section numbers,
                        identifiers, cross-references, year tags, stage numbers
                        and figure numbers — everything that names one reality
  4  Structural parity  a chapter with five table rows in French and four in
                        English is missing a row somewhere
  5  Identifier sweep   no French folder, file, column or value names survive
                        (French *prose* is fine — only identifiers are checked)
  6  Cross-file         the shot-sheet header in the manual is byte-identical to
                        the one in the downloadable template, and both trees list
                        the same directories
  7  Year bands         data-level blocks are paired FR/EN, so a band hides the
                        same content in both editions

Exit code is the number of failing passes, so this works in CI unchanged.
Standard library only.
"""
import io
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(ROOT, "recits_generatifs_manuel-v1.html")
PAGES = ["recits_generatifs_manuel-v1.html", "prompts.html", "outils.html", "index.html"]
TEMPLATE_CSV = os.path.join(ROOT, "templates", "FILM_2026_project-name",
                            "03_breakdown", "shot_sheet.csv")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr", "circle", "ellipse", "line", "path",
        "polygon", "polyline", "rect", "use", "stop"}

QUIET = "--quiet" in sys.argv
FAILURES = []


def say(msg=""):
    if not QUIET:
        print(msg)


def fail(pass_name, detail):
    FAILURES.append(pass_name)
    print("  FAIL  " + detail)


def ok(detail):
    say("  ok    " + detail)


# ─────────────────────────────── language filter ───────────────────────────────

class LangFilter(HTMLParser):
    """Re-emit the document with every element carrying `drop` (and its subtree) gone."""

    def __init__(self, drop):
        super().__init__(convert_charrefs=False)
        self.drop, self.out, self.skip = drop, [], 0

    def handle_starttag(self, tag, attrs):
        dropping = self.drop in (dict(attrs).get("class") or "").split()
        if self.skip:
            if tag not in VOID:
                self.skip += 1
            return
        if dropping:
            if tag not in VOID:
                self.skip = 1
            return
        self.out.append(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        if not self.skip and self.drop not in (dict(attrs).get("class") or "").split():
            self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.skip:
            self.skip -= 1
            return
        self.out.append("</%s>" % tag)

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)

    def handle_entityref(self, n):
        if not self.skip:
            self.out.append("&%s;" % n)

    def handle_charref(self, n):
        if not self.skip:
            self.out.append("&#%s;" % n)


def view(html, keep):
    p = LangFilter("en-only" if keep == "fr" else "fr-only")
    p.feed(html)
    return "".join(p.out)


def sections(html):
    return {m.group(1): m.group(2) for m in
            re.finditer(r'<section class="chap" id="([^"]+)"(.*?)</section>', html, re.S)}


# ───────────────────────────── 1 · HTML validity ─────────────────────────────

class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.err = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.err.append("line %d: stray </%s>" % (self.getpos()[0], tag))
        elif self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    unclosed = ["<%s> @%d" % x for x in self.stack[i + 1:]]
                    self.err.append("line %d: </%s> but unclosed %s"
                                    % (self.getpos()[0], tag, unclosed))
                    del self.stack[i:]
                    break
            else:
                self.err.append("line %d: </%s> never opened" % (self.getpos()[0], tag))


def pass_html():
    say("1 · HTML validity")
    for rel in PAGES:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        b = Balance()
        b.feed(io.open(p, encoding="utf-8").read())
        if b.err or b.stack:
            fail("html", "%s: %s %s" % (rel, b.err[:3], [x[0] for x in b.stack]))
        else:
            ok("%-34s balanced" % rel)


# ─────────────────────────────── 2 · anchors ───────────────────────────────

def pass_anchors():
    say("\n2 · Anchors")
    for rel in PAGES:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        t = io.open(p, encoding="utf-8").read()
        ids = set(re.findall(r'\bid="([^"]+)"', t))
        # skip hrefs built inside JS string concatenation
        hrefs = {h for h in re.findall(r'href="#([^"]+)"', t) if "'" not in h and "+" not in h}
        bad = sorted(hrefs - ids)
        if bad:
            fail("anchors", "%s: dangling %s" % (rel, bad))

        # local page-to-page links: the file has to be there
        local = {h.split("#")[0] for h in re.findall(r'href="([^"#][^"]*)"', t)
                 if not re.match(r"https?:|mailto:|//", h)}
        missing = sorted(f for f in local if f and not os.path.exists(os.path.join(ROOT, f)))
        if missing:
            fail("anchors", "%s: links to missing file(s) %s" % (rel, missing))

        if not bad and not missing:
            ok("%-34s %d anchors + %d page links resolve" % (rel, len(hrefs), len(local)))


# ───────────────────────────── 3 · fact parity ─────────────────────────────

def facts(block):
    return {
        "sections": sorted(set(re.findall(r"<h3[^>]*>\s*(\d+\.\d+)", block))),
        "code": sorted({re.sub(r"\s+", " ", c).strip()
                        for c in re.findall(r"<code[^>]*>(.*?)</code>", block, re.S)
                        if re.search(r"[/._]|^[a-z_]+$|^P\d", re.sub(r"<[^>]+>", "", c))}),
        "xref": sorted(set(re.findall(
            r'href="#(ch\d+|parcours|projet|derives|faq|glossaire|comment-utiliser)"', block))),
        "tags": sorted(re.findall(r'lv-tag">([^<]+)<', block)),
        "stages": sorted(set(re.findall(r'class="hd">\s*(?:Étape|Stage)\s*(\d+)', block))),
        "figs": sorted(set(re.findall(r"Fig\s*(\d+\.\d+)", block))),
    }


def pass_fact_parity(fr, en):
    say("\n3 · Fact parity between editions")
    bad = 0
    for k in [x for x in fr if x in en]:
        f, e = facts(fr[k]), facts(en[k])
        for field in ("sections", "stages", "figs", "tags", "xref", "code"):
            only_fr = [x for x in f[field] if x not in e[field]]
            only_en = [x for x in e[field] if x not in f[field]]
            if only_fr or only_en:
                bad += 1
                fail("fact-parity", "[%s] %s  FR-only %s  EN-only %s"
                     % (k, field, only_fr or "-", only_en or "-"))
    if not bad:
        ok("%d sections agree on every identifier and number" % len(fr))


# ──────────────────────────── 4 · structural parity ────────────────────────────

def counts(b):
    pat = {"tables": r"<table", "rows": r"<tr", "callouts": r'class="callout',
           "prompts": r'class="pr"', "h3": r"<h3", "h4": r"<h4", "li": r"<li",
           "pre": r"<pre", "exercises": r'class="exercise"', "faq": r'details class="faq"'}
    return {k: len(re.findall(v, b)) for k, v in pat.items()}


def pass_structural_parity(fr, en):
    say("\n4 · Structural parity between editions")
    bad = 0
    for k in [x for x in fr if x in en]:
        cf, ce = counts(fr[k]), counts(en[k])
        diff = {f: (cf[f], ce[f]) for f in cf if cf[f] != ce[f]}
        if diff:
            bad += 1
            fail("structure", "[%s] %s" % (k, ", ".join(
                "%s FR%d/EN%d" % (f, a, b) for f, (a, b) in sorted(diff.items()))))
    if not bad:
        ok("%d sections have matching structure" % len(fr))


# ───────────────────────────── 5 · identifier sweep ─────────────────────────────

# Distinctive enough that they cannot occur in prose.
BANNED_ANYWHERE = ["02_ecriture", "03_decoupage", "04_chartes", "06_plans", "07_son/",
                   "08_montage", "VALIDE", "feuille_de_plans", "charte_personnage",
                   "charte_lieu", "charte_style", "fiche_problematique",
                   "cinq_regles_du_monde", "LISEZ-MOI", "nom-du-projet", "SON_00",
                   # repo-level asset names — the word "gabarit" in prose is fine,
                   # a path or a filename is not
                   "gabarits/", "dossier-de-projet"]
# French column names and values. Only checked inside <code> and <pre>, so that the
# ordinary French words (plan, son, lieu, ambiances…) stay untouched in prose.
BANNED_IN_CODE = ["statut", "a_faire", "valide", "duree", "echelle", "lumiere",
                  "mouvement", "intention", "bloc", "fixe", "plan", "son", "lieu",
                  "ambiances", "voix", "musique"]


def literals(t):
    """Strings from a document that are *identifiers* rather than prose.

    Prompt blocks are full of French sentences, so a naive scan of <pre> would flag
    every one of them. Only three shapes count as an identifier: an inline code span
    holding a single token, a backticked single token in Markdown, and a line of a
    file tree or a CSV row.
    """
    out = []
    for c in re.findall(r"<code[^>]*>(.*?)</code>", t, re.S):
        c = re.sub(r"<[^>]+>", "", c).strip()
        if c and " " not in c:
            out.append(c)
    for c in re.findall(r"`([^`\n]+)`", t):
        c = c.strip()
        if c and " " not in c:
            out.append(c)
    blocks = re.findall(r"<pre[^>]*>(.*?)</pre>", t, re.S) or [t]
    for blk in blocks:
        # A tree line is "path  <span class=cm>comment</span>", and in the French
        # edition that comment is deliberately French prose. Only the path counts as
        # an identifier, so drop the comment before scanning. Nothing is lost: French
        # file and folder names are caught by BANNED_ANYWHERE, which scans everything.
        blk = re.sub(r'<span class="cm">.*?</span>', "", blk, flags=re.S)
        for line in re.sub(r"<[^>]+>", "", blk).splitlines():
            s = line.strip()
            if any(g in line for g in ("├──", "└──", "│")) \
               or re.match(r"^[a-z_]+(,[a-z_]+){3,}", s) \
               or re.match(r"^P\d\d,", s):
                out.append(line)
    return out


def pass_sweep():
    say("\n5 · French identifiers")
    scan = [os.path.join(ROOT, p) for p in PAGES + ["README.md", "CAPTURE-GUIDE.md", "CLAUDE.md"]]
    scan += [os.path.join(ROOT, "templates", "README.md")]
    for base, _, names in os.walk(os.path.join(ROOT, "templates", "FILM_2026_project-name")):
        scan += [os.path.join(base, n) for n in names if n != ".gitkeep"]
    hits = 0
    for p in sorted(set(scan)):
        if not os.path.isfile(p):
            continue
        t = io.open(p, encoding="utf-8", errors="replace").read()
        rel = os.path.relpath(p, ROOT)
        for term in BANNED_ANYWHERE:
            if term in t:
                fail("sweep", "%s: %r (%dx)" % (rel, term, t.count(term)))
                hits += 1
        for term in BANNED_IN_CODE:
            where = [s for s in literals(t)
                     if re.search(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", s)]
            if where:
                fail("sweep", "%s: %r used as an identifier — %s"
                     % (rel, term, where[0][:60]))
                hits += 1
    if not hits:
        ok("no French folder, file, column or value names remain")


# ───────────────────────────── 6 · cross-file ─────────────────────────────

def pass_crossfile(manual):
    say("\n6 · Manual vs downloadable template")
    if not os.path.exists(TEMPLATE_CSV):
        fail("crossfile", "template shot sheet missing: %s" % TEMPLATE_CSV)
        return
    tpl = io.open(TEMPLATE_CSV, encoding="utf-8").read().splitlines()
    hdrs = re.findall(r"shot,block,duration[^\n<]*", manual)
    if not hdrs:
        fail("crossfile", "no shot-sheet header found in the manual")
    elif tpl[0].strip() != hdrs[0].strip():
        fail("crossfile", "header differs\n          manual   %s\n          template %s"
             % (hdrs[0], tpl[0]))
    else:
        ok("shot-sheet header identical (%d columns)" % len(tpl[0].split(",")))
    rows = [r for r in tpl[1:] if r.strip()]
    if len(rows) != 20:
        fail("crossfile", "template has %d shot rows, expected 20" % len(rows))
    else:
        total = sum(int(r.split(",")[2]) for r in rows)
        if not (58 <= total <= 62):
            fail("crossfile", "template durations sum to %d s, expected 60 (± 2)" % total)
        else:
            ok("20 rows, durations sum to %d s" % total)
    trees = re.findall(r"<pre>FILM_2026_.*?journal\.md", manual, re.S)
    dirsets = [tuple(sorted(set(re.findall(r"\b\d\d_[a-z]+/", t)))) for t in trees]
    if len(set(dirsets)) > 1:
        fail("crossfile", "the two editions' trees list different directories")
    elif dirsets:
        ok("both editions list the same %d directories" % len(dirsets[0]))


# ───────────────────────────── 7 · year bands ─────────────────────────────

def pass_bands(manual):
    say("\n7 · Year bands")
    for lvl in ("p", "r"):
        fr = en = 0
        for m in re.finditer(r'<div data-level="%s">' % lvl, manual):
            stack = []
            for d in re.finditer(r"<div\b([^>]*)>|</div>", manual[:m.start()]):
                if d.group(0) == "</div>":
                    if stack:
                        stack.pop()
                else:
                    a = d.group(1) or ""
                    stack.append("fr" if 'class="fr-only"' in a
                                 else "en" if 'class="en-only"' in a else ".")
            langs = [x for x in stack if x in ("fr", "en")]
            cur = langs[-1] if langs else None
            if cur == "fr":
                fr += 1
            elif cur == "en":
                en += 1
            else:
                fail("bands", 'data-level="%s" block sits outside any language wrapper' % lvl)
        if fr != en:
            fail("bands", 'data-level="%s" unbalanced: FR %d, EN %d' % (lvl, fr, en))
        else:
            ok('data-level="%s"  FR %d = EN %d' % (lvl, fr, en))


# ─────────────────────────────────── main ───────────────────────────────────

def main():
    if not os.path.exists(MANUAL):
        sys.exit("manual not found: %s" % MANUAL)
    manual = io.open(MANUAL, encoding="utf-8").read()
    fr, en = sections(view(manual, "fr")), sections(view(manual, "en"))

    say("AUDIT · %s" % os.path.basename(MANUAL))
    say("%d KB · %d sections\n" % (len(manual.encode()) // 1024, len(fr)))

    pass_html()
    pass_anchors()
    pass_fact_parity(fr, en)
    pass_structural_parity(fr, en)
    pass_sweep()
    pass_crossfile(manual)
    pass_bands(manual)

    distinct = sorted(set(FAILURES))
    print()
    if distinct:
        print("AUDIT FAILED · %d problem(s) across %d pass(es): %s"
              % (len(FAILURES), len(distinct), ", ".join(distinct)))
    else:
        print("AUDIT PASSED · 7 passes, no problems")
    sys.exit(len(distinct))


# Guarded so the passes can be imported and reused by other scripts without the
# whole audit running as a side effect of the import.
if __name__ == "__main__":
    main()
