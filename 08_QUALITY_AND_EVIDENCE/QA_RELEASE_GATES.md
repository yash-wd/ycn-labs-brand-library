# Release Acceptance Gates — YCN Labs Brand Assets

**Controlling Authority:** `00_GOVERNANCE/CURRENT_SOURCE_AUTHORITY.md`  
**Rule:** No gate skipping. Verification must be reproducible and documented.

---

## Gate 0 — Source Integrity Verification (Mandatory Baseline)

Validate both primary source images against their exact recorded dimensions, byte counts, color profiles, and SHA-256 hashes. Do not auto-process or modify.

1. **Authoritative Master Source (6675×5195 RGB, RULING-01):**
   - Path: `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png` (Desktop copy: `/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png`)
   - Dimensions: **6675 × 5195 pixels**
   - Format: **PNG, 8-bit RGB** (opaque `#000205` / `[0, 1, 6]` field)
   - File Size: **6,633,409 bytes**
   - SHA-256: `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`
   - Gate Requirement: Bit-for-bit SHA-256 match. Aspect ratio 1.284889.

2. **Uploaded Reference Copy (2048×1593 RGBA):**
   - Path: `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`
   - Dimensions: **2048 × 1593 pixels**
   - Format: **PNG, 8-bit RGBA** (all pixels alpha == 255, opaque field)
   - File Size: **3,158,172 bytes**
   - SHA-256: `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`
   - Gate Requirement: Bit-for-bit SHA-256 match.

Fail immediately on any byte or hash mismatch across destination or backup copies.

---

## Gate 1 — Preservation and Visual Inventory

- At 100% and 400%, compare all source details: faint constellation lines, celestial node rings, outer crescent contour curvature, YCN breaks, LABS tracking, and underline flare.
- Record bounding boxes and artwork landmarks; zero clipping.
- Verify sub-pixel registration between the 6675 Master and 5620 candidate derivatives (integer offset dx=663, dy=320).

---

## Gate 2 — Reconstruction & Derivative Candidates (RULING-02 / Vector Brief)

- Transparent raster derivative approval requires Owner visual review of `08_QUALITY_AND_EVIDENCE/RULING-02/RULING-02-SHEET.png` and recorded ruling (**RULING-02**).
- For vector master candidates (v2.0):
  - Record actual authoring tools, layered Bézier structure, and styling attributes.
  - Strictly **NO auto-traced vectors** or embedded-raster SVGs passed off as vector geometry.
  - Compare side-by-side against the 5620/6675 underlay at matched scale in controlled color profiles.
  - Measure region-specific overlays, boundary strokes, and gradient falloffs. Global average pixel differences dominated by black background are invalid.
  - Test on both light and dark host surfaces across display sizes (16, 32, 48, 64, 128, 256, 512, 1024, 2048).
  - Owner must visually approve specific candidate versions and hashes. Technical scores alone cannot supersede human visual approval.

---

## Gate 3 — Export Reproducibility (BRAND-EXPORT-05)

- Every production derivative must originate deterministically from the approved master artwork.
- Record exact rasterizer, resampling filter (Lanczos), canvas dimensions, padding, background/alpha, and metadata.
- Zero stretching, non-proportional scaling, color casts, clipping, or unexpected matte fringing.
- Checksums and manifests automatically generated; repeated runs must produce bit-identical files (accounting for known encoder metadata differences).

---

## Gate 4 — Theme Variants and Surface Treatments

- **Dark Surfaces:** Approved dark artwork with luminous glows.
- **Light Surfaces:** Prior to independent approval of an on-light recolored artwork, light-theme placements must use a dark tile panel treatment (**RULING-04**).
- CMYK artwork and print proofs must be validated independently; sRGB display values do not guarantee physical color fidelity on paper or fabric.

---

## Gate 5 — Production Release and Website Rollout

- Owner explicitly approves named asset release and checksums.
- Public website repository (`ycn-labs-site`) updated strictly under a separate, authorized integration task.
- Zero website modification during brand archive work. Rollback copies preserved.

---

## Gate 6 — Governance & Repository Security

- Maintain secure backups (local vault, Git history, external offsite backup).
- Public repository visibility is temporary during active brand work; migration to private storage planned upon project completion.
- Trademarks and proprietary rights protected; no permissive software licenses applied to logo artwork.
- Rejected, legacy, or prototype assets kept quarantined and clearly labeled in `11_HISTORICAL_ASSETS/`, never silently overwritten.
