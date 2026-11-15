from layout import T, TB, ph, page_hero, cta_band, WA, MAPS, MAP_EMBED, PHONE, PHONE_INTL, IG, FB
from icons import ico

# ------------------------------------------------------------------ CLASSES
CL = {
    "pilates": ("pilates", "Pilates", "بيلاتس"),
    "yoga": ("yoga", "Yoga", "يوغا"),
    "cycling": ("bike", "Cycling", "سايكلنج"),
    "boxing": ("glove", "Boxing", "ملاكمة"),
    "functional": ("kettlebell", "Functional Training", "تدريب وظيفي"),
    "core": ("zap", "CORE", "كور"),
}
COACH = {"Deema": "ديما", "Ahmad": "أحمد", "Najeh": "ناجح", "Rashed": "راشد"}
SLOTS = [
    ("2:00 PM", "2:00 م", {6: ("pilates", None)}),
    ("6:00 – 7:00 PM", "6:00 – 7:00 م", {6: ("yoga", None)}),
    ("7:00 – 8:00 PM", "7:00 – 8:00 م", {0: ("cycling", "Deema"), 2: ("cycling", "Deema"), 3: ("boxing", "Ahmad")}),
    ("7:30 – 8:30 PM", "7:30 – 8:30 م", {6: ("functional", "Najeh"), 1: ("core", "Rashed"), 3: ("core", "Rashed")}),
]
DAYS = [(6, "Sat", "السبت", "Saturday"), (0, "Sun", "الأحد", "Sunday"), (1, "Mon", "الاثنين", "Monday"),
        (2, "Tue", "الثلاثاء", "Tuesday"), (3, "Wed", "الأربعاء", "Wednesday"), (4, "Thu", "الخميس", "Thursday"),
        (5, "Fri", "الجمعة", "Friday")]


def classes():
    head = '<th class="time"></th>' + "".join(
        f'<th data-sched-day="{d}">{T(en, ar)}</th>' for d, en, ar, _ in DAYS[:5])
    rows = ""
    for ten, tar, m in SLOTS:
        cells = f'<td class="t">{ico("clock")}{T(ten, tar)}</td>'
        for d, *_ in DAYS[:5]:
            if d in m:
                k, c = m[d]
                ic, en, ar = CL[k]
                coach = f"<small>{T(c, COACH[c])}</small>" if c else ""
                cells += f'<td class="cls">{ico(ic)}<b>{T(en, ar)}</b>{coach}</td>'
            else:
                cells += "<td></td>"
        rows += f"<tr>{cells}</tr>"

    tabs = "".join(f'<button type="button" data-d="{d}">{T(en, ar)}</button>' for d, en, ar, _ in DAYS)
    lists = ""
    for d, en, ar, full in DAYS:
        items = ""
        for ten, tar, m in SLOTS:
            if d in m:
                k, c = m[d]
                ic, cen, car = CL[k]
                coach = T("Coach " + c, "المدرب/ة " + COACH[c]) if c else T("Studio class", "حصة استوديو")
                items += f"""<div class="card slot"><div class="icon">{ico(ic)}</div><div><b>{T(cen, car)}</b><small>{coach}</small></div>
<div class="time">{T(ten, tar)}</div></div>"""
        if not items:
            items = f'<div class="card empty-day">{TB("No group classes this day — the gym floor is open as usual.", "لا توجد حصص جماعية في هذا اليوم — صالة التمرين مفتوحة كالمعتاد.")}</div>'
        lists += f'<div class="daylist" data-d="{d}" hidden>{items}</div>'

    legend = "".join(f'<span class="chip">{ico(ic)}{T(en, ar)}</span>' for ic, en, ar in CL.values())

    return page_hero("Classes Schedule", "جدول الحصص", T('Classes <span class="accent">Schedule</span>', 'جدول <span class="accent">الحصص</span>'),
                     "November group classes. Grab your spot early — our evening sessions fill up fast.",
                     "حصص شهر نوفمبر الجماعية. احجز مكانك مبكرًا — حصص المساء تمتلئ بسرعة.", "CLASS") + f"""
<section class="section">
  <div class="container">
    <div class="section-head reveal" style="max-width:none;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:20px">
      <div><span class="eyebrow">{T("November", "نوفمبر")}</span><h2 class="h-md">{T("Weekly timetable", "الجدول الأسبوعي")}</h2></div>
      <div style="display:flex;flex-wrap:wrap;gap:8px">{legend}</div>
    </div>
    <div class="sched-desktop reveal">
      <table class="sched"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>
      <div class="note" style="margin-top:14px">{ico("info")}{T("Thursday & Friday: no group classes — the gym floor is open as usual.", "الخميس والجمعة: لا توجد حصص جماعية — صالة التمرين مفتوحة كالمعتاد.")}</div>
    </div>
    <div class="sched-mobile reveal">
      <div class="daytabs" role="tablist">{tabs}</div>
      {lists}
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="grid grid-3">
      <div class="card reveal"><div class="icon">{ico("calendar")}</div><h3>{T("Book your spot", "احجز مكانك")}</h3>{TB("Reserve at reception or send us a WhatsApp message before the class.", "احجز من الاستقبال أو أرسل لنا رسالة واتساب قبل موعد الحصة.")}</div>
      <div class="card reveal" style="--d:.1s"><div class="icon">{ico("clock")}</div><h3>{T("Arrive 10 min early", "احضر قبل 10 دقائق")}</h3>{TB("Time to set up your bike, mat or gloves and warm up properly.", "وقت كافٍ لتجهيز الدراجة أو البساط أو القفازات والإحماء جيدًا.")}</div>
      <div class="card reveal" style="--d:.2s"><div class="icon">{ico("repeat")}</div><h3>{T("Updated monthly", "يُحدّث شهريًا")}</h3>{TB("New schedules are posted every month here and on our Instagram.", "ننشر الجدول الجديد كل شهر هنا وعلى إنستغرام.")}</div>
    </div>
    <div class="btn-row reveal" style="margin-top:36px">
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{ico("wa")}{T("Book on WhatsApp", "احجز عبر واتساب")}</a>
      <a class="btn btn--ghost" href="trainers.html">{T("Meet the coaches", "تعرّف على المدربين")}{ico("arrow", "flip-rtl")}</a>
    </div>
  </div>
</section>
{cta_band()}
"""


