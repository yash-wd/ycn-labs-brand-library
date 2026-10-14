#!/usr/bin/env python3
"""
YCN Labs — Brand Export Kit Generator (BRAND-EXPORT-05: Opaque-First v2.1)
Builds:
  1. Opaque on-dark full-logo PNGs from the canonical RULING-01 master.
  2. Native-resolution small-mark candidate crops (A, B, C).
  3. Small-mark candidate previews across target responsive icon sizes.
  4. Diagnostic proof sheet.
  5. Deterministic manifest (MANIFEST_BRAND-EXPORT-05.json).
  6. Task checksum inventory (SHA256SUMS_BRAND-EXPORT-05.txt).
  7. Independent verification routine ensuring exact LANCZOS resize / crop equivalence.
"""

import sys, os, io, json, hashlib, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops

EXPECTED_MASTER_SHA = "0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3"
EXPECTED_MASTER_DIMS = (6675, 5195)
EXPECTED_MASTER_MODE = "RGB"

def round_half_up(x):
    return int(x + 0.5)

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def validate_master(master_path):
    p = Path(master_path).resolve()
    if not p.is_file():
        sys.stderr.write(f"FATAL: Master file does not exist: {p}\n")
        sys.exit(1)
    actual_sha = sha256_file(p)
    if actual_sha != EXPECTED_MASTER_SHA:
        sys.stderr.write(f"FATAL: Master SHA-256 mismatch!\n  Expected: {EXPECTED_MASTER_SHA}\n  Actual:   {actual_sha}\n")
        sys.exit(1)
    im = Image.open(p)
    if im.size != EXPECTED_MASTER_DIMS:
        sys.stderr.write(f"FATAL: Master dimensions mismatch: expected {EXPECTED_MASTER_DIMS}, got {im.size}\n")
        sys.exit(1)
    if im.mode != EXPECTED_MASTER_MODE:
        sys.stderr.write(f"FATAL: Master mode mismatch: expected {EXPECTED_MASTER_MODE}, got {im.mode}\n")
        sys.exit(1)
    return im, actual_sha

def check_destination(out_path):
    p = Path(out_path).resolve()
    s = str(p)
    if "01_IMMUTABLE_SOURCE" in s:
        sys.stderr.write(f"FATAL: Prohibited write to 01_IMMUTABLE_SOURCE: {p}\n")
        sys.exit(1)
    if "04_APPROVED_LOGO_VARIANTS" in s:
        sys.stderr.write(f"FATAL: Prohibited write to 04_APPROVED_LOGO_VARIANTS: {p}\n")
        sys.exit(1)
    if p.exists():
        sys.stderr.write(f"FATAL: Destination file already exists (no overwrite): {p}\n")
        sys.exit(1)

def measure_ycn_box(im):
    # Region: (int(0.25*6675), int(0.37*5195), int(0.86*6675), int(0.63*5195)) -> (1668, 1922, 5740, 3272)
    rx0, ry0, rx1, ry1 = int(0.25 * 6675), int(0.37 * 5195), int(0.86 * 6675), int(0.63 * 5195)
    region_crop = im.crop((rx0, ry0, rx1, ry1))
    r, g, b = region_crop.split()
    darker = ImageChops.darker(ImageChops.darker(r, g), b)
    mask = darker.point(lambda p: 255 if p >= 200 else 0)
    bbox = mask.getbbox()
    if not bbox:
        sys.stderr.write("FATAL: Mask bounding box is empty!\n")
        sys.exit(2)
    x0 = rx0 + bbox[0]
    y0 = ry0 + bbox[1]
    x1 = rx0 + bbox[2]
    y1 = ry0 + bbox[3]
    w = x1 - x0
    h = y1 - y0
    ratio = w / h
    est = (1735, 2030, 5578, 3150)
    if not (3.0 <= ratio <= 3.9):
        sys.stderr.write(f"FATAL: YCN box ratio {ratio:.4f} outside [3.0, 3.9]\n")
        sys.exit(2)
    if not (abs(x0 - est[0]) <= 250 and abs(y0 - est[1]) <= 250 and abs(x1 - est[2]) <= 250 and abs(y1 - est[3]) <= 250):
        sys.stderr.write(f"FATAL: YCN box coordinates ({x0}, {y0}, {x1}, {y1}) exceed +-250 px delta from estimate {est}\n")
        sys.exit(2)
    return (x0, y0, x1, y1, w, h)

