"""Generates the static EVO GYM site. Run: python3 build/build.py"""
import os
from layout import page
import pages_a as A
import pages_b as B

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESC = "EVO GYM — premium mixed training facility in Dabouq, Amman. Train. Transform. Evolve."

PAGES = [
    ("index.html", "EVO GYM | Train. Transform. Evolve.", "EVO GYM | تمرّن. تحوّل. تطوّر.", A.home),
    ("membership.html", "Membership | EVO GYM", "الاشتراكات | EVO GYM", A.membership),
    ("trainers.html", "Trainers | EVO GYM", "المدربون | EVO GYM", A.trainers),
    ("hours.html", "Opening Hours | EVO GYM", "ساعات العمل | EVO GYM", A.hours),
    ("services.html", "Services | EVO GYM", "الخدمات | EVO GYM", A.services),
    ("classes.html", "Classes Schedule | EVO GYM", "جدول الحصص | EVO GYM", B.classes),
    ("tools.html", "Fitness Tools — BMI, BMR & TDEE | EVO GYM", "أدوات اللياقة | EVO GYM", B.tools),
    ("gallery.html", "Gallery | EVO GYM", "المعرض | EVO GYM", B.gallery),
    ("careers.html", "Careers | EVO GYM", "التوظيف | EVO GYM", B.careers),
    ("contact.html", "Contact Us | EVO GYM", "تواصل معنا | EVO GYM", B.contact),
]

for fn, ten, tar, fn_body in PAGES:
    html = page(fn, ten, tar, DESC, fn_body())
    with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print("built", fn, len(html))
