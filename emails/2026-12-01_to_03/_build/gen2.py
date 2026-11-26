# v2: three distinct day themes inspired by Alessi editorial (D1), deep-red ornament templates (D2), collage/wish-list templates (D3)
import os, random, math
S = '/tmp/claude-0/-home-user-ruby/b44f2fb9-6eed-5680-a384-23171670d6e5/scratchpad'
OUT = f'{S}/render2'; os.makedirs(OUT, exist_ok=True)
def P(n): return f'file://{S}/src/{n}'
def PR(n): return f'file://{S}/prod/{n}'
INK = '#2A1A17'
# Day 1 editorial
C1 = '#F2EBDF'; R1 = '#C3242C'
# Day 2 ornaments
K2 = '#7A0F1B'; K2b = '#A31B29'; G2 = '#D6B46E'; C2 = '#F7EEE2'
# Day 3 collage
R3 = '#B01E2A'; C3 = '#F6F0E7'; B3 = '#EBDCD2'

BASE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&display=block" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0;padding:0}
body{width:600px;font-family:Inter,Arial,sans-serif;color:#2A1A17;-webkit-font-smoothing:antialiased}
#cap{width:600px;position:relative;overflow:hidden}
.serif{font-family:Cardo,Georgia,serif}.it{font-style:italic}
.ph{background-repeat:no-repeat;background-size:cover}
.snow{position:absolute;inset:0;pointer-events:none}
</style></head><body><div id="cap">%s</div></body></html>"""

def snow(n, seed, color, maxr=2.4, h=800):
    r = random.Random(seed)
    d = ''.join(f'<circle cx="{r.uniform(0,600):.0f}" cy="{r.uniform(0,h):.0f}" r="{r.uniform(.7,maxr):.1f}" fill="{color}"/>' for _ in range(n))
    return f'<svg class="snow" width="600" height="{h}">{d}</svg>'
def spark(x, y, s, c):
    return f'<path d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s}Z" fill="{c}"/>'
def ph(photo, pos, w, h, extra=''):
    return f'<div class="ph" style="width:{w}px;height:{h}px;background-image:url({P(photo)});background-position:{pos};{extra}"></div>'

pages = {}

# =============================================================== DAY 1 · EDITORIAL
def marquee1(text, bg, fg, h=58, size=40, off=-30):
    t = (text + '  ·  ') * 4
    return f'<div style="height:{h}px;background:{bg};overflow:hidden;position:relative;border-top:2px solid {fg};border-bottom:2px solid {fg}"><div style="position:absolute;left:{off}px;top:50%;transform:translateY(-52%);white-space:nowrap;font-weight:900;font-style:italic;font-size:{size}px;letter-spacing:-1px;color:{fg};text-transform:uppercase">{t}</div></div>'

def btn1(label, bg=R1, fg='#fff'):
    return f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:700;font-size:13px;letter-spacing:.3px;padding:13px 26px">{label}</div>'

pages['strip_d1'] = f'<div style="background:{C1};padding:6px 0">{marquee1("The 12 days of Christmas · Day 1 of 12", C1, R1, 52, 34, -18)}</div>'

def gift1(slot):
    eb = 'Day 1 gift · today only' if slot == 'AM' else 'Day 1 gift · final hours'
    h = 'A FREE candle<br>with every order' if slot == 'AM' else 'Last call for your<br>FREE candle'
    return f'''<div style="height:260px;background:{C1};display:flex;border-bottom:2px solid {R1}">
<div style="width:318px;padding:30px 26px 0 30px">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;text-transform:uppercase;color:{R1}">{eb}</div>
<div style="font-size:30px;line-height:1.08;font-weight:800;color:{R1};margin:10px 0 14px;letter-spacing:-.5px">{h}</div>
<div style="display:inline-block;border:1.5px solid {R1};padding:8px 14px;font-size:12px;font-weight:700;letter-spacing:2px;color:{R1}">CODE&nbsp; FREEFLAME</div>
<div style="margin-top:14px">{btn1('Claim your FREE gift')}</div></div>
<div style="flex:1;border-left:2px solid {R1}"><div style="width:280px;height:258px;background:url({P('candle_only.jpg')}) center/cover no-repeat"></div></div></div>'''
pages['gift_d1_AM'] = gift1('AM'); pages['gift_d1_PM'] = gift1('PM')

def hero1A(photo, pos, eb, head, sub, cta):
    return f'''<div style="background:{C1}">{ph(photo,pos,600,470)}
<div style="padding:28px 34px 30px;border-top:2px solid {R1}">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;text-transform:uppercase;color:{R1}">{eb}</div>
<div style="font-size:34px;line-height:1.06;font-weight:800;color:{R1};margin:10px 0 12px;letter-spacing:-.8px">{head}</div>
<div style="font-size:14.5px;line-height:1.5;color:{INK};max-width:470px">{sub}</div>
<div style="margin-top:18px">{btn1(cta)}</div></div>
{marquee1("From £9.99 each · Save up to £89.91", R1, C1, 46, 26, -60)}</div>'''

def hero1B(photo, pos, big, sub, cta):
    return f'''<div style="background:{C1}">
<div style="padding:30px 30px 22px"><div style="font-size:46px;line-height:.98;font-weight:900;font-style:italic;color:{R1};letter-spacing:-1.5px;text-transform:uppercase">{big}</div></div>
{ph(photo,pos,600,440,'border-top:2px solid '+R1+';border-bottom:2px solid '+R1)}
<div style="padding:22px 30px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px">
<div style="font-size:14.5px;line-height:1.5;color:{INK};max-width:330px">{sub}</div>{btn1(cta)}</div></div>'''

def advent1():
    cells = ''
    for i in range(12):
        n = i + 1
        if n == 1:
            cells += f'''<div style="position:relative;height:104px;background:{C1};border:2px solid {R1}">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div class="serif it" style="font-size:15px;color:{R1};text-align:center">a treat<br>inside</div></div>
<div style="position:absolute;inset:-2px;background:{R1};transform-origin:left center;transform:perspective(500px) rotateY(-38deg);display:flex;align-items:center;justify-content:center;box-shadow:6px 0 12px rgba(0,0,0,.25)">
<div style="font-weight:900;font-style:italic;font-size:54px;color:{C1}">1</div></div></div>'''
        else:
            cells += f'<div style="height:104px;border:2px solid {R1};display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:40px;color:{R1};opacity:{0.9 if n<4 else 0.55}">{n}</div>'
    return f'''<div style="background:{C1};padding:30px 30px 30px">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;text-transform:uppercase;color:{R1}">The 12 days of Christmas</div>
<div style="font-size:40px;line-height:1;font-weight:900;font-style:italic;color:{R1};margin:8px 0 20px;letter-spacing:-1px;text-transform:uppercase">Door No. 1 is open</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px">{cells}</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:20px">
<div style="font-size:14.5px;line-height:1.5;max-width:330px">A new door every day until the 12th. Tap to open today’s door – every door hides a festive treat.</div>{btn1('Open door 1')}</div></div>'''

def cracker1():
    return f'''<div style="background:{C1};padding:30px 30px 30px;position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;text-transform:uppercase;color:{R1}">Day 1 · after-work treat</div>
<div style="font-size:40px;line-height:1;font-weight:900;font-style:italic;color:{R1};margin:8px 0 6px;letter-spacing:-1px;text-transform:uppercase">Pull the cracker</div>
<div class="serif it" style="font-size:20px;color:{R1}">…every one holds a prize</div>
<svg width="540" height="300" style="display:block;margin:10px 0 0"><g transform="translate(270,150) rotate(-10)">
<g transform="translate(-24,0)"><path d="M-200 -42 L-130 -42 L-104 -20 L-40 -46 L0 -46 L0 46 L-40 46 L-104 20 L-130 42 L-200 42 L-222 0Z" fill="{R1}"/>
{''.join(f'<rect x="{-190+i*36}" y="-46" width="12" height="92" fill="{C1}" opacity=".9"/>' for i in range(5))}</g>
<g transform="translate(24,0)"><path d="M200 -42 L130 -42 L104 -20 L40 -46 L0 -46 L0 46 L40 46 L104 20 L130 42 L200 42 L222 0Z" fill="{R1}"/>
{''.join(f'<rect x="{30+i*36}" y="-46" width="12" height="92" fill="{C1}" opacity=".9"/>' for i in range(5))}</g>
<g stroke="{R1}" stroke-width="4" stroke-linecap="round"><path d="M-10 -62 L-18 -90"/><path d="M4 -66 L6 -98"/><path d="M16 -60 L30 -86"/><path d="M-10 62 L-20 88"/><path d="M14 62 L26 88"/></g>
<rect x="-62" y="-26" width="124" height="52" fill="{C1}" stroke="{R1}" stroke-width="3"/><text x="0" y="12" text-anchor="middle" font-family="Inter" font-style="italic" font-weight="900" font-size="32" fill="{R1}">SNAP!</text></g></svg>
<div style="display:flex;justify-content:space-between;align-items:center;gap:20px;border-top:2px solid {R1};padding-top:18px">
<div style="font-size:14.5px;line-height:1.5;max-width:330px">Tap to pull it and see what falls out. Everyone’s a winner tonight.</div>{btn1('Pull to reveal')}</div></div>'''

def box1(day, name, img):
    return f'''<div style="background:{C1};border-top:2px solid {R1}">
<div style="display:flex;justify-content:space-between;align-items:baseline;padding:22px 30px 16px">
<div style="font-size:28px;font-weight:900;font-style:italic;color:{R1};letter-spacing:-.8px;text-transform:uppercase">Tuesday’s gift box</div>
<div style="font-size:11px;font-weight:700;letter-spacing:2.4px;color:{R1}">DAY 1 DEAL</div></div>
<div style="display:flex;border-top:2px solid {R1};border-bottom:2px solid {R1};position:relative">
<div style="width:299px;height:380px;background:#fff url({PR(img)}) center 55%/150% no-repeat;border-right:2px solid {R1}"></div>
{ph('p48_bsgb.jpg','50% 62%',299,380)}
<div style="position:absolute;left:250px;top:24px;width:96px;height:96px;border-radius:50%;background:{R1};color:{C1};display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 0 4px {C1}">
<div style="font-size:11px;font-weight:700;letter-spacing:1.5px">SAVE</div><div style="font-size:32px;font-weight:900;font-style:italic;line-height:1">37%</div></div></div>
<div style="padding:22px 30px 28px">
<div style="font-size:22px;font-weight:800;color:{R1};letter-spacing:-.3px">Best-Selling Gift Box – {name}</div>
<div style="font-size:14.5px;line-height:1.5;margin:6px 0 12px">Reed diffuser, natural wax candle and room mist, beautifully boxed and ready to give.</div>
<div style="display:flex;justify-content:space-between;align-items:center">
<div><span style="font-size:36px;font-weight:900;font-style:italic;color:{R1}">£23.99</span> <span style="font-size:15px;color:#7d726c">was <s>£37.99</s></span></div>{btn1('Shop the gift box')}</div></div></div>'''

pages['box_d1'] = box1(1, 'Jasmine &amp; Rosewood', 'box_jasmine.jpg')
pages['hero_d1_AM_A'] = hero1A('xmas_boxes_warm.jpg', '62% 80%', 'The 12 days of Christmas · Day 1', 'Christmas scent for every room, from £9.99', 'Bundle 10 reed diffusers and save £89.91. Mix and match any scents – one for the hallway, the lounge, the guest room and beyond.', 'Build your bundle')
pages['hero_d1_AM_B'] = hero1B('cover2.jpg', '50% 64%', 'It starts the<br>moment they<br>walk in…', 'Guests notice the second they walk in. Make every room Christmas-ready.', 'See how')
pages['hero_d1_AM_C'] = advent1()
pages['hero_d1_PM_A'] = hero1A('bundle_back.jpg', '50% 58%', 'Day 1 · Bundle &amp; save', 'One for every room. Save up to £89.91', 'Reed diffusers from £9.99 each when you bundle, plus a FREE candle with code FREEFLAME.', 'Shop bundles')
pages['hero_d1_PM_B'] = hero1B('embrace.jpg', '62% 55%', 'The house<br>everyone talks<br>about', 'Strong, never overpowering. One diffuser, every room scented.', 'Discover more')
pages['hero_d1_PM_C'] = cracker1()

# =============================================================== DAY 2 · RED ORNAMENTS
def ornament(cx, top, d, photo, pos, size='cover', string=True, ring=G2, label=None):
    cap = f'<div style="position:absolute;left:{cx-14}px;top:{top-14}px;width:28px;height:18px;background:linear-gradient({G2},#9C7A35);border-radius:4px 4px 2px 2px"></div>'
    st = f'<div style="position:absolute;left:{cx-1}px;top:0;width:2px;height:{top-12}px;background:{G2}"></div>' if string else ''
    inner = f'background:url({P(photo)}) {pos}/{size} no-repeat' if photo else f'background:{C2}'
    lab = f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">{label}</div>' if label else ''
    return f'{st}{cap}<div style="position:absolute;left:{cx-d/2}px;top:{top}px;width:{d}px;height:{d}px;border-radius:50%;{inner};box-shadow:0 0 0 5px {ring},0 16px 30px rgba(0,0,0,.35)">{lab}</div>'

def pill2(label, bg=C2, fg=K2):
    return f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:700;font-size:13px;letter-spacing:1.6px;text-transform:uppercase;padding:14px 30px;border-radius:40px">{label}</div>'
def ticket2(code):
    return f'''<div style="position:relative;display:inline-block;background:{C2};color:{K2};padding:11px 30px;font-weight:700;letter-spacing:2.5px;font-size:13px">
<span style="position:absolute;left:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:{K2};transform:translateY(-50%)"></span>
<span style="position:absolute;right:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:{K2};transform:translateY(-50%)"></span>
<span style="border-left:1.5px dashed {K2};padding-left:14px;margin-left:-6px">CODE&nbsp; {code}</span></div>'''
BG2 = f'radial-gradient(ellipse at 50% 30%, {K2b} 0%, {K2} 60%, #4E0911 100%)'

pages['strip_d2'] = f'''<div style="height:56px;background:{K2};position:relative;display:flex;align-items:center;justify-content:center;gap:18px;border-bottom:1px solid {G2}">
<svg width="600" height="56" style="position:absolute;inset:0">{spark(40,28,7,G2)}{spark(560,28,7,G2)}{''.join(f'<circle cx="{70+i*12}" cy="28" r="1.6" fill="{G2}"/>' for i in range(8))}{''.join(f'<circle cx="{446+i*12}" cy="28" r="1.6" fill="{G2}"/>' for i in range(8))}</svg>
<span class="serif it" style="color:{C2};font-size:22px">The 12 Days of Christmas</span>
<span style="width:34px;height:34px;border-radius:50%;border:1.5px solid {G2};color:{G2};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px">2</span></div>'''

def gift2(slot):
    head = 'Your Day 2 gift' if slot == 'AM' else 'Final hours…'
    sub = 'A FREE BOXED DIFFUSER WITH EVERY ORDER' if slot == 'AM' else 'YOUR FREE BOXED DIFFUSER ENDS TODAY'
    return f'''<div style="height:280px;background:{BG2};position:relative;overflow:hidden">{snow(40,22 if slot=='AM' else 23,'rgba(255,255,255,.35)',2,280)}
{ornament(150, 60, 180, 'p49_diffbox.jpg', '40% 58%', '300%')}
<div style="position:absolute;left:150px;top:44px;width:44px;height:24px;transform:translateX(-50%)"><svg width="44" height="24"><path d="M22 12 C8 -4 0 10 22 12 C44 10 36 -4 22 12Z" fill="{G2}"/></svg></div>
<div style="position:absolute;left:290px;right:24px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:flex-start">
<div class="serif it" style="color:{C2};font-size:38px;line-height:1">{head}</div>
<div style="color:{G2};font-size:10.5px;font-weight:700;letter-spacing:1.6px;margin:10px 0 16px">{sub}</div>
{ticket2('FREEDIFF')}<div style="margin-top:14px">{pill2('Claim your gift →')}</div></div></div>'''
pages['gift_d2_AM'] = gift2('AM'); pages['gift_d2_PM'] = gift2('PM')

def hero2A():
    return f'''<div style="height:760px;background:{BG2};position:relative;overflow:hidden">{snow(110,201,'rgba(255,255,255,.4)',2.2,760)}
{ornament(130, 90, 170, 'cover1.jpg', '62% 80%', '360%')}{ornament(300, 170, 200, 'bundle_back.jpg', '50% 55%', '280%')}{ornament(470, 70, 160, 'p49_diffbox.jpg', '42% 58%', '360%')}
<div style="position:absolute;left:418px;top:270px;width:110px;height:110px;border-radius:50%;background:{G2};color:{K2};display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg);box-shadow:0 8px 20px rgba(0,0,0,.3)">
<div style="font-size:11px;font-weight:700;letter-spacing:1.5px">FROM</div><div class="serif" style="font-size:34px;font-weight:700;line-height:1">£9.99</div><div style="font-size:10px;font-weight:700;letter-spacing:1px">EACH</div></div>
<div style="position:absolute;left:40px;right:40px;top:440px;text-align:center;color:{C2}">
<div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">THE 12 DAYS OF CHRISTMAS · DAY 2</div>
<div class="serif it" style="font-size:50px;line-height:1.02;margin:12px 0 14px">Fill every room<br>for Christmas</div>
<div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">Mix &amp; match 10 diffusers and save £89.91 – plus a FREE boxed diffuser with code FREEDIFF.</div>
<div style="margin-top:20px">{pill2('Build my bundle')}</div></div></div>'''

def hero2B(photo, pos, eb, head, sub, cta, arch=False):
    if arch:
        return f'''<div style="height:740px;background:{BG2};position:relative;overflow:hidden">{snow(80,233,'rgba(255,255,255,.35)',2,740)}
<div style="position:absolute;left:110px;top:40px;width:380px;height:440px;border-radius:190px 190px 0 0;background:url({P(photo)}) {pos}/cover no-repeat;box-shadow:0 0 0 6px {K2},0 0 0 8px {G2}"></div>
<div style="position:absolute;left:40px;right:40px;top:510px;text-align:center;color:{C2}">
<div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">{eb}</div>
<div class="serif it" style="font-size:42px;line-height:1.05;margin:10px 0 12px">{head}</div>
<div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">{sub}</div><div style="margin-top:18px">{pill2(cta)}</div></div></div>'''
    return f'''<div style="height:720px;position:relative;background:url({P(photo)}) {pos}/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(78,9,17,0) 40%,rgba(78,9,17,.7) 64%,rgba(78,9,17,.96) 100%)"></div>
<div style="position:absolute;inset:14px;border:1.5px solid {G2}"></div>{snow(70,244,'rgba(255,255,255,.55)',2.2,720)}
<div style="position:absolute;left:50px;right:50px;bottom:58px;text-align:center;color:{C2}">
<div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">{eb}</div>
<div class="serif it" style="font-size:52px;line-height:1.02;margin:12px 0 12px">{head}</div>
<div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.9)">{sub}</div><div style="margin-top:18px">{pill2(cta)}</div></div></div>'''

def globe2():
    fl = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".9"/>' for x,y,r in [(250,250,3),(330,230,2.5),(290,300,3.5),(360,290,2),(230,320,2.4),(310,200,2),(270,210,2.2),(350,330,3),(300,260,2)])
    return f'''<div style="height:740px;background:{BG2};position:relative;overflow:hidden">{snow(120,251,'rgba(255,255,255,.45)',2.2,740)}
<div style="position:absolute;top:44px;left:0;right:0;text-align:center;color:{C2}"><div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">DAY 2 · SHAKE IT UP</div>
<div class="serif it" style="font-size:46px;line-height:1.04;margin-top:10px">A gift is hiding<br>in the snow</div></div>
<svg width="600" height="400" style="position:absolute;left:0;top:190px"><defs><radialGradient id="g" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset=".7" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity=".4"/></radialGradient></defs>
<path d="M190 340 Q300 312 410 340 L430 382 L170 382Z" fill="{G2}"/><rect x="170" y="374" width="260" height="14" rx="4" fill="#9C7A35"/>
<circle cx="300" cy="230" r="125" fill="#3B0710"/><path d="M196 300 Q300 262 404 300 L404 340 L196 340Z" fill="#fff"/>
<g transform="translate(300,276)"><rect x="-30" y="-32" width="60" height="46" fill="{C2}"/><rect x="-32" y="-38" width="64" height="10" fill="{K2b}"/><rect x="-5" y="-38" width="10" height="52" fill="{G2}"/><path d="M0 -38 C-16 -60 -28 -42 0 -38 C28 -42 16 -60 0 -38Z" fill="{G2}"/></g>
{fl}<circle cx="300" cy="230" r="125" fill="url(#g)" stroke="{G2}" stroke-width="3"/>
<g stroke="{G2}" stroke-width="3" fill="none" stroke-linecap="round"><path d="M146 200 q-14 30 0 60"/><path d="M124 190 q-18 40 0 80"/><path d="M454 200 q14 30 0 60"/><path d="M476 190 q18 40 0 80"/></g></svg>
<div style="position:absolute;left:40px;right:40px;bottom:46px;text-align:center;color:{C2}"><div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">Tap to shake it. When the snow settles, your treat is revealed.</div><div style="margin-top:16px">{pill2('Shake to reveal')}</div></div></div>'''

def ladder2():
    lab = lambda n, s: f'<div style="font-size:10px;font-weight:700;letter-spacing:1.5px;color:{K2b}">BUNDLE OF</div><div class="serif" style="font-size:52px;line-height:.95;color:{K2};font-weight:700">{n}</div><div style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:{K2b}">{s}</div>'
    return f'''<div style="height:780px;background:{BG2};position:relative;overflow:hidden">{snow(110,261,'rgba(255,255,255,.4)',2.2,780)}
{ornament(120, 110, 150, None, '', label=lab('3','SAVE £21'))}{ornament(300, 190, 170, None, '', label=lab('6','SAVE £48'))}{ornament(480, 90, 190, None, '', label=lab('10','SAVE £89.91'))}
<div style="position:absolute;left:40px;right:40px;top:430px;text-align:center;color:{C2}">
<div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">DAY 2 · BUY MORE, SAVE MORE</div>
<div class="serif it" style="font-size:50px;line-height:1.02;margin:12px 0 14px">The more rooms,<br>the merrier</div>
<div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">Diffusers from £9.99 each in the 10-pack. Plus a FREE boxed diffuser with code FREEDIFF.</div>
<div style="margin-top:20px">{pill2('Pick my pack')}</div></div></div>'''

def peel2():
    return f'''<div style="height:740px;background:{BG2};position:relative;overflow:hidden">{snow(110,271,'rgba(255,255,255,.4)',2.2,740)}
<div style="position:absolute;top:44px;left:0;right:0;text-align:center;color:{C2}"><div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">DAY 2 · PEEL &amp; REVEAL</div>
<div class="serif it" style="font-size:46px;line-height:1.04;margin-top:10px">Peel back tonight’s<br>surprise</div></div>
<div style="position:absolute;left:150px;top:200px;width:300px;height:300px;border-radius:50%;background:{C2};box-shadow:0 18px 40px rgba(0,0,0,.4);overflow:hidden">
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding-right:90px;padding-bottom:90px">
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:{K2b}">EVERY ONE WINS</div><div class="serif it" style="font-size:64px;color:{K2};line-height:1">? ? ?</div></div>
<div style="position:absolute;right:-30px;bottom:-30px;width:190px;height:190px;background:{K2};"></div>
<div style="position:absolute;right:0;bottom:0;width:150px;height:150px;background:linear-gradient(135deg,{G2} 0%,#F1DCA6 45%,#B48E43 100%);border-top-left-radius:150px;box-shadow:-8px -8px 18px rgba(0,0,0,.25)"></div></div>
<div style="position:absolute;left:452px;top:508px;color:{G2};font-family:Cardo;font-style:italic;font-size:20px">↖ peel here</div>
<div style="position:absolute;left:40px;right:40px;bottom:46px;text-align:center;color:{C2}"><div style="font-size:15px;line-height:1.5;color:rgba(247,238,226,.88)">Tap to peel – your festive treat is waiting underneath.</div><div style="margin-top:16px">{pill2('Peel to reveal')}</div></div></div>'''

def box2(name, img):
    return f'''<div style="background:{BG2};padding:40px 34px 40px;position:relative;overflow:hidden">{snow(70,281,'rgba(255,255,255,.35)',2,900)}
<div style="text-align:center;color:{C2};position:relative"><div style="color:{G2};font-size:11.5px;font-weight:700;letter-spacing:3px">DAY 2 · GIFT OF THE DAY</div>
<div class="serif it" style="font-size:42px;line-height:1.05;margin:8px 0 24px">Wednesday’s gift to give</div></div>
<div style="background:{C2};border-radius:200px 200px 6px 6px;padding:26px 26px 30px;position:relative;text-align:center">
<div style="height:360px;border-radius:180px 180px 0 0;background:#fff url({PR(img)}) center 52%/112% no-repeat;box-shadow:0 0 0 1.5px {G2}"></div>
<div style="position:absolute;right:14px;top:150px;width:100px;height:100px;border-radius:50%;background:{K2};color:{C2};display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 0 4px {G2}">
<div style="font-size:11px;font-weight:700;letter-spacing:1.5px;color:{G2}">SAVE</div><div class="serif" style="font-size:34px;font-weight:700;line-height:1">37%</div></div>
<div class="serif it" style="font-size:30px;color:{K2};margin:22px 0 4px">Best-Selling Gift Box</div>
<div style="font-size:12px;font-weight:700;letter-spacing:2.5px;color:{K2b}">{name.upper()}</div>
<div style="font-size:14.5px;line-height:1.5;color:#5b4540;margin:10px 20px 12px">Reed diffuser, natural wax candle &amp; room mist – boxed with a ribbon and ready to give.</div>
<div style="font-size:16px;color:{K2}">Now <span class="serif" style="font-size:36px;font-weight:700">£23.99</span> <span style="color:#9b8a84">was <s>£37.99</s></span></div>
<div style="margin-top:14px">{pill2('Shop the gift box', K2, C2)}</div></div></div>'''

pages['box_d2'] = box2('Pure Lavender', 'box_lavender.jpg')
pages['hero_d2_AM_A'] = hero2A()
pages['hero_d2_AM_B'] = hero2B('p48_bsgb.jpg', '50% 55%', 'DAY 2 · READY FOR GUESTS?', '“What’s that<br>beautiful smell?”', 'The question every guest asks. Be the home people always comment on.', 'Find your scent')
pages['hero_d2_AM_C'] = globe2()
pages['hero_d2_PM_A'] = ladder2()
pages['hero_d2_PM_B'] = hero2B('p49_diffbox.jpg', '44% 55%', 'DAY 2 · AROUND THE CLOCK', 'Christmas in every room,<br>all day long', 'Our diffusers work 24/7 – no effort required. Lasts up to 12 weeks.', 'Shop diffusers', arch=True)
pages['hero_d2_PM_C'] = peel2()

# =============================================================== DAY 3 · COLLAGE / WISH LIST
def btn3(label, bg=R3, fg='#fff'):
    return f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:700;font-size:13px;letter-spacing:1.6px;text-transform:uppercase;padding:14px 28px;border-radius:3px">{label}</div>'
def tag3(top, bot, rot, bg=R3, fg='#fff', w=230):
    return f'''<div style="position:relative;width:{w}px;transform:rotate({rot}deg);background:{bg};color:{fg};padding:16px 20px 16px 44px;box-shadow:0 8px 18px rgba(0,0,0,.18);clip-path:polygon(22px 0,100% 0,100% 100%,22px 100%,0 50%)">
<span style="position:absolute;left:18px;top:50%;width:10px;height:10px;border-radius:50%;background:{C3};transform:translateY(-50%)"></span>
<div class="serif it" style="font-size:16px;opacity:.9">{top}</div><div style="font-weight:900;font-size:30px;letter-spacing:-.5px;line-height:1.05">{bot}</div></div>'''

pages['strip_d3'] = f'''<div style="height:56px;background:{C3};display:flex;align-items:center;justify-content:center;gap:16px;border-bottom:2px solid {R3}">
<span class="serif it" style="color:{R3};font-size:21px">The 12 days of</span>
<span style="background:{R3};color:#fff;font-weight:800;font-size:12px;letter-spacing:2.5px;padding:8px 16px;clip-path:polygon(8px 0,calc(100% - 8px) 0,100% 50%,calc(100% - 8px) 100%,8px 100%,0 50%)">DAY 3 OF 12</span>
<span class="serif it" style="color:{R3};font-size:21px">Christmas</span></div>'''

def gift3(slot):
    top = 'Day 3 treat · today only' if slot == 'AM' else 'Day 3 · final hours'
    return f'''<div style="height:270px;background:{R3};position:relative;overflow:hidden">{snow(30,31 if slot=='AM' else 32,'rgba(255,255,255,.25)',2,270)}
<div style="position:absolute;left:30px;top:26px;color:#fff">
<div class="serif it" style="font-size:20px">{top}</div>
<div style="font-weight:900;font-size:118px;line-height:.86;letter-spacing:-5px;margin:6px 0 4px">FREE</div>
<div style="font-size:13px;font-weight:700;letter-spacing:2.2px">CANDLE WITH EVERY ORDER</div>
<div style="margin-top:14px;display:inline-block;background:{C3};color:{R3};font-weight:800;letter-spacing:2.5px;font-size:13px;padding:9px 16px;border:1.5px dashed {R3};outline:1.5px solid {C3}">CODE FREEFLAME</div></div>
<div style="position:absolute;right:34px;top:34px;width:200px;height:200px;border-radius:50%;background:url({P('p49_candlebox.jpg')}) 70% 76%/360% no-repeat;box-shadow:0 0 0 6px {C3}"></div>
<div style="position:absolute;right:20px;top:24px;width:70px;height:70px;border-radius:50%;background:{C3};color:{R3};display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:11px;letter-spacing:1px;line-height:1.2;transform:rotate(12deg)">CLAIM<br>NOW →</div></div>'''
pages['gift_d3_AM'] = gift3('AM'); pages['gift_d3_PM'] = gift3('PM')

def collage3():
    tiles = [('xmas_boxes.jpg','64% 84%','360%'),('candle_fir.jpg','60% 55%','180%'),('cover1.jpg','62% 78%','400%'),
             ('embrace.jpg','58% 60%','300%'),None,('p49_diffbox.jpg','44% 58%','380%'),
             ('bundle_back.jpg','50% 55%','300%'),('p48_bsgb.jpg','50% 58%','260%'),('cover2.jpg','42% 72%','300%')]
    cells = ''
    for t in tiles:
        if t is None:
            cells += f'<div style="background:{C3};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="font-size:10.5px;font-weight:800;letter-spacing:2px;color:{R3}">DIFFUSERS FROM</div><div class="serif" style="font-size:58px;color:{R3};line-height:1;font-weight:700">£9.99</div><div class="serif it" style="font-size:16px;color:{R3}">when you bundle</div></div>'
        else:
            cells += f'<div style="background:url({P(t[0])}) {t[1]}/{t[2]} no-repeat"></div>'
    return f'''<div style="background:{R3};padding:30px 24px 30px">
<div style="text-align:center;color:#fff;margin-bottom:18px"><div style="font-size:11px;font-weight:700;letter-spacing:3px;opacity:.85">THE 12 DAYS OF CHRISTMAS · DAY 3</div>
<div class="serif it" style="font-size:46px;line-height:1.02;margin-top:8px">The Christmas host’s secret</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:176px;gap:6px">{cells}</div>
<div style="text-align:center;color:#fff;margin-top:20px"><div style="font-size:15px;line-height:1.5;opacity:.92">10 diffusers in any scents, save £89.91 – plus a FREE candle with code FREEFLAME.</div>
<div style="margin-top:16px">{btn3('Build my bundle', C3, R3)}</div></div></div>'''

def polaroids3():
    def pol(photo, pos, size, x, y, rot, cap):
        return f'<div style="position:absolute;left:{x}px;top:{y}px;width:220px;background:#fff;padding:12px 12px 34px;transform:rotate({rot}deg);box-shadow:0 10px 24px rgba(0,0,0,.18)"><div style="height:210px;background:url({P(photo)}) {pos}/{size} no-repeat"></div><div class="serif it" style="position:absolute;left:0;right:0;bottom:8px;text-align:center;font-size:15px;color:{R3}">{cap}</div></div>'
    return f'''<div style="height:660px;background:{C3};position:relative;overflow:hidden">
{pol('cover2.jpg','46% 70%','320%',30,50,-7,'the hallway')}{pol('embrace.jpg','60% 60%','260%',190,30,4,'the snug')}{pol('cover1.jpg','62% 78%','380%',350,70,-3,'the lounge')}
<div style="position:absolute;left:44px;right:44px;top:352px;text-align:center">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{R3}">DAY 3 · COMING HOME</div>
<div class="serif it" style="font-size:40px;line-height:1.08;color:{R3};margin:10px 0 12px">The scent that greets you before you’ve even taken your coat off.</div>
<div style="font-size:15px;line-height:1.5;color:{INK}">Fills the whole house, not just the room it’s in.</div>
<div style="margin-top:18px">{btn3('Discover more')}</div></div></div>'''

def presents3():
    def box(x, col, rib, lab):
        return f'''<g transform="translate({x},0)"><rect x="-62" y="40" width="124" height="110" fill="{col}"/><rect x="-70" y="16" width="140" height="30" fill="{col}" stroke="rgba(0,0,0,.12)"/>
<rect x="-9" y="16" width="18" height="134" fill="{rib}"/><path d="M0 16 C-30 -24 -54 4 0 16 C54 4 30 -24 0 16Z" fill="{rib}"/>
<text x="0" y="190" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="30" fill="{R3}">No. {lab}</text></g>'''
    return f'''<div style="height:740px;background:{C3};position:relative;overflow:hidden">
<div style="position:absolute;inset:16px;border:2px solid {R3}"></div>
<div style="position:absolute;top:50px;left:0;right:0;text-align:center"><div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{R3}">DAY 3 · PICK A PRESENT</div>
<div class="serif it" style="font-size:46px;line-height:1.04;color:{R3};margin-top:10px">Three presents.<br>One is yours.</div></div>
<svg width="600" height="300" style="position:absolute;left:0;top:250px"><g transform="translate(300,20) scale(1.1) translate(-300,0)">
{box(130,R3,'#E2C27A','1')}{box(300,'#fff',R3,'2')}{box(470,'#E2C27A',R3,'3')}</g></svg>
<div style="position:absolute;left:44px;right:44px;bottom:52px;text-align:center"><div style="font-size:15px;line-height:1.5">Every present hides a festive treat. Tap to pick yours and unwrap it.</div><div style="margin-top:16px">{btn3('Pick my present')}</div></div></div>'''

def tags3():
    return f'''<div style="height:720px;background:{C3};position:relative;overflow:hidden;display:flex">
<div style="width:300px;padding:44px 0 0 34px;position:relative">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{R3}">DAY 3 · FINAL HOURS</div>
<div class="serif it" style="font-size:50px;line-height:1;color:{R3};margin:10px 0 28px">Last call</div>
<div style="display:flex;flex-direction:column;gap:20px">{tag3('free candle','FREEFLAME',-4)}{tag3('diffusers from','£9.99',3,'#fff',R3)}{tag3('bundle 10 &amp; save','£89.91',-2)}</div>
<div style="font-size:14.5px;line-height:1.5;margin:28px 0 16px;max-width:240px">Bundle any scents and use code FREEFLAME today for your FREE candle.</div>{btn3('Shop bundles')}</div>
<div style="flex:1;background:url({P('p49_candlebox.jpg')}) 62% 66%/cover no-repeat;border-left:6px solid {R3}"></div></div>'''

def designer3():
    return f'''<div style="height:720px;background:{R3};position:relative;overflow:hidden">{snow(60,341,'rgba(255,255,255,.25)',2,720)}
<div style="position:absolute;left:34px;top:46px;right:34px;color:#fff">
<div style="font-size:11px;font-weight:700;letter-spacing:3px;opacity:.85">DAY 3 · SMELLS EXPENSIVE</div>
<div style="font-weight:900;font-size:64px;line-height:.92;letter-spacing:-2.5px;margin-top:12px;text-transform:uppercase">It smells<br>designer.</div></div>
<div style="position:absolute;right:30px;top:190px;width:290px;height:290px;border-radius:50%;background:url({P('cover1.jpg')}) 62% 78%/320% no-repeat;box-shadow:0 0 0 8px {C3}"></div>
<div class="serif it" style="position:absolute;left:34px;top:300px;width:250px;color:#fff;font-size:36px;line-height:1.08">It isn’t priced<br>like it.</div>
<div style="position:absolute;left:34px;right:34px;bottom:50px;color:#fff;display:flex;justify-content:space-between;align-items:flex-end;gap:20px">
<div style="font-size:15px;line-height:1.5;max-width:300px;opacity:.95">High-end scent, without the high-end price. Diffusers from £9.99 when you bundle.</div>{btn3('See for yourself', C3, R3)}</div></div>'''

def wheel3():
    cols = [R3, C3, '#E2C27A', '#fff', R3, C3, '#E2C27A', '#fff']
    labs = ['Free gift', 'Gift box', 'Bundle', 'Refill'] * 2
    segs = ''; tx = ''
    for i in range(8):
        a0 = math.radians(i*45-112.5); a1 = math.radians(i*45-67.5); r = 140
        segs += f'<path d="M0 0 L{r*math.cos(a0):.1f} {r*math.sin(a0):.1f} A{r} {r} 0 0 1 {r*math.cos(a1):.1f} {r*math.sin(a1):.1f}Z" fill="{cols[i]}" stroke="{R3}" stroke-width="2"/>'
        tx += f'<text transform="rotate({i*45}) translate(0,-92)" text-anchor="middle" font-family="Inter" font-weight="800" font-size="12" letter-spacing="1" fill="{"#fff" if cols[i]==R3 else R3}">{labs[i].upper()}</text>'
    return f'''<div style="height:740px;background:{C3};position:relative;overflow:hidden">
<div style="position:absolute;top:48px;left:0;right:0;text-align:center"><div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{R3}">DAY 3 · SPIN TO WIN</div>
<div class="serif it" style="font-size:46px;line-height:1.04;color:{R3};margin-top:10px">Give Christmas a spin</div></div>
<svg width="600" height="380" style="position:absolute;left:0;top:170px"><g transform="translate(300,200) rotate(14)"><circle r="154" fill="{R3}"/>{segs}{tx}<circle r="26" fill="#E2C27A" stroke="#fff" stroke-width="4"/></g>
<path d="M300 44 L284 20 L316 20Z" fill="{R3}"/>
{''.join(f'<circle cx="{300+170*math.cos(math.radians(a))}" cy="{200+170*math.sin(math.radians(a))}" r="4" fill="#E2C27A"/>' for a in range(0,360,30))}</svg>
<div style="position:absolute;left:44px;right:44px;bottom:50px;text-align:center"><div style="font-size:15px;line-height:1.5">Every slice is a winner. Tap to spin and see where it lands.</div><div style="margin-top:16px">{btn3('Spin now')}</div></div></div>'''

def box3(name, img):
    return f'''<div style="background:{B3};padding:36px 30px 36px">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:18px">
<div><div style="font-size:11px;font-weight:700;letter-spacing:3px;color:{R3}">DAY 3 · GIFT BOX DEAL</div><div class="serif it" style="font-size:42px;line-height:1;color:{R3};margin-top:6px">Thursday’s wish list</div></div>
<div style="font-size:30px;color:{R3}">♡</div></div>
<div style="background:#fff;padding:14px;position:relative;box-shadow:0 10px 26px rgba(0,0,0,.08)">
<div style="height:400px;background:url({PR(img)}) center 54%/112% no-repeat;border:2px solid {R3}"></div>
<div style="position:absolute;left:-8px;top:34px">{tag3('save','37%',-6,R3,'#fff',150)}</div>
<div style="display:flex;justify-content:space-between;align-items:center;padding:18px 6px 4px;gap:16px">
<div><div class="serif it" style="font-size:24px;color:{R3}">Best-Selling Gift Box</div><div style="font-size:12px;font-weight:700;letter-spacing:2.2px;margin-top:2px">{name.upper()}</div>
<div style="font-size:13.5px;line-height:1.45;color:#6a5a55;margin-top:6px;max-width:300px">Reed diffuser, natural wax candle &amp; room mist, gift-boxed.</div></div>
<div style="text-align:right"><div style="font-weight:900;font-size:36px;color:{R3};letter-spacing:-1px">£23.99</div><div style="font-size:14px;color:#8d7f79">was <s>£37.99</s></div></div></div>
<div style="padding:12px 6px 4px">{btn3('Add to my wish list – shop now')}</div></div></div>'''

pages['box_d3'] = box3('Cardamom &amp; Nutmeg', 'box_cardamom.jpg')
pages['hero_d3_AM_A'] = collage3()
pages['hero_d3_AM_B'] = polaroids3()
pages['hero_d3_AM_C'] = presents3()
pages['hero_d3_PM_A'] = tags3()
pages['hero_d3_PM_B'] = designer3()
pages['hero_d3_PM_C'] = wheel3()

for k, body in pages.items():
    open(f'{OUT}/{k}.html', 'w').write(BASE % body)
print(len(pages), 'pages')
