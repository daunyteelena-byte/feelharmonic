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
