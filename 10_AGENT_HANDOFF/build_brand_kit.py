from pathlib import Path
import json,hashlib,shutil,zipfile,csv,os,datetime,textwrap,struct
from PIL import Image

source=Path('/mnt/data/Main_YCN_LABS_logo_black_8K.png')
root=Path('/mnt/data/YCN_LABS_BRAND_LIBRARY_SOURCE_FOUNDATION_2026-10-13')
root.mkdir(exist_ok=True)
sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943'
original_target=root/'01_IMMUTABLE_SOURCE'/source.name
original_target.parent.mkdir(exist_ok=True, parents=True)
shutil.copyfile(source,original_target)
assert hashlib.sha256(original_target.read_bytes()).hexdigest()==sha
im=Image.open(source)
assert im.size == (2048,1593)
assert im.getextrema()[-1] == (255,255)

paths = [
'00_GOVERNANCE', '02_BRAND_DESIGN', '03_VECTOR_RECONSTRUCTION', '04_APPROVED_LOGO_VARIANTS',
'05_EXPORTS/WEB', '05_EXPORTS/APP', '05_EXPORTS/PRINT', '05_EXPORTS/SOCIAL', '05_EXPORTS/VIDEO',
'06_DESIGN_TOKENS', '07_GUIDELINES', '08_QUALITY_AND_EVIDENCE', '09_RELEASES', '10_AGENT_HANDOFF'
]
for p in paths: (root/p).mkdir(parents=True, exist_ok=True)
def w(p,s):
 d=root/p;d.parent.mkdir(parents=True,exist_ok=True);d.write_text(textwrap.dedent(s).strip()+"\n",encoding='utf-8')

w('README.md',f'''# YCN Labs — Brand source foundation (13 October 2026)

**Status: Source frozen; production master vectors and theme variants NOT YET APPROVED.**

This package is the beginning of the production-grade brand management system. It does **not** claim to contain validated SVGs, transparent masters, matching light-background art, or all usable sizes. Those require a separate documented reconstruction and proof process.

## Authority

- The Owner designated exactly one upload, `{source.name}`, as the sole official visual reference. Previous candidate exports, alternate masters, generated images and site derivatives do not become authoritative merely by naming or earlier ratification.
- Original bytes are preserved unchanged at `01_IMMUTABLE_SOURCE/{source.name}`.
- SHA-256: `{sha}`.
- The original is **2048 × 1593** pixels, despite the filename saying “8K.” It is an **opaque RGBA** PNG: all pixels have alpha 255, including the black backdrop.
- Existing `YCN_DECISIONS.md` decisions remain historical; a new owner decision should **supersede conflicting asset-source references without deleting history**.

## Start here

1. `00_GOVERNANCE/OWNER_SOURCE_RULING.md` — Owner authority and change control.
2. `02_BRAND_DESIGN/ARTWORK_INVENTORY.md` — required preserved visible elements.
3. `06_DESIGN_TOKENS/SAMPLED_PALETTE.json` — **measured candidate** colors, not original design values.
4. `07_GUIDELINES/BRAND_USAGE_DRAFT.md` — rules for dark and light surfaces.
5. `03_VECTOR_RECONSTRUCTION/FEASIBILITY_AND_BRIEF.md` — why exact vector recovery is not guaranteed.
6. `05_EXPORTS/EXPORT_MATRIX.csv` — required variants and release gates.
7. `08_QUALITY_AND_EVIDENCE/QA_RELEASE_GATES.md` — what must pass before a file is called official.
8. `10_AGENT_HANDOFF/AGY_TASK_BRAND_SOURCE_CONTROL_03.md` — one safe next task for AGY.

## Meaning of folders

- `01_IMMUTABLE_SOURCE` = only approved artwork presently provided.
- `03_VECTOR_RECONSTRUCTION` = work and specifications, **not** approval.
- `04_APPROVED_LOGO_VARIANTS` = intentionally empty until Owner approves derivative artwork.
- `05_EXPORTS` = intentionally empty of export assets until their source and QA are approved.
- `09_RELEASES` = no production release until sign-off and verification.

## Important fidelity rule

The original source file is pixel-perfect only when copied byte-for-byte. Upscaling the PNG, auto-removing its black background, AI-regenerating its geometry, or converting it to SVG by simply embedding the PNG **does not** produce a native, infinitely scalable equivalent. Keep the original as the ultimate reference and label all prospective reconstructions separately.

## Transfer to AGY

AGY cannot access the ChatGPT file sandbox automatically. Download this package and transfer the unmodified source file to the designated local intake directory. AGY must independently verify the expected hash before copying/archiving. A ZIP is a lossless delivery container: extraction returns exactly the original PNG bytes.
''')

