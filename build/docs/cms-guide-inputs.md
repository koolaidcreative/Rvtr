# RVTR CMS guide: inputs

Source notes for the illustrated CMS guide for Kathy, Geoff and Sasha. Written 2026-10-14 from the live Framer project (main), after the Team, News, previous/next and redirect changes of that day. Screenshots of each collection's editor go in `build/docs/shots/` (file names are listed under each collection).

Plain words throughout: a **collection** is a table, an **item** is a row (one project, one post), a **field** is a column.

---

## 1. Everyday tasks

### Open the CMS
Framer → open the RVTR project → the **CMS** icon in the left toolbar (stacked rectangles). The collections are listed on the left. Click one to see its items as a table; click an item to open its editor.

### Edit an item
Open the item, change the field, close the panel. Changes are saved at once in the editor but are **not on rvtr.com until you Publish** (see 1.6).

### Add an item
In the collection, click **+ New** (top right). Fill in the fields, at least the title and the image. New items go to the top or bottom of the list; drag the row to where it should appear (see "Order" under each collection).

### Hide an item (without deleting it)
Open the item and tick **Draft** (top of the editor), or right-click the row → Set as Draft. A draft disappears from the site, its page and the sitemap, and comes back when Draft is unticked. Use this instead of deleting.

### Order
Most lists on the site show items **in the order of the rows in the CMS**. Drag rows to reorder. Exceptions are noted below (a few lists sort by a number field or by year).

### Publish
Top right of the editor: **Publish** → check the list of changes → **Update**. Then open rvtr.com in a private window to check. Nothing an editor does is visible to the public until this step.

### Images
Upload originals (about 2400–2900 px on the long side, JPEG, sRGB). Framer makes the smaller sizes itself. Always fill in the image's **alt text** (the small field under the image): a short factual description, which screen readers read out. Credit photographers in the item's credit field where there is one.

### Rich text fields
Fields marked *formatted text* below work like a small word processor: paragraphs, bold, italic, links, lists. Paste plain text (Cmd+Shift+V) to avoid bringing in fonts from Word or Google Docs.

---

## 2. Collections

Fields are listed in the order they appear in the editor. "Shown on" says where the field appears on the site. Fields marked *(not shown)* are kept for reference and appear nowhere.

### 2.1 Projects (62 items, 9 drafts) — shot: `shots/projects.png`

Feeds the **Projects** page (the main grid and the Archive list), every **project page** (/projects/…), and the six featured projects on **Home**.

| Field | Type | What it controls |
|---|---|---|
| Home Order | number | Which Home slot (1–6) the project fills. Works only together with Featured. |
| Featured | toggle | On = eligible for Home. A project shows on Home when Featured is on **and** Home Order is 1–6. |
| Title | text | Name on cards, the Projects grid and the project page title. |
| Cover Image | image | Card image (Home, Projects grid) and the large photo at the top of the project page. |
| Subtitle | text | Line under the title on the project page (client / programme). |
| Location | text | Projects grid card and project page. |
| Description | formatted text | Intro text at the top of the project page. |
| Status | text | Project page facts (e.g. Built, Competition). |
| Year | text | Cards and project page facts. |
| Research Threads | references | Links the project to Research Threads; shown as tags on the project page. |
| Scale | text | Project page facts ("Size"). |
| Image 1 | image | Photo beside the Overview. |
| Overview | formatted text | Project page section. |
| Image 2 | image | Photo beside Credits. |
| Credits | formatted text | Project page section. |
| Image 3 | image | Second photo in the Credits section. |
| Scope and Support | formatted text | Project page "Details" section. |
| Gallery 1–4 | image | Four fixed photo slots on the project page. |
| Gallery | list of images | The long photo sequence on the project page. Every photo opens the full-screen viewer (arrows, swipe, scroll). |
| Video URL | link | *(not shown)* |
| Archive | toggle | On = the project appears in the **Archive** list instead of the main grid. Previous/Next on a project page stay within its own group. |
| Photography | text | Photo credit on the project page (shown in the facts list). |
| Meta Description | text | *(not shown on the page; for search engines when used)* |
| Vimeo Link, Vimeo Link 2 | text | Film(s) on the project page. |
| Lists | formatted text | Extra lists section on the project page. |

