# exec'd inside gen3.py: bundle sections (primary offer) + compact gift box cards (secondary)
PACKS = [('3', 'Save £21', ''), ('6', 'Save £48', ''), ('10', 'Save £89.91', 'From £9.99 each')]

# ---------------- Day 1 · editorial green
def bundle1():
    cols = ''
    for n, sv, note in PACKS:
        best = n == '10'
        bg = R1 if best else C1; fg = C1 if best else R1
        tag = f'<div style="position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:{RED1};color:#fff;font-size:10px;font-weight:800;letter-spacing:1.5px;padding:5px 10px;white-space:nowrap">BEST DEAL</div>' if best else ''
        cols += f'''<div style="position:relative;flex:1;border:2px solid {R1};background:{bg};color:{fg};text-align:center;padding:22px 8px 18px">{tag}
<div style="font-size:64px;font-weight:900;font-style:italic;line-height:.9;letter-spacing:-2px">{n}</div>
<div style="font-size:11px;font-weight:700;letter-spacing:2px;margin-top:4px">DIFFUSERS</div>
<div style="font-size:19px;font-weight:800;margin-top:10px">{sv}</div>
<div style="font-size:12px;margin-top:4px;opacity:.9;min-height:15px">{note}</div></div>'''
    return f'''<div style="background:{C1};border-top:2px solid {R1}">
{marquee1("Bundle & save · Bundle & save", R1, C1, 56, 34, -40)}
{ph('bundle_back.jpg','50% 56%',600,300,'border-bottom:2px solid '+R1)}
<div style="padding:28px 30px 30px">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;color:{R1}">TODAY’S MAIN OFFER · MIX &amp; MATCH ANY SCENTS</div>
<div style="font-size:32px;line-height:1.05;font-weight:800;color:{R1};margin:8px 0 22px;letter-spacing:-.6px">The more rooms you scent, the more you save</div>
<div style="display:flex;gap:12px">{cols}</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:16px">
<div style="font-size:14px;line-height:1.5;max-width:330px">Pick your pack, then choose any scents. Lasts up to 12 weeks each.</div>{btn1('Build your bundle')}</div></div></div>'''

def boxc1(name, img):
    return f'''<div style="background:{C1};border-top:2px solid {R1};border-bottom:2px solid {R1};display:flex">
<div style="width:250px;height:250px;background:#fff url({PR(img)}) center 54%/150% no-repeat;border-right:2px solid {R1};position:relative">
<div style="position:absolute;left:12px;top:12px;background:{RED1};color:#fff;font-size:11px;font-weight:800;letter-spacing:1.2px;padding:6px 10px">SAVE 37%</div></div>
<div style="flex:1;padding:28px 28px 0">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;color:{R1}">ALSO TODAY · GIFT BOX DEAL</div>
<div style="font-size:20px;font-weight:800;color:{R1};line-height:1.15;margin:8px 0 6px">Best-Selling Gift Box<br>{name}</div>
<div style="font-size:13px;line-height:1.45;color:{INK}">Diffuser, natural wax candle &amp; room mist, gift-boxed.</div>
<div style="margin:10px 0 12px"><span style="font-size:28px;font-weight:900;font-style:italic;color:{R1}">£23.99</span> <span style="font-size:13px;color:#7d726c">was <s>£37.99</s></span></div>
{btn1('Shop the gift box')}</div></div>'''

# ---------------- Day 2 · burgundy & gold
def bundle2():
    circ = ''
    xs = [(110, 150), (300, 176), (490, 150)]
    for (n, sv, note), (cx, d) in zip(PACKS, xs):
        best = n == '10'
        ring = G2
        inner = f'''<div style="font-size:10px;font-weight:700;letter-spacing:1.5px;color:{K2b}">BUNDLE OF</div>
<div class="serif" style="font-size:{58 if best else 50}px;line-height:.95;color:{K2};font-weight:700">{n}</div>
<div style="font-size:12px;font-weight:800;letter-spacing:1px;color:{K2}">{sv.upper()}</div>{f'<div class="serif it" style="font-size:13px;color:{K2b}">{note.lower()}</div>' if note else ''}'''
        circ += f'''<div style="position:absolute;left:{cx-d/2}px;top:{360-(d-150)/2}px;width:{d}px;height:{d}px;border-radius:50%;background:{C2};box-shadow:0 0 0 5px {ring},0 14px 26px rgba(0,0,0,.4);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">{inner}</div>'''
    return f'''<div style="height:760px;background:{BG2};position:relative;overflow:hidden">{snow(80,501,'rgba(255,255,255,.35)',2,760)}
<div style="position:absolute;top:40px;left:0;right:0;text-align:center;color:{C2}">
<div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">✦ TODAY’S MAIN OFFER ✦</div>
<div class="serif it" style="font-size:50px;line-height:1.02;margin-top:10px">Bundle &amp; save</div>
<div style="font-size:15px;color:rgba(247,238,226,.85);margin-top:8px">Mix &amp; match any scents – one for every room</div></div>
<div style="position:absolute;left:60px;right:60px;top:200px;height:190px;border-radius:140px 140px 0 0;background:url({P('bundle_back.jpg')}) 50% 56%/cover no-repeat;box-shadow:0 0 0 2px {G2}"></div>
{circ}
<div style="position:absolute;left:40px;right:40px;bottom:46px;text-align:center;color:{C2}">
<div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">Bundle 10 and every diffuser is just £9.99. Each one lasts up to 12 weeks.</div>
<div style="margin-top:16px">{pill2('Build my bundle')}</div></div></div>'''

def boxc2(name, img):
    return f'''<div style="background:{K2};padding:26px 30px;display:flex;gap:24px;align-items:center">
<div style="width:200px;height:230px;border-radius:100px 100px 4px 4px;background:#fff url({PR(img)}) center 54%/170% no-repeat;box-shadow:0 0 0 4px {G2};flex:none"></div>
<div style="color:{C2}">
<div style="color:{G2};font-size:11px;font-weight:700;letter-spacing:2.5px">ALSO TODAY · GIFT BOX DEAL</div>
<div class="serif it" style="font-size:28px;line-height:1.1;margin:8px 0 4px">Best-Selling Gift Box</div>
<div style="font-size:11.5px;font-weight:700;letter-spacing:2px;color:{G2}">{name.upper()}</div>
<div style="font-size:13.5px;line-height:1.45;margin:8px 0 10px;color:rgba(247,238,226,.85)">Diffuser, natural wax candle &amp; room mist, beautifully boxed.</div>
<div style="font-size:15px">Now <span class="serif" style="font-size:30px;font-weight:700">£23.99</span> <span style="opacity:.7">was <s>£37.99</s></span> · <b style="color:{G2}">SAVE 37%</b></div>
<div style="margin-top:12px">{pill2('Shop the gift box')}</div></div></div>'''

# ---------------- Day 3 · red & pine green collage
def bundle3():
    tags = (f"{tag3('3 diffusers','Save £21',-3,R3)}" + f"{tag3('6 diffusers','Save £48',2,G3)}" + f"{tag3('10 diffusers · from £9.99 each','Save £89.91',-2,R3,'#fff',260)}")
    return f'''<div style="height:700px;background:{C3};position:relative;overflow:hidden">
<div style="position:absolute;left:30px;top:40px;right:30px;text-align:left">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{G3}">TODAY’S MAIN OFFER</div>
<div class="serif it" style="font-size:52px;line-height:1;color:{R3};margin-top:8px">Mix, match<br>&amp; save</div></div>
<div style="position:absolute;left:30px;top:220px;display:flex;flex-direction:column;gap:18px">{tags}</div>
<div style="position:absolute;right:26px;top:70px;width:270px;background:#fff;padding:12px 12px 40px;transform:rotate(4deg);box-shadow:0 12px 28px rgba(0,0,0,.18)">
<div style="height:300px;background:url({P('bundle_back.jpg')}) 50% 56%/cover no-repeat"></div>
<div class="serif it" style="position:absolute;left:0;right:0;bottom:10px;text-align:center;font-size:17px;color:{R3}">one for every room</div></div>
<div style="position:absolute;right:40px;top:410px;width:96px;height:96px;border-radius:50%;background:{G3};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);box-shadow:0 0 0 4px {C3}">
<div style="font-size:10px;font-weight:800;letter-spacing:1px">FROM</div><div class="serif" style="font-size:30px;font-weight:700;line-height:1">£9.99</div><div style="font-size:9px;font-weight:800;letter-spacing:1px">EACH</div></div>
<div style="position:absolute;left:30px;right:30px;bottom:44px;display:flex;justify-content:space-between;align-items:center;gap:16px">
<div style="font-size:14.5px;line-height:1.5;max-width:300px">Pick any scents – every diffuser lasts up to 12 weeks.</div>{btn3('Build my bundle')}</div></div>'''