w('00_GOVERNANCE/OWNER_SOURCE_RULING.md',f'''# BRAND-SOURCE-OWNER-RULING — 2026-10-13

**Authority:** Owner's latest explicit instruction in conversation.

**Brand:** YCN Labs.

**Sole official visual reference:** `{source.name}` (SHA-256 `{sha}`).

**Non-negotiable:** Never alter logo artwork: no changes to YCN/LABS lettering, orbital crescent, fine lines, nodes, dimensions/proportions, gradients, glow, underline, highlight points, or intentional black canvas.

**Conflict treatment:** Prior decisions, including the previously referenced DECISION-050 PNG lineage, may describe historical website delivery baselines; they do not override the newly supplied sole official original. Record a new decision explicitly superseding old *source authority* where conflicting, without rewriting historical entries. No code or production site changes without separate Owner approval.

**Derived assets:** Candidate / DRAFT until proof, technical review, and the Owner visually signs off a specific file hash. Derivatives can include different delivery sizes without redrawing; new silhouettes, recolors, transparent versions, symbol-only, wordmark-only, monochrome or light-background adaptations are separate derivative decisions, not automatic authorization.

**Permitted before approval:** Byte-for-byte archival, metadata inspection, non-destructive preview proofs clearly labeled DRAFT, QA scripts and specs.

**Prohibited before approval:** Publish or distribute a reconstruction as official; replace website files; change artwork; bulk 'clean up' or delete archives; rename/rewrite original; upscale and relabel as 8K; use AI image generation to redraw the logo; claim exact image-to-vector identity without evidence.

**Sign-off record:** Owner identity, decision date, reference SHA-256, derivative SHA-256, preview link, written approval, reviewer, semantic version. Populate those only when an approval actually occurs.
''')

w('00_GOVERNANCE/STATUS_AND_CHANGES.md','''# Current status / changelog

## SOURCE-v1.0.0 — 2026-10-13
- Original user-supplied file preserved byte-identically.
- Source audit performed: dimensions, image format, alpha coverage, ICC metadata.
- Provisional palette sampled for design analysis only.
- Documents and release gates drafted; **no derivative logo files are approved**.

## Unresolved approvals
- Owner verification of source record at AGY workstation after transfer.
- Production technique for orbit/crescent/gradient/particles/glow.
- Whether dark backed presentation is sufficient on white pages.
- Whether symbol-only and monochrome versions are necessary and approved.
- CMYK and vendor print-proof color approval.
- Full vector/manual reconstruction acceptance.
''')

meta={'brand':'YCN Labs', 'asset_role':'SOLE_OWNER_SUPPLIED_OFFICIAL_ORIGINAL', 'source_status':'IMMUTABLE_MASTER_RASTER', 'source_filename':source.name,
      'sha256':sha,'bytes':source.stat().st_size,'width_px':2048,'height_px':1593,'aspect_ratio':round(2048/1593,9),
      'format':'PNG','channels':'8-bit RGBA','alpha_coverage':'fully opaque (all 255)', 'embedded_icc_profile':False,
      'transparent':False,'owner_designation_date':'2026-10-13','approved_variants':[],
      'caution':'No true independent scalable vector can be proven exact using this file alone.'}
(root/'00_GOVERNANCE'/'SOURCE_RECORD.json').write_text(json.dumps(meta,indent=2)+'\n')
(root/'01_IMMUTABLE_SOURCE'/'SHA256SUMS.txt').write_text(f'{sha}  {source.name}\n')

