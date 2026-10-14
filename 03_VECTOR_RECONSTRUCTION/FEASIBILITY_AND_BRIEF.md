# Precision reconstruction brief — not approval to redraw

> Note (14 Oct 2026): under RULING-01 the source is the 6675 × 5195 master `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png`. The 2048 × 1593 figure below describes the earlier reference copy.

## Engineering truth

- PNG is a raster grid of 2048 × 1593 pixels with opaque background, no independent art layers.
- There is **no guaranteed reversible operation** to recover original Bézier geometry, text vectors, gradient stops, soft blur/glow sources or transparency from that flattened result.
- Typical auto-tracing smooths strokes, merges near-dark lines into the background and alters flare/glow. Therefore it is unsuitable as a one-click production master here.
- Wrapping an `<image>` tag inside SVG does not make native resolution-independent vector art.
- A useful future **hybrid** logo might combine verified vector paths for lettering/geometry with tested resolution-aware raster/gradient glow effects. State limitations rather than declaring all-vector falsely.

## Proposed production method (subject to separate explicit approval)

1. Freeze and verify original source, visual reference and metadata.
2. Decompose visually into planes: dark field; crescent; orbital lines; connectivity; nodes; YCN paths; LABS paths; underline; glows.
3. Carefully trace or reconstruct crisp geometry from the reference; preserve angles, gaps, dot positions, tracking and curves.
4. Treat blue gradients and volumetric luminous halos as separate test layers, with original image remaining authority.
5. Pixel-aligned overlays at identical geometry (no aspect-ratio changes or arbitrary bounding-box stretching); use color difference, alpha/edge metrics, region-specific geometry inspection, missing-element check, and human overlay review.
6. Verify at natural size, at high zoom and on standard light/dark presentation contexts; run against original source screenshot without color management ambiguity.
7. Create a draft SVG and production-proof PNG *only if the Owner authorizes this phase*. Do not distribute as approved pending actual visual sign-off.
8. If exact fidelity is not achievable, keep original raster as only official visual and explicitly limit sizes/usage. Do not fake '8K' or overpromise infinite detail.

## Explicit unacceptable outcomes

- Missing or thickened connecting lines.
- Flattened crescent gradients, altered glow positions, simplified circular nodes.
- Incorrect stylized YCN lettering, changed LABS tracking, missing underline flare.
- Black background removal that drops the faint network or introduces visible dark/white fringe.
- New shadow, tint, bloom, ornament, font or rebalanced spacing.
- 'AI-enhanced' or hallucinated missing detail represented as exact reproduction.

## Required deliverables from a reconstruction vendor

Editable geometry master (e.g., SVG/AI source if truly vector), layer/provenance documentation, optical comparison proofs, any raster glow ingredients explicitly labeled, human visual QA record, operating/rendering dependencies, export recipe, color-management choices, final Owner approval record with asset hashes.