def boxc3(name, img):
    return f'''<div style="background:{B3};padding:24px 30px">
<div style="background:#fff;display:flex;box-shadow:0 8px 20px rgba(0,0,0,.07);border:2px solid {G3}">
<div style="width:230px;height:240px;background:url({PR(img)}) center 54%/160% no-repeat;border-right:2px solid {G3};position:relative;flex:none">
<div style="position:absolute;left:-6px;top:14px">{tag3('save','37%',-6,R3,'#fff',120)}</div></div>
<div style="padding:22px 22px 0">
<div style="font-size:11px;font-weight:700;letter-spacing:2.5px;color:{G3}">ALSO TODAY · GIFT BOX DEAL</div>
<div class="serif it" style="font-size:26px;color:{R3};line-height:1.1;margin:8px 0 2px">Best-Selling Gift Box</div>
<div style="font-size:11.5px;font-weight:700;letter-spacing:2px">{name.upper()}</div>
<div style="margin:10px 0 12px"><span style="font-weight:900;font-size:30px;color:{R3};letter-spacing:-1px">£23.99</span> <span style="font-size:13px;color:#8d7f79">was <s>£37.99</s></span></div>
{btn3('Shop the gift box')}</div></div></div>'''

pages['bundle_d1'] = bundle1(); pages['bundle_d2'] = bundle2(); pages['bundle_d3'] = bundle3()
pages['box_d1'] = boxc1('Jasmine &amp; Rosewood', 'box_jasmine.jpg')
pages['box_d2'] = boxc2('Pure Lavender', 'box_lavender.jpg')
pages['box_d3'] = boxc3('Cardamom &amp; Nutmeg', 'box_cardamom.jpg')

# ---------------- Day 2 A/B heroes · minimal moody style (nkuku-inspired)
def moody(photo, pos, size, eb, head, sub, link, h=760, top=78):
    return f'''<div style="height:{h}px;position:relative;background:#141210 url({P(photo)}) {pos}/{size} no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,10,8,.62) 0%,rgba(12,10,8,.28) 38%,rgba(12,10,8,0) 60%,rgba(12,10,8,.25) 100%)"></div>
<div style="position:absolute;left:60px;right:60px;top:{top}px;text-align:center;color:#EFE6D6">
<div style="font-size:10.5px;letter-spacing:4px;font-weight:500;opacity:.8">{eb}</div>
<div class="serif" style="font-size:42px;line-height:1.12;margin:22px 0 14px;font-weight:400;text-shadow:0 2px 14px rgba(0,0,0,.35)">{head}</div>
<div style="font-size:13px;letter-spacing:.4px;opacity:.85">{sub}</div>
<div style="display:inline-block;margin-top:22px;font-size:13px;letter-spacing:.6px;padding-bottom:3px;border-bottom:1px solid rgba(239,230,214,.85)">{link}</div></div></div>'''

pages['hero_d2_AM_A'] = moody('p49_diffbox.jpg', '46% 60%', 'auto 118%', 'THE 12 DAYS OF CHRISTMAS · DAY 2', 'Every room, scented<br>for Christmas', 'Diffusers from £9.99 each when you bundle', 'Build your bundle')
pages['hero_d2_AM_B'] = moody('p48_bsgb.jpg', '50% 62%', 'cover', 'DAY 2 · READY FOR GUESTS?', 'What’s that<br>beautiful smell?', 'From £9.99 a diffuser when you bundle', 'Shop bundles')
pages['hero_d2_PM_A'] = moody('cover1.jpg', '60% 70%', 'auto 128%', 'DAY 2 · BUNDLE &amp; SAVE', 'A diffuser for<br>every room', 'Save up to £89.91 · from £9.99 each', 'Shop now')
pages['hero_d2_PM_B'] = moody('cover2.jpg', '48% 66%', 'cover', 'DAY 2 · AROUND THE CLOCK', 'Christmas in every room,<br>all day long', 'Works 24/7 · from £9.99 each when you bundle', 'Shop now')

# ---------------- Free gift banners · bauble design on every day (own product, code, day colour)
def gift_orn(day, slot, item, code, photo, pos, size, c_mid, c_main, c_dark, seed):
    bg = f'radial-gradient(ellipse at 50% 30%, {c_mid} 0%, {c_main} 60%, {c_dark} 100%)'
    head = f'Your Day {day} gift' if slot == 'AM' else 'Final hours…'
    sub = f'A FREE {item.upper()} WITH EVERY ORDER' if slot == 'AM' else f'YOUR FREE {item.upper()} ENDS TODAY'
    ticket = f'''<div style="position:relative;display:inline-block;background:{C2};color:{c_main};padding:11px 30px;font-weight:700;letter-spacing:2.5px;font-size:13px">
<span style="position:absolute;left:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:{c_main};transform:translateY(-50%)"></span>
<span style="position:absolute;right:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:{c_main};transform:translateY(-50%)"></span>
<span style="border-left:1.5px dashed {c_main};padding-left:14px;margin-left:-6px">CODE&nbsp; {code}</span></div>'''
    return f'''<div style="height:280px;background:{bg};position:relative;overflow:hidden">{snow(40,seed,'rgba(255,255,255,.35)',2,280)}
{ornament(150, 60, 180, photo, pos, size)}
<div style="position:absolute;left:290px;right:24px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:flex-start">
<div class="serif it" style="color:{C2};font-size:38px;line-height:1">{head}</div>
<div style="color:{G2};font-size:10.5px;font-weight:700;letter-spacing:1.6px;margin:10px 0 16px">{sub}</div>
{ticket}<div style="margin-top:14px">{pill2('Claim your gift →', C2, c_main)}</div></div></div>'''

for slot in ('AM', 'PM'):
    pages[f'gift_d1_{slot}'] = gift_orn(1, slot, 'candle', 'FREEFLAME', 'candle_only.jpg', '50% 45%', 'cover', '#2E6E4D', '#1E4D36', '#0E2619', 11 + (slot == 'PM'))
    pages[f'gift_d2_{slot}'] = gift_orn(2, slot, 'boxed diffuser', 'FREEDIFF', 'p49_diffbox.jpg', '40% 58%', '300%', K2b, K2, '#2A0710', 22 + (slot == 'PM'))
    pages[f'gift_d3_{slot}'] = gift_orn(3, slot, 'candle', 'FREEFLAME', 'candle_only.jpg', '50% 45%', 'cover', '#C83440', '#B01E2A', '#5E0C14', 33 + (slot == 'PM'))

