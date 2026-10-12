## Public-source verification and fix list

Added 2026-10-12. Every item flagged above as "not on rvtr.com" was checked against public sources.

**Sources used**
- Crossref and OpenAlex records for the DOIs.
- Publisher pages and library catalogues: the CCA library, WUR and MnLINK.
- The Canada Council and canada.ca releases.
- The NSF award record.
- Taubman College news pages.
- Kathy Velikov's public CV (Taubman College, February 2023): https://taubmancollege.umich.edu/wp-content/uploads/2023/02/CV-Kathy-Velikov.pdf. This is cited below as "CV".

**Limits.** The Crossref API rate-limited this session (HTTP 429) after five records, so the remaining DOIs were checked through OpenAlex or the CV instead. That includes the Interiors DOI, 10.2752/204191212x13232577462538. No item was left unchecked because of this.

**Verdicts.**
- CONFIRMED: a public source states the fact.
- CORRECT-TO: a public source states something different, and the exact replacement text is given.
- REMOVE: no public source was found.

### A. Verification results

#### Recognition and project claims

| Item | Claim | Verdict | Source |
|---|---|---|---|
| recognition / 2009-professional-prix-de-rome-in-architecture | "$50,000"; "Colin Ripley, Kathy Velikov, Geoffrey Thün and Paul Raff"; "research on responsive northern housing" | CONFIRMED: "valued at $50,000"; "directors Colin Ripley, Kathy Velikov, Geoffrey Thün, and Paul Raff"; "extend their design research on responsive northern housing" | https://www.canada.ca/en/news/archive/2009/06/toronto-architectural-firm-rvtr-wins-canada-council-arts-professional-prix-rome.html |
| recognition / 2024-nsf-grant | "NSF Engines development award to the Purdue-led NextHouse initiative, with the University of Michigan as a partner" | CONFIRMED. NSF Engines Development Award 2315483, lead Purdue Applied Research Institute, University of Michigan listed as a partner, start 03/01/2024. | https://nsf.elsevierpure.com/en/projects/nsf-engines-development-award-developing-innovative-solutions-for-2/ ; https://www.purdue.edu/research/features/stories/nexthouse-creating-the-next-generation-of-factory-built-housing/ |
| recognition / 2024-nsf-grant | Awarding Body "Regional Innovation Engines program" (the card says "Regional Economic Engines") | CONFIRMED. Velikov is named on the proposal. | https://taubmancollege.umich.edu/news/2023/06/21/next-generation-factory-built-housing-proposal-named-nsf-regional-innovation-engines-program-semifinalist |
| projects / extraction | "15th" Venice Architecture Biennale; "comprised an installation, a film and a book" | CONFIRMED: "15th International Architecture Exhibition"; installation, film and book; RVTR (Thün, Velikov, Ripley) are collaborators | https://canadacouncil.ca/press/2015/12/extraction-wins-national-competition |
| projects / jack-layton-ferry-terminal-toronto | Year 2014–2015 | CORRECT-TO **2015**. The CV gives "2015, short-listed finalist… finalist schemes exhibited at Toronto City Hall, March 15–21, 2015". | CV |
| recognition / 2008-us-department-of-energy-… and projects / north-house (Meta Description) | "Team North's entry to the 2009 Solar Decathlon" | CONFIRMED. The CV lists the book "NORTH HOUSE: Team North entry to the 2009 Solar Decathlon" (2008). | CV |
| recognition / 2017-csla-award and projects / extraction (Overview) | CSLA "National" Award of Excellence | CONFIRMED: "National Award of Excellence, Design Communication, Risk and Resilience" | CV |
| recognition / 2008-young-architects-forum-award | "(Kathy Velikov and Geoffrey Thün)" | CONFIRMED: "Award to K. Velikov & G. Thün (RVTR)" | CV |
| recognition / 2011-innovation-in-architecture-award | "…for the North House responsive envelope system" (flagged as CHANGED above) | CONFIRMED. The CV entry is "North House Responsive Envelope System" (RVTR / Team North). **This reverses the earlier verdict.** | CV |
| recognition / 2018-wanxiang-sponsored-project | "…competition in Hangzhou" | CONFIRMED: "InnovaCity at Hangzhou" | CV |
| recognition / 2007-9th-annual-arquine-urban-design-competition | Linked to the Infographic Center project | Not confirmed. The CV gives only "Plaza de las tres Culturas: Bridging Strata (Third Place)". See the fix list. | CV |
| recognition / 2014-ford-urp-grant | Awarding Body "Ford Motor Company, University Research Program" | REMOVE the expansion. The CV has no 2014 Ford URP entry and expands URP differently, as "University Research Alliance Program". | card; CV |
| recognition / 2023-acadia-society-award-for-leadership | President 2018–2020, Vice President 2021–2022, jury quote | CONFIRMED | https://taubmancollege.umich.edu/news/2023/08/03/kathy-velikov-recognized-with-acadia-society-award-for-leadership |
| same | "created the ACADIA Diversity Committee" | REMOVE. No mention on the Taubman, ACADIA (awards and recipients) or Portico pages, or in the CV. | — |
| same | "updated the organization's publication ethics" | CORRECT-TO "developed codes of ethics and conduct" | https://taubmancollege.umich.edu/news/2020/11/17/portico-fall-2020-velikovs-experimental-practice-and-innovative-presidency/ |
| same | "during her tenure the Board became substantially more diverse" | REMOVE (no public source) | — |
| same | Award talk "Cultivating a Community of Practice", 26 October 2023 | No public source found. Keep only if Kathy confirms. | — |
| recognition / 2025-velikov-faia | "Fewer than 3%", the AIA Object wording, AIA25 Boston 4–6 June, Velikov quote | CONFIRMED | https://taubmancollege.umich.edu/news/2025/02/13/velikov-elevated-to-aias-prestigious-college-of-fellows/ |
| same | "She was nominated through the AIA Michigan chapter" | CORRECT-TO "She was one of four AIA Michigan members elevated in 2025". The release mentions no nomination route. | same |
| news / ambiguous-territory-book-2022 (outside the three audited collections) | "launched at Rizzoli Bookstore in New York in January 2023" | Launch at Rizzoli CONFIRMED. "January 2023" not found; Actar gives the book's publication date as January 2022. | https://www.pneumastudio.org/ ; https://actar.com/product/ambiguous-territory/ |
| same | "Its print run of 1,500 copies sold out." | "1,500 copies": REMOVE (no source). "Sold out": supported by rvtr.com ("Print Copy SOLD OUT!"). | rvtr.com/writing-publications/ambiguous-territory |

