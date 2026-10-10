// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// Set `site` to the real domain at go-live (used for canonical URLs / sitemap).
export default defineConfig({
  site: 'https://www.silcocklaw.co.nz',
  vite: { plugins: [tailwindcss()] },
});
