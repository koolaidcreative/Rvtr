# News edit list (from news-factcheck.md FIX verdicts)

FROM text is quoted exactly from the live site export `/home/claude/rvtr/build/audit/site-export/cms-news.json`. In that export, `Body` is plain text with paragraphs separated by `\n`. Field names in the export are `Title`, `Teaser`, `Body`, `Outbound Link`, `Outbound Label`, `Date`.

Policy applied: every fact traces to rvtr.com, a published press release or public page (the public CV PDFs on taubmancollege.umich.edu count), or Instagram. Facts that come only from the FAIA submission are cut.

No Title, Teaser or Date changes are needed except the Ambiguous Territory title. The `Introduction` field copies `Teaser` and is untouched. No `Cover Image` alt text repeats a changed Title: the Ambiguous Territory alt is null.

**Verification:** 14 edits. All FROM strings appear exactly once in the export and inside the named field.

```
PASS  arid-logics-tulane-prize-2026 / Body: export-wide count=1, in-field count=1
PASS  stretch-codes-tad-2025 / Body: export-wide count=1, in-field count=1
PASS  kathy-velikov-faia-2025 / Body: export-wide count=1, in-field count=1
PASS  kathy-velikov-faia-2025 / Body: export-wide count=1, in-field count=1
PASS  nexthouse-nsf-engines-2024 / Body: export-wide count=1, in-field count=1
PASS  nexthouse-nsf-engines-2024 / Body: export-wide count=1, in-field count=1
PASS  acadia-society-award-for-leadership-2023 / Body: export-wide count=1, in-field count=1
PASS  from-matter-to-territory-syracuse-2022 / Body: export-wide count=1, in-field count=1
PASS  from-matter-to-territory-syracuse-2022 / OutboundLink: export-wide count=1, in-field count=1
PASS  from-matter-to-territory-syracuse-2022 / OutboundLabel: export-wide count=1, in-field count=1
PASS  ambiguous-territory-book-2022 / Title: export-wide count=1, in-field count=1
PASS  ambiguous-territory-book-2022 / Body: export-wide count=1, in-field count=1
PASS  ambiguous-territory-book-2022 / Body: export-wide count=1, in-field count=1
PASS  ambiguous-territory-book-2022 / Body: export-wide count=1, in-field count=1
```


## arid-logics-tulane-prize-2026

### Edit 1: Body

FROM:
```
received an Honorable Achievement in the Innovative Studio Pedagogy category of the 2026 Tulane Prize for Climate Change Curriculum in the Built Environment.
```
TO:
```
received an Honorable Achievement in the Innovative Studio Pedagogy category of the 2025–2026 Tulane Prize for Climate Change Curriculum in the Built Environment.
```
Source: Tulane CCU Awards 2025–2026 (architecture.tulane.edu/news/tulane-CCU-awards-2025-2026): "2025-2026 Tulane Prize for Climate Change Curriculum in the Built Environment".


## stretch-codes-tad-2025

### Edit 2: Body

FROM:
```
"Stretch Codes and the Building Envelope", by Kathy Velikov, Hasan, Lewis, Menassa, Kamat and Geoffrey Thün, appears in TAD 9:1, pages 156–171.
```
TO:
```
"Stretch Codes and the Building Envelope", by Kathy Velikov, Kazi Najeeb Hasan, Geoffrey Lewis, Carol C. Menassa, Vineet R. Kamat and Geoffrey Thün, appears in Technology | Architecture + Design (TAD) 9:1, pages 156–171.
```
Source: U-M Center for Sustainable Systems citation: Velikov, Kathy, Kazi Najeeb Hasan, Geoffrey Lewis, Carol C. Menassa, Vineet R. Kamat, Geoffrey Thün. Technology|Architecture + Design 9(1): 156–71.


## kathy-velikov-faia-2025

### Edit 3: Body

FROM:
```
Kathy Velikov, Professor of Architecture and Associate Dean for Research and Creative Practice at Taubman College and a director of RVTR, has been elevated to the American Institute of Architects College of Fellows. According to the college's announcement, fewer than 3 percent of architects hold the fellowship.
```
TO:
```
Kathy Velikov, Professor of Architecture and Associate Dean for Research and Creative Practice at Taubman College and a founding partner of RVTR, has been elevated to the American Institute of Architects College of Fellows, a distinction held by less than 3% of the architecture profession.
```
Source: Taubman College, Feb 13, 2025: "founding partner of the research-based practice RVTR"; "a distinction held by less than 3% of the architecture profession".

