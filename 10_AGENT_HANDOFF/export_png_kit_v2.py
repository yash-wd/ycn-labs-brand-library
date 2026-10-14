#!/usr/bin/env python3
"""BRAND-EXPORT-05 exporter v2 (FIX-01), YCN Labs brand library.

Supersedes export_png_kit.py, which is kept unchanged as the record of the first build.
Modes:
  build        write all outputs into a NEW /tmp/ycn05fix_* directory (never into the repo)
  verify       read-only: an output tree must equal the specification exactly (pixels, cHRM,
               chunk set, every manifest field, the whole proof image, the task checksum file)
  compare-old  read-only: decoded pixels of a build must equal the PNGs stored in PREVIOUS_COMMIT
  list         print the 28 output paths, sorted
Python stdlib + Pillow only. No colour conversion; the master's cHRM chunk is copied byte-for-byte.
"""
import argparse
import hashlib
import io
import json
import struct
import subprocess
import sys
import zlib
from pathlib import Path

import PIL
from PIL import Image, ImageChops, ImageDraw, ImageFont, PngImagePlugin

MASTER_REL = "01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png"
MASTER_SHA = "0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3"
MW, MH = 6675, 5195
RECIPE_REL = "10_AGENT_HANDOFF/export_png_kit_v2.py"
PREVIOUS_COMMIT = "234846841534cd97961fa8555051dcf73ef086dd"
DATE = "2026-10-14"
YCN_BOX = (1706, 2039, 5574, 3136)
BOXES = {
    "A_ycn-crop": (1596, 1929, 5684, 3246),
    "B_ycn-square-crop": (1552, 499, 5729, 4676),
    "C_full-square-crop": (740, 0, 5935, 5195),
}
FULL = [(128, 100), (256, 199), (512, 398), (1024, 797), (2048, 1594)]
PREVIEWS = {
    "A_ycn-crop": [(74, 24), (99, 32), (124, 40), (149, 48), (199, 64)],
    "B_ycn-square-crop": [(s, s) for s in (16, 32, 48, 64, 180, 192, 512)],
    "C_full-square-crop": [(s, s) for s in (48, 64, 180, 192, 512)],
}
WEB_DIR = "05_EXPORTS/WEB/full-lockup_on-dark-opaque"
CAND_DIR = "05_EXPORTS/CANDIDATES/small-mark"
NATIVE_DIR = CAND_DIR + "/SOURCE_CANDIDATES"
PROOF_REL = "08_QUALITY_AND_EVIDENCE/BRAND-EXPORT-05/PROOF_SHEET.png"
MANIFEST_REL = "05_EXPORTS/MANIFEST_BRAND-EXPORT-05.json"
SUMS_REL = "05_EXPORTS/SHA256SUMS_BRAND-EXPORT-05.txt"
COLOUR_TYPES = (b"cHRM", b"gAMA", b"sRGB", b"iCCP", b"cICP")
FONT_SIZE = 18
PROOF_W, MARGIN, GAP = 2200, 40, 24


def fail(code, msg):
    sys.stderr.write("FAIL: " + msg + "\n")
    sys.exit(code)


def check(cond, what):
    if not cond:
        fail(7, "check failed: " + what)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def png_chunks(data, name):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(9, "not a PNG: " + name)
    pos, out = 8, []
    while pos < len(data):
        length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
        out.append((ctype, data[pos + 8:pos + 8 + length]))
        pos += 12 + length
        if ctype == b"IEND":
            break
    return out


def check_png(data, name, chrm):
    chunks = png_chunks(data, name)
    check({t for t, _ in chunks} == {b"IHDR", b"cHRM", b"IDAT", b"IEND"}, "chunk set " + name)
    check([d for t, d in chunks if t == b"cHRM"] == [chrm], "cHRM payload " + name)


def same(a, b, what):
    if a.size != b.size or a.mode != b.mode or ImageChops.difference(a, b).getbbox() is not None:
        fail(6, "pixel mismatch: " + what)


def full_rel(w, h):
    return f"{WEB_DIR}/YCN_LABS_logo-lockup_on-dark-opaque_{w}x{h}_v1.0.0.png"


