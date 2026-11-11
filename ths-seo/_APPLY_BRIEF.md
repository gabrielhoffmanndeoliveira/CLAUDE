# Brief: review and apply a THS SEO batch

Store: The House Supplier (thehousesupplier.com), Shopify. The owner has approved applying this content. You review one batch of draft files in /home/user/CLAUDE/ths-seo/, fix what is wrong, and apply what passes through the Shopify Admin API. You did not write these drafts; read them critically.

Tools: load with ToolSearch, query "select:mcp__Shopify__graphql_query,mcp__Shopify__graphql_mutation,mcp__Shopify__graphql_schema". Before your first mutation, check its arguments with graphql_schema (operation "mutation", field_name). Known to work: collectionUpdate(collection: { id, descriptionHtml, seo { title, description } }) { collection { id } userErrors { field message } }. For products use productUpdate; confirm the argument name and input type first. Do not run git. Do not touch prices, inventory, tags, themes, discounts or anything outside the fields named in your task. Do not include customer data anywhere.

## Step 1 - Save a true rollback first
Fetch the live current values for every item in the batch and write them to <import file name>_ROLLBACK_live.csv (same columns as the import file) with Python's csv module (QUOTE_ALL, UTF-8). The values must come from the API byte for byte, not retyped: query 10-25 items per call so the result is large enough to be saved to a tool-results file, then parse that file with a script. If a result comes back inline, query more items per call. Do not apply anything until this file exists and has every item.

## Step 2 - Review each row; fix or drop
Drop a row (do not apply it) when you cannot make it pass. Rules:
- No claims about price, discounts, stock, delivery time, free shipping, warranty length, "authorized dealer", or "ships from". Remove such sentences.
- No invented or unverifiable specs. Every number in new text (capacity, BTU, UEF, flow, voltage, dimensions, pressure, temperature) must match the product title or the product's custom.specifications metafield, or be backed by a manufacturer source named in the batch's REVIEW file. If the REVIEW file marks a claim "PRIORITY:" or unconfirmed and that claim appears in the text, remove the claim; if the text cannot stand without it, drop the row.
- Discontinued products must not be described as current.
- HTML must be well formed (balanced tags, no script or style, no inline event handlers). Internal links must point to handles that exist (verify collections and products with a query).
- SEO titles 60 characters max; meta descriptions 155 max; neither may contradict the body.
- For products: every block that existed in the live description after the intro (sections headed Full Specifications, Specifications, Documents & Downloads, Documents, Compatible Accessories, "See also" links, a ths-mfr-data wrapper, regulatory notes such as a California NOx note) must still be present, unchanged, in the new description. Compare against the live value from Step 1, not against the draft rollback.
- If the live value has changed since the draft was written (the draft's rollback differs from live), rebuild the row on top of the live value or drop it.
- Plain, correct US English. Remove filler and repeated sentences.
Write the reviewed rows to <import file name>_REVIEWED.csv and a log to <import file name>_APPLY_LOG.csv with columns: ID, Handle, Decision (applied / fixed and applied / dropped), What was changed in review, Reason if dropped.

## Step 3 - Apply
Each mutation call makes the store owner confirm on screen, so use as few calls as possible: put 10-15 items in each mutation call, using aliases. Check userErrors on every call.

## Step 4 - Verify
Fetch the items again (large batches, so the result is saved to a file) and compare with the REVIEWED file by script. Shopify may normalize HTML slightly (entities, whitespace); treat that as a match, but any missing section or truncated text is a failure: re-apply that item and check again. Record the final state in the log.

## Report (short)
Counts applied, fixed, dropped; the reasons for drops; anything the owner must decide. Save your work to disk as you go so an interruption does not lose it; if your output files already exist, continue from them.
