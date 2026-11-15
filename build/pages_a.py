from layout import T, TB, fx, page_hero, cta_band, WA, MAPS, MAP_EMBED, PHONE, PHONE_INTL, IG
from icons import ico, hexsvg

MARQ_WORDS = [("Train", "o"), ("Transform", ""), ("Evolve", "o"), ("Focus", ""), ("Strength", "o"),
              ("Cardio", ""), ("Cycling", "o"), ("CrossFit", ""), ("Pilates", "o"), ("Boxing", "")]


def marquee(tilt=False):
    item = "".join(f'<span class="{c}">{w}</span>{ico("spark")}' for w, c in MARQ_WORDS)
    return (f'<div class="marquee{" marquee--tilt" if tilt else ""}" dir="ltr" aria-hidden="true">'
            f'<div class="marquee__track"><div class="marquee__item">{item}</div><div class="marquee__item">{item}</div></div></div>')


# ------------------------------------------------------------------ HOME
def home():
    tiles = [
        ("dumbbell", "Free Weights Zone", "منطقة الأوزان الحرة",
         "Full dumbbell runs, barbell racks and plate-loaded machines — everything you need to build real strength.",
         "صفوف كاملة من الدمبلز ورفوف البارات وأجهزة الأوزان — كل ما تحتاجه لبناء قوة حقيقية."),
        ("cardio", "Cardio Deck", "منطقة الكارديو",
         "Life Fitness treadmills, bikes and stair climbers by the windows.", "أجهزة Life Fitness للجري والدراجات والدرج بجانب النوافذ."),
        ("kettlebell", "Functional Zone", "المنطقة الوظيفية",
         "Turf sprint track, kettlebells, plyo boxes, ropes and sleds.", "مسار سبرنت وكيتلبل وصناديق قفز وحبال وزلاجات."),
        ("bike", "Cycling Studio", "استوديو السايكلنج",
         "High-energy rides with music and coaching. Let's spin.", "حصص دراجات مليئة بالطاقة مع الموسيقى والتوجيه."),
        ("pilates", "Pilates Studio", "استوديو البيلاتس",
         "Reformer studio for strength, control and flow.", "استوديو ريفورمر للقوة والتحكم والانسيابية."),
        ("coffee", "Kitchen & Barista Corner", "ركن المطبخ والباريستا",
         "Fresh smoothies, protein shakes, coffee and healthy bites — refuel right after your session.",
         "سموذي طازج وبروتين شيك وقهوة ووجبات صحية — استعد طاقتك مباشرة بعد التمرين."),
        ("lock", "Lockers & Showers", "الخزائن والاستحمام",
         "Smart digital lockers and private shower cabins.", "خزائن ذكية برمز رقمي وكبائن استحمام خاصة."),
        ("coach", "Expert Coaching", "تدريب احترافي",
         "Coaches on the floor to guide your form and progress.", "مدربون في الصالة لتصحيح الأداء ومتابعة تقدّمك."),
    ]
    tiles_html = ""
    for i, (ic, en, ar, den, dar) in enumerate(tiles):
        tiles_html += f"""<div class="tile reveal" style="--d:{i * 0.06:.2f}s">
  {hexsvg("bg-hex")}
  <div class="icon">{ico(ic)}</div>
  <h3>{T(en, ar)}</h3>{TB(den, dar)}
</div>"""

    values = [
        ("01", "target", "Focus", "ركّز", "Every session has a purpose. Clear goals, smart programming, zero wasted reps.",
         "لكل حصة هدف. أهداف واضحة وبرمجة ذكية وبدون تكرار ضائع."),
        ("02", "flame", "Train", "تمرّن", "Train like a pro with premium equipment and coaches who actually care about your form.",
         "تمرّن كالمحترفين بأجهزة فاخرة ومدربين يهتمون فعلًا بطريقة أدائك."),
        ("03", "trend", "Evolve", "تطوّر", "Small wins, every week. Track your progress and become a stronger version of yourself.",
         "إنجازات صغيرة كل أسبوع. تابع تقدّمك وكن نسخة أقوى من نفسك."),
    ]
    vals = "".join(f"""<div class="card reveal" style="--d:{i * 0.1:.1f}s"><span class="num">{n}</span>
<div class="icon">{ico(ic)}</div><h3>{T(en, ar)}</h3>{TB(den, dar)}</div>""" for i, (n, ic, en, ar, den, dar) in enumerate(values))

    explore = [
        ("membership.html", "calendar", "Memberships", "الاشتراكات", "Flexible plans from one month to a full year.", "باقات مرنة من شهر إلى سنة كاملة."),
        ("classes.html", "users", "Classes", "الحصص", "Cycling, boxing, CORE, pilates, yoga & more.", "سايكلنج وملاكمة وكور وبيلاتس ويوغا والمزيد."),
        ("trainers.html", "coach", "Trainers", "المدربون", "Meet the coaches behind THE EVO's.", "تعرّف على مدربي EVO."),
        ("tools.html", "calc", "Fitness Tools", "أدوات اللياقة", "BMI, BMR & TDEE calculators plus expert tips.", "حاسبات BMI وBMR وTDEE ونصائح رياضية."),
    ]
    exp = "".join(f"""<a class="card card--link reveal" style="--d:{i * 0.08:.2f}s" href="{h}">
<div class="icon">{ico(ic)}</div><h3>{T(en, ar)}</h3>{TB(den, dar)}
<span class="more">{T("Explore", "استكشف")}{ico("arrow", "flip-rtl")}</span></a>""" for i, (h, ic, en, ar, den, dar) in enumerate(explore))

    body = f"""
<section class="hero">
  {fx(1)}
  <div class="container hero__grid">
    <div class="hero__text">
      <span class="eyebrow fade-up">{T("Dabouq · Amman · Since 2025", "دابوق · عمّان · منذ 2025")}</span>
      <h1 class="hero__title">
        <span class="line"><span>{T("Train.", "تمرّن.")}</span></span>
        <span class="line"><span class="grad">{T("Transform.", "تحوّل.")}</span></span>
        <span class="line"><span class="outline">{T("Evolve.", "تطوّر.")}</span></span>
      </h1>
      {TB("A premium mixed training facility led by expert coaches. More than machines — a place to train like a pro.",
          "نادٍ رياضي مختلط وفاخر بقيادة مدربين محترفين. أكثر من مجرد أجهزة — مكان لتتمرّن كالمحترفين.", "p", "lead fade-up d1")}
      <div class="btn-row fade-up d2">
        <a class="btn btn--primary" href="contact.html#trial">{T("Book a Free Trial", "احجز حصة تجريبية مجانية")}{ico("arrow", "flip-rtl")}</a>
        <a class="btn btn--ghost" href="membership.html">{T("View Memberships", "تصفّح الاشتراكات")}</a>
      </div>
      <div class="hero__meta fade-up d3">
        <span>{ico("clock")}{T("Open daily · 6 AM – 11 PM", "مفتوح يوميًا · 6 ص – 11 م")}</span>
        <span>{ico("pin")}{T("Dabouq District", "منطقة دابوق")}</span>
        <span>{ico("star")}{T("4.7 on Google", "4.7 على Google")}</span>
      </div>
    </div>
    <div class="fade-up d2">
      <div class="vframe">
        <div class="vframe__inner">
          <span class="vframe__tag"><i></i>EVO GYM</span>
          <video data-autoplay autoplay muted loop playsinline preload="metadata" poster="assets/video/hero-poster.webp">
            <source src="assets/video/hero.mp4" type="video/mp4">
          </video>
          <button class="sound-btn" type="button" aria-pressed="false" aria-label="Toggle sound">{ico("voloff", "off")}{ico("volon", "on")}<span class="lbl">Sound off</span></button>
        </div>
      </div>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"></div>
</section>

{marquee()}

<section class="section" id="about">
  <div class="container">
    <div class="split">
      <div class="reveal from-left">
        <span class="eyebrow">{T("About EVO", "من نحن")}</span>
        <p class="quote-big">{T('More than <span class="accent">machines.</span><br>Train like a <span class="outline">pro.</span>',
                                'أكثر من <span class="accent">مجرد أجهزة.</span><br>تمرّن <span class="outline">كالمحترفين.</span>')}</p>
      </div>
      <div class="reveal from-right">
        {TB("EVO GYM opened its doors in <strong>August 2025</strong> in the heart of Dabouq, Amman, with one mission: to build a place where everyone can train, transform and evolve. We are a mixed training facility built around premium equipment, a clean and modern space, and a team of expert coaches who follow up with members from day one.",
            "افتتح EVO GYM أبوابه في <strong>أغسطس 2025</strong> في قلب دابوق بعمّان، بهدف واحد: أن يكون مكانًا يستطيع فيه الجميع أن يتمرّن ويتحوّل ويتطوّر. نحن نادٍ مختلط يقوم على أجهزة فاخرة ومساحة نظيفة وعصرية، وفريق من المدربين المحترفين الذين يتابعون الأعضاء من اليوم الأول.", "p", "lead")}
        <ul class="checklist">
          <li>{ico("check")}{T("Mixed facility — open to everyone, all day", "نادٍ مختلط — مفتوح للجميع طوال اليوم")}</li>
          <li>{ico("check")}{T("Latest Life Fitness & plate-loaded equipment", "أحدث أجهزة Life Fitness وأجهزة الأوزان")}</li>
          <li>{ico("check")}{T("Group classes: cycling, boxing, CORE, pilates, yoga & more", "حصص جماعية: سايكلنج، ملاكمة، كور، بيلاتس، يوغا والمزيد")}</li>
          <li>{ico("check")}{T("Kitchen & Barista corner to refuel after training", "ركن المطبخ والباريستا لاستعادة طاقتك بعد التمرين")}</li>
        </ul>
      </div>
    </div>
    <div class="stats reveal" style="margin-top:clamp(50px,7vw,90px)">
      <div class="stat"><b><span data-count="12.6">0</span><span class="accent">K</span></b><span>{T("Instagram community", "متابع على إنستغرام")}</span></div>
      <div class="stat"><b><span data-count="4.7">0</span><span class="accent">★</span></b><span>{T("Google rating", "تقييم Google")}</span></div>
      <div class="stat"><b><span data-count="9">0</span><span class="accent">+</span></b><span>{T("Training styles", "أنواع تدريب")}</span></div>
      <div class="stat"><b><span data-count="17">0</span><span class="accent">h</span></b><span>{T("Open every day", "ساعة عمل يوميًا")}</span></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="overview">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">{T("Overview", "نظرة عامة")}</span>
      <h2 class="h-lg">{T('Inside <span class="accent">EVO</span>', 'داخل <span class="accent">EVO</span>')}</h2>
      {TB("Every zone is designed for a different way to move — from heavy lifting to recovery and fuel.",
          "كل منطقة مصمّمة لطريقة تمرين مختلفة — من رفع الأوزان الثقيلة إلى الاستشفاء والتغذية.", "p", "lead")}
    </div>
    <div class="tiles">{tiles_html}</div>
  </div>
</section>

{marquee(True)}

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">{T("Our philosophy", "فلسفتنا")}</span>
      <h2 class="h-lg">{T("Focus. Train. Evolve.", "ركّز. تمرّن. تطوّر.")}</h2>
    </div>
    <div class="grid grid-3">{vals}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">{T("Explore", "استكشف")}</span>
      <h2 class="h-lg">{T("Everything you need", "كل ما تحتاجه")}</h2>
    </div>
    <div class="grid grid-4">{exp}</div>
  </div>
</section>

{cta_band()}
"""
    return body


