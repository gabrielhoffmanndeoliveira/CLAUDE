# The House Supplier - proposed theme patches

Theme: "THS - Main (zone planner link 22/10)", gid://shopify/OnlineStoreTheme/167456145511, read through the Admin API on 2026-11-11. Nothing here has been applied. Apply on a duplicate of the theme first, check one product with images, one without, and one vendor page, then publish. Rollback for every patch: restore the "current code" shown, or republish the previous theme version.

Line numbers refer to the file as read on 2026-11-11.

---

## Patch 1 - main product image without media (the Liquid error)

**File:** `sections/ths-pdp-v2.liquid`, line 124

**Current code:**

```liquid
      <div class="pv2-main"><img id="pv2-main-img" src="{{ product.featured_media | image_url: width: 1000 }}" alt="{{ product.featured_media.alt | default: product.title | escape }}" width="1000" height="1000"></div>
```

**Proposed code:**

```liquid
      <div class="pv2-main">{%- if product.featured_media -%}<img id="pv2-main-img" src="{{ product.featured_media | image_url: width: 1000 }}" alt="{{ product.featured_media.alt | default: product.title | escape }}" width="1000" height="1000">{%- else -%}{{ 'product-1' | placeholder_svg_tag: 'pv2-ph' }}{%- endif -%}</div>
```

Optional, in the `<style>` block of the same file, so the placeholder fills the box: `.pv2-main .pv2-ph{width:90%;height:90%;fill:#c9c9c9;stroke:none}`

**Reason:** `image_url` raises "invalid url input" when `product.featured_media` is nil. The error text lands in `src`, which crawlers resolve to `/products/Liquid error (sections/ths-pdp-v2 line 124): invalid url input` (404, 2 incoming links). Both linking products are active with zero media. The default template `templates/product.json` uses this section, so any product without an image is affected.

---

## Patch 2 - accessory card image without media (same bug, not yet triggered in the crawl)

**File:** `sections/ths-pdp-v2.liquid`, line 214

**Current code:**

```liquid
        <a class="t" href="{{ a.url }}"><div class="im"><img src="{{ a.featured_media | image_url: width: 240 }}" alt="" loading="lazy"></div>{{ a.title | truncate: 80 }}</a>
```

**Proposed code:**

```liquid
        <a class="t" href="{{ a.url }}"><div class="im">{%- if a.featured_media -%}<img src="{{ a.featured_media | image_url: width: 240 }}" alt="" loading="lazy">{%- endif -%}</div>{{ a.title | truncate: 80 }}</a>
```

**Reason:** the same unguarded `image_url` call. It fails the same way as soon as a product listed in `custom.accessories` or `custom.bought_with` has no image.

---

## Patch 3 - brand link on the product page goes to the brand collection

**File:** `sections/ths-pdp-v2.liquid`, line 135

**Current code:**

```liquid
      <div class="pv2-brand"><a href="/collections/vendors?q={{ product.vendor | url_encode }}">{{ product.vendor }}</a></div>
```

**Proposed code:**

```liquid
      {%- assign pv2_vh = product.vendor | handle -%}
      {%- case pv2_vh -%}
        {%- when 'caleffi' -%}{%- assign pv2_vh = 'caleffi-north-america' -%}
        {%- when 'mrpex-systems' -%}{%- assign pv2_vh = 'mr-pex-systems' -%}
        {%- when 'enviornmental-water-systems' -%}{%- assign pv2_vh = 'environmental-water-systems' -%}
      {%- endcase -%}
      {%- assign pv2_vc = collections[pv2_vh] -%}
      <div class="pv2-brand"><a href="{% if pv2_vc != blank and pv2_vc.all_products_count > 0 %}{{ pv2_vc.url }}{% else %}{{ product.vendor | url_for_vendor }}{% endif %}">{{ product.vendor }}</a></div>
```

**Reason:** every product page links its brand name to `/collections/vendors?q=<Vendor>`. The crawl holds 114 such pages with 8,957 incoming internal links in total; 113 have no meta description, and each duplicates a brand collection that already exists (for example `vendors?q=Rheem`, 286 links, against `/collections/rheem`). `snippets/product-item.liquid` (line 195) and `snippets/product-meta.liquid` already use the brand collection when one exists; the new product section does not. The three `when` lines cover brands whose collection handle differs from the vendor name (verified in Shopify: `caleffi-north-america`, `mr-pex-systems`, `environmental-water-systems`). "RUUD" has no brand collection and keeps the vendor URL. Test note: check that a vendor whose collection is unpublished or empty falls back to the vendor URL.

