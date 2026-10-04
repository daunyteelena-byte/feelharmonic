# Ką užpildyti

Puslapyje neužpildytos vietos pažymėtos punktyriniu rėmeliu — jos matomos ir lankytojui.
Sąrašas surikiuotas pagal tai, kas labiausiai lemia užsakymą.

Tekstas keičiamas **`turinys/lt.json`, `turinys/en.json`, `turinys/it.json`**, ne
`index.html` (žr. [ADMIN.md](ADMIN.md)).

## 0. Priminti Elenai (įrašyta 2026-10-03)

- [ ] **Pirmojo FeelHarmonic renginio (2023) nuotraukos iš Facebook** — puslapyje
      28 nuotraukos, viešai matomos tik 9 mažos. Elena atsisiųs pilno dydžio
      (⋯ → Download) į `FeelHarmonic/Mano Foto`; paklausti renginio pavadinimo ir vietos.
- [ ] **Fotografų vardai** — labirintas (`labirintas.jpg`), studijiniai portretai su violončele, nauji galerijos kadrai
      (Regnum Musicale, Čiurlionio kvartetas, duetas).
- [x] **Nuotraukų išdidinimas su informacija** — padaryta 2026-10-03 visoms puslapio
      nuotraukoms; duomenys `turinys/*.json` → `"photos"` (event, place, date, by).
- [ ] **Trūksta informacijos nuotraukoms** (`"photos"` blokas): `galerija-1.jpg`, `galerija-3.jpg` — viskas; `labirintas.jpg` — vieta, fotografas; `galerija-5/6/10.jpg` — vieta, metai, fotografas; `galerija-8.jpg` — fotografas; `galerija-26…30.jpg` — renginys, vieta, data, fotografas;
- [x] **„Duetas su Anusausku“** — Artūras Anusauskas, improvizacijų didmeistris (įrašyta 2026-10-03).

## 1. Nuotraukos — svarbiausia

Visos nuotraukos dedamos į aplanką `assets/img/` su **tiksliai tokiais pavadinimais**.
Jos bendros visoms trims kalboms — įkelti reikia tik kartą.

| Failas | Kas tai |
|---|---|
| `elena.jpg` | Portretas su violončele — rodomas pirmame ekrane |
| `apie.jpg` | Antra nuotrauka skiltyje „Apie“ (koncertinė) |
| `galerija-1.jpg` … `galerija-6.jpg` | Galerija: portretas, koncertas salėje, dvaras ar bažnyčia, edukacija mokykloje, lauko renginys, instrumento detalė |
| `paslauga-koncertai.jpg` | Kortelė „Koncertai ir performansai“ (horizontali, 3:2) |
| `paslauga-edukacijos.jpg` | Kortelė „Edukacija ir mokymai“ |
| `paslauga-renginiai.jpg` | Kortelė „Renginiai nuo A iki Z“ |
| `paslauga-terapija.jpg` | Kortelė „Terapiniai ir sąmoningumo renginiai“ *(nauja)* |
| `paslauga-interaktyvu.jpg` | Kortelė „Interaktyvūs koncertai“ *(nauja)* |
| `paslauga-pokalbiai.jpg` | Kortelė „Dive into personality“ *(nauja)* |
| `studija.jpg` | Skiltis „Atvira erdvė — studija“ *(nauja)* |
| `og.jpg` | Nuotrauka, matoma dalinantis nuoroda (1200×630 px) |

Kol failų nėra, puslapis prisitaiko pats: nuotraukų vietose rodomas firminis
ženklas tamsiame fone, „Apie“ skiltis išsiplečia per visą plotį, o galerijos skiltis
kartu su nuoroda meniu paslepiama. Įdėjus failus viskas atsiranda automatiškai —
kode keisti nieko nereikia.