# ------------------------------------------------------------------ TOOLS
def field(name, en, ar, unit_en="", unit_ar="", typ="number", extra=""):
    u = f' <span style="color:var(--muted);font-weight:500">({T(unit_en, unit_ar)})</span>' if unit_en else ""
    return f"""<div class="field"><label for="{name}">{T(en, ar)}{u}</label><input id="{name}" name="{name.split("-")[-1]}" type="{typ}" inputmode="decimal" {extra} required></div>"""


def sex(prefix):
    return f"""<div class="field"><label>{T("Sex", "الجنس")}</label><div class="seg">
<label><input type="radio" name="sex" value="m" checked><span>{T("Male", "ذكر")}</span></label>
<label><input type="radio" name="sex" value="f"><span>{T("Female", "أنثى")}</span></label></div></div>"""


TIPS = [
    ("Plateau", "ثبات", "Not seeing progress anymore", "توقّف التقدّم",
     "<p>Plateaus are normal — your body adapts to what you repeat.</p><ul><li><strong>Progressive overload:</strong> add a little weight, a rep, or a set each week.</li><li>Change one variable every 4–6 weeks (exercise, tempo, rest).</li><li>Track your lifts so you know what to beat.</li><li>Check sleep and protein — recovery is where growth happens.</li></ul>",
     "<p>الثبات أمر طبيعي — جسمك يتكيّف مع ما تكرّره.</p><ul><li><strong>التحميل التدريجي:</strong> زد وزنًا بسيطًا أو تكرارًا أو مجموعة كل أسبوع.</li><li>غيّر متغيّرًا واحدًا كل 4–6 أسابيع (التمرين، السرعة، الراحة).</li><li>سجّل أوزانك لتعرف ما الذي عليك تجاوزه.</li><li>راجع نومك وكمية البروتين — النمو يحدث أثناء الاستشفاء.</li></ul>"),
    ("Soreness", "ألم عضلي", "Muscle soreness after training (DOMS)", "ألم العضلات بعد التمرين",
     "<p>Delayed-onset soreness usually peaks 24–72 hours after a new or hard workout.</p><ul><li>Keep moving: light cardio and mobility help more than full rest.</li><li>Drink enough water and eat protein with every meal.</li><li>Increase training volume gradually, especially after a break.</li><li>Sharp, joint or one-sided pain is <strong>not</strong> normal soreness — stop and get it checked.</li></ul>",
     "<p>يصل الألم العضلي المتأخر عادةً إلى ذروته بعد 24–72 ساعة من تمرين جديد أو قوي.</p><ul><li>استمر في الحركة: الكارديو الخفيف وتمارين المرونة أفضل من الراحة التامة.</li><li>اشرب ماءً كافيًا وتناول البروتين في كل وجبة.</li><li>زد حجم التمرين تدريجيًا، خصوصًا بعد الانقطاع.</li><li>الألم الحاد أو ألم المفاصل أو الألم في جهة واحدة <strong>ليس</strong> ألمًا طبيعيًا — توقّف واستشر مختصًا.</li></ul>"),
    ("Back", "الظهر", "Lower-back discomfort when lifting", "ألم أسفل الظهر أثناء رفع الأوزان",
     "<p>Most lifting-related back strain comes from form breaking down under fatigue.</p><ul><li>Brace your core (big breath, tight midsection) before every rep.</li><li>Keep a neutral spine — no rounding on deadlifts or rows.</li><li>Lower the weight until your technique is consistent.</li><li>Strengthen glutes and core (hip thrusts, planks, bird-dogs).</li></ul>",
     "<p>معظم إجهاد الظهر أثناء رفع الأوزان يأتي من انهيار الأداء الصحيح مع التعب.</p><ul><li>شدّ عضلات البطن (نفَس عميق وجذع مشدود) قبل كل تكرار.</li><li>حافظ على استقامة العمود الفقري — لا تقوّس ظهرك في الديدلفت أو التجديف.</li><li>خفّف الوزن حتى يثبت أداؤك الصحيح.</li><li>قوِّ عضلات المؤخرة والجذع (هيب ثرست، بلانك، بيرد دوج).</li></ul>"),
    ("Knees", "الركبة", "Knee pain during squats or lunges", "ألم الركبة أثناء السكوات أو اللانجز",
     "<p>Knees usually complain when they are asked to compensate for the hips or ankles.</p><ul><li>Push knees out in line with your toes — don't let them cave in.</li><li>Sit back into the hips and keep the whole foot on the floor.</li><li>Warm up with bodyweight squats and ankle mobility.</li><li>Try box squats or a shorter range, then build up.</li></ul>",
     "<p>غالبًا ما تتألم الركبة عندما تعوّض ضعف الورك أو الكاحل.</p><ul><li>ادفع الركبتين للخارج باتجاه أصابع القدم — لا تدعهما تنحنيان للداخل.</li><li>انزل بالورك للخلف وأبقِ القدم كاملة على الأرض.</li><li>أحمِ بتمارين سكوات بوزن الجسم ومرونة الكاحل.</li><li>جرّب السكوات على صندوق أو مدى حركة أقصر، ثم تدرّج.</li></ul>"),
    ("Shoulders", "الكتف", "Shoulder pain on presses", "ألم الكتف أثناء تمارين الضغط",
     "<p>Shoulders are mobile but delicate — balance and control matter.</p><ul><li>Tuck elbows to ~45° on bench and push-ups instead of flaring them.</li><li>Pull at least as much as you push (rows, face pulls).</li><li>Warm up the rotator cuff with light band work.</li><li>Avoid ego lifting — controlled reps beat heavy, sloppy ones.</li></ul>",
     "<p>الكتف مفصل مرن لكنه حسّاس — التوازن والتحكّم أساسيان.</p><ul><li>اجعل المرفقين بزاوية ~45° في البنش والضغط بدل فتحهما للخارج.</li><li>اسحب بقدر ما تدفع على الأقل (تجديف، فيس بول).</li><li>أحمِ عضلات الكفّة المدوّرة بأحزمة مطاطية خفيفة.</li><li>تجنّب رفع أوزان أكبر من قدرتك — التكرار المتحكَّم به أفضل من الثقيل العشوائي.</li></ul>"),
    ("Fat loss", "خسارة الدهون", "Training hard but not losing fat", "أتمرّن بجد لكن لا أخسر الدهون",
     "<p>Fat loss is mostly driven by a consistent calorie deficit.</p><ul><li>Use our <a class=\"accent\" href=\"#tdee\">TDEE calculator</a> and eat roughly 300–500 kcal below it.</li><li>Keep lifting weights to protect muscle.</li><li>Prioritise protein, vegetables and whole foods.</li><li>Walk more — daily steps add up more than you think.</li></ul>",
     "<p>خسارة الدهون تعتمد أساسًا على عجز ثابت في السعرات الحرارية.</p><ul><li>استخدم <a class=\"accent\" href=\"#tdee\">حاسبة TDEE</a> وتناول أقل منها بحوالي 300–500 سعرة.</li><li>استمر في رفع الأوزان للحفاظ على العضلات.</li><li>ركّز على البروتين والخضار والأطعمة الطبيعية.</li><li>امشِ أكثر — الخطوات اليومية تصنع فرقًا أكبر مما تتوقع.</li></ul>"),
    ("Motivation", "الحافز", "Losing motivation & consistency", "فقدان الحافز والاستمرارية",
     "<p>Discipline is easier when the plan is simple.</p><ul><li>Schedule workouts like appointments — same days, same time.</li><li>Set small weekly goals, not only big long-term ones.</li><li>Join a group class or train with a friend for accountability.</li><li>On low days, do a short session — showing up is the win.</li></ul>",
     "<p>الالتزام أسهل عندما تكون الخطة بسيطة.</p><ul><li>حدّد مواعيد التمرين كأنها مواعيد عمل — نفس الأيام ونفس الوقت.</li><li>ضع أهدافًا أسبوعية صغيرة وليس فقط أهدافًا كبيرة بعيدة.</li><li>انضم إلى حصة جماعية أو تمرّن مع صديق للالتزام.</li><li>في الأيام الصعبة، قم بحصة قصيرة — الحضور بحد ذاته إنجاز.</li></ul>"),
    ("Warm-up", "الإحماء", "Skipping the warm-up", "إهمال الإحماء",
     "<p>A good warm-up takes 8–10 minutes and improves performance.</p><ul><li>3–5 minutes of light cardio to raise body temperature.</li><li>Dynamic mobility for the joints you'll train.</li><li>2–3 lighter ramp-up sets before your working weight.</li></ul>",
     "<p>الإحماء الجيد يستغرق 8–10 دقائق ويحسّن أداءك.</p><ul><li>3–5 دقائق كارديو خفيف لرفع حرارة الجسم.</li><li>تمارين مرونة حركية للمفاصل التي ستمرّنها.</li><li>2–3 مجموعات تمهيدية بوزن أخف قبل وزن التمرين الأساسي.</li></ul>"),
    ("Recovery", "الاستشفاء", "Always tired & poor recovery", "تعب دائم وضعف الاستشفاء",
     "<p>You grow when you recover, not only when you train.</p><ul><li>Aim for 7–9 hours of sleep.</li><li>Plan 1–2 rest or light days per week.</li><li>Hydrate well — especially on hot days and long sessions.</li><li>Eat enough overall; under-fuelling kills energy.</li></ul>",
     "<p>العضلات تنمو أثناء الاستشفاء، وليس فقط أثناء التمرين.</p><ul><li>احرص على النوم 7–9 ساعات.</li><li>خصّص 1–2 يوم راحة أو تمرين خفيف أسبوعيًا.</li><li>اشرب الماء جيدًا — خصوصًا في الأيام الحارة والحصص الطويلة.</li><li>تناول طعامًا كافيًا؛ قلة الوقود تقتل الطاقة.</li></ul>"),
    ("Beginners", "للمبتدئين", "Not sure where to start", "لا أعرف من أين أبدأ",
     "<p>Start simple and master the basics.</p><ul><li>3 full-body sessions a week is plenty to begin.</li><li>Learn the main patterns: squat, hinge, push, pull, carry.</li><li>Leave 1–3 reps in the tank on every set.</li><li>Ask a coach to check your form — that's what we're here for.</li></ul>",
     "<p>ابدأ ببساطة وأتقن الأساسيات.</p><ul><li>3 حصص لكامل الجسم أسبوعيًا كافية للبداية.</li><li>تعلّم الحركات الأساسية: السكوات، الانحناء، الدفع، السحب، الحمل.</li><li>اترك 1–3 تكرارات احتياطية في كل مجموعة.</li><li>اطلب من المدرب مراجعة أدائك — هذا دورنا.</li></ul>"),
]


