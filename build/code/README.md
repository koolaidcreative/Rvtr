# RVTR custom code: builder's guide

Written 2026-10-11 for the Mac session that builds the RVTR site in Framer from the Archline template. Spec: `RVTR-site-plan.md` sections 5, 6 and 8. Base: the KLD custom code (`kld-framer-custom-code.html`), forked, with every `kld-` keyword renamed `rv-`, and with everything RVTR does not use taken out.

| File | What it is |
|---|---|
| `rvtr-framer-custom-code.html` | The site-wide custom code: CSS plus four small scripts (core, reveal, navigation, Instagram). About 70 KB, most of it comments. |
| `README.md` | This guide. |

There is no `RvLink.tsx`. The reason is in section 3.

---

## 0. Install

1. Set the four `SET` tokens at the top of the file first (section 1 of the CSS):
   - `--rv-paper`: Archline's page background.
   - `--rv-ink`: Archline's dark text colour.
   - `--rv-band-extra`: how far the band reaches below the desktop bar. Use `0px` if Archline's bar is already about 72–96px tall. Otherwise set it so that bar plus extra comes to about 96px.
   - `--rv-underline-offset`: nudges link underlines up or down. Leave it at `0px` unless they sit too low.

   Framer publishes colour styles as `--token-<id>` variables. Search the published HTML for the hex, then paste it with the hex as a fallback, e.g. `--rv-paper: var(--token-1a2b3c, #f5f5f2);`.
2. Framer → Site Settings → General → Custom Code → **End of `<head>` tag**, all pages, run **Once**. Every script also guards against running twice.
3. Custom code runs only on a preview or published site, never on the canvas. Install it on the "RVTR build" branch first (custom code belongs to a branch).
4. Keep this file as the source of truth. After installing, read the code back with `getCustomCode()` and compare.

What was **removed** from KLD:
- the loading curtain
- the carousel start delay and preloading
- the per-pixel brightness sampler and the split-page logic
- the photo tint
- the KLD typography overrides (`kld-display`, `kld-eyebrow`, `kld-prose` and the Besley baseline fix)
- `kld-stagger-grid`, `kld-drift`, `kld-header` and the progress bar
- `kld-card` and `kld-caption`
- `kld-cta`, now covered by the way `rv-link` reacts to any parent link
- the ProjectGallery `sizes` helper
- the Lenis hand-off
- the KLD JSON-LD

Add structured data for RVTR later from the research files if wanted.

---

## 1. Archline clean-up the code depends on (do these first)

1. **Smooth Scroll component:** if Archline ships one (Lenis, "Smooth Scroll"), hide it (`visible=false`). Native scrolling only. KLD found that Lenis makes Safari jerk, and that it makes Chrome drop `pushState`, which led to wrong addresses and 404s.
2. **Navigation component:**
   - Remove its Scroll Variant / appear effects.
   - Remove any border on the variant roots: the hairline is drawn by the code, and Framer draws borders with `::after`.
   - Remove Archline's hover effects on the nav links (rolling text, colour hovers, underlines).
   - Remove Archline's own active-link styling.
   - Nav links are plain text links (or a minimal link component with no hover variants).
3. **Appear effects on content:** the code reveals every text layer, button and framed photo automatically. Pick one:
   - **(a) Recommended:** remove Archline's Appear / Scroll Animation effects from content layers. One reveal for everything (plan section 6).
   - **(b)** Keep an Archline effect you like (e.g. a hero text tween), and add `rv-no-reveal` to that layer.

   Layers carrying Framer's optimised appear effect (`data-framer-appear-id`) are skipped automatically, but don't rely on that alone.
4. **Button component:**
   - Delete the filled and rounded variants.
   - Restyle the default to: no fill, no radius, no padding pill, label in the body text style.
   - Name its root or label layer `rv-link` (section 3).
   - The code forces `background: transparent` on `rv-link` layers as a safety net, but fix it natively too.
5. **Labels:** the copy file writes text links as "All projects →". In any layer tagged `rv-link`, **type the label without "→"**, because the arrow is drawn by the code. "← Previous" becomes "Previous" with `rv-link rv-back`.

---

## 2. Navigation (CSS section 4–5, script 2)

### Layer names

