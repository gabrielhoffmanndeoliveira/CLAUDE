<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# amerex

- **A bracket that is a VEHICLE bracket, and a material claim removed by the inverted
  proof.** Amerex `818`'s title read *&quot;Steel Fire Extinguisher Bracket (Red)&quot;*
  and **never said vehicle or marine**; Amerex's parts book gives `01211-P` as
  *&quot;Vehicle/Marine Bracket (Red) &mdash; All 5 lb., 5&frac12; lb. Aluminum Valve
  Models&quot;* and files it under Vehicle/Marine/Aviation in three documents. A buyer
  wanting a wall hanger receives a vehicle bracket, and the reverse.
  **&quot;Steel&quot; was dropped, and the reason is the `DN-62046` inverted proof in
  miniature: Amerex states a material when it means to** &mdash; the wall-hanger list on
  the same page carries *&quot;Wall Hanger Bracket (Stainless Steel)&quot;*. It is very
  likely steel and it is not stated; **if TFAS can read it off a carton it should go back
  in.** The separator no distributor states: **`821` covers the same 5 lb. and 5&frac12;
  lb. sizes but is listed for aluminum AND brass valve models**, so the valve and not the
  cylinder weight decides.
  Route: **Amerex's product pages are useless and its document library is enumerable.**
  `/products/fire-extinguisher-brackets/` **404s**, the category page is a JS shell with
  zero PDF links and `robots.txt` is a 10-byte comment &mdash; but the raw markup of
  **`/learning-center/product-brochures/`** discloses **60 PDFs** under
  `/upl/downloads/content-blocks/<slug>.pdf`, mime-clean, no bot protection. Fourth brand
  recovered by reading markup rather than the rendered page.
- **The Amerex two-line header paid a second time, and the product-photo captions invert in
  plain text.** Page 19's header is two lines plus a fragment: reading one line alone gives
  `INCLUDED / USCG / OPTIONAL / STRAP / DOLLY` with no noun, or
  `BRACKET / BRACKET / BRACKETS / BRACKETS / OPTION` with no qualifier. And the photo captions
  extract as `397 P/N 15509 / 398 P/N 15510 / ALUMINUM VALVE`, **attributing aluminum to the two
  brass models** &mdash; coordinates put ALUMINUM VALVE at x 97&ndash;190 under the left cluster
  and BRASS VALVE at x 304&ndash;375 under 397/398.
  **The `B` prefix does NOT mean brass valve on the Halotron line**: A384T, B385TS, B386T and
  B394TS all carry **anodized aluminum** valves, corroborated by the parts book filing their
  brackets under *&quot;Aluminum Valve Models&quot;*. What A and B do encode is **stated in no
  Amerex document read**, and so is `TS` &mdash; both recorded as bounded negatives rather than
  guessed. This also bounds the recorded Amerex rule *&quot;the valve, not the cylinder weight,
  decides&quot;*: that was derived on the **strap** brackets, and the parts book scopes these by
  **both** weight class and valve type.
  A per-model inversion a reader would get backwards: **the 1.4 lb A384T runs at 125 PSIG and
  the larger 2.5 lb B385TS at 100.** And a live title defect fixed in the Shopify `title` field,
  so it cost the feed too: `15231` read *&quot;Amerex **Fire** B385TS&quot;*, a stray token from
  the amerex-fire.com domain slug.
