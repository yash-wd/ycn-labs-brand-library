# AGY — BRAND-SOURCE-CONTROL-03 (one task, no visual modification)

**Owner's updated binding ruling:** The only official YCN Labs logo is the Owner-supplied file `Main_YCN_LABS_logo_black_8K.png`, SHA-256 `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`. All other vectors, reconstructions, PNG masters and website outputs are historical or unapproved unless separately signed off by Owner. Preserve `DECISION-001`; append a new decision superseding conflicting source-reference claims in `DECISION-050`, but do not modify `docs/YCN_DECISIONS.md` without a separate approved documentation task.

**Precondition:** The Owner must transfer this exact original PNG to the workstation as a new direct upload, ideally into `YCN_LABS_MASTER/01_CURRENT_PROJECT/ycn-brand-work/06-owner-source-intake/`. Do not retrieve a different-looking file based on its name; do not proceed if not provided or if hash mismatches.

**Authorized scope: read-only audit and create only new source-preservation directory, pending Owner's approval to execute.**

1. Run standard git preflight, record HEAD and worktree status; read repository rules. Do not modify repo.
2. Locate transferred Owner file; verify `sha256sum` equals `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`. Verify actual PNG dimensions 2048×1593, file size 3158172 bytes, PNG RGBA with alpha uniformly 255. Reject any mismatch.
3. Create (if absent) only `YCN_LABS_MASTER/01_CURRENT_PROJECT/YCN_LABS_BRAND_LIBRARY/01_IMMUTABLE_SOURCE/` and copy the Owner file byte-for-byte there. Do not touch existing originals. Verify output checksum.
4. Copy/source-install documentation kit into **new** subfolders of that library if and only if Owner supplies it, without overwriting any preexisting files or replacing existing policies silently.
5. Catalog legacy/logo files only by pathname and status. Mark earlier vectors, September prototypes, `ycn-brand-masters` and production web assets as `LEGACY_REVIEW_PENDING`; never delete, move or label them approved by proximity.
6. Produce `SOURCE-FREEZE-REPORT.md`: exact source/destination, timestamps, source and destination hash, PNG metadata, git status, raw commands+exit codes, any collisions; describe what was NOT done.
7. For a future separate task, recommend precision vector/hybrid feasibility, including micro-line/glow preservation. Do not generate/recolor/retouch, remove background, AI-upscale, or create final light/dark assets during this task.
8. No push/commit/deployment, no dependency install, no originals altered. No deletes. Stop on first hash or precondition failure and report.

**STOP.** Wait for Claude audit and Owner approval to proceed to the distinct reconstruction and derivative-production tasks.
