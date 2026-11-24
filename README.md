# memory-deck

Code-based slides for **Managing Memory for AI Agents** (re:Invent 2026).

Live: https://mongodb-developer.github.io/memory-deck/

## Present
Open the live URL (or `index.html` locally) in Chrome and press **F** for fullscreen.

| Key | Action |
|---|---|
| → / PageDown / Space / Enter | next step |
| ← / PageUp | back |
| B or . | blackout |
| T | toggle agent trace |
| S | speaker notes + timer |
| Home / End | first / last slide |

Deep link to a slide/step: `#/12/1`.

## Edit
Slides are in `src/slides/NN-*.html`; shared engine and CSS in `src/shell.html`.
Rebuild `index.html` after editing:

    python3 build.py

Trace numbers and some sample results are illustrative placeholders.

## QR slide
`src/parked/08-scan-slides.html` is parked. To enable it: replace `assets/qr-slides.png`
with a QR code for the live URL, move the file into `src/slides/`, then run `python3 build.py`.