def tools():
    acc = "".join(f"""<details><summary><span><span class="tag">{T(ten, tar)}</span>{T(qen, qar)}</span><span class="pm"></span></summary>
<div class="acc__body"><div class="l-en">{aen}</div><div class="l-ar" lang="ar">{aar}</div></div></details>"""
                  for ten, tar, qen, qar, aen, aar in TIPS)

    activity = [("1.2", "Sedentary (little or no exercise)", "قليل الحركة (بدون تمرين تقريبًا)"),
                ("1.375", "Light (1–3 days / week)", "نشاط خفيف (1–3 أيام أسبوعيًا)"),
                ("1.55", "Moderate (3–5 days / week)", "نشاط متوسط (3–5 أيام أسبوعيًا)"),
                ("1.725", "Very active (6–7 days / week)", "نشاط عالٍ (6–7 أيام أسبوعيًا)"),
                ("1.9", "Athlete (2× per day / physical job)", "رياضي (مرتين يوميًا / عمل بدني)")]
    opts = "".join(f'<option value="{v}"{" selected" if v == "1.55" else ""} data-en="{en}" data-ar="{ar}">{en}</option>' for v, en, ar in activity)

    return page_hero("Fitness Tools", "أدوات اللياقة", T('Fitness <span class="accent">Tools</span>', 'أدوات <span class="accent">اللياقة</span>'),
                     "Know your numbers. Calculate your BMI, BMR and daily calories — then learn how to fix the most common training problems.",
                     "اعرف أرقامك. احسب مؤشر كتلة الجسم ومعدل الأيض والسعرات اليومية — ثم تعلّم كيف تعالج أشهر مشاكل التمرين.", "TOOLS") + f"""
<section class="section">
  <div class="container">
    <div class="calc-tabs reveal" role="tablist">
      <button type="button" class="on" data-t="bmi">BMI</button>
      <button type="button" data-t="bmr">BMR</button>
      <button type="button" data-t="tdee">TDEE</button>
    </div>

    <div class="calc on" id="bmi">
      <form class="card" id="bmi-form" novalidate>
        <h3>{T("Body Mass Index", "مؤشر كتلة الجسم")}</h3>
        {TB("A quick estimate of whether your weight is in a healthy range for your height.", "تقدير سريع لمعرفة إن كان وزنك ضمن النطاق الصحي بالنسبة لطولك.", "p")}
        <div style="height:22px"></div>
        <div class="row2">{field("bmi-h", "Height", "الطول", "cm", "سم", extra='min="100" max="250" ' + ph("e.g. 175", "مثال: 175"))}{field("bmi-w", "Weight", "الوزن", "kg", "كغ", extra='min="30" max="300" ' + ph("e.g. 75", "مثال: 75"))}</div>
        <button class="btn btn--primary" type="submit">{ico("calc")}{T("Calculate BMI", "احسب المؤشر")}</button>
      </form>
      <div class="card result">
        <span class="result__unit">{T("Your BMI", "مؤشرك")}</span>
        <div class="result__val" id="bmi-val">0.0</div>
        <span class="result__cat" id="bmi-cat">—</span>
        <div class="gauge"><i></i></div>
        <div class="gauge-legend" dir="ltr"><span>&lt;18.5</span><span>18.5–25</span><span>25–30</span><span>30+</span></div>
        <p class="result__hint" id="bmi-hint">{T("Enter your height and weight to see your result.", "أدخل طولك ووزنك لمعرفة النتيجة.")}</p>
      </div>
    </div>

    <div class="calc" id="bmr">
      <form class="card" id="bmr-form" novalidate>
        <h3>{T("Basal Metabolic Rate", "معدل الأيض الأساسي")}</h3>
        {TB("The calories your body burns at complete rest (Mifflin-St Jeor formula).", "السعرات التي يحرقها جسمك في حالة الراحة التامة (معادلة Mifflin-St Jeor).", "p")}
        <div style="height:22px"></div>
        {sex("bmr")}
        <div class="row3">{field("bmr-age", "Age", "العمر", "years", "سنة", extra='min="14" max="90" ' + ph("25", "25"))}{field("bmr-h", "Height", "الطول", "cm", "سم", extra=ph("175", "175"))}{field("bmr-w", "Weight", "الوزن", "kg", "كغ", extra=ph("75", "75"))}</div>
        <button class="btn btn--primary" type="submit">{ico("calc")}{T("Calculate BMR", "احسب معدل الأيض")}</button>
      </form>
      <div class="card result">
        <span class="result__unit">{T("Basal metabolic rate", "معدل الأيض الأساسي")}</span>
        <div class="result__val" id="bmr-val">0</div>
        <span class="result__unit">{T("kcal / day", "سعرة / يوم")}</span>
        <p class="result__hint">{T("This is your baseline. Use the TDEE tab to include your daily activity.", "هذا هو الحد الأساسي. استخدم تبويب TDEE لإضافة نشاطك اليومي.")}</p>
        <p class="result__hint" id="bmr-hint" hidden></p>
      </div>
    </div>

    <div class="calc" id="tdee">
      <form class="card" id="tdee-form" novalidate>
        <h3>{T("Total Daily Energy Expenditure", "إجمالي السعرات اليومية")}</h3>
        {TB("Your estimated daily calories including activity — the number to plan your diet around.", "تقدير السعرات اليومية مع النشاط — الرقم الذي تبني عليه نظامك الغذائي.", "p")}
        <div style="height:22px"></div>
        {sex("tdee")}
        <div class="row3">{field("tdee-age", "Age", "العمر", "years", "سنة", extra='min="14" max="90" ' + ph("25", "25"))}{field("tdee-h", "Height", "الطول", "cm", "سم", extra=ph("175", "175"))}{field("tdee-w", "Weight", "الوزن", "kg", "كغ", extra=ph("75", "75"))}</div>
        <div class="field"><label for="tdee-act">{T("Activity level", "مستوى النشاط")}</label><select id="tdee-act" name="act" data-i18n-options>{opts}</select></div>
        <button class="btn btn--primary" type="submit">{ico("calc")}{T("Calculate TDEE", "احسب السعرات")}</button>
      </form>
      <div class="card result">
        <span class="result__unit">{T("Maintenance calories", "سعرات الثبات")}</span>
        <div class="result__val" id="tdee-val">0</div>
        <span class="result__unit">{T("kcal / day", "سعرة / يوم")}</span>
        <div class="tdee-grid">
          <div><b id="tdee-cut">0</b><small>{T("Fat loss (−500)", "خسارة دهون (−500)")}</small></div>
          <div class="mid"><b id="tdee-keep">0</b><small>{T("Maintain", "ثبات")}</small></div>
          <div><b id="tdee-bulk">0</b><small>{T("Lean gain (+300)", "زيادة عضلية (+300)")}</small></div>
        </div>
        <p class="result__hint" id="tdee-hint" hidden></p>
      </div>
    </div>
    <div class="note reveal" style="margin-top:22px">{ico("info")}{T("These calculators give general estimates for healthy adults and are not medical advice. For personal guidance, talk to one of our coaches or a healthcare professional.",
       "هذه الحاسبات تعطي تقديرات عامة للبالغين الأصحاء وليست نصيحة طبية. للحصول على توجيه شخصي، تحدّث مع أحد مدربينا أو مختص صحي.")}</div>
  </div>
</section>
<section class="section section--alt" id="tips">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{T("Coach's corner", "ركن المدرب")}</span>
      <h2 class="h-lg">{T('Common problems, <span class="accent">real fixes</span>', 'مشاكل شائعة، <span class="accent">حلول عملية</span>')}</h2>
      {TB("Practical tips for the issues we see most on the gym floor.", "نصائح عملية لأكثر المشاكل التي نراها في صالة التمرين.", "p", "lead")}
    </div>
    <div class="acc reveal">{acc}</div>
  </div>
</section>
{cta_band()}
"""


