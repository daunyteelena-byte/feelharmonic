# FeelHarmonic — taisyklės Claude sesijai

Statinė svetainė https://www.feelharmonic.lt/ (lietuvių, anglų, italų),
hostinama GitHub Pages iš šakos `main`. Žemiau esančios taisyklės privalomos.

Visas techninis aprašymas — @HANDOVER.md. Instrukcija savininkei (be
programavimo) — `ADMIN.md`. Neužbaigti darbai — `TODO.md`.

## Darbo su git tvarka

- **Prieš bet kokį darbą:** `git pull`. GitHub Actions botas ir redagavimai
  tiesiai GitHub svetainėje rašo į tą pačią `main` šaką.
- **Po push, kuris keitė `turinys/**`, `build.py`, `assets/css/**` ar
  `assets/js/**`,** botas po ~1 min. įkelia
  savo commitą („Puslapiai perkurti is turinio failu“). Todėl prieš kitą push
  vėl `git pull`, kitaip push bus atmestas.
- Commitinti mažais, prasmingais žingsniais, žinutes rašyti lietuviškai.
- Commitinti ir pushinti tik kai žmogus to paprašo. Force push — niekada.
- Konfliktą sugeneruotuose failuose (`index.html`, `en/index.html`,
  `it/index.html`, `sitemap.xml`) spręsti ne ranka: paimti bet kurią versiją ir
  paleisti `python build.py`.

## Kai savininkė nori papildyti puslapį

**Pirmiausia parodyti jai `ISDESTYMAS.md`** — visas skiltis su turiniu, ir rodomas,
ir paslėptas (`PASLEPTA` faile `build.py`: studija, atsiliepimai, parama), kad
matytų, kas jau parašyta ir ką galima grąžinti. Pilnas 14 skilčių išdėstymas
išsaugotas Git žymoje `pilnas-isdestymas-2026-10-03`. Pakeitus turinį ar
skilčių rinkinį — atnaujinti ir `ISDESTYMAS.md`.

## Naršyklės podėlis

CSS ir JS nuorodos turi `?v=<turinio parašas>` (`ver()` faile `build.py`).
Pakeitus `style.css` ar `main.js`, paleisti `python build.py`, kad parašas
atsinaujintų (GitHub botas tai padaro ir pats, bet tik po ~1 min.).

## Ko negalima

- Ranka redaguoti `index.html`, `en/index.html`, `it/index.html`, `sitemap.xml` —
  jie perrašomi. Tekstas keičiamas `turinys/*.json`, karkasas — `build.py`.
- Trinti ar keisti `CNAME` failą — nustotų veikti domenas.
- Pridėti naują JSON lauką tik vienoje kalboje — jis turi būti visose trijose,
  kitaip `build.py` nulūš su `KeyError`.
- Keisti sekcijų `id` nepataisius nuorodų visose kalbose.
- Dėti `loading="lazy"` prie `data-optional` nuotraukų (žr. HANDOVER.md).
- Diegti karkasų, npm ar Python bibliotekų — projektas sąmoningai be
  priklausomybių.

## Patikrinimas prieš commitą

```bash
python build.py
python -m http.server 8000
```

Tada peržiūrėti http://localhost:8000/, `/en/` ir `/it/`. Keičiant spalvas —
pertikrinti kontrastą (WCAG AA, žr. HANDOVER.md „Dizaino sistema“).

## Kalba

Dokumentacija, kodo komentarai ir commitų žinutės — lietuviškai.