### Edit 4: Body

FROM:
```
The fellowship recognizes her for "furthering the science and art of planning and building by advancing the standards of architectural education and training." Her work spans practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments, from responsive material assemblies to territorial practices for decarbonization.
```
TO:
```
The fellowship recognizes her for furthering "the science and art of planning and building by advancing the standards of architectural education and training." Her work spans practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments, from responsive architectural material assemblies to territorial practices for decarbonization.
```
Source: Same article: furthering "the science and art of planning and building by advancing the standards..." ("furthering" sits outside the quote); "responsive architectural material assemblies"; "territorial practices for decarbonization".


## nexthouse-nsf-engines-2024

### Edit 5: Body

FROM:
```
NextHouse, an initiative on next-generation factory-built housing, received a $1 million NSF Engines Development Award from the National Science Foundation. The program is run by Purdue University, with the University of Michigan as a partner.
```
TO:
```
NextHouse, an initiative on next-generation factory-built housing, received a $1 million NSF Engines Development Award from the National Science Foundation. The program is run by the Purdue Applied Research Institute (PARI), with the University of Michigan among its partners.
```
Source: Purdue, June 4, 2024: "The program is being run by the Purdue Applied Research Institute (PARI)"; partnerships "with the University of Michigan, Notre Dame, Michigan State, Ivy Tech, and Lansing Community College". NSF award record: "NSF Engines Development Award: Developing innovative solutions for next-generation factory-built housing (IN, MI)", $1,000,000.

### Edit 6: Body

FROM:
```
According to Geoffrey Thün's CV, the University of Michigan component is $115,000, with Thün as co-principal investigator. In 2023 the NextHouse proposal was named one of 34 semifinalists in the NSF Regional Innovation Engines program.
```
TO:
```
Geoffrey Thün is co-principal investigator of the $115,000 University of Michigan component. In 2023 the NextHouse proposal was named one of 34 semifinalists in the NSF Regional Innovation Engines program.
```
Source: Thün public CV (taubmancollege.umich.edu/wp-content/uploads/2023/02/CV-Geoffrey-Thun.pdf): "U-M Component: $115,000", "U-M Team: [G. Thün, CoPI]". Taubman College, Jun 21, 2023: "the 34 semifinalists selected by the NSF".


## acadia-society-award-for-leadership-2023

### Edit 7: Body

FROM:
```
As President she created the ACADIA Diversity Committee and updated its publication ethics.
```
TO:
```
As President she developed codes of ethics and conduct for the organization.
```
Source: Portico, Nov 17, 2020 (taubmancollege.umich.edu/news/2020/11/17/portico-fall-2020-velikovs-experimental-practice-and-innovative-presidency/): Velikov developed "codes of ethics and conduct". No public source names a Diversity Committee or publication ethics, so that claim is removed.


## from-matter-to-territory-syracuse-2022

### Edit 8: Body

FROM:
```
Velikov has given lectures under the same title at CU Denver (February 2021, with Thün) and as a keynote at Georgia Tech's Divergence in Architectural Research (March 2020).
```
TO:
```
Velikov has given lectures under the same title at CU Denver (February 2021, with Thün) and as a keynote at Georgia Tech's Divergence in Architectural Research Symposium (March 2020).
```
Source: Velikov public CV (Dec 2024): "From Matter to Territory." Public lecture, Syracuse University Lecture Series (2022, November 14); Keynote lecture, Divergence in Architectural Research Symposium, Georgia Tech (March 6, 2020). UCD CAP news: "Lecture by Kathy Velikov and Geoffrey Thün from rvtr on Wednesday February 24th" (2021). Thün public CV: "From Matter to Territory", Fall 2022 Lectures Series, The Syracuse University School of Architecture.

### Edit 9: OutboundLink

FROM:
```
https://soa.syr.edu/live/profiles/1154-kathy-velikov
```
TO:
```
(empty: delete)
```
Source: This page is a faculty profile and does not mention the lecture; its only event listing is an unrelated "Graduate Design Research Lecture: Andrew Saunders". No Syracuse event page for the lecture was found (soa.syr.edu profiles 1154/1155, web search). Leave empty.

