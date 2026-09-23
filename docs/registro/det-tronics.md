<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# det-tronics

- **Det-Tronics re-confirmed a true zero, and the boundary rule is precisely what does it.**
  The media API works via **`curl -L` against the `www.` host** &mdash; and note **`urllib`
  now gets an HTML shell where this file records a 403**, so that reversal has reversed again.
  326 images across four pages, and **not one filename contains any catalogue SKU or ordering
  code**: only `X5200a.png`, `x5200-ultraviolet-infrared-flame-detector.png`, `X2200a.png`.
  **`X5200` followed by `a` is alphanumeric**, so the rule refuses exactly the family match
  the discredited 89% figure was built on. **A zero that the rule produces on purpose is a
  result, not a failure.**
- **A ground-fault monitor whose own approval is conditional on an enclosure it does not
  include.** `007941-001` was the raw ERP string `EQ2220GFM (007941-001) GRND FLT MONITOR, EQP`
  in the Shopify **title**, so it cost the feed as well as the page &mdash; fourth instance of
  the raw-ERP-title shape after `010254-008`, `MX16RSF-US` and `SLM-318`. Det-Tronics publishes
  **no document of its own for it**: the WordPress media API is honest (`search=X3301` returns
  real PDFs, `search=EQ2220`, `search=ground` and `search=fault` all return `[]`), and the part
  appears on exactly one page of the EQP manual `95-8533 Rev 25.0`, in the Ordering Information
  block under the heading **POWER SUPPLIES**. The series-block trap fired there too: the GFM
  spec block ends without a CERTIFICATION line and the next page opens with one, so the Class I
  Division 2 T4 rating was claimed **only** because Appendix B names `EQ2220GFM` explicitly
  &mdash; a second, model-attributed source &mdash; and the copy states that the rating applies
  inside a suitable certified enclosure, which this DIN-rail module is not.
  The live body's *&quot;part of the Det-Tronics **Eagle Quantum**&quot;* was corrected to Eagle
  Quantum **Premier**, every occurrence being in Premier literature.


### t09 (23 Sep 2026)

- **EQ2175PS / EQ2130PS (000604-015 / -014):** EQP manual 95-8533 Rev 25.0 (Aug 2025): ordering p.95, specs p.103. These are Eagle Quantum Premier power supply/battery chargers, 75 A / 30 A at 24 VDC. **The 60 Hz models are 120/208/240 VAC; "220/240" is only the 50 Hz EQ2176PS (000604-036).** The store titles' "120/208/220" was wrong and has been fixed.
- **004000-903 "W867C3001-R":** W867 is Det-Tronics' own UV/IR flame detector test lamp (manual `95-8309-5.1_W867.pdf`, 004000-003 = W867C3001 120 VAC). **004000-903 and the -R suffix are in no document** (SKU flagged). `/legacy-products/` is a first-party lifecycle table (ROS = repair only, OBS = obsolete, factory replacement); it lists W867A/B/C as obsolete, replaced by W867C3004 (the store sells it as 004000-006; lifecycle flagged).
- **Search endpoints:** site search `?s=` echoes the query and does not discriminate; `wp/v2/pages?search=` does (bogus returns []). The WP media search matches titles only.