w('02_BRAND_DESIGN/ARTWORK_INVENTORY.md','''# Visible components of the sole approved raster source

The following elements must be accounted for, not redesigned:

1. Near-black / blue-black opaque background with subtle tonal variation. The background is **part of the supplied image**, not transparent.
2. Broad left crescent, cyan-to-electric-blue highlights and feathered luminous edge.
3. Upper/lower thin orbital arcs crossing and wrapping the crescent, with small terminal ends.
4. Several nodes and concentric outlined circles, each at its existing location.
5. Fine blue connecting constellation/network strokes, including very faint lines that are easy for automated tracing to erase.
6. Bright white/very pale blue stylized custom “YCN” lettering with distinctive breaks and precise edge geometry.
7. Wide-spaced cyan/blue “LABS” letters with custom styling/gradient, baseline relationship and exact tracking.
8. Thin luminous underline and bright terminal flare on the right.
9. Luminous halos, gradients, gradients of brightness, soft edges, white highlights, internal shadowing and subtle antialiasing.
10. All original negative spaces, overlaps, optical balances, microdetails, crop and relative placement.

**Do not infer a typeface.** YCN and LABS are artwork. Any future outline/path files must visually preserve their letterforms, not substitute text.

## Optical scaling note

The full logo is extremely complex. At favicon sizes the faint constellation is below pixel resolution. A small-size companion icon may need a separately approved optical adaptation rather than pretending the full lockup stays readable at 16px.
''')

palette=[
 {'token':'candidate.ink.background','hex':'#000205','rgb':[0,2,5], 'role':'near-black sampled field, approximate', 'approval':'NOT_APPROVED'},
 {'token':'candidate.ink.deep','hex':'#000307','rgb':[0,3,7], 'role':'near-black subtle variation', 'approval':'NOT_APPROVED'},
 {'token':'candidate.lettering.white','hex':'#F8FAFC','rgb':[248,250,252], 'role':'light lettering median bright region', 'approval':'NOT_APPROVED'},
 {'token':'candidate.cyan.primary','hex':'#0ADEF8','rgb':[10,222,248], 'role':'sampled cyan cluster', 'approval':'NOT_APPROVED'},
 {'token':'candidate.blue.electric','hex':'#05A9F3','rgb':[5,169,243], 'role':'sampled bright blue cluster', 'approval':'NOT_APPROVED'},
 {'token':'candidate.blue.deep','hex':'#0279D7','rgb':[2,121,215], 'role':'sampled rich blue cluster', 'approval':'NOT_APPROVED'},
 {'token':'candidate.blue.shadow','hex':'#074D7C','rgb':[7,77,124], 'role':'sampled dim blue cluster', 'approval':'NOT_APPROVED'},
 {'token':'candidate.cyan.glow','hex':'#43E7FB','rgb':[67,231,251], 'role':'sampled high luminance cyan cluster', 'approval':'NOT_APPROVED'},
 {'token':'candidate.cyan.ice','hex':'#83F5FB','rgb':[131,245,251], 'role':'sampled near-white cyan highlight', 'approval':'NOT_APPROVED'},
]
pal={'source_file':source.name, 'source_sha256':sha,'status':'PROVISIONAL_MEASURED_SWATCHES_NOT_A_BRAND_TOKEN_CONTRACT',
     'method':'dominant near-black / pale samples plus exploratory color clusters from sampled saturated blue/cyan pixels; gradient stops not recovered',
     'important':'The original PNG contains composite gradients and glow. HEX values are approximate sample representatives, not proven authoring swatches or vector gradient stops. Do not recolor the artwork using these guesses.',
     'color_management':'No embedded ICC in the image; interpret as sRGB provisionally and embed a controlled output profile after proof; archive source bytes unchanged.',
     'swatches':palette}
(root/'06_DESIGN_TOKENS'/'SAMPLED_PALETTE.json').write_text(json.dumps(pal,indent=2)+'\n')
w('06_DESIGN_TOKENS/COLOR_AND_TYPE_POLICY.md','''# Color and lettering policy

- `SAMPLED_PALETTE.json` contains **estimated sampled reference colors**, not approved primary/secondary brand colors.
- There is no original layered/source design palette; a flattened raster cannot uniquely reveal original design gradient stops, blend modes, halo radius, or font names.
- Keep this image intact. Exact hand-matched colors, gradients and glows must be reconstructed under visual proof, then ratified as production design tokens.
- Never change a source pixel to fit a supposed palette.
- Color specification for mature release: sRGB HEX, RGB, approved gradient stops and transparency/glow behavior; additionally print-proofed CMYK and optional Pantone cross-reference **only after print vendor proof**, not guessed conversions.
- Type: exact lettering is custom visual artwork. External brand typography (headings/body) is a **separate** design-system decision; do not infer a font family from this logo.
- Colors used for product UI may be adapted for accessibility but that does **not** authorize changing approved logo pixels.
- Ensure 'on-light' and 'on-dark' naming identifies the intended **background**, not merely the filename's dark/light wording.
''')

