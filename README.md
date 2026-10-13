# YCN Labs — Brand source foundation (13 October 2026)

**Status: Source frozen; production master vectors and theme variants NOT YET APPROVED.**

This package is the beginning of the production-grade brand management system. It does **not** claim to contain validated SVGs, transparent masters, matching light-background art, or all usable sizes. Those require a separate documented reconstruction and proof process.

## Authority

- The Owner designated exactly one upload, `Main_YCN_LABS_logo_black_8K.png`, as the sole official visual reference. Previous candidate exports, alternate masters, generated images and site derivatives do not become authoritative merely by naming or earlier ratification.
- Original bytes are preserved unchanged at `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`.
- SHA-256: `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`.
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
