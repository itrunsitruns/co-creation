import os, glob, html, json
DEST="/home/user/co-creation/dreadlocks"; A=DEST+"/assets"
FAM={ "CS45":("民族圖騰圍巾","צעיף אינדיאני"),"CS46":("波浪紋圍巾","צעיף גלים"),"CS47":("民族風圍巾","צעיף אתני"),
"CS48":("葉影印花圍巾","צעיף עלים"),"CS51":("撒哈拉長圍巾","צעיף סהרה"),"CS52":("素色圍巾","צעיף חלק"),
"CS53":("繽紛花卉圍巾","צעיף פרת צבעוני"),"CS54":("黑底花卉圍巾","צעיף פרח שחור"),"CS55":("奶油花卉圍巾","צעיף פרח שמנת"),
"CS56":("菱格紋圍巾","צעיף מעויין"),"CS57":("圖騰印花圍巾","צעיף חג'יגי"),"CS58":("菱形紋圍巾","צעיף מעוינים"),
"CS60":("水滴紋圍巾","צעיף טיפות"),"CS61":("夏日圍巾","צעיף קיצי"),"CS62":("藍調圍巾","צעיף גוון כחול"),
"CS63":("夏日花卉圍巾","צעיף פרחי קיץ"),"CS64":("棕調圍巾","צעיף גווני חום"),"CS66":("綻放花卉圍巾","צעיף פריחה"),
"CS68":("幾何紋圍巾","צעיף גאומטרי"),"CS69":("繽紛歡樂圍巾","צעיף שמחי"),"CS70":("淺藍圍巾","צעיף כחלחל"),
"CS71":("藍色圍巾","צעיף כחול"),"CS72":("粉彩圍巾","צעיף פסטל"),"CS73":("芥末黃圍巾","צעיף חרדל"),"CS74":("花卉圍巾","צעיף פרח"),
"CS10":("皺褶感圍巾","צעיף מקומט"),"LIC":("純棉大方巾","צעיף כותנה"),"PON":("針織斗篷","פונצ'ו סריג")}
COLOR={"Orange":"橘","Fuchsia":"桃紅","Green":"綠","Red":"紅","Brown":"棕","Blue":"藍","Mustard":"芥末黃","Grey":"灰","Mocha":"摩卡","Dark Grey":"深灰","White":"白","Rose / Pink":"玫瑰粉","Denim":"丹寧藍","Coffee":"咖啡","Cream":"奶油","Smoky Pink":"煙燻粉","Bottle Green":"瓶綠","Multicolor print":"繽紛印花","Blue print":"藍印花","Dark-blue floral":"深藍花卉","Pink/Magenta floral":"桃紫花卉","Zebra B&W":"黑白斑馬","Marengo / Charcoal":"鐵灰","Tan / Chestnut":"棕褐","Bordeaux":"酒紅","Olive":"橄欖","Celadon":"青瓷","Cinnamon":"肉桂","Sky Blue":"天藍","Gold":"金","Avocado":"酪梨綠"}
ROWS=[
("CS45--41--00","Orange","100% Polyester","180 x 92"),("CS45--50--00","Fuchsia","100% Polyester","180 x 92"),("CS45--92--00","Green","100% Polyester","180 x 92"),
("CS46--23--00","Red","100% Polyester","180 x 92"),("CS46--50--00","Fuchsia","100% Polyester","180 x 92"),("CS46--70--00","Brown","100% Polyester","180 x 92"),
("CS47--22--00","Blue","100% Polyester","180 x 92"),("CS47--33--00","Mustard","100% Polyester","180 x 92"),("CS47--92--00","Green","100% Polyester","180 x 92"),
("CS48--15--00","Grey","100% Polyester","180 x 92"),("CS48--22--00","Blue","100% Polyester","180 x 92"),("CS48--26--00","Mocha","100% Polyester","180 x 92"),("CS48--41--00","Orange","100% Polyester","180 x 92"),
("CS53--01--00","Multicolor print","100% Cotton","180 x 86"),("CS54--01--00","Multicolor print","100% Cotton","180 x 86"),("CS55--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS56--01--00","Multicolor print","100% Cotton","180 x 86"),("CS57--01--00","Multicolor print","100% Cotton","180 x 86"),("CS58--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS60--01--00","Multicolor print","100% Cotton","180 x 86"),("CS61--01--00","Multicolor print","100% Cotton","200 x 86"),("CS62--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS63--01--00","Multicolor print","100% Cotton","180 x 86"),("CS64--01--00","Multicolor print","100% Cotton","200 x 86"),("CS66--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS68--01--00","Multicolor print","100% Cotton","180 x 86"),("CS69--01--00","Multicolor print","100% Cotton","180 x 86"),("CS70--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS71--01--00","Multicolor print","100% Cotton","180 x 86"),("CS72--01--00","Multicolor print","100% Cotton","180 x 86"),("CS73--01--00","Multicolor print","100% Cotton","200 x 86"),("CS74--01--00","Multicolor print","100% Cotton","180 x 86"),
("CS51--2--00","Dark Grey","100% Polyester","200 x 86"),("CS51--7--00","White","100% Polyester","200 x 86"),("CS51--69--00","Rose / Pink","100% Polyester","200 x 86"),("CS51--111--00","Denim","100% Polyester","200 x 86"),("CS51--116--00","Coffee","100% Polyester","200 x 86"),
("CS52--2--00","Dark Grey","100% Polyester","180 x 86"),("CS52--22--00","Blue","100% Polyester","180 x 86"),("CS52--27--00","Cream","100% Polyester","180 x 85"),("CS52--34--00","Smoky Pink","100% Polyester","180 x 86"),("CS52--86--00","Bottle Green","100% Polyester","180 x 86"),
("LIC06--00--O-S","Blue print","100% Cotton","180 x 110"),("LIC07--00--O-S","Dark-blue floral","100% Cotton","190 x 100"),("LIC19--00--O-S","Pink/Magenta floral","100% Cotton","180 x 110"),("LIC20--00--O-S","Zebra B&W","100% Cotton","180 x 110"),
("CS10--6--00","Marengo / Charcoal","薄皺褶 Crinkle","—"),
("PON--7--O-S","White","針織 Knit","One Size"),("PON--11--O-S","Bordeaux","針織 Knit","One Size"),("PON--17--O-S","Olive","針織 Knit","One Size"),
("PON--42--O-S","Celadon","針織 Knit","One Size"),("PON--77--O-S","Cinnamon","針織 Knit","One Size"),("PON--86--O-S","Bottle Green","針織 Knit","One Size"),("PON--96--O-S","Sky Blue","針織 Knit","One Size"),("PON--103--O-S","Gold","針織 Knit","One Size"),("PON--548--O-S","Avocado","針織 Knit","One Size"),
]
fam=lambda s: s[:3] if s.startswith("LIC") else ("PON" if s.startswith("PON") else s.split("--")[0])
price=lambda s: 2380 if s.startswith("PON") else (1680 if s.startswith("LIC") else (1820 if s.startswith("CS10") else 1400))
key=lambda s: s.replace("--","_").replace(" ","")
def gallery(sku):
    multi=sorted(glob.glob(os.path.join(A,key(sku)+"__*.jpg")))
    imgs=[os.path.basename(m) for m in multi] if multi else ([key(sku)+".jpg"] if os.path.exists(os.path.join(A,key(sku)+".jpg")) else [])
    if sku.startswith("PON") and os.path.exists(os.path.join(A,"PON__ring.jpg")): imgs=imgs+["PON__ring.jpg"]
    return ["assets/"+i for i in imgs]
