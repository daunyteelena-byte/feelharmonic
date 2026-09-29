# Techninis aprašymas

Skirta tam, kas prižiūrės puslapį toliau — žmogui arba AI sesijai.
Nereikia jokio ankstesnio konteksto: viskas, ką reikia žinoti, yra čia.

## Kas tai

Statinis vieno puslapio tinklalapis **trimis kalbomis** — lietuvių, anglų ir
italų. Jokio karkaso, jokio `npm install`, jokių priklausomybių: naršyklė gauna
paprastą HTML.

Vienintelis įrankis — `build.py`: ~450 eilučių Python be bibliotekų, kuris iš
trijų JSON failų ir vieno HTML karkaso sugeneruoja tris puslapius. Tai
sąmoningas kompromisas: be jo tą patį tekstą reikėtų taisyti trijose vietose ir
kalbos neišvengiamai išsiskirtų. Sugeneruoti failai **guli repozitorijoje**,
todėl hostingui jokio build žingsnio nereikia — GitHub Pages tiesiog serviruoja
jau paruoštą HTML.

Kalba dokumentacijoje ir kodo komentaruose: lietuvių.

## Failai

```
build.py                generatorius: turinys/*.json + karkasas -> HTML
turinys/lt.json         lietuviško puslapio tekstas
turinys/en.json         angliško
turinys/it.json         itališko
index.html              SUGENERUOTAS lietuviškas puslapis — ranka neredaguoti
en/index.html           SUGENERUOTAS angliškas
it/index.html           SUGENERUOTAS itališkas
sitemap.xml             SUGENERUOTAS (visos trys kalbos su hreflang)
.github/workflows/build.yml   GitHub Actions: perkuria puslapius po push
404.html                klaidos puslapis (rašomas ranka, tik lietuviškai)
favicon.svg             ikonėlė (firminis ženklas)
assets/css/style.css    visi stiliai; spalvos ir šriftai — :root bloke viršuje
assets/js/main.js       CONFIG blokas + meniu, animacijos, forma, nuotraukos
assets/img/             nuotraukos (žr. ADMIN.md dėl pavadinimų)
spauda/vizitine.html    vizitinių kortelių šablonas spaudai
spauda/FeelHarmonic-vizitine.pdf   sugeneruotas PDF
ADMIN.md                instrukcija savininkei (be programavimo)
TODO.md                 ko dar trūksta turinyje
```

## Trys kalbos

| Kalba | Adresas | Failas |
|---|---|---|
| Lietuvių | `https://www.feelharmonic.lt/` | `index.html` |
| Anglų | `https://www.feelharmonic.lt/en/` | `en/index.html` |
| Italų | `https://www.feelharmonic.lt/it/` | `it/index.html` |

Kiekvienas puslapis turi savo `<html lang>`, `<title>`, `description`,
`canonical`, `og:locale` ir pilną `hreflang` rinkinį su `x-default` į lietuvišką
versiją. Turinys tas pats — verstas, ne sutrumpintas.

Sekcijų `id` (`#paslaugos`, `#programos`, …) visose kalbose **vienodi**, todėl
CSS, JS ir vidinės nuorodos bendros. Kalbų perjungiklis rodomas tik antraštėje —
išskleidžiamas sąrašas (`.lang-menu`, `langmenu()` faile `build.py`), matosi tik
esama kalba; jo nuorodos absoliučios (`/`, `/en/`, `/it/`).

**Pasekmė:** dukart spustelėjus `index.html` (`file://`) puslapis veikia, bet
kalbų perjungiklis — ne, nes absoliutus `/en/` rodo į disko šaknį. Norint
patikrinti perjungiklį, reikia serverio (žr. „Paleisti lokaliai“).

## Kaip perkurti puslapius

```bash
python build.py
```

Perrašo `index.html`, `en/index.html`, `it/index.html` ir `sitemap.xml`.
Reikia tik Python 3 — jokių bibliotekų.

Tą patį daro ir GitHub Actions: kai į `main` įkeliamas pakeitimas faile
`turinys/**` arba `build.py`, veiksmas paleidžia generatorių ir pats įrašo
perkurtus failus atgal į šaką. Todėl tekstą galima taisyti tiesiai GitHub
svetainėje, nieko nediegiant.

Jei JSON sugadinamas (pamiršta kabutė ar kablelis), veiksmas nulūžta su raudonu
kryželiu, o gyvas puslapis lieka nepakitęs iki taisymo.

## Dizaino sistema

