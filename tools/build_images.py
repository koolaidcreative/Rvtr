"""Generate responsive derivatives from the recovered originals in rvtr_archive/.

imgix used to do this resizing on the fly; it is gone, so we bake a fixed
ladder of widths to disk and point the srcsets at them. Each uuid directory in
the archive holds exactly one image, so the uuid alone keys an image.

Output: images/<uuid>/<stem>-<width>w.jpg  plus images/_manifest.json
Idempotent: existing, up-to-date derivatives are skipped.
"""
import json, os, sys
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
SRC = os.path.join(os.path.dirname(SITE), "rvtr_archive")
OUT = os.path.join(SITE, "images")

LADDER = [320, 640, 960, 1280, 1600]
QUALITY = 82


def targets(width):
    """Widths to emit for a source of the given width. Never upscale."""
    ws = [w for w in LADDER if w < width]
    ws.append(min(width, LADDER[-1]))       # native width, or the ladder cap
    return sorted(set(ws))


def build(job):
    uuid, path = job
    try:
        with Image.open(path) as raw:
            im = ImageOps.exif_transpose(raw)
            if im.mode != "RGB":
                im = im.convert("RGB")
            w, h = im.size
            stem = os.path.splitext(os.path.basename(path))[0]
            dest = os.path.join(OUT, uuid)
            os.makedirs(dest, exist_ok=True)
            src_mtime = os.path.getmtime(path)
            made = []
            for tw in targets(w):
                out = os.path.join(dest, f"{stem}-{tw}w.jpg")
                made.append(tw)
                if os.path.exists(out) and os.path.getmtime(out) >= src_mtime:
                    continue
                th = max(1, round(h * tw / w))
                im.resize((tw, th), Image.LANCZOS).save(
                    out, "JPEG", quality=QUALITY, optimize=True, progressive=True
                )
            # Drop derivatives from an earlier, different ladder so a lowered
            # cap does not leave orphaned wide files behind.
            keep = {f"{stem}-{tw}w.jpg" for tw in made}
            pruned = []
            for old in os.listdir(dest):
                if old.endswith(".jpg") and old not in keep:
                    os.remove(os.path.join(dest, old))
                    pruned.append(old)
            return uuid, {"stem": stem, "width": w, "height": h,
                          "sizes": made, "pruned": pruned}, None
    except Exception as e:                                  # noqa: BLE001
        return uuid, None, f"{path}: {e}"


def main():
    jobs = []
    for d in sorted(os.scandir(SRC), key=lambda e: e.name):
        if not d.is_dir():
            continue
        files = os.listdir(d.path)
        if len(files) != 1:
            print(f"SKIP {d.name}: expected 1 file, found {len(files)}", file=sys.stderr)
            continue
        jobs.append((d.name, os.path.join(d.path, files[0])))

    manifest, errors, done = {}, [], 0
    with ProcessPoolExecutor() as pool:
        for uuid, info, err in pool.map(build, jobs, chunksize=4):
            done += 1
            if err:
                errors.append(err)
            else:
                manifest[uuid] = info
            if done % 50 == 0:
                print(f"  {done}/{len(jobs)}", flush=True)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)

    total = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fs in os.walk(OUT) for f in fs
    )
    print(f"\nbuilt {len(manifest)} images, {total/1e9:.2f} GB in {OUT}")
    npruned = sum(len(v.get("pruned", ())) for v in manifest.values())
    if npruned:
        print(f"pruned {npruned} stale derivatives from a previous ladder")
    for e in errors:
        print("ERROR", e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
