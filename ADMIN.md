# Kaip pačiai keisti puslapį

Ši instrukcija skirta Elenai. Programuoti nereikia — viską galima padaryti
naršyklėje, GitHub svetainėje. Kompiuteryje nieko diegti nereikia.

Puslapis: **https://www.feelharmonic.lt/**
Kodas: **https://github.com/daunyteelena-byte/feelharmonic**

---

## Pagrindinė taisyklė

Puslapis yra **trimis kalbomis**: lietuvių, anglų ir italų. Kiekvienos kalbos
tekstas guli savo faile aplanke **`turinys`**:

| Failas | Kalba | Adresas |
|---|---|---|
| `turinys/lt.json` | lietuvių | www.feelharmonic.lt |
| `turinys/en.json` | anglų | www.feelharmonic.lt/en/ |
| `turinys/it.json` | italų | www.feelharmonic.lt/it/ |

Pakeitus vieną iš jų, GitHub pats perdaro puslapį ir internete pakeitimas
matomas **per maždaug dvi minutes**.

> **Svarbu:** failų `index.html`, `en/index.html` ir `it/index.html` redaguoti
> **nereikia ir negalima** — jie perrašomi automatiškai, ir bet koks ranka
> įrašytas pakeitimas dings. Visas tekstas keičiamas tik `turinys` aplanke.

Kiekvienas išsaugojimas įsimenamas. Jei kas nors sugriūva, viską galima
atsukti atgal per 30 sekundžių — kaip tai padaryti, parašyta pačiame gale.

---

## 1. Pakeisti tekstą arba kainą

1. Atsidaryk https://github.com/daunyteelena-byte/feelharmonic
2. Spustelėk aplanką **`turinys`**, tada failą **`lt.json`**
   (jei keiti anglišką puslapį — `en.json`, itališką — `it.json`)
3. Viršuje dešinėje spustelėk **pieštuko ikonėlę** (Edit this file)
4. Klaviatūra spausk `Ctrl + F` ir įrašyk žodį, kurį nori pakeisti
   (pavyzdžiui `Kalėdų vakaras`) — naršyklė nuves į tą vietą
5. Pakeisk tekstą. **Keisk tik žodžius tarp kabučių.**
   Pavyzdžiui čia keisti galima tik `55 min`:

   ```
   { "k": "Trukmė", "v": "55 min" }
   ```

   Kabučių, kablelių ir laužtinių skliaustų **liesti negalima** — jie laiko
   failą kartu.

6. Nuslink į apačią, spustelėk žalią **Commit changes**
7. Atsidariusiame lange dar kartą **Commit changes**

Po poros minučių atnaujink puslapį naršyklėje — pakeitimas jau ten.

**Jei pakeitimas neatsirado:** greičiausiai netyčia ištrinta kabutė arba
kablelis. Eik į https://github.com/daunyteelena-byte/feelharmonic/actions —
jei viršutinėje eilutėje raudonas kryželis, paskutinis pakeitimas nepraėjo.
Gyvas puslapis tuo metu lieka toks, koks buvo, tad nieko baisaus: atsuk
pakeitimą atgal (žr. 6 skyrių) ir pabandyk iš naujo.

> Pakeitus kainą ar duomenis viename faile, tą patį reikia padaryti ir kituose
> dviejuose — kitaip lietuviškas ir angliškas puslapiai rodys skirtingas kainas.

### Kur ieškoti dažniausiai keičiamų dalykų

| Ką keisti | Ieškok žodžio faile `turinys/lt.json` |
|---|---|
| Programos kainos | `Kaina nuo` |
| Edukacijos duomenys | `Kaip skamba emocija` |
| Individualios veiklos nr. | `Individuali veikla nr.` |
| Tekstas apie save | `Elena Daunytė — violončelininkė` |
| Klausimai ir atsakymai (DUK) | `Dažniausiai klausiama` |

Telefonas ir el. paštas visose trijose kalbose vienodi, todėl jie įrašyti ne
turinio failuose, o `build.py` ir `assets/js/main.js` — juos keičiant verta
paprašyti pagalbos.

Punktyriniu rėmeliu apvestos vietos puslapyje — tai dar neužpildyti duomenys.
Turinio faile jos atrodo taip: `<span class=\"fill\">nurodyti skaičių</span>`.
Užpildant reikia ištrinti visą tą gabalą ir palikti tik skaičių, pavyzdžiui
`120`. Dėmesio: kabutės viduje rašomos su brūkšneliu (`\"`) — taip ir palik.

---

## 2. Įkelti nuotrauką

Nuotraukos turi turėti **tikslų pavadinimą** — puslapis jų ieško pagal jį.

| Failo pavadinimas | Kur atsiras |
|---|---|
| `elena.jpg` | Pirmame ekrane, prie pavadinimo |
| `apie.jpg` | Skiltyje „Apie“ |
| `galerija-1.jpg` … `galerija-6.jpg` | Galerijoje |
| `paslauga-koncertai.jpg` | Kortelė „Koncertai ir performansai“ |
| `paslauga-edukacijos.jpg` | Kortelė „Edukacija ir mokymai“ |
| `paslauga-renginiai.jpg` | Kortelė „Renginiai nuo A iki Z“ |
| `paslauga-terapija.jpg` | Kortelė „Terapiniai ir sąmoningumo renginiai“ |
| `paslauga-interaktyvu.jpg` | Kortelė „Interaktyvūs koncertai“ |
| `paslauga-pokalbiai.jpg` | Kortelė „Dive into personality“ |
| `studija.jpg` | Skiltis „Atvira erdvė — studija“ |
| `og.jpg` | Matoma dalinantis nuoroda (1200 × 630 px) |

