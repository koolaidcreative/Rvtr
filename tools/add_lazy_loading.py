"""Add loading="lazy" to below-the-fold images.

The scraped markup has no loading attribute at all, so a project page with 42
images fetches every one before you have scrolled anywhere.

Carousels need care rather than blanket exemption. The slider is a translateX
track inside an overflow:hidden viewport, so distant slides never intersect the
viewport and a lazy slide can blank briefly when the user advances to it. But
exempting carousels entirely is nearly useless here -- the heaviest pages are
almost all carousel, so it would leave them unchanged. The compromise is to
keep the first EAGER_SLIDES of each carousel eager (what you see, plus the next
one ready for the first advance) and lazy-load the rest.

Also kept eager: the first EAGER_FIRST images in document order, which are the
header logo and the hero. Lazy-loading the LCP element delays it.

Edits are surgical: the parser only locates each <img, and the attribute is
spliced into that byte offset. The document is never re-serialised, so nothing
else in these hand-scraped files can shift.

Idempotent. Use --check to report without writing.
"""
import os, sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

EAGER_FIRST = 3          # header logo (x2) + hero
EAGER_SLIDES = 2         # visible slide + the next one
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "area",
        "base", "col", "embed", "param", "track", "wbr"}


class ImgFinder(HTMLParser):
    """Locate every <img and classify it as eager or lazy."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []          # one frame per open element
        self.counters = []       # slide counter per nested carousel container
        self.hits = []           # (offset, eager_reason|None, has_loading)
        self.line_starts = []

    def _abs_offset(self):       # HTMLParser already owns .offset
        line, col = self.getpos()
        return self.line_starts[line - 1] + col

    def _slide_index(self):
        """1-based slide number of the nearest enclosing carousel slide."""
        for frame in reversed(self.stack):
            if frame["slide"] is not None:
                return frame["slide"]
        return None

    def _classify(self, attrs):
        d = dict(attrs)
        slide = self._slide_index()
        if slide is not None and slide > EAGER_SLIDES:
            return None, "loading" in d          # lazy
        if slide is not None:
            return "carousel-head", "loading" in d
        if self.counters:
            # Inside carousel chrome but not in a slide -- leave alone.
            return "carousel-other", "loading" in d
        return None, "loading" in d

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = (d.get("class") or "").lower()
        if tag == "img":
            reason, has = self._classify(attrs)
            self.hits.append((self._abs_offset(), reason, has))
            return
        if tag in VOID:
            return
        is_slide = "carousel__slide" in cls
        is_container = "carousel" in cls and not is_slide
        frame = {"carousel": is_container, "slide": None}
        if is_container:
            self.counters.append(0)
        if is_slide and self.counters:
            self.counters[-1] += 1
            frame["slide"] = self.counters[-1]
        self.stack.append(frame)

    def handle_endtag(self, tag):
        if tag in VOID or not self.stack:
            return
        frame = self.stack.pop()
        if frame["carousel"] and self.counters:
            self.counters.pop()


def process(text):
    p = ImgFinder()
    starts, n = [0], 0
    for line in text.splitlines(keepends=True):
        n += len(line)
        starts.append(n)
    p.line_starts = starts
    p.feed(text)

    lazy, eager = [], 0
    for i, (off, reason, has) in enumerate(p.hits):
        if has or i < EAGER_FIRST or reason is not None:
            eager += 1
            continue
        lazy.append(off)
    for off in sorted(lazy, reverse=True):      # splice from the end
        assert text[off:off + 4] == "<img", "offset drifted at %d" % off
        text = text[:off + 4] + ' loading="lazy"' + text[off + 4:]
    return text, len(p.hits), len(lazy), eager


def main():
    check = "--check" in sys.argv
    pages = []
    for dp, dirs, fs in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in ("node_modules", "images", "tools")]
        pages += [os.path.join(dp, f) for f in fs if f.endswith(".html")]

    tot = lazied = changed = 0
    for page in sorted(pages):
        with open(page, encoding="utf-8", newline="") as f:
            before = f.read()
        after, n, nl, _ = process(before)
        tot += n; lazied += nl
        if after != before:
            changed += 1
            if not check:
                with open(page, "w", encoding="utf-8", newline="") as f:
                    f.write(after)

    print("%s %d/%d pages" % ("would change" if check else "changed", changed, len(pages)))
    print("  images total : %d" % tot)
    print("  marked lazy  : %d" % lazied)
    print("  left eager   : %d" % (tot - lazied))


if __name__ == "__main__":
    main()
