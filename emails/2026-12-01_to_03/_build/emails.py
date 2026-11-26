import json, os, re
S = '/tmp/claude-0/-home-user-ruby/b44f2fb9-6eed-5680-a384-23171670d6e5/scratchpad'
OUT = '/home/user/ruby/emails/2026-12-01_to_03'
os.makedirs(OUT, exist_ok=True)
U = json.load(open(f'{S}/urlmap.json'))
def img(k): return U[f'vt1203_{k}.jpg']

FOOTER_SRC = '/root/.claude/skills/synced/a6d424fb-5c76-4f79-9bd0-bbf98096c2c2_67c8da26-da79-40cd-aaaf-352ec76d15d5/valentte-email-production/references/zac-footer.html'
lines = open(FOOTER_SRC).read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('<!-- YOU MAY ALSO LIKE'))
FOOTER = '\n'.join(lines[start:]).strip()
for f in ('email', 'first_name', 'last_name'):  # Jinja null-safety
    FOOTER = FOOTER.replace('{{ customer.%s }}' % f, "{{ (customer.%s or '') }}" % f)

BUNDLE = 'https://valentte.com/reed-diffuser-bundle/'
HOME = 'https://valentte.com/'
DAYS = {
 1: dict(date='01/12/26', dow='Tuesday', item='candle', code='FREEFLAME',
         box=('Jasmine &amp; Rosewood', 'https://valentte.com/organic/best-selling-gift-box-jasmine-rosewood/'),
         tiles=[('Cardamom &amp; Nutmeg 100ml Diffuser Refill', 'https://valentte.com/organic/cardamom-and-nutmeg-100ml-diffuser-refill/', '9.99', '17.99', 44, 'tile_refill_cardamom'),
                ('Lemongrass &amp; Rosemary 100ml Diffuser Refill', 'https://valentte.com/organic/lemongrass-and-rosemary-100ml-diffuser-refill/', '10.49', '17.99', 42, 'tile_refill_lemongrass'),
                ('Customer Favourites Mini Mist Box of 4', 'https://valentte.com/organic/customer-favourites-mini-mist-box-of-4/', '7.99', '13.49', 41, 'tile_minimist')]),
 2: dict(date='02/12/26', dow='Wednesday', item='boxed diffuser', code='FREEDIFF',
         box=('Pure Lavender', 'https://valentte.com/organic/best-selling-gift-box-pure-lavender/'),
         tiles=[('White Neroli &amp; Lemon 100ml Diffuser Refill', 'https://valentte.com/organic/white-neroli-and-lemon-100ml-diffuser-refill/', '10.49', '17.99', 42, 'tile_refill_neroli'),
                ('Wild Mint &amp; Sicilian Lemon 100ml Diffuser Refill', 'https://valentte.com/organic/100ml-diffuser-refill-wild-mint-sicilian-lemon/', '9.49', '17.99', 47, 'tile_refill_wildmint'),
                ('Customer Favourites Mini Mist Box of 4', 'https://valentte.com/organic/customer-favourites-mini-mist-box-of-4/', '7.99', '13.49', 41, 'tile_minimist')]),
 3: dict(date='03/12/26', dow='Thursday', item='candle', code='FREEFLAME',
         box=('Cardamom &amp; Nutmeg', 'https://valentte.com/organic/best-selling-gift-box-cardamom-nutmeg/'),
         tiles=[('Pure Lavender 100ml Diffuser Refill', 'https://valentte.com/organic/lavender-refill-100ml-diffuser-refill/', '9.99', '17.99', 44, 'tile_refill_lavender'),
                ('Bergamot &amp; Lemon 100ml Diffuser Refill', 'https://valentte.com/organic/bergamot-and-lemon-100ml-diffuser-refill/', '10.49', '17.99', 42, 'tile_refill_bergamot'),
                ('Customer Favourites Mini Mist Box of 4', 'https://valentte.com/organic/customer-favourites-mini-mist-box-of-4/', '7.99', '13.49', 41, 'tile_minimist')]),
}
COPY = {  # subject (title test A), subject (title test B), preheader
 (1,'AM'): ('Day 1 of 12: a FREE candle is yours 🎄', 'The 12 Days of Christmas start now ✨', 'Use code FREEFLAME today – plus Christmas gift boxes now £23.99.'),
 (1,'PM'): ('Final hours: your FREE candle 🕯️', 'One for every room – diffusers from £9.99', 'Code FREEFLAME is today only – plus save up to £89.91 on bundles.'),
 (2,'AM'): ('Day 2 of 12: a FREE diffuser with every order 🎁', '“What’s that beautiful smell?”', 'Use code FREEDIFF today. Pure Lavender gift box now £23.99.'),
 (2,'PM'): ('Last call for your FREE diffuser ✨', 'The more rooms, the merrier 🎄', 'Code FREEDIFF is today only – plus diffusers from £9.99 when you bundle.'),
 (3,'AM'): ('Day 3 of 12: FREE candle unlocked 🎄', 'The Christmas host’s secret…', 'Use code FREEFLAME today – plus the Cardamom &amp; Nutmeg gift box for £23.99.'),
 (3,'PM'): ('Final hours for your FREE candle 🕯️', 'It smells designer. It isn’t priced like it.', 'Use code FREEFLAME today – plus bundles from £9.99 each.'),
}
HERO_ALT = {
 (1,'AM','A'): 'Christmas scent for every room, from £9.99 – bundle 10 reed diffusers and save £89.91. Build my bundle',
 (1,'AM','B'): 'It starts the moment they walk in… Guests notice the second they walk in. See how',
 (1,'AM','C'): 'Door No. 1 is ready to open – tap to open today’s door, every door hides a festive treat. Open door 1',
 (1,'PM','A'): 'One for every room. Save up to £89.91 – reed diffusers from £9.99 each when you bundle, plus a FREE candle with code FREEFLAME. Shop bundles',
 (1,'PM','B'): 'The house everyone talks about this Christmas. Strong, never overpowering. Discover more',
 (1,'PM','C'): 'Pull the cracker… what’s inside? Every cracker holds a prize. Pull to reveal',
 (2,'AM','A'): 'Fill every room for Christmas, from £9.99 – save £89.91 on 10 diffusers, plus a FREE boxed diffuser with code FREEDIFF. Build my bundle',
 (2,'AM','B'): 'What’s that beautiful smell? The question every guest asks. Find your scent',
 (2,'AM','C'): 'Give it a shake… a gift is hiding in the snow. Shake to reveal',
 (2,'PM','A'): 'The more rooms, the merrier – save £21 on 3, £48 on 6, £89.91 on 10 diffusers. Pick my pack',
 (2,'PM','B'): 'Christmas in every room, all day long – our diffusers work 24/7. Shop diffusers',
 (2,'PM','C'): 'Scratch to reveal your treat – every card wins. Scratch now',
 (3,'AM','A'): 'The Christmas host’s secret: £9.99 diffusers – save £89.91 on 10, plus a FREE candle with code FREEFLAME. Build my bundle',
 (3,'AM','B'): 'The scent that greets you before you’ve even taken your coat off. Discover more',
 (3,'AM','C'): 'Three presents. One is yours – every present hides a festive treat. Pick my present',
 (3,'PM','A'): 'Last call: FREE candle + diffusers from £9.99. Shop bundles',
 (3,'PM','B'): 'It smells designer. It isn’t priced like it. See for yourself',
 (3,'PM','C'): 'Give Christmas a spin – every slice is a winner. Spin now',
}

