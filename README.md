# EVO GYM — Website

Train. Transform. Evolve.

Static bilingual (English / Arabic) website for EVO GYM, Dabouq — Amman.

- Live site: https://hamzehabunemeh.github.io/evo-gym-website/
- Pages: Home, Membership, Trainers, Opening Hours, Services, Classes Schedule, Fitness Tools, Gallery, Careers, Contact Us
- Forms (contact / free trial / careers) are sent by email through FormSubmit to the address set in `assets/js/main.js` (`FORM_ENDPOINT`).

## Editing
Page content lives in `build/` (Python). After editing, regenerate the HTML:

```
python3 build/build.py
```

Placeholder content to replace when real data is available: membership prices (`build/pages_a.py → membership`), trainer bios, and the form email address.