def native_rel(cid):
    b = BOXES[cid]
    return f"{NATIVE_DIR}/YCN_LABS_small-mark-{cid}_{b[2] - b[0]}x{b[3] - b[1]}_NATIVE_CANDIDATE.png"


def preview_rel(cid, w, h):
    return f"{CAND_DIR}/YCN_LABS_small-mark-{cid}_{w}x{h}_CANDIDATE.png"


def artwork_rels():
    return [s["path"] for s in asset_specs()]


def output_paths():
    return sorted(artwork_rels() + [PROOF_REL, MANIFEST_REL, SUMS_REL])


def asset_specs():
    specs = [{"path": full_rel(w, h), "variant": "full-lockup_on-dark-opaque", "status": "PENDING_OWNER_ACCEPTANCE",
              "crop_box": None, "size": (w, h), "transform": "LANCZOS resize of master", "parent": None,
              "approval_ref": "RULING-01 source; export acceptance PENDING"} for w, h in FULL]
    for cid, box in BOXES.items():
        specs.append({"path": native_rel(cid), "variant": "small-mark-native_" + cid,
                      "status": "CANDIDATE_NOT_APPROVED", "crop_box": box, "size": (box[2] - box[0], box[3] - box[1]),
                      "transform": "crop of master; no resampling", "parent": None, "approval_ref": "NONE"})
    for cid, sizes in PREVIEWS.items():
        for w, h in sizes:
            specs.append({"path": preview_rel(cid, w, h), "variant": "small-mark-preview_" + cid,
                          "status": "CANDIDATE_NOT_APPROVED", "crop_box": BOXES[cid], "size": (w, h),
                          "transform": "crop of master, then LANCZOS resize", "parent": native_rel(cid),
                          "approval_ref": "NONE"})
    return specs


def proof_spec(size):
    return {"path": PROOF_REL, "variant": "proof-sheet", "status": "EVIDENCE", "crop_box": None, "size": size,
            "transform": "annotated composition (FIX-01 layout)", "parent": None, "approval_ref": "NONE"}


def entry(spec, recs):
    return {"asset_id": Path(spec["path"]).stem, "path": spec["path"], "variant": spec["variant"],
            "status": spec["status"], "crop_box": list(spec["crop_box"]) if spec["crop_box"] else None,
            "width": spec["size"][0], "height": spec["size"][1], "mode": "RGB", "alpha": "none (opaque)",
            "transform": spec["transform"], "colour_chunks": ["cHRM copied from master"],
            "parent_native_path": spec["parent"],
            "parent_native_sha256": recs[spec["parent"]] if spec["parent"] else None,
            "approval_ref": spec["approval_ref"], "sha256": recs[spec["path"]]}


def check_specs():
    if derive_boxes(YCN_BOX) != BOXES:
        fail(3, "candidate box derivation differs from the recorded boxes")
    for w, h in FULL:
        if int(w * MH / MW + 0.5) != h:
            fail(3, "height rounding")
    for cid, sizes in PREVIEWS.items():
        bw, bh = BOXES[cid][2] - BOXES[cid][0], BOXES[cid][3] - BOXES[cid][1]
        for w, h in sizes:
            if w > bw or h > bh:
                fail(3, "upscale refused")
            if cid == "A_ycn-crop" and w != int(h * bw / bh + 0.5):
                fail(3, "A width rounding")


def load_master(repo):
    data = (Path(repo) / MASTER_REL).read_bytes()
    if hashlib.sha256(data).hexdigest() != MASTER_SHA:
        fail(1, "master sha256 mismatch")
    im = Image.open(io.BytesIO(data))
    im.load()
    if im.size != (MW, MH) or im.mode != "RGB":
        fail(1, f"master is {im.size} {im.mode}")
    cc = {t: d for t, d in png_chunks(data, MASTER_REL) if t in COLOUR_TYPES}
    if set(cc) != {b"cHRM"} or len(cc[b"cHRM"]) != 32:
        fail(1, "unexpected master colour chunks: " + str(sorted(cc)))
    return im, cc[b"cHRM"]


