# Auburn Graduate Student Seminar — Math

## Overview

- Event: Graduate Student Seminar, Department of Mathematics & Statistics, Auburn University
- Date: September 3, 2025 (09/03/2025)
- Speaker: Le Chen
- Talk title: How do surfaces grow?

This repository contains the Reveal.js slide deck (`index.html`) and supporting media for the seminar. The deck is a static site; open locally or via GitHub Pages.

## Live Deck

- GitHub Pages: https://chenle02.github.io/Graduate_Student_Seminar_2025-09-04/
- Direct slide URL: https://chenle02.github.io/Graduate_Student_Seminar_2025-09-04/index.html

If media does not autoplay over `file://`, use the Pages link above or run a local server.

## Abstract

How do surfaces grow, and why do so many look statistically alike?
  This talk connects intuitive simulations with modern probability to explore
  surface growth and universality. We begin with a CLT refresher as a baseline
  for randomness, then show why it fails for growing interfaces: local
  interactions and spatial-temporal dependencies break independence. Using
  Tetris-like ballistic deposition (sticky and non-sticky) as model systems, we
  compare simulated interfaces and empirical fluctuation scaling, and discuss
  their relation to the KPZ universality class. We then highlight experimental
  evidence from thin-film growth where universal scaling emerges in real
  materials. Along the way, we emphasize what "universality" means, how scaling
  exponents organize phenomena, and where open questions remain—such as
  identifying non-KPZ behaviors. The goal is a concrete, visual understanding of
  stochastic growth, bridging simulations, data, and theory.  

## Local Setup (uv optional)

- Install uv:
  - macOS (brew): `brew install uv`
  - Linux/macOS (script): `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows (scoop): `scoop install uv`
- Create local venv: `uv venv -p 3.11`
- Install deps: `uv sync`
- Verify Manim: `uv run python -c "import manim; print(manim.__version__)"`

### System Dependencies

- FFmpeg (required for Manim video rendering):
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt-get install ffmpeg`
  - Windows: Install FFmpeg and add it to PATH.
- LaTeX (optional, for TeX text in scenes): TeX Live or MiKTeX.

## How To View

- Quick open: Open `index.html` directly in a browser (some media may not autoplay).
- Local server (recommended): `python3 -m http.server 8000` and visit `http://localhost:8000/index.html`.
- With uv: `uv run python -m http.server 8000`.

## Notes

- See `AGENTS.md` for repository guidelines (structure, testing, media, and docs).
- Manim render outputs to `media/`; final videos should live under `videos/` and be referenced by slides using relative paths.

## Rendering Animations with Make

A `Makefile` is provided to simplify the rendering of Manim animations. From the project root, you can use the following commands:

- `make all`: Renders both the original and the Gemini-generated LIS animations.
- `make lis`: Renders only the original LIS animation.
- `make lis-gemini`: Renders only the Gemini-generated LIS animation.
- `make clean`: Removes the `media/` directory created by Manim.

The `Makefile` handles the creation of the `videos/` directory and copies the rendered animations to the correct location.

## Custom Styles (mystyle_2025.css)

Use these helper classes in `index.html` to get consistent layout and sizing:

- `flex-container`: Side‑by‑side layout for media or cards. Wrap related blocks: `<div class="flex-container">…</div>`.
- `coauthor-container`: Compact avatar + text card, intended inside `flex-container`.
- `SimulationVideo`: Applies wide, responsive sizing to `<video>` elements used throughout the deck.
- `video-grid`: Two‑column grid for multiple videos: `<div class="video-grid"><video …></video><video …></video></div>`.
- `block`: Split view with a main video on the left and a right column; pair with `image-pair`.
- `image-pair`: Vertical stack of two images (right column of `block`).
- `source`: Small, italic credit line beneath media (images/videos).
- `left-text`: Left‑align text when the default center alignment isn’t desired.
- `bibtexnumber` / `bibtexitem`: Right‑aligned, slightly smaller typesetting for references/citations.
- `theorem`: Subtle background highlight for theorem/definition callouts.
- `img-tall-slide`: Constrain tall images so math or captions below remain visible; adds `max-height: 45vh`. Example: `<img class="img-tall-slide" src="…" />`.

Notes
- Global images default to a generous height with rounded corners. Add `img-tall-slide` (or inline styles) if an image crowds formulas/captions.
- ESC overview highlight is enhanced via CSS; no markup needed.

## Acknowledgments

- NSF: Support from DMS-CAREER and DMS-Probability awards.
- Simons Foundation: Support acknowledged.
- Manim: Animation engine used for LIS/RSK and visualizations — https://www.manim.community/
- Reveal.js: Presentation framework powering `index.html` — https://revealjs.com/
- Gemini CLI: Assisted ideation and refinement of some animations.
- Codex CLI: Coding assistant used to help edit and maintain the repo — https://github.com/openai/codex-cli
- SPDEs-Bib: Linked bibliographic resources — https://chenle02.github.io/SPDEs-Bib/index.html

## License & Attribution

- Dual license:
  - Code (e.g., `Longest_increasing_subsequence/`, `Makefile`, scripts): MIT — see `LICENSE-CODE`.
  - Content (e.g., `index.html`, `assets/`, `videos/`, `movies/`, `mystyle_2025.css`): CC BY 4.0 — see `LICENSE-CONTENT`.
- Vendored dependencies under `dist/`, `js/`, and `plugin/` retain their upstream licenses (e.g., Reveal.js under MIT).
- Attributions: External images/videos are credited in-slide. References are linked in `References_bib.html` and in-slide citations.