SECTIONS=[
 ("poncho","針織斗篷","Knit Poncho","老闆的最愛 ♥ 輕薄針織披肩，One Size。右側縮圖可點看多角度，每款附「一圈全色圖」。",["PON"]),
 ("flow","多元印花圍巾","Mixed Print Scarves","輕盈飄逸、色彩飽和的長圍巾，180×92 cm，垂墜感佳，四季皆宜；可作頸巾、披巾或頭巾。",["CS45","CS46","CS47","CS48"]),
 ("cotton","純棉印花圍巾","Cotton Printed Scarves","100% 純棉，柔軟透氣、親膚舒適，180×86 cm（部分款 200 cm）；每一條都有自己的圖案個性。",["CS53","CS54","CS55","CS56","CS57","CS58","CS60","CS61","CS62","CS63","CS64","CS66","CS68","CS69","CS70","CS71","CS72","CS73","CS74"]),
 ("sahara","撒哈拉 & 素色","Sahara & Plain","素雅好搭的長圍巾。撒哈拉款 200×86 cm、邊緣短流蘇；素色款 180×86 cm，輕柔點綴。",["CS51","CS52"]),
 ("large","純棉大方巾","Cotton Large Scarves","100% 純棉大尺幅（約 180×110 cm），可當圍巾、披肩，也能作沙灘罩衫。",["LIC"]),
 ("crinkle","皺褶感圍巾","Crinkled Scarf","薄透皺褶質感，輕盈包覆、層次十足（材質與尺寸以原廠確認為準）。",["CS10"]),
]
by={}
for r in ROWS: by.setdefault(fam(r[0]),[]).append(r)
esc=lambda s: html.escape(str(s),quote=True)
def card(sku,color,mat,size):
    f=fam(sku); zh,he=FAM[f]; czh=COLOR.get(color,color); pr=price(sku); unit=' cm' if 'x' in size else ''
    origin="Made in Bali・峇里島製造" if sku.startswith("PON") else "Made in Israel・以色列製造"
    imgs=gallery(sku)
    if not imgs: imgs=["assets/"+key(sku)+".jpg"]
    main=imgs[0]; data=esc(json.dumps(imgs)); title=f"{zh}・{czh}"
    rail=""
    if len(imgs)>1:
        ts="".join(f'<img class="t{" active" if i==0 else ""}" data-i="{i}" src="{im}" alt="{esc(title)} {i+1}">' for i,im in enumerate(imgs))
        rail=f'<div class="rail">{ts}</div>'
    return f'''      <div class="card reveal">
        <div class="ph" data-images='{data}' data-title="{esc(title)}">
          <div class="main"><img loading="lazy" src="{main}" alt="{esc(title)}"><span class="zoom" aria-hidden="true">⤢</span></div>
          {rail}
        </div>
        <div class="info">
          <p class="he-name">{esc(he)}</p>
          <h3>{esc(zh)}・{esc(czh)}</h3>
          <p class="meta">{esc(color)}　|　{esc(mat)}　|　{esc(size)}{unit}</p>
          <p class="skuline"><span class="sku">{esc(sku)}</span><span class="origin">{esc(origin)}</span></p>
          <div class="buy"><span class="price">NT$ {pr:,}</span><a class="shopee" href="#" aria-label="前往蝦皮購買">前往蝦皮購買</a></div>
        </div>
      </div>'''
