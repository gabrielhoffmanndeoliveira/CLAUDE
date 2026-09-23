<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# macurco

- **Two recon coverage figures were not reproducible, and the corrections are instructive
  rather than embarrassing.** Recon reported Det-Tronics at **89%**; the true answer is
  **zero**. The 801-item library holds only family-level assets (`X5200a.png`,
  `x2200-ultraviolet-flame-detector.png`), **no filename contains any of the 23 catalogue
  SKUs**, and REST searches for the bare part numbers return 0 rows. Recon's hits were
  family-level matches, which the boundary rule correctly forbids &mdash; `X5200` followed
  by `a` is alphanumeric. Recon reported Macurco at **48%**; that was measured on the
  *detector subset*. Of the brand's 91 products **51 are cal-gas cylinders, VRF replacement
  sensors, cal-kits and calibration fees**, for which no per-SKU asset exists and should
  not. **A coverage figure is meaningless without the denominator it was measured on.**
- **Thirteen titles assert a REGULATORY APPROVAL with no manufacturer source, and the
  agent found it by failing to source one of them.** An agent could not document the
  `-LADBS` suffix on `CX-6-LADBS` and said so; checking the live catalogue for the string
  returns **13 Macurco SKUs carrying `LADBS` in the title** &mdash; `CM-6`, `CM-12`, the
  whole `CX-6`/`CX-12` family and five `DVP-` panels. **LADBS is the Los Angeles Department
  of Building and Safety: an approval designation, not a product variant.** The suffix
  appears nowhere in Macurco's Rev 2.1.0 manual; macurco.com asserts *&quot;City of Los
  Angeles Approval&quot;* first-party, but the approval document sits behind
  `docs.macurco.com/file/<id>`, a ~15.5 KB JS shell.
  **A regulatory approval in a Merchant Center feed attribute is a different class of claim
  from a spec**, and this is the first time one has surfaced here. Nothing was changed; all
  thirteen went to the owner, because the fix is not research &mdash; **one look at the
  LADBS research-report database, or the report number from Macurco, settles all thirteen
  at once.**
- **Three first-party documents of one manufacturer disagreeing with each other, and
  publishing nothing from any of them.** Macurco's 2018 `GD-6` manual against the current
  macurco.com page: DC supply **12&ndash;48 VDC** (manual, stated twice) against
  **12&ndash;32** (site); listing **UL 61010-1** against **UL 2075 and ULC 588**;
  coverage **900 sq ft** against **1,257**. No DC limit, no standard number and no
  coverage figure went into the copy. **The listing one is worth the owner's attention:
  UL 2075 is a materially stronger claim than UL 61010-1**, and a distributor quoting
  either has a first-party source for it. The manual separately prints
  `4-1/2 x 4 x 2-1/8 in.` against `11.4 X 11.4 X 5.3 cm`, which does not convert.
  Route: **`macurco.com` has an open WordPress REST media API** serving first-party PDFs
  from `wp-content/uploads/`, which **bypasses the `docs.macurco.com` bubble.io shell
  entirely** &mdash; that shell's fingerprint reproduced at 15,547&ndash;15,548 bytes
  `text/html` for two different file ids.
- **Twenty-third product-class error, and the wrong title names precisely the single-gas sibling.**
  `CX-12` was titled *&quot;Nitrogen Dioxide Gas Detector&quot;*. **The bare `CX-12` is Macurco's
  dual-gas CO *and* NO&#8322; monitor.** Verified by the coordinator against Macurco's own WordPress
  product index with an honest bogus control (0 rows): `CX-6 / CX-12`, `CX-6-NO2 / CX-12-NO2` and
  `CX-6-CO / CX-12-CO` are **three separate product records**. So a buyer filtering for carbon
  monoxide never saw a $1,041 product, and a buyer wanting NO&#8322; alone could be sent the
  dual-gas one. Also settled: **in this family the 6/12 is the SUPPLY, not the gas** &mdash; CX-6
  low voltage, CX-12 line voltage.
  **And the UL 2075 split is a Macurco BRAND CONVENTION, confirmed on a second family in the same
  batch.** The CX manual reads *&quot;CX-6, CX-6-CO, CX-6-NO2 &ndash; ETL LISTED: Conforms to Std.
  UL 2075&quot;* against *&quot;CX-12, CX-12-CO, CX-12-NO2 &ndash; **Designed to meet** UL Std. UL
  2075&quot;*, and macurco.com's CM page carries **&quot;ETL Listed to UL 2075 (CM-6 Only)&quot;**
  twice. **The line-voltage 12-series models are not UL 2075 listed**, on either family. Worth
  having on file before another 6/12 pair comes through.
- **Macurco's two open endpoints, with honest controls:** the WordPress media API carries **1,633
  items** and the WooCommerce Store API **85 products**, the latter returning `[]` for a bogus term
  &mdash; so a miss there is a real negative. Use `macurco.com` **without** the `www.`; the `www.`
  host 301s to zero bytes.
