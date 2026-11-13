// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// Production URL. Used for canonical links, Open Graph URLs and sitemap.xml.
// Override at build time with SITE_URL if the site lives on another domain.
const SITE_URL = process.env.SITE_URL || 'https://www.smartutilbox.com';

// https://astro.build/config
export default defineConfig({
  site: SITE_URL,
  trailingSlash: 'ignore',
  integrations: [
    sitemap({
      filter: (page) => !/\/(privacy|404)\/?$/.test(new URL(page).pathname),
    }),
  ],
  vite: {
    plugins: [tailwindcss()]
  }
});
