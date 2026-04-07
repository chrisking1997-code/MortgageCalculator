import re

with open('portfolio-roi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Chart.js CDN
if 'chart.js' not in html.lower():
    html = html.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n</head>')

# Add Chart canvas to the Results Column (before Alerts Container)
canvas_html = """
                            <!-- Chart Container -->
                            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                                <h3 class="text-lg font-bold text-gray-800 mb-4 text-center" data-i18n="port-chart-title">資產分佈圖</h3>
                                <div class="relative h-64 w-full">
                                    <canvas id="portfolioChart"></canvas>
                                </div>
                            </div>
"""
if 'portfolioChart' not in html:
    html = html.replace('<!-- Alerts Container -->', canvas_html + '\n                            <!-- Alerts Container -->')

# Add Concentrated Alert Box to the Alerts Container
alert_html = """
                                <!-- Concentration Alert -->
                                <div id="concentrationAlert" class="hidden bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded-r-lg">
                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <svg class="h-5 w-5 text-yellow-500" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        </div>
                                        <div class="ml-3">
                                            <p class="text-sm text-yellow-800 font-bold" data-i18n="port-alert-conc-title">過度集中警示</p>
                                            <p class="text-xs text-yellow-700 mt-1" id="concentrationAlertDesc">⚠️ 偵測到資產過度集中於單一標的，缺乏多樣性防禦。</p>
                                        </div>
                                    </div>
                                </div>
"""
if 'concentrationAlert' not in html:
    html = html.replace('<!-- Success Message -->', alert_html + '\n                                <!-- Success Message -->')

with open('portfolio-roi/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML layout updated.")