# ------------------------------------------------------------------ MEMBERSHIP
def membership():
    def li(ok, en, ar):
        return f'<li class="{"" if ok else "no"}">{ico("check" if ok else "x")}{T(en, ar)}</li>'

    plans = [
        ("1 Month", "شهر واحد", "45", "Perfect to get started", "مثالي للبداية", False, [
            (1, "Full gym access", "دخول كامل للنادي"), (1, "Lockers & showers", "الخزائن والاستحمام"),
            (1, "Free fitness assessment", "تقييم لياقة مجاني"), (0, "Group classes", "الحصص الجماعية"),
            (0, "Personal training sessions", "جلسات تدريب شخصي"), (0, "Guest passes", "دعوات للضيوف")]),
        ("3 Months", "3 أشهر", "120", "Save 11% vs monthly", "وفّر 11% مقارنة بالشهري", False, [
            (1, "Full gym access", "دخول كامل للنادي"), (1, "Lockers & showers", "الخزائن والاستحمام"),
            (1, "Free fitness assessment", "تقييم لياقة مجاني"), (1, "All group classes", "جميع الحصص الجماعية"),
            (1, "1 personal training session", "جلسة تدريب شخصي واحدة"), (0, "Guest passes", "دعوات للضيوف")]),
        ("6 Months", "6 أشهر", "210", "Save 22% vs monthly", "وفّر 22% مقارنة بالشهري", False, [
            (1, "Full gym access", "دخول كامل للنادي"), (1, "All group classes", "جميع الحصص الجماعية"),
            (1, "2 personal training sessions", "جلستا تدريب شخصي"), (1, "2 guest passes", "دعوتان للضيوف"),
            (1, "2-week membership freeze", "تجميد الاشتراك أسبوعين"), (0, "Kitchen & Barista discount", "خصم ركن المطبخ والباريستا")]),
        ("12 Months", "12 شهرًا", "360", "Best value — save 33%", "القيمة الأفضل — وفّر 33%", True, [
            (1, "Full gym access", "دخول كامل للنادي"), (1, "All group classes", "جميع الحصص الجماعية"),
            (1, "4 personal training sessions", "4 جلسات تدريب شخصي"), (1, "6 guest passes", "6 دعوات للضيوف"),
            (1, "1-month membership freeze", "تجميد الاشتراك شهرًا"), (1, "10% off Kitchen & Barista", "خصم 10% في ركن المطبخ والباريستا")]),
    ]
    cards = ""
    for i, (en, ar, price, sen, sar, hot, feats) in enumerate(plans):
        badge = f'<span class="plan__badge">{T("Most popular", "الأكثر طلبًا")}</span>' if hot else ""
        cards += f"""<div class="card plan{" plan--hot" if hot else ""} reveal" style="--d:{i * 0.08:.2f}s">{badge}
<div class="plan__name">{T(en, ar)}</div>
<div class="plan__price"><b>{price}</b><small>{T("JOD", "دينار")}</small></div>
<div class="plan__per">{T(sen, sar)}</div>
<ul>{"".join(li(*f) for f in feats)}</ul>
<a class="btn {"btn--primary" if hot else "btn--ghost"}" href="contact.html?plan={en.replace(" ", "+")}#form">{T("Join now", "اشترك الآن")}</a>
</div>"""

    extras = [
        ("Day Pass", "تذكرة يومية", "7", "Single-day full access", "دخول كامل ليوم واحد"),
        ("Class Drop-in", "حصة منفردة", "5", "Any single group class", "أي حصة جماعية واحدة"),
        ("PT Pack · 10", "باقة تدريب شخصي · 10", "180", "10 one-on-one sessions", "10 جلسات فردية مع مدرب"),
    ]
    ex = "".join(f"""<div class="card extra reveal" style="--d:{i * 0.08:.2f}s"><div><h3>{T(en, ar)}</h3>{TB(den, dar)}</div>
<b>{p}<small style="font-size:16px;color:var(--muted)"> {T("JOD", "د.أ")}</small></b></div>""" for i, (en, ar, p, den, dar) in enumerate(extras))

    faqs = [
        ("Is the gym mixed?", "هل النادي مختلط؟",
         "Yes. EVO GYM is a mixed facility and is open to everyone during all opening hours.",
         "نعم، EVO GYM نادٍ مختلط ومفتوح للجميع طوال ساعات العمل."),
        ("Can I try the gym before subscribing?", "هل يمكنني تجربة النادي قبل الاشتراك؟",
         'Absolutely. Book a free trial session from the <a class="accent" href="contact.html#trial">Contact page</a> and our team will confirm your visit.',
         'بالتأكيد. احجز حصة تجريبية مجانية من <a class="accent" href="contact.html#trial">صفحة التواصل</a> وسيؤكد فريقنا موعد زيارتك.'),
        ("Can I freeze my membership?", "هل يمكنني تجميد اشتراكي؟",
         "6-month and 12-month memberships include a freeze period. Just let reception know in advance.",
         "اشتراكات 6 أشهر و12 شهرًا تتضمن فترة تجميد. فقط أبلغ الاستقبال مسبقًا."),
        ("What should I bring?", "ماذا أحضر معي؟",
         "Comfortable training clothes, clean indoor shoes, a towel and a water bottle. Lockers and showers are available.",
         "ملابس رياضية مريحة وحذاء نظيف للصالات الداخلية ومنشفة وزجاجة ماء. تتوفر الخزائن وغرف الاستحمام."),
        ("How do I pay?", "كيف أدفع؟",
         "Visit the reception desk in Dabouq. Our team will help you choose the right plan and complete your registration.",
         "تفضّل بزيارة الاستقبال في دابوق، وسيساعدك فريقنا في اختيار الباقة المناسبة وإتمام التسجيل."),
    ]
    acc = "".join(f"""<details><summary>{T(q, qa)}<span class="pm"></span></summary><div class="acc__body">{TB(a, aa)}</div></details>"""
                  for q, qa, a, aa in faqs)

    return page_hero("Membership", "الاشتراكات",
                     T('Member<span class="accent">ship</span>', 'الاشترا<span class="accent">كات</span>'),
                     "Choose the plan that fits your goals. Every membership includes full access to our premium training floor.",
                     "اختر الباقة التي تناسب أهدافك. كل اشتراك يتضمن دخولًا كاملًا إلى صالة التمرين الفاخرة.", "JOIN") + f"""
<section class="section">
  <div class="container">
    <div class="plans">{cards}</div>
    <div class="note reveal" style="margin-top:28px">{ico("info")}{T("Prices shown are indicative and may change. Please confirm current pricing and offers with our reception or on WhatsApp.",
         "الأسعار المعروضة تقديرية وقابلة للتغيير. يرجى تأكيد الأسعار والعروض الحالية مع الاستقبال أو عبر واتساب.")}</div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{T("Add-ons", "إضافات")}</span><h2 class="h-md">{T("Passes & extras", "تذاكر وإضافات")}</h2></div>
    <div class="extras">{ex}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">FAQ</span><h2 class="h-md">{T("Good to know", "معلومات تهمّك")}</h2></div>
    <div class="acc reveal">{acc}</div>
  </div>
</section>
{cta_band()}
"""