| Where | Name (keyword) | Notes |
|---|---|---|
| Navigation component, desktop variant | `… rv-bar` (e.g. "Desktop rv-bar") | The **variant name** is what Framer publishes on the root, so the keyword goes in the variant name. Renaming a variant keeps its id and interactions. |
| Phone and iPad closed variants | `… rv-closed` (e.g. "Phone rv-closed", "Tablet rv-closed") | Logo left, MENU right. |
| Phone and iPad open variants | `… rv-open` (e.g. "Phone Open rv-open") | The full-screen sheet in the page colour, with CLOSE in place of MENU. |
| The stack of page links (every variant) | `… rv-nav` | Holds the 7 links in order: Home, Projects, Publications, Recognition, News, Team, Contact. |
| The full-screen sheet frame (open variant) | `… rv-sheet` (optional) | Only if the sheet is a separate frame around `rv-nav`. If the `rv-nav` stack *is* the sheet (as on KLD), skip it. |
| MENU / CLOSE toggle | `… rv-menu` | Falls back to "the link without href" as on KLD. It gets a big invisible tap area. |
| Logo for the transparent bar | `… rv-logo-white` | Upload `rvtr/brand/rvtr-logo-white.svg`. |
| Logo for the band and light pages | `… rv-logo-colour` (or `rv-logo-color`) | Upload `rvtr/brand/rvtr-logo-colour.svg`. |
| The full-bleed photo at the top of a page, under the nav | `… rv-hero` | Home hero; project detail hero. This is what makes the nav white at the top of that page. |

#### Logo set-up

Put the two logo images in one logo link frame. The colour one stays in the layout flow; the white one sits absolutely on top of it, filling the frame. The code cross-fades them (0.45s).

- Give the colour image alt "RVTR" and the white one empty alt. Copy file: logo accessible name "RVTR".
- Upload the SVGs with `framer.uploadImage({ image: "data:image/svg+xml;base64,…" })` as image fills (`addSVG` fails from the agent; playbook 08).
- Strip the `<metadata>` C2PA block first: 19.4 KB → 11.7 KB each.

#### Sheet set-up (phones and iPads)

- Each link in the Open variants: **On Tap → Set Variant → the matching Closed variant**. Set this by hand: `DUPE` doesn't copy per-variant overrides.
- The Closed variants hold the same sheet at opacity 0.
- Give the Closed variant a tween transition, e.g. `tween 0.44,0.13,0.56,1 0.45s`, so CLOSE fades it out. The code fades it in.

### What it does

- **Over a hero, at the top:** white links, white MENU and the white logo (M stays maize). The faintest shadow on white text (`0 0 1px rgba(0,0,0,.25)`).
  - This is pure CSS (`html:has([data-framer-name~="rv-hero"])`), so it is right on the first paint.
  - Pages with no `rv-hero` start with dark ink.
- **Over the first 96px of scrolling:** a band in `--rv-paper` (92%, light blur) fades in behind the bar, tied to the scroll position.
  - At 48px the logo swaps to colour and every link turns to `--rv-ink`, over 0.45s. One tone for all links at any moment; no pixel reading.
  - The band's hairline draws itself in from the left (1.4s) and resets at the top.
- **Desktop hover:** the other links fade to 55%, and a hairline draws under the hovered one (in from the left, out to the right).
  - Gaps: `clamp(24px, (100vw - 1100px) / 7, 44px)`, which gives 24px at 1200, about 32px at 1325 and 44px from about 1410 up.
- **Current page:** a 5px maize dot, 7px left of the label (desktop), or at the right end of the row (sheet).
  - Detail pages light their section: `/projects/x` lights PROJECTS, `/news/x` lights NEWS, and so on.
  - Contact never lights.
- **Phone and iPad sheet:**
  - It fades in, and the rows arrive one after another (45ms apart) while their hairlines draw.
  - Tapping outside a link, or pressing Esc, closes it.
  - Tapping a link holds the sheet until the page change has taken its picture, so the menu cross-fades into the new page.
  - Contact fades the sheet and glides to the footer.