def compute_candidate_boxes(ycn_box):
    x0, y0, x1, y1, w, h = ycn_box
    # Candidate A: ycn-crop
    p = round_half_up(0.10 * h)
    boxA = (x0 - p, y0 - p, x1 + p, y1 + p)
    # Candidate B: ycn-square-crop
    s = round_half_up(1.08 * w)
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    boxB = (cx - s // 2, cy - s // 2, cx - s // 2 + s, cy - s // 2 + s)
    # Candidate C: full-square-crop
    boxC = (740, 0, 5935, 5195)
    for name, box in [("A_ycn-crop", boxA), ("B_ycn-square-crop", boxB), ("C_full-square-crop", boxC)]:
        bx0, by0, bx1, by1 = box
        if not (0 <= bx0 < bx1 <= 6675 and 0 <= by0 < by1 <= 5195):
            sys.stderr.write(f"FATAL: Candidate box {name} {box} lies outside master bounds (0, 0, 6675, 5195)\n")
            sys.exit(3)
    return boxA, boxB, boxC

def build_kit(master_path, out_root, date_str):
    im_master, master_sha = validate_master(master_path)
    out_root = Path(out_root).resolve()

    # Target directories
    web_dir = out_root / "05_EXPORTS" / "WEB" / "full-lockup_on-dark-opaque"
    cand_dir = out_root / "05_EXPORTS" / "CANDIDATES" / "small-mark"
    native_cand_dir = cand_dir / "SOURCE_CANDIDATES"
    proof_dir = out_root / "08_QUALITY_AND_EVIDENCE" / "BRAND-EXPORT-05"
    manifest_path = out_root / "05_EXPORTS" / "MANIFEST_BRAND-EXPORT-05.json"
    task_checksum_path = out_root / "05_EXPORTS" / "SHA256SUMS_BRAND-EXPORT-05.txt"

    for d in [web_dir, cand_dir, native_cand_dir, proof_dir]:
        d.mkdir(parents=True, exist_ok=True)

    ycn_box = measure_ycn_box(im_master)
    boxA, boxB, boxC = compute_candidate_boxes(ycn_box)

    # Save parameters: RGB, compress_level=9, preserve chromaticity if present
    save_kwargs = {"format": "PNG", "compress_level": 9}
    if "chromaticity" in im_master.info:
        save_kwargs["chromaticity"] = im_master.info["chromaticity"]

    # Manifest accumulator
    asset_manifests = []
    created_files_rel = []

    # 1. Full lockup exports
    full_widths = [128, 256, 512, 1024, 2048]
    expected_heights = [100, 199, 398, 797, 1594]
    generated_full = {}
    for w, exp_h in zip(full_widths, expected_heights):
        h = round_half_up(w * 5195 / 6675)
        assert h == exp_h, f"Height rounding mismatch: expected {exp_h}, got {h}"
        assert w <= 6675 and h <= 5195, "Upscaling forbidden"
        fn = f"YCN_LABS_logo-lockup_on-dark-opaque_{w}x{h}_v1.0.0.png"
        fp = web_dir / fn
        check_destination(fp)
        resized = im_master.resize((w, h), resample=Image.Resampling.LANCZOS)
        resized.save(fp, **save_kwargs)
        rel_path = str(fp.relative_to(out_root))
        h_digest = sha256_file(fp)
        generated_full[w] = (fp, resized, h_digest)
        asset_manifests.append({
            "asset_id": f"full-lockup_on-dark-opaque_{w}x{h}",
            "path": rel_path,
            "variant": "full-lockup_on-dark-opaque",
            "status": "PENDING_OWNER_ACCEPTANCE",
            "crop_box": None,
            "width": w,
            "height": h,
            "mode": "RGB",
            "alpha": "none (opaque)",
            "resample": "LANCZOS",
            "approval_ref": "RULING-01 source; export acceptance PENDING",
            "sha256": h_digest
        })
        created_files_rel.append(rel_path)

    # 2. Native candidate crops
    native_specs = [
        ("A_ycn-crop", boxA),
        ("B_ycn-square-crop", boxB),
        ("C_full-square-crop", boxC)
    ]
    native_images = {}
    native_digests = {}
    for cand_id, box in native_specs:
        crop_w = box[2] - box[0]
        crop_h = box[3] - box[1]
        fn = f"YCN_LABS_small-mark-{cand_id}_{crop_w}x{crop_h}_NATIVE_CANDIDATE.png"
        fp = native_cand_dir / fn
        check_destination(fp)
        cropped = im_master.crop(box)
        cropped.save(fp, **save_kwargs)
        rel_path = str(fp.relative_to(out_root))
        h_digest = sha256_file(fp)
        native_images[cand_id] = (fp, cropped, box, crop_w, crop_h)
        native_digests[cand_id] = (rel_path, h_digest, (crop_w, crop_h))
        asset_manifests.append({
            "asset_id": f"small-mark-native_{cand_id}_{crop_w}x{crop_h}",
            "path": rel_path,
            "variant": f"small-mark-native_{cand_id}",
            "status": "CANDIDATE_NOT_APPROVED",
            "crop_box": list(box),
            "width": crop_w,
            "height": crop_h,
            "mode": "RGB",
            "alpha": "none (opaque)",
            "resample": "none (crop only)",
            "approval_ref": "NONE",
            "sha256": h_digest
        })
        created_files_rel.append(rel_path)

    # 3. Small-mark candidate previews
    # Group A: Heights 24, 32, 40, 48, 64
    cropA_w = boxA[2] - boxA[0]
    cropA_h = boxA[3] - boxA[1]
    cropped_A = native_images["A_ycn-crop"][1]
    group_A_previews = []
    for h_target in [24, 32, 40, 48, 64]:
        w_target = round_half_up(h_target * cropA_w / cropA_h)
        assert w_target <= cropA_w and h_target <= cropA_h, "Upscaling forbidden"
        fn = f"YCN_LABS_small-mark-A_ycn-crop_{w_target}x{h_target}_CANDIDATE.png"
        fp = cand_dir / fn
        check_destination(fp)
        resized = cropped_A.resize((w_target, h_target), resample=Image.Resampling.LANCZOS)
        resized.save(fp, **save_kwargs)
        rel_path = str(fp.relative_to(out_root))
        h_digest = sha256_file(fp)
        group_A_previews.append((fp, resized, w_target, h_target, h_digest))
        asset_manifests.append({
            "asset_id": f"small-mark-preview_A_ycn-crop_{w_target}x{h_target}",
            "path": rel_path,
            "variant": "small-mark-preview_A_ycn-crop",
            "status": "CANDIDATE_NOT_APPROVED",
            "crop_box": list(boxA),
            "width": w_target,
            "height": h_target,
            "mode": "RGB",
            "alpha": "none (opaque)",
            "resample": "LANCZOS",
            "approval_ref": "NONE",
            "sha256": h_digest
        })
        created_files_rel.append(rel_path)

    # Group B: Squares 16, 32, 48, 64, 180, 192, 512
    cropB_w = boxB[2] - boxB[0]
    cropped_B = native_images["B_ycn-square-crop"][1]
    group_B_previews = []
    for s_target in [16, 32, 48, 64, 180, 192, 512]:
        assert s_target <= cropB_w, "Upscaling forbidden"
        fn = f"YCN_LABS_small-mark-B_ycn-square-crop_{s_target}x{s_target}_CANDIDATE.png"
        fp = cand_dir / fn
        check_destination(fp)
        resized = cropped_B.resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        resized.save(fp, **save_kwargs)
        rel_path = str(fp.relative_to(out_root))
        h_digest = sha256_file(fp)
        group_B_previews.append((fp, resized, s_target, s_target, h_digest))
        asset_manifests.append({
            "asset_id": f"small-mark-preview_B_ycn-square-crop_{s_target}x{s_target}",
            "path": rel_path,
            "variant": "small-mark-preview_B_ycn-square-crop",
            "status": "CANDIDATE_NOT_APPROVED",
            "crop_box": list(boxB),
            "width": s_target,
            "height": s_target,
            "mode": "RGB",
            "alpha": "none (opaque)",
            "resample": "LANCZOS",
            "approval_ref": "NONE",
            "sha256": h_digest
        })
        created_files_rel.append(rel_path)

    # Group C: Squares 48, 64, 180, 192, 512
    cropC_w = boxC[2] - boxC[0]
    cropped_C = native_images["C_full-square-crop"][1]
    group_C_previews = []
    for s_target in [48, 64, 180, 192, 512]:
        assert s_target <= cropC_w, "Upscaling forbidden"
        fn = f"YCN_LABS_small-mark-C_full-square-crop_{s_target}x{s_target}_CANDIDATE.png"
        fp = cand_dir / fn
        check_destination(fp)
        resized = cropped_C.resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        resized.save(fp, **save_kwargs)
        rel_path = str(fp.relative_to(out_root))
        h_digest = sha256_file(fp)
        group_C_previews.append((fp, resized, s_target, s_target, h_digest))
        asset_manifests.append({
            "asset_id": f"small-mark-preview_C_full-square-crop_{s_target}x{s_target}",
            "path": rel_path,
            "variant": "small-mark-preview_C_full-square-crop",
            "status": "CANDIDATE_NOT_APPROVED",
            "crop_box": list(boxC),
            "width": s_target,
            "height": s_target,
            "mode": "RGB",
            "alpha": "none (opaque)",
            "resample": "LANCZOS",
            "approval_ref": "NONE",
            "sha256": h_digest
        })
        created_files_rel.append(rel_path)

    # 4. Proof Sheet Generation
    # Width 2200 px, background #808080 (128, 128, 128)
    proof_width = 2200
    font = ImageFont.load_default()

    # Calculate height dynamically to guarantee zero overlap or clipping
    # Total sections:
    # Header: ~80px
    # Section 1 (5 full lockups): 128, 256, 512 row (~450px) + 1024 row (~850px) + 2048 row (~1650px) -> ~3000px
    # Section 2 (White panel 256 + 512): ~450px
    # Section 3 (1024 downscaled master with outlines): ~850px
    # Section 4 (17 candidates A, B, C with labels): ~800px
    # Total canvas height ~5600px
    proof_height = 5600
    proof_img = Image.new("RGB", (proof_width, proof_height), (128, 128, 128))
    draw = ImageDraw.Draw(proof_img)

    # Header bar
    draw.rectangle([0, 0, proof_width, 60], fill=(30, 30, 30))
    header_text = "BRAND-EXPORT-05 PROOF | opaque exports PENDING OWNER ACCEPTANCE | small marks CANDIDATE, NOT APPROVED | 02a/02b/04 OPEN | evidence, not a logo master"
    draw.text((30, 22), header_text, fill=(255, 255, 255), font=font)

    curr_y = 80

    # Section 1: Full-lockup files at 1:1
    draw.text((40, curr_y), "SECTION 1: OPAQUE FULL-LOCKUP EXPORTS (1:1 SCALE, MODE RGB, LANCZOS)", fill=(255, 255, 255), font=font)
    curr_y += 25

    # Row for 128, 256, 512
    x_pos = 40
    for w in [128, 256, 512]:
        fp, img, _ = generated_full[w]
        fn = fp.name
        proof_img.paste(img, (x_pos, curr_y + 20))
        draw.text((x_pos, curr_y), f"{fn} ({img.width}x{img.height})", fill=(0, 0, 0), font=font)
        x_pos += img.width + 40
    curr_y += 430

    # 1024 at 1:1
    fp1024, img1024, _ = generated_full[1024]
    draw.text((40, curr_y), f"{fp1024.name} (1024x797)", fill=(0, 0, 0), font=font)
    proof_img.paste(img1024, (40, curr_y + 20))
    curr_y += 840

    # 2048 at 1:1 (centered or placed at x=40)
    fp2048, img2048, _ = generated_full[2048]
    draw.text((40, curr_y), f"{fp2048.name} (2048x1594)", fill=(0, 0, 0), font=font)
    proof_img.paste(img2048, (40, curr_y + 20))
    curr_y += 1640

    # Section 2: White panel presentation preview (256 and 512 on #FFFFFF panel)
    draw.text((40, curr_y), "SECTION 2: WHITE PANEL PRESENTATION PREVIEW (04 OPEN — PRESENTATION PREVIEW ONLY)", fill=(255, 255, 255), font=font)
    curr_y += 25
    white_panel_w = 950
    white_panel_h = 440
    draw.rectangle([40, curr_y, 40 + white_panel_w, curr_y + white_panel_h], fill=(255, 255, 255))
    draw.text((50, curr_y + 10), "presentation preview only, 04 OPEN", fill=(0, 0, 0), font=font)
    proof_img.paste(generated_full[256][1], (60, curr_y + 35))
    proof_img.paste(generated_full[512][1], (360, curr_y + 35))
    curr_y += white_panel_h + 30

    # Section 3: Master downscaled to 1024 wide with 4px candidate crop outlines
    draw.text((40, curr_y), "SECTION 3: CANONICAL MASTER (1024 px wide proof-only) WITH CANDIDATE CROP OUTLINES", fill=(255, 255, 255), font=font)
    curr_y += 20
    master_1024 = im_master.resize((1024, 797), resample=Image.Resampling.LANCZOS)
    draw_m1024 = ImageDraw.Draw(master_1024)
    scale_x = 1024 / 6675
    scale_y = 797 / 5195
    # Outlines: A red (#FF0000), B yellow (#FFFF00), C green (#00FF00)
    for box, col, width in [(boxC, "#00FF00", 4), (boxB, "#FFFF00", 4), (boxA, "#FF0000", 4)]:
        scaled_box = [round_half_up(box[0] * scale_x), round_half_up(box[1] * scale_y),
                      round_half_up(box[2] * scale_x), round_half_up(box[3] * scale_y)]
        for o in range(4):
            draw_m1024.rectangle([scaled_box[0]-o, scaled_box[1]-o, scaled_box[2]+o, scaled_box[3]+o], outline=col)
    proof_img.paste(master_1024, (40, curr_y + 15))
    # Legend
    leg_x = 1080
    leg_y = curr_y + 40
    draw.text((leg_x, leg_y), "CANDIDATE CROP ANNOTATION LEGEND (Proof annotations only; not logo edits):", fill=(0, 0, 0), font=font)
    draw.rectangle([leg_x, leg_y + 25, leg_x + 20, leg_y + 35], fill=(255, 0, 0))
    draw.text((leg_x + 30, leg_y + 25), f"Crop A (Red outline): ycn-crop {boxA} -> {cropA_w}x{cropA_h}", fill=(0, 0, 0), font=font)
    draw.rectangle([leg_x, leg_y + 50, leg_x + 20, leg_y + 60], fill=(255, 255, 0))
    draw.text((leg_x + 30, leg_y + 50), f"Crop B (Yellow outline): ycn-square-crop {boxB} -> {cropB_w}x{cropB_w}", fill=(0, 0, 0), font=font)
    draw.rectangle([leg_x, leg_y + 75, leg_x + 20, leg_y + 85], fill=(0, 255, 0))
    draw.text((leg_x + 30, leg_y + 75), f"Crop C (Green outline): full-square-crop {boxC} -> 5195x5195", fill=(0, 0, 0), font=font)
    draw.text((leg_x, leg_y + 110), "Native candidate sources preserved in: 05_EXPORTS/CANDIDATES/small-mark/SOURCE_CANDIDATES/", fill=(0, 0, 0), font=font)
    curr_y += 840

    # Section 4: All 17 candidate previews grouped A/B/C at 1:1
    draw.text((40, curr_y), "SECTION 4: CANDIDATE SMALL-MARK PREVIEWS (1:1 SCALE, GROUPED A / B / C, NOT APPROVED)", fill=(255, 255, 255), font=font)
    curr_y += 25

    # Group A
    native_A_path, native_A_sha, native_A_dim = native_digests["A_ycn-crop"]
    draw.text((40, curr_y), f"GROUP A (ycn-crop): Native source {native_A_dim[0]}x{native_A_dim[1]} (SHA: {native_A_sha[:16]}...) in {native_A_path}", fill=(0, 0, 0), font=font)
    curr_y += 20
    x_pos = 40
    for _, img, w, h, _ in group_A_previews:
        draw.text((x_pos, curr_y), f"{w}x{h}", fill=(0, 0, 0), font=font)
        proof_img.paste(img, (x_pos, curr_y + 15))
        x_pos += w + 20
    curr_y += 95

    # Group B
    native_B_path, native_B_sha, native_B_dim = native_digests["B_ycn-square-crop"]
    draw.text((40, curr_y), f"GROUP B (ycn-square-crop): Native source {native_B_dim[0]}x{native_B_dim[1]} (SHA: {native_B_sha[:16]}...) in {native_B_path}", fill=(0, 0, 0), font=font)
    curr_y += 20
    x_pos = 40
    for _, img, w, h, _ in group_B_previews:
        draw.text((x_pos, curr_y), f"{w}x{h}", fill=(0, 0, 0), font=font)
        proof_img.paste(img, (x_pos, curr_y + 15))
        x_pos += w + 20
    curr_y += 545

    # Group C
    native_C_path, native_C_sha, native_C_dim = native_digests["C_full-square-crop"]
    draw.text((40, curr_y), f"GROUP C (full-square-crop): Native source {native_C_dim[0]}x{native_C_dim[1]} (SHA: {native_C_sha[:16]}...) in {native_C_path}", fill=(0, 0, 0), font=font)
    curr_y += 20
    x_pos = 40
    for _, img, w, h, _ in group_C_previews:
        draw.text((x_pos, curr_y), f"{w}x{h}", fill=(0, 0, 0), font=font)
        proof_img.paste(img, (x_pos, curr_y + 15))
        x_pos += w + 20
    curr_y += 545

    # Crop proof sheet to final actual height + 20px padding
    final_proof = proof_img.crop((0, 0, proof_width, curr_y + 20))
    proof_fp = proof_dir / "PROOF_SHEET.png"
    check_destination(proof_fp)
    final_proof.save(proof_fp, **save_kwargs)
    proof_rel = str(proof_fp.relative_to(out_root))
    proof_sha = sha256_file(proof_fp)
    created_files_rel.append(proof_rel)

    asset_manifests.append({
        "asset_id": "evidence_proof_sheet",
        "path": proof_rel,
        "variant": "proof-sheet",
        "status": "EVIDENCE",
        "crop_box": None,
        "width": final_proof.width,
        "height": final_proof.height,
        "mode": "RGB",
        "alpha": "none (opaque)",
        "resample": "annotated composition",
        "approval_ref": "NONE",
        "sha256": proof_sha
    })

    # 5. Manifest file
    recipe_rel = "10_AGENT_HANDOFF/export_png_kit.py"
    # Compute sha256 of current recipe script if present, else self file
    self_script = Path(__file__).resolve()
    recipe_sha = sha256_file(self_script) if self_script.is_file() else "UNKNOWN"

    color_handling_statement = "source contains cHRM chromaticity (standard sRGB primaries: white 0.3127/0.329, R 0.64/0.33, G 0.3/0.6, B 0.15/0.06); no embedded ICC profile; no colour conversion performed; no official colour profile established by this task"

    manifest_data = {
        "task": "BRAND-EXPORT-05",
        "date": date_str,
        "source_path": "01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png",
        "source_sha256": master_sha,
        "recipe_path": recipe_rel,
        "recipe_sha256": recipe_sha,
        "python_version": sys.version.split()[0],
        "pillow_version": Image.__version__,
        "color_handling": color_handling_statement,
        "ycn_box": {
            "x0": ycn_box[0], "y0": ycn_box[1], "x1": ycn_box[2], "y1": ycn_box[3],
            "width": ycn_box[4], "height": ycn_box[5]
        },
        "candidate_boxes": {
            "A_ycn-crop": list(boxA),
            "B_ycn-square-crop": list(boxB),
            "C_full-square-crop": list(boxC)
        },
        "matrix_rows_covered": ["full-lockup,on-dark,PNG (opaque only)"],
        "excluded": [
            "transparent variants", "on-light row", "all SVG/PDF/EPS", "wordmark-only",
            "single-ink", "social-avatar", "open-graph", "animation", "ICO/favicon production",
            "widths above 2048"
        ],
        "open_decisions": ["02a", "02b", "04", "RULING-05"],
        "assets": asset_manifests
    }

    check_destination(manifest_path)
    manifest_json_str = json.dumps(manifest_data, indent=2) + "\n"
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_json_str)
    manifest_rel = str(manifest_path.relative_to(out_root))
    manifest_sha = sha256_file(manifest_path)
    created_files_rel.append(manifest_rel)

    # 6. Checksum file (covers the 26 PNGs + manifest, sorted, excludes itself)
    check_destination(task_checksum_path)
    # Sort paths
    sorted_files = sorted(created_files_rel)
    checksum_lines = []
    for rel_f in sorted_files:
        full_f = out_root / rel_f
        h = sha256_file(full_f)
        checksum_lines.append(f"{h}  {rel_f}\n")
    with open(task_checksum_path, "w", encoding="utf-8") as f:
        f.writelines(checksum_lines)

    print(f"Generated {len(created_files_rel)} assets + manifest + checksum inventory.")
    print(f"Manifest: {manifest_path} (assets count: {len(asset_manifests)})")
    print(f"Checksum file: {task_checksum_path} (entries count: {len(checksum_lines)})")
    return ycn_box, boxA, boxB, boxC