### Edit 10: OutboundLabel

FROM:
```
Read at Syracuse Architecture
```
TO:
```
(empty: delete)
```
Source: Remove together with the link so no empty button renders.


## ambiguous-territory-book-2022

### Edit 11: Title

FROM:
```
Ambiguous Territory: Architecture, Landscape, and the Postnatural published by Actar
```
TO:
```
Ambiguous Territory: Architecture, Landscape and the Postnatural published by Actar
```
Source: Actar product page subtitle: "Architecture, Landscape and the Postnatural" (no serial comma); same in Velikov CV.

### Edit 12: Body

FROM:
```
Ambiguous Territory: Architecture, Landscape, and the Postnatural, edited by Cathryn Dwyre, Chris Perry, David Salomon and Kathy Velikov, is published by Actar (256 pages).
```
TO:
```
Ambiguous Territory: Architecture, Landscape and the Postnatural, edited by Cathryn Dwyre, Chris Perry, David Salomon and Kathy Velikov, is published by Actar (256 pages).
```
Source: Actar: editors "Cathryn Dwyre, Chris Perry, David Salomon, Kathy Velikov (eds.)", 256 pages.

### Edit 13: Body

FROM:
```
The book follows the exhibition and symposium of the same name, which assembled more than forty projects by architects, landscape architects and artists whose work challenges the division between the built and the natural environment. The exhibition was shown at Taubman College (2017), the University of Virginia (2018), Pratt Manhattan Gallery (2018–2019) and Ithaca College (2019), each with a public symposium.
```
TO:
```
The book grew out of the exhibition and symposium of the same name at the University of Michigan in 2017, and brings together the work of over forty architects, landscape architects, artists and historians, organized around three territories: the atmospheric, the biologic and the geologic. The exhibition travelled from Taubman College (2017) to the University of Virginia (2018), Pratt Manhattan Gallery (2018–2019) and Ithaca College (2019).
```
Source: Actar: the book "brings together the work of over forty architects, landscape architects, artists, and historians"; organized "around three territories: the atmospheric, the biologic, and the geologic"; emerged from a symposium and exhibition at the University of Michigan in fall 2017. Venues/dates: Velikov public CV (Taubman College Gallery Sept–Oct 2017; UVA Elmaleh Gallery Sept–Oct 2018; Pratt Manhattan Gallery Dec 6 2018 – Feb 15 2019; Ithaca College Handwerker Gallery Aug–Dec 2019). "Each with a public symposium" removed: symposia are documented only at Michigan and UVA. "Challenges the division between the built and the natural" removed: not in Actar text.

### Edit 14: Body

FROM:
```
\nThe book was launched at Rizzoli Bookstore in New York in January 2023. Its print run of 1,500 copies sold out.
```
TO:
```
(empty: delete)
```
Source: CUT: FAIA-submission-only. Not on Actar, not in the public CV, not found by web search. Delete the whole paragraph, including the line break before it.


## Resulting Body text after all edits (for review)

**arid-logics-tulane-prize-2026**

```
Title: Arid Logics studio receives a Tulane Prize Honorable Achievement

Arid Logics: Climate Coexistence in Desert America, the thesis seminar and studio taught by Kathy Velikov at Taubman College, received an Honorable Achievement in the Innovative Studio Pedagogy category of the 2025–2026 Tulane Prize for Climate Change Curriculum in the Built Environment.
The prize is given by the Tulane Center on Climate Change and Urbanism. The studio worked on the Las Vegas Valley.

Outbound Link: https://taubmancollege.umich.edu/news/2026/06/05/jazairy-velikov-receive-honorable-achievements-from-tulane-prize-for-climate-change-curriculum/
Outbound Label: Read at Taubman College
```

**stretch-codes-tad-2025**

```
Title: "Stretch Codes and the Building Envelope" published in TAD 9:1

"Stretch Codes and the Building Envelope", by Kathy Velikov, Kazi Najeeb Hasan, Geoffrey Lewis, Carol C. Menassa, Vineet R. Kamat and Geoffrey Thün, appears in Technology | Architecture + Design (TAD) 9:1, pages 156–171.
The article reviews energy stretch codes in the United States and Canada and their implications for building envelopes and embodied carbon.

Outbound Link: https://css.umich.edu/publications/research-publications/stretch-codes-and-building-envelope
Outbound Label: Read at the Center for Sustainable Systems
```

