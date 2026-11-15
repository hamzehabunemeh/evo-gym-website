"""Shared layout: head, header, drawer, footer, helpers."""
from icons import ico, hexsvg

PHONE = "0790080089"
PHONE_INTL = "+962790080089"
WA = "https://wa.me/962790080089"
IG = "https://www.instagram.com/evogymjo"
FB = "https://www.facebook.com/share/1JCeuu7TR3/?mibextid=wwXIfr"
MAPS = "https://maps.app.goo.gl/uYDt4tNhS5wwLRuU8"
MAP_EMBED = "https://maps.google.com/maps?q=EVO%20Gym%2C%20XRWM%2B693%2C%20Amman%2C%20Jordan&z=16&output=embed"

NAV = [
    ("index.html", "Home", "الرئيسية"),
    ("membership.html", "Membership", "الاشتراكات"),
    ("trainers.html", "Trainers", "المدربون"),
    ("hours.html", "Opening Hours", "ساعات العمل"),
    ("services.html", "Services", "الخدمات"),
    ("classes.html", "Classes Schedule", "جدول الحصص"),
    ("tools.html", "Fitness Tools", "أدوات اللياقة"),
    ("gallery.html", "Gallery", "المعرض"),
    ("careers.html", "Careers", "التوظيف"),
    ("contact.html", "Contact Us", "تواصل معنا"),
]


def T(en, ar):
    """Bilingual inline text."""
    return f'<span class="l-en">{en}</span><span class="l-ar" lang="ar">{ar}</span>'


def TB(en, ar, tag="p", cls=""):
    """Bilingual block."""
    c = f' class="{cls}"' if cls else ""
    return (f'<{tag}{c}><span class="l-en">{en}</span><span class="l-ar" lang="ar">{ar}</span></{tag}>')


def ph(en, ar):
    return f'placeholder="{en}" data-ph-en="{en}" data-ph-ar="{ar}"'


EARLY = ("<script>(function(){var l='en';try{l=localStorage.getItem('evo-lang')||'en'}catch(e){}"
         "var d=document.documentElement;d.lang=l;d.dir=l==='ar'?'rtl':'ltr';"
         "var t=d.getAttribute('data-title-'+l);if(t)document.title=t;})();</script>")


def head(title_en, title_ar, desc):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr" data-title-en="{title_en}" data-title-ar="{title_ar}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title_en}</title>
{EARLY}
<meta name="description" content="{desc}">
<meta name="theme-color" content="#040607">
<meta property="og:title" content="{title_en}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/brand/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/img/brand/favicon.png">
<link rel="apple-touch-icon" href="assets/img/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/barlow-condensed-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
</head>
"""


def header(active):
    ACT = ' class="active" aria-current="page"'
    links = "".join(
        f'<a href="{h}"{ACT if h == active else ""}>{T(en, ar)}</a>'
        for h, en, ar in NAV)
    dlinks = "".join(
        f'<a href="{h}"{ACT if h == active else ""}>{T(en, ar)}'
        f'<small>{i + 1:02d}</small></a>'
        for i, (h, en, ar) in enumerate(NAV))
    return f"""<body>
<a href="#main" class="skip">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<div class="grain" aria-hidden="true"></div>
<header class="header">
  <div class="header__inner">
    <a class="logo" href="index.html" aria-label="EVO GYM home"><img src="assets/img/brand/logo-440.png" alt="EVO GYM" width="220" height="80"></a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="header__actions">
      <button class="lang-btn" type="button" data-label-en="Switch to Arabic" data-label-ar="التبديل إلى الإنجليزية" aria-label="Switch to Arabic">{ico("globe")}<span class="l-en">عربي</span><span class="l-ar">EN</span></button>
      <button class="burger" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" aria-hidden="false">
  <div class="drawer__bg"></div>
  <div class="drawer__panel" data-lenis-prevent>
    <nav aria-label="Mobile">{dlinks}</nav>
    <div class="drawer__foot">
      <a class="btn btn--primary" href="contact.html#trial">{T("Book a Free Trial", "احجز حصة تجريبية مجانية")}</a>
      <a class="btn btn--ghost" href="{WA}" target="_blank" rel="noopener">{ico("wa")}{T("WhatsApp", "واتساب")}</a>
    </div>
  </div>
</div>
<main id="main">
"""


def ribbon(cls="", style=""):
    return f"""<svg class="ribbon {cls}" style="{style}" viewBox="0 0 1440 320" preserveAspectRatio="none" aria-hidden="true">
