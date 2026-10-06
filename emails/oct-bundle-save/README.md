# Oct · Bundle & Save Diffusers + Refills (Ruby)

Campaign email built from the Figma template **Oct-Refresh-BW- RUBY**
(file `3HcXPTDNPcYm2CohEsdFjm`, node `21416:41`, page "ruby").

| Item | Value |
|---|---|
| Bloomreach campaign | `6ac4b26f8ef045396c51ced8` (project "Valentte Prod", status **draft**) |
| Subject | Bundle & save: reed diffusers from £9.99 each |
| Preheader | Plus diffuser refills from £9.99 – Cardamom & Nutmeg and Lemongrass & Rosemary. |
| Baked images (Figma, page "ruby") | Hero 1 `21423:41`, Hero 2 `21423:43`, Cardamom refill `21423:45`, Lemongrass refill `21423:47` |
| Footer | Zac Footer, verbatim |
| Delivery Pass banners | 3.png → `03846ec0-…png`, 4.png → `fdf4a8dd-…png` on Higgsfield CloudFront; also placed in Figma `21434:41` / `21434:42` |

`oct-bundle-save.html` is byte-identical to the `jinja_html` stored in Bloomreach (checked in both
`design.data` and `split.variants[0].design.data`).

## Prices used (live on valentte.com, 6 Oct 2026)
- Reed diffuser bundle: 1 for £18.99 · 3 for £35.97 (£11.99 each) · 6 for £65.94 (£10.99 each) · 10 for £99.99 (£9.99 each)
- Cardamom & Nutmeg 100ml refill: was £17.99, now £9.99 (44% off)
- Lemongrass & Rosemary 100ml refill: was £17.99, now £10.49 (42% off)

Prices are hard-coded – re-check them on the site before this sends.

## Sections (template order)
1. Header + nav (Offers, Home Fragrance, Best Sellers)
2. Delivery Pass strips: the two real banners from Dropbox `Annual Delivery Pass Banners` (3.png, 4.png), used as-is, linking to https://valentte.com/delivery-membership/ (per the standing rule in `CLAUDE.md`)
3. Two "FREE Gift Alert" banners (Ruby's edit in Bloomreach), each with a white "Claim Your FREE Gift→" button:
   - Claim your FREE Diffuser – code NEWLD – diffuser photo, links to https://valentte.com/reed-diffuser-bundle/
   - Claim your FREE Candle – code FREECANDLE – lit candle photo, links to https://valentte.com/home-fragrance/candles/
4. Offer hero: full-bleed autumn banner (Figma `21446:41`) – headline, subline and Shop & Save button set on the image. Photo of three diffusers generated in Higgsfield (gpt_image_2_5, reference-edit from real Valentte diffuser photos); labels checked by eye and read VALENTTE LONDON correctly
5. Price ladder: The more you buy, the more you save (3 / 6 / 10). the "Buy more save more" photo row is removed (Ruby's request)
6. Review: Lesley, verified 5★ – exact wording from the review export
7. Use case: A different scent for every room – hallway, living room, bedroom, bathroom
8. Refills ("Top up the scents you love…" heading centred, per Ruby's edit in Bloomreach): Cardamom & Nutmeg and Lemongrass & Rosemary with was/now pricing
9. Dark band: Try it risk-free for 90 days
10. You may also like: Offers, Refills, Shop by Scent
11. Zac Footer

## Bloomreach editor clean-up
Ruby's visual-editor edits are kept. The editor clutter is removed: the `__visual-email-editor-body` body class, Grammarly attributes and tag, and the escaped `JINJA_ESCAPE` markers that broke the refer-a-friend link. The canonical Zac Footer is restored.

## Scheduled send – Monday 12 Oct 2026, 07:30 (UK)
Bloomreach scenario **"12/10/26 Newsletter"** (`6ac4d29dc325415410fae343`), built as a copy of the 07/10/26 Newsletter AM branch:
planned trigger 07:30 BST → New/Active/Lapsing/Passive (or clicked in last 180 days; otherwise recently viewed & not purchased) → email has value → not Klaviyo suppressed → email consent → not Weekly/Monthly → no purchase in last 7 days → not in Welcome Flow → New vs Existing split.
- `AM Email 12/10/26 - New Customers` → `send-12-10-new-customers.html` (all valentte.com links carry `?VNCFG=1`, as in the usual New Customers sends)
- `AM Email 12/10/26 - Existing Customers` → `send-12-10-existing-customers.html` (plain links)
- Frequency policy `unlimited-policy`, identity transfer `first_click`, consent category `email`.
Created as a draft – it must be started in the Bloomreach UI to go live.
- Delivery Pass strips are dynamic in both sends, using the same code as the 07/10/26 Newsletter: segmentation **"Annual Delivery Pass Active"** (`6abe3b67548525717f2931b7`, `has_delivery_pass` = true). Yes → "You've got free delivery!" (3.png, links to reed diffusers); No → "Want free delivery?" (4.png, links to /delivery-membership/). Each customer sees one strip only.