#### Publication authors (15 flagged, plus TAD 2:2)

| Slug | New Authors | Verdict | Source |
|---|---|---|---|
| jae-vol-78-issue-2 | Kathy Velikov, Geoffrey Thün, Eilis Finnegan | CORRECT-TO **Kathy Velikov, Eilís Finnegan, Geoffrey Thün**. Finnegan is a genuine co-author; the order and accent are fixed. JAE 78(2), 618–627, published 2024-07-02, DOI 10.1080/10464883.2024.2382039. | https://api.openalex.org/works/doi:10.1080/10464883.2024.2382039 |
| fabricate | Kathy Velikov, Wes McGee, Daniel Tish, Geoffrey Thün | CORRECT-TO **Wes McGee, Kathy Velikov, Geoffrey Thün, Daniel Tish**. The paper is "Infundibuliforms: Kinetic systems, additive manufacturing for cable nets, and tensile surface control", UCL Press, pp. 84–91. | CV; https://taubmancollege.umich.edu/news/2017/04/11/thun-velikov-mcgee-and-tish-present-infundibuliforms-at-the-2017-fabricate-conference |
| towards-a-robotic-architecture | Wes McGee, Kathy Velikov, Geoffrey Thün | CORRECT-TO **Wes McGee, Kathy Velikov, Geoffrey Thün, Daniel Tish** ("Prologue for a robotic architecture") | https://www.cca.qc.ca/en/search/details/library/publication/992570355 |
| next-new-york | Kathy Velikov, Geoffrey Thün | CONFIRMED ("Infrastructural Hybrids") | https://appliedresearchanddesign.com/product/next-new-york ; CV |
| the-routledge-companion-to-ecological-design-thinking | Kathy Velikov, Geoffrey Thün | CONFIRMED (chapter 3.5, "Environment-Aware Behavioral Envelopes…") | https://www.routledge.com/The-Routledge-Companion-to-Ecological-Design-Thinking-Healthful-Ecotopian/Kanaani/p/book/9781032023892 |
| architect-s-newspaper-the-texas-issue | Geoffrey Thün, Kathy Velikov | CONFIRMED ("Concrete Politics…", AN July/August 2018). The web article itself carries no byline and credits only Velikov's photographs. | CV |
| third-coast-atlas | Kathy Velikov, Geoffrey Thün | CONFIRMED ("Shed Cartographies", ActarD 2017) | CV |
| paradigms-in-computing | Kathy Velikov, Geoffrey Thün | CONFIRMED ("Towards an architecture of cyber-physical systems") | https://www.cca.qc.ca/en/search/details/library/publication/899946176 |
| a22-new-ecologies-for-osmotic-infra-structures | Kathy Velikov, Geoffrey Thün | CONFIRMED. The source order is Thün, Velikov. | CV |
| bracket-goes-soft-almanac-2 | Kathy Velikov, Geoffrey Thün, Colin Ripley | CONFIRMED. The source order is **Colin Ripley, Kathy Velikov, Geoffrey Thün** ("Soft Goes Hard", pp. 34–48). | CV |
| volume-32-centers-adrift | Kathy Velikov, Geoffrey Thün | CORRECT-TO **Geoffrey Thün, Kathy Velikov, Colin Ripley** ("Re-Centering the Periphery"). Ripley was missing. | CV |
| monu-15 | Kathy Velikov, Geoffrey Thün | CORRECT-TO **Geoffrey Thün, Kathy Velikov, Colin Ripley**. Ripley was missing. | https://taubmancollege.umich.edu/news/2011/12/07/architecture-assistant-professor-velikov-and-associate-professor-thun-publish-infra-eco-logi-urbanism-in-monu-magazine/ ; CV |
| sustainable-energy-landscapes | Kathy Velikov, Geoffrey Thün | CONFIRMED. The source order is Thün, Velikov ("Conduit Urbanism: Rethinking Infrastructural Ecologies…"). | https://taubmancollege.umich.edu/news/2012/12/20/thun-and-velikov-publish-research-on-megaregional-energy-systems-and-shed-cartographies-in-new-edited-volume/ |
| water | Kathy Velikov, Geoffrey Thün, Colin Ripley | CONFIRMED. The source order is **Colin Ripley, Geoffrey Thün, Kathy Velikov** ("Aqua Alte"). | CV |
| fuel | Kathy Velikov, Geoffrey Thün | CONFIRMED. The source order is Thün, Velikov ("Post-Carbon Highway"). | CV |
| tad-journal-2-2 | L. Junghans, D. Tish, D. Bruggmann, G. Thün, K. Velikov | CORRECT-TO **L. Junghans, D. Tish, D. Brugmann, K. Velikov, G. Thün** | https://api.crossref.org/works/10.1080/24751448.2018.1497370 |
| cleaner-environmental-systems (extra) | "N. Tilie" (copied from the old site's typo); Year blank | CORRECT-TO **N. Tillie**; Year **2022** | https://api.openalex.org/works/doi:10.1016/j.cesys.2022.100074 |

#### Publication years (35 flagged)

CONFIRMED (32):

| Slug | Year | Source |
|---|---|---|
| tad-journal-9-1 | 2025 | https://css.umich.edu/publications/research-publications/stretch-codes-and-building-envelope (TAD 9:1, DOI 10.1080/24751448.2025.2475722) |
| jae-vol-78-issue-2 | 2024 | OpenAlex |
| architecture-mps-25 | 2023 | https://doaj.org/article/2a81c8c997514f4da07f9ed502d3fa84 (August 2023) |
| the-nature-of-enclosure | 2022 | CV |
| ambiguous-territory | 2022 | Actar |
| transfewmation | 2021 | https://api.openalex.org/works/doi:10.1007/978-3-030-61977-0_9 |
| jae-vol-74-issue-1 | 2020 | Crossref 10.1080/10464883.2020.1693831 |
| tad-journal-2-2 | 2018 | Crossref |
| towards-a-robotic-architecture | 2018 | CCA |
| third-coast-atlas | 2017 | CV |
| indoor-air-vol-27-issue-5 | 2017 | Crossref 10.1111/ina.12384 |
| infrastructure-space | 2017 | CV, which settles the dossier's 2016 |
| ad-integrating-innovation-in-architecture | 2016 | https://search.mnlink.org/Record/9ab72ace-75ce-4491-bdcf-bad277464a64 |
| sound-materials | 2016 | CV |
| infra-eco-logi-urbanism | 2015 | CV |
| jae-vol-69-issue-1 | 2015 | Crossref 10.1080/10464883.2015.987073 |
| hypernatural | 2015 | CV |
| advanced-customization-… | 2015 | CV |
| paradigms-in-computing | 2014 | CCA |
| evolo-06 | 2014 | CV |
| a22-… | 2014 | CV, which settles the Trento record's 2013 |
| constructing-green | 2013 | CV |
| bracket-goes-soft-almanac-2 | 2012 | https://actar.com/product/bracket-2-goes-soft/ (December 2012) |
| volume-32-centers-adrift | 2012 | CV |
| sustainable-energy-landscapes | 2012 | Taubman news, Dec 20, 2012. The WUR catalogue gives 2013. |
| ijac-volume-10-issue-03 | 2012 | CV |
| interiors-journal-volume-3-issues-1-2 | 2012 | CV |
| monu-15 | 2011 | Taubman news, Dec 7, 2011 |
| infrastructure-as-architecture-… | 2010 | CV |
| new-geographies-02 | 2009 | https://taubmancollege.umich.edu/news/2009/11/20/professors-velikov-and-thuns-article-conduit-urbanism-published-in-new-geographies-journal-02-landscapes-of-energy/ |
| water | 2009 | CV |
| fuel | 2008 | CV |

CORRECT-TO (3):

| Slug | Change | Source |
|---|---|---|
| design-for-rethinking-resources | 2024 → **2023** (Springer, published 16 Nov 2023) | https://adk.elsevierpure.com/en/publications/design-for-rethinking-resources-proceedings-of-the-uia-world-cong/ |
| next-new-york | 2022 → **2023** ("Spring 2023" on the ORO / Applied Research and Design page; the CV says 2022) | https://appliedresearchanddesign.com/product/next-new-york |
| the-routledge-companion-to-ecological-design-thinking | 2022 → **2023** (Routledge gives © 2023; the CV says 2022) | Routledge page above |

#### Publisher, series and volume details (about 20 flagged)

| Slug | Detail | Verdict | Source |
|---|---|---|---|
| next-new-york | Next Cities series, ORO Editions | CONFIRMED | https://www.arch.virginia.edu/news/recap-next-new-york-book-talk ; ARD / ORO page |
| towards-a-robotic-architecture | ORO Editions | CONFIRMED (Applied Research and Design, an imprint of ORO Editions) | CCA |
| third-coast-atlas | Actar | CONFIRMED (ActarD) | CV |
| bracket-goes-soft-almanac-2 | Actar | CONFIRMED | Actar |
| a22-… | "Ed. Pino Scaglione, Actar" | CORRECT-TO "Eds. Pino Scaglione, M. Ricci, List / Actar" | CV |
| transfewmation | Contemporary Urban Design Thinking series, Springer | CONFIRMED | OpenAlex |
| advanced-customization-… | Springer | CONFIRMED | CV |
| constructing-green | MIT Press | CONFIRMED (Henn & Hoffman, MIT Press 2013) | CV |
| water | Alphabet City, MIT Press | CONFIRMED (MIT Press per the CV; Alphabet City per the old site's own Amazon link) | CV |
| fuel | Alphabet City, MIT Press | CONFIRMED (same sources as water) | CV |
| infra-eco-logi-urbanism | Park Books, Zürich | CONFIRMED | CV |
| hypernatural | Princeton Architectural Press | CONFIRMED | CV |
| sound-materials | Frame Publishers | CONFIRMED (Amsterdam) | CV |
| sustainable-energy-landscapes | CRC Press / Taylor & Francis | CONFIRMED | https://research.wur.nl/en/publications/sustainable-energy-landscapes-designing-planning-and-development/ |
| infrastructure-as-architecture-… | Jovis | CONFIRMED | CV |
| paradigms-in-computing | eVolo | CONFIRMED (eVolo Press) | CCA |
| new-geographies-02 | Harvard Graduate School of Design | CONFIRMED (the GSD publication page is the item's own link) | https://www.gsd.harvard.edu/publication/new-geographies-02-landscapes-of-energy/ |
| design-construction-of-high-performance-homes-korean-translation | "original edition: Routledge, 2012" | CONFIRMED | CV |
| ad-integrating-innovation-in-architecture | AD Smart 04, Wiley | CONFIRMED (AD Smart 4) | MnLINK |
| architect-magazine | "vol. 105 no. 7" | REMOVE. The July 2016 issue page shows no volume or issue number. | https://www.architectmagazine.com/magazine/2016/july/ |
| monu-15 | "Magazine on Urbanism" | CONFIRMED | https://en.wikipedia.org/wiki/MONU_(magazine) |
| volume-32-centers-adrift | Volume (Archis) #32 | CONFIRMED ("Volume: Centers Adrift, 32") | CV |

### B. Fix list (apply verbatim)

Each row gives the collection, the slug, the field, the current text and the replacement. "—" means empty.

#### B1. Corrections from public sources

| Collection | Slug | Field | From | To |
|---|---|---|---|---|
| Publications | jae-vol-78-issue-2 | Authors | Kathy Velikov, Geoffrey Thün, Eilis Finnegan | Kathy Velikov, Eilís Finnegan, Geoffrey Thün |
| Publications | fabricate | Authors | Kathy Velikov, Wes McGee, Daniel Tish, Geoffrey Thün | Wes McGee, Kathy Velikov, Geoffrey Thün, Daniel Tish |
| Publications | towards-a-robotic-architecture | Authors | Wes McGee, Kathy Velikov, Geoffrey Thün | Wes McGee, Kathy Velikov, Geoffrey Thün, Daniel Tish |
| Publications | volume-32-centers-adrift | Authors | Kathy Velikov, Geoffrey Thün | Geoffrey Thün, Kathy Velikov, Colin Ripley |
| Publications | monu-15 | Authors | Kathy Velikov, Geoffrey Thün | Geoffrey Thün, Kathy Velikov, Colin Ripley |
| Publications | tad-journal-2-2 | Authors | L. Junghans, D. Tish, D. Bruggmann, G. Thün, K. Velikov | L. Junghans, D. Tish, D. Brugmann, K. Velikov, G. Thün |
| Publications | bracket-goes-soft-almanac-2 | Authors (order only, optional) | Kathy Velikov, Geoffrey Thün, Colin Ripley | Colin Ripley, Kathy Velikov, Geoffrey Thün |
| Publications | water | Authors (order only, optional) | Kathy Velikov, Geoffrey Thün, Colin Ripley | Colin Ripley, Geoffrey Thün, Kathy Velikov |
| Publications | fuel | Authors (order only, optional) | Kathy Velikov, Geoffrey Thün | Geoffrey Thün, Kathy Velikov |
| Publications | sustainable-energy-landscapes | Authors (order only, optional) | Kathy Velikov, Geoffrey Thün | Geoffrey Thün, Kathy Velikov |
| Publications | a22-new-ecologies-for-osmotic-infra-structures | Authors (order only, optional) | Kathy Velikov, Geoffrey Thün | Geoffrey Thün, Kathy Velikov |
| Publications | a22-new-ecologies-for-osmotic-infra-structures | Venue | Ed. Pino Scaglione, Actar | Eds. Pino Scaglione, M. Ricci, List / Actar |
| Publications | cleaner-environmental-systems | Authors | P. N. ten Caat, M. J. Tenpierik, T. Sanyal, N. Tilie, A. A. J. F. van den Dobbelsteen, G. Thün, S. Cullen, S. Nakayama, T. Karanisa, S. Monti | P. N. ten Caat, M. J. Tenpierik, T. Sanyal, N. Tillie, A. A. J. F. van den Dobbelsteen, G. Thün, S. Cullen, S. Nakayama, T. Karanisa, S. Monti |
| Publications | cleaner-environmental-systems | Year | — | 2022 |
| Publications | design-for-rethinking-resources | Year | 2024 | 2023 |
| Publications | next-new-york | Year | 2022 | 2023 |
| Publications | the-routledge-companion-to-ecological-design-thinking | Year | 2022 | 2023 |
| Publications | architect-magazine | Venue | Architect, the journal of the American Institute of Architects, vol. 105 no. 7 | Architect, the journal of the American Institute of Architects |
| Projects | jack-layton-ferry-terminal-toronto | Year | 2014–2015 | 2015 |
| Recognition | 2014-ford-urp-grant | Awarding Body | Ford Motor Company, University Research Program | Ford Motor Company, URP Grant |
| Recognition | 2007-9th-annual-arquine-urban-design-competition | Summary | Third place in the 9th Arquine Urban Design Competition for the Infographic Center at the Plaza de las Tres Culturas, Mexico City. | Third place in the 9th Annual Arquine Urban Design Competition for Bridging Strata, Plaza de las Tres Culturas, Mexico City. |
| Recognition | 2007-9th-annual-arquine-urban-design-competition | Related Project | infographic-center | — (unless Kathy confirms that Bridging Strata is the Infographic Center project) |
| Recognition | 2023-acadia-society-award-for-leadership | Body (2nd paragraph, first sentence) | As President she created the ACADIA Diversity Committee and updated the organization's publication ethics; during her tenure the Board became substantially more diverse. | As President she developed ACADIA's codes of ethics and conduct. |
| Recognition | 2023-acadia-society-award-for-leadership | Body (talk sentence) | Her award talk, "Cultivating a Community of Practice", was given on 26 October 2023. | Keep only if Kathy confirms; otherwise delete the sentence. |
| Recognition | 2025-velikov-faia | Body (2nd paragraph, opening clause) | She was nominated through the AIA Michigan chapter and recognized for | She was one of four AIA Michigan members elevated in 2025, recognized for |
| News | ambiguous-territory-book-2022 | Body (last paragraph) | The book was launched at Rizzoli Bookstore in New York in January 2023. Its print run of 1,500 copies sold out. | The book was launched at Rizzoli Bookstore in New York. The print edition has sold out. |

No change is needed for these, because each was confirmed:
- the Prix de Rome summary;
- the NSF 2024 summary and awarding body;
- the Extraction description and meta description;
- RAIC 2011 "responsive envelope system", which reverses the CHANGED verdict in the Recognition table;
- Wanxiang "in Hangzhou";
- "Team North";
- CSLA "National";
- the Young Architects Forum names;
- ACADIA President 2018–2020 and Vice President 2021–2022;
- the remaining FAIA facts;
- the other 32 years and 19 publisher, series and volume details.

#### B2. Restores of dropped old-site content

The old-site text is quoted exactly. The new CMS has no Typology field, so typology values go into Scope and Support as a labelled first line.

| Collection | Slug | Field | From | To |
|---|---|---|---|---|
| Projects | french-river-visitor-center | Scope and Support | Client: Ministry of Natural Resources, Ontario Parks | Client: Ministry of Natural Resources, Ontario Parks<br>Budget: $ 4.8MM CDN |
| Projects | becoming-biomass | Scope and Support | Support: University of Tennessee School of Architecture; … (unchanged) | Typology: Urban Systems Design Research<br>Support: University of Tennessee School of Architecture; … (unchanged) |
| Projects | pavilions-at-notion | Scope and Support | — | Typology: Cultural Facilities Design |
| Projects | notion-archeological-ecological-park | Scope and Support | — | Typology: Landscape, Site, and Visitor experience design. |
| Projects | common-health-jamaica-prototype | Scope and Support | — | Typology: Prefabricated Prototype |
| Projects | research-on-the-city-2014 | Scope and Support | Scope: Research includes intensive city analysis … (unchanged) | Typology: Urban Systems Research<br>Scope: Research includes intensive city analysis … (unchanged) |
| Projects | research-through-making-v-pneus | Scope and Support | Scope: Design and prototyping of a kinetic, sensing, environment-responsive envelope system. … (unchanged) | Typology: Pneus Systems<br>Scope: Design and prototyping … (unchanged) |
| Projects | research-through-making-ii | Scope and Support | Scope: Design and prototyping of a kinetic, sensing, environment-responsive interior envelope system. … (unchanged) | Typology: Responsive Envelope System<br>Scope: Design and prototyping … (unchanged) |
| Projects | french-river-visitor-center | Scope and Support (in addition to the Budget line) | Client: Ministry of Natural Resources, Ontario Parks | Typology: Cultural Facilities<br>Client: Ministry of Natural Resources, Ontario Parks<br>Budget: $ 4.8MM CDN |
| Publications | think-space | Venue | Think Space Pamphlets, 2nd Unconference Edition, Zagreb | Think Space Pamphlets, 2nd Unconference Edition, Zagreb; Editorial team: Sanja Cvjetko Jerkovic, Luka Korlaet, Ana Dana Beroš, Lukas Pauer, Adrian Lahoud with Kata Gašpar, editorial executive assistant |
| Publications | young-architects-10 | Venue | The Architectural League of New York, Princeton Architectural Press | The Architectural League of New York, Princeton Architectural Press; foreword by Jesse Reiser, introduction by Anne Rieselbach |
| Publications | the-routledge-companion-to-ecological-design-thinking | Title | The Routledge Companion to Ecological Design Thinking | The Routledge Companion to Ecological Design Thinking: Healthful Ecotopian Visions for Architecture and Urbanism |
| Publications | jae-vol-78-issue-2 | Description (new first line) | "Across the planet, … | WORLDING. ENERGY. TRANSITIONS.<br>"Across the planet, … |
| Publications | jae-vol-74-issue-1 | Description (new first line) | The word "H2O" sits uncomfortably … | Special Issue: H2O<br>The word "H2O" sits uncomfortably … |
| Projects | 13 projects listed under the systemic RVTR-label row in the Projects table (optional) | Credits (first unlabelled line) | e.g. "Kathy Velikov, Geoffrey Thün, Dan McTavish, …" | Prefix the line with "RVTR: ", e.g. "RVTR: Kathy Velikov, Geoffrey Thün, Dan McTavish, …" |

Notes on the restores:
- **Think Space.** "editoral" on the old site has been corrected to "editorial".
- **JAE 74:1.** The old site reads "H20", with a zero; the restore uses the intended "H2O", which matches the body text.
- **Routledge subtitle.** Capitalised as on the publisher's page.
