# Post Purchase – First Time Purchasers · Day 20 – autumn version (Ruby)

Autumn re-theme of Day 20 ("Your Home Called... 🏡") from scenario "Post Purchase - First Time Purchasers (Update: 17/07)"
(`6a5a1df118246cc0f537b328`, nodes 279 Path A / 414 Path B – identical designs). The live flow was **not** changed.

- Hero "One scent is never enough" rebuilt with an autumn interior (Higgsfield mood photo, no product/text) + real Spiced Orange product photo.
- Four summer scent blocks (Lemongrass & Rosemary, Citrus Grove, Wild Mint & Sicilian Lemon, White Neroli & Lemon) replaced by three:
  - "Crisp, calm & cosy" – Snow & Sage → `/shop-by-scent/snow-sage/`
  - "Warmth in every room" – Spiced Orange → `/shop-by-scent/spiced-orange/`
  - "A festive twist" – Crushed Candy Cane → `/shop-by-scent/crushed-candy-cane/`
- Blocks built in Figma (frames `21847:199`, `21847:206`, `21847:214`, `21847:222`, page "ruby") with real catalogue product photos and Higgsfield polaroid mood photos.
- Both `jinja_html` and the Beefree editor template were updated, so the email still opens in the drag-and-drop editor.

## Bloomreach test
Scenario "Ruby test automation" `6ac8d937c02bc4fb6b7985e0`: node 3 "TEST – Day 20 (Path A) – Autumn", node 6 "TEST – Day 20 (Path B) – Autumn",
each trigger → "Ruby" condition → email. Unlimited Policy, Transfer identity First click (verified).
