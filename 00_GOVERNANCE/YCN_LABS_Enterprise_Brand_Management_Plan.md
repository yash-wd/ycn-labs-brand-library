# YCN Labs — Enterprise Brand Identity Management Plan
**Source authority date:** 13 October 2026  
**Status:** Owner-supplied logo source verified. Production derivatives pending separate approval.

## 1. The immutable identity

Only the directly uploaded `Main_YCN_LABS_logo_black_8K.png` is the authoritative design reference. Do not promote an older image, vector or design candidate on the basis of its filename or prior decision history. Register a new Owner decision superseding conflicting statements about source authority without erasing existing historical decisions.

- Pixels: 2048 × 1593; not 8K despite the filename.
- Format: PNG, 8-bit RGBA; no transparent pixels (alpha=255 throughout).
- Bytes: 3,158,172.
- ICC profile: none embedded; sRGB interpretation provisional.
- SHA-256: `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`.
- Characteristics: black/blue-black background, curved blue luminous crescent, ring/nodes, constellation strokes, custom white YCN, cyan LABS, delicate underline and terminal flare.

Keep this original intact. PNG copying can be *bit-for-bit exact*. Enlarging it cannot recover absent vector geometry. A flat raster cannot be turned into guaranteed pixel-identical, endlessly scalable geometry with a one-click trace. Transparent-background extraction is particularly risky for this logo because very dark linework and glow are composited into the opaque dark canvas.

## 2. Enterprise asset hierarchy

- `00_GOVERNANCE/`: Owner decision records, provenance, rights/trademark register, asset-status approvals, versioning, changelog, distribution permissions.
- `01_IMMUTABLE_SOURCE/`: Original uploaded source, exact bytes, read-only checksum and backup copies.
- `02_BRAND_DESIGN/`: Visual anatomy, geometry inventory, spacing and typography studies; no unapproved design changes.
- `03_VECTOR_RECONSTRUCTION/`: Candidate layered/vector/hybrid sources, method and limitations, optical alignment proofs. **Not an official master unless signed off.**
- `04_APPROVED_LOGO_VARIANTS/`: After signoff, on-dark/on-light full lockup, symbol and wordmark where approved, monochrome and small-scale versions.
- `05_EXPORTS/{WEB,APP,PRINT,SOCIAL,VIDEO}/`: Generated derivatives only, from approved release; explicit dimensions, color mode, alpha and hashes.
- `06_DESIGN_TOKENS/`: Approved RGB/sRGB color hex, gradients, typography, CMYK after proofing, accessibility references. Samples remain `DRAFT` until ratified.
- `07_GUIDELINES/`: Clear-space rules, minimum display sizes, prohibited changes, backgrounds, placement, accessibility, co-branding, printer and accessibility instructions.
- `08_QUALITY_AND_EVIDENCE/`: QA test plans, rendered pixel comparisons, print proofs, checksum verification, tool versions and Owner visual approvals.
- `09_RELEASES/`: Locked numbered releases, manifest, SHA-256, rollback, distribution packages, export scripts, approved usage docs.
- `10_AGENT_HANDOFF/`: One approved task per message, scope, stop conditions, raw audit evidence.

## 3. Required artwork/formats and when

| Family | Preferred deliverables | Source status / limitation |
|---|---|---|
| Full official composition | Original PNG | **Approved**, can copy unchanged. |
| Full on-dark responsive variants | PNG 256/512/1024/2048, optional WebP/AVIF | Lossless PNG can downsize existing pixels; validate fine details before release. |
| On-light usage | Original entire composition inside an unchanged dark panel | No change to artwork. Transparent/light-field adaptation needs separate Owner approval. |
| True resolution-independent source | Native editable SVG paths / suitable professional editor file | Needs precision manual vector/hybrid reconstruction and proof; original may require rasterized glow layer. |
| Mark-only | Owner-approved paths, PNG sizes 16/32/48/180/192/512 | Does **not** currently exist as independently approved official artwork. |
| Wordmark-only | Owner-approved full-resolution SVG/PNG | Requires cutout/trace and Owner approval. |
| Print | PDF/X-4, proofed CMYK, optionally EPS as needed | Only after approved vector/hybrid master and vendor proofs. |
| Social | PNG 400/800/1024, OG 1200×630 | Compositions are exports/templates, not replacement logos. |
| Video | Lossless quality archive + approved video-safe overlays | Transparency and motion need authorization; keep original unchanged. |

