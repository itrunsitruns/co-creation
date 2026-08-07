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
- Origin (2026-08-07 更正，依實物洗標): ponchos "Made in Bali・峇里島製造" · LIC "Made in India・印度製造"
  · 其餘全部 "Made in China・中國製造"。**不要再寫以色列製造** — 以色列是品牌與設計地，不是產地。
- Materials (2026-08-07 更正，依實物洗標): CS53–74 是 100% Polyester（原誤植純棉）· CS51 是 100% Cotton
  （原誤植聚酯）· CS10 是 50% Viscose 50% Cotton · PON 是 100% Rayon（原寫「針織 Knit」，那是織法不是纖維）。
  舊資料源自以色列官網與 Excel，與實物不符；洗標為準。
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

## 蝦皮連結 / 已售完（build_site.py 內）
- `SHOPEE = {SKU: 網址}`。一個賣場賣好幾色的，就好幾個 SKU 指到同一個網址
  （目前 CS45 三色、CS47 三色、CS48 四色各共用一個賣場）。沒登記的 SKU 按鈕維持 `href="#"`。
- `SOLD = {SKU, ...}`：卡片保留、照片還在，但主圖左上加「已售完 Sold Out」角標、圖片轉灰，
  購買按鈕換成不可點的 `<span class="soldout">`。售完優先於連結（CS48--41 有賣場但已售完）。
- 售完樣式的 CSS 住在 `index.html` 的 `<style>`（`.soldout` / `.sold-badge` / `.card.sold`），
  build_site.py 會原封不動保留 head，所以改樣式要直接改 index.html。

## Pending
- 還沒有蝦皮連結的 32 款：CS10、CS51、CS52、CS53、CS54、CS57～CS74、LIC 全系列。
- LIC19--00--O-S (pink/magenta large scarf): currently a crop of the website screenshot.

## Note
Full-resolution photo originals were organised by SKU in `/home/user/official_photos/by_sku/`
during the build session (ephemeral container — NOT in git). The committed `assets/` are ~1000px,
which are fine for web and for Shopify import.
