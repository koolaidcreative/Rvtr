"""Link assets/custom.css from every page, after the vendor stylesheet.

The scraped pages reference their stylesheet with a relative path whose depth
varies per page, but every internal link on this site is root-absolute and the
site is served from the domain root, so a root-absolute href is both correct
and depth-independent.

The tag goes immediately before </head>, i.e. after the vendor stylesheet, so
the override wins the cascade.

Idempotent -- a page that already links the file is skipped. Use --check to
report without writing.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

HREF = "/assets/custom.css"
TAG = '<link rel="stylesheet" media="all" href="%s">' % HREF


def main():
    check = "--check" in sys.argv
    pages = []
    for dp, dirs, fs in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in ("node_modules", "images", "tools")]
        pages += [os.path.join(dp, f) for f in fs if f.endswith(".html")]

    changed = skipped = nohead = 0
    for page in sorted(pages):
        with open(page, encoding="utf-8", newline="") as f:
            text = f.read()
        if HREF in text:
            skipped += 1
            continue
        i = text.lower().rfind("</head>")
        if i == -1:
            nohead += 1
            print("  NO </head>:", os.path.relpath(page, SITE))
            continue
        changed += 1
        if not check:
            out = text[:i] + TAG + "\n" + text[i:]
            with open(page, "w", encoding="utf-8", newline="") as f:
                f.write(out)

    print("%s %d/%d pages" % ("would link" if check else "linked", changed, len(pages)))
    if skipped:
        print("  already linked: %d" % skipped)
    if nohead:
        print("  MISSING </head>: %d" % nohead)
    return 1 if nohead else 0


if __name__ == "__main__":
    sys.exit(main())
