# Wed 14/10/26 AM – "Autumn, bottled" (Template 14)

Bloomreach scenario **"14/10/26 Newsletter"** (`6ac4f820c40bce1256cba680`, draft) – AM branch copied from the 13/10 AM branch:
planned trigger **Wed 14 Oct 2026, 07:30 UK** → New/Active/Lapsing/Passive (or recently viewed) → email has value → not Klaviyo
suppressed → email consent → not weekly/monthly → no purchase 7 days → not in Welcome Flow → New & Existing split.
- `AM Email 14/10/26 - New Customers` (node 1456) → `am-14-10-new-customers.html` – all valentte.com links `?VNCFG=1`
  (except refer-a-friend), FREE Gift banner = NEWLD diffuser.
- `AM Email 14/10/26 - Existing Customers` (node 1457) → `am-14-10-existing-customers.html` – plain links, FREE Gift banner = FREECANDLE.
- Both: dynamic Delivery Pass strips (segmentation "Annual Delivery Pass Active": Yes = 3.png, No = 4.png), Zac Footer with plain
  `https://valentte.com/refer-a-friend/`.
- Subject: "Autumn, bottled: Citrus Grove & Sea Salt 🍂" · Preheader: "Citrus Grove Gift Box and Sea Salt 100ml Refill – two scents for crisp autumn days."

Template 14 (Figma page "ruby", node 21476:1725) mapped as:
2×2 image grid with wave edge → "WEDNESDAY'S PICKS / AUTUMN, BOTTLED" banner + CTA → cream wave section "TODAY'S OFFERS" with
four callouts around the central image (two product halves, each linked) → Body 1 as the review section (3 exact verified 5★ reviews)
→ icons row as approved social proof (1 sold every 18 seconds / Over 1 million happy customers / 350,000+ five-star reviews).

Imagery (Higgsfield gpt_image_2_5, medium/2k, 5 credits): reference-edits of the real Citrus Grove gift box and Sea Salt refill
product photos (labels checked by eye – all read "VALENTTE LONDON"; the room-mist small print reads "30ml ℮ 1.0fl.oz" vs the real
"30ml e 1 fl. oz", illegible at email size) + three blank-slate autumn mood shots (no product/text).

Prices (live, 6 Oct 2026 – neither product currently discounted): Original Diffuser Gift Box – Citrus Grove £26.49;
100ml Diffuser Refill – Sea Salt £17.99. No /shop-by-scent/citrus-grove/ page exists (404) so the citrus tile links to the gift box.
All links checked live (200).

Figma (page "ruby"): editable frames "Wed 14/10 AM · EDITABLE – New Customers" (21515:221) and
"Wed 14/10 AM · EDITABLE – Existing Customers" (21515:309), placed to the right of Template 14. Live text + auto layout;
header, Delivery Pass strip, FREE Gift banner and Zac Footer cloned from the Tue 13/10 PM editable frames.
Fully editable pass (7 Oct): grid photos are clean images with a separate white vector wave on top; the two wave strips are
vector shapes; each offer image is a background photo + rounded product photo layer (drop shadow); the Zac Footer is rebuilt
with live text, and only the icons / payment logos / social icons remain as crops of the real footer image (never redrawn).
The Delivery Pass strips stay as the real Dropbox banner images (permanent rule).

## Update 7 Oct – bundle-led version (Ruby's Figma edits)
Both emails now match the edited New Customers Figma frame (Existing frame rebuilt from it, id 21599:182):
- FREE Gift banners replaced with Ruby's Dropbox banners (used as-is): **New = BannersC0_52.png (code NEWLD)** → /reed-diffuser-bundle/;
  **Existing = BannersC0_43.png (code FREEDIFF)** → /home-fragrance/natural-reed-diffusers/.
- Grid: 3-diffuser bundle shot ("UP TO 47% OFF" roundel) + Higgsfield room scenes of the real Sea Salt reed diffuser
  (living room, bathroom, hallway – labels checked), Shop Now pill on every tile.
- Banner "Bundle & Save 47% / AUTUMN, BOTTLED / Choose from our best-selling scents…" + SHOP THE OFFER NOW → bundle.
- "WEDNESDAY'S PICKS": gift box £26.49 → £18.99 (28% roundel), Sea Salt refill £17.99 → £10.49 (42% roundel) – live prices 7 Oct.
- "Natural scents for your whole home / Reed Diffuser Bundle Offer" reviews: the two draft quotes weren't in the review export, so
  replaced with genuine verified 5★ reviews (Elaine F. and Ryan, Ready, Set, Scent Pack). CTA "Buy your Bundle Here →".
- Stats: 47% OFF / 350k+ / 20+ Scents to choose. Subject: "Bundle & save up to 47% on reed diffusers 🍂".
