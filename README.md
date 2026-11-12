# SmartUtilBox

免費的個人理財試算工具網站（房貸、複利、定期定額、買房 vs 租房、通膨、FIRE、投資組合、匯率），以 Astro + Tailwind CSS 建置，部署於 Vercel。

## 開發

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # 輸出到 ./dist
npx astro check  # 型別檢查
```

## 結構

- `src/pages/` — 各頁面；每個工具頁的計算邏輯在頁面底部的 `<script is:inline>`
- `src/components/guides/` — 各工具頁下方的說明文字與常見問題（含 FAQ 結構化資料）
- `src/content/blog/` — 理財專欄文章（Markdown）；英文版以 `en-` 開頭，會自動與中文版互相連結
- `src/layouts/BaseLayout.astro` — 共用版型、SEO meta、AdSense、全站中英文字串
- `public/ads.txt`、`public/robots.txt` — AdSense 與搜尋引擎設定
- `vercel.json` — 舊網址的 301 轉址

## 網域

canonical、Open Graph 與 sitemap 使用 `astro.config.mjs` 的 `SITE_URL`（預設 `https://smartutilbox.com`）。
如果正式網域不同，請修改該值或在 Vercel 設定環境變數 `SITE_URL`，並同步更新 `public/robots.txt` 的 Sitemap 網址。