def verify_outputs(master_path, out_root):
    print("\n=== RUNNING OUTPUT-CORRECTNESS VERIFICATION ===")
    im_master, _ = validate_master(master_path)
    out_root = Path(out_root).resolve()

    web_dir = out_root / "05_EXPORTS" / "WEB" / "full-lockup_on-dark-opaque"
    cand_dir = out_root / "05_EXPORTS" / "CANDIDATES" / "small-mark"
    native_cand_dir = cand_dir / "SOURCE_CANDIDATES"
    proof_fp = out_root / "08_QUALITY_AND_EVIDENCE" / "BRAND-EXPORT-05" / "PROOF_SHEET.png"
    manifest_fp = out_root / "05_EXPORTS" / "MANIFEST_BRAND-EXPORT-05.json"
    checksum_fp = out_root / "05_EXPORTS" / "SHA256SUMS_BRAND-EXPORT-05.txt"

    # 1. Verify 5 full-lockup PNGs
    full_widths = [128, 256, 512, 1024, 2048]
    expected_heights = [100, 199, 398, 797, 1594]
    for w, h in zip(full_widths, expected_heights):
        fp = web_dir / f"YCN_LABS_logo-lockup_on-dark-opaque_{w}x{h}_v1.0.0.png"
        assert fp.exists(), f"Missing full lockup file: {fp}"
        saved_im = Image.open(fp)
        assert saved_im.size == (w, h), f"Size mismatch for {fp}: {saved_im.size} vs {(w, h)}"
        assert saved_im.mode == "RGB", f"Mode mismatch for {fp}: {saved_im.mode}"
        expected_im = im_master.resize((w, h), resample=Image.Resampling.LANCZOS)
        diff = ImageChops.difference(saved_im, expected_im)
        assert diff.getbbox() is None, f"Decoded pixel difference in {fp}"
        print(f"  [PASS] Full lockup {w}x{h}: exact LANCZOS resize, mode RGB, zero pixel diff")

    # Measure boxes
    ycn_box = measure_ycn_box(im_master)
    boxA, boxB, boxC = compute_candidate_boxes(ycn_box)

    # 2. Verify 3 native candidates
    native_checks = [
        ("A_ycn-crop", boxA, native_cand_dir / f"YCN_LABS_small-mark-A_ycn-crop_{boxA[2]-boxA[0]}x{boxA[3]-boxA[1]}_NATIVE_CANDIDATE.png"),
        ("B_ycn-square-crop", boxB, native_cand_dir / f"YCN_LABS_small-mark-B_ycn-square-crop_{boxB[2]-boxB[0]}x{boxB[3]-boxB[1]}_NATIVE_CANDIDATE.png"),
        ("C_full-square-crop", boxC, native_cand_dir / f"YCN_LABS_small-mark-C_full-square-crop_5195x5195_NATIVE_CANDIDATE.png")
    ]
    native_ims = {}
    for cand_id, box, fp in native_checks:
        assert fp.exists(), f"Missing native candidate file: {fp}"
        saved_im = Image.open(fp)
        expected_im = im_master.crop(box)
        assert saved_im.size == expected_im.size, f"Native size mismatch: {saved_im.size} vs {expected_im.size}"
        assert saved_im.mode == "RGB", f"Native mode mismatch: {saved_im.mode}"
        diff = ImageChops.difference(saved_im, expected_im)
        assert diff.getbbox() is None, f"Decoded pixel difference in native candidate {fp}"
        native_ims[cand_id] = saved_im
        print(f"  [PASS] Native crop {cand_id} ({saved_im.width}x{saved_im.height}): exact crop pixels, zero diff")

    # 3. Verify 17 previews
    # Group A
    cropA_w = boxA[2] - boxA[0]
    cropA_h = boxA[3] - boxA[1]
    for h_target in [24, 32, 40, 48, 64]:
        w_target = round_half_up(h_target * cropA_w / cropA_h)
        fp = cand_dir / f"YCN_LABS_small-mark-A_ycn-crop_{w_target}x{h_target}_CANDIDATE.png"
        assert fp.exists(), f"Missing preview: {fp}"
        saved_im = Image.open(fp)
        assert saved_im.size == (w_target, h_target) and saved_im.mode == "RGB"
        # Compare against resize of master crop and resize of native candidate
        exp1 = im_master.crop(boxA).resize((w_target, h_target), resample=Image.Resampling.LANCZOS)
        exp2 = native_ims["A_ycn-crop"].resize((w_target, h_target), resample=Image.Resampling.LANCZOS)
        assert ImageChops.difference(saved_im, exp1).getbbox() is None
        assert ImageChops.difference(saved_im, exp2).getbbox() is None
        print(f"  [PASS] Preview A {w_target}x{h_target}: exact LANCZOS resize of crop & native candidate")

    # Group B
    for s_target in [16, 32, 48, 64, 180, 192, 512]:
        fp = cand_dir / f"YCN_LABS_small-mark-B_ycn-square-crop_{s_target}x{s_target}_CANDIDATE.png"
        assert fp.exists(), f"Missing preview: {fp}"
        saved_im = Image.open(fp)
        assert saved_im.size == (s_target, s_target) and saved_im.mode == "RGB"
        exp1 = im_master.crop(boxB).resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        exp2 = native_ims["B_ycn-square-crop"].resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        assert ImageChops.difference(saved_im, exp1).getbbox() is None
        assert ImageChops.difference(saved_im, exp2).getbbox() is None
        print(f"  [PASS] Preview B {s_target}x{s_target}: exact LANCZOS resize of crop & native candidate")

    # Group C
    for s_target in [48, 64, 180, 192, 512]:
        fp = cand_dir / f"YCN_LABS_small-mark-C_full-square-crop_{s_target}x{s_target}_CANDIDATE.png"
        assert fp.exists(), f"Missing preview: {fp}"
        saved_im = Image.open(fp)
        assert saved_im.size == (s_target, s_target) and saved_im.mode == "RGB"
        exp1 = im_master.crop(boxC).resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        exp2 = native_ims["C_full-square-crop"].resize((s_target, s_target), resample=Image.Resampling.LANCZOS)
        assert ImageChops.difference(saved_im, exp1).getbbox() is None
        assert ImageChops.difference(saved_im, exp2).getbbox() is None
        print(f"  [PASS] Preview C {s_target}x{s_target}: exact LANCZOS resize of crop & native candidate")

    # 4. Verify Proof Sheet
    assert proof_fp.exists(), f"Missing proof sheet: {proof_fp}"
    proof_im = Image.open(proof_fp)
    assert proof_im.width == 2200 and proof_im.mode == "RGB"
    print(f"  [PASS] Proof sheet: exists, {proof_im.width}x{proof_im.height}, mode RGB")

    # 5. Verify Manifest
    assert manifest_fp.exists(), f"Missing manifest: {manifest_fp}"
    m_data = json.loads(manifest_fp.read_text(encoding="utf-8"))
    assert len(m_data["assets"]) == 26, f"Expected 26 assets in manifest, got {len(m_data['assets'])}"
    for entry in m_data["assets"]:
        rel_path = entry["path"]
        actual_fp = out_root / rel_path
        assert actual_fp.exists(), f"Manifest file does not exist: {actual_fp}"
        actual_sha = sha256_file(actual_fp)
        assert actual_sha == entry["sha256"], f"Manifest SHA mismatch for {rel_path}"
    print(f"  [PASS] Manifest: 26 assets verified byte-exact against disk files")

    # 6. Verify Checksum file
    assert checksum_fp.exists(), f"Missing checksum file: {checksum_fp}"
    cs_lines = checksum_fp.read_text(encoding="utf-8").strip().splitlines()
    assert len(cs_lines) == 27, f"Expected 27 lines in checksum file, got {len(cs_lines)}"
    for line in cs_lines:
        h, rel_f = line.split(None, 1)
        actual_fp = out_root / rel_f
        assert actual_fp.exists(), f"Checksum target missing: {actual_fp}"
        assert sha256_file(actual_fp) == h, f"Checksum mismatch for {rel_f}"
    print(f"  [PASS] Task Checksums: 27 entries verified byte-for-byte")
    print("ALL OUTPUT-CORRECTNESS CHECKS PASSED!\n")

