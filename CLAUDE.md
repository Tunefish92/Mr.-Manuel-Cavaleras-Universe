# Mr. Manuel Cavaleras Universe

Unofficial fan overview of the characters in the cartoons of the YouTube channel @manuelcavaleras. One static page (`index.html`), published by GitHub Pages from `main`. Site text is German.

## Rules

- `transkripte/` holds the full subtitles of all videos and is git-ignored. Never commit or publish it: the texts belong to the channel and this repo is public. Use it to look things up, and quote at most a short line with its time stamp on the page.
- `figuren/` has one still per character; `figuren/README.md` maps each file to character, video and time stamp. Keep that list in step with the files.
- `index.html` is the whole site: the data lives in the `V` (videos), `chars`, `mentioned` and `rels` constants in its script. Every file in `figuren/` must be the `img` of one entry in `chars`.
- Round portraits (parade and cards) load `figuren/thumb/`, the lightbox loads the full still. After adding or changing a still run `tools/thumbs.sh`; letting the browser shrink the full stills makes the thin lines look broken.
- The header must keep the "Inoffizielle Fan-Seite" badge and the link to the real channel.
- The look is a fixed dark space theme (star canvas `#sky`, planets, orbits). All motion must stay switched off under `prefers-reduced-motion`.
- Do not put a CSS `filter` on the map's `.edge` paths: straight lines have an empty bounding box and disappear.
- Mark every fact on the page as "belegt" (said or shown in a video, description or merch) or "vermutet". Names that only come from auto-generated captions count as "vermutet".

## Refreshing transcripts and stills

Scripts in `tools/` were run from a scratch folder that holds `vid/`, `dl/`, `subs_manual/`, `subs_auto/` and `out/`; they are not wired to the repo layout.

- yt-dlp: install into a venv (`python3 -m venv`, `pip install yt-dlp`), pass `--js-runtimes node`.
- Fetch creator-written subtitles (`--write-subs --sub-langs "de,de-AT,de-DE,en,en-US"`) and auto captions (`--write-auto-subs --sub-langs ".*-orig"`) in two separate runs. Asking for all languages hits translated tracks and YouTube answers 429.
- `tools/conv.py` turns the json3 tracks into Markdown, `tools/sheet.sh` builds a 20-frame contact sheet per video.
- `tools/crops.tsv` lists name, video id, contact-sheet time and crop box (fractions) per character. `tools/crop.sh` cuts from the very frame the contact sheet shows; seeking with `-ss` to the sheet's time stamp lands in a different scene.

## Checking the page

No test suite. Open `index.html` in headless Chromium (Playwright's cached `chrome-headless-shell` works with `playwright-core` and `executablePath`) and check: 82 cards, no broken image, no horizontal overflow at 390 px, lightbox opens, pages, zooms and closes, search narrows the cards, no console errors. Screenshots with `--force-prefers-reduced-motion` show the final state; `--virtual-time-budget` does not advance the CSS animations.
