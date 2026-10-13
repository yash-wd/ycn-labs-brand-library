# YCN Labs — Current Source Authority & Asset Governance

**Document ID:** `00_GOVERNANCE/CURRENT_SOURCE_AUTHORITY.md`  
**Date Established:** 2026-10-13  
**Controlling Authority:** Owner RULING-01, Owner Decision `BRAND-DAY-CLOSE-09`  
**Status:** Permanent Controlling Baseline for All Brand & Identity Operations  

---

## 1. Scope of Brand Authority

All brand work happens in this library (`ycn-labs-brand-library`). Vault folders `ycn-brand-work/` and `ycn-brand-masters/` are frozen history; never write there.

This document serves as the supreme controlling authority for logo asset lineage across all repositories, design tools, and future AI pair-programming sessions.

---

## 2. Definitive Source Hierarchy

### A. Authoritative Master Source (RULING-01)
- **File:** `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png`  
- **Original Physical Location:** `/home/ycn-labs/Desktop/Main_YCN_LABS_logo_black_8K.png`  
- **Dimensions:** 6675 × 5195 pixels  
- **Color Depth & Format:** 8-bit RGB, opaque field (`#000205` / `[0, 1, 6]`), PNG  
- **File Size:** 6,633,409 bytes  
- **SHA-256:** `0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3`  
- **Governance Ruling:** Formally ratified under **RULING-01** (13 October 2026). It is consistent with being the parent source (aspect match 0.057%, IoU 95.92%, mean error inside artwork 1.09%). This file is the primary visual truth for all brand geometry, letterforms, and colors.

### B. Uploaded Reference Copy (Immutable Downscale)
- **File:** `01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png`  
- **Dimensions:** 2048 × 1593 pixels  
- **Color Depth & Format:** 8-bit RGBA (all 255 alpha, fully opaque), PNG  
- **File Size:** 3,158,172 bytes  
- **SHA-256:** `8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943`  
- **Role:** Preserved byte-for-byte as the Owner's uploaded reference copy and historic foundation package reference.

### C. Transparent Master Derivatives (Awaiting RULING-02)
- **Dark Transparent Master:**  
  `11_HISTORICAL_ASSETS/masters/ycn-logo-dark-transparent-MASTER.png`  
  - Dimensions: 5620 × 4580 pixels (8-bit RGBA)  
  - SHA-256: `85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784`  
  - Status: Candidate derivative. Forensic measurement confirms 1:1 scale (0.0000% width delta, 0.0644% height delta), dx=663, dy=320 translation (corr 0.993566), solid pixel mean |dRGB| = 1.6583/255, 0.0000% pixels > 16 delta. **Owner visual approval pending under RULING-02.**
- **Light Transparent Master:**  
  `11_HISTORICAL_ASSETS/masters/ycn-logo-light-transparent-MASTER.png`  
  - Dimensions: 5620 × 4580 pixels (8-bit RGBA)  
  - SHA-256: `416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9`  
  - Status: Candidate derivative. Alpha IoU with dark master = 97.2464%, Mean |dAlpha| = 4.8411. **Approval pending under RULING-02.**

---

## 3. Precedence Over Historical Documents

Historical documents preserved in this archive (including `00_GOVERNANCE/SOURCE_RECORD.json`, `00_GOVERNANCE/OWNER_SOURCE_RULING.md`, `12_ORIGINAL_PACKAGES/YCN_LABS_Brand_Source_Foundation_2026-10-13.zip`, and `10_AGENT_HANDOFF/CLAUDE_READ_FIRST.md`) were generated at earlier stages when only the 2048px reference was accessible.

- **Preservation Principle:** These records remain preserved for historical audit integrity.
- **Precedence Rule:** Where any historical document describes the 2048px image as the "sole authorized source", that statement is superseded by Owner **RULING-01** and this document.
- **Website Lineage (`DECISION-050`):** The website's historical `DECISION-050` records previous deployment lineage for website assets. Future brand production follows the current Owner source hierarchy. Updating the website's decision register will occur as a separate, authorized documentation task upon deployment of finished brand exports.

---

## 4. Vector Master Status

**No approved production SVG or vector master exists yet.**  
AI auto-tracing and generative redrawing are strictly forbidden. The final vector master is deferred to a professional human vector artist using the 5620/6675 raster underlay.
