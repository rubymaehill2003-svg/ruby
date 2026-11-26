# v2 emails: reuse v1 data/structure, swap in themed images + themed live-HTML sections per day
import json, re, os
S = '/tmp/claude-0/-home-user-ruby/b44f2fb9-6eed-5680-a384-23171670d6e5/scratchpad'
src = open(f'{S}/build/emails.py').read()
src = src[:src.index('manifest = []')]           # definitions only
src = src.replace("os.makedirs(OUT, exist_ok=True)", "")
g = {}; exec(src, g)
U1 = json.load(open(f'{S}/urlmap.json')); U2 = json.load(open(f'{S}/urlmap2.json')); U4 = json.load(open(f'{S}/urlmap4.json'))
def img(k):
    return U4.get(k) or U1[f'vt1203_{k}.jpg']
OUT = '/home/user/ruby/emails/2026-12-01_to_03'
DAYS, COPY, FOOTER, HEADER, a, imgrow = g['DAYS'], g['COPY'], g['FOOTER'], g['HEADER'], g['a'], g['imgrow']
BUNDLE, HOME = g['BUNDLE'], g['HOME']
HERO_ALT = dict(g['HERO_ALT'])
HERO_ALT[(1,'AM','C')] = 'Door No. 1 is open – a 12-door advent calendar, tap to open today’s door. Open door 1'
HERO_ALT[(2,'PM','B')] = 'Christmas in every room, all day long – our diffusers work 24/7, lasts up to 12 weeks. Shop diffusers'
HERO_ALT[(2,'PM','C')] = 'Peel back tonight’s surprise – tap to peel, your festive treat is waiting underneath. Peel to reveal'
HERO_ALT[(3,'PM','B')] = 'It smells designer. It isn’t priced like it. Diffusers from £9.99 when you bundle. See for yourself'

HERO_ALT[(1,'AM','B')] = 'It starts the moment they walk in… Bundle a diffuser for every room from £9.99 each. Build your bundle'
HERO_ALT[(1,'PM','B')] = 'The house everyone talks about. Bundle up and every diffuser is just £9.99. Shop bundles'
HERO_ALT[(1,'AM','C')] = 'Door No. 1 is open – tap to open today’s door, every door hides a bundle saving. Open door 1'
HERO_ALT[(1,'PM','C')] = 'Pull the cracker – every one holds a bundle saving, diffusers from £9.99. Pull to reveal'
HERO_ALT[(2,'AM','A')] = 'Every room, scented for Christmas. Diffusers from £9.99 each when you bundle. Build your bundle'
HERO_ALT[(2,'AM','B')] = 'What’s that beautiful smell? From £9.99 a diffuser when you bundle. Shop bundles'
HERO_ALT[(2,'PM','A')] = 'A diffuser for every room. Save up to £89.91, from £9.99 each. Shop now'
HERO_ALT[(2,'PM','B')] = 'Christmas in every room, all day long. Works 24/7, from £9.99 each when you bundle. Shop now'
HERO_ALT[(2,'AM','C')] = 'A bundle saving is hiding in the snow – shake to reveal, up to £89.91 off'
HERO_ALT[(2,'PM','C')] = 'Peel back tonight’s bundle surprise – up to £89.91 off. Peel to reveal'
HERO_ALT[(3,'AM','B')] = 'The scent that greets you before you’ve even taken your coat off. Bundle one for every room from £9.99 each. Build my bundle'
HERO_ALT[(3,'AM','C')] = 'Three presents, one is yours – every present hides a bundle saving. Pick my present'
HERO_ALT[(3,'PM','C')] = 'Give Christmas a spin – every slice is a bundle saving. Spin now'