Spalvos ir šriftai aprašyti kintamaisiais `assets/css/style.css` pradžioje.
Keičiant temą užtenka pataisyti `:root` bloką — visa kita paseks.

| Kintamasis | Reikšmė | Kur naudojama |
|---|---|---|
| `--teal` | `#0B3C41` | Meniu, hero, CTA juosta, poraštė |
| `--teal-deep` | `#072B2F` | Poraštė, tuščios nuotraukų vietos |
| `--gold` | `#CE8E34` | Dekoracijos, mygtukai, ženklas |
| `--gold-lt` | `#E2A94F` | Smulkus tekstas ant tamsaus fono |
| `--gold-ink` | `#8A5E18` | Tekstas ant šviesaus fono (kontrastui) |
| `--cream` / `--paper` | `#F6F1E6` / `#FCFAF4` | Šviesios juostos |

**Svarbu dėl kontrasto:** ryškus auksas ant kreminio fono duoda tik 2,4:1 —
neįskaitomas. Todėl tekstui šviesiame fone naudojamas `--gold-ink`, o ryškusis
paliktas dekoracijoms ir tamsiam fonui. Visos teksto poros patikrintos,
rezultatai 4,78–12,09:1 (WCAG AA). Keičiant spalvas tai reikia pertikrinti.

Šriftai: **Playfair Display** (antraštės) ir **Jost** (tekstas), iš Google Fonts.
Abu turi lietuviškas raides (latin-ext subsetas).

Firminis ženklas — inline SVG `<symbol id="mark">` kiekvieno puslapio pradžioje
(konstanta `MARK` faile `build.py`). Naudojamas per `<use href="#mark"/>` meniu,
hero fone, skirtuke, poraštėje ir tuščiose nuotraukų vietose.

Vėliau pridėti stiliai — kalbų perjungiklis (`.lang-menu`), „NEW“ ženklelis
(`.tag-new`), studijos blokas (`.studio`) ir vaizdo įrašo rėmelis (`.video`) —
surašyti failo gale, po komentaru su pavadinimu.

## JavaScript

Vienas failas, be priklausomybių, **bendras visoms trims kalboms**. Viršuje —
`CONFIG` blokas (el. paštas ir Formspree adresas), tai vienintelė vieta, kurią
reikia redaguoti kasdienėje priežiūroje.

Kad tas pats failas veiktų visomis kalbomis, visi formos pranešimai („Siunčiama…“,
„Ačiū — užklausa gauta“ ir kt.) imami iš `data-*` atributų ant `<form>`, o į juos
patenka iš `turinys/<kalba>.json` bloko `"js"`. Funkcija `t("msg-ok")` faile
`main.js` nuskaito atitinkamą atributą.

Ką daro:
- mobilųjį meniu (burger),
- aktyvios sekcijos žymėjimą meniu (IntersectionObserver),
- turinio pasirodymą slenkant (`.reveal` klasė),
- užklausos formą: siunčia į Formspree, o jei jis nesukonfigūruotas —
  atidaro el. pašto programą su paruoštu laišku,
- **trūkstamų nuotraukų tvarkymą**: jei failo nėra, vietoje jo rodomas
  firminis ženklas; jei nėra nė vienos galerijos nuotraukos, visa galerijos
  skiltis ir nuoroda meniu paslepiamos; jei nėra „Apie“ nuotraukos, tekstas
  išsiplečia per visą plotį.

Puslapis veikia ir be JavaScript — tada tiesiog nėra animacijų ir mobiliojo
meniu. `.reveal` elementai paslepiami tik tada, kai JS įsikrauna (`.js` klasė
ant `<html>`), todėl be JS turinys matomas iš karto.

## Hostingas

GitHub Pages, šaka `main`, aplankas `/` (root).
Adresas: https://www.feelharmonic.lt/ (senasis
https://daunyteelena-byte.github.io/feelharmonic/ persiunčia į jį).

Failas `.nojekyll` išjungia Jekyll apdorojimą.
Nuorodos į CSS, JS ir nuotraukas reliatyvios (`en/` ir `it/` puslapiuose —
su `../`), todėl puslapį galima perkelti į bet kurį hostingą. Absoliučios yra
tik kalbų perjungiklio nuorodos — jos reikalauja, kad svetainė gulėtų domeno
šaknyje (taip ir yra).

Įkėlus pakeitimą į `main`, puslapis persikuria automatiškai per ~1 min. Jei
pakeistas `turinys/**` arba `build.py`, prieš tai dar suveikia GitHub Actions
veiksmas, kuris perkuria HTML — tada iš viso užtrunka ~2 min.

## Domenas

