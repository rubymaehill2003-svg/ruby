# Valentte email production – Ruby's standing rules

These apply on top of the `valentte-email-production` skill.

## Delivery Pass strips (permanent rule)

Whenever a reference email has strip headlines at the top that mention the **Delivery Pass**
(e.g. "You've got free delivery! Your Unlimited Delivery Pass is live." /
"Want free delivery? Get it all year with our Unlimited Delivery Pass."):

- Use the **two real banner images** from Dropbox, as-is, as the two strips:
  `/Valentte's shared workspace/Email Marketing/2026 Email Marketing/Annual Delivery Pass Banners`
- Do **not** rebuild those strips as black-and-white wireframe blocks, and do not rewrite them
  as live HTML or new copy – drop the two images in directly, in place of both strips.
- This applies to B&W templates in Figma and to the built emails made from them.

## FREE Gift banners – new vs existing customers (permanent rule)

When an email is sent as separate **New Customers** and **Existing Customers** versions (e.g. the
New & Existing Customer Split in the daily newsletter scenarios):

- The FREE Gift banner whose discount code contains **"NEW"** (e.g. `NEWLD`) goes **only** in the
  **New Customers** version.
- The other FREE Gift banner (the code without "NEW", e.g. `FREECANDLE`) goes **only** in the
  **Existing Customers** version.
- Never show both FREE Gift banners in the same version.

## Frequency policy (permanent rule)

Every email uploaded into Bloomreach – in any scenario (newsletters, test scenarios, flows) or as an email campaign – must
have **Unlimited Policy** selected as its frequency policy (`frequency_policy: "unlimited-policy"` on the send-email node).
Check it on every create/update, and re-check after any copy or clone.

## Transfer identity = First click (permanent rule)

Every email created or updated in Bloomreach Engagement for Ruby (Valentte Prod project) – standalone email campaigns
**and** every send-email step inside scenarios/flows – must have **Transfer identity** set to **First click**
(API field `transfer_user_identity: "first_click"`), never Disabled.

1. Always include `"transfer_user_identity": "first_click"` in the payload on every create/update.
2. After every upload, re-fetch the email and check what the setting actually reads.
3. Known limitation (tested 9 Oct 2026): the API accepts this field but often doesn't save it, so it may still read
   `disabled`. When that happens, tell Ruby the email's name and remind her to switch "Transfer identity" to
   "First click" in that email's settings in Bloomreach before it sends. Never report an email as finished without
   that reminder.
4. Don't change any other emails just to apply this rule.