# ---------------- "12 Days. 12 Deals." salesy section (per day, own colours)
def deals(day, bg, panel, ink, acc, hot, hot_fg, head_css, sub_css, today_line, btn, thumb=None, price='', stack=False, tag='TODAY ONLY'):
    cells = ''
    for n in range(1, 13):
        if n < day:
            cells += f'''<div style="height:84px;border:1.5px solid {acc};opacity:.55;display:flex;flex-direction:column;align-items:center;justify-content:center;color:{ink}">
<div style="font-size:26px;font-weight:900;font-style:italic;text-decoration:line-through">{n}</div><div style="font-size:8.5px;font-weight:800;letter-spacing:1.2px">DEAL ENDED</div></div>'''
        elif n == day:
            cells += f'''<div style="height:84px;background:{hot};color:{hot_fg};display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 0 3px {panel},0 0 0 5px {hot};transform:scale(1.08)">
<div style="font-size:32px;font-weight:900;font-style:italic;line-height:1">{n}</div><div style="font-size:8.5px;font-weight:800;letter-spacing:1.2px">OPEN NOW</div></div>'''
        else:
            cells += f'''<div style="height:84px;border:1.5px dashed {acc};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{ink}">
<div style="font-size:26px;font-weight:900;font-style:italic;opacity:.9">{n}</div><div style="font-size:8.5px;font-weight:800;letter-spacing:1.2px;opacity:.75">🔒 {n} DEC</div></div>'''
    nxt = f'Come back tomorrow – Day {day+1}’s deal unlocks at 7:30am.'
    return f'''<div style="background:{bg};padding:34px 28px 34px;position:relative;overflow:hidden">{snow(50,600+day,'rgba(255,255,255,.18)',2,700)}
<div style="text-align:center;position:relative">
<div style="display:inline-block;background:{hot};color:{hot_fg};font-size:11px;font-weight:800;letter-spacing:2.5px;padding:6px 14px">THE 12 DAYS OF CHRISTMAS</div>
<div style="{head_css};color:{ink};margin:14px 0 8px">12 days. 12 deals.</div>
<div style="{sub_css};color:{ink};opacity:.92">A brand-new deal drops every single day for the first 12 days of December – and each one is gone in 24 hours.</div></div>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin:24px 4px 22px;position:relative">{cells}</div>
<div style="background:{panel};padding:20px 22px;position:relative;display:flex;gap:18px;align-items:center;justify-content:space-between">
{f'<div style="width:96px;height:96px;flex:none;background:#fff url({PR(thumb)}) center/cover no-repeat;border:1.5px solid {hot}"></div>' if thumb else ''}
<div style="flex:1"><div style="font-size:11px;font-weight:800;letter-spacing:2px;color:{hot}">DAY {day} · {tag}</div>
<div style="font-size:19px;font-weight:800;line-height:1.25;color:#2A1A17;margin-top:4px">{today_line}</div>{price}
{f'<div style="margin-top:12px">{btn}</div>' if stack else ''}</div>
{'' if stack else f'<div style="flex:none">{btn}</div>'}</div></div>'''

