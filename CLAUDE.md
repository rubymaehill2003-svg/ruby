# Valentte email rules (permanent)

## Every email MUST include all three of these – no exceptions

Applies to every Valentte email built or edited: campaigns, newsletters, scenario/flow emails, templates and Figma email frames.

1. **Topper (header)** – the VALENTTE / LONDON logo row linking to https://valentte.com/, followed by the nav row (Offers → /sale/, Home Fragrance → /home-fragrance/natural-reed-diffusers/, Best Sellers → /best-sellers/). Never remove the header logo row, even if the hero image also has a logo – remove the logo from the hero instead.
2. **Delivery pass banner** – directly under the topper, using the dynamic segmentation block (segmentation "Annual Delivery Pass Active", id `6abe3b67548525717f2931b7`):

```
{% if  segmentations['6abe3b67548525717f2931b7'] == 'Yes'  %}
  <tr><td style="padding:0 0 10px;font-size:0;line-height:0;"><a href="https://valentte.com/home-fragrance/natural-reed-diffusers/" target="_blank" style="display:block;text-decoration:none;"><img src="https://d2ol7oe51mr4n9.cloudfront.net/user_3J5VVo50uL70F327Y6AS8CqWwV6/03846ec0-1121-4b6e-b4d4-08d5ebad812b.png" width="600" height="60" alt="You’ve got free delivery! Your Unlimited Delivery Pass is live." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>
{% endif %}
{% if  segmentations['6abe3b67548525717f2931b7'] == 'No'  %}
  <tr><td style="padding:0 0 10px;font-size:0;line-height:0;"><a href="https://valentte.com/delivery-membership/" target="_blank" style="display:block;text-decoration:none;"><img src="https://d2ol7oe51mr4n9.cloudfront.net/user_3J5VVo50uL70F327Y6AS8CqWwV6/fdf4a8dd-98c3-4d71-8452-4d06f079e2c7.png" width="600" height="60" alt="Want free delivery? Get it all year with our Unlimited Delivery Pass." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>
{% endif %}
```

3. **Footer** – the standard sliced Valentte footer ("FOOTER: Top5 #7 Higgsfield background"): refer-a-friend, secure checkout/payment icons, phone + email, Facebook/TikTok/Instagram, contact preferences + unsubscribe (`{{ email.unsubscribe }}`), not-monitored note, address, View in Browser (`{{ email.view }}`). Reference copy: the 16/10/26 Newsletter PM email (scenario `6acdd02e1842e1f9598199e6`, node 35).

Before finishing any email, check all three are present (logo row + nav, both delivery pass `{% if %}` blocks, footer with unsubscribe) and say so in the summary.

## Logo: always use the "Aiden logo"

Whenever an email needs the logo (header/topper logo row, or anywhere else a logo appears), use the **Aiden logo** – Figma frame **"Aiden Header"** (node `22470:6`, page "Valentte PPF", file `3HcXPTDNPcYm2CohEsdFjm`). Clone that frame; don't rebuild or swap in another logo.

- Spec: 600 × 86 white frame, vertical auto-layout, centred, padding 26 top / 14 bottom, 2px gap.
- "VALENTTE" – Constantia Regular 26px, letter-spacing 2px, `#212121`.
- "LONDON" – Constantia Regular 10px, letter-spacing 0, `#595959`.
- HTML equivalent (links to https://valentte.com/ with `display:block`): same text and sizes, `font-family:Constantia,Georgia,'Times New Roman',serif`.
