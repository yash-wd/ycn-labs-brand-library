# YCN Labs — handoff to Claude (read this first)

**Date:** 2026-10-13  
**Purpose:** Supply the complete, verified content of the ChatGPT-created 23-file **source-foundation package** as **separate, individually uploadable files**. Filenames have been prefixed with the original folder path to prevent duplicate `README.md` files from overwriting each other. Other than filenames and their location, package files are byte-for-byte unchanged. The original official logo filename is unchanged.

## Critical owner instruction

Only `Main_YCN_LABS_logo_black_8K.png` is the official logo reference. Preserve every pixel. SHA-256: `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`. This is actually 2048×1593 px, fully opaque 8-bit RGBA. Existing vector prototypes, alternate masters, and website variants are not authorized replacements. Historic decisions must be preserved and conflicts reconciled via a **new Owner-approved ruling**, not silent rewriting.

**Package state:** This is source and governance groundwork only. No validated SVG/vector master, on-light transparent rendition, symbol-only derivative, favicon, print-ready export, or production rollout is completed or approved here. Color samples and usage guides are provisional.

## Suggested upload sequence to Claude

1. Upload **this** document and the original official PNG first.
2. Upload all **A-priority** documents. Ask Claude to identify the sole authorized original, existing status, conflicts, and exactly what task is next. Do not approve implementation merely by uploading.
3. Upload **B-priority** documents next to review the complete roadmap and technical constraints.
4. Upload **C-priority** integrity/release files when checking manifests, coverage, QA evidence and reproducibility.
5. The separate `EXTRA__YCN_LABS_Enterprise_Brand_Management_Plan.md` is a supplementary narrative plan (not inside the 23-file ZIP).

## Next AGY task, not yet an execution approval

`10_AGENT_HANDOFF__AGY_TASK_BRAND_SOURCE_CONTROL_03.md` is the proposed single next task, covering exact original transfer, SHA-256 verification, immutable preservation and reporting. It forbids edits, upscaling, recoloring, site migration, commits/pushes and source substitution. Claude should review it under existing AGENTS/Owner approval rules before AGY runs it.

## Important restrictions

- The local file paths under `/mnt/data/` are ChatGPT download paths, **not** AGY workstation locations.
- Do not infer that a file named `8K` actually has 8K resolution.
- On white/light pages, unchanged original can be embedded as a complete dark panel; a true transparent/light-themed adaptation modifies artwork and requires explicit approval.
- Do not confuse plans, scripts, templates or candidate swatches with approved brand graphics.
- The individual files came from the ZIP and were hash-compared to their source; the ZIP was integrity-checked separately.

## All original 23 package files (with individual-share filename mapping)

