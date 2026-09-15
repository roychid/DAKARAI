# Dakarai Albert Mapuranga — Personal Executive Website (Flask)

Built from the ClientFlow Digital developer brief (Sept 2026), on your org's
Flask + Jinja2 stack.

## Status

All 9 routes are built and smoke-tested (200 on every page, no broken image
references): `/`, `/about`, `/leadership`, `/bhc`, `/agriculture`, `/vision`,
`/work`, `/media`, `/contact`.

Design system is what was already in `static/css/style.css` when you handed
this over — dark background, gold accent, Inter + Playfair Display — extended
with section/card/timeline/gallery classes the new pages needed, same token
names throughout.

## Deploy to Vercel

This project is set up for zero-config Vercel deployment (`app.py` at the
root is a supported entrypoint, `public/static/` mirrors `static/` for
Vercel's CDN — Flask's own static serving isn't used on Vercel).

**Fastest path (no GitHub needed):**

```bash
npm i -g vercel
cd dakarai-website
vercel
```

Follow the prompts (link or create a project, accept defaults) — it'll give
you a live `*.vercel.app` URL to send the client in under a minute. Run
`vercel --prod` once you're happy with a preview, to get a stable production
URL.

**Or via GitHub:** push this folder to a repo, then import it at
vercel.com/new — same zero-config detection applies.

Note: `requirements.txt` was UTF-16-encoded when handed over (a Windows
PowerShell artifact from `pip freeze >`) — that would have failed silently
or errored on Vercel's Linux build. Re-saved as plain UTF-8 with the same
pinned versions; verified with a clean `pip install`.

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

(The venv you uploaded was Windows-only, doesn't run in this environment —
excluded from this zip. Recreate it locally as above.)

## What's real vs. placeholder

- **Portraits** (`static/images/portraits/`): studio headshot (hero), a
  summit/conference photo, a farm visit shot — all real, from the asset drop.
- **Agriculture** (`static/images/agriculture/`): 7 real photos — tobacco
  fields, irrigation pivot, wheat/barley, livestock, field vehicle.
- **BHC / construction** (`static/images/bhc/`): **empty.** Nothing in Neo's
  asset drop showed a construction site, building, or BHC branding. The BHC
  page is text-only until those come through — flag this to Neo.
- **`/work`**: single placeholder card — no confirmed project list yet.
- Original unsorted assets (including 3 videos, plus a few beach/restaurant
  selfies I didn't use) are kept in `/assets` for reference — not linked from
  any page.

## Where content lives

Copy is written directly into each template (this stack doesn't have a
central content file like a JS `content.ts` would) — anything not in the
brief's confirmed table is marked with a `.note` block citing the brief
section, e.g. career dates, education, farm specifics, BHC website/LinkedIn
links.

## Before publish (brief sections 9/10)

- [ ] Replace every "pending confirmation" note once the client confirms.
- [ ] Get BHC/construction photography from Neo — `bhc.html` needs it.
- [ ] Get the confirmed project list for `/work`.
- [ ] Add a real `favicon.ico` to `static/` (referenced in `base.html`, not
      yet present).
- [ ] Build the digital business card (brief section 6) — separate piece,
      not started yet.
- [ ] Test tel/mailto/WhatsApp links on iOS and Android.