w('03_VECTOR_RECONSTRUCTION/FEASIBILITY_AND_BRIEF.md','''# Precision reconstruction brief — not approval to redraw

## Engineering truth

- PNG is a raster grid of 2048 × 1593 pixels with opaque background, no independent art layers.
- There is **no guaranteed reversible operation** to recover original Bézier geometry, text vectors, gradient stops, soft blur/glow sources or transparency from that flattened result.
- Typical auto-tracing smooths strokes, merges near-dark lines into the background and alters flare/glow. Therefore it is unsuitable as a one-click production master here.
- Wrapping an `<image>` tag inside SVG does not make native resolution-independent vector art.
- A useful future **hybrid** logo might combine verified vector paths for lettering/geometry with tested resolution-aware raster/gradient glow effects. State limitations rather than declaring all-vector falsely.

## Proposed production method (subject to separate explicit approval)

1. Freeze and verify original source, visual reference and metadata.
2. Decompose visually into planes: dark field; crescent; orbital lines; connectivity; nodes; YCN paths; LABS paths; underline; glows.
3. Carefully trace or reconstruct crisp geometry from the reference; preserve angles, gaps, dot positions, tracking and curves.
4. Treat blue gradients and volumetric luminous halos as separate test layers, with original image remaining authority.
5. Pixel-aligned overlays at identical geometry (no aspect-ratio changes or arbitrary bounding-box stretching); use color difference, alpha/edge metrics, region-specific geometry inspection, missing-element check, and human overlay review.
6. Verify at natural size, at high zoom and on standard light/dark presentation contexts; run against original source screenshot without color management ambiguity.
7. Create a draft SVG and production-proof PNG *only if the Owner authorizes this phase*. Do not distribute as approved pending actual visual sign-off.
8. If exact fidelity is not achievable, keep original raster as only official visual and explicitly limit sizes/usage. Do not fake '8K' or overpromise infinite detail.

## Explicit unacceptable outcomes

- Missing or thickened connecting lines.
- Flattened crescent gradients, altered glow positions, simplified circular nodes.
- Incorrect stylized YCN lettering, changed LABS tracking, missing underline flare.
- Black background removal that drops the faint network or introduces visible dark/white fringe.
- New shadow, tint, bloom, ornament, font or rebalanced spacing.
- 'AI-enhanced' or hallucinated missing detail represented as exact reproduction.

## Required deliverables from a reconstruction vendor

Editable geometry master (e.g., SVG/AI source if truly vector), layer/provenance documentation, optical comparison proofs, any raster glow ingredients explicitly labeled, human visual QA record, operating/rendering dependencies, export recipe, color-management choices, final Owner approval record with asset hashes.
''')

w('04_APPROVED_LOGO_VARIANTS/README.md','''# No derivative logo has been approved yet

The sole official file is in `01_IMMUTABLE_SOURCE`.

Do not place generated/vector/transparent/recolored/monochrome/mark-only derivatives here before written Owner approval referencing the exact file checksum and preview.

Desired future logo forms (subject to proof and owner acceptance):
- full-lockup / on-dark and on-light presentation
- symbol-only / on-dark and on-light if extractable and approved
- wordmark-only / on-dark and on-light if extractable and approved
- monochrome/1-color optical versions if needed for manufacturing and explicitly approved
- small-size simplified icon if required and separately approved

No new visual design is implicitly authorized by this folder plan.
''')

