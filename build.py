#!/usr/bin/env python3
"""Assemble index.html from src/shell.html + src/slides/NN-*.html (sorted by filename)."""
import pathlib
root = pathlib.Path(__file__).parent
parts = sorted((root / "src" / "slides").glob("[0-9][0-9]-*.html"))
shell = (root / "src" / "shell.html").read_text()
body = "\n".join(f"<!-- {p.name} -->\n" + p.read_text().strip() for p in parts)
(root / "index.html").write_text(shell.replace("<!--SLIDES-->", body))
print(f"built index.html from {len(parts)} slides")
