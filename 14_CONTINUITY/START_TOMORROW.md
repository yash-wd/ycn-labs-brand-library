# YCN Labs — Brand Library Continuity Guide (Start Tomorrow)

**Repository:** `https://github.com/yash-wd/ycn-labs-brand-library` (Public)  
**Local Root:** `/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/YCN_LABS_BRAND_LIBRARY/`  
**Date:** 2026-10-13  

## 1. Quick Start for Future AI Sessions (GPT / Claude / AGY)

If you are beginning a new session tomorrow, execute the following pre-flight sequence to recover full context without relying on chat history:

1. **Verify State & Documents:**
   - Read `14_CONTINUITY/CURRENT_STATUS.md` for the technical baseline.
   - Read `14_CONTINUITY/OPEN_OWNER_DECISIONS.md` for pending Owner decisions (RULING-02 through RULING-04).
   - Read `00_GOVERNANCE/OWNER_PUBLIC_REPOSITORY_RULING.md` for public repository governance & trademark notice.
   - Read `00_GOVERNANCE/YCN_LABS_Enterprise_Brand_Management_Plan.md` for the overarching enterprise brand plan.
   - Read `14_CONTINUITY/DOWNLOADS_CLEANUP_2026-10-13.md` for cleanup and completeness audit history.
   - Read `10_AGENT_HANDOFF/CLAUDE_READ_FIRST.md` for original package handoff context.
   - Read `13_AI_REPORTS/CLAUDE_REVIEW_2026-10-13.md` for standing rulings.
2. **Verify Checksums:**
   - Run `sha256sum -c 14_CONTINUITY/SHA256SUMS.txt` from the brand library root.
3. **Core Brand Authority:**
   - **Ratified Authoritative Master:** `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png` (SHA256: `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`, per Owner RULING-01). The duplicate original file remains preserved at `/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png`.
   - **Uploaded Reference Copy:** `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png` (2048x1593, SHA256: `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`). (Redundant copy in `Downloads/` cleaned up).
   - **Dark Transparent Master:** `11_HISTORICAL_ASSETS/masters/ycn-logo-dark-transparent-MASTER.png` (5620x4580, SHA256: `85808a7d...`; proportions and letter scale match 99.93% and 0.6%; pixel overlap 60%; visual sheet shows same design; Owner visual approval pending per RULING-02).
   - **Light Transparent Master:** `11_HISTORICAL_ASSETS/masters/ycn-logo-light-transparent-MASTER.png` (5620x4580, SHA256: `416de4b7...`; not yet compared; approval pending per RULING-02).

## 2. Standing Rules & Boundaries
- **Dual-Repository Architecture:**
  - `ycn-labs-site`: Public website code; receives only released exports in `public/brand/`. Never push raw master sources here.
  - `ycn-labs-brand-library`: Centralized public brand archive for master art, audit sheets, tokens, and governance.
- **Trademark Notice:** All visual marks and logos are proprietary trademarks of YCN Labs. No permissive license applies to logo artwork.
- **No AI Logo Regeneration:** Never generate new replacement logos using AI tools or auto-tracers. The logo design is finalized (`DECISION-001`).
- **Vector Master Production:** Deferred to a professional human vector artist using the 5620/6675 master as a locked underlay.

## 3. Tomorrow's Next Authorized Tasks
1. **RULING-02 Review:** Owner visually reviews `11_HISTORICAL_ASSETS/audits/06-identity-audit/IDENTITY-SHEET.png` to issue approval ruling on the 5620px transparent masters.
2. **Execute BRAND-EXPORT-05:** Upon RULING-02 approval, deterministically generate production export kit (web/app/social sizes) into `05_EXPORTS/` and `04_APPROVED_LOGO_VARIANTS/`.
3. **Commission Vector Master:** Deliver 5620/6675 PNG underlay to professional vector illustrator.