def measure_ycn(im):
    r = (int(0.25 * MW), int(0.37 * MH), int(0.86 * MW), int(0.63 * MH))
    red, green, blue = im.crop(r).split()
    mask = ImageChops.darker(ImageChops.darker(red, green), blue).point(lambda v: 255 if v >= 200 else 0)
    bb = mask.getbbox()
    if not bb:
        fail(2, "empty YCN mask")
    return (r[0] + bb[0], r[1] + bb[1], r[0] + bb[2], r[1] + bb[3])


def derive_boxes(ycn):
    x0, y0, x1, y1 = ycn
    p = int(0.10 * (y1 - y0) + 0.5)
    s = int(1.08 * (x1 - x0) + 0.5)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    return {
        "A_ycn-crop": (x0 - p, y0 - p, x1 + p, y1 + p),
        "B_ycn-square-crop": (cx - s // 2, cy - s // 2, cx - s // 2 + s, cy - s // 2 + s),
        "C_full-square-crop": (740, 0, 5935, 5195),
    }


def render_asset(im, spec, crops):
    if spec["crop_box"] is None:
        return im.resize(spec["size"], Image.Resampling.LANCZOS)
    crop = crops[spec["crop_box"]]
    if spec["parent"] is None:
        return crop
    return crop.resize(spec["size"], Image.Resampling.LANCZOS)


def proof_font():
    return ImageFont.load_default(size=FONT_SIZE)


def wrap(text, font, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            trial = word if not cur else cur + " " + word
            if font.getlength(trial) <= maxw:
                cur = trial
                continue
            if cur:
                lines.append(cur)
            while font.getlength(word) > maxw:
                k = len(word)
                while k > 1 and font.getlength(word[:k]) > maxw:
                    k -= 1
                lines.append(word[:k])
                word = word[k:]
            cur = word
        lines.append(cur)
    return lines


def white_panel(img256, img512):
    panel = Image.new("RGB", (MARGIN + 256 + GAP + 512 + MARGIN, 398 + 2 * MARGIN), (255, 255, 255))
    panel.paste(img256, (MARGIN, MARGIN))
    panel.paste(img512, (MARGIN + 256 + GAP, MARGIN))
    return panel


def crop_overlay(im):
    ov = im.resize((1024, 797), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(ov)
    sx, sy = 1024 / MW, 797 / MH
    for cid, colour in (("C_full-square-crop", (0, 255, 0)), ("B_ycn-square-crop", (255, 255, 0)),
                        ("A_ycn-crop", (255, 0, 0))):
        b = BOXES[cid]
        rect = [int(b[0] * sx + 0.5), int(b[1] * sy + 0.5), int(b[2] * sx + 0.5) - 1, int(b[3] * sy + 0.5) - 1]
        draw.rectangle(rect, outline=colour, width=4)
    return ov


def proof_blocks(im, imgs, recs):
    blocks = [
        ("BRAND-EXPORT-05 PROOF SHEET (FIX-01). Evidence, not a logo master. Opaque exports: PENDING OWNER "
         "ACCEPTANCE. Small marks: CANDIDATE, NOT APPROVED. Open: 02a, 02b, 04, RULING-05. Panels are 1:1 "
         "unless marked REDUCED.", None),
        ("SECTION 1 - opaque full-logo exports (LANCZOS resize of the RULING-01 master)", None),
    ]
    for w, h in FULL:
        rel = full_rel(w, h)
        blocks.append((f"{rel} | {w}x{h} | sha256 {recs[rel]}", imgs[rel]))
    blocks.append(("SECTION 2 - presentation preview only (04 OPEN): the 256 and 512 exports at 1:1 on a white panel",
                   white_panel(imgs[full_rel(256, 199)], imgs[full_rel(512, 398)])))
    blocks.append(("SECTION 3 - REDUCED proof-only view of the master (1024 px wide). Crop outlines: A red, B yellow, "
                   "C green. Outlines are annotations, not artwork edits.", crop_overlay(im)))
    for cid, box in BOXES.items():
        rel_n = native_rel(cid)
        blocks.append((f"SECTION 4 - candidate {cid}, NOT APPROVED | crop box {list(box)} | native parent {rel_n} | "
                       f"sha256 {recs[rel_n]}", None))
        for w, h in PREVIEWS[cid]:
            rel = preview_rel(cid, w, h)
            blocks.append((f"{Path(rel).name} | {w}x{h} | sha256 {recs[rel]}", imgs[rel]))
    return blocks


def layout(blocks, font):
    ascent, descent = font.getmetrics()
    lh = ascent + descent + 4
    maxw = PROOF_W - 2 * MARGIN
    y, placed = MARGIN, []
    for label, img in blocks:
        lines = wrap(label, font, maxw)
        ty = y
        y += lh * len(lines) + 6
        box = None
        if img is not None:
            if img.width > maxw:
                fail(5, "panel wider than the proof sheet")
            box = (MARGIN, y, MARGIN + img.width, y + img.height)
            y += img.height
        placed.append((lines, ty, img, box))
        y += GAP
    return placed, y + MARGIN, lh


def render_proof(placed, height, lh, font):
    sheet = Image.new("RGB", (PROOF_W, height), (128, 128, 128))
    draw = ImageDraw.Draw(sheet)
    for lines, ty, img, box in placed:
        for i, line in enumerate(lines):
            draw.text((MARGIN, ty + i * lh), line, fill=(0, 0, 0), font=font)
        if img is not None:
            sheet.paste(img, box[:2])
    return sheet


def make_manifest(entries, chrm, font):
    return {
        "task": "BRAND-EXPORT-05", "fix": "FIX-01", "date": DATE,
        "supersedes_outputs_of_commit": PREVIOUS_COMMIT,
        "source_path": MASTER_REL, "source_sha256": MASTER_SHA,
        "source_colour_chunks": {"cHRM": chrm.hex()},
        "colour_handling": ("The master's only colour chunk (cHRM, 32 bytes) is copied byte-for-byte into every PNG "
                            "written here. The master has no gAMA, sRGB, iCCP or cICP chunk and none is added. "
                            "No colour conversion is performed. No official colour profile is established by this "
                            "task."),
        "recipe_path": RECIPE_REL, "recipe_sha256": sha256_file(Path(__file__).resolve()),
        "toolchain": {
            "python_version": sys.version.split()[0], "pillow_version": PIL.__version__,
            "zlib_runtime_version": zlib.ZLIB_RUNTIME_VERSION, "zlib_compile_version": zlib.ZLIB_VERSION,
            "png_compress_level": 9,
            "proof_font": " ".join(font.getname()) + f", {FONT_SIZE} px, Pillow load_default",
        },
        "ycn_box": list(YCN_BOX), "candidate_boxes": {k: list(v) for k, v in BOXES.items()},
        "matrix_rows_covered": ["full-lockup,on-dark,PNG (opaque only)"],
        "excluded": ["transparent variants", "on-light row", "all SVG/PDF/EPS", "wordmark-only", "single-ink",
                     "social-avatar", "open-graph", "animation", "ICO/favicon production", "widths above 2048"],
        "open_decisions": ["02a", "02b", "04", "RULING-05", "BRAND-EXPORT-05 acceptance"],
        "assets": entries,
    }


def save_png(img, path, chrm):
    if path.exists() or path.is_symlink():
        fail(4, "refusing to overwrite " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    info = PngImagePlugin.PngInfo()
    info.add(b"cHRM", chrm)
    img.save(path, format="PNG", compress_level=9, pnginfo=info)


def build(repo, out):
    im, chrm = load_master(repo)
    if measure_ycn(im) != YCN_BOX:
        fail(2, "measured YCN box differs from the recorded box " + str(YCN_BOX))
    check_specs()
    crops = {box: im.crop(box) for box in BOXES.values()}
    imgs, recs, entries = {}, {}, []
    for spec in asset_specs():
        img = render_asset(im, spec, crops)
        save_png(img, out / spec["path"], chrm)
        imgs[spec["path"]], recs[spec["path"]] = img, sha256_file(out / spec["path"])
        entries.append(entry(spec, recs))
    font = proof_font()
    placed, height, lh = layout(proof_blocks(im, imgs, recs), font)
    sheet = render_proof(placed, height, lh, font)
    save_png(sheet, out / PROOF_REL, chrm)
    recs[PROOF_REL] = sha256_file(out / PROOF_REL)
    entries.append(entry(proof_spec(sheet.size), recs))
    (out / MANIFEST_REL).write_text(json.dumps(make_manifest(entries, chrm, font), indent=2) + "\n", encoding="utf-8")
    paths = sorted([e["path"] for e in entries] + [MANIFEST_REL])
    (out / SUMS_REL).write_text("".join(f"{sha256_file(out / p)}  {p}\n" for p in paths), encoding="utf-8")
    print(f"BUILD OK: {len(entries)} PNGs + manifest + task checksums in {out}")


def verify(repo, out):
    im, chrm = load_master(repo)
    check_specs()
    crops = {box: im.crop(box) for box in BOXES.values()}
    imgs, recs = {}, {}
    for spec in asset_specs():
        rel = spec["path"]
        data = (out / rel).read_bytes()
        check_png(data, rel, chrm)
        img = Image.open(io.BytesIO(data))
        img.load()
        check(img.mode == "RGB" and img.size == spec["size"], "size/mode " + rel)
        same(img, render_asset(im, spec, crops), rel)
        if spec["parent"]:
            same(img, imgs[spec["parent"]].resize(spec["size"], Image.Resampling.LANCZOS), rel + " (from native file)")
        imgs[rel], recs[rel] = img, hashlib.sha256(data).hexdigest()
    font = proof_font()
    placed, height, lh = layout(proof_blocks(im, imgs, recs), font)
    for _, _, img, box in placed:
        if img is not None:
            check(box[2] <= PROOF_W and box[3] <= height, "panel inside proof " + str(box))
    data = (out / PROOF_REL).read_bytes()
    check_png(data, PROOF_REL, chrm)
    sheet = Image.open(io.BytesIO(data))
    sheet.load()
    same(sheet, render_proof(placed, height, lh, font), "whole proof sheet (labels, panels, bounds)")
    recs[PROOF_REL] = hashlib.sha256(data).hexdigest()
    entries = [entry(s, recs) for s in asset_specs()] + [entry(proof_spec(sheet.size), recs)]
    manifest = json.loads((out / MANIFEST_REL).read_text(encoding="utf-8"))
    check(manifest == make_manifest(entries, chrm, font), "manifest differs from the specification")
    paths = sorted([e["path"] for e in entries] + [MANIFEST_REL])
    expected_sums = "".join(f"{sha256_file(out / p)}  {p}\n" for p in paths)
    check((out / SUMS_REL).read_text(encoding="utf-8") == expected_sums, "task checksum file")
    print(f"VERIFY PASS: {len(entries)} PNGs (recipe pixels, cHRM, chunk set), whole proof sheet, every manifest "
          f"field, {len(paths)} task checksums")


def compare_old(repo, out):
    rels = artwork_rels()
    for rel in rels:
        old_bytes = subprocess.run(["git", "-C", str(repo), "show", f"{PREVIOUS_COMMIT}:{rel}"],
                                   check=True, capture_output=True).stdout
        old = Image.open(io.BytesIO(old_bytes))
        old.load()
        new = Image.open(out / rel)
        new.load()
        same(new, old, f"new build vs {PREVIOUS_COMMIT[:7]}:{rel}")
    print(f"COMPARE-OLD PASS: {len(rels)} artwork PNGs have identical decoded pixels to commit {PREVIOUS_COMMIT[:7]}")


def main():
    ap = argparse.ArgumentParser(description="BRAND-EXPORT-05 exporter v2 (FIX-01)")
    ap.add_argument("mode", choices=["build", "verify", "compare-old", "list"])
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.mode == "list":
        print("\n".join(output_paths()))
        return
    if not args.out:
        fail(8, "--out is required")
    out = Path(args.out).resolve()
    if args.mode == "build":
        if out.parent != Path("/tmp") or not out.name.startswith("ycn05fix_") or out.exists():
            fail(8, "build output must be a new directory /tmp/ycn05fix_*")
        build(args.repo, out)
    elif args.mode == "verify":
        verify(args.repo, out)
    else:
        compare_old(args.repo, out)


if __name__ == "__main__":
    main()
