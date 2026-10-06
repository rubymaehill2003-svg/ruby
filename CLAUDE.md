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