# ------------------------------------------------------------------ GALLERY
GAL = [
    ("Locker room with digital lockers", "غرفة الخزائن الرقمية"),
    ("Functional training zone", "منطقة التدريب الوظيفي"),
    ("Life Fitness strength machines", "أجهزة القوة من Life Fitness"),
    ("Coach guiding a member", "مدرب يوجّه أحد الأعضاء"),
    ("Sprint track and weights floor", "مسار السبرنت وصالة الأوزان"),
    ("Cardio stair climbers", "أجهزة الكارديو"),
    ("Dumbbell area — Focus. Train. Evolve.", "منطقة الدمبلز"),
    ("Barbell racks", "رفوف البارات"),
    ("Pilates reformer studio", "استوديو البيلاتس"),
    ("Shower cabins", "كبائن الاستحمام"),
    ("Kitchen & Barista corner — juice bar", "ركن المطبخ والباريستا"),
    ("EVO GYM reception", "استقبال EVO GYM"),
]


def gallery():
    items = f"""<div class="g-video reveal"><div class="vframe"><div class="vframe__inner">
<span class="vframe__tag"><i></i>EVO GYM</span>
<video data-autoplay autoplay muted loop playsinline preload="metadata" poster="assets/video/gallery-poster.webp"><source src="assets/video/gallery.mp4" type="video/mp4"></video>
<button class="sound-btn" type="button" aria-pressed="false" aria-label="Toggle sound">{ico("voloff", "off")}{ico("volon", "on")}<span class="lbl">Sound off</span></button>
</div></div></div>"""
    for i, (en, ar) in enumerate(GAL, 1):
        n = f"{i:02d}"
        items += f"""<button type="button" class="g-item reveal" style="--d:{(i % 4) * 0.06:.2f}s" data-full="assets/img/gallery/g{n}.webp" aria-label="{en}">
<img src="assets/img/gallery/g{n}-sm.webp" srcset="assets/img/gallery/g{n}-sm.webp 450w, assets/img/gallery/g{n}.webp 900w" sizes="(max-width:640px) 50vw, 25vw" width="450" height="800" alt="{en}" loading="lazy" decoding="async">
<span class="zoom-ico">{ico("zoom")}</span></button>"""

    return page_hero("Gallery", "المعرض", T('The <span class="accent">Gallery</span>', '<span class="accent">المعرض</span>'),
                     "Step inside EVO GYM. Tap any photo to view it full screen.",
                     "ادخل إلى EVO GYM. اضغط على أي صورة لعرضها بالحجم الكامل.", "INSIDE") + f"""
<section class="section">
  <div class="container"><div class="gallery">{items}</div>
    <div class="btn-row reveal" style="justify-content:center;margin-top:40px">
      <a class="btn btn--ghost" href="{IG}" target="_blank" rel="noopener">{ico("instagram")}{T("More on Instagram", "المزيد على إنستغرام")}</a>
    </div>
  </div>
</section>
<div class="lightbox" aria-hidden="true" role="dialog" aria-label="Image viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close">{ico("x")}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous">{ico("left")}</button>
  <img src="" alt="">
  <button class="lb-btn lb-next" type="button" aria-label="Next">{ico("right")}</button>
  <span class="lb-count"></span>
</div>
{cta_band()}
"""