# ------------------------------------------------------------------ TRAINERS
TRAINERS = [
    ("R", "Rashed", "راشد", "Head Coach · Strength & CORE", "مدرب رئيسي · قوة وكور",
     "Known among members for his day-by-day follow-up, Rashed builds strength programs that fit your level and keeps your technique sharp from your very first session.",
     "معروف بين الأعضاء بمتابعته اليومية، يصمّم راشد برامج قوة تناسب مستواك ويحرص على صحة أدائك من أول حصة.",
     [("zap", "CORE", "كور"), ("dumbbell", "Strength", "قوة"), ("coach", "Personal Training", "تدريب شخصي")]),
    ("N", "Najeh", "ناجح", "Functional Training Coach", "مدرب التدريب الوظيفي",
     "Najeh's functional sessions combine strength, conditioning and mobility to make you move better in the gym and in everyday life.",
     "تجمع حصص ناجح الوظيفية بين القوة واللياقة والمرونة لتتحرّك بشكل أفضل داخل النادي وفي حياتك اليومية.",
     [("kettlebell", "Functional", "وظيفي"), ("flame", "Conditioning", "لياقة")]),
    ("D", "Deema", "ديما", "Cycling Coach", "مدربة السايكلنج",
     "Deema leads high-energy cycling rides packed with rhythm and motivation — great cardio that never feels boring.",
     "تقود ديما حصص سايكلنج مليئة بالطاقة والإيقاع والتحفيز — كارديو ممتاز لا يشعرك بالملل أبدًا.",
     [("bike", "Cycling", "سايكلنج"), ("cardio", "Cardio", "كارديو")]),
    ("A", "Ahmad", "أحمد", "Boxing Coach", "مدرب الملاكمة",
     "Ahmad teaches boxing fundamentals, footwork and pad work — a full-body workout that builds power, speed and confidence.",
     "يعلّم أحمد أساسيات الملاكمة وحركة القدمين والتدريب على البادات — تمرين لكامل الجسم يبني القوة والسرعة والثقة.",
     [("glove", "Boxing", "ملاكمة"), ("target", "Pad work", "بادات")]),
]


