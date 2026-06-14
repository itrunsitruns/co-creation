# Signa Taiwan × Dreadlocks — Storefront build notes (handoff)

Live: https://itrunsitruns.github.io/co-creation/dreadlocks/
Repo path: itrunsitruns/co-creation → /dreadlocks/
Parent hub card: co-creation/index.html ＋ syntax-field-archive homepage "Co-Creation Series".

## Files
- `index.html`  ← GENERATED. Do not hand-edit large parts; regenerate with build_site.py.
- `assets/`     ← product photos. Naming: SKU "CS46--23--00" → key "CS46_23_00" →
                  `CS46_23_00__1.jpg`, `__2.jpg`, ... (multiple angles, right-side thumbnail rail).
                  Poncho cards also append `PON__ring.jpg` (all-colour ring) automatically.
- `build_site.py` ← regenerates index.html from the data table + whatever images exist in assets/.
- `_BUILD_NOTES.md` ← this file.

## How the gallery works
For each SKU, build_site.py globs `assets/<key>__*.jpg` (sorted). First = main image;
the rest show as a clickable right-side thumbnail rail; clicking main = full-screen lightbox.
Ponchos get the colour-ring appended as the last thumbnail.

## Product data (inside build_site.py)
- ROWS = list of (SKU, colour, material, size) — 56 in-stock colours.
- Prices: scarf NT$1,400 · cotton-large(LIC) NT$1,680 · crinkled(CS10) NT$1,820 · poncho(PON) NT$2,380.
- Origin: scarves "Made in Israel・以色列製造" · ponchos "Made in Bali・峇里島製造".
- Bilingual throughout (中文 first on cards' names; English-first on origin line).
- Font: Noto Sans TC site-wide, light weight (300/400). Logo title-case "Dreadlocks / Signa Taiwan".

## To replace / add photos
1. Put `assets/<key>__N.jpg` (max ~1000px) into assets/.
2. `python3 build_site.py`
3. commit → merge to `main` (GitHub Pages serves main).

## To add a NEW product
1. Add a row to ROWS in build_site.py (SKU, colour, material, size).
2. Add it to the right SECTION's family list; add FAM[]/COLOR[] entries if it's a new family/colour.
3. Add its photos to assets/ (naming as above).
4. Rebuild + deploy.

## Deploy
Develop on a `claude/...` branch, then:
`git merge --no-ff <branch> -m "..."` into `main`, `git push origin main`.

## Pending
- PON--103--O-S (Gold poncho): still a placeholder crop — needs a real photo.
- LIC19--00--O-S (pink/magenta large scarf): currently a crop of the website screenshot.

## Note
Full-resolution photo originals were organised by SKU in `/home/user/official_photos/by_sku/`
during the build session (ephemeral container — NOT in git). The committed `assets/` are ~1000px,
which are fine for web and for Shopify import.