w('07_GUIDELINES/BRAND_USAGE_DRAFT.md','''# YCN Labs — logo usage policy (DRAFT)

## Universal rules

- Logo mark, lettering, gradient, orbital details, faint nodes and glow come only from the final approved files. No unofficial redraws or AI-generated recreations.
- Never stretch/non-uniformly resize, skew, distort, rotate, recolor, sharpen destructively, remove components, add fonts, paste other logos inside, or mix parts from different versions.
- Do not crop visible nodes, orbit terminals or flare. Respect whole-source aspect ratio 2048:1593 unless a distinct, Owner-approved crop/lockup exists.
- Size only proportionally. Avoid JPEG as a transparency master; PNG is lossless but finite-resolution. WEBP/AVIF may be web delivery variants but never supersede source PNG.
- Clear space must be computed from measured outer artwork bounds after source decomposition and approved with actual usage proofs; **do not invent an official X-based clearance yet**.
- Minimum usable printed/digital sizes must be verified by optical proofs for full logo and mark-only variants; current detailed composition will not work at every icon size.
- Do not use the untagged PNG color values as CMYK/Pantone standards without proofing. Supply local printing vendor with intended physical dimensions/material/substrate to assess resolution and glow reproductions.

## Dark theme

- The original opaque dark-background artwork is the sole currently authorized presentation. Use it as a complete image without keying out black pixels or recoloring elements. Test visual seam against host background.

## Light theme — strict interpretation of 'no changes'

- To show this exact logo on a white page **without changing its artwork**, use the untouched, complete dark-background image as an inset dark panel/card. Surrounding white layout is allowed; the official image itself is unchanged.
- A transparent logo or dark-colored YCN lettering on a white canvas requires color/alpha adaptation. That is a distinct derivative and needs the Owner's explicit visual approval, even when geometry is preserved.

## Accessibility

- Provide alternative text `YCN Labs`. Logo contrast and readability should be evaluated over all host backgrounds. WCAG's logo-text contrast exception is not a license for unreadable treatment. Product/UI text should meet normal accessibility contrast requirements without recoloring the official logo.

## Governance

- Every production usage links to an approved release identifier, source SHA-256 and per-export checksum.
- For any change to the visual identity: new Owner decision; old versions retained in read-only historical release directory.
- Asset release tags proposed: `SOURCE-v1.0.0` (approved source), `DERIVATIVE-v1.0.0-DRAFT` until signed off, then `LOGO-SYSTEM-v1.0.0`.
''')

w('07_GUIDELINES/PLACEMENT_AND_PRINT_DRAFT.md','''# Placement, print and special situations — requires proof

Digital: maintain intrinsic ratio; use responsive `object-fit: contain` rather than cover; prefer source resolution adequate for CSS render width × display pixel ratio. One 2048px image cannot create extra detail above 2048 input pixels.

Business stationery: full-color imagery needs 300ppi at final size for high-quality raster printing. At 300ppi, the 2048px-wide source corresponds to about 6.83 inches/17.3cm width, subject to printer/process. Large signage needs an approved high-scale reconstruction or responsible raster scaling with real proofs, not a claim of lossless infinite zoom.

Embroidery/laser engraving/embossing: glows and thin constellation details may be physically unmanufacturable. Ask for a separately approved one-color production/optical adaptation and proof on the target material. Do not silently simplify official source.

Favicons/app icons: 16–48px cannot represent this full wordmark and micro-line structure legibly. Produce a small-size mark only with explicit Owner authorization; do not claim it is a faithful full-logo export.

Motion: do not animate/redesign the base artwork without Owner authorization; if allowed, define animated logo asset separately from the static brand source.
''')

