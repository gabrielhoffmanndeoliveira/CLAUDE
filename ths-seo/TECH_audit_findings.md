# The House Supplier - technical SEO audit (working draft, written section by section)

Date: 2026-11-11. Sources: Ahrefs Site Audit (project 10234181), Search Console data in Ahrefs, live theme "THS - Main (zone planner link 22/10)" (gid://shopify/OnlineStoreTheme/167456145511) read through the Shopify Admin API. Nothing was changed in the store, the theme or Ahrefs. The store's own URLs could not be fetched from this environment, so nothing here was checked against the live HTML.

(The summary with the three most valuable fixes is added at the top when the audit is complete.)

## 1. Liquid error in sections/ths-pdp-v2.liquid line 124

**Found.** Line 124 renders the main product image:

    <div class="pv2-main"><img id="pv2-main-img" src="{{ product.featured_media | image_url: width: 1000 }}" alt="{{ product.featured_media.alt | default: product.title | escape }}" width="1000" height="1000"></div>

`image_url` raises "invalid url input" when its input is nil. For a product with no media, `product.featured_media` is nil, so Liquid prints the error text inside `src="..."`. The browser and crawlers resolve that text as a relative URL, which gives `/products/Liquid error (sections/ths-pdp-v2 line 124): invalid url input` (404).

**Evidence.**
- Ahrefs: the 404 URL has 2 incoming links, both image links, from exactly two pages: `/products/2-1-10-15-air-test-gauge-w-test-body` and `/products/toto-usa-aquia-iv-washlet-s550e-cotton-elongated-bowl-1-28-0-8-gpf`.
- Shopify: both products are ACTIVE with `mediaCount = 0` and `featuredMedia = null` (gid://shopify/Product/7715698016359 Pasco 1726-10G; gid://shopify/Product/7716752490599 Toto ST446EMA#01).
- `templates/product.json` (the default product template) and `templates/product.pdp-v2.json` both use the `ths-pdp-v2` section, so every product without an image is affected, not only a pilot group. The section's own comment still says "Used only by templates/product.pdp-v2.json", which is no longer true.
- The same unguarded pattern is on line 214 (accessory card: `a.featured_media | image_url: width: 240`): it fails the same way when a "Frequently bought with" product has no image. Lines 128 and 262 loop over `product.media` and are safe when there is no media.

**Fix (theme edit).** Guard the filter and show the theme's placeholder when there is no image. Exact current and proposed lines are in TECH_theme_patches.md (patches 1 and 2).

**Also do (Shopify admin):** add an image to the two products above. A product page without an image is also not eligible for Google Shopping and image results.

**Who:** theme edit (developer or theme code editor); images in Shopify admin.
**Expected effect:** removes the 404 URL and the broken image on every product without media; no ranking effect on its own, but it removes a visible error on the page.