**Order:** main grid and Archive list follow the CMS row order, each filtered by Archive. Keep all non-archive projects above the archive ones (re-grouped 2026-10-14) so that Previous/Next behave. Home uses Home Order instead.

### 2.2 News (25 items) — shot: `shots/news.png`

Geoff's news and blog. Feeds the **News** page, every **news post** (/news/…), the news cards on **Home** and "More news" under each post.

| Field | Type | What it controls |
|---|---|---|
| Order | number | Picks the Home news slots 1–3 (where that Home section is shown). |
| Title | text | Card and post title. |
| Cover Image | image | Card image and the large photo at the top of the post. |
| Category (not shown) | text | Cleared on 2026-10-14 and hidden everywhere (old values backed up). |
| Date | text | Shown on cards and the post. Type it as it should read, e.g. "October 2026". |
| Author, Author Avatar, Last Edited | text / image | *(hidden on the post)* |
| Teaser | text | Short line on the News page list and the post's summary. |
| Introduction | text | *(hidden on the post)* |
| Body | formatted text | The post itself. |
| Outbound Link | link | Optional "Read at …" link at the end of the post; hidden when empty. |
| Outbound Label | text | The words of that link, e.g. "Read at Taubman College". |
| Featured | toggle | *(not used at present)* |
| Tags | text | Optional, free text, for Geoff's own use. Not shown on the site. |
| Gallery | list of images | Optional photos shown under the post as a staggered grid (3 columns desktop, 2 tablet, 1 phone). Each photo opens the full-screen viewer. The grid hides when empty. |

**Order:** the News page and Previous/Next follow the CMS row order. Put the newest post at the top.

### 2.3 Publications (73 items) — shot: `shots/publications.png`

Feeds the **Publications** page (cover grid) and the publications shelf on **Home**. There are no individual publication pages; each card links out.

| Field | Type | What it controls |
|---|---|---|
| Title | text | Card title. |
| Venue | text | Publisher / journal line on the Publications page. |
| Type | option | Book, Book chapter, Journal article, Catalogue, Proceedings, Press. *(The visible label comes from Type Label.)* |
| Year | text | Shown on cards. The Home shelf shows the 6 most recent by Year. |
| Authors | text | *(not shown)* |
| Description | formatted text | *(not shown)* |
| Cover | image | The cover image (shown in a uniform 3:4 frame). |
| Images | list of images | *(not shown)* |
| Link | link | Where the card goes (publisher page, PDF). |
| Link Label | text | *(not shown)* |
| Related Projects | references | *(not shown)* |
| Order | number | Picks Home slots 1–3 (where that Home section is shown). |
| Featured | toggle | *(not used at present)* |
| Type Label | text | The type as written on the card ("Book", "Journal article"). |

**Order:** the Publications page follows the CMS row order; the Home shelf sorts by Year (newest first), 6 covers.

### 2.4 Recognition (57 items) — shot: `shots/recognition.png`

Feeds the **Recognition** page (list of awards, grants, exhibitions). No individual pages.

| Field | Type | What it controls |
|---|---|---|
| Title | text | Main line. |
| Kind | option | Category of recognition *(not shown as text)*. |
| Awarding Body | text | Second line. |
| Year | text | Year column. |
| Summary, Body | text / formatted text | *(not shown)* |
| Image | image | Small image in the row. |
| Link | link | Where the row links. |
| Related Project | reference | *(not shown)* |
| Has Page, Order, Featured | toggle / number | *(not used at present)* |

**Order:** CMS row order.

### 2.5 Team (82 items) — shot: `shots/team.png`