w('08_QUALITY_AND_EVIDENCE/QA_RELEASE_GATES.md','''# Release acceptance gates — no gate skipping

**Gate 0 — source integrity (mandatory immediately)**
- Transfer owner-supplied original, verify exact SHA-256, bytes, PNG dimensions, 8-bit RGBA and alpha==255. Do not auto-process.
- Require independent SHA-256 read back from destination and backup; fail on mismatch.

**Gate 1 — preservation and visual inventory**
- At 100% and 400%, compare all source details, especially faint internal lines, node rings, crescent outer edge, YCN breaks, LABS tracking and underline flare.
- Record original/source bounding boxes and geometry; no clipping.

**Gate 2 — reconstruction candidate (only after Owner authorizes work)**
- Record actual tools/versions and whether geometric layers are vector, filters, or raster backing. No embedded-raster SVG passed off as fully vector.
- Side-by-side tests are based on true rendered assets, not artist's sketches or simulated substitutes.
- Compare matched-size/matched-canvas images in a controlled profile; do NOT stretch different aspect ratios to line up or quote meaningless global average percentages dominated by dark background.
- Use region-specific overlay, 1px edge crops, missing-point/line inventory, luminance/gradient/glow comparisons, optical review.
- Test on white and dark hosts, multiple viewports and outputs 16/32/48/64/128/256/512/1024/2048 where relevant; record any loss of legibility.
- Owner must visually approve specific version/hashes. Technical scores alone cannot prove exact identity.

**Gate 3 — export reproducibility**
- Every derivative generated from the same *approved* artwork; export tool versions, profiles, rasterizer, size, background/alpha and code recorded.
- No stretching, non-proportional resizing, color cast, clipping or unexpected matte/halo.
- Metadata manifest and file checksums automatically created; repeat build compare hashes (allow justified encoder/platform differences with evidence).

**Gate 4 — theme variants and print**
- On-dark can use original as-is. On-light adaptation requires explicit approval if artwork changes.
- CMYK artwork and print proofs validated by designer and print vendor; web color values do not guarantee appearance on fabric/foil/paper.

**Gate 5 — release and rollout**
- Owner approves named exact files and checksum; reviewer independently verifies.
- Create immutable versioned release; keep release notes + rollback copy + staged deployment screenshots.
- Migrate public site only under separate task; lint/types/tests/build and viewport/theme QA; rollback demonstrated.

**Gate 6 — governance**
- Keep 3-2-1 backup copies (separate medium + offsite), periodic checksum/restore tests, least-privilege access, no public release of editable sources unless specifically authorized.
- Keep rejected, obsolete and legacy graphics quarantined and labeled, not erased during active work.
''')

w('08_QUALITY_AND_EVIDENCE/QA_EVIDENCE_TEMPLATE.tsv','''gate	asset_id	file_path	expected_source_sha	actual_sha	width_px	height_px	alpha	profile	tool_and_version	method	pass_fail	issues	reviewer	owner_approval_ref	date
''')

rows=[
 ('full-lockup','on-dark','PNG', '128;256;512;1024;2048', 'WEB/PRINT', 'Pending: only unchanged original is approved'),
 ('full-lockup','on-light','PNG', '128;256;512;1024;2048', 'WEB/PRINT', 'Exact source on a dark tile currently; transparent/light adaptation requires owner approval'),
 ('full-lockup','on-dark','SVG', 'resolution-independent geometry', 'WEB/PRINT', 'Future candidate: fidelity and glow technical proof required'),
 ('full-lockup','on-light','SVG', 'resolution-independent geometry', 'WEB/PRINT', 'Future candidate: explicit light-use owner approval required'),
 ('mark-only','on-dark','SVG;PNG', '16;32;48;64;128;180;192;256;512;1024', 'FAVICON/APP/SOCIAL', 'No approved symbol-only asset exists; owner sign-off required'),
 ('mark-only','on-light','SVG;PNG', '16;32;48;64;128;180;192;256;512;1024', 'FAVICON/APP/SOCIAL', 'No approved symbol-only asset exists; owner sign-off required'),
 ('wordmark-only','on-dark','SVG;PNG', '256;512;1024;2048', 'DOCS/WEB', 'Crop/extraction is derivative; sign-off required'),
 ('wordmark-only','on-light','SVG;PNG', '256;512;1024;2048', 'DOCS/WEB', 'Crop/extraction is derivative; sign-off required'),
 ('full-logo','single-ink','PDF;SVG;EPS', 'vector', 'STAMP/EMBOSS/LASER', 'Requires explicit separate monochrome reduction approval'),
 ('full-lockup','on-dark','PDF/X-4', 'vector or validated hybrid', 'PRINT', 'CMYK/vendor proof after vector/hybrid sign-off'),
 ('social-avatar','platform-dependent','PNG', '400;800;1024', 'SOCIAL', 'Template geometry and logo safe area must be approved'),
 ('open-graph','brand panel','PNG;WEBP', '1200x630', 'WEB/SOCIAL', 'Composition template is not a logo master; preserve original artwork'),
 ('app-icon','platform-dependent','PNG', '180;192;512', 'APP', 'Needs owner-approved icon crop / optical simplification'),
 ('favicon','platform-dependent','PNG;ICO;SVG', '16;32;48', 'WEB', 'Requires optical simplification approval'),
 ('animated-lockup','on-dark','MOV ProRes4444;WebM alpha;MP4', '1080p;4K (as deliverable)', 'VIDEO', 'Future only; animation of image needs owner approval')]
