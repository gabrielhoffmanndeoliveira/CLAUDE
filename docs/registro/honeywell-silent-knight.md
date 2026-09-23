<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-silent-knight

- **Two revisions of one Honeywell datasheet disagree on the number a battery
  calculation depends on.** Silent Knight `350098` **Rev K (02/22)** gives the 5815XL
  &quot;Standby &amp; Alarm Current: 55 mA&quot;; **Rev J (01/18)** gives &quot;55 mA
  minimum &ndash; 125 mA max&quot;. No current figure was published. Rev J also lists
  5820XL and 5820XL-EVS IntelliKnight compatibility that Rev K drops, and **no document
  says support was withdrawn**, so the copy states the current list and mentions the
  older one as a relationship rather than asserting a discontinuation either way.
- **A new category for the denominator audit: a SKU that is a CABINET photographed with a
  populated panel.** `006820CB` is the Silent Knight 6820 **cabinet**, and its only asset
  is a red enclosure containing a fully populated 6820 panel with the door silkscreened
  &quot;Model 6820 Fire Alarm Control Communicator&quot;. That is the incomplete-product
  trap in picture form &mdash; the inverse of the thirteen text cases, where a bare
  component was *described* as a complete product. Here a complete product is *pictured*
  on a bare component's page. It is also the brand's only SKU, which is why Silent Knight
  reads 0%.
- **`U` = ULTRA Series across Honeywell and Silent Knight**, manufacturer-stated:
  6808U, 6820U, IFP-300U, IFP-1100U, FCP-300U, with Honeywell's own firmware page listing
  the conversions (`6820 -> 6820U`). A one-letter suffix that names a product generation,
  and none of the affected titles said so.

- **EVS-CE4 (enrichment e02):** `manuals-and-guides/installation-guides/hbt-fire-LS10070-001SK-E-B2-EVS-CE4-installation-manual.pdf` (B2, 12/8/2021; Rev A1 at `LS-10070-001SK-E.pdf`). Adds circuits 5&ndash;8 to EVS-50W/EVS-125W, 20 mA / 180 mA. Rev A1 lists 5820XL-EVS only; B2 adds 6820EVS. Datasheet 351631 also names the EVS-100W (coordinator-verified) &mdash; the title names the two the install sheet names. 350605-E and 350606-D both claim &quot;up to four amplifiers &hellip; total of 500 watts&quot;, which does not add up for the EVS-50W &mdash; not published. Type Speakers flagged.

### e04 (23 Sep 2026): SK-F485C and SD505-6IB, ad-candidate lot

- **SK-F485C is multimode.** LS10004-001SK-E:C (12/13/2021) specifies duplex 62.5 µm multimode fibre, duplex ST connectors, up to 1.0 mile (1.6 km) and 115.2 kbit/s, and calls it "a module used in pairs". Rev A (2012), data sheet 350806 Rev C 12/17 (Silent Knight) and 351559 Rev C 02/22 (Farenhyt) agree. Route: EDAM `manuals-and-guides/installation-guides/hbt-fire-LS10004-001SK-E-C-SK-F485C-installation-manual.pdf`. The 5815RMK remote mounting kit is required with the 5808, 5700 and 6700, and is not stocked. The Honeywell product page's structured data files it under "discontinued-products" while the banner is hidden (`d-none`). That is page chrome, flagged low.
- **SD505-6IB is not a detector base.** Data sheet 350316 Rev D (2010) heads it "6” Isolator Module" and says it "fits underneath the SD505-6AB detector base". Installation sheet 151175B (12/00) calls it an extension base. The coordinator changed the title noun from Base to Module, the manufacturer's term. The two documents disagree on the back box (dual gang/4 in. square/octagon vs single or double gang), so it was left out of the copy. The SD505-6AB is not stocked, and whether it comes in the carton is unsettled (flag).
