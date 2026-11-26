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
def deals(day, bg, panel, ink, acc, hot, hot_fg, head_css, sub_css, today_line, btn):
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
<div><div style="font-size:11px;font-weight:800;letter-spacing:2px;color:{hot}">DAY {day} · TODAY ONLY</div>
<div style="font-size:19px;font-weight:800;line-height:1.25;color:#2A1A17;margin-top:4px">{today_line}</div>
<div style="font-size:12.5px;color:#5c4c47;margin-top:6px">{nxt}</div></div>
<div style="flex:none">{btn}</div></div></div>'''

pages['deals_d1'] = deals(1, R1, C1, C1, 'rgba(242,235,223,.9)', RED1, '#fff',
    'font-size:54px;font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-2px;line-height:.95', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME', btn1("Shop today’s deal", RED1))
pages['deals_d2'] = deals(2, BG2, C2, C2, G2, G2, K2,
    'font-family:Cardo,Georgia,serif;font-style:italic;font-size:54px;line-height:1', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE boxed diffuser with code FREEDIFF', pill2("Shop today’s deal", K2, C2))
pages['deals_d3'] = deals(3, R3, C3, '#fff', 'rgba(255,255,255,.85)', G3, '#fff',
    'font-weight:900;font-size:58px;letter-spacing:-2.5px;line-height:.95;text-transform:uppercase', 'font-size:15px;line-height:1.5;max-width:470px;margin:0 auto',
    'Diffuser bundles from £9.99 each + a FREE candle with code FREEFLAME', btn3("Shop today’s deal", G3))