TH = {
 1: dict(name='Editorial · forest green & red', page='#E6E0D2', card='#F2EBDF', ink='#2A1A17', acc='#1E4D36', head_font='Inter,Arial,sans-serif', head_style='font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-.5px',
         tile_bg='#F2EBDF', tile_border='2px solid #1E4D36', btn='background:#1E4D36;color:#ffffff;border-radius:0;', title='More to love today', eyebrow='ALSO ON OFFER · DAY 1', align='left',
         proof_bg='#B3202A', proof_fg='#F2EBDF', proof_quote_font='Inter,Arial,sans-serif;font-weight:900;font-style:italic;text-transform:uppercase', rem_bg='#F2EBDF', rem_border='2px solid #1E4D36', rem_radius='0'),
 2: dict(name='Moody burgundy & gold', page='#2A0710', card='#5A1023', ink='#F7EEE2', acc='#D6B46E', head_font='Cardo,Georgia,serif', head_style='font-style:italic',
         tile_bg='#5A1023', tile_border='1.5px solid #D6B46E', btn='background:#F7EEE2;color:#5A1023;border-radius:30px;', title='Little gifts under £11', eyebrow='✦ ALSO ON OFFER · DAY 2 ✦', align='center',
         proof_bg='#F7EEE2', proof_fg='#5A1023', proof_quote_font='Cardo,Georgia,serif;font-style:italic', rem_bg='#F7EEE2', rem_border='1.5px dashed #5A1023', rem_radius='4px'),
 3: dict(name='Collage · red & pine green', page='#EBDCD2', card='#F6F0E7', ink='#2A1A17', acc='#B01E2A', head_font='Cardo,Georgia,serif', head_style='font-style:italic',
         tile_bg='#ffffff', tile_border='2px solid #B01E2A', btn='background:#B01E2A;color:#ffffff;border-radius:3px;', title='Little luxuries, big savings', eyebrow='ALSO ON OFFER · DAY 3', align='center',
         proof_bg='#2A5A40', proof_fg='#ffffff', proof_quote_font='Cardo,Georgia,serif;font-style:italic', rem_bg='#ffffff', rem_border='2px dashed #B01E2A', rem_radius='6px'),
}

def tiles(day):
    t = TH[day]; cells = ''
    for name, url, now, was, pct, k in DAYS[day]['tiles']:
        tagc = '#5A1023' if day == 2 else '#ffffff'
        tagbg = t['acc']
        cells += f'''<td class="stack-col" width="33%" valign="top" style="width:33.33%;padding:0 6px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{t['tile_bg']};border:{t['tile_border']};"><tr><td align="{t['align']}" style="padding:10px 10px 14px;">
{a(url, f'<img src="{img(k)}" width="160" alt="{name} – now £{now}" style="display:block;width:100%;max-width:160px;height:auto;border:0;margin:0 auto;">')}
<div style="padding:10px 0 4px;"><span style="display:inline-block;font-family:Inter,Arial,sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;color:{tagc};background:{tagbg};padding:3px 8px;">SAVE {pct}%</span></div>
<div style="font-family:{t['head_font']};{'font-style:italic;' if day>1 else 'font-weight:700;'}font-size:{15 if day==1 else 16}px;line-height:20px;color:{t['ink']};min-height:40px;">{name}</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:14px;color:{t['ink']};padding:6px 0 10px;"><b>£{now}</b> <span style="opacity:.6;text-decoration:line-through;">£{was}</span></div>
{a(url, f'<span style="display:inline-block;font-family:Inter,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:1.2px;{t["btn"]}padding:10px 16px;">SHOP NOW</span>')}
</td></tr></table></td>'''
    return f'''<tr><td align="{t['align']}" style="padding:32px 18px 30px;background:{t['card']};">
<div style="font-family:Inter,Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:2.5px;color:{t['acc']};padding:0 6px;">{t['eyebrow']}</div>
<div style="font-family:{t['head_font']};{t['head_style']};font-size:{28 if day==1 else 32}px;line-height:36px;color:{t['acc'] if day!=2 else t['ink']};padding:6px 6px 18px;">{t['title']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>'''

def proof(day):
    t = TH[day]
    return f'''<tr><td align="center" style="padding:30px 30px 28px;background:{t['proof_bg']};">
<div style="font-family:Inter,Arial,sans-serif;font-size:18px;letter-spacing:4px;color:{t['proof_fg']};">★★★★★</div>
<div style="font-family:{t['proof_quote_font']};font-size:{24 if day==1 else 27}px;line-height:32px;color:{t['proof_fg']};padding:8px 0 6px;">Everyone who visits asks what it is.</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:13px;line-height:20px;color:{t['proof_fg']};opacity:.85;">350,000+ five-star reviews &nbsp;·&nbsp; Over 1 million happy customers &nbsp;·&nbsp; 1 sold every 18 seconds</div>
</td></tr>'''

def reminder(day, slot):
    t = TH[day]; d = DAYS[day]
    when = 'Today only' if slot == 'AM' else 'Final hours today'
    fg = '#5A1023' if day == 2 else t['acc']
    outer = t['card']
    return f'''<tr><td align="center" style="padding:26px 30px 26px;background:{outer};">
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border:{t['rem_border']};border-radius:{t['rem_radius']};background:{t['rem_bg']};"><tr><td align="center" style="padding:18px 26px;">
<div style="font-family:Inter,Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:2.5px;color:{fg};">DON’T FORGET · {when.upper()}</div>
<div style="font-family:{t['head_font']};{t['head_style']};font-size:22px;line-height:28px;color:{fg};padding:6px 0 4px;">A FREE {d['item']} with every order</div>
<div style="font-family:Inter,Arial,sans-serif;font-size:14px;color:#3a2a26;">Use code <b style="letter-spacing:1.5px;color:{fg};">{d['code']}</b> at checkout.</div>
</td></tr></table></td></tr>'''

