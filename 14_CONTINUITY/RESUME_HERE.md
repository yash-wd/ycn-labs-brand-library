# YCN Labs — Brand Library Cold-Resume Authority

**Document ID:** `14_CONTINUITY/RESUME_HERE.md`  
**Effective Date:** 2026-10-13  
**Status:** Permanent, Date-Independent Canonical Entry Point for Future AI Sessions  
**Owner Working Routine:** https://github.com/yash-wd/ycn-labs-site/blob/main/docs/YCN_LABS_OWNER_WORKING_ROUTINE.md  
**Dual-Repository Architecture:**
- **Brand Library:** `https://github.com/yash-wd/ycn-labs-brand-library` (Local: `/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/YCN_LABS_BRAND_LIBRARY/`)
- **Website Repository:** `https://github.com/yash-wd/ycn-labs-site` (Local: `/home/ycn-labs/Desktop/ycn-labs-site/`)
- **Local Vault:** `/home/ycn-labs/Desktop/YCN_LABS_MASTER/` (Local protected archive; never published)

---

## 1. Cold-Resume Core Facts (State of Record)

- **Last Close Date & Time:** 2026-10-13T14:16:00+05:30 (from `YCN_LABS_MASTER/LAST_CLOSE.txt`)
- **Latest State Reference:** Latest state = latest commit on GitHub main of each repo
- **Brand Library Commit (HEAD before this close):** `ddf0664` (verified on `origin/main`)
- **Website Commit (HEAD before this close):** `770c034` (verified on `origin/main`)
- **Vault Backup Status:** **LOCAL ONLY — NO EXTERNAL BACKUP RECORDED**. The local vault `/home/ycn-labs/Desktop/YCN_LABS_MASTER/` requires physical copy to an external drive by the Owner. This status must be reported at every close until confirmed.
- **Package Checksums Baseline Notice:**  
  `PACKAGE-SHA256SUMS.txt` describes the ZIP as delivered on 13 Oct. `README.md`, `01_IMMUTABLE_SOURCE/SHA256SUMS.txt` and `08_QUALITY_AND_EVIDENCE/QA_RELEASE_GATES.md` were edited afterwards on purpose and show FAILED there. The live check is `14_CONTINUITY/SHA256SUMS.txt`; originals are inside `12_ORIGINAL_PACKAGES/`.

---

## 2. Completed Tasks Summary

1. **`BRAND-INTAKE-01` / `BRAND-LINEAGE-02` / `BRAND-ARCHIVE-06`:** Comprehensive audit of candidate files; 6675px master identified in BRAND-ARCHIVE-06; transparent masters evaluated in BRAND-LINEAGE-02.
2. **`BRAND-SOURCE-CONTROL-03` / `PUBLISH-07`:** Built structured 15-folder brand library (00–14); published public repository on GitHub (`yash-wd/ycn-labs-brand-library`).
3. **`BRAND-CLEANUP-08` / `DAY-CLOSE-09`:** Verified file hashes and eliminated redundant Downloads duplicates.
4. **`RULING-01` Ratification:** Ratified 6675×5195 image as the Authoritative Master Source; preserved 2048px as uploaded reference downscale.
5. **`RULING-02` Forensic Evidence Generation:** Completed pixel-level forensic measurements proving native 1:1 scale (0.0000% w / 0.0644% h delta, dx=663, dy=320 offset, 0.0000% pixels > 16 delta) between 6675 master and 5620 transparent master.
6. **`YCN-CLOSE-PROTOCOL-01`:** Established permanent cross-project close-and-cold-resume protocol. Four unique 12 Oct files safely routed to vault `_INTAKE/2026-10-12/`.

---

## 3. Exactly ONE Next Task Per Active Workstream

