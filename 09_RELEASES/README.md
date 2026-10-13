# Immutable release policy

- Approved release files only. Do not overwrite published asset hashes in place.
- A release contains `README`, `LOGO-USAGE`, `MANIFEST.json`, `SHA256SUMS.txt`, export script/version, validation logs, Owner approval ID, preview evidence, rollback instructions.
- Version naming: `YCN_LABS_logo-lockup_on-dark_v1.0.0.png`; on-light means intended background, not recolor by assumption.
- A pixel/geometry/wordmark/color change requires new signed decision and potentially major version; only export bug fix/repackaging with same design is a patch release.
- Public Git repository and CDN should store approved distribution exports only; protected design source remains outside the website's public directory.
- Use restricted master storage; build/distribute from a canonical manifest and script. Maintain 3-2-1 backup policy and periodic restore test.
