/* EVO GYM — site script */
(function () {
  "use strict";
  var FORM_ENDPOINT = "https://formsubmit.co/ajax/hamzehabunemeh@gmail.com";
  var WA = "https://wa.me/962790080089";
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- i18n ---------------- */
  var STR = {
    en: {
      openNow: "Open now", closedNow: "Closed now",
      closesAt: "Closes at {t} today", opensAt: "Opens at {t}", opensTomorrow: "Opens tomorrow at {t}",
      today: "Today", noClass: "No group classes this day — the gym floor is open as usual.",
      bmiUnder: "Underweight", bmiNormal: "Healthy weight", bmiOver: "Overweight", bmiObese: "Obese",
      bmiHint: "BMI is a quick screening number. It doesn't separate muscle from fat, so athletes may read higher.",
      fill: "Please fill in all fields with valid numbers.",
      kcal: "kcal / day", sending: "Sending…",
      ok: "Thank you! Your message has been sent. Our team will get back to you shortly.",
      okJob: "Thank you! Your application has been received. We'll contact you if your profile matches.",
      err: 'Something went wrong while sending. Please try again or <a href="' + WA + '" target="_blank" rel="noopener">message us on WhatsApp</a>.',
      muted: "Sound off", unmuted: "Sound on",
      activate: "This form is waiting for one-time activation by the gym. Please try again later or message us on WhatsApp.",
      days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    },
    ar: {
      openNow: "مفتوح الآن", closedNow: "مغلق الآن",
      closesAt: "يغلق اليوم الساعة {t}", opensAt: "يفتح الساعة {t}", opensTomorrow: "يفتح غدًا الساعة {t}",
      today: "اليوم", noClass: "لا توجد حصص جماعية في هذا اليوم — صالة التمرين مفتوحة كالمعتاد.",
      bmiUnder: "نقص في الوزن", bmiNormal: "وزن صحي", bmiOver: "زيادة في الوزن", bmiObese: "سمنة",
      bmiHint: "مؤشر كتلة الجسم رقم تقريبي للفحص السريع، ولا يفرّق بين العضل والدهون، لذا قد يظهر أعلى لدى الرياضيين.",
      fill: "يرجى تعبئة جميع الحقول بأرقام صحيحة.",
      kcal: "سعرة / يوم", sending: "جارٍ الإرسال…",
      ok: "شكرًا لك! تم إرسال رسالتك بنجاح، وسيتواصل معك فريقنا قريبًا.",
      okJob: "شكرًا لك! تم استلام طلبك، وسنتواصل معك إذا كان ملفك مناسبًا.",
      err: 'حدث خطأ أثناء الإرسال. حاول مرة أخرى أو <a href="' + WA + '" target="_blank" rel="noopener">راسلنا على واتساب</a>.',
      muted: "الصوت مغلق", unmuted: "الصوت يعمل",
      activate: "هذا النموذج بانتظار تفعيل لمرة واحدة من إدارة النادي. يرجى المحاولة لاحقًا أو مراسلتنا على واتساب.",
      days: ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"]
    }
  };
  function lang() { return root.lang === "ar" ? "ar" : "en"; }
  function t(k) { return STR[lang()][k]; }
  var langHooks = [];

  function applyLang(l) {
    root.lang = l;
    root.dir = l === "ar" ? "rtl" : "ltr";
    try { localStorage.setItem("evo-lang", l); } catch (e) {}
    var tt = root.getAttribute("data-title-" + l);
    if (tt) document.title = tt;
    document.querySelectorAll("[data-ph-en]").forEach(function (el) {
      el.setAttribute("placeholder", el.getAttribute("data-ph-" + l) || "");
    });
    document.querySelectorAll("option[data-en]").forEach(function (o) {
      o.textContent = o.getAttribute("data-" + l);
    });
    document.querySelectorAll("[data-label-en]").forEach(function (el) {
      el.setAttribute("aria-label", el.getAttribute("data-label-" + l) || "");
    });
    langHooks.forEach(function (fn) { fn(); });
  }
  document.querySelectorAll(".lang-btn").forEach(function (b) {
    b.addEventListener("click", function () { applyLang(lang() === "ar" ? "en" : "ar"); });
  });

  /* ---------------- smooth scroll (Lenis) ---------------- */
  var lenis = null;
  if (!reduce && window.Lenis) {
    lenis = new window.Lenis({ duration: 1.15, smoothWheel: true, easing: function (x) { return Math.min(1, 1.001 - Math.pow(2, -10 * x)); } });
    (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
  }

  /* ---------------- header / progress / top ---------------- */
  var header = document.querySelector(".header");
  var progress = document.querySelector(".progress");
  var toTop = document.querySelector(".to-top");
  var parallax = [].slice.call(document.querySelectorAll("[data-parallax]"));
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("scrolled", y > 30);
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
    if (toTop) toTop.classList.toggle("show", y > 700);
    if (!reduce) parallax.forEach(function (el) {
      var s = parseFloat(el.getAttribute("data-parallax")) || 0.2;
      el.style.transform = "translate3d(0," + (y * s).toFixed(1) + "px,0)";
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () {
    if (lenis) lenis.scrollTo(0); else window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* ---------------- mobile drawer ---------------- */
  var burger = document.querySelector(".burger");
  function closeNav() { document.body.classList.remove("nav-open"); if (burger) burger.setAttribute("aria-expanded", "false"); if (lenis) lenis.start(); }
  if (burger) burger.addEventListener("click", function () {
    var open = document.body.classList.toggle("nav-open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) { open ? lenis.stop() : lenis.start(); }
  });
  document.querySelectorAll(".drawer__bg, .drawer nav a").forEach(function (el) { el.addEventListener("click", closeNav); });
  document.querySelectorAll(".drawer nav a").forEach(function (a, i) { a.style.transitionDelay = (0.05 + i * 0.04) + "s"; });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeNav(); });

  /* ---------------- reveal + counters ---------------- */
  function countUp(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var dur = 1800, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var e = 1 - Math.pow(1 - p, 4);
      el.textContent = (end * e).toFixed(dec);
      if (p < 1) requestAnimationFrame(step);
    }
    if (reduce) el.textContent = end.toFixed(dec); else requestAnimationFrame(step);
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add("in");
      en.target.querySelectorAll("[data-count]").forEach(countUp);
      if (en.target.hasAttribute("data-count")) countUp(en.target);
      io.unobserve(en.target);
    });
  }, { threshold: 0.14, rootMargin: "0px 0px -6% 0px" });
  document.querySelectorAll(".reveal, .weekbar, .stats").forEach(function (el) { io.observe(el); });

  /* card cursor glow */
  document.querySelectorAll(".card").forEach(function (c) {
    c.addEventListener("pointermove", function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty("--mx", (e.clientX - r.left) + "px");
      c.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  /* ---------------- videos ---------------- */
  var vids = [].slice.call(document.querySelectorAll("video[data-autoplay]"));
  function setBtn(btn, v) {
    btn.classList.toggle("unmuted", !v.muted);
    var lbl = btn.querySelector(".lbl");
    if (lbl) lbl.textContent = v.muted ? t("muted") : t("unmuted");
    btn.setAttribute("aria-pressed", v.muted ? "false" : "true");
  }
  vids.forEach(function (v) {
    v.muted = true; v.defaultMuted = true; v.setAttribute("muted", "");
    var p = v.play(); if (p && p.catch) p.catch(function () {});
    var btn = v.closest(".vframe").querySelector(".sound-btn");
    if (btn) {
      setBtn(btn, v);
      btn.addEventListener("click", function () {
        var willUnmute = v.muted;
        vids.forEach(function (o) { if (o !== v) { o.muted = true; var b = o.closest(".vframe").querySelector(".sound-btn"); if (b) setBtn(b, o); } });
        v.muted = !willUnmute;
        if (v.paused) v.play().catch(function () {});
        setBtn(btn, v);
      });
      langHooks.push(function () { setBtn(btn, v); });
    }
  });
  if (vids.length) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { v.play().catch(function () {}); }
        else { v.pause(); }
      });
    }, { threshold: 0.15 });
    vids.forEach(function (v) { vio.observe(v); });
  }

  /* ---------------- Amman time helpers ---------------- */
  function ammanNow() {
    var parts = new Intl.DateTimeFormat("en-US", { timeZone: "Asia/Amman", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).formatToParts(new Date());
    var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
    var map = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return { day: map[o.weekday], mins: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10) };
  }
  var HOURS = { 0: [6, 23], 1: [6, 23], 2: [6, 23], 3: [6, 23], 4: [6, 23], 5: [9, 21], 6: [6, 23] };
  function fmtH(h) {
    var ar = lang() === "ar";
    var hh = h % 12 === 0 ? 12 : h % 12;
    var suf = h < 12 ? (ar ? "ص" : "AM") : (ar ? "م" : "PM");
    return hh + ":00 " + suf;
  }

  function renderStatus() {
    var box = document.querySelector("[data-status]");
    var n = ammanNow();
    document.querySelectorAll("[data-day-row]").forEach(function (tr) {
      tr.classList.toggle("today", +tr.getAttribute("data-day-row") === n.day);
      tr.querySelector("td").setAttribute("data-today", t("today"));
    });
    document.querySelectorAll("[data-sched-day]").forEach(function (th) {
      th.classList.toggle("today", +th.getAttribute("data-sched-day") === n.day);
    });
    if (!box) return;
    var h = HOURS[n.day], open = n.mins >= h[0] * 60 && n.mins < h[1] * 60;
    box.classList.toggle("open", open); box.classList.toggle("closed", !open);
    box.querySelector("b").textContent = open ? t("openNow") : t("closedNow");
    var sub;
    if (open) sub = t("closesAt").replace("{t}", fmtH(h[1]));
    else if (n.mins < h[0] * 60) sub = t("opensAt").replace("{t}", fmtH(h[0]));
    else sub = t("opensTomorrow").replace("{t}", fmtH(HOURS[(n.day + 1) % 7][0]));
    box.querySelector(".status__sub").textContent = sub;
  }
  renderStatus(); langHooks.push(renderStatus); setInterval(renderStatus, 60000);

  /* ---------------- schedule (mobile tabs) ---------------- */
  var tabs = document.querySelector(".daytabs");
  if (tabs) {
    var lists = document.querySelectorAll(".daylist");
    function showDay(d) {
      tabs.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-d") === d); });
      lists.forEach(function (l) { l.hidden = l.getAttribute("data-d") !== d; });
    }
    tabs.addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) showDay(b.getAttribute("data-d")); });
    var today = String(ammanNow().day);
    showDay(tabs.querySelector('[data-d="' + today + '"]') ? today : tabs.querySelector("button").getAttribute("data-d"));
  }

  /* ---------------- calculators ---------------- */
  var ctabs = document.querySelector(".calc-tabs");
  if (ctabs) {
    ctabs.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      ctabs.querySelectorAll("button").forEach(function (x) { x.classList.toggle("on", x === b); });
      document.querySelectorAll(".calc").forEach(function (c) { c.classList.toggle("on", c.id === b.getAttribute("data-t")); });
    });
    if (location.hash) { var hb = ctabs.querySelector('[data-t="' + location.hash.slice(1) + '"]'); if (hb) hb.click(); }
  }
  function num(form, n) { var v = parseFloat(form.elements[n] && form.elements[n].value); return isFinite(v) && v > 0 ? v : null; }
  function radio(form, n) { var r = form.querySelector('[name="' + n + '"]:checked'); return r ? r.value : null; }
  function animateNum(el, val, dec) {
    if (reduce) { el.textContent = val.toFixed(dec); return; }
    var s = null, from = 0;
    (function step(ts) { if (!s) s = ts; var p = Math.min((ts - s) / 900, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = (from + (val - from) * e).toFixed(dec); if (p < 1) requestAnimationFrame(step); })(performance.now());
  }

  var bmiForm = document.getElementById("bmi-form");
  var lastBmi = null;
  function bmiCat(b) { return b < 18.5 ? ["bmiUnder", "#4aa3ff"] : b < 25 ? ["bmiNormal", "#2ee68a"] : b < 30 ? ["bmiOver", "#ffc23a"] : ["bmiObese", "#ff6b4a"]; }
  function paintBmi() {
    if (lastBmi == null) return;
    var c = bmiCat(lastBmi), cat = document.getElementById("bmi-cat");
    cat.textContent = t(c[0]); cat.style.color = c[1]; cat.style.background = c[1] + "1f";
    document.getElementById("bmi-hint").textContent = t("bmiHint");
  }
  if (bmiForm) bmiForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var h = num(bmiForm, "h"), w = num(bmiForm, "w");
    if (!h || !w) { document.getElementById("bmi-hint").textContent = t("fill"); return; }
    var b = w / Math.pow(h / 100, 2); lastBmi = b;
    animateNum(document.getElementById("bmi-val"), b, 1);
    var pos = Math.max(0, Math.min(1, (b - 12) / (40 - 12)));
    document.querySelector("#bmi .gauge i").style.left = (pos * 100) + "%";
    paintBmi();
  });
  langHooks.push(paintBmi);

  function bmr(form) {
    var a = num(form, "age"), h = num(form, "h"), w = num(form, "w"), s = radio(form, "sex");
    if (!a || !h || !w || !s) return null;
    return 10 * w + 6.25 * h - 5 * a + (s === "m" ? 5 : -161);
  }
  var bmrForm = document.getElementById("bmr-form");
  if (bmrForm) bmrForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var v = bmr(bmrForm), hint = document.getElementById("bmr-hint");
    if (!v) { hint.hidden = false; hint.textContent = t("fill"); return; }
    hint.hidden = true;
    animateNum(document.getElementById("bmr-val"), Math.round(v), 0);
  });
  var tdeeForm = document.getElementById("tdee-form");
  if (tdeeForm) tdeeForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var v = bmr(tdeeForm), act = parseFloat(tdeeForm.elements.act.value), hint = document.getElementById("tdee-hint");
    if (!v) { hint.hidden = false; hint.textContent = t("fill"); return; }
    hint.hidden = true;
    var td = Math.round(v * act);
    animateNum(document.getElementById("tdee-val"), td, 0);
    animateNum(document.getElementById("tdee-cut"), Math.round(td - 500), 0);
    animateNum(document.getElementById("tdee-keep"), td, 0);
    animateNum(document.getElementById("tdee-bulk"), Math.round(td + 300), 0);
  });

  /* ---------------- forms (FormSubmit) ---------------- */
  var ICO_OK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>';
  var ICO_ERR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 7v6M12 17h.01"/></svg>';
  document.querySelectorAll("form[data-remote]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var btn = form.querySelector('button[type="submit"]');
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form), data = {};
      fd.forEach(function (v, k) { data[k] = v; });
      if (data._honey) return;
      data._captcha = "false"; data._template = "table";
      data["Language"] = lang() === "ar" ? "Arabic" : "English";
      btn.disabled = true; btn.classList.add("loading");
      status.className = "form-status";
      fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) === "true") {
            status.className = "form-status ok";
            status.innerHTML = ICO_OK + "<span>" + t(form.getAttribute("data-remote") === "job" ? "okJob" : "ok") + "</span>";
            form.reset(); toggleTrial();
          } else {
            var m = res.j && res.j.message ? String(res.j.message) : "";
            var e = new Error("fail"); e.activation = /activat/i.test(m); throw e;
          }
        })
        .catch(function (e) {
          status.className = "form-status err";
          status.innerHTML = ICO_ERR + "<span>" + t(e && e.activation ? "activate" : "err") + "</span>";
        })
        .then(function () { btn.disabled = false; btn.classList.remove("loading"); });
    });
  });

  /* trial toggle on contact */
  var subj = document.getElementById("c-subject");
  function toggleTrial() {
    var box = document.querySelector(".trial-fields"); if (!box || !subj) return;
    var on = subj.value === "Free Trial Session";
    box.classList.toggle("show", on);
    box.querySelectorAll("input,select").forEach(function (i) { i.required = on; });
  }
  if (subj) {
    subj.addEventListener("change", toggleTrial);
    var qs = new URLSearchParams(location.search);
    if (qs.get("subject")) subj.value = qs.get("subject");
    if (qs.get("plan")) {
      subj.value = "Membership";
      var msg = document.getElementById("c-msg");
      if (msg && !msg.value) msg.value = (lang() === "ar" ? "أرغب بالاشتراك في باقة: " : "I'm interested in the plan: ") + qs.get("plan");
    }
    if (/trial/i.test(location.hash)) { subj.value = "Free Trial Session"; }
    var dt = document.getElementById("c-date");
    if (dt) dt.min = new Date().toISOString().slice(0, 10);
    toggleTrial();
  }

  /* ---------------- lightbox ---------------- */
  var items = [].slice.call(document.querySelectorAll(".g-item"));
  var lb = document.querySelector(".lightbox");
  if (lb && items.length) {
    var img = lb.querySelector("img"), cnt = lb.querySelector(".lb-count"), idx = 0, lastFocus;
    function show(i) {
      idx = (i + items.length) % items.length;
      img.style.opacity = 0;
      var src = items[idx].getAttribute("data-full");
      var pre = new Image(); pre.onload = function () { img.src = src; img.alt = items[idx].querySelector("img").alt; img.style.opacity = 1; }; pre.src = src;
      cnt.textContent = (idx + 1) + " / " + items.length;
    }
    function open(i) { lastFocus = document.activeElement; show(i); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); if (lenis) lenis.stop(); document.body.style.overflow = "hidden"; lb.querySelector(".lb-close").focus(); }
    function close() { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); if (lenis) lenis.start(); document.body.style.overflow = ""; if (lastFocus) lastFocus.focus(); }
    items.forEach(function (it, i) { it.addEventListener("click", function () { open(i); }); });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(idx + 1);
      if (e.key === "ArrowLeft") show(idx - 1);
    });
    var sx = null;
    lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (sx == null) return; var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); sx = null;
    });
  }

  /* year */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  applyLang(lang());
})();
