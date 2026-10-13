# YCN Labs — Brand Lineage & Vector Master Recommendation

**Task:** `BRAND-LINEAGE-AUDIT-02`  
**Date:** 2026-10-13 08:16:18  
**Controlling Authority:** `docs/YCN_DECISIONS.md` (`DECISION-001`, `DECISION-050`)  
**Status:** Audit Complete — Definitive Technical Verdict Delivered  

---

## 1. Executive Summary & Verdict

### Recommendation: **ROUTE B (Precision Vector Reconstruction from Ratified PNG Masters)**
- **Route A (Existing SVG as Production Master):** **DISQUALIFIED BY EVIDENCE.**
- **Route B (Precision Vector Reconstruction of Ratified PNG Masters):** **UNANIMOUSLY SUPPORTED BY EVIDENCE.**

Neither the August vector set (`g070`–`g155`) nor the September vector candidate pair (`g211`/`g212`) can be designated as the official production master without violating binding Owner decisions.

---

## 2. Evidence-Based Disqualification of Route A

### A. The August Vector Set (`g070`–`g155`)
1. **Design Divergence:** The August SVGs (`g070`–`g155`) represent an early conceptual exploration of a simple 24px wireframe geometric "Y" monogram (`ARCHIVED_Brand_Identity_v2.0.md`).
2. **Contract Breach:** They bear zero geometric relationship to the complex orbital network mark approved by the Owner in `DECISION-001`. Using them would constitute an unapproved brand redesign.
3. **Classification:** **`DIFFERENT-DESIGN`**.

### B. The September Vector Candidate (`g211` / `g212`)
1. **Unapproved Candidate Status:** As documented in `YCN_LABS_STAGE_A_QA_v0.1.json`, candidate `v0.1` explicitly failed its release gate (`FAIL_RELEASE_GATE_EXPECTED_CANDIDATE_ONLY`).
2. **Missing Light Theme:** `light_theme_generated: false`. The Stage A reconstruction stopped at dark geometry only; no light-theme vector master was ever derived.
3. **Geometry and Raster Divergence:**
   - Reconstructed from an opaque alternate black render (`Main_YCN_LABS_logo_black_8K.png`, 2048×1593), not the approved transparent master.
   - Contours were mathematically smoothed, altering the original hand-drawn or generated curves.
   - Faint internal network lines were omitted.
   - Measured IoU vs source hard geometry is 96.56% (alpha difference vs ratified master is 16.05%).
4. **Governing Exclusion:** `DECISION-050` explicitly ruled: *"The 23 Sep 2026 opaque 8K files are private alternate renders, not production assets... Final official logo replacement is established as a separate, independently scoped task."*
5. **Classification:** **`RECONSTRUCTION-BASIS`**, not an approved master.

---

## 3. The Evidentiary Foundation for Route B

### A. Ratified Source Authority (DECISION-050)
1. **Ratified Source Files:**
   - Light: `/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/ycn-brand-masters/masters/ycn-logo-light-transparent-MASTER.png` (5620×4580, RGBA, SHA256: `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`)
   - Dark: `/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/ycn-brand-masters/masters/ycn-logo-dark-transparent-MASTER.png` (5620×4580, RGBA, SHA256: `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`)
2. **Verified Live Lineage:**
   - `ycn-logo-light-transparent-448.png` and `ycn-logo-dark-transparent-448.png` are proven by pixel-level delta testing to be exact Lanczos downscales (0.0000 mean difference) of these 5620×4580 master files.
3. **Requirement:**
   - Both light and dark transparent masters exist at pristine 5620×4580 resolution with full alpha channels.
   - A precision vectorisation task (`BRAND-MASTER-01`) must directly trace and extract the true mathematical Bézier paths and network nodes from these 5620×4580 masters for both themes simultaneously.
   - `g211`'s mathematical coordinates can be referenced as an auxiliary baseline for dark geometry, but the authoritative artwork must align 100% with the ratified masters.

---

## 4. Deliverables Checklist for Next Task (`BRAND-MASTER-01`)

1. **True Dual-Theme Master SVGs:**
   - Mark (Symbol), Wordmark, and Full Lockup for Light Background.
   - Mark (Symbol), Wordmark, and Full Lockup for Dark Background.
   - Pure vector paths only (zero `<image>`, zero `<text>`, clean geometry).
2. **Contrast & Theme Verification:**
   - Verified 3:1 minimum contrast compliance against `#ffffff` and `#0b0b0b`.
3. **Automated Export Pipeline (`BRAND-EXPORT-01`):**
   - Lossless PNGs (88, 176, 224, 264, 448, 1024, 2048), WebP variants.
   - Favicons (16, 32, 48), App icons (180, 192, 512), OG image (1200×630).
4. **Site Integration (`BRAND-SITE-01`):**
   - `BrandLogo` component switching mode seamlessly with theme tokens.

---

*Report sealed. Awaiting Owner review of comparison sheets in `05-lineage-review/`.*
