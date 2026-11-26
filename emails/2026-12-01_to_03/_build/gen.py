# Generates one HTML page per email image, to be screenshotted at 2x by render.js
import os, json, html

S = '/tmp/claude-0/-home-user-ruby/b44f2fb9-6eed-5680-a384-23171670d6e5/scratchpad'
OUT = f'{S}/render'
os.makedirs(OUT, exist_ok=True)
def P(name): return f'file://{S}/src/{name}'
def PR(name): return f'file://{S}/prod/{name}'

GREEN = '#1E3A2B'; GREEN2 = '#2C5240'; RED = '#8C1D24'; GOLD = '#B8913F'; GOLDL = '#E2C27A'
CREAM = '#F4EDE3'; PAGE = '#F7F5F2'; INK = '#212121'; ORANGE = '#FFA220'

BASE = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&display=block" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:600px;background:#fff;font-family:Inter,Arial,sans-serif;color:{INK};-webkit-font-smoothing:antialiased}}
#cap{{width:600px;position:relative;overflow:hidden}}
.serif{{font-family:Cardo,Georgia,serif}}
.eyebrow{{font-family:Inter;font-weight:600;letter-spacing:3px;text-transform:uppercase;font-size:11px;color:{GOLD}}}
.btn{{display:inline-block;background:{ORANGE};color:{INK};font-weight:700;font-size:14px;letter-spacing:1.6px;text-transform:uppercase;padding:15px 34px;border-radius:40px}}
.snow{{position:absolute;inset:0;pointer-events:none}}
</style></head><body><div id="cap">%s</div></body></html>"""

def snow(n=40, seed=1, color='rgba(255,255,255,.75)', maxr=2.6, h=800):
    import random
    r = random.Random(seed); dots = []
    for _ in range(n):
        x = r.uniform(0, 600); y = r.uniform(0, h); rad = r.uniform(.8, maxr)
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.1f}" fill="{color}"/>')
    return f'<svg class="snow" viewBox="0 0 600 {h}" preserveAspectRatio="none" width="600" height="{h}">{"".join(dots)}</svg>'

def star(x, y, s=8, c=GOLDL):
    return f'<path d="M{x} {y-s} L{x+s*.28} {y-s*.28} L{x+s} {y} L{x+s*.28} {y+s*.28} L{x} {y+s} L{x-s*.28} {y+s*.28} L{x-s} {y} L{x-s*.28} {y-s*.28}Z" fill="{c}"/>'

def holly(x, y, sc=1):
    return f'''<g transform="translate({x},{y}) scale({sc})">
<path d="M0 0 C-14 -6 -26 -2 -34 -12 C-26 -14 -22 -22 -28 -30 C-16 -26 -8 -30 -4 -22 C-2 -16 -2 -8 0 0Z" fill="#2F6B45"/>
<path d="M0 0 C14 -6 26 -2 34 -12 C26 -14 22 -22 28 -30 C16 -26 8 -30 4 -22 C2 -16 2 -8 0 0Z" fill="#3B7D52"/>
<circle cx="-5" cy="-3" r="5" fill="#B3202A"/><circle cx="5" cy="-4" r="5" fill="#C42B33"/><circle cx="0" cy="4" r="5" fill="#A51C25"/></g>'''

pages = {}

# ---------------------------------------------------------------- 12 DAYS STRIP
def strip(day):
    dots = ''
    for i in range(12):
        x = 410 + i * 14.5
        if i < day:
            dots += f'<circle cx="{x}" cy="24" r="5.4" fill="{GOLDL}"/>' if i == day - 1 else f'<circle cx="{x}" cy="24" r="4" fill="{GOLD}"/>'
        else:
            dots += f'<circle cx="{x}" cy="24" r="3.8" fill="none" stroke="rgba(226,194,122,.6)" stroke-width="1.2"/>'
    return f'''<div style="height:48px;background:{GREEN};position:relative;border-bottom:2px solid {RED}">
<svg width="600" height="48" style="position:absolute;inset:0">{star(20,24,6)}{star(580,24,6)}{dots}
<text x="396" y="28" text-anchor="end" font-family="Inter" font-size="10.5" font-weight="700" letter-spacing="2" fill="{GOLDL}">DAY {day} OF 12</text></svg>
<div style="position:absolute;left:36px;top:0;height:48px;display:flex;align-items:center">
<span class="serif" style="color:#fff;font-size:20px;font-style:italic">The 12 Days of Christmas</span></div></div>'''
for d in (1, 2, 3):
    pages[f'strip_d{d}'] = strip(d)

# ---------------------------------------------------------------- FREE GIFT BANNER
GIFTS = {1: ('candle', 'FREEFLAME', 'p49_candlebox.jpg', '66% 70%', 150),
         2: ('diffuser', 'FREEDIFF', 'p49_diffbox.jpg', '44% 58%', 175),
         3: ('candle', 'FREEFLAME', 'p49_candlebox.jpg', '70% 74%', 165)}
def giftbanner(day, slot):
    item, code, photo, pos, zoom = GIFTS[day]
    eyebrow = f'DAY {day} · TODAY ONLY' if slot == 'AM' else f'DAY {day} · FINAL HOURS'
    head = f'A FREE {item}<br>with every order' if slot == 'AM' else f'Last call: your<br>FREE {item}'
    return f'''<div style="height:240px;background:{CREAM};position:relative">
<div style="position:absolute;left:-60px;top:-40px;width:340px;height:320px;border-radius:50%;overflow:hidden;background:url({P(photo)}) {pos}/{zoom}% no-repeat"></div>
<div style="position:absolute;left:-60px;top:-40px;width:340px;height:320px;border-radius:50%;box-shadow:inset 0 0 0 5px {CREAM}, inset 0 0 0 7px {GOLD}"></div>
{snow(26, day*7+ (1 if slot=='PM' else 0), 'rgba(184,145,63,.35)', 2.2, 240).replace('class="snow"','class="snow" style="left:300px;width:300px"')}
<svg width="600" height="240" style="position:absolute;inset:0">{holly(560,40,.62)}</svg>
<div style="position:absolute;left:300px;right:20px;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
<div class="eyebrow" style="font-size:10.5px;color:{RED}">✦ {eyebrow} ✦</div>
<div class="serif" style="font-size:31px;line-height:1.05;margin:8px 0 12px;color:{INK}">{head}</div>
<div style="border:1.5px dashed {GOLD};background:#fff;border-radius:6px;padding:8px 18px;font-weight:700;letter-spacing:2.2px;font-size:13px;color:{GOLD}">USE CODE&nbsp; {code}</div>
<div class="btn" style="margin-top:12px;padding:11px 26px;font-size:12px;text-transform:none;letter-spacing:.4px">Claim Your FREE Gift →</div>
</div></div>'''
for d in (1, 2, 3):
    for s in ('AM', 'PM'):
        pages[f'gift_d{d}_{s}'] = giftbanner(d, s)

# ---------------------------------------------------------------- GIFT BOX OFFER CARD
BOXES = {1: ('Jasmine &amp; Rosewood', 'box_jasmine.jpg'), 2: ('Pure Lavender', 'box_lavender.jpg'), 3: ('Cardamom &amp; Nutmeg', 'box_cardamom.jpg')}
DAYNAME = {1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday'}
def boxcard(day):
    name, img = BOXES[day]
    return f'''<div style="background:{GREEN};padding:34px 30px 34px;position:relative">
{snow(60, day*3, 'rgba(255,255,255,.35)', 2.2, 820)}
<svg width="600" height="90" style="position:absolute;left:0;top:0">{holly(40,40,.8)}{holly(560,40,.8)}</svg>
<div style="text-align:center;position:relative">
<div class="eyebrow" style="color:{GOLDL}">✦ Day {day} gift box deal ✦</div>
<div class="serif" style="color:#fff;font-size:34px;margin:8px 0 20px">{DAYNAME[day]}’s gift to give</div></div>
<div style="background:#fff;position:relative;border-radius:4px;overflow:hidden;box-shadow:0 0 0 6px rgba(226,194,122,.35)">
<div style="position:relative;height:430px;background:url({PR(img)}) center 46%/108% no-repeat"></div>
<div style="position:absolute;top:18px;right:18px;width:92px;height:92px;border-radius:50%;background:{RED};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 0 3px #fff, 0 0 0 4.5px {RED}">
<div style="font-size:11px;letter-spacing:1.5px;font-weight:700">SAVE</div><div class="serif" style="font-size:30px;line-height:1">37%</div></div>
<div style="text-align:center;padding:22px 30px 30px">
<div class="eyebrow" style="font-size:11px">Save £14 · Gift-ready</div>
<div class="serif" style="font-size:27px;line-height:1.15;margin:8px 0 10px">Best-Selling Gift Box<br><i>{name}</i></div>
<div style="font-size:15px;color:#5a5a5a;line-height:1.45">Reed diffuser, natural wax candle &amp; room mist,<br>beautifully boxed and ready to give.</div>
<div style="margin:14px 0 16px;font-size:17px">Now <span class="serif" style="font-size:34px;font-weight:700">£23.99</span> <span style="color:#8a8a8a;font-size:16px">was <s>£37.99</s></span></div>
<div class="btn">Shop the gift box</div></div></div></div>'''
for d in (1, 2, 3):
    pages[f'box_d{d}'] = boxcard(d)

# ---------------------------------------------------------------- HEROES
def hero_A(photo, pos, eyebrow, head, sub, cta, strip_txt, h=760, photo_h=430):
    return f'''<div style="height:{h}px;position:relative;background:{CREAM}">
<div style="position:absolute;left:0;right:0;top:0;height:{photo_h+40}px;background:url({P(photo)}) {pos}/cover no-repeat"></div>
{snow(70, len(head), 'rgba(255,255,255,.55)', 2.4, h)}
<div style="position:absolute;left:40px;right:40px;top:{photo_h-40}px;background:#FFFDF8;padding:34px 34px 34px;text-align:center;box-shadow:0 0 0 1px rgba(184,145,63,.5), 0 0 0 7px {CREAM}, 0 0 0 8px rgba(184,145,63,.6)">
<div class="eyebrow">{eyebrow}</div>
<div class="serif" style="font-size:40px;line-height:1.08;margin:12px 0 12px">{head}</div>
<div style="font-size:16px;line-height:1.5;color:#444">{sub}</div>
<div class="btn" style="margin-top:20px">{cta} →</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:42px;background:{GREEN};color:{GOLDL};display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:600;letter-spacing:2.6px">{strip_txt}</div></div>'''

def hero_B(photo, pos, eyebrow, head, sub, cta, h=700):
    return f'''<div style="height:{h}px;position:relative;background:url({P(photo)}) {pos}/cover no-repeat">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,28,20,0) 22%,rgba(15,28,20,.62) 52%,rgba(15,28,20,.95) 100%)"></div>
{snow(90, len(head)+3, 'rgba(255,255,255,.7)', 2.6, h)}
<div style="position:absolute;left:48px;right:48px;bottom:56px;text-align:center;color:#fff">
<div class="eyebrow" style="color:{GOLDL}">✦ {eyebrow} ✦</div>
<div class="serif" style="font-size:44px;line-height:1.08;margin:14px 0 14px;text-shadow:0 2px 18px rgba(0,0,0,.35)">{head}</div>
<div style="font-size:16px;line-height:1.5;color:rgba(255,255,255,.88)">{sub}</div>
<div class="btn" style="margin-top:22px;background:#fff">{cta} →</div></div></div>'''

def frame_C(inner, eyebrow, head, sub, cta, bg=GREEN, h=720, seed=5, mid=None):
    mid = mid or GREEN2
    return f'''<div style="height:{h}px;position:relative;background:radial-gradient(ellipse at 50% 42%, {mid} 0%, {bg} 64%, #0E1F16 100%);overflow:hidden">
{snow(120, seed, 'rgba(255,255,255,.55)', 2.4, h)}
<svg width="600" height="{h}" style="position:absolute;inset:0">{holly(46,44,.9)}{holly(554,44,.9)}{star(110,120,7)}{star(500,150,6)}{star(80,330,5)}{star(530,360,7)}</svg>
<div style="position:absolute;top:44px;left:0;right:0;text-align:center"><div class="eyebrow" style="color:{GOLDL}">✦ {eyebrow} ✦</div>
<div class="serif" style="color:#fff;font-size:40px;line-height:1.08;margin:10px 60px 0">{head}</div></div>
{inner}
<div style="position:absolute;left:40px;right:40px;bottom:46px;text-align:center;color:rgba(255,255,255,.88)">
<div style="font-size:15.5px;line-height:1.5">{sub}</div>
<div class="btn" style="margin-top:18px">{cta} →</div></div></div>'''

def game_door(n):
    return f'''<div style="position:absolute;left:180px;top:190px;width:240px;height:330px">
<div style="position:absolute;inset:-14px;border-radius:120px 120px 8px 8px;background:{GOLD};box-shadow:0 10px 30px rgba(0,0,0,.4)"></div>
<div style="position:absolute;inset:0;border-radius:110px 110px 4px 4px;background:#FFF6E2;overflow:hidden">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column"><div class="serif" style="font-size:22px;color:{RED};font-style:italic">a treat inside…</div></div></div>
<div style="position:absolute;inset:0;border-radius:110px 110px 4px 4px;background:linear-gradient(135deg,{RED},#6E141A);transform-origin:left center;transform:perspective(900px) rotateY(-28deg);box-shadow:8px 0 18px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center">
<div style="position:absolute;inset:16px;border-radius:96px 96px 2px 2px;border:2px solid rgba(226,194,122,.7)"></div>
<div class="serif" style="font-size:150px;color:{GOLDL};line-height:1">{n}</div>
<div style="position:absolute;right:20px;top:52%;width:14px;height:14px;border-radius:50%;background:{GOLDL}"></div></div>
<svg width="300" height="80" style="position:absolute;left:-30px;top:-46px">{holly(150,52,1.1)}</svg></div>'''

def game_cracker():
    return f'''<svg width="600" height="360" style="position:absolute;left:0;top:180px">
<defs><linearGradient id="cr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C2313A"/><stop offset="1" stop-color="#7A161D"/></linearGradient></defs>
<g transform="translate(300,170) rotate(-8)">
<g transform="translate(-26,0)"><path d="M-170 -34 L-110 -34 L-90 -18 L-36 -40 L0 -40 L0 40 L-36 40 L-90 18 L-110 34 L-170 34 L-190 0Z" fill="url(#cr)"/>
<rect x="-70" y="-40" width="16" height="80" fill="{GOLDL}"/><path d="M-190 0 L-170 -34 L-182 -16Z" fill="#5c1015"/>
<g fill="{GOLDL}">{''.join(f'<circle cx="{-150+i*22}" cy="{-12+(i%2)*24}" r="3"/>' for i in range(4))}</g></g>
<g transform="translate(26,0)"><path d="M170 -34 L110 -34 L90 -18 L36 -40 L0 -40 L0 40 L36 40 L90 18 L110 34 L170 34 L190 0Z" fill="url(#cr)"/>
<rect x="54" y="-40" width="16" height="80" fill="{GOLDL}"/>
<g fill="{GOLDL}">{''.join(f'<circle cx="{86+i*22}" cy="{-12+(i%2)*24}" r="3"/>' for i in range(4))}</g></g>
<g stroke="{GOLDL}" stroke-width="3" stroke-linecap="round"><path d="M-12 -52 L-20 -74"/><path d="M0 -56 L0 -84"/><path d="M12 -52 L22 -74"/><path d="M-12 52 L-20 74"/><path d="M12 52 L22 74"/></g>
<text x="0" y="8" text-anchor="middle" font-family="Cardo" font-size="34" font-weight="700" fill="#fff">SNAP!</text></g>
<text x="300" y="320" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="22" fill="{GOLDL}">You’ve won… ? ? ?</text></svg>'''

def game_globe():
    flakes = ''.join(f'<circle cx="{c[0]}" cy="{c[1]}" r="{c[2]}" fill="#fff" opacity=".9"/>' for c in [(250,250,3),(330,230,2.5),(290,300,3.5),(360,290,2),(230,320,2.4),(310,200,2),(270,210,2.2),(350,330,3),(300,260,2)])
    return f'''<svg width="600" height="380" style="position:absolute;left:0;top:170px">
<defs><radialGradient id="g" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#E9F3F6" stop-opacity=".55"/><stop offset=".7" stop-color="#A9C7D0" stop-opacity=".25"/><stop offset="1" stop-color="#fff" stop-opacity=".5"/></radialGradient></defs>
<path d="M190 330 Q300 300 410 330 L430 372 L170 372Z" fill="{GOLD}"/><rect x="170" y="364" width="260" height="14" rx="4" fill="#8A6A2A"/>
<circle cx="300" cy="230" r="120" fill="#24453A"/>
<path d="M200 300 Q300 260 400 300 L400 330 L200 330Z" fill="#fff"/>
<g transform="translate(300,272)"><rect x="-28" y="-30" width="56" height="44" fill="#fff" stroke="{RED}" stroke-width="2"/><rect x="-30" y="-36" width="60" height="10" fill="{RED}"/><rect x="-4" y="-36" width="8" height="50" fill="{GOLDL}"/><path d="M0 -36 C-14 -56 -26 -40 0 -36 C26 -40 14 -56 0 -36Z" fill="{GOLDL}"/></g>
<path d="M240 270 L252 236 L264 270Z" fill="#2F6B45"/><path d="M336 270 L350 228 L364 270Z" fill="#2F6B45"/>
{flakes}<circle cx="300" cy="230" r="120" fill="url(#g)" stroke="rgba(255,255,255,.7)" stroke-width="3"/>
<path d="M232 160 Q260 132 300 128" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" opacity=".6"/>
<g stroke="{GOLDL}" stroke-width="3" stroke-linecap="round" fill="none"><path d="M150 200 q-14 30 0 60"/><path d="M128 190 q-18 40 0 80"/><path d="M450 200 q14 30 0 60"/><path d="M472 190 q18 40 0 80"/></g></svg>'''

def game_scratch():
    return f'''<div style="position:absolute;left:90px;top:200px;width:420px;height:290px;border-radius:14px;background:#FFF6E2;box-shadow:0 0 0 5px {GOLD},0 14px 34px rgba(0,0,0,.4);overflow:hidden">
<div style="position:absolute;top:22px;left:0;right:0;text-align:center"><div class="eyebrow" style="color:{RED}">✦ Every card wins ✦</div>
<div class="serif" style="font-size:26px;margin-top:4px">Your festive treat</div></div>
<div style="position:absolute;left:34px;right:34px;top:100px;height:150px;border-radius:10px;background:#FBF3DF;box-shadow:inset 0 0 0 2px rgba(184,145,63,.5);display:flex;align-items:center;justify-content:center">
<div class="serif" style="font-size:46px;color:{GOLD};letter-spacing:10px">? ? ?</div></div>
<svg width="420" height="290" style="position:absolute;inset:0"><defs><pattern id="fr" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" fill="#CBD8DE"/><rect width="6" height="12" fill="#DDE7EB"/></pattern>
<mask id="m"><rect x="34" y="100" width="352" height="150" rx="10" fill="#fff"/><path d="M40 210 C120 150 170 230 250 160 C290 128 320 150 350 120" stroke="#000" stroke-width="44" fill="none" stroke-linecap="round"/></mask></defs>
<rect x="34" y="100" width="352" height="150" rx="10" fill="url(#fr)" mask="url(#m)"/>
<text x="330" y="236" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="17" fill="#557079">scratch here ❄</text>
<g transform="translate(360,112) rotate(30)"><ellipse rx="22" ry="22" fill="{GOLD}"/><ellipse rx="16" ry="16" fill="{GOLDL}"/><text y="6" text-anchor="middle" font-family="Cardo" font-size="18" font-weight="700" fill="{GOLD}">V</text></g></svg></div>'''

def game_presents():
    def box(x, col, rib, lab):
        return f'''<g transform="translate({x},0)"><rect x="-62" y="40" width="124" height="110" fill="{col}"/><rect x="-70" y="16" width="140" height="30" fill="{col}" stroke="rgba(0,0,0,.15)"/>
<rect x="-9" y="16" width="18" height="134" fill="{rib}"/><path d="M0 16 C-30 -24 -54 4 0 16 C54 4 30 -24 0 16Z" fill="{rib}"/>
<circle cx="0" cy="80" r="0"/><text x="0" y="186" text-anchor="middle" font-family="Cardo" font-size="30" font-weight="700" fill="{GOLDL}">{lab}</text></g>'''
    return f'''<svg width="600" height="400" style="position:absolute;left:0;top:200px"><g transform="translate(300,90) scale(1.12) translate(-300,0)">
{box(130,'#B3202A',GOLDL,'1')}{box(300,'#F4EDE3','#2C5240','2')}{box(470,GOLD,'#1E3A2B','3')}</g>
<text x="300" y="20" text-anchor="middle" font-family="Cardo" font-style="italic" font-size="22" fill="{GOLDL}">Which one is yours?</text></svg>'''

def game_wheel():
    cols = [RED, CREAM, GREEN2, GOLD, RED, CREAM, GREEN2, GOLD]
    labs = ['Free gift', 'Gift box', 'Bundle', 'Refill', 'Free gift', 'Gift box', 'Bundle', 'Refill']
    import math
    segs = ''; tx = ''
    for i in range(8):
        a0 = math.radians(i*45 - 90 - 22.5); a1 = math.radians(i*45 - 90 + 22.5); r = 140
        segs += f'<path d="M0 0 L{r*math.cos(a0):.1f} {r*math.sin(a0):.1f} A{r} {r} 0 0 1 {r*math.cos(a1):.1f} {r*math.sin(a1):.1f}Z" fill="{cols[i]}" stroke="{GOLDL}" stroke-width="2"/>'
        am = i*45 - 90; fill = INK if cols[i] in (CREAM, GOLD) else '#fff'
        tx += f'<text transform="rotate({am+90}) translate(0,-92)" text-anchor="middle" font-family="Inter" font-weight="700" font-size="12" letter-spacing="1" fill="{fill}">{labs[i].upper()}</text>'
    return f'''<svg width="600" height="360" style="position:absolute;left:0;top:178px"><g transform="translate(300,190) rotate(14)">
<circle r="152" fill="{GOLD}"/>{segs}{tx}<circle r="26" fill="{GOLDL}" stroke="#fff" stroke-width="4"/></g>
<path d="M300 22 L284 0 L316 0Z" fill="#fff" transform="translate(0,22)"/>
<g stroke="rgba(255,255,255,.6)" stroke-width="3" fill="none" stroke-linecap="round"><path d="M120 120 q-24 70 0 140"/><path d="M480 120 q24 70 0 140"/></g></svg>'''

# copy per send ------------------------------------------------------------
BUNDLE = 'FROM £9.99 EACH · SAVE UP TO £89.91 · MIX &amp; MATCH'
H = {}
H[(1,'AM','A')] = hero_A('xmas_boxes_warm.jpg', '62% 82%', 'The 12 Days of Christmas · Day 1', 'Christmas scent for every room, from £9.99', 'Bundle 10 reed diffusers and save £89.91. Mix &amp; match any scents.', 'Build my bundle', BUNDLE)
H[(1,'AM','B')] = hero_B('cover2.jpg', '50% 60%', 'Day 1 · The countdown begins', 'It starts the moment they walk in…', 'Guests notice the second they walk in. Make every room Christmas-ready.', 'See how')
H[(1,'AM','C')] = frame_C(game_door(1), 'The 12 Days of Christmas', 'Door No. 1 is ready to open', 'Tap to open today’s door. Every door hides a festive treat – and every one is a winner.', 'Open door 1', seed=11)
H[(1,'PM','A')] = hero_A('bundle_back.jpg', '50% 58%', 'Day 1 · Bundle &amp; save', 'One for every room. Save up to £89.91', 'Reed diffusers from £9.99 each when you bundle, plus a FREE candle with code FREEFLAME.', 'Shop bundles', BUNDLE)
H[(1,'PM','B')] = hero_B('embrace.jpg', '60% 50%', 'Day 1 · Evening glow', 'The house everyone talks about this Christmas', 'Strong, never overpowering. One diffuser, every room scented.', 'Discover more')
H[(1,'PM','C')] = frame_C(game_cracker(), 'Day 1 · Pull the cracker', 'Pull the cracker… what’s inside?', 'Snap! Every cracker holds a prize. Tap to pull and reveal yours.', 'Pull to reveal', bg='#5E1218', seed=12, mid='#9A2530')
H[(2,'AM','A')] = hero_A('cover1.jpg', '64% 80%', 'The 12 Days of Christmas · Day 2', 'Fill every room for Christmas, from £9.99', 'Mix &amp; match 10 diffusers and save £89.91, plus a FREE boxed diffuser with code FREEDIFF.', 'Build my bundle', BUNDLE)
H[(2,'AM','B')] = hero_B('p48_bsgb.jpg', '50% 55%', 'Day 2 · Ready for guests?', '“What’s that beautiful smell?”', 'The question every guest asks. Be the home people always comment on.', 'Find your scent')
H[(2,'AM','C')] = frame_C(game_globe(), 'Day 2 · Shake the snow globe', 'Give it a shake… a gift is hiding in the snow', 'Tap to shake it up. When the snow settles, your treat is revealed.', 'Shake to reveal', bg='#173248', seed=21, mid='#2D5470')
def ladder():
    rows = [('3 diffusers', 'Save £21'), ('6 diffusers', 'Save £48'), ('10 diffusers', 'Save £89.91')]
    r = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 4px;border-bottom:1px solid rgba(184,145,63,.35)"><span class="serif" style="font-size:24px">{a}</span><span style="font-weight:700;letter-spacing:1.5px;font-size:13px;color:{RED}">{b.upper()}</span></div>' for a, b in rows)
    return r
H[(2,'PM','A')] = hero_A('xmas_boxes2.jpg', '62% 82%', 'Day 2 · Buy more, save more', f'The more rooms, the merrier</div><div style="text-align:left;margin:4px 10px 6px">{ladder()}</div><div style="display:none">', 'Diffusers from £9.99 each in the 10-pack. Plus a FREE boxed diffuser with code FREEDIFF.', 'Pick my pack', BUNDLE, h=840, photo_h=380)
H[(2,'PM','B')] = hero_B('p49_diffbox.jpg', '42% 50%', 'Day 2 · Around the clock', 'Christmas in every room, all day long', 'Our diffusers work 24/7 – no effort required. Lasts up to 12 weeks.', 'Shop diffusers')
H[(2,'PM','C')] = frame_C(game_scratch(), 'Day 2 · Scratch card', 'Scratch to reveal your treat', 'One card, one festive treat – every card wins. Tap to scratch away the frost.', 'Scratch now', seed=22)
H[(3,'AM','A')] = hero_A('p49_candlebox.jpg', '62% 72%', 'The 12 Days of Christmas · Day 3', 'The Christmas host’s secret: £9.99 diffusers', '10 diffusers in any scents, save £89.91 – plus a FREE candle with code FREEFLAME.', 'Build my bundle', BUNDLE)
H[(3,'AM','B')] = hero_B('cover2.jpg', '30% 70%', 'Day 3 · Coming home', 'The scent that greets you before you’ve even taken your coat off.', 'Fills the whole house, not just the room it’s in.', 'Discover more')
H[(3,'AM','C')] = frame_C(game_presents(), 'Day 3 · Pick a present', 'Three presents. One is yours.', 'Every present hides a festive treat. Tap to pick yours and unwrap it.', 'Pick my present', bg='#5E1218', seed=31, mid='#9A2530')
H[(3,'PM','A')] = hero_A('embrace.jpg', '62% 62%', 'Day 3 · Final hours', 'Last call: FREE candle + diffusers from £9.99', 'Bundle any scents and save up to £89.91. Use code FREEFLAME today for your FREE candle.', 'Shop bundles', BUNDLE)
H[(3,'PM','B')] = hero_B('cover1.jpg', '40% 50%', 'Day 3 · Smells expensive', 'It smells designer. It isn’t priced like it.', 'High-end scent, without the high-end price. Diffusers from £9.99 when you bundle.', 'See for yourself')
H[(3,'PM','C')] = frame_C(game_wheel(), 'Day 3 · Spin the wheel', 'Give Christmas a spin', 'Every slice is a winner. Tap to spin and see where it lands.', 'Spin now', seed=32)
for (d, s, v), body in H.items():
    pages[f'hero_d{d}_{s}_{v}'] = body

for k, body in pages.items():
    open(f'{OUT}/{k}.html', 'w').write(BASE % body)
print(len(pages), 'pages')
