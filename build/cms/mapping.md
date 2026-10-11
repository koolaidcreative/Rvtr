# RVTR CMS import: mapping notes

These notes cover the five JSON files in this folder, which were built from the scraped Monograph site. Each item's content comes from its own `main article section.page-section`. The "More Work" and "More News" grids are excluded.

- projects.json: 53 items (8 featured, 10 archive)
- publications.json: 73 items (6 featured)
- recognition.json: 57 items (9 featured; FAIA 2025 and ACADIA 2023 are pinned on top)
- team.json: 82 people (directors, research associate and alumni)
- instagram-fallback.json: 6 images

Images are hot-linked from raw.githubusercontent.com/koolaidcreative/Rvtr at the largest rendition on disk. All 643 files were checked locally, and 5 sampled URLs returned HTTP 200.

## Projects

Projects are ordered with the featured items first, then by year, newest first.

| # | Slug | Title | Thread | Feat. | Archive | Status | Year | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | becoming-biomass | Becoming Biomass | Territories and Urban Systems | yes |  | Speculative | 2022–2024 | Regional decarbonization scenario for the Tennessee Valley (RVTR + POST). |
| 2 | pavilions-at-notion | Pavilions at Notion | Field Research | yes |  | Research | 2018–2019 | Part of the Notion (Turkey) field research cluster with the Kelsey Museum. |
| 3 | extraction | Extraction | Exhibitions and Installations | yes |  | Exhibition | 2016 | Canadian Pavilion exhibition, Venice 2016 (team led by curator Pierre Bélanger). |
| 4 | infundibuliforms | Infundibuliforms | Responsive Envelopes and Material Systems | yes |  | Prototype | 2015–2016 | Kinetic, robotically fabricated elastomeric cable-net envelope prototype. |
| 5 | infra-eco-logi-urbanism | Infra Eco Logi Urbanism: Liberty Gallery, Ann Arbor | Exhibitions and Installations | yes |  | Exhibition | 2012–2013 | Touring exhibition venue (Ann Arbor); best-photographed IELU venue. |
| 6 | resonant-chamber | Resonant Chamber | Responsive Envelopes and Material Systems | yes |  | Prototype | 2011–2013 | Rigid-origami acoustic envelope prototype. |
| 7 | pneusystems | PneuSystems | Responsive Envelopes and Material Systems | yes |  | Prototype | 2013 | Cellular pneumatic envelope prototypes. |
| 8 | north-house | North House | Buildings and Prototypes | yes |  | Prototype | 2008–2010 | Full-scale solar-powered prefabricated house prototype (2009 Solar Decathlon). |
| 9 | transect-31-52-11-n-111-07-29-w-to-37-04-42-n-116-01-49-w | Transect: 31°52′11″ N, 111°07′29″ W to 37°04′42″ N, 116°01′49″ W | Field Research |  |  | Exhibition | 2025 | Site-based high desert section drawing; fieldwork-led territorial reading. |
| 10 | notion-archeological-ecological-park | Notion Archeological Ecological Park | Field Research |  |  | Research | 2014–2019 | Fieldwork-based site analysis and park planning at Notion, Turkey. |
| 11 | latitudo-borealis | Latitudo Borealis | Responsive Envelopes and Material Systems |  |  | Prototype | 2016–2017 | Timber wall assembly reversing winter heat flow; material system research. |
| 12 | common-health-jamaica-prototype | Common_Health+ Clinic, Sandy Bay, Jamaica | Buildings and Prototypes |  |  | Prototype | 2016 | Prefabricated container clinic prototype, shipped to Jamaica in 2016. |
| 13 | post-human-frontiers | Posthuman Frontiers: Data, Designers and Cognitive Machines | Exhibitions and Installations |  |  | Exhibition | 2016 | ACADIA 2016 exhibition design (with SPAN). |
| 14 | jack-layton-ferry-terminal-toronto | Jack Layton Ferry Terminal, Toronto | Buildings and Prototypes |  |  | Competition | 2014–2015 | Building-scale invited competition (shortlisted finalist) with Clément Blanchet and Batlle i Roig. |
| 15 | notion-excavation-house | Notion Excavation House | Field Research |  |  | Research | 2015–present | Facility for the Notion archaeological field project. |
| 16 | protean-prototypes | Protean Prototypes, Chicago | Territories and Urban Systems |  |  | Research | 2014–2015 | City-scale accessibility and mobility research, Chicago. |
| 17 | the-luminous-veil | The Luminous Veil, Toronto | Archive |  | yes | Built | 1998–2015 | Pre-RVTR work with Dereck Revington Studio (competition 1998; lighting 2015). |
| 18 | new-brutalist-image-tate-britain | New Brutalist Image, Tate Britain, London | Exhibitions and Installations |  |  | Exhibition | 2014–2015 | Spatial planning and display design for Tate Britain. |
| 19 | research-on-the-city-2014 | Research on the City 2014: Protean Prototypes | Territories and Urban Systems |  |  | Research | 2014–2015 | Taubman Research on the City grant phase of Protean Prototypes. |
| 20 | research-through-making-v-pneus | Research Through Making V | Exhibitions and Installations |  |  | Exhibition | 2014 | Taubman Research Through Making exhibition of PneuSystems. |
| 21 | infra-eco-logi-urbanism-yale-new-haven-ct | Infra Eco Logi Urbanism: Yale, New Haven | Exhibitions and Installations |  |  | Exhibition | 2014 | Touring exhibition venue (Yale). |
| 22 | lodge-at-dry-pine-bay | Lodge at Dry Pine Bay, French River, Ontario | Archive |  | yes |  | 2012–2014 | Private client lodge. |
| 23 | conduit-urbanism | Conduit Urbanism: Great Lakes Megaregion | Territories and Urban Systems |  |  | Research | 2008–2013 | Multi-year megaregional design research (basis of Infra Eco Logi Urbanism). |
| 24 | infra-eco-logi-urbanism-montreal | Infra Eco Logi Urbanism: Montreal | Exhibitions and Installations |  |  | Exhibition | 2012–2013 | Touring exhibition venue (Montreal). |
| 25 | infra-eco-logi-urbanism-ryerson-toronto-on | Infra Eco Logi Urbanism: Ryerson, Toronto | Exhibitions and Installations |  |  | Exhibition | 2012–2013 | Touring exhibition venue (Toronto). |
| 26 | nervous-ether | Nervous Ether | Responsive Envelopes and Material Systems |  |  | Prototype | 2013 | Pneumatic responsive skin installation from the PneuSystems research. |
| 27 | research-through-making-iii | Research Through Making III | Exhibitions and Installations |  |  | Exhibition | 2012 | Taubman Research Through Making exhibition of Resonant Chamber. |
| 28 | mobiprize | MobiPrize | Responsive Envelopes and Material Systems |  |  | Built | 2012 | Digitally fabricated award object (with Matter Design). |
| 29 | helsinki-south-harbor | Public Logistics: Helsinki South Harbor, Finland | Territories and Urban Systems |  |  | Competition | 2011 | Waterfront urban design competition (RVTR team). |
| 30 | penser-tout-haut | Penser Tout Haut | Exhibitions and Installations |  |  | Exhibition | 2011 | Group exhibition curated by Elke Krasny that included RVTR. |
| 31 | stratus | The Stratus Project | Responsive Envelopes and Material Systems |  |  | Prototype | 2010 | Kinetic, sensing interior envelope prototype. |
| 32 | research-through-making-ii | Research Through Making II | Exhibitions and Installations |  |  | Exhibition | 2010 | Taubman Research Through Making exhibition of Stratus. |
| 33 | latitude-housing-system | Latitude Housing System: Cherepovets, Russia | Buildings and Prototypes |  |  | Competition | 2008–2010 | Mass-customized housing system; RVTR-authored, honorable mention. |
| 34 | convenience-gallery | Convenience Gallery, Toronto | Exhibitions and Installations |  |  | Exhibition | 2009 | Re-installation of Office Project / Project Office (Velikov, sole author). |
| 35 | nexus-park-city | Nexus / Park / City: Changchun, China | Territories and Urban Systems |  |  | Competition | 2008 | Invited urban/landscape masterplan (first-place commission per dossier). |
| 36 | matters-of-concern | Matters of Concern | Exhibitions and Installations |  |  | Exhibition | 2008 | RVTR's first solo exhibition (2008). |
| 37 | buoyant-aquacology | Buoyant Aquacology: Venetian Futures | Territories and Urban Systems |  |  | Competition | 2007 | Territorial-scale competition proposal for the Venetian lagoon (RVTR authors). |
| 38 | office-project-project-office | Office Project / Project Office | Exhibitions and Installations |  |  | Exhibition | 2007 | Installation by Kathy Velikov (sole author), 2007. |
| 39 | infographic-center | Infographic Center, Mexico City | Buildings and Prototypes |  |  | Competition | 2007 | RVTR competition entry, 3rd place (2007 Arquine). |
| 40 | swamp-house | S.W.A.M.P. House, Sauble Beach, Ontario | Archive |  | yes |  | 2005–2006 | Private residence by Velikov + Thün before RVTR (2005–2006). |
| 41 | french-river-visitor-center | French River Visitor Center, Alban, Ontario | Archive |  | yes | Built | 2001–2006 | Pre-RVTR building; Thün as associate at Baird Sampson Neuert. |
| 42 | season-house | Seasons House, Hamilton, Ontario | Archive |  | yes |  | 2005–2006 | Private residence by Velikov + Thün Building Studio (2005–2006). |
| 43 | grounding | Grounding | Archive |  | yes | Exhibition | 1995 | 1995 student-era installation; credited as team member role. |
| 44 | the-glm-gateway-toronto-on | The GLM Gateway, Toronto | Territories and Urban Systems |  |  | Speculative |  | Intervention within the Conduit Urbanism megaregional project. |
| 45 | the-detroit-windsor-crossing | The Detroit–Windsor Crossing | Territories and Urban Systems |  |  | Speculative |  | Intervention within the Conduit Urbanism megaregional project. |
| 46 | notion-turkey | Ionian Archeology, Notion, Turkey | Field Research |  |  | Research |  | Archaeological survey and field research at Notion with U-M and Brown. |
| 47 | the-exchange-chicago-il | The Exchange, Chicago | Territories and Urban Systems |  |  | Speculative |  | Intervention within the Conduit Urbanism megaregional project. |
| 48 | insignia-caeli | Insignia Caeli: Yucatán Peninsula, Mexico | Field Research |  |  | Research |  | Site-based mirror interventions at cenotes in the Yucatán. |
| 49 | shadowtime-landscape-37-59-34-58-n-27-11-50-26-e | Shadowtime: 37°59′34.58″ N, 27°11′50.26″ E | Field Research |  |  | Research |  | Landscape piece at the Notion coordinates; field research cluster. |
| 50 | harmony | Harmony: Stratford, Ontario | Archive |  | yes |  |  | Early building/landscape design (team suggests c. 2007–2008); not research-led; undated. |
| 51 | pampas-house | Pampas House: Buenos Aires, Argentina | Archive |  | yes |  |  | Private commission; credited as team member role. |
| 52 | jalisco-state-library | Jalisco State Library: Guadalajara, Mexico | Archive |  | yes |  |  | Credited as team member role. |
| 53 | beirut-house-of-arts-and-culture | House of Arts and Culture: Beirut, Lebanon | Archive |  | yes | Competition |  | Competition entry credited as team member role. |

