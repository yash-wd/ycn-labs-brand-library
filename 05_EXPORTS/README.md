# Planned export families — intentionally not generated

See `EXPORT_MATRIX.csv`. Never bulk-generate assets from an unapproved reconstruction.

Raster PNGs are lossless for the pixels they store but are fixed-resolution. New 4096/8192px resizes of a 2048px source do not recover real detail. SVG vectors scale clean geometry but optical glows may require separate filters or resampling. JPEG is not a master format, especially for transparency; WebP/AVIF can be appropriate delivery encodings.

Only after master approval, generate responsive 1x/2x/3x assets as needed by real viewports rather than hundreds of arbitrarily sized files.
