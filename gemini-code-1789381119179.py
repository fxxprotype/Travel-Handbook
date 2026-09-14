# Re-generate index.html file to ensure it's fresh and complete
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>比荷希欧洲之旅旅行手册 (2026.09.25 - 10.08)</title>
  <style>
    :root {
      --bg-color: #f8f9fa;
      --card-bg: #ffffff;
      --text-main: #1f2937;
      --text-muted: #6b7280;
      --accent: #2563eb;
      --accent-light: #eff6ff;
      --border: #e5e7eb;
      --warning-bg: #fef2f2;
      --warning-border: #fca5a5;
      --warning-text: #991b1b;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
      --map-bg: #f1f5f9;
    }

    [data-theme="dark"] {
      --bg-color: #111827;
      --card-bg: #1f2937;
      --text-main: #f9fafb;
      --text-muted: #9ca3af;
      --accent: #60a5fa;
      --accent-light: #1e3a8a;
      --border: #374151;
      --warning-bg: #450a0a;
      --warning-border: #991b1b;
      --warning-text: #fca5a5;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --map-bg: #1e293b;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.5;
      padding-bottom: 40px;
      transition: background-color 0.3s, color 0.3s;
    }

    .container {
      max-width: 680px;
      margin: 0 auto;
      padding: 16px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }

    h1 { font-size: 1.3rem; font-weight: 700; }

    .theme-toggle {
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 0.85rem;
      cursor: pointer;
    }

    .card {
      background: var(--card-bg);
      border-radius: 16px;
      padding: 18px;
      margin-bottom: 16px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* Focus Card */
    .focus-card {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #ffffff;
      border: none;
    }
    .focus-card .label { font-size: 0.85rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 0.5px; }
    .focus-card .event-title { font-size: 1.25rem; font-weight: 700; margin: 6px 0 12px 0; }
    .countdown {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      text-align: center;
    }
    .time-box {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(4px);
      padding: 8px 4px;
      border-radius: 10px;
    }
    .time-box .num { font-size: 1.4rem; font-weight: 800; line-height: 1.2; }
    .time-box .unit { font-size: 0.7rem; opacity: 0.8; }

    /* Map Card */
    .map-container {
      background: var(--map-bg);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
    }
    svg { width: 100%; height: auto; max-height: 260px; }

    /* Table & Bookings */
    .booking-item {
      padding: 10px 0;
      border-bottom: 1px dashed var(--border);
    }
    .booking-item:last-child { border-bottom: none; }
    .booking-header { display: flex; justify-content: space-between; font-weight: 600; font-size: 0.95rem; }
    .booking-sub { font-size: 0.85rem; color: var(--text-muted); margin-top: 4px; }
    .badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .badge-flight { background: #dbeafe; color: #1e40af; }
    .badge-hotel { background: #fef3c7; color: #92400e; }
    .badge-dining { background: #fce7f3; color: #9d174d; }

    /* Itinerary Timeline */
    .day-block {
      margin-bottom: 20px;
    }
    .day-header {
      background: var(--accent-light);
      color: var(--accent);
      padding: 8px 12px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .map-toggle-btn {
      font-size: 0.8rem;
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 2px 8px;
      border-radius: 6px;
      cursor: pointer;
    }
    .day-map {
      display: none;
      margin-bottom: 10px;
      background: var(--map-bg);
      border-radius: 8px;
      padding: 10px;
      font-size: 0.85rem;
    }
    .nav-btn {
      display: inline-block;
      margin-top: 6px;
      padding: 4px 10px;
      background: var(--accent);
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .timeline-item {
      display: flex;
      gap: 12px;
      padding: 8px 0;
      position: relative;
    }
    .time-col {
      width: 55px;
      font-weight: 600;
      font-size: 0.85rem;
      color: var(--accent);
      flex-shrink: 0;
    }
    .content-col {
      flex-grow: 1;
      font-size: 0.9rem;
    }
    .loc-link {
      color: var(--text-main);
      text-decoration: none;
      font-weight: 600;
    }
    .loc-link:hover { text-decoration: underline; color: var(--accent); }
    .tag-booking {
      background: #fee2e2;
      color: #991b1b;
      font-size: 0.7rem;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 600;
      margin-left: 4px;
    }

    /* Warning Box */
    .warning-box {
      background: var(--warning-bg);
      border: 1px solid var(--warning-border);
      color: var(--warning-text);
      padding: 12px;
      border-radius: 10px;
      font-size: 0.85rem;
      margin-bottom: 16px;
    }
    .warning-box ul { padding-left: 18px; margin-top: 6px; }

    /* Checklist */
    .todo-list { list-style: none; }
    .todo-item {
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
    }
    .todo-item:last-child { border-bottom: none; }
    .todo-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }

    /* Tips */
    .tip-item { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px; }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <h1>欧洲三国旅行手册 ✈️</h1>
      <button class="theme-toggle" onclick="toggleTheme()">🌓 主题模式</button>
    </header>

    <!-- 🚨 风险提示卡片 -->
    <div class="warning-box">
      <strong>⚠️ 关键行程风险提示（请特别注意）：</strong>
      <ul>
        <li><strong>重庆转机急迫</strong>：9月25日 MU5433 21:15抵渝，距 02:50 洲际航班仅 2.75 小时！非联程需重新提行李托运，建议迅速行动！</li>
        <li><strong>阿姆早班机</strong>：10月2日 05:40 航班，凌晨 03:30 前必须抵达 AMS 机场并完成还车！</li>
        <li><strong>布鲁塞尔同天转机</strong>：10月8日 09:30 抵BRU，12:00 飞上海，转机缓冲 2.5 小时，落地后请直奔海航柜台/登机口。</li>
      </ul>
    </div>

    <!-- 1. 顶部「此刻关注」卡片 -->
    <div class="card focus-card">
      <div class="label">Next Up / 下一个事件</div>
      <div class="event-title" id="next-event">加载行程事件中...</div>
      <div class="countdown">
        <div class="time-box"><div class="num" id="cd-days">00</div><div class="unit">天 DAYS</div></div>
        <div class="time-box"><div class="num" id="cd-hours">00</div><div class="unit">时 HRS</div></div>
        <div class="time-box"><div class="num" id="cd-mins">00</div><div class="unit">分 MINS</div></div>
        <div class="time-box"><div class="num" id="cd-secs">00</div><div class="unit">秒 SECS</div></div>
      </div>
    </div>

    <!-- 2. 行程总览地图 -->
    <div class="card">
      <div class="card-title">🗺️ 行程路线总览 (手绘感)</div>
      <div class="map-container">
        <svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg">
          <!-- 背景线条与标注 -->
          <style>
            .map-line { fill: none; stroke-width: 3; stroke-dasharray: 6; stroke-linecap: round; }
            .city-node { fill: var(--card-bg); stroke-width: 3; }
            .city-text { font-size: 11px; font-weight: bold; fill: var(--text-main); }
            .hotel-text { font-size: 9px; fill: var(--text-muted); }
          </style>
          
          <!-- 比荷段路线 (红色) -->
          <path class="map-line" stroke="#ef4444" d="M 120 180 L 160 120 L 220 100 L 260 50 L 280 110" />
          <!-- 希腊段路线 (蓝色) -->
          <path class="map-line" stroke="#3b82f6" d="M 440 100 L 400 200 L 480 230 L 520 180" />
          
          <!-- 城市节点 -->
          <!-- 布鲁塞尔 -->
          <circle cx="120" cy="180" r="7" class="city-node" stroke="#ef4444" />
          <text x="120" y="200" text-anchor="middle" class="city-text">布鲁塞尔 (BRU)</text>
          
          <!-- 安特卫普 -->
          <text x="160" y="105" text-anchor="middle" class="city-text">安特卫普</text>
          <circle cx="160" cy="120" r="6" class="city-node" stroke="#ef4444" />
          <text x="160" y="138" text-anchor="middle" class="hotel-text">宿 Botanical Sanctuary (3晚)</text>

          <!-- 鹿特丹 -->
          <circle cx="220" cy="100" r="6" class="city-node" stroke="#ef4444" />
          <text x="220" y="85" text-anchor="middle" class="city-text">鹿特丹</text>
          <text x="220" y="118" text-anchor="middle" class="hotel-text">宿 Marriott (1晚)</text>

          <!-- 阿姆斯特丹 -->
          <circle cx="260" cy="50" r="6" class="city-node" stroke="#ef4444" />
          <text x="260" y="35" text-anchor="middle" class="city-text">阿姆斯特丹</text>
          <text x="260" y="68" text-anchor="middle" class="hotel-text">宿 Mandarin Oriental (2晚)</text>

          <!-- 圣托里尼 -->
          <circle cx="440" cy="100" r="6" class="city-node" stroke="#3b82f6" />
          <text x="440" y="85" text-anchor="middle" class="city-text">圣托里尼</text>
          <text x="440" y="118" text-anchor="middle" class="hotel-text">宿 Mystique (2晚)</text>

          <!-- 迈泰奥拉 -->
          <circle cx="400" cy="200" r="6" class="city-node" stroke="#3b82f6" />
          <text x="400" y="190" text-anchor="end" class="city-text">迈泰奥拉</text>
          <text x="400" y="218" text-anchor="end" class="hotel-text">宿 Storyteller (1晚)</text>

          <!-- 德尔菲 -->
          <circle cx="480" cy="230" r="6" class="city-node" stroke="#3b82f6" />
          <text x="480" y="250" text-anchor="middle" class="city-text">德尔菲</text>
          <text x="480" y="265" text-anchor="middle" class="hotel-text">宿 Amalia (1晚)</text>

          <!-- 雅典 -->
          <circle cx="520" cy="180" r="6" class="city-node" stroke="#3b82f6" />
          <text x="545" y="184" text-anchor="start" class="city-text">雅典</text>
          <text x="545" y="198" text-anchor="start" class="hotel-text">宿 Electra Palace (2晚)</text>
        </svg>
      </div>
    </div>

    <!-- 3. 已确认大件（机票/酒店/餐馆） -->
    <div class="card">
      <div class="card-title">🎫 已确认预订 (隐去敏感号)</div>
      
      <div class="booking-item">
        <div class="booking-header">
          <span>航班 MU5433 / 海航 HU0469</span>
          <span class="badge badge-flight">机票</span>
        </div>
        <div class="booking-sub">09-25 20:50 上海PVG ✈️ 重庆CKG 00:05+1 | 09-26 02:50 CKG ✈️ 布鲁塞尔BRU 08:20</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Botanical Sanctuary Antwerp</span>
          <span class="badge badge-hotel">酒店 3晚</span>
        </div>
        <div class="booking-sub">09-26 入住 ~ 09-29 退房 | 安特卫普</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Rotterdam Marriott Hotel</span>
          <span class="badge badge-hotel">酒店 1晚</span>
        </div>
        <div class="booking-sub">09-29 入住 ~ 09-30 退房 | 鹿特丹</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Mandarin Oriental Amsterdam</span>
          <span class="badge badge-hotel">酒店 2晚</span>
        </div>
        <div class="booking-sub">09-30 入住 ~ 10-02 退房 | 阿姆斯特丹</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>航班 HV6891 / FR1233</span>
          <span class="badge badge-flight">机票</span>
        </div>
        <div class="booking-sub">10-02 05:40 阿姆AMS ✈️ 圣托里尼JTR 10:05 | 10-04 08:20 JTR ✈️ 雅典ATH 09:10</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Mystique, Luxury Collection</span>
          <span class="badge badge-hotel">酒店 2晚</span>
        </div>
        <div class="booking-sub">10-02 入住 ~ 10-04 退房 | 圣托里尼 OIA</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Storyteller Boutique / Amalia Delphi</span>
          <span class="badge badge-hotel">酒店 自驾段</span>
        </div>
        <div class="booking-sub">10-04 迈泰奥拉 (1晚) | 10-05 德尔菲 (1晚)</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>Electra Palace Athens</span>
          <span class="badge badge-hotel">酒店 2晚</span>
        </div>
        <div class="booking-sub">10-06 入住 ~ 10-08 退房 | 雅典</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>The Zillers Rooftop Gastronomy</span>
          <span class="badge badge-dining">晚宴预订</span>
        </div>
        <div class="booking-sub">10-07 (周三) 19:00 | 4人 | 雅典露台餐厅</div>
      </div>

      <div class="booking-item">
        <div class="booking-header">
          <span>航班 A3620 / 海航 HU7922</span>
          <span class="badge badge-flight">机票</span>
        </div>
        <div class="booking-sub">10-08 07:30 雅典ATH ✈️ 布鲁塞尔BRU 09:30 | 12:00 BRU ✈️ 上海PVG 05:00+1</div>
      </div>
    </div>

    <!-- 4. 逐日行程列表 -->
    <div class="card">
      <div class="card-title">🗓️ 逐日行程与一键导航</div>

      <!-- Day 1 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 1: 09-25 (周五) 上海 ✈️ 重庆 (UTC+8)</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d1')">展开地图</button>
        </div>
        <div class="day-map" id="map-d1">
          📍 今日路线：上海浦东机场 ➔ 重庆江北机场 T3A<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&destination=Chongqing+Jiangbei+International+Airport" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">20:50</div>
          <div class="content-col"><a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Shanghai+Pudong+International+Airport" target="_blank">上海浦东机场 T1</a> 乘坐 MU5433 起飞。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">00:05+1</div>
          <div class="content-col"><a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Chongqing+Jiangbei+International+Airport" target="_blank">重庆江北机场 T3A</a> 降落。⚠️ 迅速领取行李并前往海航国际柜台！</div>
        </div>
      </div>

      <!-- Day 2 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 2: 09-26 (周六) 抵达布鲁塞尔 🚗 安特卫普</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d2')">展开地图</button>
        </div>
        <div class="day-map" id="map-d2">
          📍 今日路线：BRU机场 ➔ 布鲁塞尔大广场 ➔ 安特卫普酒店<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Brussels+Airport&destination=Botanic+Sanctuary+Antwerp&waypoints=Grand+Place+Brussels" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">02:50</div>
          <div class="content-col">重庆起飞 (HU0469)，08:20 降落布鲁塞尔 (BRU, UTC+2)。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">10:00</div>
          <div class="content-col">取车并游览 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Grand+Place+Brussels" target="_blank">布鲁塞尔大广场</a>、<a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Manneken+Pis" target="_blank">尿尿小童</a>。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">15:00</div>
          <div class="content-col">开车前往安特卫普，入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Botanic+Sanctuary+Antwerp" target="_blank">Botanic Sanctuary Antwerp</a>。</div>
        </div>
      </div>

      <!-- Day 3 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 3: 09-27 (周日) 根特 & 布鲁日一日游 🚗</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d3')">展开地图</button>
        </div>
        <div class="day-map" id="map-d3">
          📍 今日路线：安特卫普 ➔ 根特 ➔ 布鲁日 ➔ 返回安特卫普<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Antwerp&destination=Antwerp&waypoints=Ghent|Bruges" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">08:30</div>
          <div class="content-col">自驾去 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Ghent+City+Center" target="_blank">根特</a> (圣巴夫大教堂、伯爵城堡)。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">13:00</div>
          <div class="content-col">开往 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Bruges+Market+Square" target="_blank">布鲁日</a> (市集广场、爱之湖游船)。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">19:30</div>
          <div class="content-col">返回安特卫普酒店休息。</div>
        </div>
      </div>

      <!-- Day 4 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 4: 09-28 (周一) 安特卫普一日游</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d4')">展开地图</button>
        </div>
        <div class="day-map" id="map-d4">
          📍 今日路线：安特卫普中央车站 ➔ 圣母大教堂 ➔ 梅尔街<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&destination=Antwerp+Central+Station" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">10:00</div>
          <div class="content-col">游览 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Antwerp-Central+railway+station" target="_blank">安特卫普中央车站</a>、<a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Cathedral+of+Our+Lady+Antwerp" target="_blank">圣母大教堂</a>。</div>
        </div>
      </div>

      <!-- Day 5 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 5: 09-29 (周二) 小孩堤防 🚗 鹿特丹</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d5')">展开地图</button>
        </div>
        <div class="day-map" id="map-d5">
          📍 今日路线：安特卫普 ➔ 小孩堤防 ➔ 鹿特丹万豪酒店<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Antwerp&destination=Rotterdam+Marriott+Hotel&waypoints=Kinderdijk" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:30</div>
          <div class="content-col">自驾至 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Kinderdijk+windmills" target="_blank">小孩堤防</a> 风车群。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">14:00</div>
          <div class="content-col">开往鹿特丹，参观 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Cube+Houses+Rotterdam" target="_blank">立体方块屋</a>、<a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Markthal+Rotterdam" target="_blank">Markthal集市</a>。入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Rotterdam+Marriott+Hotel" target="_blank">Rotterdam Marriott</a>。</div>
        </div>
      </div>

      <!-- Day 6 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 6: 09-30 (周三) 羊角村 🚗 风车村 🚗 阿姆秀</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d6')">展开地图</button>
        </div>
        <div class="day-map" id="map-d6">
          📍 今日路线：鹿特丹 ➔ 羊角村 ➔ 桑斯安斯 ➔ 阿姆文华东方<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Rotterdam&destination=Mandarin+Oriental+Conservatorium+Amsterdam&waypoints=Giethoorn|Zaanse+Schans" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">08:00</div>
          <div class="content-col">早起开往 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Giethoorn" target="_blank">羊角村</a> 租船游览。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">14:00</div>
          <div class="content-col">开往 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Zaanse+Schans" target="_blank">桑斯安斯风车村</a>。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">18:00</div>
          <div class="content-col">入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Mandarin+Oriental+Conservatorium+Amsterdam" target="_blank">Mandarin Oriental Amsterdam</a>。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">21:00</div>
          <div class="content-col">红灯区 & <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Casa+Rosso+Amsterdam" target="_blank">Casa Rosso (粉象秀)</a> <span class="tag-booking">需现场购票</span></div>
        </div>
      </div>

      <!-- Day 7 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 7: 10-01 (周四) 阿姆双博物馆艺术日</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d7')">展开地图</button>
        </div>
        <div class="day-map" id="map-d7">
          📍 今日路线：梵高博物馆 ➔ 荷兰国家博物馆<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Van+Gogh+Museum&destination=Rijksmuseum" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:30</div>
          <div class="content-col"><a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Van+Gogh+Museum" target="_blank">梵高博物馆</a> <span class="tag-booking">需提前预约</span></div>
        </div>
        <div class="timeline-item">
          <div class="time-col">13:30</div>
          <div class="content-col"><a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Rijksmuseum" target="_blank">荷兰国家博物馆</a> <span class="tag-booking">需提前预约</span></div>
        </div>
        <div class="timeline-item">
          <div class="time-col">22:00</div>
          <div class="content-col">⚠️ 提前收拾行李，结账，准备凌晨03:30退房赶往机场！</div>
        </div>
      </div>

      <!-- Day 8 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 8: 10-02 (周五) 飞圣托里尼 ✈️ OIA日落 (UTC+3)</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d8')">展开地图</button>
        </div>
        <div class="day-map" id="map-d8">
          📍 今日路线：AMS机场还车 ➔ JTR机场 ➔ OIA悬崖酒店<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Santorini+Airport&destination=Mystique+a+Luxury+Collection+Hotel+Santorini" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">03:30</div>
          <div class="content-col">出发前往阿姆史基浦机场 (AMS) 还车。05:40 航班 (HV6891) 起飞。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">10:05</div>
          <div class="content-col">降落圣托里尼 (JTR)，前往 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Mystique+a+Luxury+Collection+Hotel+Santorini" target="_blank">Mystique Hotel</a>。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">17:30</div>
          <div class="content-col">前往 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Oia+Sunset+Viewpoint" target="_blank">OIA小镇</a> 抢占位置看爱琴海日落。</div>
        </div>
      </div>

      <!-- Day 9 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 9: 10-03 (周六) 圣托里尼环岛一日游</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d9')">展开地图</button>
        </div>
        <div class="day-map" id="map-d9">
          📍 今日路线：费拉小镇 ➔ 黑沙滩 ➔ 蓝顶教堂<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Fira&destination=Perissa+Black+Sand+Beach" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">10:00</div>
          <div class="content-col">游览 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Fira+Santorini" target="_blank">费拉小镇 (Fira)</a>、国家地理同款蓝顶教堂。</div>
        </div>
      </div>

      <!-- Day 10 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 10: 10-04 (周日) 飞雅典 🚗 开往迈泰奥拉</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d10')">展开地图</button>
        </div>
        <div class="day-map" id="map-d10">
          📍 今日路线：ATH机场取车 ➔ 迈泰奥拉酒店 (约4小时)<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Athens+International+Airport&destination=The+Storyteller+Boutique+House" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">08:20</div>
          <div class="content-col">圣托里尼起飞 (FR1233)，09:10 降落雅典 (ATH)。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">10:30</div>
          <div class="content-col">雅典机场取车，自驾开往迈泰奥拉 (Meteora)。入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=The+Storyteller+Boutique+House" target="_blank">The Storyteller Boutique</a>。</div>
        </div>
      </div>

      <!-- Day 11 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 11: 10-05 (周一) 迈泰奥拉修道院 🚗 德尔菲</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d11')">展开地图</button>
        </div>
        <div class="day-map" id="map-d11">
          📍 今日路线：迈泰奥拉修道院 ➔ 德尔菲酒店 (约3.5小时)<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Meteora&destination=Amalia+Hotel+Delphi" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:00</div>
          <div class="content-col">游览 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Great+Meteoron+Monastery" target="_blank">迈泰奥拉天空之城修道院</a> (注意着装)。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">14:00</div>
          <div class="content-col">开往德尔菲，入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Amalia+Hotel+Delphi" target="_blank">Amalia Hotel Delphi</a>。</div>
        </div>
      </div>

      <!-- Day 12 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 12: 10-06 (周二) 德尔菲遗址 🚗 开回雅典</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d12')">展开地图</button>
        </div>
        <div class="day-map" id="map-d12">
          📍 今日路线：德尔菲遗址 ➔ 雅典市区还车 ➔ 雅典酒店<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Delphi&destination=Electra+Palace+Athens" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:00</div>
          <div class="content-col">参观 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Delphi+Archaeological+Site" target="_blank">德尔菲遗址与博物馆</a>。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">14:00</div>
          <div class="content-col">自驾返回雅典市区还车，入住 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Electra+Palace+Athens" target="_blank">Electra Palace Athens</a>。</div>
        </div>
      </div>

      <!-- Day 13 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 13: 10-07 (周三) 雅典卫城 & 露台晚宴</span>
          <button class="map-toggle-btn" onclick="toggleMap('map-d13')">展开地图</button>
        </div>
        <div class="day-map" id="map-d13">
          📍 今日路线：雅典卫城 ➔ 宪法广场 ➔ The Zillers 餐厅<br>
          <a class="nav-btn" href="https://www.google.com/maps/dir/?api=1&origin=Acropolis+of+Athens&destination=The+Zillers+Rooftop+Gastronomy" target="_blank">🗺️ 打开全天导航</a>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:00</div>
          <div class="content-col">游览 <a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=Acropolis+of+Athens" target="_blank">雅典卫城</a> <span class="tag-booking">需提前约时段</span></div>
        </div>
        <div class="timeline-item">
          <div class="time-col">19:00</div>
          <div class="content-col"><a class="loc-link" href="https://www.google.com/maps/search/?api=1&query=The+Zillers+Rooftop+Gastronomy" target="_blank">The Zillers Rooftop Gastronomy</a> 晚宴 <span class="tag-booking">已定4人 19:00</span></div>
        </div>
      </div>

      <!-- Day 14 -->
      <div class="day-block">
        <div class="day-header">
          <span>Day 14: 10-08 (周四) 返程 雅典 ✈️ 布鲁塞尔 ✈️ 上海</span>
        </div>
        <div class="timeline-item">
          <div class="time-col">05:00</div>
          <div class="content-col">退房赶往雅典机场 (ATH)。07:30 航班 (A3620) 起飞。</div>
        </div>
        <div class="timeline-item">
          <div class="time-col">09:30</div>
          <div class="content-col">降落布鲁塞尔 (BRU)。⚠️ 2.5小时转机，12:00 HU7922 起飞回上海 (PVG 05:00+1)。</div>
        </div>
      </div>

    </div>

    <!-- 5. 待办事项列表 -->
    <div class="card">
      <div class="card-title">📝 待办清单 (办完告知我修改代码)</div>
      <ul class="todo-list">
        <li class="todo-item"><div class="todo-dot"></div>申根签证及保险打印件准备</li>
        <li class="todo-item"><div class="todo-dot"></div>国际驾照翻译件 (IDP / 驾照公证书)</li>
        <li class="todo-item"><div class="todo-dot"></div>预订梵高博物馆门票 (10-01)</li>
        <li class="todo-item"><div class="todo-dot"></div>预订雅典卫城门票 (10-07)</li>
        <li class="todo-item"><div class="todo-dot"></div>比利时 & 希腊租车确认件与主驾驶信用卡</li>
      </ul>
    </div>

    <!-- 6. 实用贴士 -->
    <div class="card">
      <div class="card-title">💡 实用贴士</div>
      <div class="tip-item">1. <strong>时区注意</strong>：比利时/荷兰属于中欧时间 (UTC+2)，希腊属于东欧时间 (UTC+3)，比荷兰快 1 小时！跨国飞行请注意手机时区自动切换。</div>
      <div class="tip-item">2. <strong>欧洲驾车</strong>：阿姆斯特丹极难停车，建议停 P+R 停车场；比利时跨国驶入荷兰需告知租车公司确认保险覆盖。</div>
      <div class="tip-item">3. <strong>迈泰奥拉修道院</strong>：女性必须穿过膝长裙/用围巾包裹，男性必须穿长裤，否则禁止入内。</div>
    </div>

  </div>

  <script>
    // 跨时区时间节点定义 (格式: ISO 8601 带时区偏移)
    const scheduleEvents = [
      { name: "MU5433 上海起飞 🛫", time: "2026-09-25T20:50:00+08:00" },
      { name: "HU0469 重庆起飞 🛫 (转机紧迫)", time: "2026-09-26T02:50:00+08:00" },
      { name: "抵达布鲁塞尔 🛬", time: "2026-09-26T08:20:00+02:00" },
      { name: "HV6891 飞圣托里尼 🛫 (凌晨出发)", time: "2026-10-02T05:40:00+02:00" },
      { name: "FR1233 飞雅典 🛫", time: "2026-10-04T08:20:00+03:00" },
      { name: "The Zillers 露台晚宴 🍷", time: "2026-10-07T19:00:00+03:00" },
      { name: "A3620 雅典起飞返程 🛫", time: "2026-10-08T07:30:00+03:00" },
      { name: "HU7922 布鲁塞尔飞上海 🛫", time: "2026-10-08T12:00:00+02:00" }
    ];

    function updateCountdown() {
      const now = new Date();
      let nextEvent = null;

      for (let evt of scheduleEvents) {
        let evtTime = new Date(evt.time);
        if (evtTime > now) {
          nextEvent = { ...evt, targetDate: evtTime };
          break;
        }
      }

      if (!nextEvent) {
        document.getElementById("next-event").innerText = "旅程圆满结束！🎉";
        return;
      }

      document.getElementById("next-event").innerText = nextEvent.name;
      const diff = nextEvent.targetDate - now;

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const mins = Math.floor((diff / 1000 / 60) % 60);
      const secs = Math.floor((diff / 1000) % 60);

      document.getElementById("cd-days").innerText = String(days).padStart(2, '0');
      document.getElementById("cd-hours").innerText = String(hours).padStart(2, '0');
      document.getElementById("cd-mins").innerText = String(mins).padStart(2, '0');
      document.getElementById("cd-secs").innerText = String(secs).padStart(2, '0');
    }

    setInterval(updateCountdown, 1000);
    updateCountdown();

    // 展开/收起当日地图
    function toggleMap(id) {
      const el = document.getElementById(id);
      if (el.style.display === "block") {
        el.style.display = "none";
      } else {
        el.style.display = "block";
      }
    }

    // 暗黑模式切换
    function toggleTheme() {
      const body = document.body;
      if (body.getAttribute("data-theme") === "dark") {
        body.removeAttribute("data-theme");
      } else {
        body.setAttribute("data-theme", "dark");
      }
    }
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file regenerated successfully.")