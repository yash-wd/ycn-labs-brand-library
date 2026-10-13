# Release acceptance gates — no gate skipping

**Gate 0 — source integrity (mandatory immediately)**
- Transfer owner-supplied original, verify exact SHA-256, bytes, PNG dimensions, 8-bit RGBA and alpha==255. Do not auto-process.
- Require independent SHA-256 read back from destination and backup; fail on mismatch.

**Gate 1 — preservation and visual inventory**
- At 100% and 400%, compare all source details, especially faint internal lines, node rings, crescent outer edge, YCN breaks, LABS tracking and underline flare.
- Record original/source bounding boxes and geometry; no clipping.

**Gate 2 — reconstruction candidate (only after Owner authorizes work)**
- Record actual tools/versions and whether geometric layers are vector, filters, or raster backing. No embedded-raster SVG passed off as fully vector.
- Side-by-side tests are based on true rendered assets, not artist's sketches or simulated substitutes.
- Compare matched-size/matched-canvas images in a controlled profile; do NOT stretch different aspect ratios to line up or quote meaningless global average percentages dominated by dark background.
- Use region-specific overlay, 1px edge crops, missing-point/line inventory, luminance/gradient/glow comparisons, optical review.
- Test on white and dark hosts, multiple viewports and outputs 16/32/48/64/128/256/512/1024/2048 where relevant; record any loss of legibility.
- Owner must visually approve specific version/hashes. Technical scores alone cannot prove exact identity.

**Gate 3 — export reproducibility**
- Every derivative generated from the same *approved* artwork; export tool versions, profiles, rasterizer, size, background/alpha and code recorded.
- No stretching, non-proportional resizing, color cast, clipping or unexpected matte/halo.
- Metadata manifest and file checksums automatically created; repeat build compare hashes (allow justified encoder/platform differences with evidence).

**Gate 4 — theme variants and print**
- On-dark can use original as-is. On-light adaptation requires explicit approval if artwork changes.
- CMYK artwork and print proofs validated by designer and print vendor; web color values do not guarantee appearance on fabric/foil/paper.

**Gate 5 — release and rollout**
- Owner approves named exact files and checksum; reviewer independently verifies.
- Create immutable versioned release; keep release notes + rollback copy + staged deployment screenshots.
- Migrate public site only under separate task; lint/types/tests/build and viewport/theme QA; rollback demonstrated.

**Gate 6 — governance**
- Keep 3-2-1 backup copies (separate medium + offsite), periodic checksum/restore tests, least-privilege access, no public release of editable sources unless specifically authorized.
- Keep rejected, obsolete and legacy graphics quarantined and labeled, not erased during active work.