- **Contact:**
  - Link it in Framer to **Home → Scroll Section "contact"**, so it publishes as `/#contact`.
  - On Home the code glides there with native smooth scrolling. A long distance first jumps to ¾ of a screen short, then glides; the block lands 24px below the band.
  - On other pages Framer opens `/#contact`, and the code settles the block exactly in place once the page has loaded. Typed addresses and the old `/contact` → `/#contact` redirect get the same.
  - To glide to the current page's own footer from every page instead, set `CONTACT_MODE = "here"` in script 2. The footer is on every page, so this is a valid alternative; the plan chose `/#contact`.
- **Page changes:** everything re-runs on Framer's client-side page changes: route hooks, the view-transition hook and the observers. During a page change, colour changes are instant; the page cross-fade carries them.

### Do natively, not in code

- Logo left and MENU right on phone and iPad, both always on screen: plain layout in the variants.
- Opening and closing: the variants and On Tap.
- The sheet's fill, its padding, and the iPad column width.
- Nav type: Archline's nav text style.
- Navigation fixed at the top, in every page or the layout template.
- Semantic tag `nav` on the component root.
- `overscroll="contain"` on the sheet.

---

## 3. Text links (CSS section 3)

### Layer names

| Where | Name | Notes |
|---|---|---|
| A text link (link frame, Button component root, or the label text layer) | `… rv-link` | The label is Archline's **body text style**, auto width. |
| "Previous" style links | `… rv-link rv-back` | Arrow before the label, pointing left, slides left. |
| Optional drawn arrow inside an rv-link | `… rv-arrow` | Only if you'd rather place a native SVG layer. The code arrow then steps aside and this layer slides 4px. |

### What it does

- A thin arrow is drawn after the label: an inline SVG used as a CSS mask, in the text's own colour, 0.9em × 0.65em, 1px stroke.
  - On hover the arrow slides 4px right, and a hairline underline draws under the words (not the arrow) from the left. Both take 0.35s, ease-out.
  - On un-hover the line leaves to the right.
  - Hovering anywhere on a link frame that *contains* an `rv-link` (a card with "View project" inside) animates it too.
- Keyboard focus draws the underline.
- An `rv-link` whose CMS link is empty is plain text: no hand cursor, no line.
- The arrow turns maize on hover (plan section 3: maize as the single accent). To keep it in the text colour, set `--rv-link-arrow-hover: currentColor`.
- No fill, no pill, no radius, ever (forced).
- No layout shift: the arrow is in the CSS from the first paint, and hover changes only `translate` and `scale`.

