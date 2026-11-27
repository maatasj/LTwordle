# Žodinėlis — Cumulative Project Report

**Repository:** https://github.com/maatasj/LTwordle  
**Published Page:** https://maatasj.github.io/LTwordle/web/

## Stage 1 (Due: November 29, 2026)

### 1. Project Concept
**Žodinėlis** is a Lithuanian 5-letter Wordle-style web game where the player tries to guess a hidden 5-letter Lithuanian word in six attempts using color-coded letter feedback (green for exact position, yellow for present in another position, gray for absent).

Across the three course stages, the project evolves from a static HTML/CSS prototype (Stage 1) into a reusable C module (Stage 2) and a C console tool that customizes and generates the web page files locally without manual code edits (Stage 3).

### 2. Team & Roles
* **Matas:** Facilitator, Exhibitor
* **Alan:** Builder (Frontend), Designer
* **Ratmir:** Builder (C)
* **Ignas:** Architect, Critic

### 3. Stage 1 Accomplishments & Architecture
* **Static Web Prototype (web/index.html):** Created a static HTML/CSS layout displaying the game title, 5-letter grid structure, tile feedback colors, and sample Lithuanian words.
* **Online Deployment:** Published the static web page via GitHub Pages at https://maatasj.github.io/LTwordle/web/.
* **Word List Filtering (assets/):** Extracted 5-letter Lithuanian words into `5-letter-lithuanian-words-list.txt` using `filterNwords.py`.
* **Repository & Stage Scaffolding:** Set up the project directory structure (`web/`, `src/`, `assets/`, `reports/`) with placeholders (`src/main.c`, `web/styles.css`, `web/app.js`) ready for Stages 2 and 3.

### 4. Stage 1 Time Log (Hours by Team Member)

| Team Member | Hours |
| :--- | :---: |
| **Matas** | 1.5 |
| **Alan** | 1.0 |
| **Ratmir** | 0.0 |
| **Ignas** | 0.0 |
| **Team Total** | **2.5** |