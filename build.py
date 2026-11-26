#!/usr/bin/env python3
"""Assemble index.html from src/shell.html + src/slides/NN-*.html (sorted by filename)."""
import pathlib
root = pathlib.Path(__file__).parent
parts = sorted((root / "src" / "slides").glob("[0-9][0-9]-*.html"))
shell = (root / "src" / "shell.html").read_text()
import re
body = "\n".join(f"<!-- {p.name} -->\n" + re.sub(r"render slide \d\d", f"render slide {i:02d}", p.read_text().strip()) for i, p in enumerate(parts, 1))
(root / "index.html").write_text(shell.replace("<!--SLIDES-->", body))
print(f"built index.html from {len(parts)} slides")