**kathy-velikov-faia-2025**

```
Title: Kathy Velikov elevated to the AIA College of Fellows

Kathy Velikov, Professor of Architecture and Associate Dean for Research and Creative Practice at Taubman College and a founding partner of RVTR, has been elevated to the American Institute of Architects College of Fellows, a distinction held by less than 3% of the architecture profession.
The fellowship recognizes her for furthering "the science and art of planning and building by advancing the standards of architectural education and training." Her work spans practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments, from responsive architectural material assemblies to territorial practices for decarbonization.
"I am truly honored to be recognized for my work by the AIA and the distinguished jury of peers," Velikov said. The new fellows were honored at AIA25 in Boston, June 4–6, 2025.

Outbound Link: https://taubmancollege.umich.edu/news/2025/02/13/velikov-elevated-to-aias-prestigious-college-of-fellows/
Outbound Label: Read at Taubman College
```

**nexthouse-nsf-engines-2024**

```
Title: NextHouse receives an NSF Engines Development Award

NextHouse, an initiative on next-generation factory-built housing, received a $1 million NSF Engines Development Award from the National Science Foundation. The program is run by the Purdue Applied Research Institute (PARI), with the University of Michigan among its partners.
Geoffrey Thün is co-principal investigator of the $115,000 University of Michigan component. In 2023 the NextHouse proposal was named one of 34 semifinalists in the NSF Regional Innovation Engines program.

Outbound Link: https://www.purdue.edu/research/features/stories/nexthouse-creating-the-next-generation-of-factory-built-housing/
Outbound Label: Read at Purdue
```

**acadia-society-award-for-leadership-2023**

```
Title: Kathy Velikov receives the ACADIA Society Award for Leadership

The Association for Computer Aided Design in Architecture (ACADIA) gave Kathy Velikov its 2023 Society Award for Leadership, for "extraordinary contributions and service to the ACADIA community". The jury citation states: "This award recognizes the significant role that Kathy Velikov has played in ACADIA's leadership."
Velikov was President of ACADIA from 2018 to 2020 and Vice President from 2021 to 2022. As President she developed codes of ethics and conduct for the organization. She was Technical Co-Chair of ACADIA 2016, Posthuman Frontiers, at the University of Michigan.
She gave the award talk, "Cultivating a Community of Practice", on October 26, 2023.

Outbound Link: https://taubmancollege.umich.edu/news/2023/08/03/kathy-velikov-recognized-with-acadia-society-award-for-leadership
Outbound Label: Read at Taubman College
```

**from-matter-to-territory-syracuse-2022**

```
Title: From Matter to Territory: lecture at Syracuse University

Kathy Velikov and Geoffrey Thün gave the lecture "From Matter to Territory" at the Syracuse University School of Architecture.
Velikov has given lectures under the same title at CU Denver (February 2021, with Thün) and as a keynote at Georgia Tech's Divergence in Architectural Research Symposium (March 2020).

Outbound Link: (empty)
Outbound Label: (empty)
```

**ambiguous-territory-book-2022**

```
Title: Ambiguous Territory: Architecture, Landscape and the Postnatural published by Actar

Ambiguous Territory: Architecture, Landscape and the Postnatural, edited by Cathryn Dwyre, Chris Perry, David Salomon and Kathy Velikov, is published by Actar (256 pages). It has a foreword by Catherine Ingraham and an afterword by Peder Anker.
The book grew out of the exhibition and symposium of the same name at the University of Michigan in 2017, and brings together the work of over forty architects, landscape architects, artists and historians, organized around three territories: the atmospheric, the biologic and the geologic. The exhibition travelled from Taubman College (2017) to the University of Virginia (2018), Pratt Manhattan Gallery (2018–2019) and Ithaca College (2019).

Outbound Link: https://actar.com/product/ambiguous-territory/
Outbound Label: Read at Actar
```


## Notes

- **Syracuse date.** The two public CVs disagree. Velikov's CV gives 2022, November 14 (kept). Thün's CV gives November 10, 2022. Velikov's CV matches the CU Denver press page exactly (Feb 24, 2021); Thün's CV gives Feb 27 for that talk. So Nov 14 is the better-supported date.

- **NextHouse date.** The item's June 4, 2024 is the date of the Purdue story. The NSF award itself started March 1, 2024. No change is needed for a news date.
