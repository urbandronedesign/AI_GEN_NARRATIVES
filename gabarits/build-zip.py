#!/usr/bin/env python3
"""Build gabarits/dossier-de-projet.zip from gabarits/FILM_2026_nom-du-projet/.

The repo needs .gitkeep files to track empty directories; a student's archive
should not contain them. So we zip the real files, then re-create every empty
directory as a proper zip directory entry.

    python gabarits/build-zip.py
"""
import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "FILM_2026_nom-du-projet")
OUT = os.path.join(HERE, "dossier-de-projet.zip")
ROOT = "FILM_2026_nom-du-projet"

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

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for d in sorted(dirs):
        z.writestr(zipfile.ZipInfo(d), b"")
    for abspath, arcname in sorted(files, key=lambda x: x[1]):
        z.write(abspath, arcname)

kb = os.path.getsize(OUT) // 1024
print("wrote %s  (%d files, %d empty dirs, %d KB)" % (
    os.path.relpath(OUT, os.path.dirname(HERE)), len(files), len(dirs), kb))
for _, a in sorted(files, key=lambda x: x[1]):
    print("   ", a)
for d in sorted(dirs):
    print("    (dir)", d)