def a(href, inner, extra=''):
    return f'<a href="{href}" target="_blank" style="display:block;text-decoration:none;{extra}">{inner}</a>'
def imgrow(src, href, alt, bg='#ffffff'):
    return (f'<tr><td style="padding:0;font-size:0;line-height:0;background:{bg};">'
            + a(href, f'<img src="{src}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;">')
            + '</td></tr>')

def tiles(day):
    cells = ''
    for name, url, now, was, pct, k in DAYS[day]['tiles']:
        cells += f'''<td class="stack-col" width="33%" valign="top" style="width:33.33%;padding:0 6px;">
{a(url, f'<img src="{img(k)}" width="176" alt="{name} – now £{now}" style="display:block;width:100%;max-width:176px;height:auto;border:0;margin:0 auto;border-radius:4px;">')}
<div style="font-family:Inter,Arial,sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;color:#8C1D24;padding:10px 0 4px;">SAVE {pct}%</div>
<div style="font-family:Cardo,Georgia,serif;font-size:16px;line-height:20px;color:#212121;min-height:40px;">{name}</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:14px;color:#212121;padding:6px 0 10px;"><b>£{now}</b> <span style="color:#8a8a8a;text-decoration:line-through;">£{was}</span></div>
{a(url, '<span style="display:inline-block;font-family:Inter,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:1.2px;color:#212121;background:#FFA220;border-radius:30px;padding:10px 18px;">SHOP NOW</span>')}
</td>'''
    return f'''<tr><td align="center" style="padding:34px 18px 30px;background:#F7F5F2;">
<div style="font-family:Inter,Arial,sans-serif;font-size:11px;font-weight:600;letter-spacing:3px;color:#B8913F;">✦ ALSO ON OFFER TODAY ✦</div>
<div style="font-family:Cardo,Georgia,serif;font-size:28px;line-height:34px;color:#212121;padding:6px 0 20px;">More festive savings</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>'''