# ------------------------------------------------------------------ FORMS
def inp(id_, name, en, ar, typ="text", req=True, phen="", phar="", extra=""):
    r = ' <span class="req">*</span>' if req else ""
    p = ph(phen, phar) if phen else ""
    return f"""<div class="field"><label for="{id_}">{T(en, ar)}{r}</label><input id="{id_}" name="{name}" type="{typ}" {p} {extra}{" required" if req else ""}></div>"""


def status_div():
    return '<div class="form-status" role="status" aria-live="polite"></div>'


def submit_btn(en, ar):
    return f'<button class="btn btn--primary" type="submit" style="margin-top:6px"><span class="spinner"></span>{ico("send", "btn-ico flip-rtl")}{T(en, ar)}</button>'


# ------------------------------------------------------------------ CAREERS
def careers():
    perks = [
        ("users", "A team that lifts each other", "فريق يدعم بعضه", "Work alongside passionate coaches in a modern, friendly environment.", "اعمل مع مدربين شغوفين في بيئة عصرية وودّية."),
        ("award", "Grow your career", "طوّر مسيرتك", "Learning, certifications and room to grow with a new, fast-growing brand.", "تعلّم وشهادات ومجال للنمو مع علامة جديدة سريعة التطوّر."),
        ("dumbbell", "Train where you work", "تمرّن حيث تعمل", "Full gym access and staff perks at the Kitchen & Barista corner.", "دخول كامل للنادي ومزايا للموظفين في ركن المطبخ والباريستا."),
    ]
    pk = "".join(f'<div class="perk reveal" style="--d:{i * 0.1:.1f}s"><div class="icon">{ico(ic)}</div><div><b>{T(en, ar)}</b>{TB(den, dar)}</div></div>'
                 for i, (ic, en, ar, den, dar) in enumerate(perks))
    avail = [("Full-time", "دوام كامل"), ("Part-time", "دوام جزئي"), ("Flexible", "مرن")]
    av = "".join(f'<option value="{en}" data-en="{en}" data-ar="{ar}">{en}</option>' for en, ar in avail)

    return page_hero("Careers", "التوظيف", T('Join the <span class="accent">Team</span>', 'انضم إلى <span class="accent">فريقنا</span>'),
                     "Passionate about fitness and people? We're always looking for great coaches and staff to grow with EVO.",
                     "شغوف بالرياضة وبالناس؟ نبحث دائمًا عن مدربين وموظفين مميزين لينموا معنا في EVO.", "CAREERS") + f"""
<section class="section">
  <div class="container contact-wrap">
    <div>
      <div class="section-head reveal" style="margin-bottom:30px"><span class="eyebrow">{T("Why EVO", "لماذا EVO")}</span><h2 class="h-md">{T("Work with us", "اعمل معنا")}</h2></div>
      <div class="perks">{pk}</div>
      <div class="note reveal" style="margin-top:28px">{ico("info")}{T("Write the position you're applying for — coaching, reception, barista, cleaning, management or anything else.", "اكتب الوظيفة التي تتقدّم لها — مدرب، استقبال، باريستا، نظافة، إدارة أو غير ذلك.")}</div>
    </div>
    <form class="card form-card reveal" data-remote="job" novalidate id="form">
      <h2 class="h-md">{T("Apply now", "قدّم الآن")}</h2>
      {TB("Fill in the form and our team will review your application.", "املأ النموذج وسيقوم فريقنا بمراجعة طلبك.")}
      <input type="hidden" name="_subject" value="New job application — EVO GYM website">
      <input type="hidden" name="Form" value="Job Application">
      <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
      {inp("j-name", "Full Name", "Full name", "الاسم الكامل", phen="Your full name", phar="اسمك الكامل", extra='autocomplete="name"')}
      <div class="row2">
        {inp("j-email", "Email", "Email", "البريد الإلكتروني", "email", phen="name@email.com", phar="name@email.com", extra='autocomplete="email" dir="ltr"')}
        {inp("j-phone", "Phone", "Phone", "رقم الهاتف", "tel", phen="07X XXX XXXX", phar="07X XXX XXXX", extra='autocomplete="tel" dir="ltr"')}
      </div>
      {inp("j-position", "Position", "Position applying for", "الوظيفة المتقدَّم لها", phen="", phar="")}
      <div class="row2">
        {inp("j-exp", "Years of Experience", "Years of experience", "سنوات الخبرة", "number", phen="e.g. 3", phar="مثال: 3", extra='min="0" max="60"')}
        <div class="field"><label for="j-avail">{T("Availability", "التفرّغ")} <span class="req">*</span></label><select id="j-avail" name="Availability" data-i18n-options required>{av}</select></div>
      </div>
      {inp("j-cert", "Certifications", "Certifications (if any)", "الشهادات (إن وجدت)", req=False, phen="e.g. ACE, NASM, ISSA…", phar="مثال: ACE، NASM، ISSA…")}
      {inp("j-cv", "CV Link", "Link to your CV / LinkedIn", "رابط السيرة الذاتية / لينكدإن", "url", req=False, phen="https://", phar="https://", extra='dir="ltr"')}
      <div class="field"><label for="j-about">{T("Tell us about yourself", "عرّفنا بنفسك")}</label><textarea id="j-about" name="About" {ph("Experience, skills, why EVO…", "خبراتك ومهاراتك ولماذا EVO…")}></textarea></div>
      {submit_btn("Submit application", "إرسال الطلب")}
      {status_div()}
    </form>
  </div>
</section>
"""


