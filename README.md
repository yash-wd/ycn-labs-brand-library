# YCN Labs — Brand Library & Asset Archive

**Repository:** `https://github.com/yash-wd/ycn-labs-brand-library`  
**Controlling Authority:** `00_GOVERNANCE/CURRENT_SOURCE_AUTHORITY.md`  
**Status:** Source Frozen, RULING-01 Recorded, Public Archive Established  

---

## 1. Brand Asset Hierarchy & Authoritative Sources

This repository serves as the centralized public brand asset archive, source freeze, and design governance register for **YCN Labs**.

### A. Authoritative Master Source (`01_IMMUTABLE_SOURCE/`)
- **Authoritative Master (6675×5195):**  
  `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png`  
  *SHA-256:* `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`  
  *Format:* 6675 × 5195 pixels, 8-bit RGB, 6,633,409 bytes.  
  *Lineage:* Formally ratified as the Authoritative Master Source per Owner **RULING-01** (13 Oct 2026). Mathematical audit confirmed aspect ratio match within 0.057% and 95.92% silhouette IoU vs the uploaded reference.
- **Uploaded Reference Copy (2048×1593):**  
  `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`  
  *SHA-256:* `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`  
  *Format:* 2048 × 1593 pixels, 8-bit RGBA (all 255 alpha, opaque `#000205` black field), 3,158,172 bytes.  
  *Lineage:* Preserved byte-for-byte as the Owner-uploaded reference downscale.

### B. High-Resolution Transparent Candidates (`11_HISTORICAL_ASSETS/masters/`)
- **Dark Transparent Master (5620×4580):**  
  `11_HISTORICAL_ASSETS/masters/ycn-logo-dark-transparent-MASTER.png`  
  *SHA-256:* `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`  
  *Status:* Proportions and letter scale match to 99.93% and 0.6%; visual sheet confirms same design; Owner visual approval pending (**RULING-02**).
- **Light Transparent Master (5620×4580):**  
  `11_HISTORICAL_ASSETS/masters/ycn-logo-light-transparent-MASTER.png`  
  *SHA-256:* `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`  
  *Status:* Compared 13 Oct 2026: alpha IoU 97.2464% vs the dark master (see `08_QUALITY_AND_EVIDENCE/RULING-02/RULING-02-NUMBERS.txt`); approval pending (**RULING-02b**).

### C. Excluded & Reference-Only Assets
- `11_HISTORICAL_ASSETS/masters/YCN_LABS_logo_8K.png` (7680×7680, SHA-256: `ca90462d...`): Excluded (near-square 1.04:1 aspect ratio, different layout).
- `11_HISTORICAL_ASSETS/vectors/g211` / `g212` (Sept 2026 SVGs): Prototype candidate vectors that failed release gate (IoU 96.56%); retained for coordinate topology reference only.
- `11_HISTORICAL_ASSETS/vectors/g070`–`g155` (August 2026 SVGs): Early wireframe geometric monogram concepts; different design.

---

## 2. Directory Architecture

```
YCN_LABS_BRAND_LIBRARY/
├── 00_GOVERNANCE/             # Owner rulings, source records, and change control
├── 01_IMMUTABLE_SOURCE/       # Authoritative 6675px and 2048px master PNGs
├── 02_BRAND_DESIGN/           # Artwork anatomy, orbital nodes, and letterform specs
├── 03_VECTOR_RECONSTRUCTION/  # Vectorization brief and technical requirements
├── 04_APPROVED_LOGO_VARIANTS/ # Reserved for ratified production vector & theme variants
├── 05_EXPORTS/                # Production export specifications (sizes, formats)
├── 06_DESIGN_TOKENS/          # Measured color palette and typography references
├── 07_GUIDELINES/             # Brand usage rules and surface presentation guidance
├── 08_QUALITY_AND_EVIDENCE/   # QA release gates and verification templates
├── 09_RELEASES/               # Versioned distribution manifests
├── 10_AGENT_HANDOFF/          # Verification scripts and phase definitions
├── 11_HISTORICAL_ASSETS/      # 5620/7680 masters, 26 YCN SVGs, audits, intake manifest
├── 12_ORIGINAL_PACKAGES/      # Original GPT Brand Source Foundation ZIP archive
├── 13_AI_REPORTS/             # Review records and engineering task execution logs
└── 14_CONTINUITY/             # Tomorrow start guide, status, open decisions, checksums
```

---

## 3. Which Files Can Be Used Today

- **Active Web Assets:** The public website repository ([ycn-labs-site](https://github.com/yash-wd/ycn-labs-site)) continues to serve its existing verified assets in `public/brand/`.
- **Authoritative Brand References:** Any brand artwork reference, presentation asset, or media graphic must source directly from `01_IMMUTABLE_SOURCE/`.
- **Unfinished Work:**
  - True resolution-independent vector masters (SVG/AI) are **NOT YET PRODUCED**. AI auto-tracing has been rejected; a human vector artist will redraw the master using the 5620/6675 PNG underlay.
  - Opaque on-dark PNG exports (128–2048 px) built under BRAND-EXPORT-05 from the RULING-01 master, pending Owner acceptance. Transparent variants follow RULING-02; favicons and app icons follow a small-mark ruling.

---

## 4. How to Resume Work Tomorrow

For any pair-programming agent or engineer starting a new session:
1. Consult `14_CONTINUITY/RESUME_HERE.md` (canonical entry point; `START_TOMORROW.md` only points to it).
2. Review `14_CONTINUITY/OPEN_OWNER_DECISIONS.md` for pending Owner decisions (RULING-02 through RULING-04).
3. Validate repository integrity via `sha256sum -c 14_CONTINUITY/SHA256SUMS.txt`.

---

## 5. Trademark & Proprietary Rights Notice

**Copyright © 2026 YCN Labs. All Rights Reserved.**

All brand marks, logos, orbital celestial symbols, custom lettering, wordmarks, trade dress, and visual artwork contained in this repository are the exclusive proprietary trademarks and intellectual property of **YCN Labs**. 

Public repository availability on GitHub is provided solely for transparent brand management, versioning, and authorized technical integration. **No permissive software license (such as MIT, Apache 2.0, or BSD) applies to the visual artwork or trademarks.** Commercial reproduction, modification, scraping, or unauthorized redistribution of the YCN Labs logo is strictly prohibited without explicit written permission.
