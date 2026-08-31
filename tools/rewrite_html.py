"""Repoint every dead monograph.imgix.net URL at the local derivatives.

The imgix CDN is gone. Its URLs survive in three attributes only -- srcset,
src and content (og:image / schema.org) -- and each carries the uuid that keys
the recovered original, so the uuid alone is enough to rebuild the link. The
original filename in the URL is ignored: one reference on the site omitted its
file extension entirely and imgix served it anyway.

Originals are NOT copied into the site; they stay in rvtr_archive/.
Run build_images.py first. Idempotent. Use --check to audit without writing.
"""
import html as htmllib
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
BACKUP = os.path.join(HERE, "_html_backup")
MANIFEST = os.path.join(SITE, "images", "_manifest.json")

# og:image must be absolute for social scrapers; matches the existing canonical.
BASE = "https://www.rvtr.com"

ATTR = re.compile(r'\b(srcset|src|content)="([^"]*monograph\.imgix\.net[^"]*)"')
UUID = re.compile(r'imgix\.net/([0-9a-f-]{36})/')
WIDTH = re.compile(r'[?&]w=(\d+)')


def pick(sizes, want):
    """Smallest generated width that still covers `want`."""
    return next((w for w in sizes if w >= want), sizes[-1])


def local(uuid, info, width):
    return f"/images/{uuid}/{info['stem']}-{width}w.jpg"


def rewrite(text, manifest, stats):
    def sub(m):
        attr, value = m.group(1), m.group(2)
        found = UUID.search(value)
        if not found:
            return m.group(0)
        uuid = found.group(1)
        info = manifest.get(uuid)
        if not info:
            stats["unknown"].add(uuid)
            return m.group(0)
        sizes = info["sizes"]
        stats[attr] += 1

        if attr == "srcset":
            # Rebuild from the ladder we actually generated rather than from the
            # old imgix entries, so every descriptor states a true pixel width.
            entries = ", ".join(f"{local(uuid, info, w)} {w}w" for w in sizes)
            return f'{attr}="{entries}"'

        want = WIDTH.search(htmllib.unescape(value))
        if attr == "content":
            # og:image: absolute, and as large as we have.
            return f'{attr}="{BASE}{local(uuid, info, sizes[-1])}"'
        return f'{attr}="{local(uuid, info, pick(sizes, int(want.group(1)) if want else 0))}"'

    return ATTR.sub(sub, text)


def main():
    check = "--check" in sys.argv
    if not os.path.exists(MANIFEST):
        sys.exit(f"missing {MANIFEST} -- run build_images.py first")
    with open(MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)

    pages = []
    for dp, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in ("node_modules", "images", "tools")]
        pages += [os.path.join(dp, f) for f in files if f.endswith(".html")]

    stats = {"srcset": 0, "src": 0, "content": 0, "unknown": set()}
    changed, leftovers = 0, []
    for page in sorted(pages):
        rel = os.path.relpath(page, SITE)
        # newline="" preserves the file's existing line endings; the repo is
        # LF and this runs on Windows, so text mode would rewrite every line.
        with open(page, encoding="utf-8", newline="") as f:
            before = f.read()
        after = rewrite(before, manifest, stats)
        if "imgix" in after:
            leftovers.append((rel, after.count("imgix")))
        if after != before:
            changed += 1
            if not check:
                bak = os.path.join(BACKUP, rel)
                if not os.path.exists(bak):           # never overwrite a backup
                    os.makedirs(os.path.dirname(bak), exist_ok=True)
                    shutil.copy2(page, bak)
                with open(page, "w", encoding="utf-8", newline="") as f:
                    f.write(after)

    print(f"{'would rewrite' if check else 'rewrote'} {changed}/{len(pages)} pages")
    print(f"  srcset={stats['srcset']}  src={stats['src']}  content={stats['content']}")
    if stats["unknown"]:
        print(f"  UNKNOWN uuids (no recovered original): {len(stats['unknown'])}")
        for u in sorted(stats["unknown"]):
            print("   ", u)
    if leftovers:
        print(f"  LEFTOVER imgix references in {len(leftovers)} pages:")
        for rel, n in leftovers[:10]:
            print(f"    {rel}: {n}")
    return 1 if (stats["unknown"] or leftovers) else 0


if __name__ == "__main__":
    sys.exit(main())
