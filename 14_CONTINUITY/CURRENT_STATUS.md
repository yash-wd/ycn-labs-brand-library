# YCN Labs Brand Assets — Current Technical Status

**Date:** 2026-10-13  
**Repository:** `https://github.com/yash-wd/ycn-labs-brand-library` (Public)  
**Controlling Authority:** `00_GOVERNANCE/CURRENT_SOURCE_AUTHORITY.md`  
**Status:** Source Authority Finalized, Downloads Fully Cleaned, RULING-02 Evidence Prepared  

## Current Baseline:

1. **Source Artwork Resolution & Provenance:**
   - `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png`: 6675×5195, 8-bit RGB, SHA-256 `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`. Consistent with being parent source (aspect match 0.057%, IoU 95.92%, mean error 1.09%). Ratified Authoritative Master per Owner RULING-01. Desktop copy preserved at `/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png`.
   - `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`: 2048×1593, 8-bit RGBA (all 255 alpha), SHA-256 `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`. Preserved byte-for-byte as the Owner-uploaded reference downscale.

2. **Transparent Master Derivatives (18 Aug 2026) & Forensic Evidence (RULING-02):**
   - `ycn-logo-dark-transparent-MASTER.png` (5620×4580, SHA-256 `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`):
     - Forensic measurements (`08_QUALITY_AND_EVIDENCE/RULING-02/`):
       - Native 1:1 scale: width delta 0.0000%, height delta 0.0644% (no resampling).
       - Integer offset: dx=663, dy=320 (Pearson correlation = 0.993566).
       - High-alpha pixels (alpha >= 250): Mean |ΔRGB| = 1.6583 / 255, 0.0000% pixels > 16.
       - Full overlap composited over sampled background: Mean |ΔRGB| = 0.7756 / 255, 0.0000% pixels > 16.
       - Comparison sheet: `RULING-02-SHEET.png` (SHA-256: `bf2cce1e...`).
       - Status: Awaiting Owner visual approval (**RULING-02**).
   - `ycn-logo-light-transparent-MASTER.png` (5620×4580, SHA-256 `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`):
     - Alpha IoU vs dark master: 97.2464%, Mean |Δalpha| = 4.8411 / 255.
     - Status: Awaiting Owner visual approval (**RULING-02**).

3. **Excluded / Non-Production Assets:**
   - `YCN_LABS_logo_8K.png` (7680×7680): Excluded (near-square 1.04:1 aspect ratio, different layout).
   - September SVGs `g211`/`g212`: Failed release gate; reference topology only.
   - August SVGs `g070`–`g155`: Early wireframe monogram concepts; different design.

4. **Vector Master Status:**
   - Vectorization deferred to human vector artist with 5620/6675 underlay. AI auto-tracing rejected.

5. **Consolidation, Cleanup & Day Close (BRAND-DAY-CLOSE-09):**
   - Full Downloads audit: All redundant matching files removed; 8 YCN-named non-matching project files from 12 Oct left untouched.
   - Supreme source authority established in `00_GOVERNANCE/CURRENT_SOURCE_AUTHORITY.md`.
   - Temporary public repository lifecycle documented in `00_GOVERNANCE/OWNER_PUBLIC_REPOSITORY_RULING.md`.
   - QA release gates updated to validate both 6675 and 2048 files in `08_QUALITY_AND_EVIDENCE/QA_RELEASE_GATES.md`.
   - Review protocol restored in `14_CONTINUITY/PROCESS_NOTES.md`.