- **Brand Library Workstream:**  
  **Next Task:** **Owner acceptance of BRAND-EXPORT-05 (opaque-first), then rulings 02a/02b/04 and RULING-05**
  Opaque on-dark exports (128–2048 px) and small-mark candidates are built and await Owner acceptance: inspect `08_QUALITY_AND_EVIDENCE/BRAND-EXPORT-05/PROOF_SHEET.png`, `05_EXPORTS/MANIFEST_BRAND-EXPORT-05.json` and `05_EXPORTS/CANDIDATES/small-mark/SOURCE_CANDIDATES/`. Remaining brand work (status only; nothing here is authorised):
    - Transparent on-dark and on-light PNG kits after RULING-02a/02b, from their own approved masters; white-page treatment under RULING-04.
    - Small-mark exports after RULING-05: favicon 16/32/48 + ICO, apple-touch 180, Android 192/512 with maskable safe-zone check, navbar files.
    - Widths above 2048 (e.g. 3072 for 3x screens) only if a placement needs them.
    - Final guidelines and controlled release LOGO-SYSTEM-v1.0.0: placement map, clear space, minimum sizes, theme rules, alt text "YCN Labs".
    - Vector-artist brief (RULING-03); artist delivery and acceptance are separate later outcomes.
    - Social avatar, Open Graph 1200x630, wordmark-only, print, single-ink and animation rows, only when required.
    - Website integration (separate website task): one BrandLogo component, srcset 1x/2x/3x, WebP/AVIF delivery copies, favicon set, dark/light switching, viewport and density tests, and a "use approved brand files only; never generate or redraw the logo" rule in the site's AGENTS.md, CLAUDE.md and GEMINI.md.
    - Independent external backup with a restore test; one coordinated CLOSE.
- **Website Workstream:**  
  **Next Task:** **`YCN-NAV-ORIGINAL-STYLE-01`**  
  Restore original cyan glow with fading tail at 80 px/s (Option A) with bounded test update to `__tests__/navbar-polish-04.test.tsx` (PENDING OWNER APPROVAL). Owner must say "A" and "yes" to proceed.

---

## 4. Pending Owner Decisions Register

1. **`RULING-02a` (Dark Transparent Master Approval):**  
   `ycn-logo-dark-transparent-MASTER.png` (5620×4580 RGBA, SHA-256: `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`). Native 1:1 scale with 6675 master. Same pixels, background removed. Safe to approve.
2. **`RULING-02b` (Light Transparent Master Approval):**  
   `ycn-logo-light-transparent-MASTER.png` (5620×4580 RGBA, SHA-256: `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`). On-light adaptation with dark-teal LABS and black YCN. Alpha IoU 97.25%. Owner judges by eye.
3. **`RULING-03` (Vector Master Production Authorization):**  
   Deferred to v2.0. Commission human vector artist with raster underlay. AI auto-tracing strictly rejected.
4. **`RULING-04` (Light-Theme Surface Treatment):**  
   On light backgrounds, display the dark mark inside a dark container tile pending finalized on-light artwork.

---

## 5. Superseded Directives & Historical Items (Do Not Execute)

- **`BRAND-FIND-01` (Logo Selection from Contact Sheets):**  
  **SUPERSEDED** by Owner RULING-01. The official logo is established and frozen under DECISION-001; do NOT search for alternative candidates or offer new logo selections.
- **Generative AI / Vector Auto-Tracing:**  
  **FORBIDDEN** under DECISION-001 and RULING-03.
- **Claims that 2048px is the sole master:**  
  **SUPERSEDED** by Owner RULING-01. The 6675px image is the authoritative parent source; 2048px is its uploaded reference downscale.
- **`tools/close-day.sh` as whole-project reconciliation:**  
  **SUPERSEDED** by `docs/CLOSE_PROTOCOL.md`. The legacy shell script only updates website `docs/STATE.md`; the canonical close protocol governs cross-project handoffs.

---

## 6. Files Outside Repositories & Security Isolation

- **Local Vault (`/home/ycn-labs/Desktop/YCN_LABS_MASTER/`):**  
  Contains confidential security audit (`_INTAKE/2026-10-12/YCN_LABS_INDEPENDENT_REPO_AND_DELIVERY_AUDIT_2026-10-12.md`), execution roadmap, raw proof renders, historical vector explorations, and large source archives. Because both active repositories are public, sensitive and security-critical documentation MUST NOT be committed to GitHub.
- **Desktop Original (`/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png`):**  
  Protected physical file anchor. Never deleted.

---

## 7. Operational Roles for Future AI Sessions

> Brand workstream from 14 Oct 2026: Claude plans tasks; GPT independently reviews tasks and evidence; AGY executes; the Owner approves artwork and authorises every push.

- **GPT:** Formulates strategy, scopes single atomic tasks, strictly respects `RESUME_HERE.md`.
- **Claude:** Inspects raw output, audits cryptographic hashes, enforces review gates: Commit → Evidence → Claude PASS → Owner push.
- **AGY:** Linux execution agent, runs commands, captures stdout/stderr, adheres strictly to non-destructive constraints.
