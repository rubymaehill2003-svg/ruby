# PPF-01 · Thank You For Your Order (Ruby)

Post-purchase email 1, built from the Figma wireframe **PPF-01-BW- RUBY**
(file `3HcXPTDNPcYm2CohEsdFjm`, node `21102:88`, page "Valentte PPF").

| Item | Value |
|---|---|
| Bloomreach campaign | `6ac3bbc809601ba2fb2ed8f7` (project "Valentte Prod", status **draft**) |
| Subject | Thank you – your order is in good hands |
| Preheader | Here’s a little look at how your order comes together, from our Cheshire workshop to your door. |
| Hero banner (Figma) | node `21391:17` "PPF-01-RUBY · Hero (600w)", next to the wireframe |
| Footer | Zac Footer, verbatim |

`ppf-01-thank-you.html` is byte-identical to the `jinja_html` stored in Bloomreach
(checked after creation in both `design.data` and `split.variants[0].design.data`).

## Sections
1. Header: VALENTTE wordmark + nav (Offers, Home Fragrance, Gift Sets, Best Sellers)
2. Hero: baked-text image (Figma, wave-cut bottom) – "Thank you for your order"
3. Intro: null-safe greeting, order-confirmed copy, signed Justina & Luke → Shop Best Sellers
4. "Handmade in Cheshire, hand wrapped with care": wide image + 3-step timeline → Shop Gift Sets
5. Dark story block: "From a kitchen table to over 1 million homes" → Read Our Story
6. "A few tips before your order arrives": reed diffusers / candles / placement → Shop Home Fragrance
7. You may also like: Gifting, Refills, Offers
8. Zac Footer

All copy uses approved wording from the Valentte USPs & Key Messaging and Product Knowledge sources.
Photos are real Valentte photography from the approved Dropbox folders (no AI generation in this build),
hosted on Higgsfield/CloudFront.