with (root/'05_EXPORTS'/'EXPORT_MATRIX.csv').open('w', newline='') as f:
 writer=csv.writer(f);writer.writerow(['component','theme','format','target_dimensions','use','release_gate']);writer.writerows(rows)

w('05_EXPORTS/README.md','''# Planned export families — intentionally not generated

See `EXPORT_MATRIX.csv`. Never bulk-generate assets from an unapproved reconstruction.

Raster PNGs are lossless for the pixels they store but are fixed-resolution. New 4096/8192px resizes of a 2048px source do not recover real detail. SVG vectors scale clean geometry but optical glows may require separate filters or resampling. JPEG is not a master format, especially for transparency; WebP/AVIF can be appropriate delivery encodings.

Only after master approval, generate responsive 1x/2x/3x assets as needed by real viewports rather than hundreds of arbitrarily sized files.
''')

w('09_RELEASES/README.md','''# Immutable release policy

- Approved release files only. Do not overwrite published asset hashes in place.
- A release contains `README`, `LOGO-USAGE`, `MANIFEST.json`, `SHA256SUMS.txt`, export script/version, validation logs, Owner approval ID, preview evidence, rollback instructions.
- Version naming: `YCN_LABS_logo-lockup_on-dark_v1.0.0.png`; on-light means intended background, not recolor by assumption.
- A pixel/geometry/wordmark/color change requires new signed decision and potentially major version; only export bug fix/repackaging with same design is a patch release.
- Public Git repository and CDN should store approved distribution exports only; protected design source remains outside the website's public directory.
- Use restricted master storage; build/distribute from a canonical manifest and script. Maintain 3-2-1 backup policy and periodic restore test.
''')

w('10_AGENT_HANDOFF/AGY_TASK_BRAND_SOURCE_CONTROL_03.md',f'''# AGY — BRAND-SOURCE-CONTROL-03 (one task, no visual modification)

**Owner's updated binding ruling:** The only official YCN Labs logo is the Owner-supplied file `{source.name}`, SHA-256 `{sha}`. All other vectors, reconstructions, PNG masters and website outputs are historical or unapproved unless separately signed off by Owner. Preserve `DECISION-001`; append a new decision superseding conflicting source-reference claims in `DECISION-050`, but do not modify `docs/YCN_DECISIONS.md` without a separate approved documentation task.

**Precondition:** The Owner must transfer this exact original PNG to the workstation as a new direct upload, ideally into `YCN_LABS_MASTER/01_CURRENT_PROJECT/ycn-brand-work/06-owner-source-intake/`. Do not retrieve a different-looking file based on its name; do not proceed if not provided or if hash mismatches.

**Authorized scope: read-only audit and create only new source-preservation directory, pending Owner's approval to execute.**

1. Run standard git preflight, record HEAD and worktree status; read repository rules. Do not modify repo.
2. Locate transferred Owner file; verify `sha256sum` equals `{sha}`. Verify actual PNG dimensions 2048×1593, file size 3158172 bytes, PNG RGBA with alpha uniformly 255. Reject any mismatch.
3. Create (if absent) only `YCN_LABS_MASTER/01_CURRENT_PROJECT/YCN_LABS_BRAND_LIBRARY/01_IMMUTABLE_SOURCE/` and copy the Owner file byte-for-byte there. Do not touch existing originals. Verify output checksum.
4. Copy/source-install documentation kit into **new** subfolders of that library if and only if Owner supplies it, without overwriting any preexisting files or replacing existing policies silently.
5. Catalog legacy/logo files only by pathname and status. Mark earlier vectors, September prototypes, `ycn-brand-masters` and production web assets as `LEGACY_REVIEW_PENDING`; never delete, move or label them approved by proximity.
6. Produce `SOURCE-FREEZE-REPORT.md`: exact source/destination, timestamps, source and destination hash, PNG metadata, git status, raw commands+exit codes, any collisions; describe what was NOT done.
7. For a future separate task, recommend precision vector/hybrid feasibility, including micro-line/glow preservation. Do not generate/recolor/retouch, remove background, AI-upscale, or create final light/dark assets during this task.
8. No push/commit/deployment, no dependency install, no originals altered. No deletes. Stop on first hash or precondition failure and report.

**STOP.** Wait for Claude audit and Owner approval to proceed to the distinct reconstruction and derivative-production tasks.
''')