<defs><linearGradient id="rg" x1="0" x2="1"><stop offset="0" stop-color="#2ee6f5" stop-opacity="0"/><stop offset=".3" stop-color="#2ee6f5"/><stop offset=".7" stop-color="#4fd1c5"/><stop offset="1" stop-color="#4fd1c5" stop-opacity="0"/></linearGradient></defs>
<path d="M-40 250 C 180 60, 380 40, 540 190 S 860 330, 1010 170 S 1300 10, 1480 120"/></svg>"""


def fx(variant=1):
    if variant == 1:
        return f"""<div class="fx" aria-hidden="true">
  <div class="fx__glow" style="top:-20%;inset-inline-end:-15%"></div>
  <div class="fx__glow" style="bottom:-35%;inset-inline-start:-25%;opacity:.6"></div>
  <div class="fx__hex float" style="top:16%;inset-inline-start:6%;width:70px">{hexsvg()}</div>
  <div class="fx__hex float d2" style="top:62%;inset-inline-start:42%;width:46px;opacity:.3">{hexsvg()}</div>
  <div class="fx__hex float d3" style="top:10%;inset-inline-end:8%;width:110px;opacity:.25">{hexsvg()}</div>
  {ribbon("", "top:auto;bottom:4%;opacity:.55")}
</div>"""
    return f"""<div class="fx" aria-hidden="true">
  <div class="fx__glow" style="top:-40%;inset-inline-end:-20%"></div>
  <div class="fx__hex float" style="top:28%;inset-inline-end:12%;width:90px;opacity:.35">{hexsvg()}</div>
  <div class="fx__hex float d2" style="top:58%;inset-inline-end:30%;width:40px;opacity:.25">{hexsvg()}</div>
  {ribbon("", "bottom:0;opacity:.45")}
</div>"""


def page_hero(crumb_en, crumb_ar, title_html, lead_en, lead_ar, bgword):
    return f"""<section class="page-hero">
  {fx(2)}
  <div class="page-hero__bgword" aria-hidden="true">{bgword}</div>
  <div class="container">
    <div class="crumbs fade-up"><a href="index.html">{T("Home", "الرئيسية")}</a><span>/</span><span class="accent">{T(crumb_en, crumb_ar)}</span></div>
    <h1 class="fade-up d1">{title_html}</h1>
    {TB(lead_en, lead_ar, "p", "lead fade-up d2")}
  </div>
</section>
"""


def cta_band():
    return f"""<section class="section--tight">
  <div class="container">
    <div class="cta reveal zoom">
      {fx(2)}
      <div class="cta__inner">
        <div>
          <span class="eyebrow">{T("Start today", "ابدأ اليوم")}</span>
          <h2 class="h-lg">{T('Your evolution <span class="accent">starts now</span>', 'تطوّرك <span class="accent">يبدأ الآن</span>')}</h2>
        </div>
        <div class="btn-row">
          <a class="btn btn--primary" href="contact.html#trial">{T("Book a Free Trial", "احجز حصة تجريبية")}{ico("arrow", "flip-rtl btn-ico")}</a>
          <a class="btn btn--ghost" href="{WA}" target="_blank" rel="noopener">{ico("wa")}{T("Chat on WhatsApp", "راسلنا على واتساب")}</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def footer():
    links1 = "".join(f'<li><a href="{h}">{T(en, ar)}</a></li>' for h, en, ar in NAV[:5])
    links2 = "".join(f'<li><a href="{h}">{T(en, ar)}</a></li>' for h, en, ar in NAV[5:])
    return f"""</main>
<footer class="footer">
  <div class="container">
    <div class="footer__big" aria-hidden="true">Train. Transform. Evolve.</div>
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/img/brand/logo-440.png" alt="EVO GYM" width="220" height="80" loading="lazy">
        {TB("A premium mixed training facility in Dabouq, Amman — led by expert coaches. More than machines.",
            "نادٍ رياضي مختلط وفاخر في دابوق، عمّان — بقيادة مدربين محترفين. أكثر من مجرد أجهزة.")}
        <div class="socials">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ico("instagram")}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ico("facebook")}</a>
          <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico("wa")}</a>
          <a href="tel:{PHONE_INTL}" aria-label="Call">{ico("phone")}</a>
        </div>
      </div>
      <div><h4>{T("Explore", "استكشف")}</h4><ul>{links1}</ul></div>
      <div><h4>{T("More", "المزيد")}</h4><ul>{links2}</ul></div>
      <div>
        <h4>{T("Opening Hours", "ساعات العمل")}</h4>
        <ul class="f-hours">
          <li><span>{T("Sat – Thu", "السبت – الخميس")}</span><b dir="ltr">6 AM – 11 PM</b></li>
          <li><span>{T("Friday", "الجمعة")}</span><b dir="ltr">9 AM – 9 PM</b></li>
        </ul>
        <h4 style="margin-top:26px">{T("Visit", "زورونا")}</h4>
        <ul>
          <li><a href="{MAPS}" target="_blank" rel="noopener">{T("Dabouq District, Amman", "منطقة دابوق، عمّان")}</a></li>
          <li><a href="tel:{PHONE_INTL}" dir="ltr">{PHONE}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> EVO GYM. {T("All rights reserved.", "جميع الحقوق محفوظة.")}</span>
      <span>{T("Train. Transform. Evolve.", "تمرّن. تحوّل. تطوّر.")}</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico("wa")}</a>
<button class="to-top" type="button" aria-label="Back to top">{ico("up")}</button>
<script src="assets/js/vendor/lenis.min.js" defer></script>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page(active, title_en, title_ar, desc, body):
    return head(title_en, title_ar, desc) + header(active) + body + footer()
