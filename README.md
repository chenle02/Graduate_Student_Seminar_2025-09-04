# Auburn Graduate Student Seminar -- Math
# 
* Title: How Surfaces grow
* Abstract: In this talk, we will explore the fascinating world of surface
  growth phenomena, delving into the mathematical models that describe how
  surfaces evolve over time. We will discuss key concepts such as scaling laws,
  universality classes, and the role of stochastic processes in surface growth.
  The talk will also highlight recent advancements in the field and their
  applications in various scientific domains, including materials science and
  biology. Attendees will gain a deeper understanding of the mathematical
  frameworks used to analyze surface growth and the implications of these models
  in real-world scenarios.  


## Setup With uv

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

## Common Commands

- Serve slides: `uv run -s serve` then open `http://localhost:8000/index.html`.
- Render LIS animation (after scene is added): `uv run -s render_lis`.
- Manual serve alternative: `uv run python -m http.server 8000`.

## Notes

- See `AGENTS.md` for repository guidelines (structure, testing, media, and docs).
- Manim render outputs to `media/`; final videos should live under `videos/` and be referenced by slides using relative paths.
