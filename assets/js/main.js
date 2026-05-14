(function () {
  "use strict";

  /**
   * Full-page loader: hide after window load (images, fonts, etc.)
   */
  function hidePageLoader() {
    const el = document.getElementById("ss-page-loader");
    if (!el) return;
    el.classList.add("ss-page-loader--hide");
    document.documentElement.classList.remove("ss-page-loading");
    window.setTimeout(() => {
      el.remove();
    }, 500);
  }

  if (document.readyState === "complete") {
    hidePageLoader();
  } else {
    window.addEventListener("load", hidePageLoader);
  }
})();

(function () {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader || (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top'))) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    const body = document.querySelector('body');
    const wasMobileNavActive = body.classList.contains('mobile-nav-active');
    body.classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
    if (wasMobileNavActive) {
      const fd = document.querySelector('.ss-features-dropdown');
      const tr = document.querySelector('.ss-nav-features-trigger');
      if (fd) fd.classList.remove('ss-mega-open');
      if (tr) tr.setAttribute('aria-expanded', 'false');
    }
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  if (scrollTop) {
    scrollTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox (optional — script may be omitted on some pages)
   */
  if (typeof GLightbox !== 'undefined') {
    GLightbox({
      selector: '.glightbox'
    });
  }

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate Pure Counter (optional — script may be omitted on some pages)
   */
  if (typeof PureCounter !== 'undefined') {
    new PureCounter();
  }

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function (e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu > ul > li > a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  /**
   * Features mega menu: position under header; open/close on click only
   */
  function updateFeaturesMegaPanelTop() {
    const header = document.querySelector('#header');
    if (!header) return;
    const bottom = header.getBoundingClientRect().bottom;
    document.documentElement.style.setProperty('--ss-mega-top', `${bottom}px`);
  }

  window.addEventListener('scroll', updateFeaturesMegaPanelTop, { passive: true });
  window.addEventListener('resize', updateFeaturesMegaPanelTop);
  window.addEventListener('load', updateFeaturesMegaPanelTop);

  const featuresDropdown = document.querySelector('.ss-features-dropdown');
  const featuresTrigger = document.querySelector('.ss-nav-features-trigger');
  const featuresMegaPanel = document.getElementById('features-mega-panel');

  function closeFeaturesMega() {
    if (!featuresDropdown || !featuresTrigger) return;
    featuresDropdown.classList.remove('ss-mega-open');
    featuresTrigger.setAttribute('aria-expanded', 'false');
  }

  function openFeaturesMega() {
    if (!featuresDropdown || !featuresTrigger) return;
    featuresDropdown.classList.add('ss-mega-open');
    featuresTrigger.setAttribute('aria-expanded', 'true');
    updateFeaturesMegaPanelTop();
  }

  if (featuresDropdown && featuresTrigger && featuresMegaPanel) {
    featuresTrigger.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (featuresDropdown.classList.contains('ss-mega-open')) {
        closeFeaturesMega();
      } else {
        openFeaturesMega();
      }
    });

    document.addEventListener('click', function (e) {
      if (!featuresDropdown.classList.contains('ss-mega-open')) return;
      if (!featuresDropdown.contains(e.target)) {
        closeFeaturesMega();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        closeFeaturesMega();
      }
    });

    featuresMegaPanel.querySelectorAll('.ss-mega-item').forEach(function (link) {
      link.addEventListener('click', function () {
        closeFeaturesMega();
      });
    });
  }

})();