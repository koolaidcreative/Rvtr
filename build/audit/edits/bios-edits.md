# Director bios: exact edit list

Prepared 2026-10-12 from the fact-check in `bios-factcheck.md`.

**The policy behind these edits (from Sasha).** Every fact must trace to one of:
- rvtr.com;
- a published press release or other public page (the public CV PDFs count);
- @rvtrarchitecture on Instagram.

Claims that rest only on Kathy's private FAIA submission are removed, and the sentences around them are rewritten so they still read well.

## How to apply

**Two places.** Each fact lives in two places, and both must be edited:
1. **The CMS Team item.** These are the fields `Bio`, `Appointments`, `Visiting`, `Leadership` and `Honours`.
2. **The "Read full bio" component.** These are the Framer components **"Kathy Velikov"** and **"Geoffrey Thün"**, layer `Bio/<Name>/Collapsed/Answer`.
   - It repeats Bio paragraphs 2 and 3 (Geoff: 2 to 4), followed by the four lists under their headings.
   - It uses curly quotes and apostrophes (’ “ ”).
   - It puts a non-breaking space (U+00A0) before the last word of each paragraph.
   - The component FROM and TO below already include these characters, so copy them from the code blocks exactly.

**Paragraph 1.** Bio paragraph 1 also appears on the `/team` page spread, but no edit touches paragraph 1.

**Checks.** Every FROM string was matched exactly once against the site export (`site-export/*.json`). After the edits, the component text was checked again against its CMS fields, and they still match.

There are full replacement texts in an appendix, for anyone who would rather paste whole fields.

## Kathy Velikov

### Edit 1: `Bio`