`feelharmonic.lt` nupirktas Hostingeryje 2026-09-07. Pagrindinis adresas —
`www.feelharmonic.lt`; šakninį domeną GitHub persiunčia pats.

- DNS Hostingerio zonoje: keturi A įrašai į `185.199.108–111.153` ir
  `CNAME www` į `daunyteelena-byte.github.io.` MX ir TXT įrašai priklauso
  paštui — jų liesti negalima.
- Repozitorijos šaknyje `CNAME` su eilute `www.feelharmonic.lt`.
  **Trinti negalima.** Jei domenas įrašomas per GitHub sąsają, GitHub šį failą
  sukuria pats — tada prieš kitą `git push` būtinas `git pull`, kitaip
  pushinsi be jo ir domenas nustos veikti.
- GitHub → Settings → Pages → Custom domain, tada **Enforce HTTPS**.
- `og:image`, `canonical`, `robots.txt` ir `sitemap.xml` jau nurodo į
  `https://www.feelharmonic.lt/`.

## Vizitinės

`spauda/vizitine.html` — 85 × 55 mm su 3 mm nuopjova (failas 91 × 61 mm).
Kortelių fonai nupiešti SVG figūromis, ne CSS fonais, todėl spausdinami
visada, nepriklausomai nuo „Background graphics“ nustatymo.

PDF generuojamas taip:

```bash
chrome --headless=new --no-pdf-header-footer \
  --print-to-pdf=FeelHarmonic-vizitine.pdf spauda/vizitine.html
```

Rezultatas turi būti 2 puslapiai po 258 × 173 pt (= 91 × 61 mm).

## Paleisti lokaliai

```bash
python -m http.server 8000
```

Tada http://localhost:8000/ — veikia ir kalbų perjungiklis. Dukart spustelėjus
`index.html` puslapis irgi atsidarys, bet perjungiklio nuorodos neveiks
(žr. „Trys kalbos“).

## Ko šiame projekte NĖRA (ir kodėl)

- **Karkaso, npm, node_modules** — vienintelė priklausomybė yra Python 3
  standartinė biblioteka. Sugeneruoti puslapiai laikomi repozitorijoje, todėl
  net ir dingus generatoriui svetainė toliau veiks.
- **Kalbos perjungimo per JavaScript** — kiekviena kalba turi savo adresą ir
  savo HTML. Taip Google indeksuoja visas tris versijas, o puslapis veikia ir
  išjungus JS. Automatinio permetimo pagal naršyklės kalbą sąmoningai nėra:
  GitHub Pages neturi serverio pusės, o JS permetimas kenkia SEO ir erzina.
- **CMS** — realiai keičiasi tik kainos, nuotraukos ir atsiliepimai, kelis
  kartus per metus, o `turinys/*.json` redaguojamas tiesiai GitHub svetainėje.
  Jei prireiktų, tinkamiausias kelias: hostingą perkelti į Netlify (ta pati
  repozitorija, nemokamai) ir uždėti Decap CMS.
- **Tamsios temos** — dizainas sąmoningai vienspalvis, paimtas iš logotipo.

## Į ką atkreipti dėmesį keičiant

- `index.html`, `en/index.html`, `it/index.html` ir `sitemap.xml` **perrašomi**.
  Taisyti reikia `turinys/*.json` arba `build.py`.
- Pridedant naują lauką į JSON, jį reikia pridėti **visose trijose** kalbose —
  kitaip `build.py` nulūš su `KeyError` ir tai bus matyti Actions žurnale.
- JSON laukuose leidžiamas paprastas HTML (`<em>`, `<span class="fill">`),
  todėl tekstas neekranuojamas. Į turinį nedėti nepatikimo teksto.
- Sekcijų `id` keisti negalima nekeičiant `nav`/`footer` nuorodų visose kalbose.
- **`loading="lazy"` prie `data-optional` nuotraukų dėti negalima.** Trūkstamų
  nuotraukų tvarkymas `main.js` remiasi `error` įvykiu; atidėta nuotrauka
  niekada nepradeda krautis, tad įvykio nesulaukia — galerija lieka nepaslėpta
  su tuščiomis dėžėmis, o firminis ženklas neatsiranda. Kai visos nuotraukos
  bus įkeltos ir atsarginio varianto nebereikės, `lazy` galima grąžinti.
- `.about-photo` klasę naudoja ir studijos, ir „Apie“ skiltis, o studija
  puslapyje yra anksčiau — todėl `main.js` jos ieško tik `.about` viduje.

## Kas dar neužbaigta

Žr. [TODO.md](TODO.md).