pages['deals_d1'] = deals(1, R1, C1, C1, 'rgba(242,235,223,.9)', RED1, '#fff',
    'font-size:54px;font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-2px;line-height:.95', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME', btn1("Shop today’s deal", RED1))
pages['deals_d2'] = deals(2, BG2, C2, C2, G2, G2, K2,
    'font-family:Cardo,Georgia,serif;font-style:italic;font-size:54px;line-height:1', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE boxed diffuser with code FREEDIFF', pill2("Shop today’s deal", K2, C2))
pages['deals_d3'] = deals(3, R3, C3, '#fff', 'rgba(255,255,255,.85)', G3, '#fff',
    'font-weight:900;font-size:58px;letter-spacing:-2.5px;line-height:.95;text-transform:uppercase', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME', btn3("Shop today’s deal", G3))

pages['deals_d1_AM'] = deals(1, R1, C1, C1, 'rgba(242,235,223,.9)', RED1, '#fff',
    'font-size:54px;font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-2px;line-height:.95', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Customer Favourites Mini Mist Box of 4', btn1("Shop today’s deal", RED1), thumb='minimist.jpg',
    price=f'<div style="margin-top:4px"><span style="font-size:24px;font-weight:900;font-style:italic;color:{RED1}">£7.99</span> <span style="font-size:13px;color:#7d726c">was <s>£13.49</s></span> <span style="display:inline-block;background:{RED1};color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">41% OFF</span></div>')

# ================= TUESDAY PM · "Tuesday night" layout (night green + gold, new formats)
N1 = '#0F2A1D'; N1b = '#173D2A'; GOLDN = '#D6B46E'; CRN = '#F3EBDD'
BGN = f'radial-gradient(ellipse at 50% 20%, {N1b} 0%, {N1} 60%, #08180F 100%)'
def btnN(label, bg=RED1, fg='#fff'):
    return f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:700;font-size:13px;letter-spacing:1.4px;text-transform:uppercase;padding:14px 22px;border-radius:2px;white-space:nowrap">{label}</div>'

def bundle1PM():
    steps = [('1', 'Pick your pack', '3, 6 or 10 diffusers'), ('2', 'Choose any scents', 'Mix &amp; match freely'), ('3', 'Save up to £89.91', 'From £9.99 each')]
    st = ''.join(f'''<div style="flex:1;text-align:center;color:{CRN}"><div style="width:54px;height:54px;border-radius:50%;border:1.5px solid {GOLDN};margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-family:Cardo,Georgia,serif;font-size:26px;color:{GOLDN}">{n}</div>
<div style="font-size:15px;font-weight:700">{t}</div><div style="font-size:12.5px;opacity:.75;margin-top:4px">{s}</div></div>''' for n, t, s in steps)
    pills = ''.join(f'<div style="background:rgba(15,42,29,.88);border:1px solid {GOLDN};color:{CRN};padding:10px 14px;text-align:center;flex:1"><div class="serif" style="font-size:26px;color:{GOLDN};line-height:1">{n}</div><div style="font-size:11px;font-weight:700;letter-spacing:1px;margin-top:3px">{sv}</div></div>' for n, sv in [('3', 'SAVE £21'), ('6', 'SAVE £48'), ('10', 'SAVE £89.91')])
    return f'''<div style="background:{BGN};padding:40px 0 36px;position:relative;overflow:hidden">{snow(60,701,'rgba(255,255,255,.25)',2,760)}
<div style="text-align:center;color:{CRN};padding:0 30px;position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{GOLDN}">TONIGHT’S MAIN OFFER</div>
<div class="serif it" style="font-size:46px;line-height:1.05;margin:10px 0 26px">Build your bundle tonight</div></div>
<div style="display:flex;gap:10px;padding:0 26px;position:relative">{st}</div>
<div style="position:relative;margin:30px 0 0;height:300px;background:url({P('bundle_back.jpg')}) 50% 56%/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,42,29,0) 40%,rgba(15,42,29,.85) 100%)"></div>
<div style="position:absolute;left:26px;right:26px;bottom:18px;display:flex;gap:10px">{pills}</div></div>
<div style="text-align:center;margin-top:26px;position:relative">{btnN('Start building')}</div></div>'''

def box1PM(name):
    return f'''<div style="height:380px;position:relative;background:#111 url({P('p48_bsgb.jpg')}) 50% 60%/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,24,15,.95) 0%,rgba(8,24,15,.8) 45%,rgba(8,24,15,0) 75%)"></div>
<div style="position:absolute;left:34px;top:0;bottom:0;width:300px;display:flex;flex-direction:column;justify-content:center;color:{CRN}">
<div style="font-size:11px;font-weight:700;letter-spacing:2.5px;color:{GOLDN}">ALSO TONIGHT · GIFT BOX DEAL</div>
<div class="serif it" style="font-size:32px;line-height:1.1;margin:10px 0 4px">Best-Selling<br>Gift Box</div>
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:{GOLDN}">{name.upper()}</div>
<div style="font-size:13.5px;line-height:1.45;margin:10px 0 12px;opacity:.85">Diffuser, natural wax candle &amp; room mist – gift-boxed.</div>
<div><span class="serif" style="font-size:34px;font-weight:700">£23.99</span> <span style="font-size:14px;opacity:.7">was <s>£37.99</s></span> <span style="display:inline-block;background:{RED1};color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">37% OFF</span></div>
<div style="margin-top:16px">{btnN('Shop the gift box', CRN, N1)}</div></div></div>'''

def deals1PM():
    dots = ''
    for n in range(1, 13):
        if n == 1:
            dots += f'<div style="text-align:center;flex:1"><div style="width:30px;height:30px;margin:0 auto;border-radius:50%;background:{RED1};color:#fff;font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px {N1},0 0 0 5px {RED1}">1</div><div style="font-size:8.5px;font-weight:800;letter-spacing:.8px;color:{CRN};margin-top:8px">TODAY</div></div>'
        else:
            dots += f'<div style="text-align:center;flex:1"><div style="width:26px;height:26px;margin:2px auto 0;border-radius:50%;border:1.5px solid {GOLDN};color:{GOLDN};font-weight:700;font-size:11px;display:flex;align-items:center;justify-content:center">{n}</div><div style="font-size:8.5px;font-weight:700;letter-spacing:.8px;color:{CRN};opacity:.6;margin-top:8px">{n} DEC</div></div>'
    return f'''<div style="background:{N1};padding:36px 28px 34px;position:relative;overflow:hidden;border-top:1px solid rgba(214,180,110,.35)">{snow(40,702,'rgba(255,255,255,.2)',2,520)}
<div style="display:flex;gap:26px;align-items:center;position:relative">
<div style="width:150px;height:150px;flex:none;border-radius:50%;border:2px solid {GOLDN};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{CRN}">
<div style="font-size:10px;font-weight:700;letter-spacing:2px;color:{GOLDN}">DAY</div><div class="serif" style="font-size:72px;line-height:.9">1</div><div style="font-size:10px;font-weight:700;letter-spacing:2px;color:{GOLDN}">OF 12</div></div>
<div style="color:{CRN}"><div style="display:inline-block;background:{RED1};color:#fff;font-size:10.5px;font-weight:800;letter-spacing:2px;padding:5px 10px">ENDS AT MIDNIGHT</div>
<div class="serif it" style="font-size:38px;line-height:1.05;margin:10px 0 8px">12 days. 12 deals.</div>
<div style="font-size:14px;line-height:1.5;opacity:.88">A new deal every day for the first 12 days of December. Tonight’s is gone at midnight.</div></div></div>
<div style="position:relative;margin:28px 0 24px"><div style="position:absolute;left:30px;right:30px;top:15px;height:1px;background:rgba(214,180,110,.5)"></div>
<div style="display:flex;position:relative">{dots}</div></div>
<div style="background:{CRN};padding:18px 22px;display:flex;justify-content:space-between;align-items:center;gap:16px;position:relative">
<div><div style="font-size:11px;font-weight:800;letter-spacing:2px;color:{RED1}">TONIGHT ONLY</div>
<div style="font-size:17px;font-weight:800;line-height:1.3;color:#2A1A17;margin-top:3px">Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME</div>
</div>{btnN("Shop tonight’s deal")}</div></div>'''

pages['bundle_d1_PM'] = bundle1PM()
pages['box_d1_PM'] = box1PM('Jasmine &amp; Rosewood')
pages['deals_d1_PM'] = deals1PM()

# ---- Tuesday PM heroes in night style (same photo for A & B as requested)
def heroN_A():
    return f'''<div style="background:{N1}">
<div style="height:470px;background:url({P('p49_diffbox.jpg')}) 44% 62%/cover no-repeat;position:relative"><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,42,29,0) 55%,rgba(15,42,29,1) 100%)"></div></div>
<div style="padding:4px 34px 34px;text-align:center;color:{CRN};position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{GOLDN}">DAY 1 · TONIGHT’S BUNDLE OFFER</div>
<div class="serif it" style="font-size:44px;line-height:1.05;margin:12px 0 12px">One for every room.<br>Save up to £89.91</div>
<div style="font-size:15px;line-height:1.5;opacity:.88">Reed diffusers from £9.99 each when you bundle, plus a FREE candle with code FREEFLAME.</div>
<div style="margin-top:20px">{btnN('Shop bundles')}</div></div>
<div style="height:44px;background:{GOLDN};color:{N1};display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:800;letter-spacing:2.6px">FROM £9.99 EACH · SAVE UP TO £89.91 · ENDS AT MIDNIGHT</div></div>'''

def heroN_B():
    return f'''<div style="height:760px;position:relative;background:url({P('p49_diffbox.jpg')}) 44% 60%/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,24,15,.15) 30%,rgba(8,24,15,.8) 62%,rgba(8,24,15,.97) 100%)"></div>
<div style="position:absolute;inset:16px;border:1px solid rgba(214,180,110,.7)"></div>{snow(60,711,'rgba(255,255,255,.45)',2,760)}
<div style="position:absolute;left:50px;right:50px;bottom:60px;text-align:center;color:{CRN}">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{GOLDN}">DAY 1 · AFTER DARK</div>
<div class="serif it" style="font-size:50px;line-height:1.04;margin:12px 0 12px">The house everyone<br>talks about</div>
<div style="font-size:15px;line-height:1.5;opacity:.88">Strong, never overpowering. Bundle up and every diffuser is just £9.99.</div>
<div style="margin-top:20px">{btnN('Shop bundles', GOLDN, N1)}</div></div></div>'''

def heroN_C():
    return f'''<div style="background:{BGN};padding:40px 30px 36px;position:relative;overflow:hidden;text-align:center">{snow(90,712,'rgba(255,255,255,.35)',2.2,700)}
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{GOLDN};position:relative">DAY 1 · AFTER-WORK TREAT</div>
<div class="serif it" style="font-size:48px;line-height:1.04;color:{CRN};margin:10px 0 0;position:relative">Pull tonight’s cracker</div>
<svg width="540" height="300" style="display:block;margin:6px 0 0;position:relative"><g transform="translate(270,150) rotate(-10)">
<g transform="translate(-24,0)"><path d="M-200 -42 L-130 -42 L-104 -20 L-40 -46 L0 -46 L0 46 L-40 46 L-104 20 L-130 42 L-200 42 L-222 0Z" fill="{RED1}"/>
{''.join(f'<rect x="{-190+i*36}" y="-46" width="10" height="92" fill="{GOLDN}" opacity=".95"/>' for i in range(5))}</g>
<g transform="translate(24,0)"><path d="M200 -42 L130 -42 L104 -20 L40 -46 L0 -46 L0 46 L40 46 L104 20 L130 42 L200 42 L222 0Z" fill="{RED1}"/>
{''.join(f'<rect x="{30+i*36}" y="-46" width="10" height="92" fill="{GOLDN}" opacity=".95"/>' for i in range(5))}</g>
<g stroke="{GOLDN}" stroke-width="4" stroke-linecap="round"><path d="M-10 -62 L-18 -90"/><path d="M4 -66 L6 -98"/><path d="M16 -60 L30 -86"/><path d="M-10 62 L-20 88"/><path d="M14 62 L26 88"/></g>
<rect x="-62" y="-26" width="124" height="52" fill="{N1}" stroke="{GOLDN}" stroke-width="3"/><text x="0" y="12" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="32" fill="{GOLDN}">Snap!</text></g></svg>
<div style="font-size:15px;line-height:1.5;color:{CRN};opacity:.9;position:relative">Every cracker holds a bundle saving – diffusers from £9.99 each. Everyone wins.</div>
<div style="margin-top:18px;position:relative">{btnN('Pull to reveal')}</div></div>'''

pages['hero_d1_PM_A'] = heroN_A(); pages['hero_d1_PM_B'] = heroN_B(); pages['hero_d1_PM_C'] = heroN_C()

# ================= TUESDAY PM · brightened version (same layouts, light sage & cream)
L_BG = '#EAF2E7'; L_BG2 = '#F7FAF4'; L_CARD = '#FFFFFF'; L_TXT = '#1E4D36'; L_GOLD = '#B0863A'; L_CREAM = '#F7F1E6'
L_GRAD = f'radial-gradient(ellipse at 50% 15%, {L_BG2} 0%, {L_BG} 70%, #DCE9D8 100%)'

def bundle1PM_L():
    steps = [('1', 'Pick your pack', '3, 6 or 10 diffusers'), ('2', 'Choose any scents', 'Mix &amp; match freely'), ('3', 'Save up to £89.91', 'From £9.99 each')]
    st = ''.join(f'''<div style="flex:1;text-align:center;color:{L_TXT}"><div style="width:54px;height:54px;border-radius:50%;background:{L_TXT};margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-family:Cardo,Georgia,serif;font-size:26px;color:#fff">{n}</div>
<div style="font-size:15px;font-weight:700">{t}</div><div style="font-size:12.5px;opacity:.75;margin-top:4px">{s}</div></div>''' for n, t, s in steps)
    pills = ''.join(f'<div style="background:rgba(255,255,255,.94);border:1.5px solid {L_TXT};color:{L_TXT};padding:10px 14px;text-align:center;flex:1"><div class="serif" style="font-size:26px;color:{RED1};line-height:1">{n}</div><div style="font-size:11px;font-weight:800;letter-spacing:1px;margin-top:3px">{sv}</div></div>' for n, sv in [('3', 'SAVE £21'), ('6', 'SAVE £48'), ('10', 'SAVE £89.91')])
    return f'''<div style="background:{L_GRAD};padding:40px 0 36px;position:relative;overflow:hidden">
<div style="text-align:center;color:{L_TXT};padding:0 30px;position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{RED1}">TONIGHT’S MAIN OFFER</div>
<div class="serif it" style="font-size:46px;line-height:1.05;margin:10px 0 26px">Build your bundle tonight</div></div>
<div style="display:flex;gap:10px;padding:0 26px;position:relative">{st}</div>
<div style="position:relative;margin:30px 26px 0;height:300px;background:url({P('bundle_back.jpg')}) 50% 56%/cover no-repeat;box-shadow:0 0 0 6px #fff">
<div style="position:absolute;left:16px;right:16px;bottom:16px;display:flex;gap:10px">{pills}</div></div>
<div style="text-align:center;margin-top:26px;position:relative">{btnN('Start building', RED1)}</div></div>'''

def box1PM_L(name):
    return f'''<div style="height:380px;position:relative;background:#f4efe6 url({P('p48_bsgb.jpg')}) 50% 60%/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(247,241,230,.98) 0%,rgba(247,241,230,.92) 46%,rgba(247,241,230,0) 76%)"></div>
<div style="position:absolute;left:34px;top:0;bottom:0;width:300px;display:flex;flex-direction:column;justify-content:center;color:{L_TXT}">
<div style="font-size:11px;font-weight:700;letter-spacing:2.5px;color:{RED1}">ALSO TONIGHT · GIFT BOX DEAL</div>
<div class="serif it" style="font-size:32px;line-height:1.1;margin:10px 0 4px">Best-Selling<br>Gift Box</div>
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:{L_GOLD}">{name.upper()}</div>
<div style="font-size:13.5px;line-height:1.45;margin:10px 0 12px;color:#3b4a40">Diffuser, natural wax candle &amp; room mist – gift-boxed.</div>
<div><span class="serif" style="font-size:34px;font-weight:700">£23.99</span> <span style="font-size:14px;color:#7a7a72">was <s>£37.99</s></span> <span style="display:inline-block;background:{RED1};color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">37% OFF</span></div>
<div style="margin-top:16px">{btnN('Shop the gift box', L_TXT)}</div></div></div>'''

def deals1PM_L():
    dots = ''
    for n in range(1, 13):
        if n == 1:
            dots += f'<div style="text-align:center;flex:1"><div style="width:30px;height:30px;margin:0 auto;border-radius:50%;background:{RED1};color:#fff;font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px {L_CREAM},0 0 0 5px {RED1}">1</div><div style="font-size:8.5px;font-weight:800;letter-spacing:.8px;color:{RED1};margin-top:8px">TODAY</div></div>'
        else:
            dots += f'<div style="text-align:center;flex:1"><div style="width:26px;height:26px;margin:2px auto 0;border-radius:50%;background:#fff;border:1.5px solid {L_TXT};color:{L_TXT};font-weight:700;font-size:11px;display:flex;align-items:center;justify-content:center">{n}</div><div style="font-size:8.5px;font-weight:700;letter-spacing:.8px;color:{L_TXT};opacity:.6;margin-top:8px">{n} DEC</div></div>'
    return f'''<div style="background:{L_CREAM};padding:36px 28px 34px;position:relative;overflow:hidden">
<div style="display:flex;gap:26px;align-items:center;position:relative">
<div style="width:150px;height:150px;flex:none;border-radius:50%;background:{L_TXT};display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;box-shadow:0 0 0 6px {L_CREAM},0 0 0 8px {L_GOLD}">
<div style="font-size:10px;font-weight:700;letter-spacing:2px;color:#E2C27A">DAY</div><div class="serif" style="font-size:72px;line-height:.9">1</div><div style="font-size:10px;font-weight:700;letter-spacing:2px;color:#E2C27A">OF 12</div></div>
<div style="color:{L_TXT}"><div style="display:inline-block;background:{RED1};color:#fff;font-size:10.5px;font-weight:800;letter-spacing:2px;padding:5px 10px">ENDS AT MIDNIGHT</div>
<div class="serif it" style="font-size:38px;line-height:1.05;margin:10px 0 8px">12 days. 12 deals.</div>
<div style="font-size:14px;line-height:1.5;color:#3b4a40">A new deal every day for the first 12 days of December. Tonight’s is gone at midnight.</div></div></div>
<div style="position:relative;margin:28px 0 24px"><div style="position:absolute;left:30px;right:30px;top:15px;height:1.5px;background:{L_TXT};opacity:.35"></div>
<div style="display:flex;position:relative">{dots}</div></div>
<div style="background:#fff;border:1.5px solid {L_TXT};padding:18px 22px;display:flex;justify-content:space-between;align-items:center;gap:16px;position:relative">
<div><div style="font-size:11px;font-weight:800;letter-spacing:2px;color:{RED1}">TONIGHT ONLY</div>
<div style="font-size:17px;font-weight:800;line-height:1.3;color:#2A1A17;margin-top:3px">Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME</div>
</div>{btnN("Shop tonight’s deal")}</div></div>'''

def heroL_A():
    return f'''<div style="background:{L_BG}">
<div style="height:470px;background:url({P('p49_diffbox.jpg')}) 44% 62%/cover no-repeat;position:relative;filter:brightness(1.12)"><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(234,242,231,0) 60%,rgba(234,242,231,1) 100%)"></div></div>
<div style="padding:4px 34px 34px;text-align:center;color:{L_TXT};position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{RED1}">DAY 1 · TONIGHT’S BUNDLE OFFER</div>
<div class="serif it" style="font-size:44px;line-height:1.05;margin:12px 0 12px">One for every room.<br>Save up to £89.91</div>
<div style="font-size:15px;line-height:1.5;color:#3b4a40">Reed diffusers from £9.99 each when you bundle, plus a FREE candle with code FREEFLAME.</div>
<div style="margin-top:20px">{btnN('Shop bundles', RED1)}</div></div>
<div style="height:44px;background:{L_TXT};color:#fff;display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:800;letter-spacing:2.6px">FROM £9.99 EACH · SAVE UP TO £89.91 · ENDS AT MIDNIGHT</div></div>'''

def heroL_B():
    return f'''<div style="background:{L_CREAM};padding:22px 22px 32px">
<div style="height:470px;background:url({P('p49_diffbox.jpg')}) 44% 60%/cover no-repeat;filter:brightness(1.12);box-shadow:0 0 0 1.5px {L_GOLD}"></div>
<div style="text-align:center;color:{L_TXT};padding:26px 24px 0">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{RED1}">DAY 1 · AFTER DARK</div>
<div class="serif it" style="font-size:48px;line-height:1.04;margin:12px 0 12px">The house everyone<br>talks about</div>
<div style="font-size:15px;line-height:1.5;color:#3b4a40">Strong, never overpowering. Bundle up and every diffuser is just £9.99.</div>
<div style="margin-top:20px">{btnN('Shop bundles', L_TXT)}</div></div></div>'''

def heroL_C():
    return f'''<div style="background:{L_GRAD};padding:40px 30px 36px;position:relative;overflow:hidden;text-align:center">{snow(70,712,'rgba(176,134,58,.35)',2.2,700)}
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{RED1};position:relative">DAY 1 · AFTER-WORK TREAT</div>
<div class="serif it" style="font-size:48px;line-height:1.04;color:{L_TXT};margin:10px 0 0;position:relative">Pull tonight’s cracker</div>
<svg width="540" height="300" style="display:block;margin:6px 0 0;position:relative"><g transform="translate(270,150) rotate(-10)">
<g transform="translate(-24,0)"><path d="M-200 -42 L-130 -42 L-104 -20 L-40 -46 L0 -46 L0 46 L-40 46 L-104 20 L-130 42 L-200 42 L-222 0Z" fill="{RED1}"/>
{''.join(f'<rect x="{-190+i*36}" y="-46" width="10" height="92" fill="#E2C27A"/>' for i in range(5))}</g>
<g transform="translate(24,0)"><path d="M200 -42 L130 -42 L104 -20 L40 -46 L0 -46 L0 46 L40 46 L104 20 L130 42 L200 42 L222 0Z" fill="{RED1}"/>
{''.join(f'<rect x="{30+i*36}" y="-46" width="10" height="92" fill="#E2C27A"/>' for i in range(5))}</g>
<g stroke="{L_GOLD}" stroke-width="4" stroke-linecap="round"><path d="M-10 -62 L-18 -90"/><path d="M4 -66 L6 -98"/><path d="M16 -60 L30 -86"/><path d="M-10 62 L-20 88"/><path d="M14 62 L26 88"/></g>
<rect x="-62" y="-26" width="124" height="52" fill="#fff" stroke="{L_TXT}" stroke-width="3"/><text x="0" y="12" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="32" fill="{L_TXT}">Snap!</text></g></svg>
<div style="font-size:15px;line-height:1.5;color:#3b4a40;position:relative">Every cracker holds a bundle saving – diffusers from £9.99 each. Everyone wins.</div>
<div style="margin-top:18px;position:relative">{btnN('Pull to reveal', RED1)}</div></div>'''

pages['bundle_d1_PM'] = bundle1PM_L(); pages['box_d1_PM'] = box1PM_L('Jasmine &amp; Rosewood'); pages['deals_d1_PM'] = deals1PM_L()
pages['hero_d1_PM_A'] = heroL_A(); pages['hero_d1_PM_B'] = heroL_B(); pages['hero_d1_PM_C'] = heroL_C()

# ================= WEDNESDAY AM upgrades
pages['gift_d2_AM'] = gift_orn(2, 'AM', 'boxed diffuser', 'FREEDIFF', 'diffuser_only.jpg', '50% 88%', 'cover', K2b, K2, '#2A0710', 22)
pages['hero_d2_AM_A'] = moody('ai_festive_A.jpg', '50% 60%', 'cover', 'THE 12 DAYS OF CHRISTMAS · DAY 2', 'Every room, scented<br>for Christmas', 'Diffusers from £9.99 each when you bundle', 'Build your bundle')
pages['hero_d2_AM_B'] = moody('ai_festive_B.jpg', '50% 62%', 'cover', 'DAY 2 · READY FOR GUESTS?', 'What’s that<br>beautiful smell?', 'From £9.99 a diffuser when you bundle', 'Shop bundles')

def bundle2AM(bar='★ TODAY ONLY · BUNDLE &amp; SAVE ★', eb='TODAY’S MAIN OFFER', strip='bundle_back.jpg', spos='50% 56%'):
    def card(n, sv, extra, best=False):
        rib = f'<div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:{G2};color:{K2};font-size:10px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;white-space:nowrap">BEST VALUE</div>' if best else ''
        return f'''<div style="position:relative;flex:1;background:{C2 if not best else '#fff'};text-align:center;padding:22px 8px 18px;box-shadow:{'0 0 0 3px '+G2 if best else 'none'};{'transform:scale(1.06)' if best else ''}">{rib}
<div style="font-size:11px;font-weight:800;letter-spacing:1.5px;color:{K2b}">BUNDLE OF</div>
<div class="serif" style="font-size:62px;line-height:.95;font-weight:700;color:{K2}">{n}</div>
<div style="display:inline-block;background:{K2};color:{C2};font-size:13px;font-weight:800;letter-spacing:.5px;padding:6px 10px;margin-top:6px">{sv}</div>
<div style="font-size:12px;color:{K2b};margin-top:8px;font-weight:600;min-height:15px">{extra}</div></div>'''
    ticks = ''.join(f'<div style="display:flex;align-items:center;gap:8px"><span style="width:20px;height:20px;border-radius:50%;background:{G2};color:{K2};font-size:12px;font-weight:900;display:inline-flex;align-items:center;justify-content:center">✓</span>{t}</div>' for t in ['Any scents, mix &amp; match', 'Each lasts up to 12 weeks', 'FREE boxed diffuser · FREEDIFF'])
    return f'''<div style="background:{BG2};padding:0 0 36px;position:relative;overflow:hidden">{snow(70,801,'rgba(255,255,255,.3)',2,900)}
<div style="background:{G2};color:{K2};text-align:center;font-size:12px;font-weight:800;letter-spacing:3px;padding:10px 0;position:relative">{bar}</div>
<div style="text-align:center;color:{C2};padding:30px 30px 0;position:relative">
<div style="font-size:12px;font-weight:700;letter-spacing:3px;color:{G2}">{eb}</div>
<div class="serif" style="font-size:64px;line-height:.98;font-weight:700;margin:8px 0 6px">Save up to £89.91</div>
<div class="serif it" style="font-size:24px;color:{G2}">diffusers from just £9.99 each</div></div>
<div style="display:flex;gap:12px;padding:30px 30px 0;position:relative">{card('3','SAVE £21','')}{card('6','SAVE £48','')}{card('10','SAVE £89.91','just £9.99 each',True)}</div>
<div style="margin:26px 30px 0;height:230px;background:url({P(strip)}) {spos}/cover no-repeat;box-shadow:0 0 0 2px {G2};position:relative"></div>
<div style="display:flex;justify-content:space-between;gap:10px;padding:20px 30px 0;color:{C2};font-size:13px;font-weight:600;position:relative">{ticks}</div>
<div style="text-align:center;margin-top:24px;position:relative"><div style="display:inline-block;background:{G2};color:{K2};font-weight:800;font-size:15px;letter-spacing:1.8px;padding:17px 44px;border-radius:40px;box-shadow:0 8px 20px rgba(0,0,0,.35)">BUILD MY BUNDLE &amp; SAVE →</div>
<div style="color:{C2};font-size:12.5px;margin-top:12px;opacity:.85"><span style="color:{G2};letter-spacing:2px">★★★★★</span> &nbsp;350,000+ five-star reviews</div></div></div>'''

def box2AM(name, img, eb='ALSO TODAY · GIFT BOX DEAL'):
    return f'''<div style="background:{K2};padding:30px 30px 34px">
<div style="background:{C2};padding:18px 18px 24px;box-shadow:0 0 0 2px {G2}">
<div style="display:flex;justify-content:space-between;align-items:center;padding:0 4px 12px">
<div style="font-size:11px;font-weight:800;letter-spacing:2.5px;color:{K2b}">{eb}</div>
<div style="background:{K2};color:{C2};font-size:12px;font-weight:800;letter-spacing:1px;padding:5px 10px">SAVE 37%</div></div>
<div style="height:404px;background:#fff url({P(img) if img.endswith('_ai.jpg') else PR(img)}) center/cover no-repeat;border:1px solid #e3d6c4"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;padding:18px 4px 0;gap:16px">
<div><div class="serif it" style="font-size:30px;line-height:1.05;color:{K2}">Best-Selling Gift Box</div>
<div style="font-size:12.5px;font-weight:800;letter-spacing:2px;color:{K2b};margin-top:4px">{name.upper()}</div>
<div style="font-size:13.5px;color:#5b4540;margin-top:6px">Reed diffuser, natural wax candle &amp; room mist, gift-boxed.</div></div>
<div style="text-align:right;flex:none"><div class="serif" style="font-size:40px;font-weight:700;color:{K2};line-height:1">£23.99</div><div style="font-size:14px;color:#9b8a84">was <s>£37.99</s></div></div></div>
<div style="padding:16px 4px 0">{pill2('Shop the gift box', K2, C2)}</div></div></div>'''

pages['bundle_d2_AM'] = bundle2AM()
pages['box_d2_AM'] = box2AM('Pure Lavender', 'box_lavender_ai.jpg')
pages['deals_d2_AM'] = deals(2, BG2, C2, C2, G2, G2, K2,
    'font-family:Cardo,Georgia,serif;font-style:italic;font-size:54px;line-height:1', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Wild Mint &amp; Sicilian Lemon Reed Diffuser Refill (100ml)', pill2("Shop today’s deal", K2, C2), thumb='refill_wildmint.jpg', stack=True,
    price=f'<div style="margin-top:4px"><span class="serif" style="font-size:28px;font-weight:700;color:{K2}">£9.49</span> <span style="font-size:13px;color:#8d7f79">was <s>£17.99</s></span> <span style="display:inline-block;background:{K2};color:{C2};font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">47% OFF</span></div>')

# ================= WEDNESDAY PM upgrades (same treatment as AM, evening variants)
pages['gift_d2_PM'] = gift_orn(2, 'PM', 'boxed diffuser', 'FREEDIFF', 'diffuser_only.jpg', '50% 88%', 'cover', K2b, K2, '#2A0710', 23)
pages['hero_d2_PM_A'] = moody('ai_festive_PM_A.jpg', '50% 60%', 'cover', 'DAY 2 · FINAL HOURS', 'Cosy nights,<br>beautifully scented', 'Save up to £89.91 · diffusers from £9.99 each', 'Shop bundles')
pages['hero_d2_PM_B'] = moody('ai_festive_PM_B.jpg', '50% 60%', 'cover', 'DAY 2 · HOSTING THIS CHRISTMAS?', 'Set the table.<br>Scent the room.', 'From £9.99 a diffuser when you bundle', 'Build your bundle')
pages['bundle_d2_PM'] = bundle2AM('★ FINAL HOURS · BUNDLE &amp; SAVE ★', 'TONIGHT’S MAIN OFFER · ENDS MIDNIGHT', 'xmas_boxes_warm.jpg', '50% 55%')
pages['box_d2_PM'] = box2AM('Pure Lavender', 'box_lavender_ai.jpg', 'ALSO TONIGHT · GIFT BOX DEAL')
pages['deals_d2_PM'] = deals(2, BG2, C2, C2, G2, G2, K2,
    'font-family:Cardo,Georgia,serif;font-style:italic;font-size:54px;line-height:1', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Wild Mint &amp; Sicilian Lemon Reed Diffuser Refill (100ml)', pill2("Shop tonight’s deal", K2, C2), thumb='refill_wildmint.jpg', stack=True, tag='FINAL HOURS',
    price=f'<div style="margin-top:4px"><span class="serif" style="font-size:28px;font-weight:700;color:{K2}">£9.49</span> <span style="font-size:13px;color:#8d7f79">was <s>£17.99</s></span> <span style="display:inline-block;background:{K2};color:{C2};font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">47% OFF</span></div>')

# ================= WEDNESDAY PM · own "evening edit" layout (cream + burgundy + gold, lighter than AM)
PMC = '#F6EEE3'   # cream page
def heroPM(photo, pos, eb, head, sub, link):
    return f'''<div style="background:{PMC};padding:34px 34px 40px;text-align:center;position:relative">
<div style="position:relative;height:600px;background:#1a1410 url({P(photo)}) {pos}/cover no-repeat;box-shadow:0 0 0 1px {G2},0 0 0 8px {PMC},0 0 0 9px {G2}">
<div style="position:absolute;top:18px;left:18px;background:{K2};color:{C2};font-size:10.5px;font-weight:800;letter-spacing:2.5px;padding:7px 12px">{eb}</div></div>
<div style="color:{G2};font-size:18px;letter-spacing:10px;margin:30px 0 4px">✦ ✦ ✦</div>
<div class="serif it" style="font-size:48px;line-height:1.05;color:{K2}">{head}</div>
<div style="font-size:15px;color:#5b4540;margin:12px 0 22px">{sub}</div>
{pill2(link, K2, C2)}</div>'''

def bundlePM():
    def row(n, sv, note, best=False):
        return f'''<div style="display:flex;align-items:center;gap:14px;background:{'#fff' if best else PMC};border:{'2px solid '+G2 if best else '1px solid #e2d3bf'};padding:14px 16px;position:relative">
{f'<div style="position:absolute;top:-11px;right:14px;background:{G2};color:{K2};font-size:9.5px;font-weight:800;letter-spacing:1.5px;padding:4px 10px">BEST VALUE</div>' if best else ''}
<div class="serif" style="font-size:46px;font-weight:700;color:{K2};width:62px;text-align:center;line-height:1">{n}</div>
<div style="flex:1"><div style="font-size:11px;font-weight:800;letter-spacing:1.5px;color:{K2b}">DIFFUSERS</div><div style="font-size:12.5px;color:#6b5650;margin-top:2px">{note}</div></div>
<div style="background:{K2};color:{C2};font-size:14px;font-weight:800;padding:8px 10px;white-space:nowrap">{sv}</div></div>'''
    return f'''<div style="background:{PMC};padding:8px 34px 40px">
<div style="border-top:1px solid {G2};padding-top:30px;text-align:center">
<div style="font-size:11.5px;font-weight:800;letter-spacing:3px;color:{K2b}">TONIGHT’S MAIN OFFER · ENDS MIDNIGHT</div>
<div class="serif" style="font-size:44px;line-height:1.05;color:{K2};margin:8px 0 4px">Bundle up &amp; save<br><span class="it" style="color:{K2b}">up to £89.91</span></div></div>
<div style="display:flex;gap:18px;margin-top:26px;align-items:stretch">
<div style="width:200px;flex:none;background:url({P('xmas_boxes_warm.jpg')}) 50% 50%/cover no-repeat;box-shadow:0 0 0 1px {G2}"></div>
<div style="flex:1;display:flex;flex-direction:column;gap:14px">{row('3','SAVE £21','Mix &amp; match any scents')}{row('6','SAVE £48','Scent every room')}{row('10','SAVE £89.91','Just £9.99 each',True)}</div></div>
<div style="display:flex;justify-content:center;gap:18px;margin-top:22px;font-size:12px;color:#5b4540;font-weight:600;white-space:nowrap">
<span>✓ Lasts up to 12 weeks</span><span>✓ FREE diffuser · FREEDIFF</span><span><span style="color:{G2}">★★★★★</span> 350,000+ reviews</span></div>
<div style="text-align:center;margin-top:22px">{pill2('Build my bundle &amp; save →', K2, C2)}</div></div>'''

def boxPM(name, img):
    return f'''<div style="background:{BG2};padding:34px 30px;position:relative;overflow:hidden">{snow(40,909,'rgba(255,255,255,.25)',2,500)}
<div style="display:flex;background:{C2};position:relative;box-shadow:0 0 0 2px {G2}">
<div style="width:300px;flex:none;background:url({P(img)}) 50% 50%/cover no-repeat"></div>
<div style="flex:1;padding:26px 22px">
<div style="display:inline-block;background:{K2};color:{C2};font-size:11px;font-weight:800;letter-spacing:1px;padding:5px 9px">SAVE 37%</div>
<div style="font-size:10.5px;font-weight:800;letter-spacing:2.5px;color:{K2b};margin-top:14px">ALSO TONIGHT</div>
<div class="serif it" style="font-size:30px;line-height:1.05;color:{K2};margin-top:4px">Best-Selling<br>Gift Box</div>
<div style="font-size:12px;font-weight:800;letter-spacing:2px;color:{K2b};margin-top:8px">{name.upper()}</div>
<div style="font-size:13px;color:#5b4540;margin-top:8px;line-height:1.45">Reed diffuser, natural wax candle &amp; room mist, beautifully gift-boxed.</div>
<div style="margin-top:14px"><span class="serif" style="font-size:38px;font-weight:700;color:{K2}">£23.99</span> <span style="font-size:14px;color:#9b8a84">was <s>£37.99</s></span></div>
<div style="margin-top:14px;white-space:nowrap">{pill2('Shop gift box', K2, C2)}</div></div></div></div>'''

pages['hero_d2_PM_A'] = heroPM('ai_festive_PM_A.jpg', '50% 72%', 'DAY 2 · FINAL HOURS', 'Cosy nights,<br>beautifully scented', 'Save up to £89.91 · diffusers from £9.99 each', 'Shop bundles')
pages['hero_d2_PM_B'] = heroPM('ai_festive_PM_B.jpg', '50% 70%', 'DAY 2 · HOSTING THIS CHRISTMAS?', 'Set the table.<br>Scent the room.', 'From £9.99 a diffuser when you bundle', 'Build your bundle')
pages['bundle_d2_PM'] = bundlePM()
pages['box_d2_PM'] = boxPM('Pure Lavender', 'box_lavender_portrait_ai.jpg')

# ================= THURSDAY AM upgrades · bright red, pine green & cream (collage spirit)
def hero3AM(photo, pos, eb, head, sub, link):
    return f'''<div style="background:{G3};padding:34px 30px 0;position:relative;overflow:hidden">{snow(50,313,'rgba(255,255,255,.35)',2.2,900)}
<div style="text-align:center;color:{C3};position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3.5px;opacity:.9">{eb}</div>
<div class="serif it" style="font-size:46px;line-height:1.05;margin:10px 0 8px">{head}</div>
<div style="font-size:14.5px;opacity:.92">{sub}</div></div>
<div style="position:relative;margin:24px 0 0;height:560px;background:#fff url({P(photo)}) {pos}/cover no-repeat;border:8px solid {C3};border-bottom:0">
<div style="position:absolute;left:50%;bottom:26px;transform:translateX(-50%)">{btn3(link, R3)}</div>
<div style="position:absolute;top:18px;right:18px;width:96px;height:96px;border-radius:50%;background:{R3};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg);box-shadow:0 6px 16px rgba(0,0,0,.25)">
<div style="font-size:10px;font-weight:800;letter-spacing:1.5px">FROM</div><div class="serif" style="font-size:30px;font-weight:700;line-height:1">£9.99</div><div style="font-size:9.5px;font-weight:800;letter-spacing:1.5px">EACH</div></div></div></div>'''

def bundle3AM():
    def card(n, off, note, bg, best=False):
        rib = f'<div style="position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:#F2C94C;color:#3a1a12;font-size:10px;font-weight:900;letter-spacing:1.5px;padding:5px 12px;white-space:nowrap;border-radius:3px">★ BEST VALUE ★</div>' if best else ''
        return f'''<div style="position:relative;flex:1;background:{bg};color:#fff;text-align:center;padding:24px 8px 18px;border-radius:6px;{'transform:scale(1.07);box-shadow:0 10px 24px rgba(0,0,0,.22)' if best else 'box-shadow:0 4px 12px rgba(0,0,0,.12)'}">{rib}
<div style="width:14px;height:14px;border-radius:50%;background:{C3};margin:0 auto 8px"></div>
<div style="font-size:12px;font-weight:800;letter-spacing:1.5px;opacity:.9">{n} DIFFUSERS</div>
<div style="font-size:15px;font-weight:700;margin-top:10px;opacity:.9">SAVE</div>
<div style="font-size:44px;font-weight:900;letter-spacing:-1.5px;line-height:1">{off}</div>
<div style="font-size:12px;margin-top:8px;font-weight:600;min-height:15px">{note}</div></div>'''
    ticks = ''.join(f'<div style="display:flex;align-items:center;gap:8px"><span style="width:20px;height:20px;border-radius:50%;background:{G3};color:#fff;font-size:12px;font-weight:900;display:inline-flex;align-items:center;justify-content:center">✓</span>{t}</div>' for t in ['Mix &amp; match any scents', 'Each lasts up to 12 weeks', 'FREE candle · FREEFLAME'])
    return f'''<div style="background:{C3};padding:0 0 36px;position:relative">
<div style="background:{R3};color:#fff;text-align:center;font-size:12px;font-weight:800;letter-spacing:3px;padding:11px 0">TODAY ONLY · BUNDLE &amp; SAVE · ENDS MIDNIGHT</div>
<div style="text-align:center;padding:30px 30px 0">
<div style="font-size:12px;font-weight:800;letter-spacing:3px;color:{G3}">TODAY’S MAIN OFFER</div>
<div style="font-size:60px;font-weight:900;letter-spacing:-2.5px;line-height:.98;color:{R3};margin:8px 0 6px">SAVE UP TO £89.91</div>
<div class="serif it" style="font-size:24px;color:{G3}">on diffuser bundles – from just £9.99 each</div></div>
<div style="display:flex;gap:14px;padding:34px 30px 0">{card('3','£21','',G3)}{card('6','£48','',R3)}{card('10','£89.91','just £9.99 each',G3,True)}</div>
<div style="position:relative;margin:30px 30px 0;height:230px;background:url({P('xmas_boxes.jpg')}) 50% 55%/cover no-repeat;border:6px solid #fff;box-shadow:0 6px 18px rgba(0,0,0,.14);transform:rotate(-1deg)"></div>
<div style="display:flex;justify-content:space-between;gap:10px;padding:24px 30px 0;color:#2A1A17;font-size:13px;font-weight:600">{ticks}</div>
<div style="text-align:center;margin-top:24px"><div style="display:inline-block;background:{R3};color:#fff;font-weight:800;font-size:15px;letter-spacing:1.8px;padding:18px 46px;border-radius:4px;box-shadow:0 8px 18px rgba(176,30,42,.35)">BUILD MY BUNDLE &amp; SAVE →</div>
<div style="color:#2A1A17;font-size:12.5px;margin-top:12px"><span style="color:{R3};letter-spacing:2px">★★★★★</span> &nbsp;350,000+ five-star reviews</div></div></div>'''

def box3AM(name, img):
    return f'''<div style="background:{G3};padding:30px 30px 34px;position:relative;overflow:hidden">{snow(30,323,'rgba(255,255,255,.3)',2,700)}
<div style="background:#fff;padding:18px 18px 24px;position:relative;border-radius:4px">
<div style="display:flex;justify-content:space-between;align-items:center;padding:0 4px 12px">
<div style="font-size:11px;font-weight:800;letter-spacing:2.5px;color:{G3}">ALSO TODAY · GIFT BOX DEAL</div>
<div style="background:{R3};color:#fff;font-size:12px;font-weight:800;letter-spacing:1px;padding:5px 10px">SAVE 37%</div></div>
<div style="height:404px;background:#fff url({P(img)}) center/cover no-repeat"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;padding:18px 4px 0;gap:16px">
<div><div class="serif it" style="font-size:30px;line-height:1.05;color:{R3}">Best-Selling Gift Box</div>
<div style="font-size:12.5px;font-weight:800;letter-spacing:2px;color:{G3};margin-top:4px">{name.upper()}</div>
<div style="font-size:13.5px;color:#5b4540;margin-top:6px">Reed diffuser, natural wax candle &amp; room mist, gift-boxed.</div></div>
<div style="text-align:right;flex:none"><div style="font-size:40px;font-weight:900;letter-spacing:-1px;color:{R3};line-height:1">£23.99</div><div style="font-size:14px;color:#9b8a84">was <s>£37.99</s></div></div></div>
<div style="padding:16px 4px 0">{btn3('Shop the gift box', R3)}</div></div></div>'''

pages['hero_d3_AM_A'] = hero3AM('ai_thu_A.jpg', '50% 70%', 'THE 12 DAYS OF CHRISTMAS · DAY 3', 'Deck the halls<br>(and scent them too)', 'Diffusers from £9.99 each when you bundle', 'Build my bundle')
pages['hero_d3_AM_B'] = hero3AM('ai_thu_B.jpg', '50% 70%', 'DAY 3 · COMING HOME FOR CHRISTMAS', 'The scent that says<br>“welcome home”', 'Bundle one for every room from £9.99 each', 'Shop bundles')
pages['bundle_d3_AM'] = bundle3AM()
pages['box_d3_AM'] = box3AM('Cardamom &amp; Nutmeg', 'box_cardamom_ai.jpg')
pages['deals_d3_AM'] = deals(3, R3, C3, '#fff', 'rgba(255,255,255,.85)', G3, '#fff',
    'font-weight:900;font-size:58px;letter-spacing:-2.5px;line-height:.95;text-transform:uppercase', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Bergamot &amp; Lemon Reed Diffuser Refill (100ml)', btn3("Shop today’s deal", G3), thumb='refill_bergamot.jpg', stack=True,
    price=f'<div style="margin-top:4px"><span style="font-size:26px;font-weight:900;color:{R3}">£10.49</span> <span style="font-size:13px;color:#7d726c">was <s>£17.99</s></span> <span style="display:inline-block;background:{R3};color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;padding:3px 7px;margin-left:4px">42% OFF</span></div>')