PROOF = '''<tr><td align="center" style="padding:30px 30px 28px;background:#1E3A2B;">
<div style="font-family:Inter,Arial,sans-serif;font-size:18px;letter-spacing:4px;color:#E2C27A;">★★★★★</div>
<div style="font-family:Cardo,Georgia,serif;font-size:26px;line-height:32px;color:#ffffff;padding:8px 0 6px;">Everyone who visits asks what it is.</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:13px;line-height:20px;color:rgba(255,255,255,.82);">350,000+ five-star reviews &nbsp;·&nbsp; Over 1 million happy customers &nbsp;·&nbsp; 1 sold every 18 seconds</div>
</td></tr>'''

def reminder(day, slot):
    d = DAYS[day]
    when = 'Today only' if slot == 'AM' else 'Final hours today'
    return f'''<tr><td align="center" style="padding:26px 30px 8px;background:#ffffff;">
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border:1.5px dashed #B8913F;border-radius:8px;background:#F4EDE3;"><tr><td align="center" style="padding:18px 26px;">
<div style="font-family:Inter,Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:2.5px;color:#8C1D24;">✦ DON’T FORGET · {when.upper()} ✦</div>
<div style="font-family:Cardo,Georgia,serif;font-size:22px;line-height:28px;color:#212121;padding:6px 0 4px;">A FREE {d['item']} with every order</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:14px;color:#444444;">Use code <b style="letter-spacing:1.5px;color:#B8913F;">{d['code']}</b> at checkout.</div>
</td></tr></table></td></tr>'''

HEADER = '''<!-- HEADER: Aiden Header (image, default from 04/11/26) -->
<tr><td align="center" style="padding:0;font-size:0;line-height:0;"><a href="https://valentte.com/" target="_blank" style="display:block;text-decoration:none;"><img src="https://d2ol7oe51mr4n9.cloudfront.net/user_3J5VVo50uL70F327Y6AS8CqWwV6/d10a9ac0-4992-41fb-b5e4-b175a88512b0.png" width="600" height="71" alt="Valentte London" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>
<tr><td align="center" style="padding:6px 24px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td align="center" width="33%" style="padding:0 6px;"><a href="https://valentte.com/sale/" target="_blank" style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#212121;text-decoration:none;white-space:nowrap;">Offers</a></td><td align="center" width="33%" style="padding:0 6px;"><a href="https://valentte.com/gift-boxes/" target="_blank" style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#212121;text-decoration:none;white-space:nowrap;">Christmas Gifts</a></td><td align="center" width="33%" style="padding:0 6px;"><a href="https://valentte.com/best-sellers/" target="_blank" style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#212121;text-decoration:none;white-space:nowrap;">Best Sellers</a></td></tr></tbody></table></td></tr>'''

