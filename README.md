# FeelHarmonic

Vieno puslapio svetainė **trimis kalbomis** (lietuvių, anglų, italų):
koncertai ir performansai, edukacijos ir mokymai, terapiniai bei sąmoningumo
renginiai, šventės nuo A iki Z.

Statinis puslapis — jokių duomenų bazių, jokio WordPress. Redaguojami failai:

| Failas | Kam |
|---|---|
| `turinys/lt.json` | **Visas lietuviško puslapio tekstas** |
| `turinys/en.json` | Angliško |
| `turinys/it.json` | Itališko |
| `assets/js/main.js` | `CONFIG` blokas viršuje: el. paštas ir formos adresas |
| `assets/css/style.css` | Spalvos (`:root` blokas viršuje) |
| `build.py` | Puslapio karkasas (HTML) — retai |

Failai `index.html`, `en/index.html`, `it/index.html` ir `sitemap.xml`
**sukuriami automatiškai** — ranka jų neredaguoti.

| Kalba | Adresas | Failas |
|---|---|---|
| Lietuvių | https://www.feelharmonic.lt/ | `index.html` |
| Anglų | https://www.feelharmonic.lt/en/ | `en/index.html` |
| Italų | https://www.feelharmonic.lt/it/ | `it/index.html` |

---

## 1. Perkurti puslapius ir paleisti lokaliai

Pakeitus tekstą `turinys/*.json`:

```bash
python build.py
```

Perrašo visus tris puslapius ir `sitemap.xml`. Reikia tik Python 3, jokių
bibliotekų. Įkėlus pakeitimą į GitHub tą patį padaro ir GitHub Actions, tad
komandos paleisti nebūtina.

Peržiūrai reikia serverio (kitaip neveiks kalbų perjungiklis):

```bash
python -m http.server 8000
```

Tada http://localhost:8000/

---

## 2. Įkelti į GitHub

Repozitorija dar nesukurta GitHub'e. Prisijunk ir sukurk:

```bash
gh auth login
```

Tada iš šio aplanko:

```bash
gh repo create feelharmonic --public --source=. --remote=origin --push
```

Jei nenori naudoti `gh`, sukurk tuščią repozitoriją per github.com (pavadinimas `feelharmonic`,
**be** README) ir paleisk:

```bash
git remote add origin https://github.com/daunyteelena-byte/feelharmonic.git
git push -u origin main
```

---

## 3. Įjungti GitHub Pages

GitHub → repozitorija `feelharmonic` → **Settings** → **Pages**:

- **Source:** `Deploy from a branch`
- **Branch:** `main`, aplankas `/ (root)`
- **Save**

Po 1–2 min. svetainė bus adresu:
`https://daunyteelena-byte.github.io/feelharmonic/`

Prijungus domeną (žr. 5 skyrių) tas adresas persiunčia į `https://www.feelharmonic.lt/`.

Pastaba: GitHub Pages nemokamai veikia tik **viešose** repozitorijose.

---

## 4. Prijungti formą (kad užklausos ateitų į paštą)

Kol kas mygtukas „Siųsti užklausą“ atidaro el. pašto programą su paruoštu laišku.
Kad užklausos ateitų automatiškai:

1. Registruokis [formspree.io](https://formspree.io) (nemokamai — 50 užklausų per mėnesį).
2. Sukurk naują formą, nurodyk savo el. paštą.
3. Nukopijuok gautą adresą (`https://formspree.io/f/xxxxxxxx`).
4. `assets/js/main.js`, `CONFIG` blokas:

```js
var CONFIG = {
  email: "elena.daunyte@feelharmonic.lt",
  formEndpoint: "https://formspree.io/f/xxxxxxxx"
};
```

5. `git commit` ir `git push` — po minutės veiks.

Pirmą užklausą Formspree paprašys patvirtinti el. paštu. Būtinai išsiųsk testinę.

---

## 5. Domenas feelharmonic.lt

Domenas nupirktas Hostingeryje 2026-09-07. Pagrindinis adresas — **`www.feelharmonic.lt`**;
šakninis `feelharmonic.lt` į jį persiunčiamas paties GitHub.

**Repozitorijoje** jau yra `CNAME` failas su eilute `www.feelharmonic.lt`. Jo trinti negalima:
be jo GitHub nežino, kurią repozitoriją rodyti tuo adresu.

> Jei GitHub Pages nustatymuose įrašysi domeną per naršyklę, GitHub `CNAME` failą sukurs pats —
> tada prieš kitą `git push` būtina `git pull`, kitaip pushinsi be to failo ir domenas nustos veikti.

**Hostinger DNS zonoje** (Domains → feelharmonic.lt → DNS / Nameservers) turi būti:

| Tipas | Pavadinimas | Reikšmė |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `daunyteelena-byte.github.io` |

MX ir TXT įrašų, kuriuos Hostingeris sukūrė paštui, **liesti negalima** — jie nesusiję su puslapiu.

**GitHub** → Settings → Pages → Custom domain: `www.feelharmonic.lt` → Save.
Palaukus, kol atsiras varnelė „DNS check successful", įjungti **Enforce HTTPS**.
Sertifikatas išduodamas per 15 min – kelias valandas.

Kaip visa tai veikia ir kur genda, paaiškinta faile `../domeno-schema.html`.

---

## 6. Kaip atnaujinti turinį

```bash
git add -A
git commit -m "Atnaujintas turinys"
git push
```

Jei keitei `turinys/**` arba `build.py`, GitHub Actions veiksmas
(`.github/workflows/build.yml`) pats perkuria HTML ir įrašo jį atgal į šaką;
tada GitHub Pages paskelbia puslapį. Iš viso ~2 min.

Sugadinus JSON (pamiršta kabutė ar kablelis) veiksmas nulūžta, o gyvas puslapis
lieka nepakitęs. Būseną matyti čia:
https://github.com/daunyteelena-byte/feelharmonic/actions

---

## Ką dar reikia užpildyti

Žr. [TODO.md](TODO.md). Puslapyje visos neužpildytos vietos pažymėtos
punktyriniu rėmeliu — jos matomos ir lankytojui, todėl prieš siunčiant
nuorodą užsakovams jas reikia pakeisti tikru turiniu.

---

## 7. Vizitinės kortelės

`spauda/vizitine.html` — spaudai paruoštas šablonas (85 × 55 mm + 3 mm nuopjova).
Atidaryk Chrome ir spausk `Ctrl + P` → Save as PDF, mastelis 100 %, paraštės None,
„Background graphics“ įjungta. Gausi dviejų puslapių PDF, kurį priima spaustuvės.
Visos instrukcijos ir CMYK reikšmės surašytos pačiame faile.

---

## 8. Perdavimas ir priežiūra

- **[ADMIN.md](ADMIN.md)** — instrukcija savininkei: kaip pačiai keisti tekstą,
  kainas, nuotraukas ir atsiliepimus per GitHub svetainę, be programavimo.
- **[HANDOVER.md](HANDOVER.md)** — techninis aprašymas tam, kas prižiūrės
  puslapį toliau: struktūra, dizaino sistema, hostingas, sprendimų motyvai.