---

## Patch 4 - "Request a quote" link points straight at the contact page

**File:** `sections/ths-pdp-v2.liquid`, line 201

**Current code:**

```liquid
          <a href="/pages/request-a-quote"><svg viewBox="0 0 24 24"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/></svg>Request a quote</a>
```

**Proposed code:**

```liquid
          <a href="/pages/contact-us?quote={{ v.sku | default: product.title | url_encode }}" rel="nofollow"><svg viewBox="0 0 24 24"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/></svg>Request a quote</a>
```

Simpler variant if the prefilled reference is not wanted: `href="/pages/contact-us"` (and no `rel`).

**Reason:** this is the link behind "16,245 pages link to a broken page". The page does not exist; since 2026-11-11 a redirect sends it to `/pages/contact-us`, so every product page now carries a link to a redirect. The `?quote=` form matches what `snippets/ths-bigticket-quote.liquid` already does, and `templates/robots.txt.liquid` already disallows `?quote=` URLs, so `rel="nofollow"` is consistent there. Keep the redirect in place after the edit (external links and cached pages still use the old URL).

---

## Patch 5 - noindex vendor and product-type listing pages

**File:** `layout/theme.liquid`, inside the `{%- liquid ... -%}` block that sets `seo_noindex`

**Current code:**

```liquid
      # Internal search result pages hold no standalone search value.
      if request.page_type == 'search'
        assign seo_noindex = true
      endif
```

**Proposed code:**

```liquid
      # Internal search result pages hold no standalone search value.
      if request.page_type == 'search'
        assign seo_noindex = true
      endif

      # Automatic vendor / product-type listings (/collections/vendors?q=, /collections/types?q=).
      # Each duplicates a brand or category collection and cannot be given its own content.
      if request.path == '/collections/vendors' or request.path == '/collections/types'
        assign seo_noindex = true
      endif
```

**Reason:** these pages are generated by Shopify, have no description field, and compete with the brand collections. Their canonical tag lower-cases the query (`?q=Rheem` declares `?q=rheem`), so both spellings show up in Search Console. With patch 3 they lose almost all internal links; noindex stops the remainder from being indexed. This also closes 113 of the 114 "meta description missing" URLs. Apply after patch 3, not before. Test note: confirm on a vendor page that the page source contains `<meta name="robots" content="noindex,follow">`; if `request.path` does not match in this theme, use `collection.handle == 'vendors' or collection.handle == 'types'` instead.

**Alternative, if the owner prefers to keep vendor pages indexable:** leave the noindex out and add a description fallback after the `policy` branch of the meta description block:

```liquid
    {%- elsif request.path == '/collections/vendors' and collection.title != blank -%}
      <meta name="description" content="{{ collection.title | escape }} products at {{ shop.name | escape }}: plumbing, heating and HVAC supplies and repair parts, listed with part numbers and specifications.">
```

---

## Patch 6 (lower priority) - one Product structured-data block per product page

**File:** `sections/ths-pdp-v2.liquid`, lines 253-274

**Current code:** the whole block from `<script type="application/ld+json">` (line 253, `"@type": "Product"`) to its closing `</script>` (line 274).

**Proposed code:** delete those lines.

**Reason:** `snippets/microdata-schema.liquid` (rendered from `layout/theme.liquid`) already outputs the complete Product block with `@id`, `url`, `category`, `gtin` and the return policy. The section adds a second, thinner Product block without `@id`, so the crawled product pages carry two Product entities (checked on two crawled pages). Today both show the same price and availability, but they are computed by different code (the section uses its own in-stock / backorder logic), so they can drift apart and give Google conflicting offers. Before deleting, confirm in Google's Rich Results Test that the remaining block still reports the BackOrder state the section used; if not, move that logic into the snippet instead.

---

## Not a theme change, listed here so it is not attempted in the theme

- `templates/robots.txt.liquid`: no change recommended. It keeps Shopify's default rules and adds `Disallow: /*?quote=` and `Disallow: /*&quote=`. Do not add rules for `?variant=` or `utm_` URLs: Google's free product listings land on those URLs and they earned 148 of the 360 clicks in the Search Console sample.
- `layout/theme.liquid` canonical tag (`<link rel="canonical" href="{{ canonical_url }}">`): no change recommended.
