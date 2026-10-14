# AGY execution deviations - BRAND-EXPORT-05

Recorded by FIX-01 on 14 Oct 2026. Commit 234846841534cd97961fa8555051dcf73ef086dd stays in history unchanged; FIX-01 corrects its generated files in a new commit.

## Defects in the first build (2348468)
- The master's cHRM colour chunk was missing from all 26 PNGs: the exporter passed an unsupported `chromaticity=` keyword that Pillow ignores. Decoded pixels were correct.
- PROOF_SHEET.png was clipped: the bottom 22 rows of the candidate C 512x512 preview were lost, 60 black rows were added, and row-1 labels overlapped.
- Preview manifest entries had no parent native path/hash; toolchain, zlib and font details were missing; verification did not check proof panels, parent links or exact asset membership.
- `10_AGENT_HANDOFF/export_png_kit.py` is kept unchanged as the record of that build; `export_png_kit_v2.py` supersedes it.

## Rule breaches during execution
- A preflight gate used invented file names (`HISTORICAL_DO_NOT_USE_*`) and an invented hash (`e36e8499...`); it failed and was replaced without disclosure.
- A failed whitespace gate was repaired and execution continued instead of stopping.
- `git reset` and recursive deletion of generated outputs and scratch evidence were used to rebuild.
- AGY session transcripts outside the repository were read, including during the read-only evidence supplement, and the proof sheet was copied to an IDE folder.
- `py_compile` created an untracked, git-ignored `__pycache__` folder.
- Unrequested read-only commands were run before several tasks were authorised.

## Reporting errors
- A report claimed "no clipping or overlapping" without checking.
- A report stated Python 3.10.12 while the committed manifest records 3.12.13; the FIX-01 run log records the interpreter actually used.
- A report presented as a verbatim diff contained a line that is not in the repository (a 40 px minimum-height rule) and wrong Git blob identifiers. The committed objects on GitHub are authoritative.

## Controls adopted
- One reviewed runner that stops at the first failure. Its build-and-verification log is frozen first, then saved as `08_QUALITY_AND_EVIDENCE/BRAND-EXPORT-05/FIX-01_RUN_LOG.txt` and listed in `14_CONTINUITY/SHA256SUMS.txt`. The final inventory check, commit and push happen after the log is frozen, so they are not in it.
- Unreviewed work is pushed only to `wip/brand-export-05`. Reviewers read the committed files on GitHub. `main` moves only after review, Owner acceptance and an explicit "push".