Rekomendacijos: kvadratinės arba vertikalios, ne mažesnės kaip 1200 px pločio,
suspaustos iki ~300 KB (tinka [squoosh.app](https://squoosh.app)).
Naudoti tik tas nuotraukas, kurių teisės priklauso Elenai arba dėl kurių susitarta su fotografu.

## 2. Naujų paslaugų kainos

2026-09-09 pridėtos naujos kryptys. Jų programose kol kas parašyta „Sutartinė“ —
tai teisinga, bet silpniau parduoda nei skaičius. Kai bus aišku, įrašyti „nuo … €“
visose trijose kalbose (`programs` ir `edu` blokai):

- [ ] **Alternatyvus koncertas — performansas** (2–5 atlikėjai)
- [ ] **Interaktyvus koncertas**
- [ ] **Harmonizuojantis renginys** (buvęs „Terapinis“) (90 min, 8–25 dalyviai) — kartu nuspręsti,
      kas yra terapeutas ir kaip dalijamas honoraras
- [ ] **Retreat‘as** (1–3 dienos) — greičiausiai lieka sutartinė, nes labai skiriasi
- [ ] **„Dive into personality“** — atskirai ar kaip priedas prie koncerto
- [ ] **Kūrybinės dirbtuvės** ir **grojimo mokymai** — valandinis įkainis

Kol kainos sutartinės, DUK ir programų prieraše paaiškinta, kad konkreti suma
atsiunčiama per vieną darbo dieną — to užtenka, kad užklausa neužstrigtų.

## 3. Skaičiai ir rekvizitai

Įrašyta 2026-09-05 pagal verslo plano kainoraštį:

- [x] **Kainos „nuo“** — pagal sudėtį: „Kalėdų vakaras“ 450 / 700 / 950 €,
      „Vasaros klasika“ 650 / 900 €, ceremonija nuo 350 €, renginys „po raktu“ nuo 1 500 €
- [x] **Edukacijos kaina** — 5 €/mok. (Kultūros paso riba 2026 m. — 14 €/mok. per metus)
- [x] **Kelionė** — iki 60 km nuo Vilniaus įskaičiuota, toliau 0,25 €/km
- [x] **Atšaukimo terminas** — 14 dienų *(pasiūlymas; jei sutartyje kitaip, pataisyti)*
- [x] **Edukacijos amžiaus grupė** — 1–8 kl. *(pasiūlymas; patvirtinti su Elena)*

Dar reikia — šių įrašyti negalima be tikrų duomenų:

- [ ] **Individualios veiklos pažymos nr.** ir adresas sąskaitoms → DUK ir poraštės rekvizitai
      (trijuose failuose: `faq` ir `footer.details`)
- [ ] **Aparatūros pajėgumas** — kiek žmonių salei pakanka turimos garso sistemos
- [ ] **Socialinių tinklų nuorodos** — kai bus sukurti profiliai (žr. kanalų planą)

Padaryta 2026-09-07:

- [x] **Antras edukacinis užsiėmimas** — „Garso partitūra“, 2–8 kl., 45 min, iki 30, 5 €/mok.
      Tekstas iš Kultūros paso paraiškos; teikiama nuo 2027-01, atrinkus paraišką
- [x] **Domenas** — `www.feelharmonic.lt`; šakninis persiunčia į www. Paštas
      `elena.daunyte@feelharmonic.lt` įrašytas puslapyje, poraštėje ir vizitinėje
- [x] **Segmentai** — pridėti dvarai/erdvės ir įmonės/agentūros
- [x] **Enforce HTTPS** — įjungta (patikrinta 2026-10-03)

Padaryta 2026-09-09:

- [x] **Puslapio papildymai** pagal `FeelHarmonic_Papildymai.docx`: alternatyvūs
      koncertai-performansai, interaktyvūs koncertai, terapiniai ir sąmoningumo
      renginiai, joga/meditacijos/retreat‘ai, kūrybinės dirbtuvės ir mokymai,
      atlikėjų paieška (ryšininkavimas), renginys nuo A iki Z, „Dive into
      personality“, atvira erdvė (studija), vestuvių ir įmonių segmentai
- [x] **Trys kalbos** — lietuvių `/`, anglų `/en/`, italų `/it/` su `hreflang`,
      kalbų perjungikliu ir atskiru `sitemap.xml` įrašu kiekvienai

## 4. Studija (atvira erdvė)

Skiltis paskelbta su žyma **„Rengiama“**, nes erdvės dar nėra. Kai paaiškės:

- [ ] Adresas ir kada atsidaro → pakeisti `studio.eyebrow` iš „Rengiama“ į
      „Mus rasite“ ir įrašyti adresą į kontaktus
- [ ] Nuotrauka `studija.jpg`
- [ ] Jei erdvės atsisakoma — visą `studio` bloką ir nuorodą meniu pašalinti
      (`build.py` funkcija `studio()` ir `nav` / `mobileNav` / `footer.pages` įrašai)

## 5. Kalbos

- [ ] **Vertimų peržiūra** — anglišką ir itališką tekstą verta duoti perskaityti
      gimtakalbiam prieš siunčiant nuorodą užsienio partneriams. Ypač: programų
      pavadinimai ir DUK.
- [ ] **Kultūros pasas** angliškai ir itališkai paaiškintas kaip valstybinė
      mokyklų programa. Jei atsiras oficialus angliškas pavadinimas, suvienodinti.
- [ ] Pridedant naują tekstą **visada** pildyti visus tris failus — kitaip
      generatorius nulūš ir puslapis neatsinaujins.

## 6. Forma

- [ ] **Formspree adresas** → `assets/js/main.js`, `CONFIG.formEndpoint`.
      Kol neįrašytas, mygtukas atidaro el. pašto programą su paruoštu laišku.
      Formos pranešimai visomis kalbomis jau paruošti (`js` blokas turinio failuose).

## 7. Kai atsiras

- [ ] **Vaizdo įrašai** — koncerto ištrauka ir edukacinis užsiėmimas.
      Įrašo kodą pakanka įrašyti į `"videos": []` turinio failuose (žr. ADMIN.md, 4 sk.).
- [ ] **Trys atsiliepimai** su vardu, pareigomis ir įstaiga.
      Prašyti raštu iškart po renginio, kartu prašant leidimo paskelbti.
      Nesugalvotų atsiliepimų nerašyti — kultūros įstaigose žmonės pažįsta vieni kitus.
- [ ] **Kultūros paso žymė** — patvirtinus edukaciją, pakeisti „Rengiama Kultūros paso atrankai“
      į tikslų statusą ir pridėti nuorodą į katalogą.

## Terminai

- **Rugsėjis** — nuotraukos, veiklos nr., aparatūros skaičius. Kainos ir nuoroda jau
  tvarkoje, tad kalėdinius pasiūlymus kultūros centrams galima siųsti nelaukiant nuotraukų —
  laiške svarbiausia kaina ir laisvos datos, o ne galerija.
- **Spalis** — Kultūros paso kvietimas. Iki jo puslapis turi būti gyvas: vertinant
  tikrinama, ar teikėjas realus. Tikslias datas pasitikrinti kulturospasas.lt.