def trainers():
    cards = ""
    for i, (ini, en, ar, ren, rar, den, dar, chips) in enumerate(TRAINERS):
        ch = "".join(f'<span class="chip">{ico(c)}{T(a, b)}</span>' for c, a, b in chips)
        cards += f"""<article class="card trainer reveal" style="--d:{i * 0.08:.2f}s">
<div class="trainer__media">
  <svg class="trainer__hex" viewBox="0 0 100 100" aria-hidden="true"><path class="o" d="M50 0 97 25 97 75 50 100 3 75 3 25Z"/><path class="f" d="M50 10 88 31 88 69 50 90 12 69 12 31Z"/></svg>
  <span class="trainer__initial" aria-hidden="true">{ini}</span>
  <span class="trainer__role">{T(ren.split(" · ")[0], rar.split(" · ")[0])}</span>
</div>
<div class="trainer__body"><h3>{T(en, ar)}</h3><p class="accent" style="font-weight:600;margin-bottom:10px">{T(ren, rar)}</p>{TB(den, dar)}
<div class="trainer__classes">{ch}</div></div>
</article>"""

    steps = [
        ("01", "smile", "Meet your coach", "تعرّف على مدربك", "A short consultation about your goals, history and schedule.", "جلسة قصيرة للتعرّف على أهدافك وتاريخك الرياضي ووقتك."),
        ("02", "calc", "Assess & plan", "تقييم وخطة", "Fitness assessment and a program built around you.", "تقييم لياقة وبرنامج مصمّم خصيصًا لك."),
        ("03", "trend", "Train & track", "تمرّن وتابع", "One-on-one sessions with regular progress check-ins.", "جلسات فردية مع متابعة دورية لتقدّمك."),
    ]
    st = "".join(f"""<div class="card reveal" style="--d:{i * 0.1:.1f}s"><span class="num">{n}</span><div class="icon">{ico(ic)}</div><h3>{T(en, ar)}</h3>{TB(den, dar)}</div>"""
                 for i, (n, ic, en, ar, den, dar) in enumerate(steps))

    return page_hero("Trainers", "المدربون", T('Our <span class="accent">Coaches</span>', 'مدربو<span class="accent">نا</span>'),
                     "Certified, passionate and always on the floor. Meet the team that will push you to evolve.",
                     "محترفون وشغوفون وموجودون دائمًا في الصالة. تعرّف على الفريق الذي سيدفعك للتطوّر.", "COACH") + f"""
<section class="section">
  <div class="container"><div class="trainers">{cards}</div></div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{T("Personal training", "التدريب الشخصي")}</span>
      <h2 class="h-lg">{T('One coach. <span class="accent">One goal.</span>', 'مدرب واحد. <span class="accent">هدف واحد.</span>')}</h2>
      {TB("Get faster results with a program designed only for you. Here's how it works:", "احصل على نتائج أسرع ببرنامج مصمّم لك وحدك. هكذا تسير الأمور:", "p", "lead")}
    </div>
    <div class="grid grid-3">{st}</div>
    <div class="btn-row reveal" style="margin-top:36px">
      <a class="btn btn--primary" href="contact.html?subject=Personal+Training#form">{T("Request a coach", "اطلب مدربًا")}{ico("arrow", "flip-rtl")}</a>
      <a class="btn btn--ghost" href="classes.html">{T("See class schedule", "شاهد جدول الحصص")}</a>
    </div>
  </div>
</section>
{cta_band()}
"""


