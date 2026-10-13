# YCN Labs Brand Assets — Current Technical Status

**Date:** 2026-10-13  
**Status:** Source Frozen, Mathematical Audit Complete, Library Consolidated  

## Current Baseline:
1. **Source Artwork Resolution & Provenance:**
   - `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png`: 6675×5195, 8-bit RGB, SHA-256 `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`. Verified via Lanczos downscaling as the true high-resolution parent source artwork (IoU 95.92%, mean error 1.09%).
   - `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`: 2048×1593, 8-bit RGBA (all 255 alpha), SHA-256 `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`. Preserved byte-for-byte as the Owner-uploaded reference master.
2. **Transparent Master Derivatives (18 Aug 2026):**
   - `ycn-logo-dark-transparent-MASTER.png` (5620×4580, SHA-256 `85808a7d...`): Verified as the identical artwork cropped directly to the visible bounds at 3.262× glyph scale (aspect match: 99.93%).
   - `ycn-logo-light-transparent-MASTER.png` (5620×4580, SHA-256 `416de4b7...`): Matching light-theme derivative.
3. **Excluded / Non-Production Assets:**
   - `YCN_LABS_logo_8K.png` (7680×7680): Excluded (near-square 1.04:1 aspect ratio, different layout).
   - September SVGs `g211`/`g212`: Failed release gate; reference topology only.
   - August SVGs `g070`–`g155`: Early wireframe monogram concepts; different design.
4. **Vector Master Status:**
   - Vectorization deferred to human vector artist. AI auto-tracing rejected.