No file named 8K shall be represented as actual 8192px detail unless the source geometry and render genuinely support that output. Raster transparent PNG is not infinitely scalable. No print profile, Pantone ID, font family, gradient stop or clear-space dimension should be invented and called official.

## 4. Sampled candidate palette (not approved color standards)

The only original color source is the flattened PNG. Sampled approximate RGB representatives, **not** the original artist's design palette:

| Role | Example sampled HEX |
|---|---|
| Near-black ink | `#000205` |
| Blue-black variation | `#000307` |
| Pale logo white | `#F8FAFC` |
| Electric cyan | `#0ADEF8` |
| Bright blue | `#05A9F3` |
| Deep bright blue | `#0279D7` |
| Dark blue | `#074D7C` |
| Cyan glow | `#43E7FB` |
| Ice cyan highlight | `#83F5FB` |

The full reference contains additional intermediate gradients, reflections, shadowing, halo and antialiasing colors. These approximate samples are useful for design research, not a license to recolor the original.

## 5. Dual theme, no design change

- **Dark context:** show the full original raster as supplied. Its black backdrop is part of the artwork.
- **White/light context:** preserve the exact original inside an inset dark panel on the white page. That gives two *presentation contexts*, not two different logo drawings.
- A clean transparent logo that sits directly on white, with dark-colored YCN letters and adjusted faint orbital strokes, is a **new derived artwork treatment** requiring explicit visual approval. It cannot be created without modifying the supplied pixels.

## 6. Release process (mandatory)

1. **SOURCE FREEZE:** hash-check Owner file, preserve unchanged, back up, add source record.
2. **TECHNICAL FEASIBILITY:** inspect exact geometry and faint pixels, choose manual vector/hybrid strategy with known limitations. No automated simplification.
3. **PRODUCTION PROOF:** build candidate geometry + glow; align to original at native size, zoomed crops and multiple usage sizes; record differences, no false 100% match claims.
4. **OWNER SIGN-OFF:** review full-screen overlays and comparison crops for on-dark; approve only specific files and hashes.
5. **THEME SIGN-OFF:** separate review for a transparent or light-field derivative if requested, or keep the original in a dark presentation frame for light websites.
6. **EXPORT AND QA:** deterministic tool/script, sharp geometry, no unexpected matte, anti-aliased perimeter tests, formats and size manifest.
7. **SITE INTEGRATION:** separate task with code tests, dark/light screenshots, responsive viewport coverage, rollback; do not disturb frozen website work in brand-design task.
8. **IMMUTABLE RELEASE:** versioned directory, `MANIFEST.json`, `SHA256SUMS.txt`, `CHANGELOG.md`, approval ID, scripts, archived release.

## 7. How this will be maintained

- **One source of truth:** Owner original + source fingerprint + approved derived master(s) with immutable release references. No “final2 / new-logo-v6 / final-final” naming.
- **Every export traceable:** manifest record `asset_id`, `source_sha`, `variant`, `format`, `dimensions`, `color_profile`, `alpha`, `tool_version`, `export_timestamp`, `file_sha`, `approval_ref`, `status`.
- **One controlled deployment point:** website BrandLogo component references approved versioned assets, not hand-copied files in many components; any replacing release is a reviewed task.
- **Backups:** three copies on two types of storage with an offsite copy and periodic checksum/restore tests. One laptop copy is not sufficient.
- **Access control:** editable source write access only to Owner/approved designers; read-only distribution kit for marketing/vendors; keep source outside the public web directory.
- **Legal:** record provenance, ownership, trademark/registration references where applicable; no trademark registration can be inferred merely from a logo image.
- **Deprecation:** keep historical references and obsolete assets quarantined until the production site has completed a safe staged migration; delete only with explicit Owner consent.

## 8. Immediate action

> **HISTORICAL — superseded 14 Oct 2026.** BRAND-SOURCE-CONTROL-03 is complete. The current next task is always the one named in `14_CONTINUITY/RESUME_HERE.md`.

Transfer the unchanged official PNG (directly or in the provided ZIP) to AGY. The first AGY task is **BRAND-SOURCE-CONTROL-03**, supplied in the foundation kit. It only verifies and stores the source, updates *proposed* governance records, and reports evidence. **No logo redraw, background removal, vector or website change** is approved by that task.

After AGY returns a passing source-freeze audit, obtain a precision reconstruction feasibility proposal. Approve production only when the method respects every fine detail. If exact optical equivalence is impossible, keep the source PNG as the sole official graphic and document the usage limitations.
