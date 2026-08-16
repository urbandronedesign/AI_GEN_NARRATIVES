#!/usr/bin/env python3
"""Build gabarits/dossier-de-projet.zip from gabarits/FILM_2026_project-name/.

The repo needs .gitkeep files to track empty directories; a student's archive
should not contain them. So we zip the real files, then re-create every empty
directory as a proper zip directory entry.

    python gabarits/build-zip.py
"""
import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "FILM_2026_project-name")
OUT = os.path.join(HERE, "dossier-de-projet.zip")
ROOT = "FILM_2026_project-name"

if not os.path.isdir(SRC):
    raise SystemExit("source tree not found: " + SRC)

files, dirs = [], []
for base, subdirs, names in os.walk(SRC):
    rel = os.path.relpath(base, SRC).replace("\\", "/")
    prefix = ROOT if rel == "." else ROOT + "/" + rel
    real = [n for n in sorted(names) if n != ".gitkeep"]
    for n in real:
        files.append((os.path.join(base, n), prefix + "/" + n))
    # a directory with no real file of its own still has to exist in the archive
    if not real:
        dirs.append(prefix + "/")

# Deterministic: identical inputs must give a byte-identical archive, so CI can tell
# "a template changed and the zip was not rebuilt" from "the zip was rebuilt on another
# day". That means a fixed timestamp on every entry rather than the file's mtime, which
# a fresh git checkout rewrites anyway.
STAMP = (2026, 1, 1, 0, 0, 0)
TEXT = {".md", ".csv", ".txt", ".json"}

def entry(name):
    """A ZipInfo with every platform-dependent field pinned.

    ZipInfo defaults create_system to 0 on Windows and 3 elsewhere, which alone is
    enough to change the archive's bytes between a maintainer's laptop and CI.
    """
    info = zipfile.ZipInfo(name, STAMP)
    info.create_system = 3      # Unix, on every host
    info.create_version = 20
    info.extract_version = 20
    return info


with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for d in sorted(dirs):
        info = entry(d)
        info.external_attr = (0o40755 << 16) | 0x10  # directory bit
        z.writestr(info, b"")
    for abspath, arcname in sorted(files, key=lambda x: x[1]):
        info = entry(arcname)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        with open(abspath, "rb") as fh:
            data = fh.read()
        # Normalise line endings to LF. Otherwise the archive's bytes depend on whether
        # the working tree happens to hold CRLF or LF, and the "is the zip stale?" check
        # in CI would fire on a fresh checkout rather than on a real change.
        if os.path.splitext(arcname)[1].lower() in TEXT:
            data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        z.writestr(info, data)

kb = os.path.getsize(OUT) // 1024
print("wrote %s  (%d files, %d empty dirs, %d KB)" % (
    os.path.relpath(OUT, os.path.dirname(HERE)), len(files), len(dirs), kb))
for _, a in sorted(files, key=lambda x: x[1]):
    print("   ", a)
for d in sorted(dirs):
    print("    (dir)", d)