# ------------------------------------------------------------------ CONTACT
def contact():
    subjects = [("General Inquiry", "استفسار عام"), ("Free Trial Session", "حجز حصة تجريبية مجانية"),
                ("Membership", "الاشتراكات"), ("Personal Training", "التدريب الشخصي"),
                ("Group Classes", "الحصص الجماعية"), ("Feedback", "ملاحظات واقتراحات")]
    so = "".join(f'<option value="{en}" data-en="{en}" data-ar="{ar}">{en}</option>' for en, ar in subjects)
    times = [("Morning (6 AM – 12 PM)", "صباحًا (6 ص – 12 م)"), ("Afternoon (12 – 5 PM)", "ظهرًا (12 – 5 م)"), ("Evening (5 – 11 PM)", "مساءً (5 – 11 م)")]
    to = "".join(f'<option value="{en}" data-en="{en}" data-ar="{ar}">{en}</option>' for en, ar in times)

    infos = [
        (f"tel:{PHONE_INTL}", "phone", "Call us", "اتصل بنا", f'<span dir="ltr">{PHONE}</span>', ""),
        (WA, "wa", "WhatsApp", "واتساب", f'<span dir="ltr">{PHONE}</span>', ' target="_blank" rel="noopener"'),
        (IG, "instagram", "Instagram", "إنستغرام", '<span dir="ltr">@evogymjo</span>', ' target="_blank" rel="noopener"'),
        (FB, "facebook", "Facebook", "فيسبوك", "EVO GYM", ' target="_blank" rel="noopener"'),
        (MAPS, "pin", "Location", "الموقع", T("Dabouq District, Amman", "منطقة دابوق، عمّان"), ' target="_blank" rel="noopener"'),
        ("hours.html", "clock", "Opening hours", "ساعات العمل", T("Sat–Thu 6 AM–11 PM · Fri 9 AM–9 PM", "السبت–الخميس 6 ص–11 م · الجمعة 9 ص–9 م"), ""),
    ]
    il = "".join(f'<a class="card info reveal" style="--d:{i * 0.06:.2f}s" href="{h}"{tgt}><div class="icon">{ico(ic)}</div><div><small>{T(en, ar)}</small><b>{v}</b></div></a>'
                 for i, (h, ic, en, ar, v, tgt) in enumerate(infos))

    return page_hero("Contact Us", "تواصل معنا", T('Get in <span class="accent">Touch</span>', 'تواصل <span class="accent">معنا</span>'),
                     "Questions, memberships or a free trial session — send us a message and our team will reply shortly.",
                     "أسئلة أو اشتراكات أو حصة تجريبية مجانية — أرسل لنا رسالة وسيرد فريقنا قريبًا.", "HELLO") + f"""
<section class="section" id="trial">
  <div class="container contact-wrap">
    <div class="info-list">{il}</div>
    <form class="card form-card reveal" data-remote="contact" novalidate id="form">
      <span class="eyebrow">{T("Free trial available", "حصة تجريبية مجانية")}</span>
      <h2 class="h-md">{T("Send a message", "أرسل رسالة")}</h2>
      {TB('Choose <strong class="accent">"Free Trial Session"</strong> to book your first visit on us.', 'اختر <strong class="accent">"حجز حصة تجريبية مجانية"</strong> لتحجز زيارتك الأولى مجانًا.')}
      <input type="hidden" name="_subject" value="New message — EVO GYM website">
      <input type="hidden" name="Form" value="Contact">
      <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
      {inp("c-name", "Full Name", "Full name", "الاسم الكامل", phen="Your full name", phar="اسمك الكامل", extra='autocomplete="name"')}
      <div class="row2">
        {inp("c-phone", "Phone", "Phone", "رقم الهاتف", "tel", phen="07X XXX XXXX", phar="07X XXX XXXX", extra='autocomplete="tel" dir="ltr"')}
        {inp("c-email", "Email", "Email", "البريد الإلكتروني", "email", phen="name@email.com", phar="name@email.com", extra='autocomplete="email" dir="ltr"')}
      </div>
      <div class="field"><label for="c-subject">{T("Subject", "الموضوع")} <span class="req">*</span></label><select id="c-subject" name="Subject" data-i18n-options required>{so}</select></div>
      <div class="trial-fields">
        <div class="row2">
          <div class="field"><label for="c-date">{T("Preferred date", "التاريخ المفضّل")} <span class="req">*</span></label><input id="c-date" name="Trial Date" type="date"></div>
          <div class="field"><label for="c-time">{T("Preferred time", "الوقت المفضّل")} <span class="req">*</span></label><select id="c-time" name="Trial Time" data-i18n-options>{to}</select></div>
        </div>
      </div>
      <div class="field"><label for="c-msg">{T("Message", "الرسالة")}</label><textarea id="c-msg" name="Message" {ph("How can we help you?", "كيف يمكننا مساعدتك؟")}></textarea></div>
      {submit_btn("Send message", "إرسال")}
      {status_div()}
    </form>
  </div>
</section>
<section class="section--tight section--alt">
  <div class="container"><div class="map reveal zoom" style="aspect-ratio:21/8;min-height:320px"><iframe src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="EVO GYM location map"></iframe></div></div>
</section>
"""