**Why:** Policy: the old framing paraphrased the FAIA submission. The new wording follows her Taubman profile (https://taubmancollege.umich.edu/faculty/directory/kathy-velikov/) and the FAIA news item (https://taubmancollege.umich.edu/news/2025/02/13/velikov-elevated-to-aias-prestigious-college-of-fellows/).

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
Her work is practice-based design research, in which new knowledge comes from design propositions and prototypes, developed through speculation, prototyping and visualization. At the material scale she prototypes building skins that integrate environmental sensing, kinetic action and responsiveness. At the territorial scale she uses urban analysis to build scenarios for decarbonized futures and new social infrastructures.
```
TO
```text
Her work is practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments. Developed through speculation, prototyping and visualization, it spans three strands: responsive architectural material assemblies, resilient multifunctional urban infrastructures, and territorial practices for decarbonization.
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 2: `Bio`

**Why:** Wording: rvtr.com credits her as Co-PI (Thün and Wes McGee were lead PIs): https://www.rvtr.com/projects/resonant-chamber

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
; co-led Resonant Chamber, a rigid-origami acoustic envelope
```
TO
```text
; was co-principal investigator for Resonant Chamber, a rigid-origami acoustic envelope
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 3: `Bio`

**Why:** Policy: the publication counts appear only in the FAIA submission. Paragraph 2 now ends "…SSHRC, Ford and Guardian Industries."

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
 She has published two books, more than twenty book chapters, thirty journal articles and forty conference papers.
```
TO
*(nothing: delete the FROM text)*
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Curly quotes and/or a non-breaking space differ from Location A.

FROM
```text
 She has published two books, more than twenty book chapters, thirty journal articles and forty conference papers.
```
TO
*(nothing: delete the FROM text)*

### Edit 4: `Bio`

**Why:** Policy: the Diversity Committee and publication ethics appear only in the FAIA submission. The new wording is from Portico 2020: https://taubmancollege.umich.edu/news/2020/11/17/portico-fall-2020-velikovs-experimental-practice-and-innovative-presidency/

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
As President she created the ACADIA Diversity Committee and updated its publication ethics.
```
TO
```text
As President she developed codes of ethics and conduct for the organization.
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 5: `Bio`

**Why:** Policy: the guest-critic list appears only in the FAIA submission. Realities and Realms 2016 stays; it is public at https://taubmancollege.umich.edu/news/2016/11/23/velikov-presents-at-realities-and-realms/ and is also in KV-CV.

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
and Visiting Professor at Ryerson University in 2010, and is an invited guest critic at schools including Harvard GSD, Princeton, MIT and The Bartlett; in 2016 she spoke at the Realities and Realms Symposium at Harvard GSD.
```
TO
```text
and Visiting Professor at Ryerson University in 2010, and in 2016 she presented at the Realities and Realms Symposium at Harvard GSD.
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 6: `Bio`

**Why:** Policy: both numbers appear only in the FAIA submission.

**Location A**: CMS Team item `kathy-velikov`, field `Bio`

FROM
```text
 She has taught more than 800 architecture students and employed more than 60 graduate research assistants.
```
TO
*(nothing: delete the FROM text)*
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 7: `Appointments`

**Why:** Policy: the split into "research lab 2017–" and "RVTR Inc 2007–2017" appears only in the FAIA submission. The public KV-CV reads "2007-present RVTR, Ann Arbor and Toronto: Partner and Director".

**Location A**: CMS Team item `kathy-velikov`, field `Appointments`

FROM
```text
Director, RVTR (research lab), Ann Arbor, 2017–
Founding Partner and Director, RVTR Inc, Ann Arbor and Toronto, 2007–2017
```
TO
```text
Partner and Director, RVTR, Ann Arbor and Toronto, 2007–
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 8: `Visiting`

**Why:** Policy: both lines appear only in the FAIA submission. KV-CV lists a 2022 Syracuse lecture, not a workshop.

**Location A**: CMS Team item `kathy-velikov`, field `Visiting`

FROM (delete these whole lines, including their line breaks)
```text
Program Advisory Board, Florida Atlantic University School of Architecture, 2023–
Design Research Workshop, M.Arch, Syracuse University, 2022
```
TO
*(nothing: the line or lines are removed)*
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Delete the same whole lines; they are identical there.

### Edit 9: `Visiting`

**Why:** Policy: the guest-critic list appears only in the FAIA submission.

**Location A**: CMS Team item `kathy-velikov`, field `Visiting`

FROM (delete these whole lines, including their line breaks)
```text
Invited guest critic: Harvard GSD, Princeton, MIT, The Bartlett, Carnegie Mellon, Cornell Tech, University of Pennsylvania Weitzman, University of Virginia, University of Chicago, among others
```
TO
*(nothing: the line or lines are removed)*
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Delete the same whole lines; they are identical there.

### Edit 10: `Leadership`

**Why:** Policy: replaced with the Portico 2020 wording (URL above).

**Location A**: CMS Team item `kathy-velikov`, field `Leadership`

FROM
```text
Founder of the ACADIA Diversity Committee
```
TO
```text
Developed ACADIA's codes of ethics and conduct as President
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Curly quotes and/or a non-breaking space differ from Location A.

FROM
```text
Founder of the ACADIA Diversity Committee
```
TO
```text
Developed ACADIA’s codes of ethics and conduct as President
```

### Edit 11: `Leadership`

**Why:** WRONG fix: she moderated, and per KV-CV co-organized, the workshop, not the Forum. Sources: https://taubmancollege.umich.edu/news/2016/04/04/taubman-college-partners-with-lafargeholcim-forum-on-sustainable-construction-in-detroit/ and https://www.holcimfoundation.org/experts/kathy-velikov

**Location A**: CMS Team item `kathy-velikov`, field `Leadership`

FROM
```text
Co-organizer, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
```
TO
```text
Co-organizer and moderator (with Geoffrey Thün), "Territorial Scale" workshop, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Curly quotes and/or a non-breaking space differ from Location A.

FROM
```text
Co-organizer, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
```
TO
```text
Co-organizer and moderator (with Geoffrey Thün), “Territorial Scale” workshop, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
```

### Edit 12: `Leadership`

**Why:** Policy: the peer-review and jury service appears only in the FAIA submission. KV-CV lists neither.

**Location A**: CMS Team item `kathy-velikov`, field `Leadership`

FROM (delete these whole lines, including their line breaks)
```text
Peer reviewer for IJAC, JAE, Architectural Science Review, ACADIA and FABRICATE; juror, eVolo Skyscraper Competition and ACSA Steel Design Competition
```
TO
*(nothing: the line or lines are removed)*
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Delete the same whole lines; they are identical there.

### Edit 13: `Honours`

**Why:** WRONG fix (award name): https://taubmancollege.umich.edu/news/2020/03/06/acsa-honors-publication-by-junghans-velikov-and-thun/

**Location A**: CMS Team item `kathy-velikov`, field `Honours`

FROM
```text
2020 TAD Award for Research Contribution, "Climate Measures"
```
TO
```text
2020 TAD Research Contribution Award (inaugural), "Climate Measures"
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Curly quotes and/or a non-breaking space differ from Location A.

FROM
```text
2020 TAD Award for Research Contribution, “Climate Measures”
```
TO
```text
2020 TAD Research Contribution Award (inaugural), “Climate Measures”
```

### Edit 14: `Honours`

**Why:** Wording: RAIC lists the category as "Innovation in Architecture" (https://raic.org/node/101759). This now matches Geoff's line.

**Location A**: CMS Team item `kathy-velikov`, field `Honours`

FROM
```text
2011 RAIC Award of Excellence for Innovation in the Practice of Architecture, North House
```
TO
```text
2011 RAIC Award of Excellence, Innovation in Architecture, North House
```
**Location B**: component "Kathy Velikov" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

## Geoffrey Thün

### Edit 15: `Bio`

**Why:** Addition: Google Patents, US9260863B2, granted 2016-02-16. Inventors: Geoffrey Thun, Elizabeth Sauve, Raj Patel, Terence Caulkins, David Rife. https://patents.google.com/patent/US9260863B2/en

**Location A**: CMS Team item `geoffrey-thun`, field `Bio`

FROM
```text
and co-led The Stratus Project and Resonant Chamber, two prototypes of responsive interior envelopes.
```
TO
```text
and co-led The Stratus Project and Resonant Chamber, two prototypes of responsive interior envelopes. He is the first-named inventor on U.S. Patent 9,260,863 (2016) for the acoustic envelope system developed through Resonant Chamber.
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 16: `Bio`

**Why:** WRONG fix: M-NEX is an international consortium led by Keio University and Qatar University; Thün is listed as the U-M partner. Sources: https://belmontforum.org/projects/the-moveable-nexus-design-led-urban-food-water-and-energy-management-innovation-in-new-boundary-conditions-of-change and GT-CV (U-M team PI). The Detroit workshop is from m-nex.net ("M-NEX Detroit Design Workshop", 2019).

**Location A**: CMS Team item `geoffrey-thun`, field `Bio`

FROM
```text
He was principal investigator for M-NEX, a Detroit project funded in 2018 through the Belmont Forum's SUGI Food-Water-Energy Nexus program, and is co-principal investigator for the University of Michigan component of NextHouse,
```
TO
```text
He was principal investigator for the University of Michigan team in M-NEX (The Moveable Nexus), an international project funded in 2018 through the Belmont Forum's SUGI Food-Water-Energy Nexus program that held a design workshop in Detroit. He is also co-principal investigator for the University of Michigan component of NextHouse,
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Curly quotes and/or a non-breaking space differ from Location A.

FROM
```text
He was principal investigator for M-NEX, a Detroit project funded in 2018 through the Belmont Forum’s SUGI Food-Water-Energy Nexus program, and is co-principal investigator for the University of Michigan component of NextHouse,
```
TO
```text
He was principal investigator for the University of Michigan team in M-NEX (The Moveable Nexus), an international project funded in 2018 through the Belmont Forum’s SUGI Food-Water-Energy Nexus program that held a design workshop in Detroit. He is also co-principal investigator for the University of Michigan component of NextHouse,
```

### Edit 17: `Bio`

**Why:** Wording: Taubman's 2015 announcement says he "will serve as Chair of the conference": https://taubmancollege.umich.edu/news/2015/11/12/taubman-college-to-host-2016-acadia-conference/

**Location A**: CMS Team item `geoffrey-thun`, field `Bio`

FROM
```text
He co-organized ACADIA 2016, Posthuman Frontiers, at the University of Michigan,
```
TO
```text
He chaired ACADIA 2016, Posthuman Frontiers, hosted at the University of Michigan,
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 18: `Bio`

**Why:** Wording: RAIC category name (https://raic.org/node/101759).

**Location A**: CMS Team item `geoffrey-thun`, field `Bio`

FROM
```text
the 2011 RAIC Award of Excellence for Innovation,
```
TO
```text
the 2011 RAIC Award of Excellence for Innovation in Architecture,
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 19: `Leadership`

**Why:** Wording: same source as the Bio change.

**Location A**: CMS Team item `geoffrey-thun`, field `Leadership`

FROM
```text
Co-organizer, ACADIA 2016, Posthuman Frontiers, University of Michigan;
```
TO
```text
Conference Chair, ACADIA 2016, Posthuman Frontiers, University of Michigan;
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 20: `Leadership`

**Why:** WRONG fix: see the Bio change.

**Location A**: CMS Team item `geoffrey-thun`, field `Leadership`

FROM
```text
Principal investigator, M-NEX, Belmont Forum SUGI Food-Water-Energy Nexus, 2018
```
TO
```text
Principal investigator, University of Michigan team, M-NEX (The Moveable Nexus), Belmont Forum SUGI Food-Water-Energy Nexus, 2018
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

### Edit 21: `Honours`

**Why:** Wording: now matches Kathy's line.

**Location A**: CMS Team item `geoffrey-thun`, field `Honours`

FROM
```text
2011 RAIC Award of Excellence for Innovation in Architecture, North House
```
TO
```text
2011 RAIC Award of Excellence, Innovation in Architecture, North House
```
**Location B**: component "Geoffrey Thün" (Read full bio, `Answer` layer). Same FROM and TO as Location A.

## /team page

### Edit 22: "Our History" description text

**Why:** the 2016 recognition was an Honorable Mention, not an R+D Award. Source: https://taubmancollege.umich.edu/news/2016/07/18/mcgee-thun-velikov-win-honorable-mention-in-2016-architect-magazine-rd-awards/

**Location**: `/team` page, text layer `Description`, path `Description/Container/Content`. Applies on all breakpoints; there are no tablet or phone overrides.

FROM
```text
Designers (2008) and Architect magazine R+D Awards in 2010 and 2016.
```
TO
```text
Designers (2008), an Architect magazine R+D Award (2010) and an R+D Honorable Mention (2016).
```

## Optional: list headings in the "Read full bio" components

These headings are static text inside each component. They are not CMS fields.

**Kathy.** Once the guest-critic line is removed, nothing under the heading is a "review".
- FROM `Visiting, examining and reviews`
- TO `Visiting, examining and talks`

**Geoff.** His list has only visiting posts.
- FROM `Visiting, examining and reviews`
- TO `Visiting positions`

If you change a heading, change it only in the component. The appendix keeps the current headings.

---

## Appendix: full replacement text after all edits

### Kathy Velikov: CMS item `kathy-velikov`

`Bio`
```text
Kathy Velikov is an architect, researcher and educator, and a director of RVTR, the research lab she co-founded in Toronto in 2007 with Geoffrey Thün, Colin Ripley and Paul Raff. She is Professor of Architecture and Associate Dean for Research and Creative Practice at Taubman College of Architecture and Urban Planning, University of Michigan, and directs the Institute for Advanced Construction Futures, a University of Michigan Impact Institute funded in January 2026 to advance low-carbon construction. She is licensed in Michigan and Ontario. In 2025 she was elevated to the College of Fellows of the American Institute of Architects.
Her work is practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments. Developed through speculation, prototyping and visualization, it spans three strands: responsive architectural material assemblies, resilient multifunctional urban infrastructures, and territorial practices for decarbonization. With RVTR she was architect of record for North House, the solar-powered prototype for northern climates built for the 2009 U.S. Department of Energy Solar Decathlon; was co-principal investigator for Resonant Chamber, a rigid-origami acoustic envelope that received a U.S. patent in 2016; and co-authored Infra Eco Logi Urbanism: A Project for the Great Lakes Megaregion (Park Books, 2015). RVTR was part of the EXTRACTION team at the Canadian Pavilion, 2016 Venice Architecture Biennale. Her research has been funded by NSF, the National Fish and Wildlife Foundation, the U.S. Department of Transportation, SSHRC, Ford and Guardian Industries.
She was President of ACADIA, the Association for Computer Aided Design in Architecture, from 2018 to 2020 and Vice President from 2021 to 2022. As President she developed codes of ethics and conduct for the organization. She was Technical Co-Chair of ACADIA 2016, Posthuman Frontiers, hosted at the University of Michigan, and co-edited its proceedings. Since 2022 she has been External Examiner for the MArch Architectural Design (B-Pro) program at The Bartlett, UCL. She was Visiting Guest Professor at California College of the Arts in 2013 and Visiting Professor at Ryerson University in 2010, and in 2016 she presented at the Realities and Realms Symposium at Harvard GSD. She co-edited Ambiguous Territory: Architecture, Landscape, and the Postnatural (Actar, 2022) and co-curated its exhibition, shown at four galleries from 2017 to 2019.
At Taubman College she teaches thesis and design studios and seminars in ecology and technology. Her housing studio received the 2020 AIA/ACSA Housing Design Education Award, and in 2023 ACADIA gave her its Society Award for Leadership. She holds a B.ES and a B.Arch from the University of Waterloo and an MA in History of Art and Architecture from the University of Toronto.
```

`Appointments`
```text
Professor of Architecture, Taubman College, University of Michigan, 2021–
Associate Dean for Research and Creative Practice, Taubman College, 2021–
Director, Institute for Advanced Construction Futures, University of Michigan, 2026–
Partner and Director, RVTR, Ann Arbor and Toronto, 2007–
Associate Professor, Taubman College, 2015–2021; Assistant Professor, 2009–2015
Assistant Professor, University of Waterloo, 2007–2009
Willard A. Oberdick Fellow, Taubman College, 2006–2007
Licensed architect: Michigan (since 2012), Ontario (since 2002)
```

`Visiting`
```text
External Examiner, MArch Architectural Design (B-Pro), The Bartlett, UCL, 2022–
Visiting Guest Professor, Summer Studio, California College of the Arts, 2013
Visiting Professor, MArch Summer Studio, Ryerson University (now Toronto Metropolitan University), 2010
Speaker, Realities and Realms Symposium, Harvard GSD, 2016
```

`Leadership`
```text
ACADIA: Board of Directors, 2016–2017; President, 2018–2020; Vice President, 2021–2022
Developed ACADIA's codes of ethics and conduct as President
Technical Co-Chair, ACADIA 2016, Posthuman Frontiers, University of Michigan; co-editor of the proceedings and projects catalog
Co-organizer and moderator (with Geoffrey Thün), "Territorial Scale" workshop, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
Co-curator, Ambiguous Territory, exhibition and symposium, 2017–2019; co-editor of the book, Actar, 2022
Fellow, Big Ten Academic Alliance Academic Leadership Program, 2022–2023
```

`Honours`
```text
2026 Tulane Prize Honorable Achievement, Innovative Studio Pedagogy, studio Arid Logics
2025 Fellow, American Institute of Architects (FAIA)
2023 ACADIA Society Award for Leadership
2020 AIA/ACSA Housing Design Education Award, studio New Domesticities New Collectivities
2020 TAD Research Contribution Award (inaugural), "Climate Measures"
2017 AZ Award, Social Good, EXTRACTION (with OPSYS)
2017 CSLA National Award of Excellence, EXTRACTION
2016 Architect R+D Awards, Honorable Mention, Infundibuliforms
2013 Architizer A+ Awards, Architecture + Sound, Jury Award and Popular Choice Award, Resonant Chamber
2013 JAE Best Design as Scholarship Article Award, "Thick Air"
2012 ACSA Faculty Design Award, The Stratus Project
2011 RAIC Award of Excellence, Innovation in Architecture, North House
2010 Architect R+D Award of Excellence, North House
2010 OAA Design Excellence Award, North House
2009 Professional Prix de Rome in Architecture, Canada Council for the Arts (RVTR)
2008 Young Architects Forum Award, Architectural League of New York
```

### Kathy Velikov: component "Kathy Velikov", `Answer` layer (whole text)

```text
Her work is practice-based design research toward environmentally responsive, technologically enabled and climate-positive built environments. Developed through speculation, prototyping and visualization, it spans three strands: responsive architectural material assemblies, resilient multifunctional urban infrastructures, and territorial practices for decarbonization. With RVTR she was architect of record for North House, the solar-powered prototype for northern climates built for the 2009 U.S. Department of Energy Solar Decathlon; was co-principal investigator for Resonant Chamber, a rigid-origami acoustic envelope that received a U.S. patent in 2016; and co-authored Infra Eco Logi Urbanism: A Project for the Great Lakes Megaregion (Park Books, 2015). RVTR was part of the EXTRACTION team at the Canadian Pavilion, 2016 Venice Architecture Biennale. Her research has been funded by NSF, the National Fish and Wildlife Foundation, the U.S. Department of Transportation, SSHRC, Ford and Guardian Industries.
She was President of ACADIA, the Association for Computer Aided Design in Architecture, from 2018 to 2020 and Vice President from 2021 to 2022. As President she developed codes of ethics and conduct for the organization. She was Technical Co-Chair of ACADIA 2016, Posthuman Frontiers, hosted at the University of Michigan, and co-edited its proceedings. Since 2022 she has been External Examiner for the MArch Architectural Design (B-Pro) program at The Bartlett, UCL. She was Visiting Guest Professor at California College of the Arts in 2013 and Visiting Professor at Ryerson University in 2010, and in 2016 she presented at the Realities and Realms Symposium at Harvard GSD. She co-edited Ambiguous Territory: Architecture, Landscape, and the Postnatural (Actar, 2022) and co-curated its exhibition, shown at four galleries from 2017 to 2019.
At Taubman College she teaches thesis and design studios and seminars in ecology and technology. Her housing studio received the 2020 AIA/ACSA Housing Design Education Award, and in 2023 ACADIA gave her its Society Award for Leadership. She holds a B.ES and a B.Arch from the University of Waterloo and an MA in History of Art and Architecture from the University of Toronto.
Appointments
Professor of Architecture, Taubman College, University of Michigan, 2021–
Associate Dean for Research and Creative Practice, Taubman College, 2021–
Director, Institute for Advanced Construction Futures, University of Michigan, 2026–
Partner and Director, RVTR, Ann Arbor and Toronto, 2007–
Associate Professor, Taubman College, 2015–2021; Assistant Professor, 2009–2015
Assistant Professor, University of Waterloo, 2007–2009
Willard A. Oberdick Fellow, Taubman College, 2006–2007
Licensed architect: Michigan (since 2012), Ontario (since 2002)
Visiting, examining and reviews
External Examiner, MArch Architectural Design (B-Pro), The Bartlett, UCL, 2022–
Visiting Guest Professor, Summer Studio, California College of the Arts, 2013
Visiting Professor, MArch Summer Studio, Ryerson University (now Toronto Metropolitan University), 2010
Speaker, Realities and Realms Symposium, Harvard GSD, 2016
Leadership and service
ACADIA: Board of Directors, 2016–2017; President, 2018–2020; Vice President, 2021–2022
Developed ACADIA’s codes of ethics and conduct as President
Technical Co-Chair, ACADIA 2016, Posthuman Frontiers, University of Michigan; co-editor of the proceedings and projects catalog
Co-organizer and moderator (with Geoffrey Thün), “Territorial Scale” workshop, LafargeHolcim Foundation 5th International Forum, Infrastructure Space, Detroit, 2016
Co-curator, Ambiguous Territory, exhibition and symposium, 2017–2019; co-editor of the book, Actar, 2022
Fellow, Big Ten Academic Alliance Academic Leadership Program, 2022–2023
Selected honors
2026 Tulane Prize Honorable Achievement, Innovative Studio Pedagogy, studio Arid Logics
2025 Fellow, American Institute of Architects (FAIA)
2023 ACADIA Society Award for Leadership
2020 AIA/ACSA Housing Design Education Award, studio New Domesticities New Collectivities
2020 TAD Research Contribution Award (inaugural), “Climate Measures”
2017 AZ Award, Social Good, EXTRACTION (with OPSYS)
2017 CSLA National Award of Excellence, EXTRACTION
2016 Architect R+D Awards, Honorable Mention, Infundibuliforms
2013 Architizer A+ Awards, Architecture + Sound, Jury Award and Popular Choice Award, Resonant Chamber
2013 JAE Best Design as Scholarship Article Award, “Thick Air”
2012 ACSA Faculty Design Award, The Stratus Project
2011 RAIC Award of Excellence, Innovation in Architecture, North House
2010 Architect R+D Award of Excellence, North House
2010 OAA Design Excellence Award, North House
2009 Professional Prix de Rome in Architecture, Canada Council for the Arts (RVTR)
2008 Young Architects Forum Award, Architectural League of New York
```

### Geoffrey Thün: CMS item `geoffrey-thun`

`Bio`
```text
Geoffrey Thün is a designer, researcher and educator, and a director of RVTR, which he co-founded in Toronto in 2007 with Kathy Velikov, Colin Ripley and Paul Raff; he leads the lab's design research. He is Professor of Architecture at Taubman College of Architecture and Urban Planning and Associate Vice President for Research: Social Sciences, Humanities, and the Arts at the University of Michigan, where he is the research office's liaison to those units. He is also co-director of the university's Urban Collaboratory.
His research applies complex-systems approaches across scales: regional territories and city planning, high-performance buildings, and full-scale prototypes of responsive, kinetic building envelopes. He was faculty lead and principal investigator for North House, the Team North entry to the 2009 U.S. Department of Energy Solar Decathlon, and co-led The Stratus Project and Resonant Chamber, two prototypes of responsive interior envelopes. He is the first-named inventor on U.S. Patent 9,260,863 (2016) for the acoustic envelope system developed through Resonant Chamber. With Kathy Velikov and Colin Ripley he developed Conduit Urbanism and Infra Eco Logi Urbanism, design research on the Great Lakes Megaregion published by Park Books in 2015 and exhibited in Montreal, Toronto, New Haven, Ann Arbor and Knoxville. He was principal investigator for the University of Michigan team in M-NEX (The Moveable Nexus), an international project funded in 2018 through the Belmont Forum's SUGI Food-Water-Energy Nexus program that held a design workshop in Detroit. He is also co-principal investigator for the University of Michigan component of NextHouse, the Purdue-led factory-built housing initiative that received a National Science Foundation Engines Development Award in 2024. In 2024 he gave the keynote "Responsive Envelopes: Paradigms and Potentials" at the Facade Tectonics World Congress.
At Taubman College he was Associate Dean for Research and Creative Practice from 2014 to 2020 and Senior Associate Dean from 2020 to 2021. He chaired ACADIA 2016, Posthuman Frontiers, hosted at the University of Michigan, co-edited its proceedings and catalog, and co-designed its exhibition with Matias del Campo. With Dan McTavish he planned and designed the display for New Brutalist Image 1949–55 at Tate Britain (2014–2015). He taught at the University of Waterloo from 2006 to 2009, was Adjunct Associate Professor at Ryerson University from 2011 to 2015, and has held visiting positions at California College of the Arts, Université du Québec à Montréal, Dalhousie University, Keio University and the International Solar University in Switzerland. He teaches design studios and courses on urban systems, site operations and material systems.
He shared in RVTR's recognition, including the 2009 Professional Prix de Rome in Architecture, the 2010 Architect R+D Award of Excellence and the 2011 RAIC Award of Excellence for Innovation in Architecture, and received the University of Waterloo Outstanding Faculty Researcher Award in 2008. Before RVTR he worked at Dereck Revington Studio and at Baird Sampson Neuert Architects, where he was central to the French River Visitor Centre. He holds a B.A. in Sociology from the University of Western Ontario, a B.ES and a B.Arch from the University of Waterloo, and a Master of Urban Design from the University of Toronto.
```

`Appointments`: unchanged.

`Visiting`: unchanged.

`Leadership`
```text
Conference Chair, ACADIA 2016, Posthuman Frontiers, University of Michigan; co-editor of the proceedings and catalog; exhibition co-designer with Matias del Campo
Principal investigator, University of Michigan team, M-NEX (The Moveable Nexus), Belmont Forum SUGI Food-Water-Energy Nexus, 2018
Faculty lead and principal investigator, North House, Team North, 2009 Solar Decathlon
Moderator, "Territorial Scale" workshop, LafargeHolcim Foundation 5th International Forum, Detroit, 2016
Co-founder, Metropolitan Futures Group, University of Michigan
Spatial planning and display design with Dan McTavish, New Brutalist Image 1949–55, Tate Britain, 2014–2015
Keynote, Facade Tectonics 2024 World Congress
```

`Honours`
```text
2017 AZ Award, Social Good, EXTRACTION
2016 Architect R+D Awards, Honorable Mention, Infundibuliforms
2013 Architizer A+ Awards, Architecture + Sound, Jury Award and Popular Choice Award, Resonant Chamber
2013 JAE Best Design as Scholarship Article Award, "Thick Air"
2012 ACSA Faculty Design Award, The Stratus Project
2011 RAIC Award of Excellence, Innovation in Architecture, North House
2010 Architect R+D Award of Excellence, North House
2009 Professional Prix de Rome in Architecture, Canada Council for the Arts (RVTR)
2008 University of Waterloo Outstanding Faculty Researcher Award
2008 Young Architects Forum Award, Architectural League of New York
```

### Geoffrey Thün: component "Geoffrey Thün", `Answer` layer (whole text)

```text
His research applies complex-systems approaches across scales: regional territories and city planning, high-performance buildings, and full-scale prototypes of responsive, kinetic building envelopes. He was faculty lead and principal investigator for North House, the Team North entry to the 2009 U.S. Department of Energy Solar Decathlon, and co-led The Stratus Project and Resonant Chamber, two prototypes of responsive interior envelopes. He is the first-named inventor on U.S. Patent 9,260,863 (2016) for the acoustic envelope system developed through Resonant Chamber. With Kathy Velikov and Colin Ripley he developed Conduit Urbanism and Infra Eco Logi Urbanism, design research on the Great Lakes Megaregion published by Park Books in 2015 and exhibited in Montreal, Toronto, New Haven, Ann Arbor and Knoxville. He was principal investigator for the University of Michigan team in M-NEX (The Moveable Nexus), an international project funded in 2018 through the Belmont Forum’s SUGI Food-Water-Energy Nexus program that held a design workshop in Detroit. He is also co-principal investigator for the University of Michigan component of NextHouse, the Purdue-led factory-built housing initiative that received a National Science Foundation Engines Development Award in 2024. In 2024 he gave the keynote “Responsive Envelopes: Paradigms and Potentials” at the Facade Tectonics World Congress.
At Taubman College he was Associate Dean for Research and Creative Practice from 2014 to 2020 and Senior Associate Dean from 2020 to 2021. He chaired ACADIA 2016, Posthuman Frontiers, hosted at the University of Michigan, co-edited its proceedings and catalog, and co-designed its exhibition with Matias del Campo. With Dan McTavish he planned and designed the display for New Brutalist Image 1949–55 at Tate Britain (2014–2015). He taught at the University of Waterloo from 2006 to 2009, was Adjunct Associate Professor at Ryerson University from 2011 to 2015, and has held visiting positions at California College of the Arts, Université du Québec à Montréal, Dalhousie University, Keio University and the International Solar University in Switzerland. He teaches design studios and courses on urban systems, site operations and material systems.
He shared in RVTR’s recognition, including the 2009 Professional Prix de Rome in Architecture, the 2010 Architect R+D Award of Excellence and the 2011 RAIC Award of Excellence for Innovation in Architecture, and received the University of Waterloo Outstanding Faculty Researcher Award in 2008. Before RVTR he worked at Dereck Revington Studio and at Baird Sampson Neuert Architects, where he was central to the French River Visitor Centre. He holds a B.A. in Sociology from the University of Western Ontario, a B.ES and a B.Arch from the University of Waterloo, and a Master of Urban Design from the University of Toronto.
Appointments
Professor of Architecture, Taubman College, University of Michigan, 2020–
Associate Vice President for Research: Social Sciences, Humanities, and the Arts, University of Michigan, 2021–
Director of Design Research, RVTR, 2007–
Co-director, Urban Collaboratory, University of Michigan
Senior Associate Dean for Research and Creative Practice, Taubman College, 2020–2021
Associate Dean for Research and Creative Practice, Taubman College, 2014–2020
Associate Professor, Taubman College, 2009–2020
Assistant Professor, University of Waterloo, 2006–2009
Adjunct Associate Professor, Ryerson University, 2011–2015
LEED AP since 2004
Visiting, examining and reviews
Keio University (online), 2021
Adjunct and external reader, Dalhousie University, 2012–2017
California College of the Arts, Summer 2013
Université du Québec à Montréal, Winter 2013
International Solar University, Falera, Switzerland, Summer 2011
Ryerson University, Summer 2010
Leadership and service
Conference Chair, ACADIA 2016, Posthuman Frontiers, University of Michigan; co-editor of the proceedings and catalog; exhibition co-designer with Matias del Campo
Principal investigator, University of Michigan team, M-NEX (The Moveable Nexus), Belmont Forum SUGI Food-Water-Energy Nexus, 2018
Faculty lead and principal investigator, North House, Team North, 2009 Solar Decathlon
Moderator, “Territorial Scale” workshop, LafargeHolcim Foundation 5th International Forum, Detroit, 2016
Co-founder, Metropolitan Futures Group, University of Michigan
Spatial planning and display design with Dan McTavish, New Brutalist Image 1949–55, Tate Britain, 2014–2015
Keynote, Facade Tectonics 2024 World Congress
Selected honors
2017 AZ Award, Social Good, EXTRACTION
2016 Architect R+D Awards, Honorable Mention, Infundibuliforms
2013 Architizer A+ Awards, Architecture + Sound, Jury Award and Popular Choice Award, Resonant Chamber
2013 JAE Best Design as Scholarship Article Award, “Thick Air”
2012 ACSA Faculty Design Award, The Stratus Project
2011 RAIC Award of Excellence, Innovation in Architecture, North House
2010 Architect R+D Award of Excellence, North House
2009 Professional Prix de Rome in Architecture, Canada Council for the Arts (RVTR)
2008 University of Waterloo Outstanding Faculty Researcher Award
2008 Young Architects Forum Award, Architectural League of New York
```

### /team page, `Description` layer (whole text)
```text
The lab’s work has received the Architectural League Prize for Young Architects + Designers (2008), an Architect magazine R+D Award (2010) and an R+D Honorable Mention (2016). In 2016 RVTR represented Canada at the Venice Architecture Biennale as part of EXTRACTION, led by curator Pierre Bélanger.
```

---

## Removed because only in Kathy's FAIA submission

Each item below was taken off the site because its only source is Kathy's FAIA submission. If Kathy wants any of them back, a public source is needed. That can be:
- a line in her public CV on taubmancollege.umich.edu;
- a news item or press release;
- an rvtr.com page;
- an Instagram post.

Once she supplies or approves one, the original wording can be restored from the FROM texts above.

- **Publication counts.** "Two books, more than twenty book chapters, thirty journal articles and forty conference papers."
- **Teaching numbers.** "Taught more than 800 architecture students."
- **Research assistants.** "Employed more than 60 graduate research assistants."
- **Guest-critic schools.** Harvard GSD, Princeton, MIT, The Bartlett, Carnegie Mellon, Cornell Tech, Penn Weitzman, University of Virginia and University of Chicago.
  - The Harvard GSD symposium talk, Realities and Realms 2016, **stays**, because it is public.
- **ACADIA Diversity Committee.** That she created it, and that she updated ACADIA's publication ethics.
  - This is replaced with the public wording "developed codes of ethics and conduct", from Taubman's Portico, 2020.
- **Florida Atlantic University.** Program Advisory Board, School of Architecture, 2023 to present.
- **Syracuse.** Design Research Workshop, M.Arch, Syracuse University, 2022.
  - Her public CV lists only a 2022 Syracuse lecture, "From Matter to Territory". That lecture could be added instead if she likes.
- **Peer review.** Peer reviewer for IJAC, JAE, Architectural Science Review, ACADIA and FABRICATE.
- **Juries.** Juror for the eVolo Skyscraper Competition and the ACSA Steel Design Competition.
- **RVTR appointment split.** "Director, RVTR (research lab), Ann Arbor, 2017–" and "Founding Partner and Director, RVTR Inc, 2007–2017".
  - These are merged into the public CV's wording, "Partner and Director, RVTR, Ann Arbor and Toronto, 2007–".
- **Research framing.** The FAIA description of her research: "new knowledge comes from design propositions and prototypes"; "building skins that integrate environmental sensing, kinetic action and responsiveness"; "urban analysis to build scenarios for decarbonized futures and new social infrastructures".
  - This is replaced with the public wording of her Taubman profile.
