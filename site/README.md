# Silcock Law — production site (Astro + Tailwind)

Ported from the locked mockup (`../mockups/index.html`, Jo's picks of 21–23 Jun 2026).
Pages: Home, About, Services, Contact. Logo = `public/logo/silcocklaw-logo.svg` (outlined, see `../assets/logo/`).

    npm install
    npm run dev       # http://localhost:4321
    npm run build     # static output in dist/

Before go-live:
- Remove the `noindex` meta in `src/layouts/Base.astro`.
- Set `PUBLIC_FORM_ENDPOINT` on the host (Formspree / Netlify / Mailgun relay). Without it the
  contact form validates, then asks the visitor to email or phone.
- Host is still undecided (Netlify or Cloudflare Pages); both build with `npm run build` → `dist/`.
