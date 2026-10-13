# YCN Labs Brand Library — Close Protocol Integration

**Canonical Specification:** [`ycn-labs-site/docs/CLOSE_PROTOCOL.md`](https://github.com/yash-wd/ycn-labs-site/blob/main/docs/CLOSE_PROTOCOL.md)  
**Document ID:** `14_CONTINUITY/CLOSE_PROTOCOL.md`  
**Effective Date:** 2026-10-13  
**Status:** Brand-Specific Rules for Permanent Close Protocol  

---

## 1. Canonical Reference

The standing Owner Close Protocol is defined canonically in the website repository at `docs/CLOSE_PROTOCOL.md`. Whenever the Owner says **CLOSE**, that procedure must be executed across both repositories and local working directories.

---

## 2. Brand-Specific Reconciliation Rules

During the close execution, the Brand Library adheres to the following mandatory standards:

1. **Intake Classification & Candidate Routing:**
   - Any newly discovered logo files, brand documentation, or brand AI handoffs route exclusively into the appropriate numbered folder in `ycn-labs-brand-library`.
   - New artwork enters **ONLY** as a candidate file under `11_HISTORICAL_ASSETS/` or `03_VECTOR_RECONSTRUCTION/`.
   - **NEVER** place unapproved artwork directly into `04_APPROVED_LOGO_VARIANTS/`. Only files formally approved by the Owner may enter `04_APPROVED_LOGO_VARIANTS/`.

2. **Immutable Source Protection:**
   - The authoritative master `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png` and reference downscale `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png` must never be altered, overwritten, or removed.
   - The desktop file `/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png` is permanently protected.

3. **Cryptographic Checksum Verification:**
   - Prior to closing, regenerate and verify `14_CONTINUITY/SHA256SUMS.txt` against all tracked files in the brand library (`sha256sum -c 14_CONTINUITY/SHA256SUMS.txt`).
   - Notice: `PACKAGE-SHA256SUMS.txt` reflects the static delivered ZIP from 13 Oct. Modified governance files show FAILED under that static check; live verification is governed by `14_CONTINUITY/SHA256SUMS.txt`.

4. **Public Repository Safety Audit:**
   - Because `ycn-labs-brand-library` is a public repository, ensure no proprietary credentials, private business communications, or confidential security audits are committed.
   - Security audits, large files (>25 MB), and raw intake dumps are preserved strictly in `/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/_INTAKE/<YYYY-MM-DD>/`.

5. **Continuity Documents Update:**
   - Every close must update `14_CONTINUITY/CURRENT_STATUS.md`, `14_CONTINUITY/OPEN_OWNER_DECISIONS.md`, `14_CONTINUITY/BRAND_ASSET_INDEX.tsv`, and `14_CONTINUITY/RESUME_HERE.md`.
   - `START_TOMORROW.md` remains a permanent one-line pointer to `RESUME_HERE.md`.