w('10_AGENT_HANDOFF/PROJECT_PHASES.md','''# Delivery plan — independent approval gates

- **BRAND-SOURCE-CONTROL-03**: Obtain Owner's exact only source, preserve byte-identically, record updated authority (non-code).
- **BRAND-RECON-FEASIBILITY-04**: Analyze small details, propose reproducible vector/hybrid architecture, render *DRAFT* proofs and disclose deviations. No official design change.
- **BRAND-MASTER-PRODUCTION-05**: If and only if Owner approves the method, construct and visually compare high-fidelity layered/vector candidate; have independent reviewer and Owner approve hashes.
- **BRAND-THEME-06**: Owner separately decides whether original dark image on dark card is acceptable on light UI; any recolored/transparent light asset must be approved explicitly.
- **BRAND-EXPORT-07**: Build automated exports with manifest, media profiles, QA, size table, color proof.
- **BRAND-SITE-08**: Separate approved code task to swap to canonical BrandLogo component, preserve frozen entrance and motion, test 375/768/1024/1280/1440 and reduced motion; no automatic site updates from this package.
- **BRAND-RELEASE-09**: Signed versioned release, backup/rollback, deprecate legacy references only after validation, and protect sources.
''')

# self-contained verification tool using only Python stdlib for PNG header and checksum
w('10_AGENT_HANDOFF/verify_original.py',f'''#!/usr/bin/env python3
"""Read-only hash + format check of owner supplied YCN Labs source."""
import hashlib, struct, pathlib, sys
EXPECTED_SHA = "{sha}"
EXPECTED_SIZE = 3158172
EXPECTED_DIMS = (2048,1593)

def main(path):
    p=pathlib.Path(path)
    b=p.read_bytes()
    h=hashlib.sha256(b).hexdigest()
    if b[:8] != b"\\x89PNG\\r\\n\\x1a\\n": raise SystemExit('Not a PNG file')
    width,height,depth,color,compression,filter_method,interlace = struct.unpack('>IIBBBBB',b[16:29])
    print(f'FILE: {{p}}\\nSHA256: {{h}}\\nBYTES: {{len(b)}}\\nSIZE: {{width}}x{{height}}\\nBIT_DEPTH: {{depth}}\\nPNG_COLOR_TYPE: {{color}}')
    assert h==EXPECTED_SHA, 'ERROR: NOT IDENTICAL TO OWNER SOURCE'
    assert len(b)==EXPECTED_SIZE and (width,height)==EXPECTED_DIMS and depth==8 and color==6, 'Metadata mismatch'
    print('PASS: file bytes exactly match Owner-supplied PNG')
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python verify_original.py /path/to/file.png')
    main(sys.argv[1])
''')

# Create package-wide manifest (excluding itself + checksum file)
manifest=[]
for file in sorted(root.rglob('*')):
 if not file.is_file() or file.name in ('PACKAGE-MANIFEST.json','PACKAGE-SHA256SUMS.txt'): continue
 manifest.append({'path':str(file.relative_to(root)), 'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
(root/'PACKAGE-MANIFEST.json').write_text(json.dumps({'package_status':'SOURCE_AND_GOVERNANCE_FOUNDATION_ONLY','source_sha256':sha,'files':manifest},indent=2)+'\n')
(root/'PACKAGE-SHA256SUMS.txt').write_text(''.join(f'{e["sha256"]}  {e["path"]}\n' for e in manifest)+'\n')
zip_path=Path('/mnt/data/YCN_LABS_Brand_Source_Foundation_2026-10-13.zip')
with zipfile.ZipFile(zip_path,'w',allowZip64=True) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file():
   # Store PNG without recompressing; original PNG bytes stay identical regardless
   z.write(p, arcname=str(root.name+'/'+str(p.relative_to(root))),compress_type=(zipfile.ZIP_STORED if p.suffix.lower()=='.png' else zipfile.ZIP_DEFLATED))

# Validate inside zip
with zipfile.ZipFile(zip_path) as z:
 for name in z.namelist():
  if name.endswith('/'+source.name): assert hashlib.sha256(z.read(name)).hexdigest()==sha
print('CREATED',root)
print('FILE COUNT',sum(1 for x in root.rglob('*') if x.is_file()))
print('ZIP', zip_path, 'bytes',zip_path.stat().st_size)
print('MD guide',root/'README.md')
print('source SHA',sha)