The SVG, should you want it as a native layer (`rv-arrow`):

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 10" width="14" height="10"><path d="M0 5h12.6M8.6 1l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1"/></svg>
```

### Why no RvLink.tsx code component

A styled native link is clearly better here.

- Framer's own links keep client-side page changes and the Archline page transitions. A code component's `<a>` would reload the page.
- Native links bind to CMS link fields and page links in the panel.
- Native links use Archline's text styles (code components can't use text styles).
- Native links are editable by Kathy and Geoff.
- Native links render in the server HTML for SEO.

The arrow is drawn by CSS rather than inserted into the page, because inserting an element into Framer's markup before React hydrates it causes a hydration mismatch.

### Rows, pager, photos (same section)

| Where | Name | What |
|---|---|---|
| A list row (Recognition, News, Team alumni), a link frame ending in its own 1px line layer | `… rv-row` | A darker line draws along the hairline on hover. Rows without a link stay still. Use a line layer, not a border. |
| The Previous / All projects / Next row | `… rv-pager` | Bigger invisible tap areas (labels are small). Put `rv-link` / `rv-back` on the links inside. |
| A photo or the link frame holding it (project tiles, publication covers, Instagram tiles) | `… rv-zoom` | KLD's photo hover: a slow 2% push-in (spring in, 0.6s out) under a pale veil. No border on that layer, and no Framer Hover effect on it. |

**Do natively instead:** inside a component (e.g. Archline's project card) a hover *variant* returns on the component's own transition. If Archline's card is a component, you can do the 2% push-in there natively (scale 1.02, `spring-duration 1s 0 0s` in, `tween 0.31,0,0.35,1 0.6s` out) and skip `rv-zoom`. On page-level layers use `rv-zoom`, because Framer's Hover effect returns on a quick default spring there.

---

## 4. Reveal (CSS section 7, script 1)

KLD did this in code, so RVTR keeps it in code. The native Appear / Scroll Animation can't do these four things:

- wait for a photo to finish loading
- apply to every text layer without tagging each
- wait for Framer's view-transition page changes (Safari restarts animations under them)
- draw lines only once the page has nearly stopped

**The motion:** fade while rising 24px over 0.6s, curve `0.44, 0.13, 0.56, 1`, once.

| Want | Name | Notes |
|---|---|---|
| Every text layer, button, framed photo | (automatic) | Nav and footer text excluded. Set `AUTO = false` in script 1 to make it tag-only. |
| A card (photo + caption) as one piece | `rv-reveal` | Waits up to 1.8s for its photos. |
| Top-of-page content (hero title, page intro) | `rv-intro`, plus `rv-d1`…`rv-d5` for 90ms steps | Reveals straight away. Tagged blocks inside `rv-hero` still reveal. |
| A list or grid rising item by item | `rv-stagger` on the stack or CMS list | 90ms steps, max 450ms. Works through Framer's `display: contents` wrappers. |
| A hairline drawing itself | `rv-rule` on the 1px line layer; `rv-slow` for a long full-width one (1.4s) | Draws when well inside the window and the page has nearly stopped. |
| Leave something still | `rv-no-reveal` | Also for any layer that keeps an Archline effect. |
| Footer | `rv-footer` on the footer root, or the `footer` tag on it | Its own text stays still; tagged blocks in it (the Instagram tiles) still reveal. Its lines redraw on each page. |

Photos wait on a quiet placeholder (5% ink on paper) until downloaded and decoded, then fade in. A full-width photo at the very top of a page only fades, without rising.

The `rv-hero` photo opens on a ~1 KB blurred copy, from Framer's CDN `?scale-down-to=64`, and comes into focus over it.

**Do natively:** the home hero's soft fade as you scroll away (plan section 4.1, "like KLD"). On the hero frame:

- Scroll Animation → Layer in View
- threshold 0.5, replay on
- opacity 0 → 1, `tween 0.44,0.13,0.56,1 0.8s`

Then add `rv-no-reveal` to the hero frame, or leave it, since `rv-hero` is already skipped by the automatic reveal.

Archline's page transitions stay native (Page Effect).

---

## 5. Footer: Instagram and Vimeo (script 3, plan section 8)

### Instagram

| Where | Name / setting |
|---|---|
| The tile grid (a CMS list of the **Instagram** collection: Image, Link) | `… rv-insta rv-stagger` |
| Each tile | A link frame bound to the Link field, image fill bound to Image, aspect ratio 1:1, `rv-zoom` |
| Layout | **Native:** Framer Grid with 6 columns on desktop and iPad, 3 columns on phones (3 × 2), gap from Archline. Limit the list to 6 items. |
| New tab | Set "open in new tab" natively. The script also forces `target=_blank rel=noopener` on every tile, fallback tiles included. |

**How the feed works:**
- Once `INSTAGRAM_FEED` (top of script 3) holds the Behold JSON feed URL, the visible tiles show the six newest posts, newest first. Each links to its post.
- Alt text comes from the caption's first line (hashtags removed, up to 140 characters), then Behold's alt text, then "Instagram post by RVTR".
- **Caching:** the post list is kept for one hour in `localStorage["rv-instagram"]`, inside a try/catch. A stale copy shows at once while a fresh one loads.
- **Failures:** a failed fetch is remembered for an hour (`rv-instagram-fail`), so a locked or paused feed isn't hammered. On any failure the CMS tiles stay.
- **Domain lock:** Behold feeds can be locked to domains. KLD's answered **403 on `*.framer.app`**, so branch previews show the fallback tiles.
  - The script fetches only on `FEED_HOSTS` (default `rvtr.com`, `www.rvtr.com`), so previews make no request and leave no 403 in the console.
  - If Behold's domain list includes the framer.app address, add it to `FEED_HOSTS` too.
- **Login:** Sasha connects @rvtrarchitecture in Behold (Business or Creator account; login is Sasha's alone) and sends the feed URL. Until then the six CMS tiles (strong project photos) are the live tiles.
- **Testing without a feed:** set `window.RV_INSTAGRAM_FEED = "https://feeds.behold.so/MOCK"` from an injected script (it beats the constant and the host list), and stub `fetch`.

### Vimeo

- **Footer:** the "Films on Vimeo" text link (`rv-link`) with the Vimeo icon, slightly larger than the Instagram icon, linking to `https://vimeo.com/rvtr`. No feed.
- **Project pages:** embed with these player parameters:

```
https://player.vimeo.com/video/<ID>?color=ffffff&badge=0&byline=0&title=0&portrait=0
```

**Natively:** use Framer's Vimeo component bound to the CMS "Video 1 URL" field if its player honours these options. Otherwise use an **Embed** (URL mode) bound to the same field, with the import script writing the full player URL above. In HTML mode:

```html
<iframe src="https://player.vimeo.com/video/<ID>?color=ffffff&badge=0&byline=0&title=0&portrait=0" loading="lazy" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;inset:0;width:100%;height:100%;border:0" title="<Project title>, film"></iframe>
```

- Use a 16:9 frame (aspect ratio on the frame). Hide it with `isSet` when the field is empty.
- Optional extra parameter: `dnt=1` (no Vimeo tracking cookies).
- **Poster:** Vimeo shows its own thumbnail. To make the project cover the poster without code, set that video's thumbnail to the cover in Vimeo (video settings → Thumbnail → upload). A click-to-load facade is possible in code later, but not recommended for Tuesday.

---

## 6. Native settings that replace code (summary)

| Need | Native Framer |
|---|---|
| Menu open and close | Navigation variants + On Tap → Set Variant |
| Instagram grid 6 / 3 × 2 | Grid columns per breakpoint, 1:1 tiles, limit 6 |
| Contact target | Scroll Section "contact" on the footer contact block; nav link → Home + section |
| Hero fade on scroll | Scroll Animation, Layer in View, replay, 0.8s tween |
| Card hover inside a component | Hover variant with the component transition (instead of `rv-zoom`) |
| Page transitions | Archline's Page Effect |
| Video | Vimeo component or Embed with the parameters above |
| Reduced motion | Site setting "Reduced Motion" on, as well as the code's own handling |
| Show a row only if a field is set | Conditional visibility (`isSet`) |

---

## 7. Switches (turn things off in seconds)

| What | Where |
|---|---|
| Automatic reveal of every text and photo | `AUTO` in script 1 (`false` = tagged layers only) |
| Contact behaviour | `CONTACT_MODE` in script 2 (`"home"` or `"here"`) |
| Band and tone timing | `BAND_AT` (48) and `BAND_RANGE` (96) in script 2. If you change `BAND_RANGE`, also change `animation-range: 0px 96px` in CSS section 4. |
| Instagram feed | `INSTAGRAM_FEED`, `FEED_HOSTS` in script 3 (empty feed = no request) |
| Maize arrow on hover | `--rv-link-arrow-hover` in `:root` |
| Debug | `window.RV_DEBUG = true` logs any error inside an event hook as a warning |

---

## 8. Test checklist

Test on the branch preview, then live after publishing and warming. Use the playbook's WebKit harness (`framer-playbook/tools/webkit-harness`) for Safari, and headless Chrome. Judge motion from real frames, not screenshots.

**Sizes:**
- 1325 × 748 (Safari and Chrome)
- 1440 × 900
- iPad 820 × 1180 (watch the 13px scrollbar tipping 820 into phone in the harness)
- phone 390 × 844, and 360 wide

### Nav
- [ ] Home at the top: logo white (M maize), links white with the faintest edge, maize dot on HOME.
- [ ] Team, Publications (no hero): dark from the first frame, with no white flash.
- [ ] Scroll 0 → 120px slowly: the band fades in over 96px, the tone flips at 48px (0.45s), and the hairline draws once.
- [ ] Scroll back to the top: everything reverses, and the hairline resets.
- [ ] Safari trackpad flick: the band stays in step and nothing jerks.
- [ ] Hover each link: the others go to 55%, the hairline draws in and leaves to the right. No pill, no colour change.
- [ ] Dot on the right link on every page, including a project page (PROJECTS) and a news post (NEWS). Never on Contact.
- [ ] Gaps at 1200, 1325, 1440: even, no wrapping, the bar never overlaps the logo.