def email(day, slot, ver):
    d = DAYS[day]; subj, subjB, pre = COPY[(day, slot)]; t = TH[day]
    boxname, boxurl = d['box']
    rows = [
      HEADER,
      f'<!-- 12 DAYS OF CHRISTMAS thin banner (sits on top of the free gift banner) · Day {day} theme: {t["name"]} -->',
      imgrow(img(f'strip_d{day}'), HOME, f'The 12 Days of Christmas – Day {day} of 12'),
      '<!-- FREE GIFT banner -->',
      imgrow(img(f'gift_d{day}_{slot}'), BUNDLE, f"FREE {d['item']} with every order – use code {d['code']}. Claim your FREE gift"),
      f'<!-- HERO · Version {ver} -->',
      imgrow(img(f'hero_d{day}_{slot}_{ver}'), BUNDLE, HERO_ALT[(day, slot, ver)]),
      '<!-- MAIN OFFER: DIFFUSER BUNDLE (3 / 6 / 10) -->',
      imgrow(img(f'bundle_d{day}'), BUNDLE, 'Bundle & save – 3 diffusers save £21, 6 diffusers save £48, 10 diffusers save £89.91, from £9.99 each. Build your bundle', bg=t['card']),
      '<!-- SECONDARY OFFER: GIFT BOX DEAL OF THE DAY -->',
      imgrow(img(f'box_d{day}'), boxurl, f'Also today: Best-Selling Gift Box – {boxname} – now £23.99, was £37.99. Save 37%. Shop the gift box', bg=t['card']),
      '<!-- 12 DAYS. 12 DEALS. – a new deal every day for the first 12 days of December -->',
      (imgrow(img('deals_d1_AM'), 'https://valentte.com/organic/customer-favourites-mini-mist-box-of-4/', "12 days. 12 deals. A brand-new deal every day for the first 12 days of December, each gone in 24 hours. Day 1 – today only: Customer Favourites Mini Mist Box of 4, now £7.99, was £13.49, 41% off. Shop today’s deal", bg=t['card']) if (day, slot) == (1, 'AM') else
       imgrow(img(f'deals_d{day}'), BUNDLE, f"12 days. 12 deals. A brand-new deal every day for the first 12 days of December, each gone in 24 hours. Day {day} – today only: diffuser bundles from £9.99 each plus a FREE {d['item']} with code {d['code']}. Shop today’s deal", bg=t['card'])),
      '<!-- MORE OFFERS (retail price sheet) -->', tiles(day),
      '<!-- SOCIAL PROOF -->', proof(day),
      '<!-- FREE GIFT reminder -->', reminder(day, slot),
      FOOTER,
    ]
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only">
<title>{subj}</title>
<style>
  :root {{ color-scheme: light only; supported-color-schemes: light only; }}
  body, table, td {{ margin:0; padding:0; }} img {{ border:0; display:block; }} body {{ background:{t['page']}; }}
  @media only screen and (max-width:620px) {{ .wrap {{ width:100% !important; }} img {{ max-width:100% !important; height:auto !important; }} .stack-col {{ display:block !important; width:100% !important; max-width:100% !important; padding:0 0 18px !important; }} }}
</style></head>
<body bgcolor="{t['page']}" style="margin:0;padding:0;background:{t['page']};">
<div style="display:none;max-height:0;overflow:hidden;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="{t['page']}" style="background:{t['page']};"><tr><td align="center" style="padding:24px 0 0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="width:600px;background:#ffffff;">
<!-- {slot} Email {d['date']} · Hero Test {ver} · 12 Days of Christmas Day {day} · theme {t['name']} -->
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
            o, c = len(re.findall(r'<a\s', h)), h.count('</a>'); assert o == c, fn
            s, sb, p = COPY[(day, slot)]
            manifest.append(dict(file=fn, day=day, date=DAYS[day]['date'], dow=DAYS[day]['dow'], slot=slot, version=ver, theme=TH[day]['name'],
                                 node_name=f'{slot} Email {DAYS[day]["date"]} - Hero Test {ver}', subject_A=s, subject_B=sb, preheader=p.replace('&amp;','&'), anchors=o))
json.dump(manifest, open(f'{OUT}/manifest.json', 'w'), indent=1, ensure_ascii=False)
json.dump({**U1, **U2}, open(f'{OUT}/_build/urlmap.json', 'w'), indent=1)
print(len(manifest), 'emails')
