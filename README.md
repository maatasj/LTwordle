# Žodinėlis

A Lithuanian 5-letter Wordle web game (`https://maatasj.github.io/LTwordle/web/`).

## Folder Structure
- `web/` — Static web page (`index.html`, `styles.css`, `app.js`)
- `src/` — C module and console generator (Stages 2–3)
- `assets/` — Lithuanian word lists, filtering script (`filterNwords.py`), and license (`COPYING.txt`)
- `reports/` — Cumulative team report (`report.md`)

## Running Locally
1. Open `web/index.html` directly in any web browser (or serve the `web/` folder with a local HTTP server).
2. To regenerate the 5-letter word list from `assets/lithuanian-words-list.txt`:
   ```bash
   python3 assets/filterNwords.py
