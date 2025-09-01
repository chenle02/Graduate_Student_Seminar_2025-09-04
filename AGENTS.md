# Repository Guidelines

## Project Structure & Module Organization
- `index.html`: Main Reveal.js slide deck for 2025-09-03.
- `assets/`: Images and logos used by slides (e.g., `Random_Deposition_Demo.png`).
- `videos/` and `movies/`: Local media referenced via `<video>` tags.
- `css/`: Source styles (SCSS themes) from Reveal.js; do not edit unless updating themes.
- `dist/`, `js/`, `plugin/`: Vendored Reveal.js distribution and plugins; treat as read-only.
- `mystyle_2025.css`: Custom styling overrides for this talk.
- `bibtex/`, `References_bib.html`: Bibliography assets.

## Build, Test, and Development Commands
- Serve locally (recommended):
  - `python3 -m http.server 8000` then open `http://localhost:8000/index.html`.
- Quick open (may hit browser file:// limits for media):
  - Open `index.html` directly in a browser.
- No build step is required; this is a static site. Keep vendored files under `dist/`, `js/`, and `plugin/` intact.

## Coding Style & Naming Conventions
- HTML/CSS: 2-space indentation; keep tags/attributes lowercase; group related sections with nested `<section>`.
- Custom CSS: Add overrides in `mystyle_2025.css` (avoid modifying `dist/` files).
- JS: Avoid editing `js/` unless bumping Reveal.js; initialize via `Reveal.initialize(...)` in `index.html` if needed.
- Assets: Use descriptive names with underscores; mirror existing patterns (e.g., `Contrasting_Sand_and_Snow_Pile.png`, `config_piece_19_nonsticky_w=50_seed=10.mp4`).
- Archive prior decks as separate HTML files (e.g., `index_2024.html`).

## Testing Guidelines
- Visual pass: Load `index.html`; verify slide navigation, themes, and no console errors.
- Media check: Confirm all `<video>` sources in `videos/` load and play; check images render and aspect ratios remain correct.
- Links/embeds: Verify external links use HTTPS and iframes load.
- Paths: Ensure relative paths remain valid after asset changes.

## Commit & Pull Request Guidelines
- Commit messages: Use a concise scope and imperative subject, e.g.,
  - `slides: add KPZ overview section`
  - `assets: add NSF logo and CLT images`
  - `styles: tweak .flex-container spacing`
- PRs: Include a short description, before/after screenshots or a brief screencast, and reference related issues if any.
- Media hygiene: Optimize images/videos where possible; keep large files out of diff churn and avoid renaming unless necessary.