# ------------------------------------------------------------------ HOURS
def hours():
    rows = [(6, "Saturday", "السبت", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (0, "Sunday", "الأحد", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (1, "Monday", "الاثنين", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (2, "Tuesday", "الثلاثاء", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (3, "Wednesday", "الأربعاء", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (4, "Thursday", "الخميس", "6:00 AM – 11:00 PM", "6:00 ص – 11:00 م"),
            (5, "Friday", "الجمعة", "9:00 AM – 9:00 PM", "9:00 ص – 9:00 م")]
    tr = "".join(f'<tr data-day-row="{d}"{" class=\"short\"" if d == 5 else ""}><td>{T(en, ar)}</td><td>{T(hen, har)}</td></tr>'
                 for d, en, ar, hen, har in rows)
    # week bar (0..24h scale)
    bars = ""
    for i, (d, en, ar, _, __) in enumerate(rows):
        s, e = (9, 21) if d == 5 else (6, 23)
        bars += f'<div><i style="top:{s / 24 * 100:.1f}%;bottom:{100 - e / 24 * 100:.1f}%;--d:{i * 0.08:.2f}s"></i><span>{T(en[:3], ar)}</span></div>'

    return page_hero("Opening Hours", "ساعات العمل", T('Opening <span class="accent">Hours</span>', 'ساعات <span class="accent">العمل</span>'),
                     "Early mornings or late nights — we're open 17 hours a day, six days a week, and 12 hours on Fridays.",
                     "صباحًا باكرًا أو في وقت متأخر — نحن مفتوحون 17 ساعة يوميًا طوال 6 أيام، و12 ساعة يوم الجمعة.", "OPEN") + f"""
<section class="section">
  <div class="container hours-wrap">
    <div class="reveal from-left">
      <div class="card status" data-status><i class="status__dot" aria-hidden="true"></i><div><b>—</b><span class="status__sub"></span></div></div>
      <table class="hours"><tbody>{tr}</tbody></table>
      <div class="note" style="margin-top:16px">{ico("clock")}{T("Times shown in Amman local time.", "الأوقات حسب توقيت عمّان المحلي.")}</div>
    </div>
    <div class="reveal from-right">
      <div class="card mixed" style="margin-bottom:22px"><div class="icon">{ico("users")}</div><div><h3 style="margin-bottom:4px">{T("Mixed gym", "نادٍ مختلط")}</h3>{TB("EVO GYM is open to everyone during all opening hours.", "EVO GYM مفتوح للجميع طوال ساعات العمل.")}</div></div>
      <div class="card">
        <h3>{T("Your week at EVO", "أسبوعك في EVO")}</h3>
        {TB("Visual overview of opening hours (00:00 – 24:00).", "عرض مرئي لساعات العمل (00:00 – 24:00).")}
        <div class="weekbar">{bars}</div>
      </div>
      <div class="card" style="margin-top:22px">
        <h3>{T("Best times to train", "أفضل أوقات التمرين")}</h3>
        {TB("Quieter hours are usually early mornings (6–9 AM) and early afternoons. Evenings are the most energetic — that's when most group classes run.",
            "الأوقات الأهدأ غالبًا في الصباح الباكر (6–9 ص) وبداية الظهيرة. المساء هو الأكثر حيوية — وفيه تُقام معظم الحصص الجماعية.")}
        <a class="btn btn--ghost" style="margin-top:20px" href="classes.html">{T("Classes schedule", "جدول الحصص")}{ico("arrow", "flip-rtl")}</a>
      </div>
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">{T("Find us", "موقعنا")}</span>
        <h2 class="h-md">{T("Dabouq District, Amman", "منطقة دابوق، عمّان")}</h2>
        {TB("Easy to reach from all over West Amman. Tap below for directions straight to our door.", "سهل الوصول من جميع مناطق غرب عمّان. اضغط أدناه للحصول على الاتجاهات مباشرة.", "p", "lead")}
        <div class="btn-row" style="margin-top:28px">
          <a class="btn btn--primary" href="{MAPS}" target="_blank" rel="noopener">{ico("map")}{T("Get directions", "احصل على الاتجاهات")}</a>
          <a class="btn btn--ghost" href="tel:{PHONE_INTL}">{ico("phone")}<span dir="ltr">{PHONE}</span></a>
        </div>
      </div>
      <div class="map reveal zoom"><iframe src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="EVO GYM location map"></iframe></div>
    </div>
  </div>
</section>
{cta_band()}
"""


# ------------------------------------------------------------------ SERVICES
def services():
    S = [
        ("dumbbell", "Strength & Free Weights", "القوة والأوزان الحرة",
         "A complete strength floor: dumbbells, barbells, racks, benches and premium plate-loaded and selectorized machines from Life Fitness. Whether you're a beginner or chasing a new PR, you'll find everything you need.",
         "صالة قوة متكاملة: دمبلز وبارات ورفوف ومقاعد وأجهزة أوزان فاخرة من Life Fitness. سواء كنت مبتدئًا أو تسعى لرقم قياسي جديد، ستجد كل ما تحتاجه.",
         [("Hypertrophy", "تضخيم"), ("Powerlifting", "باورلفتنج"), ("Toning", "شدّ")], "feature"),
        ("cardio", "Cardio", "الكارديو", "Treadmills, bikes, ellipticals and stair climbers with views over Dabouq.", "أجهزة جري ودراجات وإليبتيكال ودرج مع إطلالة على دابوق.", [], ""),
        ("flame", "CrossFit", "كروس فت", "High-intensity, constantly varied workouts that build strength and conditioning together.", "تمارين عالية الشدة ومتنوعة تبني القوة واللياقة معًا.", [], ""),
        ("bike", "Cycling", "سايكلنج", "Coached indoor cycling rides — music, rhythm and serious calorie burn.", "حصص دراجات داخلية مع مدربة — موسيقى وإيقاع وحرق سعرات عالٍ.", [("Sun · Tue", "الأحد · الثلاثاء")], ""),
        ("kettlebell", "Functional Training", "التدريب الوظيفي", "Kettlebells, sleds, ropes and plyo boxes on our turf sprint track.", "كيتلبل وزلاجات وحبال وصناديق قفز على مسار السبرنت.", [("Sat", "السبت")], ""),
        ("glove", "Boxing", "الملاكمة", "Technique, footwork and pad work — a full-body workout that builds confidence.", "تقنيات وحركة قدمين وتدريب على البادات — تمرين لكامل الجسم يبني الثقة.", [("Wed", "الأربعاء")], ""),
        ("zap", "CORE", "كور", "Focused core sessions for a stronger midsection, better posture and a healthier back.", "حصص مركّزة لجذع أقوى وقوام أفضل وظهر أكثر صحة.", [("Mon · Wed", "الاثنين · الأربعاء")], ""),
        ("pilates", "Pilates", "بيلاتس", "Reformer pilates in a calm, dedicated studio. Strength · Control · Flow.", "بيلاتس ريفورمر في استوديو هادئ ومخصّص. قوة · تحكّم · انسيابية.", [("Sat", "السبت")], ""),
        ("yoga", "Yoga", "يوغا", "Mobility, breathing and balance to recover and reset.", "مرونة وتنفّس وتوازن للاستشفاء واستعادة النشاط.", [("Sat", "السبت")], ""),
        ("coach", "Personal Training", "التدريب الشخصي", "One-on-one coaching with a program built around your goals.", "تدريب فردي مع برنامج مصمّم حول أهدافك.", [], ""),
        ("lock", "Lockers & Showers", "الخزائن والاستحمام", "Digital-code lockers and clean, private shower cabins.", "خزائن برمز رقمي وكبائن استحمام نظيفة وخاصة.", [], ""),
        ("coffee", "Kitchen & Barista Corner", "ركن المطبخ والباريستا",
         "Our in-house juice bar and café: fresh smoothies, protein shakes, specialty coffee, healthy snacks and supplements — the perfect place to refuel and hang out after your workout.",
         "الجوس بار والمقهى الخاص بنا: سموذي طازج وبروتين شيك وقهوة مختصّة ووجبات خفيفة صحية ومكمّلات — المكان المثالي لاستعادة طاقتك والاسترخاء بعد التمرين.",
         [("Smoothies", "سموذي"), ("Protein shakes", "بروتين شيك"), ("Coffee", "قهوة"), ("Healthy bites", "وجبات صحية")], "full"),
    ]
    cards = ""
    for i, (ic, en, ar, den, dar, chips, kind) in enumerate(S):
        cls = "card--feature" if kind else ""
        style = "grid-column:1/-1" if kind == "full" else ""
        ch = "".join(f'<span class="chip">{ico("calendar") if "·" in a or len(a) <= 3 else ico("check")}{T(a, b)}</span>' for a, b in chips)
        cards += f"""<div class="card {cls} reveal" style="--d:{(i % 3) * 0.08:.2f}s;{style}"><div class="icon">{ico(ic)}</div>
<h3>{T(en, ar)}</h3>{TB(den, dar)}{f'<div class="chips">{ch}</div>' if ch else ""}</div>"""

    return page_hero("Services", "الخدمات", T('Our <span class="accent">Services</span>', '<span class="accent">خدماتنا</span>'),
                     "From heavy lifting to reformer pilates — and a great coffee afterwards. Everything under one roof.",
                     "من رفع الأوزان الثقيلة إلى بيلاتس الريفورمر — وقهوة رائعة بعدها. كل شيء تحت سقف واحد.", "MOVE") + f"""
<section class="section">
  <div class="container"><div class="svc">{cards}</div></div>
</section>
{cta_band()}
"""
