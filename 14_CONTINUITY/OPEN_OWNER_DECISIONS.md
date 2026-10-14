# Owner Decisions Register

## DECIDED:
- **RULING-01: Parent Source Ratification (DECIDED 13 Oct 2026)**
  - **Verdict:** "6675 is the original; 2048 is its uploaded copy."
  - **Details:** `Main_YCN_LABS_logo_black_8K__6675x5195.png` (SHA256: `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`) is ratified as the Authoritative Master Source. The 2048×1593 file (`8b982547...`) is maintained as its uploaded reference downscale.

---

## PENDING / OPEN:
1. **RULING-02a: Dark Transparent Master Approval (PENDING)**
   - *Scope:* `ycn-logo-dark-transparent-MASTER.png` (5620×4580, SHA256: `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`).
   - *Forensic Metrics:* Native 1:1 scale with 6675 master (0.0000% w, 0.0644% h delta), dx=663, dy=320 offset, 0.0000% pixels > 16 delta. Same pixels, background removed. Safe to approve.

2. **RULING-02b: Light Transparent Master Approval (PENDING)**
   - *Scope:* `ycn-logo-light-transparent-MASTER.png` (5620×4580, SHA256: `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`).
   - *Forensic Metrics:* Recolored for white backgrounds (black YCN, dark-teal LABS). Alpha IoU with dark master = 97.2464%, Mean |dAlpha| = 4.8411. Shape edges differ by ~3% (design adaptation). Owner judges by eye.

3. **RULING-03: Vector Production Authorization (PENDING)**
   - *Status:* Deferred to v2.0.
   - *Scope:* Commission a human vector artist to redraw the logo as layered SVG/AI using the 5620/6675 raster underlay. AI auto-tracing rejected.

4. **RULING-04: Light-Theme Surface Treatment (PENDING)**
   - *Status:* On light backgrounds, display the dark mark on a dark tile panel until an independently approved on-light recolored artwork is authored.
5. **RULING-05: Small-Mark Selection (PENDING)**
   - *Scope:* Native crop candidates A (YCN crop; navbar), B (YCN-centred square; favicon) and C (full-logo square; app icon) in `05_EXPORTS/CANDIDATES/small-mark/SOURCE_CANDIDATES/`; previews in `05_EXPORTS/CANDIDATES/small-mark/`.
   - *Rule:* Each approval names one exact native file, its full SHA-256 and its permitted use; different uses may use different candidates. Choosing a preview is not approval. The Owner may reject all candidates; rejection does not by itself authorise a redesign or commission.

6. **BRAND-EXPORT-05 Acceptance (PENDING)**
   - *Scope:* Owner visual acceptance of the five opaque exports in `05_EXPORTS/WEB/full-lockup_on-dark-opaque/`, via `08_QUALITY_AND_EVIDENCE/BRAND-EXPORT-05/PROOF_SHEET.png`.
