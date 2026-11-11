# The House Supplier - technical SEO audit

Date: 2026-11-11. Nothing was changed in the store, the theme or Ahrefs.

**Sources.** Ahrefs Site Audit, project 10234181 (pages crawled between 2026-11-09 and 2026-11-11; the audit keeps recrawling, so some counts differ slightly from the 2026-11-09 figures); Search Console data in Ahrefs for 2026-08-11 to 2026-11-10 (the API returns the top 500 pages only); the live theme "THS - Main (zone planner link 22/10)" (gid://shopify/OnlineStoreTheme/167456145511) and store data read through the Shopify Admin API.

**Limits.** The store's own URLs could not be fetched from this environment. Statements about page HTML come from the copy Ahrefs stored when it crawled, checked on seven pages (home, two collections, three products, one vendor page). The rendered `robots.txt` could not be read (Ahrefs holds no copy); only its Liquid template was.

**Companion files:** `TECH_theme_patches.md` (six theme patches), `TECH_links_to_redirects.csv`, `TECH_missing_meta_descriptions_urls.csv`, `TECH_missing_meta_descriptions_matrixify.csv` and its ROLLBACK (both header only, see section 3).

---

## The three most valuable fixes

1. **Fix the "Request a quote" link on the product page (theme patch 4, one line).** `sections/ths-pdp-v2.liquid` line 201 links every product page to `/pages/request-a-quote`, a page that does not exist. That one line is the whole "16,245 pages link to a broken page" issue. The redirect added on 2026-11-11 stops the 404, but every product page still links to a redirect until the line is changed.
2. **Send the product-page brand link to the brand collection and noindex the vendor pages (theme patches 3 and 5).** Line 135 of the same file links the brand name to `/collections/vendors?q=<Vendor>`. The crawl holds 114 of these auto-generated pages with 8,957 internal links pointing at them. They duplicate the brand collections, 113 of them have no meta description (that is the whole "missing meta description" issue apart from the cart), and their canonical tag points to a differently-cased URL. A brand collection exists for 112 of the 113.
3. **Give the brand-plus-category collections internal links, starting with Rheem and Navien tankless (Shopify admin: navigation and content).** `/collections/navien-tankless-water-heaters` has 11 internal links and `/collections/rheem-tankless-water-heaters` has 66, while collections in the main menu have 17,219. Neither is in the menu, and the tankless products' breadcrumb and "more in" links go to `/collections/tankless-water-heaters-gas`. Details in section 8.

The Liquid error asked about first (section 1) is a confirmed two-line theme fix (patches 1 and 2). It affects the two active products that have no image, so it is quick to fix but small in effect.

---

## 1. Liquid error in sections/ths-pdp-v2.liquid line 124

**Found.** Line 124 renders the main product image:

    <div class="pv2-main"><img id="pv2-main-img" src="{{ product.featured_media | image_url: width: 1000 }}" ...></div>

`image_url` raises "invalid url input" when its input is nil. For a product with no media, `product.featured_media` is nil, Liquid prints the error text inside `src="..."`, and crawlers resolve that text as a relative URL: `/products/Liquid error (sections/ths-pdp-v2 line 124): invalid url input` (404).

**Evidence.**
- Ahrefs: the 404 URL has 2 incoming links, both image links, from `/products/2-1-10-15-air-test-gauge-w-test-body` and `/products/toto-usa-aquia-iv-washlet-s550e-cotton-elongated-bowl-1-28-0-8-gpf`.
- Shopify: both products are ACTIVE with `mediaCount = 0` and `featuredMedia = null` (gid://shopify/Product/7715698016359, Pasco 1726-10G; gid://shopify/Product/7716752490599, Toto ST446EMA#01).
- `templates/product.json` (the default) and `templates/product.pdp-v2.json` both use the `ths-pdp-v2` section, so any product without an image is affected. The comment at the top of the section still says it is used only by the pilot template.
- Line 214 (accessory card, `a.featured_media | image_url: width: 240`) has the same unguarded call. Lines 128 and 262 loop over `product.media` and are safe.

**Fix.** Guard both calls: theme patches 1 and 2 (current line and corrected line are given there). Also add an image to the two products.
**Who:** theme edit; images in Shopify admin.
**Effect:** removes the 404 URL and the broken image. No ranking effect by itself; products without an image are also not eligible for Google's product listings.

---

## 2. Canonical tags

**Found.** The theme emits one canonical tag, in `layout/theme.liquid`: `<link rel="canonical" href="{{ canonical_url }}">`. No SEO snippet or app snippet overrides it; `snippets/social-meta-tags.liquid` uses the same value for `og:url`. `canonical_url` is computed by Shopify.

**Evidence.**
- In the stored HTML of three product pages, two collections and the home page the canonical is the clean, absolute `https://www.thehousesupplier.com/...` URL of the page.
- Across the 968 non-product HTML pages in the crawl, every page is self-canonical except the 113 vendor pages, whose canonical lower-cases the query (`/collections/vendors?q=Rheem` declares `/collections/vendors?q=rheem`).
- `?variant=` and UTM URLs: Shopify's `canonical_url` for a product is the product URL without the query string, so these URLs declare the clean product URL as canonical. This could not be confirmed on the live pages, because Ahrefs requested no parameterised product URL and direct fetches are blocked.
- Why they still appear in Search Console: in the top 500 pages, 188 are product URLs carrying `?variant=...&country=US&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic`. They account for 148 of 360 clicks and 18,886 impressions, mostly at average positions 1 to 7. Those are the link URLs of the Google & YouTube app's product feed: Search Console reports free product listing results under the feed URL, not under the canonical. They are not duplicate pages in the index.
- Paginated collections (`?page=N`) keep their own self-referencing canonical, as intended by the 2026-09-26 theme revision; seven such URLs appear in the Search Console sample.

**Fix.** None for products. Do not block or redirect the `?variant=`/UTM URLs: they are where the free listings land. For the vendor pages, see section 3 (patches 3 and 5).
**Who:** no action; optional check by the owner: open one product URL with `?variant=...&utm_source=google` and view source to confirm the canonical.
**Effect:** none needed.

---

## 3. Missing meta descriptions

**Found.** The issue now holds 114 URLs (104 on 2026-11-09; the crawl has progressed since). None is a product, a collection or a page:
- `/cart` (noindex by design; no description needed);
- 113 vendor listing pages, `/collections/vendors?q=<Vendor>`.

The full list, with internal link counts and the matching brand collection, is in `TECH_missing_meta_descriptions_urls.csv`.

**Why.** `layout/theme.liquid` prints the description only `if page_description` (with a fallback for policy pages). Vendor pages are generated by Shopify and have no description field, so `page_description` is empty. Products, collections and pages are not affected: none of the roughly 16,200 product pages, 773 collections, 26 pages and 46 articles in the crawl is flagged.

**About the Matrixify files.** `TECH_missing_meta_descriptions_matrixify.csv` and its ROLLBACK contain the header row only. A vendor page is not a Shopify object and cannot be given a description by import, so there is no row to write, and writing descriptions for objects that already have one would not address this issue.

**Fix.** Of the 113 vendor pages, 101 have an indexable brand collection, 11 have a brand collection that is itself noindex (empty or hidden), and 1 (RUUD) has none.
1. Theme patch 3: link the brand name on product pages to the brand collection.
2. Theme patch 5: noindex vendor and type listing pages. An alternative that keeps them indexable and gives them a generated description is included in the same patch.
**Who:** theme edit.
**Effect:** clears 113 of the 114 URLs from this issue, moves about 8,950 internal links from duplicate pages to the brand collections, and removes the mixed-case duplicate URLs from Search Console over time.

---

## 4. Links to redirects

**Found.** 820 pages link to 15 redirecting collection URLs. None comes from the menu, the footer or a theme snippet. All are links stored in content:
- **Product descriptions**, in the closing "See also: ..." paragraph (781 product pages);
- **Collection descriptions**, same "See also" paragraph (36 collections);
- **Three pages**: `/pages/catalog-index` (9 old links), `/pages/copper-pipe-dimensions-specs`, `/pages/pvc-cpvc-pipe-dimensions-specs`.

Largest targets: `/collections/tyler-pipe-company` (337 pages), `/collections/rheem-manufacturing` (290), `/collections/dwv` (218), `/collections/no-hub-pipe` (175), `/collections/strut-channel` (71). These are old collection handles that were renamed or merged.

Since 2026-11-11 there is one more, and it is the largest: `/pages/request-a-quote`, linked from every product page by `sections/ths-pdp-v2.liquid` line 201 (16,245 pages).

All 38 source/target pairs, sorted by occurrences, are in `TECH_links_to_redirects.csv` (the first 30 rows are the top 30).

**Evidence.** Ahrefs "page has links to redirect" (820 pages, `links_internal3xx`), plus the stored HTML of two products and one collection, where the old links sit in the description's "See also" paragraph. The attribution of the remaining rows to that paragraph is by pattern, not checked page by page.

**Fix.**
- Theme patch 4 for the quote link.
- A find-and-replace of the 15 old paths in product and collection `Body HTML` (export with Matrixify, replace `/collections/<old>"` with the target in the CSV, import with a rollback file of the original bodies), and a manual edit of the three pages.
- Two targets need a decision first: `/collections/no-hub-pipe` and `/collections/threaded-both-ends-10-lengths` redirect to pipe collections; `/collections/black-iron-pipe` is itself empty and noindex (section 6), so the link should be removed, not repointed.
**Who:** theme edit (quote link); API or Matrixify content update (descriptions); Shopify admin (three pages).
**Effect:** internal links pass straight to the live collection; the issue drops from 820 pages (and 16,245 for the quote link) to zero. Hygiene, with a small benefit for the brand collections that currently receive their links through a redirect (Tyler Pipe, Rheem).

---

## 5. Crawl bloat

**Found.** The 86,706 URLs are not bloat from filters or parameters. The crawl contains none: no filter, sort, search, tag or `/collections/x/products/y` URL, and no `?page=` URL.

| Pattern | URLs in crawl | Note |
|---|---|---|
| Image, CSS and JS files under `/cdn/shop/` | 68,000 to 69,200 | about 79%; product images at several widths |
| Product pages | 16,000 to 16,350 | all self-canonical |
| Collections | 773 | 64 are noindex, including `/collections/all` (section 6) |
| Vendor pages `/collections/vendors?q=` | 114 | indexable duplicates (section 3) |
| Blog articles and blog index | 46 | |
| Pages / policies / home, cart, `/collections` | 26 / 6 / 3 | |
| Redirects, 404, 429 and 503 responses | 26 | 15 collection redirects, 4 host or protocol redirects, 2 x 404, 4 x 429 and 1 x 503 on product pages during the crawl |
| XML sitemaps | 20 | |
| External files (PDF datasheets on cdn.shopify.com, manufacturer sites) | 500 or more | |
| Collection filter URLs (`filter.`), sort (`sort_by`) | 0 | |
| `/collections/x/products/y` | 0 | |
| Pagination `?page=` | 0 | present on the site, not requested by the crawler |
| Search `/search`, tag pages | 0 | |

Ranges are given where the API returns no totals (counted by probing offsets).

**Why there is no parameter bloat.**
- Filters are form checkboxes in `sections/main-collection.liquid`, not links, and sorting is a select; neither produces crawlable `href`s.
- Product cards link to `/products/handle` (83 product links on the stored collection page, none with a collection prefix).
- `templates/robots.txt.liquid` keeps Shopify's default rule groups and adds two rules, `Disallow: /*?quote=` and `Disallow: /*&quote=`. It removes nothing.
- The Search Console sample confirms it from Google's side: no filter, sort, search, tag or collection-prefixed URL among the top 500 pages. The only parameter URLs are the product-feed URLs (section 2) and seven `?page=` URLs.

**What to block or canonicalize.**
- Vendor pages: noindex (patch 5). Do not block them in robots.txt, or Google cannot see the noindex.
- Pagination: leave as is. The theme's own notes record that noindexing page 2+ orphaned 4,385 products in September.
- `?variant=` and UTM URLs: leave alone.
- Filters, sort, search: nothing to add.
- The image share only matters for the Ahrefs crawl budget; image crawling can be switched off in the Ahrefs project settings if the crawl credit is needed elsewhere.

**Who:** theme edit (patch 5) only.
**Effect:** removes the one real family of duplicate listing pages. Not determined: why the crawler requested no `?page=` URL (project setting or robots rule), so the crawl says nothing about how many paginated URLs exist.

---

## 6. Noindex pages in the sitemap

**Found.** Ten collections:

| Collection | Collection ID | Products (all archived) |
|---|---|---|
| `/collections/sewer-drain-pipe` | 297631318119 | 11 |
| `/collections/black-iron-pipe` | 297897787495 | 7 |
| `/collections/threaded-coupled` | 297626861671 | 26 |
| `/collections/type-l-hard` | 297627877479 | 20 |
| `/collections/pvc-dwv-sch40-cellular-core` | 297632071783 | 10 |
| `/collections/type-m-hard` | 297629384807 | 16 |
| `/collections/type-k-hard` | 297633349735 | 8 |
| `/collections/valencia-pipe` | 297568403559 | 47 |
| `/collections/rjb-wholesale` | 297570074727 | 11 |
| `/collections/plain-end-a53` | 297634267239 | 7 |

**Why each is noindex.** The same reason for all ten. They are pipe collections whose products are all ARCHIVED (collections last updated 2026-10-27). On the storefront they show no products, and `layout/theme.liquid` sets `noindex,follow` when `collection.all_products_count == 0`. The collections themselves are still published and do not carry the `seo.hidden` metafield, so Shopify keeps them in `sitemap_collections_1.xml`.

For comparison, the other 54 noindex collections in the crawl are not in the sitemap; the two checked (`in-stock`, `shower-accessories`) carry `seo.hidden = 1`, which is what removes a page from the sitemap.

**Fix.** Either:
- set the metafield `seo.hidden` (integer) to `1` on the ten collections, which removes them from the sitemap (rollback: delete the metafield); or
- if pipe is not coming back, delete or unpublish the collections and redirect each handle to `/collections/pipe-hose-tubing`, as was already done for `/collections/no-hub-pipe`. Note that `/collections/threaded-both-ends-10-lengths` currently redirects to `/collections/black-iron-pipe`, which is one of the ten.
**Who:** API change or Matrixify (metafield), or Shopify admin (redirects).
**Effect:** clears the 10 sitemap errors. Small.

---

## 7. Nofollow internal links

**Found.** 1,055 pages (product pages plus the home page) carry nofollow internal links, from two theme snippets:
- `snippets/ths-bigticket-quote.liquid` line 10: "Get a written quote" links to `/pages/contact-us?quote=<product title and SKU>` with `rel="nofollow"`. This accounts for the product pages (999 of the 1,000 pages sampled), one link per page, on higher-priced items.
- `snippets/ths-home-heating.liquid` line 64: the "Add to cart" links on the home page, `/cart/add?id=...&quantity=1`, with `rel="nofollow"` (7 links). The same pattern is in `snippets/ths-bought-with.liquid` and `snippets/ths-cart-addon-row.liquid`.

**Should they be followed?** No. Both are correct as they are. The quote URLs are one-per-product variations of the contact page and are also disallowed in `robots.txt`; the cart-add URLs are actions, not pages. The related notice "page has nofollow and dofollow incoming links" (460 pages) was not examined.

**Fix.** None. This is a notice, not a problem.
**Who / effect:** no action.

---

## 8. Landing pages for "rheem tankless water heater" and "navien tankless water heater"

**Found (Search Console, 2026-08-11 to 2026-11-10).**

| Query | Impressions | Avg. position | Top URL |
|---|---|---|---|
| navien tankless water heater | 566 | 14.7 | product NHW-SU 199,000 BTU, with `?variant=...utm_medium=product_sync` |
| rheem tankless water heater | 380 | 15.9 | product RTGH 180,000 BTU NG, with `?variant=...utm_medium=product_sync` |

| Collection | Impressions | Avg. position | Clicks | Internal links |
|---|---|---|---|---|
| `/collections/navien-tankless-water-heaters` | 781 | 30.9 | 0 | 11 |
| `/collections/rheem-tankless-water-heaters` | 483 | 23.7 | 0 | 66 |

In this period the home page is the top URL for "rheem tankless propane water heater" and "who sells navien tankless water heaters", not for "rheem tankless water heater" itself; the home-page landing in the brief was not reproduced.

**Why the collection is not the page shown.** Two separate things:
1. The product URLs that "win" are free product listings. They carry the product feed's tracking parameters and sit at positions 1 to 7, which is where Google shows product results. They do not displace the collection; they are a different result type and they bring clicks (section 2). They will keep appearing as top URL whatever is done to the collection.
2. As an ordinary web result the collection ranks on page 3 to 4. The collections themselves are in order: indexable, self-canonical, in the sitemap, 38 and 65 products, specific SEO titles and descriptions. What they lack is links:
   - Neither is in the main menu. The menu links `/collections/navien`, Navien boilers, Navien combi boilers, Navien parts, Rheem 40 and 50 gallon heaters and Rheem tankless parts (17,219 links each) but not the two tankless collections. On the home page the Rheem tankless collection is linked once, through an image with no anchor text; the Navien one not at all.
   - The tankless products do not point to them. `custom.primary_collection` of the Navien NPE-240S2 and of the Rheem RTGH 180 is `tankless-water-heaters-gas`, so the breadcrumb and the "More in ..." block of every Rheem and Navien tankless product link to the generic category.
   - The brand link on each product page goes to `/collections/vendors?q=Rheem` (286 links) and `?q=Navien` (75 links), and the "See also" paragraph of Rheem products links to `/collections/rheem-manufacturing`, a redirect.
   - The site's overall authority is very low (Ahrefs Domain Rating 0.7 per the project brief), so internal links are the main lever available on-site.

**What to change.**
1. Add "Rheem Tankless Water Heaters" and "Navien Tankless Water Heaters" to the Water Heaters part of the main menu and the mobile menu (Shopify admin > Content > Menus). This is the single biggest change: it takes them from 66 and 11 links to site-wide.
2. Link to them with their names as anchor text from `/collections/rheem`, `/collections/navien`, `/collections/tankless-water-heaters` and `/collections/tankless-water-heaters-gas` (collection descriptions), and from the tankless guides (`/blogs/guides/navien-vs-rinnai-tankless-water-heaters`, `/blogs/guides/what-size-tankless-water-heater-do-i-need`, `/blogs/guides/navien-npe-a2-vs-s2`).
3. In the "See also" paragraph of Rheem and Navien tankless products, add the brand tankless collection and replace `/collections/rheem-manufacturing` with `/collections/rheem` (same content update as section 4).
4. Theme patch 3, so the brand name on each product links to `/collections/rheem` and `/collections/navien`.
5. Optional: set `custom.primary_collection` of the Rheem and Navien tankless heaters to the brand tankless collection, so breadcrumbs and the "More in" block point there. Trade-off: the generic gas tankless collection then loses those links, so do this only if the brand queries matter more than "gas tankless water heater".
**Who:** Shopify admin (menus), content update by API or Matrixify (descriptions, metafield), theme edit (patch 3).
**Effect:** the collections should move up for the brand-plus-category queries over the following weeks; given the domain's authority, page one is not a safe expectation from internal links alone. The product-listing URLs will remain in Search Console and should.

---

## Other findings noticed on the way

- **Two Product structured-data blocks on every product page** (one from `snippets/microdata-schema.liquid`, one from `sections/ths-pdp-v2.liquid`). Theme patch 6.
- **Five product pages in the sitemap answered 429 or 503** to the crawler. Most likely rate limiting during the crawl, not a site fault; worth a glance at the next crawl.
- **`/collections/vendors?q=Enviornmental Water Systems`**: the vendor name is misspelled on those products ("Enviornmental").
- The comment at the top of `sections/ths-pdp-v2.liquid` and in `snippets/ths-more-in-collection.liquid` still describes the section as a pilot rendered from `main-product.liquid`; both are out of date.

## What could not be determined

- The rendered `robots.txt` (only the template was read).
- The canonical tag actually served on `?variant=`/UTM URLs (expected from Shopify's behaviour, not observed).
- How many `?page=` URLs exist, and why the crawler requested none.
- How many active products have no image beyond the two the crawl found.
- Exact totals for product pages and image files (ranges given).
- Whether every "See also" link in section 4 sits in the description; three pages were inspected.