## Publications

Publications are ordered by year, newest first. An item with an unknown year (null) takes the position of its neighbour in the old site list.

| # | Slug | Type | Year | Year source | Feat. |
|---|---|---|---|---|---|
| 1 | tad-journal-9-1 | Journal article | 2025 | dossier 5 and 6.3 (TAD 9:1, 2025) |  |
| 2 | plastic-futures | Book chapter | unknown | - |  |
| 3 | building-metabolism | Book chapter | unknown | - |  |
| 4 | jae-vol-78-issue-2 | Journal article | 2024 | FAIA PDF 2.3 / dossier (JAE 78(2) 2024) | yes |
| 5 | design-for-rethinking-resources | Proceedings | 2024 | cover filename (_2024_); congress held 2023 |  |
| 6 | architecture-mps-25 | Journal article | 2023 | cover filename (amps_2023) |  |
| 7 | next-new-york | Book chapter | 2022 | FAIA PDF 2.3 (ORO 2022) |  |
| 8 | the-nature-of-enclosure | Book chapter | 2022 | FAIA PDF 2.3 (Actar 2022) |  |
| 9 | ambiguous-territory | Book | 2022 | dossier 6.2 / FAIA PDF (Actar 2022) | yes |
| 10 | the-routledge-companion-to-ecological-design-thinking | Book chapter | 2022 | FAIA PDF 2.3 (Routledge 2022) |  |
| 11 | cleaner-environmental-systems | Journal article | unknown | - |  |
| 12 | transfewmation | Book chapter | 2021 | FAIA PDF 2.3 (Springer 2021) |  |
| 13 | the-city-and-complexity-life-design-and-commerce-in-the-built-environment | Proceedings | 2020 | text |  |
| 14 | jae-vol-74-issue-1 | Journal article | 2020 | FAIA PDF 2.3 (JAE 74(1) 2020) |  |
| 15 | structures-vol-18 | Journal article | 2019 | text citation |  |
| 16 | tad-journal-2-2 | Journal article | 2018 | FAIA PDF 2.3 (TAD 2(2) 2018) | yes |
| 17 | architect-s-newspaper-the-texas-issue | Journal article | 2018 | subtitle |  |
| 18 | towards-a-robotic-architecture | Book chapter | 2018 | FAIA PDF 2.3 (ORO 2018) |  |
| 19 | third-coast-atlas | Book chapter | 2017 | FAIA PDF 2.3 (Actar 2017) |  |
| 20 | 2017-acsa-proximate-and-remote | Proceedings | 2017 | subtitle |  |
| 21 | 2017-acadia-projects | Catalogue | 2017 | title |  |
| 22 | indoor-air-vol-27-issue-5 | Journal article | 2017 | cover filename (indoorair_2017) |  |
| 23 | fabricate | Proceedings | 2017 | text |  |
| 24 | infrastructure-space | Book chapter | 2017 | FAIA PDF 2.3 (Ruby Press 2017); dossier gives 2016 |  |
| 25 | footprint-vol-11-issue-02 | Journal article | unknown | - |  |
| 26 | architect-magazine | Press | 2016 | subtitle |  |
| 27 | ad-integrating-innovation-in-architecture | Press | 2016 | FAIA PDF 2.3 press list (Wiley 2016) |  |
| 28 | sound-materials | Press | 2016 | FAIA PDF 2.3 press list (Frame 2016) |  |
| 29 | acadia-2016-projects-catalog | Catalogue | 2016 | title |  |
| 30 | 2016-acadia-proceedings | Proceedings | 2016 | title | yes |
| 31 | extraction-exhibition-catalog | Catalogue | 2016 | subtitle | yes |
| 32 | oase-96 | Journal article | 2016 | text citation |  |
| 33 | ijac-vol-13-issue-02 | Journal article | 2015 | text citation |  |
| 34 | infra-eco-logi-urbanism | Book | 2015 | dossier 6.1 (Park Books 2015) | yes |
| 35 | jae-vol-69-issue-1 | Journal article | 2015 | FAIA PDF 2.3 (JAE 69(1) 2015) |  |
| 36 | hypernatural | Press | 2015 | FAIA PDF 2.3 press list (Princeton Architectural Press 2015) |  |
| 37 | advanced-customization-in-architectural-design-and-construction | Press | 2015 | FAIA PDF 2.3 press list (Springer 2015) |  |
| 38 | design-construction-of-high-performance-homes-korean-translation | Book chapter | unknown | - |  |
| 39 | paradigms-in-computing | Book chapter | 2014 | FAIA PDF 2.3 (eVolo/ActarD 2014) |  |
| 40 | leonardo-vol-47-number-4-2014 | Journal article | 2014 | title |  |
| 41 | evolo-06 | Journal article | 2014 | FAIA PDF 2.3 (eVolo 06 2014) |  |
| 42 | a22-new-ecologies-for-osmotic-infra-structures | Book chapter | 2014 | FAIA PDF 2.3 (Actar 2014) |  |
| 43 | what-s-the-matter | Proceedings | unknown | - |  |
| 44 | architecture-and-national-identity | Book | unknown | - |  |
| 45 | performative-materials-in-architecture-and-design | Book chapter | unknown | - |  |
| 46 | 2013-txa-interactive-conference-proceedings | Proceedings | 2013 | title |  |
| 47 | constructing-green | Book chapter | 2013 | dossier 6.3 (MIT Press 2013) |  |
| 48 | think-space | Journal article | 2013 | text citation |  |
| 49 | infra-eco-logi-urbanism-exhibition-catalog | Catalogue | unknown | - |  |
| 50 | specifics | Proceedings | unknown | - |  |
| 51 | bracket-goes-soft-almanac-2 | Book chapter | 2012 | FAIA PDF 2.3 (Actar 2012) |  |
| 52 | volume-32-centers-adrift | Journal article | 2012 | dossier 6.3 / FAIA PDF (Volume 32, 2012) |  |
| 53 | leonardo-vol-45-number-4-2012 | Journal article | 2012 | title |  |
| 54 | sustainable-energy-landscapes | Book chapter | 2012 | FAIA PDF 2.3 (Taylor & Francis 2012) |  |
| 55 | jae-vol-65-issue-2 | Journal article | 2012 | text citation |  |
| 56 | ijac-volume-10-issue-03 | Journal article | 2012 | FAIA PDF 2.3 (IJAC 10(3) 2012) |  |
| 57 | interiors-journal-volume-3-issues-1-2 | Journal article | 2012 | FAIA PDF 2.3 (Interiors 3(1–2) 2012) |  |
| 58 | monu-15 | Journal article | 2011 | dossier 6.3 (MONU 15, 2011) |  |
| 59 | eco-structure-oct-11 | Press | 2011 | title (Oct '11) |  |
| 60 | architect-aug-10 | Press | 2010 | title (Aug '10) |  |
| 61 | infrastructure-as-architecture-designing-composite-networks | Book chapter | 2010 | FAIA PDF 2.3 (Jovis 2010) |  |
| 62 | canadian-architect-10 | Press | 2010 | title and text |  |
| 63 | new-geographies-02 | Journal article | 2009 | FAIA PDF 2.3 (New Geographies 02 2009) |  |
| 64 | jae-vol-62-issue-4 | Journal article | 2009 | text citation |  |
| 65 | water | Book chapter | 2009 | FAIA PDF 2.3 (MIT Press 2009) |  |
| 66 | young-architects-10 | Book chapter | 2009 | text (publication date 6/1/2009) |  |
| 67 | fuel | Book chapter | 2008 | FAIA PDF 2.3 (MIT Press 2008) |  |
| 68 | dimensions-21 | Journal article | 2008 | subtitle |  |
| 69 | in-place-of-sound | Book | unknown | - |  |
| 70 | canadian-architect-04-07 | Press | 2007 | title (04:07) and cover filename |  |
| 71 | twenty-and-change-emerging-canadian-design-practices | Press | unknown | - |  |
| 72 | canadian-architect-05 | Press | 2005 | subtitle |  |
| 73 | houses-of-steel | Press | unknown | - |  |

## Recognition

Recognition items are ordered with FAIA and ACADIA pinned first, then by year, newest first. Each Year comes from the old title or the text card, never from the old JSON "date". Titles follow the wording on the text cards and the FAIA PDF.

| # | Slug | Kind | Year | Feat. | Related project |
|---|---|---|---|---|---|
| 1 | 2025-velikov-faia | Fellowship | 2025 | yes |  |
| 2 | 2023-acadia-society-award-for-leadership | Award | 2023 | yes |  |
| 3 | 2024-nsf-grant | Grant | 2024 | yes |  |
| 4 | 2024-nfwf-grant | Grant | 2024 | yes |  |
| 5 | 2020-tad-research-contribution-award | Award | 2020 |  | latitudo-borealis |
| 6 | 2019-guardian-industries-sponsored-project | Sponsored research | 2019 |  |  |
| 7 | 2019-urban-studies-foundation | Grant | 2019 |  |  |
| 8 | 2019-bloomberg-philanthropies-grant | Grant | 2019 |  |  |
| 9 | 2019-ford-alliance-grant | Grant | 2019 |  |  |
| 10 | 2018-wanxiang-sponsored-project | Sponsored research | 2018 |  |  |
| 11 | 2018-michigan-mellon-project-subgrant | Grant | 2018 |  |  |
| 12 | 2018-prototyping-tomorrow-grant | Grant | 2018 |  |  |
| 13 | 2018-sugi-fwe-nexus-grant | Grant | 2018 |  |  |
| 14 | 2017-az-award | Award | 2017 | yes | extraction |
| 15 | 2017-csla-award | Award | 2017 |  | extraction |
| 16 | 2017-ford-alliance-grant | Grant | 2017 |  |  |
| 17 | 2016-ford-alliance-grant | Grant | 2016 |  |  |
| 18 | 2016-r-d-honorable-mention | Award | 2016 | yes | infundibuliforms |
| 19 | 2015-us-dot-nextrans | Grant | 2015 |  |  |
| 20 | 2015-epa-grant | Grant | 2015 |  |  |
| 21 | 2014-acsa-faculty-design-award-honorable-mention | Award | 2014 |  | infra-eco-logi-urbanism |
| 22 | 2014-aia-upjohn-research-initiative | Grant | 2014 |  | pneusystems |
| 23 | 2014-ford-urp-grant | Grant | 2014 |  |  |
| 24 | 2014-research-on-the-city-grant | Grant | 2014 |  | research-on-the-city-2014 |
| 25 | 2013-us-dot-nextrans-award | Grant | 2013 |  |  |
| 26 | 2013-architizer-a-awards-program | Award | 2013 |  | resonant-chamber |
| 27 | 2013-jae-best-design-as-scholarship-award | Award | 2013 |  | stratus |
| 28 | 2013-us-dot-nextrans-new-cartographies | Grant | 2013 |  |  |
| 29 | 2013-research-through-making-grant | Grant | 2013 |  | pneusystems |
| 30 | 2012-acsa-faculty-design-award | Award | 2012 |  | stratus |
| 31 | 2012-small-projects-grant | Grant | 2012 |  | resonant-chamber |
| 32 | 2012-um-office-for-the-vice-president-of-research | Grant | 2012 |  |  |
| 33 | 2012-special-project-grant | Grant | 2012 |  |  |
| 34 | 2011-eco-structure-evergreen-award | Award | 2011 |  | north-house |
| 35 | 2011-canada-council-for-the-arts | Grant | 2011 |  |  |
| 36 | 2011-van-alen-institute-honorable-mention | Prize | 2011 |  | conduit-urbanism |
| 37 | 2011-innovation-in-architecture-award | Award | 2011 | yes | north-house |
| 38 | 2011-research-through-making-grant | Grant | 2011 |  | resonant-chamber |
| 39 | 2011-research-creation-grant | Grant | 2011 |  | stratus |
| 40 | 2011-um-wims-seed-grant | Grant | 2011 |  |  |
| 41 | 2011-guardian-industries-inc | Sponsored research | 2011 |  |  |
| 42 | 2010-design-excellence-award | Award | 2010 |  | north-house |
| 43 | 2010-r-d-award | Award | 2010 | yes | north-house |
| 44 | 2010-research-through-making-grant | Grant | 2010 |  | stratus |
| 45 | 2009-professional-prix-de-rome-in-architecture | Prize | 2009 | yes |  |
| 46 | 2009-royal-architectural-institute-of-canada | Award | 2009 |  |  |
| 47 | 2009-research-creation-grant | Grant | 2009 |  |  |
| 48 | 2009-technology-development-fund-grant | Grant | 2009 |  | north-house |
| 49 | 2009-twenty-change-02 | Award | 2009 |  |  |
| 50 | 2008-living-steel-extreme-housing | Prize | 2008 |  | latitude-housing-system |
| 51 | 2008-canada-council-for-the-arts | Grant | 2008 |  | matters-of-concern |
| 52 | 2008-prototypes-development-grant | Grant | 2008 |  | north-house |
| 53 | 2008-us-department-of-energy-national-renewable-energy-laboratory | Grant | 2008 |  | north-house |
| 54 | 2008-young-architects-forum-award | Prize | 2008 |  |  |
| 55 | 2007-9th-annual-arquine-urban-design-competition | Prize | 2007 |  | infographic-center |
| 56 | 2005-canadian-architect-magazine | Award | 2005 |  | swamp-house |
| 57 | 2000-toronto-society-of-architects | Prize | 2000 |  |  |

## Slug changes (redirects)

All other slugs are unchanged. Projects keep their old slugs.

| Old URL | New slug | Why |
|---|---|---|
| /writing-publications/archis | volume-32-centers-adrift | the item is Volume #32 Centers Adrift |
| /writing-publications/extraction-exhibition-catalog-2016-venice-bienalle | extraction-exhibition-catalog | removes the typo |
| /writing-publications/footprint-vol-11-issue-01 | footprint-vol-11-issue-02 | the item is issue 02 |
| /writing-publications/leonardo-vol-47-no-4 | evolo-06 | the item is eVolo 06 (the old slug was a duplicate) |
| /writing-publications/structures-vol-17 | structures-vol-18 | the item is volume 18 |
| /awards-grants/2008-young-architect-s-forum-award | 2008-young-architects-forum-award | descriptive slug |
| /awards-grants/2011-eco-structure-evergreen-award-3eab14c0-9432-49a3-a7e8-be4400b3615c | 2011-eco-structure-evergreen-award | drops the uuid suffix (the real Evergreen award) |
| /awards-grants/2011-eco-structure-evergreen-award | 2011-um-wims-seed-grant | the old page is the WIMS SEED grant. **Collision:** the old slug is reused by the real Evergreen item, so do not redirect it if both live under the same path |
| /awards-grants/2011-honorable-mention-vai-projects-in-public-architecture | 2011-van-alen-institute-honorable-mention | descriptive slug |
| /awards-grants/2013-acsa | 2013-jae-best-design-as-scholarship-award | descriptive slug |
| /awards-grants/2014-acsa | 2014-acsa-faculty-design-award-honorable-mention | descriptive slug |
| /awards-grants/2014-aia-award | 2014-aia-upjohn-research-initiative | descriptive slug |
| /awards-grants/2014-ford-urp-grant-a8b91c0d-5bc5-4426-9dea-68d71729de34 | 2014-ford-urp-grant | descriptive slug |
| /awards-grants/2014-taubman-college | 2014-research-on-the-city-grant | descriptive slug |
| /awards-grants/2015-epa-award | 2015-epa-grant | descriptive slug |
| /awards-grants/2020-acsa-award | 2020-tad-research-contribution-award | descriptive slug |
| /awards-grants/sugi-fwe-nexus-grant-program | 2018-sugi-fwe-nexus-grant | descriptive slug |

## Uncertainties and things to check

- **Publication years unknown (null):** plastic-futures, building-metabolism, cleaner-environmental-systems, footprint-vol-11-issue-02, design-construction-of-high-performance-homes-korean-translation, what-s-the-matter, architecture-and-national-identity, performative-materials-in-architecture-and-design, infra-eco-logi-urbanism-exhibition-catalog, specifics, in-place-of-sound, twenty-and-change-emerging-canadian-design-practices, houses-of-steel.
- **AIA Upjohn Research Initiative:** the old title says 2014, but the dossier and FAIA PDF say it was awarded in 2013. 2014 is kept.
- **Guardian "The Benefits of Glass":** the site says 2011, the FAIA grants list says 2010. 2011 is kept.
- **Infra Eco Logi Urbanism venues:** the years in the old project tables conflict with the FAIA PDF (Ryerson 2014; LRA Gallery Jan–Feb 2015).
- **PneuSystems:** the site says 2013, the FAIA PDF says 2012–2014.
- **Infrastructure Space (Ruby Press):** FAIA says 2017, the dossier says 2016. 2017 is used.
- **Design for Rethinking Resources:** the year 2024 comes from the cover filename, but the congress was held in 2023.
- **2009 RAIC item:** per its text card, this is an honorable mention for the Bluepoint Facade.
- **NSF Engines grant:** "Regional Economic Engines" was changed to the official "Regional Innovation Engines".
- **Text card wording:** "American Association of Architects" on one card was corrected to American Institute of Architects.
- **Name spellings:** Mauro Carena→Carreño, Maya Przybilski→Przybylski, Weinriech→Weinreich, Lisa Sauvé, Zain AbuSeir, Clément Blanchet, Pierre Bélanger. Unresolved variants: Farid Noufaily/Noufailly, Baktash/Bakhtash, Storey-Fleming variants, Brugman/Brugmann. "Archeology" is kept as spelled on the old site.
- **Non-archive judgement calls:** Office Project (2007) and Convenience Gallery (2009) list Kathy Velikov as sole author and are kept non-archive. Harmony is archived and undated.
- **Status null:** swamp-house, harmony, season-house, pampas-house, lodge-at-dry-pine-bay and jalisco-state-library (built status not stated).
- **Cover images:** each cover defaults to the item's first image. Several are drawings or renders (e.g. Becoming Biomass, Extraction), so pick a photo if wanted.
- **Award images:** these are the old blue text cards and are probably not suitable for display. The text on them was transcribed into Title/Summary.
- **Extraction description:** the old page had no usable text, so DescriptionHTML was written from the dossier and FAIA PDF facts only.
- **Outbound links:** these were not verified, because the sandbox proxy returns 403 for external sites.
- **Dropped links:** these pointed to local PDFs not in the repo or to private Dropbox previews: cleaner-environmental-systems (Thun_Sanyal_Velikov_2021_Mapping FEW Systems across Cascading Scales_Detroit.pdf); jae-vol-65-issue-2 (JAE-65-2_ThickAir_2012.pdf); leonardo-vol-47-number-4-2014 (VelikovThunOMalley_Leonardo_NervousEther.pdf); sugi-fwe-nexus-grant-program (RVTR_M-NEX Living Lab Detroit_220630.pdf).
- **Not added:** FAIA-list items missing from the old site are candidates only, e.g. 2020 AIA/ACSA Housing Design Education Award, 2014 TEX-FAB honorable mention, 2015 Jack Layton Ferry Terminal finalist, and the 2022–23 Big Ten Academic Alliance fellowship.
- **Team:** bios and portraits are empty or null. Alumni years come from the about page. One alumni link (Daniel Tish) pointed to an image file and was dropped.