| Priority | Original relative path | Individual upload name | Brief |
|---|---|---|---|
| A | `00_GOVERNANCE/OWNER_SOURCE_RULING.md` | `00_GOVERNANCE__OWNER_SOURCE_RULING.md` | Owner ruling: one official image, forbidden changes, derivative approval rules and historical decision conflicts |
| A | `00_GOVERNANCE/SOURCE_RECORD.json` | `00_GOVERNANCE__SOURCE_RECORD.json` | Machine-readable official image facts: hash, dimensions, bytes, opacity and approval status |
| B | `00_GOVERNANCE/STATUS_AND_CHANGES.md` | `00_GOVERNANCE__STATUS_AND_CHANGES.md` | Source baseline/changelog and list of decisions still open |
| A | `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png` | `Main_YCN_LABS_logo_black_8K.png` | Sole official visual reference, bit-for-bit copy of Owner-uploaded original PNG |
| A | `01_IMMUTABLE_SOURCE/SHA256SUMS.txt` | `01_IMMUTABLE_SOURCE__SHA256SUMS.txt` | Checksum verification line for the original PNG |
| A | `02_BRAND_DESIGN/ARTWORK_INVENTORY.md` | `02_BRAND_DESIGN__ARTWORK_INVENTORY.md` | Preservation checklist for crescent, orbital nodes, tiny lines, YCN/LABS letterforms, glows and flare |
| B | `03_VECTOR_RECONSTRUCTION/FEASIBILITY_AND_BRIEF.md` | `03_VECTOR_RECONSTRUCTION__FEASIBILITY_AND_BRIEF.md` | Technical feasibility, faithful manual/hybrid reconstruction approach and limitations; NOT permission to redraw |
| B | `04_APPROVED_LOGO_VARIANTS/README.md` | `04_APPROVED_LOGO_VARIANTS__README.md` | Clarifies that no light/transparent/vector/mark-only derivative is approved yet |
| B | `05_EXPORTS/EXPORT_MATRIX.csv` | `05_EXPORTS__EXPORT_MATRIX.csv` | Future asset types, sizes, uses, and approval/release gate for every export family |
| B | `05_EXPORTS/README.md` | `05_EXPORTS__README.md` | Explains why exports have not been generated and how quality/resolution should be handled |
| B | `06_DESIGN_TOKENS/COLOR_AND_TYPE_POLICY.md` | `06_DESIGN_TOKENS__COLOR_AND_TYPE_POLICY.md` | Color profile, typography, gradient and palette governance; sampled colors are not official tokens |
| B | `06_DESIGN_TOKENS/SAMPLED_PALETTE.json` | `06_DESIGN_TOKENS__SAMPLED_PALETTE.json` | Exploratory measured HEX/RGB swatches, explicitly NOT APPROVED as brand tokens |
| B | `07_GUIDELINES/BRAND_USAGE_DRAFT.md` | `07_GUIDELINES__BRAND_USAGE_DRAFT.md` | Draft logo usage rules for light/dark surfaces, distortions, accessibility and source traceability |
| B | `07_GUIDELINES/PLACEMENT_AND_PRINT_DRAFT.md` | `07_GUIDELINES__PLACEMENT_AND_PRINT_DRAFT.md` | Draft print/display limitations, high-DPI sizing, signage, favicon and manufacturing restrictions |
| C | `08_QUALITY_AND_EVIDENCE/QA_EVIDENCE_TEMPLATE.tsv` | `08_QUALITY_AND_EVIDENCE__QA_EVIDENCE_TEMPLATE.tsv` | Blank row/column schema for QA checks, reviewers, evidence and approval references |
| A | `08_QUALITY_AND_EVIDENCE/QA_RELEASE_GATES.md` | `08_QUALITY_AND_EVIDENCE__QA_RELEASE_GATES.md` | Mandatory source integrity, reconstruction, export, theme, print, release and backup QA gates |
| C | `09_RELEASES/README.md` | `09_RELEASES__README.md` | Immutable versioning, release contents, manifest and rollback conventions; no actual release exists |
| A | `10_AGENT_HANDOFF/AGY_TASK_BRAND_SOURCE_CONTROL_03.md` | `10_AGENT_HANDOFF__AGY_TASK_BRAND_SOURCE_CONTROL_03.md` | Exact next AGY task: transfer, hash-check and archive official PNG; no redesign or site edits |
| B | `10_AGENT_HANDOFF/PROJECT_PHASES.md` | `10_AGENT_HANDOFF__PROJECT_PHASES.md` | Future multi-stage brand workflow with individual approval gates and separate website task |
| A | `10_AGENT_HANDOFF/verify_original.py` | `10_AGENT_HANDOFF__verify_original.py` | Read-only Python script to validate source SHA, byte count, PNG signature, dimensions and color type |
| C | `PACKAGE-MANIFEST.json` | `PACKAGE-MANIFEST.json` | Original ZIP file inventory with hashes and sizes |
| C | `PACKAGE-SHA256SUMS.txt` | `PACKAGE-SHA256SUMS.txt` | Original ZIP-package per-file SHA-256 ledger for integrity verification |
| A | `README.md` | `README.md` | Start-here guide explaining source authority, scope, status and limitations |

## Separate non-ZIP files

- `EXTRA__YCN_LABS_Enterprise_Brand_Management_Plan.md`: full narrative enterprise brand architecture; separate from the 23 ZIP files.
- `CLAUDE_FILE_INDEX.csv`: machine-readable table of all original 23 ZIP files and exact hashes.
- `CLAUDE_READ_FIRST.md`: this handoff, created afterwards for easy Claude sharing; not inside the original ZIP.
- `/mnt/data/build_brand_kit.py`: original ChatGPT-side package construction helper, **not an approved production export script**, not part of the ZIP and not required for the next AGY task.
