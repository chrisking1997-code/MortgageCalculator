import { test, expect } from '@playwright/test';

test('Verify global dark theme styling on multiple pages', async ({ page }) => {
  // Test Index Page
  await page.goto('http://localhost:8080/');

  // Verify body is dark
  const bodyBg = await page.evaluate(() => window.getComputedStyle(document.body).backgroundColor);
  expect(bodyBg).toBe('rgb(9, 9, 11)'); // zinc-950

  // Verify font family includes Playfair Display or Noto Serif TC
  const h1Font = await page.evaluate(() => window.getComputedStyle(document.querySelector('h1')).fontFamily);
  expect(h1Font).toMatch(/Playfair Display|Noto Serif TC/);

  // Verify Sidebar background
  const sidebarBg = await page.evaluate(() => window.getComputedStyle(document.querySelector('aside')).backgroundColor);
  expect(sidebarBg).toBe('rgb(9, 9, 11)'); // zinc-950

  // Test Portfolio Page
  await page.goto('http://localhost:8080/portfolio-roi');

  // Verify body is dark
  const portBodyBg = await page.evaluate(() => window.getComputedStyle(document.body).backgroundColor);
  expect(portBodyBg).toBe('rgb(9, 9, 11)'); // zinc-950

  // Verify active sidebar link styling
  const activeLinkBorder = await page.evaluate(() => window.getComputedStyle(document.querySelector('a[href="/portfolio-roi"]')).borderLeftColor);
  expect(activeLinkBorder).toBe('rgb(217, 119, 6)'); // amber-600

  console.log('Global dark theme verification passed.');
});