Directors, research associates and alumni. Feeds the **Team** page (directors' spreads, research associates, alumni names) and the director cards on **Home** (picked by Order 1–3).

| Field | Type | What it controls |
|---|---|---|
| Name | text | Name on the Team page (and Home). |
| Role | text | The line under a director's name; the role in the other lists. |
| Group | option | Director / Research Associate / Alumni: decides which part of the Team page the person appears in. |
| Years | text | Years in the lab (associates, alumni; Home). |
| Portrait | image | Director portrait on the Team page and Home. |
| Short Line | text | Used on Home. |
| Full Bio | formatted text | Directors: the text inside "Read full bio". |
| Appointments (not shown), Visiting (not shown), Leadership (not shown) | formatted text | Kept for reference; removed from the site at Kathy's request (2026-10-13). |
| Selected Honors | formatted text | Directors: the list at the end of "Read full bio", one honour per paragraph. The heading hides if empty. |
| Link | link | Directors: "Taubman College profile" link (hidden if empty). Alumni: the name links here. |
| Order | number | Picks Home slots 1–3. **Changing it changes Home.** |
| Alumni Line, Alumni Entry | text / formatted text | Alumni list entries. |
| Short Bio | text (multi-line) | Directors: the paragraph shown before "Read full bio". |
| Photo Lines | list of text | Directors: the short lines under the portrait (one row per line). |
| Photo Credit | text | Directors: optional small credit under the portrait, e.g. "Photograph by …". Hidden when empty. |
| Team Page Order | number | Order of the directors on the Team page (Geoff 1, Kathy 2). |

### 2.6 Team Hero (10 items) — shot: `shots/team-hero.png`

The moving strip of photos at the top of the **Team** page (added 2026-10-14).

| Field | Type | What it controls |
|---|---|---|
| Title | text | Name for your reference (the project). |
| Image | image | The photo. Fill in alt text. |
| Size | option | Tall / Medium tall / Medium / Short: the height of this photo in the strip. Mixing sizes keeps the staggered rhythm. |
| Order | number | Position in the strip (1 first). |
| Show | toggle | Off = left out of the strip. |

### 2.7 Home Hero (4 items) — shot: `shots/home-hero.png`

The large changing photos at the top of **Home**.

| Field | Type | What it controls |
|---|---|---|
| Image | image | The photo (use wide, high-resolution images). |
| Alt | text | *(reference; the image's own alt text is what's read out)* |
| Project | text | The project caption shown with the photo. |
| Order | number | Sequence (1 first). |
| Show | toggle | Off = left out. |

### 2.8 Research Threads (7 items, 1 draft) — shot: `shots/research-threads.png`

The research themes on the **Expertise** page; also tagged on project pages.

| Field | Type | What it controls |
|---|---|---|
| Order | number | Which of the 7 positions on the Expertise page the thread fills. |
| Ordinal Number | text | The number shown ("01"). |
| Name | text | Thread name (Expertise page, project page tags). |
| Image | image | Expertise page image. |
| Description | formatted text | Expertise page text. |

### 2.9 Research Team (3 items) — shot: `shots/research-team.png`

Current research associates and assistants, in the scrolling row on the **Team** page (currently hidden on the page).

| Field | Type | What it controls |
|---|---|---|
| Name, Program, Years, Photo | text / image | The card. |
| Role, Link, Link Label | text / link | *(not shown)* |
| Order | number | Order in the row. |
| Current | toggle | On = shown. |

### 2.10 Instagram (6 items) — shot: `shots/instagram.png`

The six photo tiles in the **footer** on every page.

| Field | Type | What it controls |
|---|---|---|
| Image | image | Tile photo. |
| Link | link | Where the tile goes (the Instagram post). |
| Order, Title | number / text | *(reference; tiles follow the CMS row order, first 6)* |

### 2.11 Legal (2 items) — shot: `shots/legal.png`

Legal pages (/legal/…): Page Title, Effective Date, Main Content, E-mail, Phone Number, each shown on the page.

---

## 3. Things that are not in the CMS

- Page text such as intros, section titles and the About text on Team: edited directly on the page in Framer (or with On-Page Editing on the live site).
- Redirects: Site Settings → Hosting → Redirects. Currently: /contact → /#contact, and /old → https://rvtr.netlify.app/ (the archived old site). Framer redirects are permanent.
- Navigation and footer: the Navigation and Footer components.

## 4. Notes for the guide writer

- Old `/publications/[slug]` page is a template leftover bound to News; not linked anywhere. Candidate for removal.
- Previous / View all / Next appears at the bottom of every project and news page (2026-10-14).
- Screenshots: take each collection's table view at about 1325 × 748, crop to the editor, save under `shots/` with the names above; one extra shot of an open item editor (Team → Kathy Velikov) as `shots/team-item.png`.
