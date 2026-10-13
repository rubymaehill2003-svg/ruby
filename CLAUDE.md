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
5. The API read-back is also unreliable for this field: after Ruby switches it to First click in the Bloomreach UI, the API
   can still report `disabled` (seen 9 Oct 2026 on six campaigns). Once Ruby confirms she has switched it in the UI,
   treat that email as done – don't keep re-flagging it.

## Subject lines & preview text (permanent rule)

For every email (campaigns, scenario/flow emails, A/B variants):

- **Sentence case** for both the subject line and the preview text (preheader) – capitalise only the first word and
  proper nouns/product names (e.g. "Lemongrass & Rosemary"), never Title Case.
- The word **free** is always written in caps: **FREE** (in subject lines and preview text).
- Every subject line includes **one relevant emoji**.
- The preview text must **not repeat** what the subject line already says – it should add something new.
- Across subject + preview, aim for a **mix of offer-driven and curiosity-led** copy (e.g. one carries the offer, the
  other teases/intrigues).
- Check this on every create/update before uploading to Bloomreach.

## Dark Mode compatibility (permanent rule)

Every email must keep its intended Light Mode appearance in Dark Mode (desktop and mobile) as closely as each email
client allows – Dark Mode must not change, invert or distort the design.

- Text colours, background colours and brand colours stay the same as the Light Mode design wherever supported.
- Images, logos, banners and product imagery keep their original colours (no inversion, no transparent-background
  logos/text that disappear on dark backgrounds – give them a solid background baked into the image).
- Buttons/CTAs keep their intended fill and text colours and contrast; no text may become invisible or hard to read.

How to apply it in the HTML (check on every build/update):
1. `<meta name="color-scheme" content="light only">` and `<meta name="supported-color-schemes" content="light only">`,
   plus `:root { color-scheme: light only; supported-color-schemes: light only; }` in the `<style>` block.
2. Set explicit `bgcolor` attributes **and** inline `background-color` on body, wrapper tables and every coloured cell;
   set an explicit inline `color` on every text element (never rely on defaults).
3. Outlook.com/Office 365 overrides: add `[data-ogsc]` (text) and `[data-ogsb]` (background) rules that re-assert the
   light colours for key classes (body, text, buttons).
4. Text-heavy sections that must never invert (e.g. hero headlines, offer badges) are baked into images, as already done
   for sliced sections; any PNG with transparency must be flattened onto its intended background colour.
5. Bulletproof buttons: background colour set on the `<td>` (bgcolor + inline style) and the `<a>`, with explicit text colour.
6. Known limits to tell Ruby about when relevant: Gmail iOS/Android apps and Outlook apps can still force partial or full
   colour inversion that no code can fully prevent – images are never inverted, so keep critical text inside images.