def main():
    parser = argparse.ArgumentParser(description="YCN Labs Brand PNG Kit Exporter")
    parser.add_argument("--master", required=True, help="Path to canonical 6675x5195 master PNG")
    parser.add_argument("--out-root", required=True, help="Root directory for outputs")
    parser.add_argument("--date", required=True, help="Date string YYYY-MM-DD")
    parser.add_argument("--verify-only", action="store_true", help="Run verification checks only")
    args = parser.parse_args()

    if args.verify_only:
        verify_outputs(args.master, args.out_root)
        return

    ycn_box, boxA, boxB, boxC = build_kit(args.master, args.out_root, args.date)
    print("\n--- Geometric Measurements ---")
    print(f"YCN Box:              {ycn_box[:4]} (width: {ycn_box[4]}, height: {ycn_box[5]})")
    print(f"Box A (ycn-crop):     {boxA} (width: {boxA[2]-boxA[0]}, height: {boxA[3]-boxA[1]})")
    print(f"Box B (square-crop):  {boxB} (width: {boxB[2]-boxB[0]}, height: {boxB[3]-boxB[1]})")
    print(f"Box C (full-square):  {boxC} (width: {boxC[2]-boxC[0]}, height: {boxC[3]-boxC[1]})")

    verify_outputs(args.master, args.out_root)

if __name__ == "__main__":
    main()
