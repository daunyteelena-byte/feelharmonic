#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FeelHarmonic - puslapio generatorius
=====================================================================
Puslapio tekstai gyvena aplanke `turinys/` - po vieną JSON failą kiekvienai
kalbai (lt.json, en.json, it.json). Puslapio karkasas (HTML) aprašytas čia.

Paleidimas:

    python build.py

Perrašo tris failus:  index.html  (lietuviškas),  en/index.html,  it/index.html
ir atnaujina sitemap.xml.

TAISYKLE: index.html, en/index.html ir it/index.html RANKA neredaguojami -
juos perrašo šis skriptas. Teksta keisti turinys/*.json failuose, po to paleisti
skripta iš naujo.

JSON laukuose leidžiamas paprastas HTML (<em>, <b>, <span class="fill">...</span>),
todel tekstas neekranuojamas.
"""

import hashlib
import urllib.parse
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent


def ver(rel):
    """Trumpas failo turinio parašas: ?v=... pasikeičia tik pakeitus failą,
    todėl naršyklė iškart pasiima naują CSS/JS, o ne seną iš podėlio."""
    return hashlib.sha1((ROOT / rel).read_bytes()).hexdigest()[:8]
CONTENT = ROOT / "turinys"

SITE = "https://www.feelharmonic.lt"
LANGS = ["lt", "en", "it"]
OUT = {"lt": ROOT / "index.html", "en": ROOT / "en" / "index.html", "it": ROOT / "it" / "index.html"}
HREF = {"lt": "/", "en": "/en/", "it": "/it/"}
BASE = {"lt": "", "en": "../", "it": "../"}
LOCALE = {"lt": "lt_LT", "en": "en_GB", "it": "it_IT"}
LANG_SHORT = {"lt": "LT", "en": "EN", "it": "IT"}
LANG_NAME = {"lt": "Lietuvių", "en": "English", "it": "Italiano"}

EMAIL = "info@feelharmonic.lt"
# Mokėjimo už knygelę rekvizitai — įrašomi į „Įsigyti knygelę“ laiško šabloną
BANK_NAME = "Elena Daunytė"
BANK_IBAN = "LT81 7300 0100 8950 9422"
FACEBOOK = "https://www.facebook.com/profile.php?id=100090960240169"
FB_ICON = ('<svg class="fb-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-7.5h2.6'
           'l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9'
           'v2.3H7.9v3h2.6V21z"/></svg>')

# Šūkis, kuriuo baigiasi kiekviena skiltis. Visomis kalbomis vienodas.
MOTTO = '<p class="motto reveal">Let it come!</p>'

MARK = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="mark" viewBox="0 0 100 100">
    <g class="mark">
      <g class="beam">
        <polygon points="50.95,45.80 50.00,0.00 49.05,45.80"/>
        <polygon points="49.05,54.20 50.00,100.00 50.95,54.20"/>
        <polygon points="54.20,50.95 91.00,50.00 54.20,49.05"/>
        <polygon points="45.80,49.05 9.00,50.00 45.80,50.95"/>
        <polygon points="53.64,47.70 81.82,18.18 52.30,46.36"/>
        <polygon points="52.30,53.64 81.82,81.82 53.64,52.30"/>
        <polygon points="46.36,52.30 18.18,81.82 47.70,53.64"/>
        <polygon points="47.70,46.36 18.18,18.18 46.36,47.70"/>
        <polygon points="52.48,46.48 63.78,16.74 50.73,45.76"/>
        <polygon points="50.73,54.24 63.78,83.26 52.48,53.52"/>
        <polygon points="47.52,53.52 36.22,83.26 49.27,54.24"/>
        <polygon points="49.27,45.76 36.22,16.74 47.52,46.48"/>
        <polygon points="54.24,49.27 85.11,35.46 53.52,47.52"/>
        <polygon points="53.52,52.48 85.11,64.54 54.24,50.73"/>
        <polygon points="45.76,50.73 14.89,64.54 46.48,52.48"/>
        <polygon points="46.48,47.52 14.89,35.46 45.76,49.27"/>
      </g>
      <path class="tri" d="M50 22 L76 74 L24 74 Z"/>
      <circle class="dot" cx="50" cy="50" r="6.6"/>
      <circle class="dot" cx="34" cy="20" r="3.0"/>
      <circle class="dot" cx="58" cy="17" r="1.0"/>
      <circle class="dot" cx="20" cy="33" r="1.8"/>
      <circle class="dot" cx="74" cy="35" r="1.3"/>
      <circle class="dot" cx="76" cy="63" r="2.2"/>
      <circle class="dot" cx="53" cy="79" r="2.6"/>
    </g>
  </symbol>
<symbol id="mark-sm" viewBox="0 0 100 100">
    <g class="mark-sm">
      <g class="ray">
        <line x1="50" y1="8"  x2="50" y2="92"/>
        <line x1="16" y1="50" x2="84" y2="50"/>
        <line x1="26" y1="26" x2="74" y2="74"/>
        <line x1="74" y1="26" x2="26" y2="74"/>
      </g>
      <path class="tri" d="M50 26 L74 72 L26 72 Z"/>
      <circle class="dot" cx="50" cy="50" r="6.4"/>
    </g>
  </symbol>
</svg>"""


def attr(text):
    """Ekranuoja teksta HTML atributui."""
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def photo(base, src, alt, cls="shot", cap=None):
    fig = ['<figure class="%s" data-photo>' % cls,
           '  <svg class="ph-empty" viewBox="0 0 100 100" aria-hidden="true"><use href="#mark"/></svg>',
           '  <img src="%sassets/img/%s" alt="%s" data-optional>' % (base, src, attr(alt))]
    if cap:
        fig.append('  <figcaption>%s</figcaption>' % cap)
    fig.append('</figure>')
    return "\n      ".join(fig)


def langmenu(lang, aria):
    """Antrastes kalbu pasirinkimas: rodoma tik esama kalba, kitos -- paspaudus."""
    out = ['<details class="lang-menu">',
           '  <summary aria-label="%s: %s">%s<svg viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4"/></svg></summary>'
           % (attr(aria), attr(LANG_NAME[lang]), LANG_SHORT[lang]),
           '  <div class="lang-list" role="group" aria-label="%s">' % attr(aria)]
    for code in LANGS:
        cur = ' class="is-current" aria-current="page"' if code == lang else ""
        out.append('    <a href="%s" hreflang="%s" lang="%s"%s><b>%s</b>%s</a>'
                   % (HREF[code], code, code, cur, LANG_SHORT[code], LANG_NAME[code]))
    out.append("  </div>")
    out.append("</details>")
    return "\n    ".join(out)


def head(lang, c):
    b = BASE[lang]
    m = c["meta"]
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s%s">' % (code, SITE, HREF[code]) for code in LANGS)
    return """<!doctype html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>%(title)s</title>
<meta name="description" content="%(desc)s">

<link rel="canonical" href="%(site)s%(href)s">
%(alts)s
<link rel="alternate" hreflang="x-default" href="%(site)s/">
<meta property="og:url" content="%(site)s%(href)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="%(locale)s">
<meta property="og:site_name" content="FeelHarmonic">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(ogdesc)s">
<meta property="og:image" content="%(site)s/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B3C41">

<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="%(b)sfavicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="%(b)sapple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;1,400&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap">
<link rel="stylesheet" href="%(b)sassets/css/style.css?v=%(cssv)s">
</head>
<body>
""" % {"lang": lang, "title": attr(m["title"]), "desc": attr(m["description"]),
       "ogdesc": attr(m["ogDescription"]), "site": SITE, "href": HREF[lang],
       "alts": alts, "locale": LOCALE[lang], "b": b, "cssv": ver("assets/css/style.css")}


def header(lang, c):
    nav = "\n      ".join('<a href="%s">%s</a>' % (i["href"], i["label"]) for i in shown(c["nav"]))
    mob = "\n  ".join('<a href="%s">%s</a>' % (i["href"], i["label"]) for i in shown(c["mobileNav"]))
    return """<a class="skip" href="#turinys">%(skip)s</a>

<!-- ženklo šablonas -->
%(mark)s

<header id="nav">
  <div class="in">
    <a class="brand" href="#top">
      <svg><use href="#mark-sm"/></svg>
      <b>FeelHarmonic</b>
    </a>
    <nav class="main" aria-label="%(navaria)s">
      %(nav)s
      <a class="btn" href="#kontaktai">%(cta)s</a>
    </nav>
    %(langs)s
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="%(menuaria)s">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<nav class="mobile-nav" id="mobile-nav" aria-label="%(mobaria)s">
  <a class="btn solid" href="#kontaktai">%(cta)s</a>
  %(mob)s
</nav>
""" % {"skip": c["skip"], "mark": MARK, "nav": nav, "mob": mob, "cta": c["navCta"],
       "navaria": attr(c["navAria"]), "mobaria": attr(c["menuAria"]),
       "menuaria": attr(c["menuBtnAria"]),
       "langs": langmenu(lang, c["langAria"])}


def hero(lang, c):
    h = c["hero"]
    facts = "\n        ".join("<span>%s</span>" % f for f in h["facts"])
    # „Vardas — vaidmuo · vaidmuo“: vardas atskiroje eilutėje, o taškas
    # lieka prie ankstesnio žodžio, kad eilutė neprasidėtų „·“
    name, roles = h["roles"].split(" — ", 1)
    roles = ('<span class="tl-name">%s</span><span class="tl-roles">%s</span>'
             % (name, roles.replace(" · ", "&nbsp;· ")))
    return """
<main id="top">
<span id="turinys"></span>

<!-- ---------- HERO ---------- -->
<div class="hero">
  <svg class="halo" aria-hidden="true"><use href="#mark"/></svg>
  <div class="in">
    <div>
      <p class="tagline">%(roles)s</p>
      <h1>%(h1)s</h1>
      <p class="kicker">%(kicker)s</p>
      <p class="sub">%(sub)s</p>
      <div class="acts">
        <a class="btn solid" href="#kontaktai">%(cta1)s</a>
        <a class="btn" href="#programos">%(cta2)s</a>
      </div>
      <div class="hero-facts">
        %(facts)s
      </div>
    </div>

    <figure class="portrait" data-photo>
      <svg class="ph-empty" viewBox="0 0 100 100" aria-hidden="true"><use href="#mark"/></svg>
      <img src="%(b)sassets/img/elena.jpg" alt="%(alt)s" width="1000" height="1000" data-optional>
      <figcaption>
        <b>Elena Daunytė</b>
        <span>%(role)s</span>
      </figcaption>
    </figure>
  </div>
</div>
""" % {"roles": roles, "h1": h["h1"], "kicker": h["kicker"], "sub": h["sub"], "cta1": h["ctaPrimary"], "cta2": h["ctaSecondary"],
       "facts": facts, "b": BASE[lang], "alt": attr(h["portraitAlt"]), "role": h["portraitRole"]}


def services(lang, c):
    s = c["services"]
    cards = []
    for it in s["items"]:
        tag = ' <span class="tag-new">%s</span>' % it["tag"] if it.get("tag") else ""
        cards.append("""<article class="card">
        %(fig)s
        <div class="tx">
          <h3>%(h3)s%(tag)s</h3>
          <p>%(p)s</p>
          <a class="more" href="%(href)s">%(more)s</a>
        </div>
      </article>""" % {"fig": photo(BASE[lang], it["img"], it["alt"]), "h3": it["h3"],
                       "tag": tag, "p": it["p"], "href": it["moreHref"], "more": it["more"]})
    # plati nuotrauka-juosta po įvadu (neprivaloma: "banner" su img, alt, cap)
    banner = ""
    if s.get("banner"):
        bn = s["banner"]
        banner = """
    <figure class="svc-banner reveal">
      <img src="%sassets/img/%s" alt="%s" width="1600" height="686">
      <figcaption>%s%s</figcaption>
    </figure>
""" % (BASE[lang], bn["img"], attr(bn["alt"]),
       ('<span class="svc-banner-tag">%s</span>' % bn["tag"]) if bn.get("tag") else "", bn["cap"])
    return """
<!-- ---------- PASLAUGOS ---------- -->
<section id="paslaugos" class="band-cream">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>
%(banner)s
    <div class="grid3 reveal">
      %(cards)s
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": s["eyebrow"], "h2": s["h2"], "lede": s["lede"],
       "cards": "\n\n      ".join(cards), "motto": MOTTO, "banner": banner}


def video_item(base, v):
    if "file" in v or "youtube" in v:
        # Visas aprašymas matomas iš karto, bet apačioje išblunka; mygtukas
        # „Skaityti daugiau“ jį išskleidžia (be JS tekstas rodomas visas).
        more = ""
        if v.get("more") or v.get("facts") or v.get("closing"):
            paras = "".join("\n            <p>%s</p>" % x for x in v.get("more", []))
            facts = "".join("\n              <dt>%s</dt><dd>%s</dd>" % (f["k"], f["v"])
                            for f in v.get("facts", []))
            more = """%s
            <dl>%s
            </dl>
            <p class="clip-closing">%s</p>""" % (paras, facts, v.get("closing", ""))
        toggle = ""
        if more:
            toggle = ('\n          <button class="clip-toggle" type="button" aria-expanded="false" hidden '
                      'data-more="%s" data-less="%s">%s</button>'
                      % (attr(v["moreLabel"]), attr(v["lessLabel"]), v["moreLabel"]))
        # "Įsigyti" — atidaro laišką su paruošta tema (kol nėra el. parduotuvės)
        # „Užsakyti renginį“ — veda į kontaktų formą ir iš anksto parenka temą
        buy = ""
        acts = []
        if v.get("bookLabel"):
            acts.append('<a class="btn solid" href="#kontaktai" data-book-option="%s" data-book-message="%s">%s</a>'
                        % (attr(v["bookOption"]), attr(v["bookMessage"]), v["bookLabel"]))
        if v.get("buyLabel"):
            # laiško šablonas: egzempliorių skaičius, vardas, adresas ir mokėjimo rekvizitai
            body = "\r\n".join(v.get("buyBody", [])).format(name=BANK_NAME, iban=BANK_IBAN)
            acts.append('<a class="btn" href="mailto:%s?subject=%s&amp;body=%s">%s</a>'
                        % (EMAIL, urllib.parse.quote(v["buySubject"]), urllib.parse.quote(body),
                           v["buyLabel"]))
        if acts:
            buy = '\n          <div class="clip-acts">\n            %s\n          </div>' % "\n            ".join(acts)
        if "youtube" in v:
            player = ('<div class="clip-yt"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" '
                      'title="%s" loading="lazy" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" '
                      'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">'
                      '</iframe></div>' % (attr(v["youtube"]), attr(v["title"])))
        else:
            player = ('<video controls playsinline preload="none" poster="%s%s" aria-label="%s">\n'
                      '          <source src="%s%s" type="video/mp4">\n        </video>'
                      % (base, attr(v["poster"]), attr(v["title"]), base, attr(v["file"])))
        sub = '\n          <span class="clip-sub">%s</span>' % v["subtitle"] if v.get("subtitle") else ""
        lead = '\n          <span class="clip-lead">%s</span>' % v["lead"] if v.get("lead") else ""
        return """<figure class="clip">
        %(player)s
        <figcaption>
          <span class="clip-cat">%(cat)s</span>
          <b>%(title)s</b>%(sub)s%(lead)s
          <div class="clip-text">
            <p class="clip-note">%(note)s</p>%(more)s
          </div>%(toggle)s%(callout)s
          <span class="clip-meta">%(meta)s</span>%(buy)s
        </figcaption>
      </figure>""" % {"player": player, "cat": v["cat"], "title": attr(v["title"]), "note": v["note"],
                      "sub": sub, "lead": lead, "more": more, "toggle": toggle,
                      "callout": ('\n          <p class="clip-callout">%s</p>' % v["callout"]) if v.get("callout") else "",
                      "meta": v.get("meta", ""),
                      "buy": buy}
    return ('<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/%s" '
            'title="%s" loading="lazy" allowfullscreen '
            'allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe></div>'
            % (attr(v["id"]), attr(v["title"])))


def media(lang, c):
    m = c["media"]
    # Kai JSON faile atsiranda "videos" sąrašas, vietoj tuščių vietų rodomi
    # tikri įrašai. Kol sąrašas tuščias arba jo nėra — rodomos vietos.
    # Įrašas su "id" — paprastas YouTube (16:9) be aprašymo; su "youtube" —
    # vertikalus YouTube Short'as, o su "file" — vaizdo failas iš assets/video/
    # (su viršeliu "poster"). Abu pastarieji rodomi su kategorija "cat", aprašymu "note",
    # data bei vieta "meta"). Neprivalomi: "subtitle", "lead", o "more",
    # "facts" ir "closing" rodomi išblunkantys, kol paspaudžiamas "moreLabel".
    videos = m.get("videos") or []
    if videos:
        slots = "\n      ".join(video_item(BASE[lang], v) for v in videos)
    else:
        slots = "\n      ".join(
            '<div class="slot-dark"><strong>%s</strong><span>%s</span></div>' % (s["t"], s["d"])
            for s in m["slots"])
    return """
<!-- ---------- ĮRAŠAI ---------- -->
<section id="irasai" class="band-teal">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <a class="media-card reveal" href="https://www.lrt.lt/mediateka/irasas/2000197212/klipvid-2021-elena-daunyte-ryto-ugnis" target="_blank" rel="noopener">
      <span class="media-play" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="currentColor"><path d="M6.5 4.2v11.6L16 10 6.5 4.2Z"/></svg>
      </span>
      <span class="media-body">
        <span class="media-label">%(label)s</span>
        <b>Elena Daunytė — „Ryto ugnis“</b>
        <span class="media-note">%(note)s</span>
      </span>
      <span class="media-go" aria-hidden="true">
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h7v7M13 3 3.5 12.5"/></svg>
      </span>
    </a>

    <div class="video-slots reveal">
      <!-- ĮDĖTI: <div class="video"><iframe src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe></div> -->
      %(slots)s
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": m["eyebrow"], "h2": m["h2"], "lede": m["lede"],
       "label": m["cardLabel"], "note": m["cardNote"], "slots": slots, "motto": MOTTO}


def who(lang, c):
    items = "\n      ".join(
        """<div class="who">
        <span class="n">%s</span>
        <h3>%s</h3>
        <p>%s</p>
      </div>""" % (i["n"], i["h3"], i["p"]) for i in c["who"]["items"])
    return """
<!-- ---------- KAM SKIRTA ---------- -->
<section id="kam">
  <div class="in">
    <div class="who-grid reveal">
      %s
    </div>

    %s
  </div>
</section>
""" % (items, MOTTO)


def edu(lang, c):
    e = c["edu"]
    arts = []
    for a in e["items"]:
        facts = "\n          ".join(
            '<li><b>%s</b><span>%s</span></li>' % (f["k"], f["v"]) for f in a["facts"])
        arts.append("""<article>
        <h3>%(h3)s</h3>
        <p>%(p)s</p>
        <ul class="facts">
          %(facts)s
        </ul>
      </article>""" % {"h3": a["h3"], "p": a["p"], "facts": facts})
    notes = "\n    ".join('<p class="after-note reveal">%s</p>' % n for n in e["notes"])
    return """
<!-- ---------- EDUKACIJOS ---------- -->
<section id="edukacijos" class="band-cream">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <div class="edu reveal">
      %(arts)s
    </div>

    %(notes)s

    %(motto)s
  </div>
</section>
""" % {"eyebrow": e["eyebrow"], "h2": e["h2"], "lede": e["lede"],
       "arts": "\n\n      ".join(arts), "notes": notes, "motto": MOTTO}


def programs(lang, c):
    p = c["programs"]
    arts = []
    for a in p["items"]:
        tag = ' <span class="tag-new">%s</span>' % a["tag"] if a.get("tag") else ""
        specs = "\n          ".join(
            '<div><span class="k">%s</span><span class="v">%s</span></div>' % (s["k"], s["v"])
            for s in a["specs"])
        arts.append("""<article class="prog">
        <div>
          <h3>%(h3)s%(tag)s</h3>
          <p>%(p)s</p>
        </div>
        <div class="prog-specs">
          %(specs)s
        </div>
      </article>""" % {"h3": a["h3"], "tag": tag, "p": a["p"], "specs": specs})
    return """
<!-- ---------- PROGRAMOS ---------- -->
<section id="programos">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <div class="programs reveal">
      %(arts)s
    </div>

    <p class="after-note reveal">%(note)s</p>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": p["eyebrow"], "h2": p["h2"], "lede": p["lede"],
       "arts": "\n\n      ".join(arts), "note": p["note"], "motto": MOTTO}


def growth(lang, c):
    g = c["growth"]
    paras = "\n      ".join("<p>%s</p>" % x for x in g["paras"])
    steps = "\n      ".join(
        """<li>
        <span class="n">%02d</span>
        <b>%s</b>
        <span>%s</span>
      </li>""" % (i + 1, s["k"], s["v"]) for i, s in enumerate(g["steps"]))
    return """
<!-- ---------- ASMENINIS AUGIMAS: ŽMOGUS — INSTRUMENTAS ---------- -->
<section id="augimas" class="band-teal">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <div class="manifest reveal">
      %(paras)s
    </div>

    <p class="path-intro reveal">%(intro)s</p>
    <ol class="path reveal">
      %(steps)s
    </ol>

    <p class="manifest-close reveal">%(closing)s</p>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": g["eyebrow"], "h2": g["h2"], "lede": g["lede"], "paras": paras,
       "intro": g["pathIntro"], "steps": steps, "closing": g["closing"], "motto": MOTTO}


def art_exchange(lang, c):
    a = c["artExchange"]
    tag = ' <span class="tag-new">%s</span>' % a["tag"] if a.get("tag") else ""
    paras = "\n        ".join("<p>%s</p>" % x for x in a["paras"])
    iv = a["interview"]
    return """
<!-- ---------- MENAIS MAINAIS ---------- -->
<section id="menais-mainais" class="band-cream">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s%(tag)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <div class="two exchange reveal">
      <div>
        %(paras)s
        <p class="accent">%(accent)s</p>
        <a class="btn dark" href="#kontaktai">%(cta)s</a>
      </div>

      <a class="media-card light" href="%(url)s" target="_blank" rel="noopener">
        <span class="media-play" aria-hidden="true">
          <svg viewBox="0 0 20 20" fill="currentColor"><path d="M4 11.6C4 8 6 5.6 9 4.5l.7 1.4C8 6.7 7.1 8 7 9.4h2.6V16H4v-4.4Zm7.4 0c0-3.6 2-6 5-7.1l.7 1.4c-1.7.8-2.6 2.1-2.7 3.5H17V16h-5.6v-4.4Z"/></svg>
        </span>
        <span class="media-body">
          <span class="media-label">%(ivlabel)s</span>
          <b>%(ivtitle)s</b>
          <span class="media-note">%(ivnote)s</span>
        </span>
        <span class="media-go" aria-hidden="true">
          <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h7v7M13 3 3.5 12.5"/></svg>
        </span>
      </a>
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": a["eyebrow"], "h2": a["h2"], "tag": tag, "lede": a["lede"],
       "paras": paras, "accent": a["accent"], "cta": a["cta"], "url": attr(iv["url"]),
       "ivlabel": iv["label"], "ivtitle": iv["title"], "ivnote": iv["note"], "motto": MOTTO}


def studio(lang, c):
    s = c["studio"]
    pts = "\n          ".join("<li>%s</li>" % x for x in s["points"])
    return """
<!-- ---------- STUDIJA ---------- -->
<section id="studija" class="band-teal">
  <div class="in">
    <div class="two studio reveal">
      <div>
        <p class="eyebrow">%(eyebrow)s</p>
        <h2>%(h2)s</h2>
        <p class="lede">%(lede)s</p>
        <ul class="creds">
          %(pts)s
        </ul>
        <a class="btn" href="#kontaktai">%(cta)s</a>
      </div>
      <div class="about-photo" data-photo>
        <svg class="ph-empty" viewBox="0 0 100 100" aria-hidden="true"><use href="#mark"/></svg>
        <img src="%(b)sassets/img/studija.jpg" alt="%(alt)s" data-optional>
      </div>
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": s["eyebrow"], "h2": s["h2"], "lede": s["lede"], "pts": pts,
       "cta": s["cta"], "b": BASE[lang], "alt": attr(s["alt"]), "motto": MOTTO}


def gallery(lang, c):
    g = c["gallery"]
    figs = "\n      ".join(photo(BASE[lang], i["img"], i["alt"], cap=i["cap"]) for i in g["items"])
    return """
<!-- ---------- GALERIJA ---------- -->
<section id="galerija" class="band-cream">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>

    <div class="gallery reveal" data-lb-close="%(lbclose)s" data-lb-prev="%(lbprev)s" data-lb-next="%(lbnext)s">
      %(figs)s
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": g["eyebrow"], "h2": g["h2"], "lede": g["lede"], "figs": figs, "motto": MOTTO, "lbclose": attr(g["lightbox"]["close"]), "lbprev": attr(g["lightbox"]["prev"]), "lbnext": attr(g["lightbox"]["next"])}


def about(lang, c):
    a = c["about"]
    paras = "\n        ".join("<p>%s</p>" % x for x in a["paras"])
    creds = "\n          ".join("<li>%s</li>" % x for x in a["creds"])
    return """
<!-- ---------- APIE ---------- -->
<section id="apie">
  <div class="in">
    <div class="two about reveal">
      <div>
        <p class="eyebrow">%(eyebrow)s</p>
        <h2>%(h2)s</h2>
        %(paras)s

        <ul class="creds">
          %(creds)s
        </ul>

        <p>%(last)s</p>
        <a class="btn dark" href="#kontaktai">%(cta)s</a>
      </div>

      <div class="about-photo" data-photo>
        <svg class="ph-empty" viewBox="0 0 100 100" aria-hidden="true"><use href="#mark"/></svg>
        <img src="%(b)sassets/img/apie.jpg" alt="%(alt)s" data-optional>
      </div>
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": a["eyebrow"], "h2": a["h2"], "paras": paras, "creds": creds,
       "last": a["closing"], "cta": a["cta"], "b": BASE[lang], "alt": attr(a["alt"]),
       "motto": MOTTO}


def quotes(lang, c):
    q = c["quotes"]
    slots = "\n      ".join(
        '<div class="slot"><strong>%s</strong><span>%s</span></div>' % (s["t"], s["d"])
        for s in q["slots"])
    return """
<!-- ---------- ATSILIEPIMAI ---------- -->
<section id="atsiliepimai" class="band-cream">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
      <p class="lede">%(lede)s</p>
    </div>
    <div class="quotes reveal">
      %(slots)s
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": q["eyebrow"], "h2": q["h2"], "lede": q["lede"], "slots": slots, "motto": MOTTO}


def faq(lang, c):
    f = c["faq"]
    items = "\n      ".join(
        """<details>
        <summary>%s</summary>
        <div class="ans">%s</div>
      </details>""" % (i["q"], i["a"]) for i in f["items"])
    return """
<!-- ---------- DUK ---------- -->
<section id="duk">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
    </div>
    <div class="faq reveal">
      %(items)s
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": f["eyebrow"], "h2": f["h2"], "items": items, "motto": MOTTO}


def patreon(lang, c):
    p = c["patreon"]
    # Kol "url" tuščias, rodoma pažymėta vieta su užrašu „netrukus“.
    # Įrašius Patreon nuorodą, vietoj jos atsiranda mygtukas.
    if p.get("url"):
        action = ('<a class="btn dark" href="%s" target="_blank" rel="noopener">%s</a>'
                  % (attr(p["url"]), p["btn"]))
    else:
        action = '<div class="slot"><strong>%s</strong><span>%s</span></div>' % (
            p["soonTitle"], p["soonText"])
    return """
<!-- ---------- PARAMA (PATREON) ---------- -->
<section id="parama" class="band-cream">
  <div class="in">
    <div class="two patreon reveal">
      <div>
        <p class="eyebrow">%(eyebrow)s</p>
        <h2>%(h2)s</h2>
        <p class="lede">%(lede)s</p>
      </div>
      <div class="patreon-box">
        %(action)s
      </div>
    </div>

    %(motto)s
  </div>
</section>
""" % {"eyebrow": p["eyebrow"], "h2": p["h2"], "lede": p["lede"], "action": action,
       "motto": MOTTO}


def cta(lang, c):
    x = c["cta"]
    return """
<!-- ---------- CTA ---------- -->
<section class="band-teal cta">
  <div class="in">
    <h2>%s</h2>
    <p class="lede">%s</p>
    <a class="btn solid" href="#kontaktai">%s</a>

    %s
  </div>
</section>
""" % (x["h2"], x["lede"], x["btn"], MOTTO)


def contact(lang, c):
    k = c["contact"]
    f = k["fields"]
    opts = "\n              ".join("<option>%s</option>" % o for o in k["options"])
    direct = []
    for d in k["direct"]:
        if d["type"] == "tel":
            v = '<a href="tel:+37067004184">+370 670 04184</a>'
        elif d["type"] == "email":
            v = '<a data-email href="mailto:%s">%s</a>' % (EMAIL, EMAIL)
        elif d["type"] == "facebook":
            v = ('<a class="fb-link" href="%s" target="_blank" rel="noopener">%sFeelHarmonic</a>'
                 % (FACEBOOK, FB_ICON))
        else:
            v = d["v"]
        direct.append("<dt>%s</dt>\n        <dd>%s</dd>" % (d["k"], v))
    js = c["js"]
    data = " ".join('data-%s="%s"' % (key, attr(val)) for key, val in js.items())
    return """
<!-- ---------- KONTAKTAI ---------- -->
<section id="kontaktai">
  <div class="in">
    <div class="head reveal">
      <p class="eyebrow">%(eyebrow)s</p>
      <h2>%(h2)s</h2>
    </div>

    <div class="two reveal">
      <form id="uzklausa" novalidate %(data)s>
        <div class="row2">
          <div class="field"><label for="v">%(f_name)s</label><input id="v" name="vardas" type="text" autocomplete="name" required></div>
          <div class="field"><label for="i">%(f_org)s</label><input id="i" name="istaiga" type="text" autocomplete="organization"></div>
        </div>
        <div class="row2">
          <div class="field"><label for="e">%(f_mail)s</label><input id="e" name="pastas" type="email" autocomplete="email" required></div>
          <div class="field"><label for="t">%(f_tel)s</label><input id="t" name="telefonas" type="tel" autocomplete="tel"></div>
        </div>
        <div class="row2">
          <div class="field">
            <label for="k">%(f_type)s</label>
            <select id="k" name="tipas">
              %(opts)s
            </select>
          </div>
          <div class="field"><label for="d">%(f_date)s</label><input id="d" name="data" type="text" placeholder="%(p_date)s"></div>
        </div>
        <div class="field"><label for="z">%(f_msg)s</label><textarea id="z" name="zinute" placeholder="%(p_msg)s"></textarea></div>

        <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">

        <button class="btn dark" type="submit">%(submit)s</button>
        <p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
      </form>

      <dl class="direct">
        %(direct)s
      </dl>
    </div>

    %(motto)s
  </div>
</section>
</main>
""" % {"eyebrow": k["eyebrow"], "h2": k["h2"], "data": data, "opts": opts, "motto": MOTTO,
       "f_name": f["name"], "f_org": f["org"], "f_mail": f["email"], "f_tel": f["phone"],
       "f_type": f["type"], "f_date": f["date"], "p_date": attr(f["datePlaceholder"]),
       "f_msg": f["message"], "p_msg": attr(f["messagePlaceholder"]),
       "submit": k["submit"], "direct": "\n        ".join(direct)}


def footer(lang, c):
    f = c["footer"]
    items = shown(f["pages"])
    # Parama — paslėpta kaip skiltis, bet jei Patreon nuoroda jau yra, poraštėje
    # rodoma kaip nuoroda tiesiai į Patreon
    url = c["patreon"].get("url")
    if "parama" in PASLEPTA and url:
        items = [dict(i, href=url) if i["href"] == "#parama" else i for i in f["pages"]
                 if i["href"].lstrip("#") not in PASLEPTA - {"parama"}]
    pages = "\n          ".join(
        '<li><a href="%s"%s>%s</a></li>'
        % (i["href"], "" if i["href"].startswith("#") else ' target="_blank" rel="noopener"', i["label"])
        for i in items)
    details = "\n          ".join("<li>%s</li>" % x for x in f["details"])
    return """
<!-- ---------- PORAŠTĖ ---------- -->
<footer>
  <div class="in">
    <div class="cols">
      <div>
        <div class="fbrand">
          <svg aria-hidden="true"><use href="#mark-sm"/></svg>
          <div><b>FeelHarmonic</b><span class="tg">Let it come!</span></div>
        </div>
        <p style="max-width:34ch;margin:0 0 18px">%(about)s</p>
        <a class="fb-round" href="%(fb)s" target="_blank" rel="noopener" aria-label="%(fbaria)s" title="Facebook">%(fbicon)s</a>
      </div>
      <div>
        <h4>%(colpages)s</h4>
        <ul>
          %(pages)s
        </ul>
      </div>
      <div>
        <h4>%(coldetails)s</h4>
        <ul>
          %(details)s
          <li><a data-email href="mailto:%(email)s">%(email)s</a></li>
          <li><a href="tel:+37067004184">+370 670 04184</a></li>
        </ul>
      </div>
    </div>
    <div class="fbot">
      <span>&copy; <span id="year">%(year)s</span> FeelHarmonic</span>
      <span>%(credit)s</span>
      <span>%(city)s</span>
    </div>
  </div>
</footer>
""" % {"about": f["about"], "colpages": f["colPages"], "pages": pages,
       "coldetails": f["colDetails"], "credit": f["photoCredit"], "details": details, "city": f["city"], "email": EMAIL,
       "year": datetime.date.today().year,
       "fb": FACEBOOK, "fbaria": attr(f["facebookAria"]), "fbicon": FB_ICON}


def jsonld(lang, c):
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "name": "Elena Daunytė",
                "jobTitle": c["schema"]["jobTitle"],
                "url": SITE + HREF[lang],
                "email": EMAIL,
                "telephone": "+370 670 04184",
                "worksFor": {"@type": "Organization", "name": "FeelHarmonic",
                             "slogan": "Let it come!", "url": SITE + "/",
                             "sameAs": [FACEBOOK]},
                "knowsLanguage": ["lt", "en", "it"],
                "knowsAbout": c["schema"]["knowsAbout"],
            },
            {
                "@type": "FAQPage",
                "inLanguage": lang,
                "mainEntity": [
                    {"@type": "Question", "name": q["q"],
                     "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
                    for q in c["schema"]["faq"]
                ],
            },
        ],
    }
    return ('\n<script type="application/ld+json">\n%s\n</script>\n'
            % json.dumps(data, ensure_ascii=False, indent=2))


# Laikinai paslėptos skiltys (pagal jų id). Kad grąžintumėte — ištrinkite id iš
# sąrašo ir paleiskite build.py; tekstai turinys/*.json lieka nepaliesti.
#   studija      — kol studija tik „Rengiama“
#   atsiliepimai — kol nėra tikrų atsiliepimų (dabar ten pastabos savininkei)
#   parama       — kol nėra Patreon puslapio; kai "patreon.url" užpildytas,
#                  poraštėje atsiranda nuoroda tiesiai į Patreon
PASLEPTA = {"studija", "atsiliepimai", "parama"}


def shown(items):
    """Meniu ir poraštės nuorodos be paslėptų skilčių."""
    return [i for i in items if i["href"].lstrip("#") not in PASLEPTA]


def page(lang, c):
    return "".join([
        head(lang, c), header(lang, c), hero(lang, c), services(lang, c), media(lang, c),
        who(lang, c), edu(lang, c), programs(lang, c), growth(lang, c), art_exchange(lang, c),
        "" if "studija" in PASLEPTA else studio(lang, c),
        gallery(lang, c), about(lang, c),
        "" if "atsiliepimai" in PASLEPTA else quotes(lang, c),
        faq(lang, c),
        "" if "parama" in PASLEPTA else patreon(lang, c),
        cta(lang, c), contact(lang, c),
        footer(lang, c), jsonld(lang, c),
        '\n<script src="%sassets/js/main.js?v=%s"></script>\n</body>\n</html>\n' % (BASE[lang], ver("assets/js/main.js")),
    ])


def sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for lang in LANGS:
        links = "\n".join(
            '    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (o, SITE, HREF[o])
            for o in LANGS)
        urls.append("""  <url>
    <loc>%s%s</loc>
%s
    <lastmod>%s</lastmod>
    <changefreq>monthly</changefreq>
    <priority>%s</priority>
  </url>""" % (SITE, HREF[lang], links, today, "1.0" if lang == "lt" else "0.8"))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(urls) + "\n</urlset>\n")


def main():
    for lang in LANGS:
        with open(CONTENT / ("%s.json" % lang), encoding="utf-8") as fh:
            c = json.load(fh)
        out = OUT[lang]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, c), encoding="utf-8")
        print("parasyta  %s" % out.relative_to(ROOT))
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    print("parasyta  sitemap.xml")


if __name__ == "__main__":
    main()