### Phone and iPad
- [ ] MENU opens: the sheet fades in, the rows arrive one by one, the lines draw, CLOSE replaces MENU.
- [ ] Tap empty sheet → closes. Esc → closes. MENU takes one tap (big target).
- [ ] Tap Projects: the menu cross-fades into the new page, and the new page's nav is right (dark or white).
- [ ] Tap Contact: the sheet fades and the page glides to the contact block.
- [ ] Sideways phone (short screen): the sheet scrolls if needed.

### Contact
- [ ] On Home: glides; the "Contact" heading sits just below the band.
- [ ] From Team: opens Home at the contact block, settled exactly.
- [ ] `/#contact` typed in fresh, and old `/contact` (redirect): lands correctly after load.

### Links
- [ ] Every "→" link: one arrow only (no typed "→" left), arrow slides 4px and turns maize, underline under the words only.
- [ ] "Previous": arrow on the left, slides left.
- [ ] Measure the link box before and during hover: no layout shift.

### Reveal
- [ ] Text, tiles and photos rise 24px over 0.6s once. Photos never paint line by line.
- [ ] Lists stagger. Lines draw after the page settles.
- [ ] Footer lines redraw on each page.

### Client-side page changes
Click between pages; don't reload.
- [ ] Reveals, dot, tone, band and Instagram tiles all correct after each change.
- [ ] Back and Forward also work.
- [ ] The address bar always matches the page shown. Use the playbook's `navfuzz.mjs` for random clicks, Back and wheel.

### Instagram
- [ ] Preview (framer.app): the CMS tiles show, and no feed request is made unless the host is in `FEED_HOSTS`.
- [ ] Live with the feed: six newest posts, newest first, open in a new tab, alt from the caption.
- [ ] 6 in a row on desktop, 3 × 2 on phone.

### Reduced motion
macOS: System Settings → Accessibility → Display → Reduce motion; or emulate it in Chrome DevTools.
- [ ] Nothing rises, slides, draws or zooms. Content is visible immediately.
- [ ] Contact jumps instead of gliding.
- [ ] The underline simply appears on hover.

### Console
- [ ] No errors or warnings in Safari and Chrome on every page. The one exception: with `FEED_HOSTS` emptied on a locked feed, Chrome logs the 403 network line.

What was already checked here (headless Chromium 1325 × 748 and 390 × 844, against a mock page shaped like Framer's markup, 2026-10-11):
- nav tone at the top, on the band and on a page without a hero
- band, dot, hover dimming
- the `rv-link` arrow, hover and `rv-back`, with no layout shift
- reveal, including after a client-side page change with a view transition
- Contact glide on Home, from the sheet and on arrival with `#contact`
- Instagram feed: mocked feed, a 403, and caching
- phone sheet: open, tap outside, Esc
- reduced motion
- zero console errors

**Not yet checked:** Safari/WebKit (not available in the cloud), and Archline's real markup.

---

## 9. Decisions for the builder on the Archline side

1. **Colours:** Archline's background and ink colour styles → `--rv-paper` and `--rv-ink`. Also check whether the band height needs `--rv-band-extra`.
2. **Navigation structure:** rename the variants with `rv-bar` / `rv-closed` / `rv-open`. Decide whether the sheet is the `rv-nav` stack itself (KLD) or a separate `rv-sheet` frame. Make sure every open-variant link closes the menu (On Tap → Set Variant).
3. **Archline's content effects:** remove them (recommended), or keep chosen ones with `rv-no-reveal`. Also hide any Smooth Scroll component.
4. **Button component:** restyle it to the text link and tag it `rv-link`. Remove "→" from the typed labels.
5. **Project cards:** a native hover variant inside the card component, or `rv-zoom` on the page-level frame. Not both.
6. **Hero tagging:** tag only photos that sit under the nav at the top of the page as `rv-hero` (Home, project detail). A pale hero needs a shade layer (a top gradient) for the white nav. Don't lighten the photo.
7. **Contact behaviour:** `/#contact` to Home (plan, default) or this page's footer (`CONTACT_MODE = "here"`).
8. **Maize arrow on hover:** on (plan section 3) or text colour.
9. **Vimeo:** Framer's Vimeo component if it honours the parameters, else Embed. Poster via Vimeo's thumbnail setting.
10. **Instagram:** `FEED_HOSTS` must match Behold's domain list once the feed exists.
