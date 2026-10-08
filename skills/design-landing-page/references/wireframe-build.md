# Building the landing-page wireframe

Read at step 8, only if the member accepted the wireframe. Build one self-contained HTML file by adapting [REFERENCE-WIREFRAME.html](../REFERENCE-WIREFRAME.html) from this skill's folder.

1. **Keep the structural skeleton exactly** — sticky page header, three-column layout (sidebar / canvas / annotation panel), browser-chrome frame with traffic lights and URL bar, scroll-based annotation rendering via IntersectionObserver. Same lo-fi greyscale palette as the onboarding wireframe — do not pull color from `docs/DESIGN.md`. The wireframe's job is *flow critique not visual evaluation*; polish would mask copy and structure problems.

2. **Replace the sidebar list** with the 11 section names from the markdown spec. The IDs and `data-section` attributes must match the section keys used in the annotations object.

3. **Replace each `<section class="page-section">`** with a wireframe of the page's actual section, using the wireframe primitives:
   - `.wire-nav` + `.wire-logo` + `.wire-nav-links` + `.wire-cta-small` for the header
   - `.wire-hero` + `.wire-headline-xl` + `.wire-sub-lg` + `.wire-cta-lg` + `.wire-hero-visual` + `.wire-hero-testimonial` for the hero
   - `.wire-eyebrow` + `.wire-logos` + `.wire-logo-box` for the social proof bar
   - `.wire-eyebrow` + `.wire-h2` + `.wire-section-sub` + `.wire-hero-visual` for the problem
   - `.wire-steps` + `.wire-step` + `.wire-step-num` + `.wire-step-title` + `.wire-step-desc` for the solution
   - `.wire-features` + `.wire-feature` + `.wire-feature-icon` + `.wire-feature-title` + `.wire-feature-desc` for the features
   - `.wire-testimonials` + `.wire-testimonial-card` + `.wire-testimonial-quote` + `.wire-testimonial-author` + `.wire-rating` for deep social proof
   - `.wire-pricing` + `.wire-pricing-tier` (with `.popular` modifier) + `.wire-popular-badge` + `.wire-pricing-name` + `.wire-pricing-amount` + `.wire-pricing-period` + `.wire-pricing-features` + `.wire-pricing-cta` for pricing
   - `.wire-faq` + `.wire-faq-item` + `.wire-faq-q` + `.wire-faq-a` for FAQ
   - `.wire-final-cta` + `.wire-h2` + `.wire-sub-lg` + `.wire-cta-lg` + `.wire-secondary-link` for the final CTA
   - `.wire-footer` + `.wire-footer-col` + `.wire-footer-bottom` + `.wire-compliance-badges` for the footer

   Extend with new primitives only if a section genuinely needs one. **Populate every primitive with the actual copy from the markdown spec** — same headlines, same CTAs, same testimonial quotes, same FAQ questions and answers. If the wireframe and the markdown drift, the wireframe is stale.

4. **Populate the `annotations` JS object** with one entry per section, each containing `title`, `goal`, `proves`, `risk`, `ref`. These read directly from the Goal / What this proves / Drop-off risk / Reference fields of the markdown spec, so the wireframe and the doc stay in sync. The annotation appears in the right panel automatically as the user scrolls (IntersectionObserver with `rootMargin: "-30% 0px -55% 0px"` so the active section is whichever is most prominent in the viewport).

5. **Keep the styling lo-fi.** Greyscale palette, dashed wireframe boxes for placeholder visuals, system fonts, no real imagery. Do not import external fonts. Do not pull color from `docs/DESIGN.md`. The wireframe is intentionally neutral so structure and copy problems surface clearly.

6. **Single file, no dependencies.** No external CSS, no CDN scripts, no images. The member double-clicks the file and it opens in any browser.

Test the file mentally before writing — every sidebar item must scroll to a real section; the IntersectionObserver must trigger annotation updates as the user scrolls; the browser chrome must stay sticky at the top of the canvas frame.