def email(day, slot, ver):
    d = DAYS[day]; subj, subjB, pre = COPY[(day, slot)]
    boxname, boxurl = d['box']
    rows = [
      '<!-- 12 DAYS OF CHRISTMAS thin banner -->',
      imgrow(img(f'strip_d{day}'), HOME, f'The 12 Days of Christmas – Day {day} of 12'),
      HEADER,
      '<!-- FREE GIFT banner -->',
      imgrow(img(f'gift_d{day}_{slot}'), BUNDLE, f"FREE {d['item']} with every order – use code {d['code']}. Claim your FREE gift"),
      f'<!-- HERO · Version {ver} -->',
      imgrow(img(f'hero_d{day}_{slot}_{ver}'), BUNDLE, HERO_ALT[(day, slot, ver)]),
      '<!-- GIFT BOX OFFER OF THE DAY (moved up) -->',
      imgrow(img(f'box_d{day}'), boxurl, f'Best-Selling Gift Box – {boxname} – now £23.99, was £37.99. Save 37%. Shop the gift box', bg='#1E3A2B'),
      '<!-- MORE OFFERS (retail price sheet) -->', tiles(day),
      '<!-- SOCIAL PROOF -->', PROOF,
      '<!-- FREE GIFT reminder -->', reminder(day, slot),
      FOOTER,
    ]
    title = subj
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only">
<title>{title}</title>
<style>
  :root {{ color-scheme: light only; supported-color-schemes: light only; }}
  body, table, td {{ margin:0; padding:0; }} img {{ border:0; display:block; }} body {{ background:#f2efe9; }}
  @media only screen and (max-width:620px) {{ .wrap {{ width:100% !important; }} img {{ max-width:100% !important; height:auto !important; }} .stack-col {{ display:block !important; width:100% !important; max-width:100% !important; padding:0 0 22px !important; }} }}
</style></head>
<body bgcolor="#f2efe9" style="margin:0;padding:0;background:#f2efe9;">
<div style="display:none;max-height:0;overflow:hidden;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#f2efe9" style="background:#f2efe9;"><tr><td align="center" style="padding:24px 0 0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="width:600px;background:#ffffff;">
<!-- {slot} Email {d['date']} · Hero Test {ver} · 12 Days of Christmas Day {day} -->
{chr(10).join(rows)}
</table>
</td></tr></table>
</body></html>
'''

manifest = []
for day in (1, 2, 3):
    for slot in ('AM', 'PM'):
        for ver in ('A', 'B', 'C'):
            h = email(day, slot, ver)
            fn = f'd{day}_{DAYS[day]["date"].replace("/","-")}_{slot}_Hero-{ver}.html'
            open(f'{OUT}/{fn}', 'w').write(h)
            opens, closes = len(re.findall(r'<a\s', h)), h.count('</a>')
            assert opens == closes, (fn, opens, closes)
            assert 'vt_popup' not in h
            s, sb, p = COPY[(day, slot)]
            manifest.append(dict(file=fn, day=day, date=DAYS[day]['date'], dow=DAYS[day]['dow'], slot=slot, version=ver,
                                 node_name=f'{slot} Email {DAYS[day]["date"]} - Hero Test {ver}', subject_A=s, subject_B=sb,
                                 preheader=re.sub('&amp;', '&', p), anchors=opens, bytes=len(h)))
json.dump(manifest, open(f'{OUT}/manifest.json', 'w'), indent=1, ensure_ascii=False)
print(len(manifest), 'emails;', manifest[0]['anchors'], 'anchors each approx;', max(m['bytes'] for m in manifest), 'max bytes')