secs=[]
for k,zh,en,desc,fams in SECTIONS:
    cards=[card(*r) for f in fams for r in by.get(f,[])]
    secs.append(f'''  <section id="{k}">
    <div class="wrap">
      <div class="sec-head reveal"><p class="kicker">{esc(en)}・{len(cards)} 款</p><h2>{esc(zh)}</h2><p class="sec-desc">{esc(desc)}</p></div>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>''')
TOTAL=len(ROWS)
CSS=open(DEST+"/index.html").read().split("<style>")[1].split("</style>")[0]
CSS=CSS+"\n.card .origin{font-size:.72rem;color:var(--olive);letter-spacing:.03em;margin-top:4px}"
PAGE=open(DEST+"/index.html").read()
# replace sections + total by regenerating from template parts: simplest is to swap the <body>..sections..; but we rebuild fully:
import re
head=PAGE.split("</head>")[0]+"</head>"
# rebuild body using existing static parts (header/hero/story/footer/lightbox/script) by regenerating sections only is complex;
# Instead, reuse the previously-saved full template structure by string rebuild:
body=f'''<body>
<header><div class="nav">
  <div class="logo">Dreadlocks<small>Signa Taiwan 選品</small></div>
  <ul>
    <li><a href="#poncho">針織斗篷</a></li><li><a href="#flow">印花圍巾</a></li>
    <li><a href="#cotton">純棉圍巾</a></li><li><a href="#sahara">撒哈拉/素色</a></li>
    <li><a href="#values">品牌理念</a></li><li><a href="#story">品牌故事</a></li><li><a href="../">← Co-Creation</a></li>
  </ul>
</div></header>
<div class="hero">
  <p class="eyebrow">Israel → Taiwan</p>
  <h1>來自以色列的手感織品<br>第一站：圍巾<span class="he">צעיפים מישראל</span></h1>
  <p>Dreadlocks 是以色列的自然系服飾品牌，以根源文化與大地色彩聞名。Signa Taiwan 把它完整地帶來台灣——從一條圍巾開始。本系列 {TOTAL} 款顏色，每一條都有自己的希伯來名字。</p>
  <p style="opacity:.8;margin-top:14px;font-size:.92rem">Dreadlocks is a natural-style humanswear label from Israel, rooted in earthy colours and a free-spirited soul. Signa Taiwan brings the full brand to Taiwan — beginning with a single scarf. This collection has {TOTAL} colours, each with its own Hebrew name.</p>
  <div class="cta-row"><a class="btn btn-solid" href="#poncho">看招牌針織斗篷</a><a class="btn btn-line" href="#values">品牌故事</a></div>
</div>
<div class="swatch-strip" aria-hidden="true"><span style="background:var(--eggplant)"></span><span style="background:var(--olive)"></span><span style="background:var(--cognac)"></span><span style="background:var(--mocha)"></span><span style="background:var(--cream)"></span></div>
{chr(10).join(secs)}
<section id="values">
  <div class="wrap">
    <div class="sec-head reveal" style="text-align:center;max-width:none"><p class="kicker">Our Values</p><h2 style="font-weight:400">品牌理念</h2></div>
    <div class="vgrid">
      <div class="vitem reveal"><div class="vic">🌿</div><h4>自然系<span>Natural Style</span></h4><p>根源文化、大地色彩，崇尚自然與自在。<br>Rooted in nature — earthy colours &amp; a free spirit.</p></div>
      <div class="vitem reveal"><div class="vic">♻️</div><h4>永續環保<span>Ecological Vision</span></h4><p>具環境意識、公平善待的品牌。<br>Environmentally conscious, with fair &amp; ethical practices.</p></div>
      <div class="vitem reveal"><div class="vic">🇮🇱</div><h4>以色列品牌<span>Israeli Brand</span></h4><p>自 1999 年，於加利利設計與製造。<br>Designed &amp; made in the Galilee since 1999.</p></div>
      <div class="vitem reveal"><div class="vic">🛡️</div><h4>安心購物<span>Secure Shopping</span></h4><p>安全交易、購物有保障。<br>Safe, secure transactions you can trust.</p></div>
      <div class="vitem reveal"><div class="vic">🏅</div><h4>品質把關<span>Quality Control</span></h4><p>嚴選優質布料、原創印花。<br>Quality fabrics &amp; original, in-house prints.</p></div>
    </div>
  </div>
</section>
<section class="story" id="story"><div class="wrap" style="text-align:center">
  <div class="sec-head reveal"><p class="kicker">From the Roots</p><h2>一條從地中海到太平洋的線</h2></div>
  <div class="journey reveal"><div class="pt"><div class="city">以色列</div><div class="sub">設計・縫製</div></div><div class="line"></div><div class="pt"><div class="city">台灣</div><div class="sub">選品・送到你手上</div></div></div>
  <p class="body reveal">Dreadlocks 的全系列——上衣、洋裝、瑜珈系列、飾品——將隨著季節陸續抵達。<br>圍巾，是我們的第一封信。</p>
  <p class="body reveal" style="margin-top:16px;opacity:.78">Dreadlocks' full collection — tops, dresses, the yoga line and accessories — will arrive season by season.<br>The scarf is our first letter.</p>
</div></section>
<footer><div class="wrap">
  <div>© Signa Taiwan・以色列 Dreadlocks 原廠選品<br>signataiwan@gmail.com</div>
  <div><a href="#">蝦皮賣場</a> ・ <a href="#">Instagram</a> ・ <a href="../">Co-Creation ↗</a></div>
</div></footer>
<div class="lb" id="lb" aria-modal="true" role="dialog">
  <button class="close" id="lbClose" aria-label="關閉">✕</button>
  <button class="prev" id="lbPrev" aria-label="上一張">‹</button>
  <img class="lbmain" id="lbImg" src="" alt="">
  <button class="next" id="lbNext" aria-label="下一張">›</button>
  <div class="cap" id="lbCap"></div>
  <div class="thumbs" id="lbThumbs"></div>
</div>
'''
script=PAGE.split("<div class=\"lb\"")[1]
script="<script>"+PAGE.split("<script>")[1]
PAGE2=head+"\n"+body+script
open(DEST+"/index.html","w",encoding="utf-8").write(PAGE2)
print("rebuilt:",len(PAGE2),"bytes")
for r in by["PON"]: print(r[0], len(gallery(r[0])),"imgs")
