/* FeelHarmonic — puslapio logika
   ------------------------------------------------------------------
   VIENINTELĖ VIETA, KURIĄ REIKIA REDAGUOTI: CONFIG blokas žemiau.
   ------------------------------------------------------------------ */

var CONFIG = {
  // El. pašto adresas, kuriuo su tavimi susisieks užsakovai.
  email: "info@feelharmonic.lt",

  // Formspree adresas. Registruokis formspree.io, sukurk formą ir
  // įklijuok gautą nuorodą (atrodo taip: https://formspree.io/f/abcdwxyz).
  // Kol čia lieka "PAKEISTI", forma atidarys el. pašto programą su
  // paruoštu laišku — puslapis veikia, tik be automatinio siuntimo.
  formEndpoint: "PAKEISTI"
};

(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- metai poraštėje ---------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- el. pašto adresas iš CONFIG ---------- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-email]"), function (el) {
    el.textContent = CONFIG.email;
    if (el.tagName === "A") el.setAttribute("href", "mailto:" + CONFIG.email);
  });

  /* ---------- mobilusis meniu ---------- */
  var burger = document.getElementById("burger");
  var mobileNav = document.getElementById("mobile-nav");

  if (burger && mobileNav) {
    var closeMenu = function () {
      mobileNav.classList.remove("is-open");
      burger.setAttribute("aria-expanded", "false");
      document.body.classList.remove("no-scroll");
    };

    burger.addEventListener("click", function () {
      var open = mobileNav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("no-scroll", open);
    });

    Array.prototype.forEach.call(mobileNav.querySelectorAll("a"), function (a) {
      a.addEventListener("click", closeMenu);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeMenu();
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth >= 980) closeMenu();
    });
  }

  /* ---------- kalbų sąrašas antraštėje: užsidaro spustelėjus šalia ar Escape ---------- */
  var langMenu = document.querySelector(".lang-menu");
  if (langMenu) {
    document.addEventListener("click", function (e) {
      if (langMenu.open && !langMenu.contains(e.target)) langMenu.open = false;
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && langMenu.open) {
        langMenu.open = false;
        langMenu.querySelector("summary").focus();
      }
    });
  }

  /* ---------- vaizdo įrašo aprašymas: išblunkantis, „Skaityti daugiau“ ---------- */
  Array.prototype.forEach.call(document.querySelectorAll(".clip-toggle"), function (btn) {
    var text = btn.previousElementSibling;
    if (!text || !text.classList.contains("clip-text")) return;
    text.classList.add("is-collapsed");
    btn.hidden = false;
    btn.addEventListener("click", function () {
      var open = text.classList.toggle("is-collapsed") === false;
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? btn.getAttribute("data-less") : btn.getAttribute("data-more");
      var box = btn.closest(".clip") || text;
      if (!open) box.scrollIntoView({ block: "nearest" });
    });
    // paspaudus ant teksto — išskleidžiama arba suskleidžiama (bet ne žymint
    // tekstą kopijavimui ir ne paspaudus nuorodą)
    text.addEventListener("click", function (e) {
      if (e.target.closest("a")) return;
      var sel = window.getSelection && String(window.getSelection());
      if (sel && !text.classList.contains("is-collapsed")) return;
      btn.click();
    });
  });

  /* ---------- „Užsakyti renginį“: kontaktų formoje parenka temą ir žinutę ---------- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-book-option]"), function (a) {
    a.addEventListener("click", function () {
      var sel = document.getElementById("k");
      var msg = document.getElementById("z");
      var opt = a.getAttribute("data-book-option");
      if (sel) Array.prototype.forEach.call(sel.options, function (o) {
        if (o.text === opt) sel.value = o.value;
      });
      if (msg && !msg.value.trim()) msg.value = a.getAttribute("data-book-message") + "\n";
    });
  });

  /* ---------- nuotraukos: paspaudus atsidaro per visą ekraną su informacija ----------
     Visos nuotraukos su data-lb. Galerijos nuotraukos vartomos rodyklėmis,
     kitos (pirmas ekranas, kortelės, „Apie“, juosta) rodomos po vieną. */
  var lbLabels = document.querySelector("[data-lb-close]");
  var L = {
    close: lbLabels ? lbLabels.dataset.lbClose : "×",
    prev: lbLabels ? lbLabels.dataset.lbPrev : "‹",
    next: lbLabels ? lbLabels.dataset.lbNext : "›"
  };
  var figOf = function (im) { return im.closest("figure, .portrait, .about-photo") || im.parentNode; };
  var all = Array.prototype.filter.call(document.querySelectorAll("img[data-lb]"), function (im) {
    return figOf(im).offsetParent !== null;
  });
  if (all.length) {
    var lb = null, set = [], cur = 0, lastFocus = null;
    var titleOf = function (im) {
      var cap = figOf(im).querySelector("figcaption");
      if (cap && figOf(im).classList.contains("shot")) return cap.textContent.trim();
      if (cap && figOf(im).classList.contains("svc-banner")) return cap.textContent.trim();
      return im.alt;
    };
    var render = function () {
      var im = set[cur], big = lb.querySelector("img");
      big.src = im.currentSrc || im.src;
      big.alt = im.alt;
      var meta = im.getAttribute("data-lb-meta") || "";
      var count = set.length > 1 ? (cur + 1) + " / " + set.length : "";
      var cap = lb.querySelector("figcaption");
      cap.textContent = titleOf(im);
      if (meta) { var m = document.createElement("span"); m.className = "lb-meta"; m.textContent = meta; cap.appendChild(m); }
      if (count) { var s = document.createElement("small"); s.textContent = count; cap.appendChild(s); }
      lb.classList.toggle("is-single", set.length < 2);
    };
    var close = function () {
      if (!lb) return;
      lb.classList.remove("is-open");
      document.body.classList.remove("no-scroll");
      var el = lb; lb = null;
      setTimeout(function () { el.remove(); }, 250);
      if (lastFocus) lastFocus.focus();
    };
    var go = function (d) { if (set.length < 2) return; cur = (cur + d + set.length) % set.length; render(); };
    var open = function (im) {
      var g = im.closest(".gallery");
      set = g ? all.filter(function (x) {
        return x.closest(".gallery") === g && x.complete && x.naturalWidth > 0 && x.isConnected;
      }) : [im];
      cur = set.indexOf(im); lastFocus = document.activeElement;
      lb = document.createElement("div");
      lb.className = "lightbox";
      lb.setAttribute("role", "dialog");
      lb.setAttribute("aria-modal", "true");
      lb.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure>' +
        '<button class="lb-close" type="button" aria-label="' + L.close + '">&times;</button>' +
        '<button class="lb-prev" type="button" aria-label="' + L.prev + '">&#8249;</button>' +
        '<button class="lb-next" type="button" aria-label="' + L.next + '">&#8250;</button>';
      document.body.appendChild(lb);
      document.body.classList.add("no-scroll");
      render();
      requestAnimationFrame(function () { lb.classList.add("is-open"); });
      lb.querySelector(".lb-close").focus();
      lb.addEventListener("click", function (e) {
        if (e.target.closest(".lb-close")) close();
        else if (e.target.closest(".lb-prev")) go(-1);
        else if (e.target.closest(".lb-next")) go(1);
        else if (!e.target.closest("img")) close();
      });
    };
    all.forEach(function (im) {
      var f = figOf(im);
      // tik įsikėlusios nuotraukos (be nuotraukos lieka ženklas — jo nedidiname)
      var ready = function () { return im.complete && im.naturalWidth > 0 && im.isConnected; };
      var mark = function () { if (ready()) f.classList.add("lb-zoom"); };
      mark(); im.addEventListener("load", mark);
      f.setAttribute("tabindex", "0");
      f.setAttribute("aria-label", im.alt);
      f.addEventListener("click", function () { if (ready()) open(im); });
      f.addEventListener("keydown", function (e) {
        if ((e.key === "Enter" || e.key === " ") && ready()) { e.preventDefault(); open(im); }
      });
    });
    document.addEventListener("keydown", function (e) {
      if (!lb) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") go(-1);
      else if (e.key === "ArrowRight") go(1);
    });
    // braukimas telefone
    var sx = null;
    document.addEventListener("touchstart", function (e) { if (lb) sx = e.touches[0].clientX; }, { passive: true });
    document.addEventListener("touchend", function (e) {
      if (!lb || sx === null) return;
      var dx = e.changedTouches[0].clientX - sx; sx = null;
      if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
    });
  }

  /* ---------- navigacijos būsena slenkant ---------- */
  var nav = document.getElementById("nav");
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle("is-stuck", window.scrollY > 12);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- aktyvi nuoroda meniu ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll("nav.main a[href^='#']"));
  if (navLinks.length && "IntersectionObserver" in window) {
    var sections = navLinks
      .map(function (a) { return document.querySelector(a.getAttribute("href")); })
      .filter(Boolean);

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (a) {
          a.classList.toggle("is-active", a.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });

    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- turinio pasirodymas slenkant ---------- */
  var revealables = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        obs.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.06 });

    Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
  }

  /* ---------- trūkstamos nuotraukos ----------
     Nesant failo, vietoj tuščio rėmelio rodoma tamsi plokštuma su
     bangos ženklu. Jei nėra nė vienos galerijos nuotraukos, visa
     galerijos skiltis paslepiama — taip puslapis atrodo baigtas. */

  function tidyPhotos() {
    var gallery = document.querySelector(".gallery");
    if (gallery && !gallery.querySelector("img")) {
      var section = document.getElementById("galerija");
      if (section) section.hidden = true;
      Array.prototype.forEach.call(
        document.querySelectorAll("a[href='#galerija']"),
        function (a) { a.hidden = true; }
      );
    }

    /* Ieškoma tik „Apie“ bloko viduje: .about-photo klasę naudoja ir studijos
       skiltis, o ji puslapyje yra anksčiau, tad document.querySelector rastų ją. */
    var about = document.querySelector(".about");
    var aboutPhoto = about && about.querySelector(".about-photo");
    if (about && aboutPhoto && !aboutPhoto.querySelector("img")) {
      about.classList.add("no-photo");
    }
  }

  var pending = document.querySelectorAll("img[data-optional]").length;

  Array.prototype.forEach.call(document.querySelectorAll("img[data-optional]"), function (img) {
    var settle = function (failed) {
      if (failed) {
        var holder = img.closest("[data-photo]");
        if (holder) holder.classList.add("is-empty");
        img.remove();
      }
      pending -= 1;
      if (pending <= 0) tidyPhotos();
    };

    if (img.complete) {
      settle(img.naturalWidth === 0);
      return;
    }
    img.addEventListener("error", function () { settle(true); });
    img.addEventListener("load", function () { settle(false); });
  });

  // atsarginis variantas, jei kuri nors nuotrauka niekada neatsako
  setTimeout(tidyPhotos, 2500);

  /* ---------- užklausos forma ---------- */
  var form = document.getElementById("uzklausa");
  if (!form) return;

  var msg = document.getElementById("form-msg");
  var btn = form.querySelector("button[type=submit]");

  /* Formos tekstai ateina iš paties puslapio (data-* atributai), todėl
     lietuviškas, angliškas ir itališkas puslapiai naudoja tą patį failą.
     Tekstus keisti turinys/<kalba>.json bloke "js", po to paleisti build.py. */
  function t(key) {
    return form.getAttribute("data-" + key) || "";
  }

  function say(text, state) {
    if (!msg) return;
    msg.textContent = text;
    msg.setAttribute("data-state", state || "");
  }

  function mailtoFallback(data) {
    var body = [
      t("mail-name") + ": " + (data.get("vardas") || ""),
      t("mail-org") + ": " + (data.get("istaiga") || ""),
      t("mail-email") + ": " + (data.get("pastas") || ""),
      t("mail-phone") + ": " + (data.get("telefonas") || ""),
      t("mail-type") + ": " + (data.get("tipas") || ""),
      t("mail-date") + ": " + (data.get("data") || ""),
      "",
      data.get("zinute") || ""
    ].join("\n");

    var subject = t("mail-subject") + " " + (data.get("tipas") || t("mail-fallback"));

    window.location.href =
      "mailto:" + CONFIG.email +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(body);

    say(t("msg-mailto") + " " + CONFIG.email, "");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var honeypot = form.querySelector("[name=_gotcha]");
    if (honeypot && honeypot.value) return;

    if (!form.checkValidity()) {
      say(t("msg-invalid"), "err");
      form.reportValidity();
      return;
    }

    var data = new FormData(form);

    if (CONFIG.formEndpoint.indexOf("formspree.io") === -1) {
      mailtoFallback(data);
      return;
    }

    btn.disabled = true;
    say(t("msg-sending"), "");

    fetch(CONFIG.formEndpoint, {
      method: "POST",
      body: data,
      headers: { Accept: "application/json" }
    })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        form.reset();
        say(t("msg-ok"), "ok");
      })
      .catch(function () {
        say(t("msg-fail") + " " + CONFIG.email, "err");
      })
      .then(function () {
        btn.disabled = false;
      });
  });
})();