Nuotraukos bendros visoms trims kalboms — įkelti reikia tik kartą.

Kaip įkelti:

1. Eik į https://github.com/daunyteelena-byte/feelharmonic/tree/main/assets/img
2. Spustelėk **Add file → Upload files**
3. Nutempk nuotrauką (pavadinimas turi sutapti su lentele aukščiau)
4. Apačioje **Commit changes**

Nuotrauka atsiras pati, kode keisti nieko nereikia.

**Svarbu:** nuotrauka turi būti ne mažesnė kaip 1200 px pločio, bet ir ne
didesnė kaip ~500 KB, kitaip puslapis krausis lėtai. Suspausti nemokamai
galima čia: https://squoosh.app

Kol nuotraukų nėra, jų vietose rodomas firminis ženklas, o galerijos skiltis
tiesiog nerodoma. Puslapis nesugriūva.

---

## 3. Pridėti atsiliepimą

Faile `turinys/lt.json` susirask `Ką sako užsakovai`. Kiek žemiau yra dvi
eilutės, prasidedančios `{ "t": "Atsiliepimas`. Vietoj jų įrašyk tikrą
atsiliepimą — į `"t"` vardą ir įstaigą, į `"d"` patį tekstą:

```json
{ "t": "Rasa Petraitienė, Trakų kultūros rūmai", "d": "Programa buvo paruošta laiku, o salė po koncerto dar ilgai neišsiskirstė." }
```

Tą patį pakartok `en.json` ir `it.json` — atsiliepimą galima palikti originalo
kalba, tik vardą ir įstaigą užrašyk taip pat.

Visada prašyk leidimo skelbti. Nesugalvotų atsiliepimų nerašyti —
kultūros įstaigose žmonės pažįsta vieni kitus.

---

## 4. Įdėti vaizdo įrašą

Turinio faile susirask eilutę `"videos": [],` (ji yra skiltyje „Įrašai“).
Vietoj tuščių skliaustų įrašyk savo YouTube įrašų kodus. Kodas — tai raidės,
matomos adreso juostoje po `watch?v=`:

```json
"videos": [
  { "id": "dQw4w9WgXcQ", "title": "Koncerto ištrauka" },
  { "id": "abcdEfGhIjK", "title": "Edukacinis užsiėmimas" }
],
```

Kai tik čia atsiranda bent vienas įrašas, tuščios vietos su aprašymais dingsta
ir jų vietoje atsiranda tikri grotuvai. Tą patį pakartok visose trijose kalbose
(įrašai tie patys, tik pavadinimą išversk).

---

## 5. Kad užklausos ateitų į paštą

Dabar mygtukas „Siųsti užklausą“ atidaro el. pašto programą su paruoštu
laišku. Kad laiškai ateitų automatiškai:

1. Registruokis https://formspree.io (nemokamai — 50 užklausų per mėnesį)
2. Sukurk formą, nurodyk savo el. paštą
3. Nukopijuok gautą adresą (`https://formspree.io/f/xxxxxxxx`)
4. GitHub'e atidaryk `assets/js/main.js`, spausk pieštuką
5. Pirmose eilutėse pakeisk `PAKEISTI` į savo adresą:

```js
formEndpoint: "https://formspree.io/f/xxxxxxxx"
```

6. **Commit changes**

Būtinai išsiųsk sau testinę užklausą — Formspree pirmą kartą paprašo patvirtinti.

---

## 6. Jei kas nors sulūžo

Nieko baisaus neatsitiko. Kiekvienas išsaugojimas įsimintas, grąžinti galima taip:

1. Eik į https://github.com/daunyteelena-byte/feelharmonic/commits/main
2. Rask paskutinį savo pakeitimą (viršuje)
3. Spustelėk jį, tada viršuje dešinėje **⋯ → Revert**
4. **Commit changes**

Puslapis grįš į būseną prieš tą pakeitimą.

---

## Ko geriau neliesti

- Failų **`index.html`, `en/index.html`, `it/index.html` ir `sitemap.xml`** —
  jie sukuriami automatiškai iš `turinys` aplanko, tad bet koks ranka įrašytas
  pakeitimas dings per kitą atnaujinimą.
- Failo **`build.py`** — tai variklis, kuris tuos puslapius sudeda.
- Failo `assets/css/style.css` — ten dizainas. Spalvas keisti galima
  pačiame viršuje (`--teal`, `--gold`), bet visa kita geriau palikti.
- Failo `assets/js/main.js` — išskyrus tą vieną Formspree eilutę.
- Aplanko `.github` — ten instrukcija, kaip puslapį perdaryti.

Turinio failuose (`turinys/*.json`) laisvai keičiamas **tik tekstas tarp
kabučių**. Pavadinimų kairėje nuo dvitaškio (`"h2"`, `"lede"`, `"specs"`)
keisti nereikia.

Jei reikia keisti dizainą, pridėti naują skiltį ar dar vieną kalbą — tam reikia
žmogaus, mokančio HTML. Techninis aprašymas jam paruoštas faile `HANDOVER.md`.

---

## Kas dar neužpildyta

Žr. [TODO.md](TODO.md) — ten surašyta, ko trūksta ir kokia eilės tvarka.
