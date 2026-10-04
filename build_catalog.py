import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
DATA_DIR = os.path.join(BASE_DIR, "data")
REPO_URL_BASE = "https://zenq-graphics-api-online.vercel.app"

NEW_ASSETS = {
    "vietnam": {
        "name": "Việt Nam & Văn hóa",
        "items": [
            ("vn_flag", "Cờ đỏ sao vàng Việt Nam", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600">
  <rect width="900" height="600" fill="#DA251D"/>
  <polygon points="450,140 488,258 612,258 512,331 550,450 450,376 350,450 388,331 288,258 412,258" fill="#FFFF00"/>
</svg>'''),
            ("vn_flag_circle", "Huy hiệu cờ Việt Nam 3D", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <defs>
    <radialGradient id="flagGlow" cx="35%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#FF4D4D"/>
      <stop offset="70%" stop-color="#C8102E"/>
      <stop offset="100%" stop-color="#800010"/>
    </radialGradient>
    <linearGradient id="starGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFF200"/>
      <stop offset="100%" stop-color="#FFC000"/>
    </linearGradient>
    <linearGradient id="shineOverlay" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <circle cx="250" cy="250" r="230" fill="url(#flagGlow)" stroke="#A00E20" stroke-width="6"/>
  <polygon points="250,90 286,200 402,200 308,268 344,380 250,310 156,380 192,268 98,200 214,200" fill="url(#starGrad)"/>
  <ellipse cx="250" cy="160" rx="190" ry="110" fill="url(#shineOverlay)"/>
</svg>'''),
            ("vn_map", "Bản đồ Việt Nam hình chữ S", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 700" width="400" height="700">
  <defs>
    <linearGradient id="mapGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E52D27"/>
      <stop offset="100%" stop-color="#B31217"/>
    </linearGradient>
  </defs>
  <!-- Bản đồ hình chữ S cách điệu đặc trưng -->
  <path d="M 170 30 C 230 40 260 70 240 100 C 210 120 180 130 190 160 C 200 180 240 220 260 260 C 280 300 290 350 280 400 C 270 440 240 480 220 520 C 190 560 160 600 170 630 C 180 650 160 670 140 660 C 110 640 110 600 130 570 C 150 530 180 490 200 450 C 220 410 230 360 210 320 C 190 280 150 240 140 200 C 130 160 140 120 150 80 C 155 50 160 30 170 30 Z" fill="url(#mapGrad)" stroke="#B31217" stroke-width="2"/>
  <!-- Thủ đô Hà Nội (Ngôi sao vàng) -->
  <polygon points="190,95 195,107 208,107 197,115 201,127 190,120 179,127 183,115 172,107 185,107" fill="#FFEB3B"/>
  <!-- Quần đảo Hoàng Sa & Trường Sa -->
  <circle cx="320" cy="310" r="7" fill="#E52D27"/>
  <circle cx="335" cy="325" r="5" fill="#E52D27"/>
  <circle cx="310" cy="330" r="4" fill="#E52D27"/>
  <circle cx="330" cy="460" r="6" fill="#E52D27"/>
  <circle cx="350" cy="480" r="8" fill="#E52D27"/>
  <circle cx="365" cy="500" r="5" fill="#E52D27"/>
  <circle cx="340" cy="510" r="6" fill="#E52D27"/>
  <!-- Đảo Phú Quốc -->
  <ellipse cx="105" cy="625" rx="8" ry="14" fill="#E52D27"/>
</svg>'''),
            ("vn_non_la", "Nón lá bài thơ Việt Nam", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <defs>
    <linearGradient id="nonLaGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFF8E7"/>
      <stop offset="50%" stop-color="#EED9A4"/>
      <stop offset="100%" stop-color="#CBB179"/>
    </linearGradient>
    <linearGradient id="ribbonRed" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E53935"/>
      <stop offset="100%" stop-color="#B71C1C"/>
    </linearGradient>
  </defs>
  <!-- Quai nón lụa mềm mại -->
  <path d="M 120 260 C 100 320 90 380 90 395 C 100 390 120 340 135 280 Z" fill="url(#ribbonRed)"/>
  <path d="M 380 260 C 400 320 410 380 410 395 C 400 390 380 340 365 280 Z" fill="url(#ribbonRed)"/>
  <!-- Thân nón lá hình nón đặc trưng -->
  <polygon points="250,50 460,270 40,270" fill="url(#nonLaGrad)" stroke="#B39968" stroke-width="4"/>
  <!-- Vành đáy nón lá uốn cong mềm mại -->
  <path d="M 40 270 Q 250 300 460 270 Q 250 285 40 270 Z" fill="#B39968"/>
  <!-- Các vòng nan tre đồng tâm nón lá -->
  <path d="M 80 230 Q 250 250 420 230" stroke="#B39968" stroke-width="2" fill="none"/>
  <path d="M 120 190 Q 250 205 380 190" stroke="#B39968" stroke-width="2" fill="none"/>
  <path d="M 160 150 Q 250 160 340 150" stroke="#B39968" stroke-width="2" fill="none"/>
  <path d="M 200 110 Q 250 118 300 110" stroke="#B39968" stroke-width="2" fill="none"/>
</svg>'''),
            ("vn_trong_dong", "Trống đồng Đông Sơn cổ đại", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <radialGradient id="dongSonGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="60%" stop-color="#FFB300"/>
      <stop offset="100%" stop-color="#B57C1E"/>
    </radialGradient>
  </defs>
  <!-- Vành tròn ngoài cùng -->
  <circle cx="300" cy="300" r="280" fill="none" stroke="#D4AF37" stroke-width="6"/>
  <circle cx="300" cy="300" r="260" fill="none" stroke="#B57C1E" stroke-width="4"/>
  <circle cx="300" cy="300" r="230" fill="none" stroke="#D4AF37" stroke-width="5" stroke-dasharray="10 8"/>
  <circle cx="300" cy="300" r="190" fill="none" stroke="#B57C1E" stroke-width="4"/>
  <circle cx="300" cy="300" r="150" fill="none" stroke="#D4AF37" stroke-width="4" stroke-dasharray="6 6"/>
  <circle cx="300" cy="300" r="110" fill="none" stroke="#B57C1E" stroke-width="3"/>
  <!-- Ngôi sao 14 cánh tâm trống đồng -->
  <polygon points="300,195 310,240 345,208 335,250 378,235 348,268 395,272 355,290 395,315 352,325 385,355 340,348 355,390 322,365 318,405 300,370 282,405 278,365 245,390 260,348 215,355 248,325 205,315 245,290 205,272 252,268 222,235 265,250 255,208 290,240" fill="url(#dongSonGrad)" stroke="#8D5B10" stroke-width="2"/>
  <circle cx="300" cy="300" r="22" fill="#FFE082" stroke="#8D5B10" stroke-width="2"/>
</svg>'''),
            ("vn_flag_ribbon", "Dải cờ lụa đỏ sao vàng góc chéo", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350" width="500" height="350">
  <defs>
    <linearGradient id="ribbonGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E53935"/>
      <stop offset="40%" stop-color="#C62828"/>
      <stop offset="80%" stop-color="#8E0000"/>
    </linearGradient>
  </defs>
  <!-- Dải lụa uốn lượn bay bổng -->
  <path d="M 0 0 L 450 0 C 420 80 430 160 490 220 L 440 280 C 370 200 340 120 220 150 C 120 180 80 280 0 320 Z" fill="url(#ribbonGrad)"/>
  <!-- Nếp gấp lụa 3D phía sau -->
  <path d="M 440 280 C 410 240 390 200 390 170 L 450 180 Z" fill="#5F0000"/>
  <!-- Ngôi sao vàng uốn theo nếp lụa -->
  <polygon points="360,60 373,95 410,95 380,117 392,152 360,130 328,152 340,117 310,95 347,95" fill="#FFEB3B"/>
</svg>'''),
            ("vn_bunting_flags", "Dây cờ phướn đỏ sao vàng", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250" width="800" height="250">
  <!-- Dây treo cong mềm mại -->
  <path d="M 20 60 Q 400 180 780 60" fill="none" stroke="#757575" stroke-width="3"/>
  <!-- 5 lá cờ đỏ sao vàng đung đưa -->
  <!-- Lá 1 -->
  <g transform="translate(110, 80) rotate(-15)">
    <rect width="70" height="50" rx="3" fill="#DA251D"/>
    <polygon points="35,12 39,23 50,23 41,29 44,40 35,33 26,40 29,29 20,23 31,23" fill="#FFFF00"/>
  </g>
  <!-- Lá 2 -->
  <g transform="translate(240, 115) rotate(-6)">
    <rect width="70" height="50" rx="3" fill="#DA251D"/>
    <polygon points="35,12 39,23 50,23 41,29 44,40 35,33 26,40 29,29 20,23 31,23" fill="#FFFF00"/>
  </g>
  <!-- Lá 3 (chính giữa) -->
  <g transform="translate(365, 125)">
    <rect width="70" height="50" rx="3" fill="#DA251D"/>
    <polygon points="35,12 39,23 50,23 41,29 44,40 35,33 26,40 29,29 20,23 31,23" fill="#FFFF00"/>
  </g>
  <!-- Lá 4 -->
  <g transform="translate(490, 115) rotate(6)">
    <rect width="70" height="50" rx="3" fill="#DA251D"/>
    <polygon points="35,12 39,23 50,23 41,29 44,40 35,33 26,40 29,29 20,23 31,23" fill="#FFFF00"/>
  </g>
  <!-- Lá 5 -->
  <g transform="translate(620, 80) rotate(15)">
    <rect width="70" height="50" rx="3" fill="#DA251D"/>
    <polygon points="35,12 39,23 50,23 41,29 44,40 35,33 26,40 29,29 20,23 31,23" fill="#FFFF00"/>
  </g>
</svg>'''),
            ("vn_compass_rose", "La bàn hàng hải cổ điển", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <!-- Vòng tròn chia độ la bàn -->
  <circle cx="250" cy="250" r="220" fill="none" stroke="#2C3E50" stroke-width="4"/>
  <circle cx="250" cy="250" r="200" fill="none" stroke="#2C3E50" stroke-width="2"/>
  <circle cx="250" cy="250" r="170" fill="none" stroke="#7F8C8D" stroke-width="1.5" stroke-dasharray="4 4"/>
  <!-- 4 Kim chỉ chính N - S - W - E -->
  <!-- Hướng Bắc N -->
  <polygon points="250,30 262,230 250,250 238,230" fill="#2C3E50"/>
  <polygon points="250,30 262,230 250,250" fill="#E74C3C"/>
  <!-- Hướng Nam S -->
  <polygon points="250,470 262,270 250,250 238,270" fill="#BDC3C7"/>
  <polygon points="250,470 250,250 238,270" fill="#7F8C8D"/>
  <!-- Hướng Đông E -->
  <polygon points="470,250 270,262 250,250 270,238" fill="#BDC3C7"/>
  <polygon points="470,250 270,238 250,250" fill="#7F8C8D"/>
  <!-- Hướng Tây W -->
  <polygon points="30,250 230,262 250,250 230,238" fill="#BDC3C7"/>
  <polygon points="30,250 250,250 230,262" fill="#7F8C8D"/>
  <!-- Các hướng phụ NE, NW, SE, SW -->
  <polygon points="390,110 260,240 250,250 240,260" fill="#95A5A6"/>
  <polygon points="110,110 240,240 250,250 260,260" fill="#95A5A6"/>
  <polygon points="390,390 260,260 250,250 240,240" fill="#95A5A6"/>
  <polygon points="110,390 240,260 250,250 260,240" fill="#95A5A6"/>
  <!-- Tâm la bàn -->
  <circle cx="250" cy="250" r="18" fill="#2C3E50" stroke="#FFFFFF" stroke-width="3"/>
  <!-- Chữ cái 4 phương -->
  <text x="250" y="24" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#E74C3C" text-anchor="middle">N</text>
  <text x="250" y="495" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#2C3E50" text-anchor="middle">S</text>
  <text x="495" y="258" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#2C3E50" text-anchor="middle">E</text>
  <text x="12" y="258" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#2C3E50" text-anchor="middle">W</text>
</svg>'''),
            ("vn_lotus", "Hoa sen hồng Việt Nam", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <defs>
    <linearGradient id="lotusPink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FF80AB"/>
      <stop offset="60%" stop-color="#F48FB1"/>
      <stop offset="100%" stop-color="#C2185B"/>
    </linearGradient>
    <linearGradient id="lotusCenter" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FF4081"/>
      <stop offset="100%" stop-color="#AD1457"/>
    </linearGradient>
    <linearGradient id="leafGreen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#81C784"/>
      <stop offset="100%" stop-color="#2E7D32"/>
    </linearGradient>
  </defs>
  <!-- Lá sen xanh bên dưới -->
  <path d="M 50 320 C 150 290 350 290 450 320 C 380 370 120 370 50 320 Z" fill="url(#leafGreen)"/>
  <!-- Các cánh sen hai bên -->
  <path d="M 100 280 C 80 180 200 160 250 290 C 180 290 130 290 100 280 Z" fill="url(#lotusPink)" opacity="0.9"/>
  <path d="M 400 280 C 420 180 300 160 250 290 C 320 290 370 290 400 280 Z" fill="url(#lotusPink)" opacity="0.9"/>
  <path d="M 140 260 C 130 140 240 100 250 280 C 200 280 160 275 140 260 Z" fill="url(#lotusPink)"/>
  <path d="M 360 260 C 370 140 260 100 250 280 C 300 280 340 275 360 260 Z" fill="url(#lotusPink)"/>
  <!-- Cánh sen búp trung tâm -->
  <path d="M 250 60 C 290 140 300 220 250 280 C 200 220 210 140 250 60 Z" fill="url(#lotusCenter)"/>
  <!-- Đài sen vàng chính giữa -->
  <ellipse cx="250" cy="275" rx="30" ry="12" fill="#FFD54F"/>
</svg>''')
        ]
    },
    "music": {
        "name": "Âm nhạc & Giai điệu",
        "items": [
            ("music_treble_clef", "Khóa Sol cổ điển chuẩn mực", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 450" width="200" height="450">
  <path d="M 98 420 C 80 420 65 405 65 385 C 65 365 80 352 98 352 C 112 352 122 360 125 372 L 125 150 C 125 100 110 50 85 20 C 78 12 72 20 78 30 C 95 65 102 110 102 165 C 60 180 30 220 30 270 C 30 330 80 375 140 350 C 175 330 190 285 175 240 C 160 200 120 180 85 195 C 65 205 55 230 65 250 C 75 270 100 270 110 255 C 115 245 110 235 102 235 C 96 235 92 240 92 245 C 92 250 90 255 82 250 C 78 245 78 238 85 230 C 95 218 120 220 130 245 C 142 275 125 315 95 320 C 65 325 45 295 48 260 C 50 215 80 185 115 175 L 115 390 C 112 408 108 420 98 420 Z" fill="#1E293B"/>
</svg>'''),
            ("music_double_eighth", "Cặp nốt móc đơn", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <!-- Đầu nốt trái -->
  <ellipse cx="70" cy="230" rx="35" ry="25" transform="rotate(-25 70 230)" fill="#1E293B"/>
  <!-- Thân nốt trái -->
  <rect x="92" y="60" width="12" height="170" fill="#1E293B"/>
  <!-- Đầu nốt phải -->
  <ellipse cx="210" cy="190" rx="35" ry="25" transform="rotate(-25 210 190)" fill="#1E293B"/>
  <!-- Thân nốt phải -->
  <rect x="232" y="20" width="12" height="170" fill="#1E293B"/>
  <!-- Xà ngang nối hai nốt nhạc (Beam) -->
  <polygon points="92,60 244,20 244,48 92,88" fill="#1E293B"/>
</svg>'''),
            ("music_badge_round", "Icon nốt nhạc nền đĩa tròn", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="discBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00B4DB"/>
      <stop offset="100%" stop-color="#0083B0"/>
    </linearGradient>
  </defs>
  <circle cx="200" cy="200" r="190" fill="url(#discBlue)"/>
  <!-- Nốt nhạc đôi màu trắng nổi bật -->
  <g fill="#FFFFFF">
    <ellipse cx="130" cy="280" rx="35" ry="25" transform="rotate(-25 130 280)"/>
    <rect x="153" y="115" width="14" height="165"/>
    <ellipse cx="270" cy="245" rx="35" ry="25" transform="rotate(-25 270 245)"/>
    <rect x="293" y="80" width="14" height="165"/>
    <polygon points="153,115 307,80 307,112 153,147"/>
  </g>
</svg>'''),
            ("music_sparkle_notes", "Cụm nốt nhạc lấp lánh", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <!-- Nốt móc đơn hồng -->
  <ellipse cx="140" cy="300" rx="30" ry="22" transform="rotate(-20 140 300)" fill="#E91E63"/>
  <rect x="160" y="140" width="10" height="160" fill="#E91E63"/>
  <path d="M 170 140 C 210 150 230 190 220 230 C 215 200 195 170 170 165 Z" fill="#E91E63"/>
  <!-- Nốt đôi vàng ấm -->
  <ellipse cx="280" cy="240" rx="26" ry="18" transform="rotate(-20 280 240)" fill="#FFB300"/>
  <rect x="298" y="90" width="9" height="150" fill="#FFB300"/>
  <ellipse cx="380" cy="210" rx="26" ry="18" transform="rotate(-20 380 210)" fill="#FFB300"/>
  <rect x="398" y="60" width="9" height="150" fill="#FFB300"/>
  <polygon points="298,90 407,60 407,82 298,112" fill="#FFB300"/>
  <!-- Các ngôi sao lấp lánh 4 cánh xung quanh -->
  <path d="M 70 120 Q 90 120 90 100 Q 90 120 110 120 Q 90 120 90 140 Q 90 120 70 120 Z" fill="#00E5FF"/>
  <path d="M 420 130 Q 435 130 435 115 Q 435 130 450 130 Q 435 130 435 145 Q 435 130 420 130 Z" fill="#FF4081"/>
  <path d="M 230 50 Q 240 50 240 40 Q 240 50 250 50 Q 240 50 240 60 Q 240 50 230 50 Z" fill="#FFEA00"/>
</svg>'''),
            ("music_bass_clef", "Khóa Fa trầm cổ điển", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <path d="M 120 150 C 120 120 95 95 65 95 C 35 95 10 120 10 150 C 10 180 35 205 65 205 C 80 205 92 200 102 190 C 120 160 145 130 180 130 C 230 130 260 170 260 220 C 260 280 210 330 150 370 C 135 380 145 390 160 380 C 235 330 290 270 290 200 C 290 130 240 90 170 90 C 130 90 100 115 80 145 C 75 140 70 135 65 135 C 55 135 48 142 48 150 C 48 160 55 168 65 168 C 85 168 100 180 120 150 Z" fill="#1E293B"/>
  <circle cx="230" cy="165" r="16" fill="#1E293B"/>
  <circle cx="230" cy="235" r="16" fill="#1E293B"/>
</svg>'''),
            ("music_rainbow_trail", "Dải nốt nhạc bay đa sắc", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="600" height="300">
  <!-- Dải 5 dòng kẻ khuông nhạc uốn lượn sắc màu -->
  <path d="M 20 220 C 150 120 300 260 580 80" fill="none" stroke="#E91E63" stroke-width="4" opacity="0.6"/>
  <path d="M 20 235 C 150 135 300 275 580 95" fill="none" stroke="#9C27B0" stroke-width="4" opacity="0.6"/>
  <path d="M 20 250 C 150 150 300 290 580 110" fill="none" stroke="#2196F3" stroke-width="4" opacity="0.6"/>
  <!-- Các nốt nhạc nhiều màu bay theo dòng kẻ -->
  <ellipse cx="100" cy="190" rx="20" ry="14" transform="rotate(-20 100 190)" fill="#E91E63"/>
  <rect x="114" y="90" width="7" height="100" fill="#E91E63"/>
  <ellipse cx="240" cy="150" rx="20" ry="14" transform="rotate(-20 240 150)" fill="#FF9800"/>
  <rect x="254" y="50" width="7" height="100" fill="#FF9800"/>
  <ellipse cx="380" cy="200" rx="20" ry="14" transform="rotate(-20 380 200)" fill="#4CAF50"/>
  <rect x="394" y="100" width="7" height="100" fill="#4CAF50"/>
  <ellipse cx="500" cy="110" rx="20" ry="14" transform="rotate(-20 500 110)" fill="#00BCD4"/>
  <rect x="514" y="20" width="7" height="90" fill="#00BCD4"/>
</svg>''')
        ]
    },
    "audio": {
        "name": "Nhạc cụ & Âm thanh",
        "items": [
            ("audio_soundwave", "Dải sóng âm thanh Soundwave", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="600" height="200">
  <defs>
    <linearGradient id="waveGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4A00E0"/>
      <stop offset="50%" stop-color="#8E2DE2"/>
      <stop offset="100%" stop-color="#F000FF"/>
    </linearGradient>
  </defs>
  <!-- Các cột sóng âm đối xứng nhịp nhàng -->
  <g fill="url(#waveGrad)">
    <rect x="40" y="80" width="8" height="40" rx="4"/>
    <rect x="65" y="65" width="8" height="70" rx="4"/>
    <rect x="90" y="50" width="8" height="100" rx="4"/>
    <rect x="115" y="75" width="8" height="50" rx="4"/>
    <rect x="140" y="40" width="8" height="120" rx="4"/>
    <rect x="165" y="20" width="8" height="160" rx="4"/>
    <rect x="190" y="45" width="8" height="110" rx="4"/>
    <rect x="215" y="60" width="8" height="80" rx="4"/>
    <rect x="240" y="30" width="8" height="140" rx="4"/>
    <rect x="265" y="15" width="8" height="170" rx="4"/>
    <rect x="290" y="10" width="8" height="180" rx="4"/>
    <rect x="315" y="15" width="8" height="170" rx="4"/>
    <rect x="340" y="35" width="8" height="130" rx="4"/>
    <rect x="365" y="65" width="8" height="70" rx="4"/>
    <rect x="390" y="25" width="8" height="150" rx="4"/>
    <rect x="415" y="45" width="8" height="110" rx="4"/>
    <rect x="440" y="30" width="8" height="140" rx="4"/>
    <rect x="465" y="70" width="8" height="60" rx="4"/>
    <rect x="490" y="55" width="8" height="90" rx="4"/>
    <rect x="515" y="75" width="8" height="50" rx="4"/>
    <rect x="540" y="85" width="8" height="30" rx="4"/>
  </g>
</svg>'''),
            ("audio_headphones", "Tai nghe chụp tai Studio", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <defs>
    <linearGradient id="hpGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#37474F"/>
      <stop offset="100%" stop-color="#212121"/>
    </linearGradient>
  </defs>
  <!-- Quai đeo vòm đầu (Headband) -->
  <path d="M 80 260 C 80 120 150 60 250 60 C 350 60 420 120 420 260" fill="none" stroke="url(#hpGrad)" stroke-width="26" stroke-linecap="round"/>
  <!-- Đệm tai trái (Ear cup) -->
  <rect x="50" y="240" width="60" height="120" rx="28" fill="#455A64" stroke="#263238" stroke-width="6"/>
  <rect x="90" y="260" width="25" height="80" rx="12" fill="#212121"/>
  <!-- Đệm tai phải (Ear cup) -->
  <rect x="390" y="240" width="60" height="120" rx="28" fill="#455A64" stroke="#263238" stroke-width="6"/>
  <rect x="385" y="260" width="25" height="80" rx="12" fill="#212121"/>
</svg>'''),
            ("audio_piano_keys", "Bàn phím đàn Grand Piano", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300" width="500" height="300">
  <!-- Thân hộp gỗ đàn piano -->
  <rect x="10" y="10" width="480" height="280" rx="12" fill="#1A1A1A"/>
  <rect x="30" y="50" width="440" height="220" fill="#FFFFFF" stroke="#000000" stroke-width="3"/>
  <!-- Phím trắng (White keys) -->
  <line x1="85" y1="50" x2="85" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="140" y1="50" x2="140" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="195" y1="50" x2="195" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="250" y1="50" x2="250" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="305" y1="50" x2="305" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="360" y1="50" x2="360" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <line x1="415" y1="50" x2="415" y2="270" stroke="#CCCCCC" stroke-width="2"/>
  <!-- Phím đen (Black keys) -->
  <rect x="68" y="50" width="32" height="135" rx="3" fill="#111111"/>
  <rect x="123" y="50" width="32" height="135" rx="3" fill="#111111"/>
  <rect x="233" y="50" width="32" height="135" rx="3" fill="#111111"/>
  <rect x="288" y="50" width="32" height="135" rx="3" fill="#111111"/>
  <rect x="343" y="50" width="32" height="135" rx="3" fill="#111111"/>
</svg>'''),
            ("audio_guitar_acoustic", "Đàn Guitar thùng gỗ Acoustic", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 600" width="300" height="600">
  <defs>
    <linearGradient id="guitarWood" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#D7A15C"/>
      <stop offset="50%" stop-color="#B87333"/>
      <stop offset="100%" stop-color="#80471C"/>
    </linearGradient>
  </defs>
  <!-- Đầu đàn & khóa dây -->
  <rect x="135" y="10" width="30" height="70" rx="6" fill="#5D4037"/>
  <!-- Cần đàn -->
  <rect x="142" y="80" width="16" height="200" fill="#3E2723"/>
  <!-- Thùng đàn guitar chuẩn dáng số 8 -->
  <path d="M 150 260 C 100 260 70 300 70 340 C 70 380 110 400 90 440 C 60 500 100 580 150 580 C 200 580 240 500 210 440 C 190 400 230 380 230 340 C 230 300 200 260 150 260 Z" fill="url(#guitarWood)" stroke="#5D4037" stroke-width="4"/>
  <!-- Lỗ thoát âm tròn ở giữa thùng đàn -->
  <circle cx="150" cy="380" r="34" fill="#212121" stroke="#D7A15C" stroke-width="5"/>
  <!-- Ngựa đàn -->
  <rect x="130" y="490" width="40" height="14" rx="3" fill="#3E2723"/>
  <!-- Dây đàn -->
  <line x1="150" y1="80" x2="150" y2="490" stroke="#FFFFFF" stroke-width="2" opacity="0.8"/>
</svg>'''),
            ("audio_drum_set", "Dàn trống biểu diễn nhạc Rock", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 450" width="500" height="450">
  <!-- Chân đỡ kim loại -->
  <line x1="250" y1="340" x2="250" y2="430" stroke="#78909C" stroke-width="6"/>
  <!-- Trống Bass to ở giữa (Bass drum) -->
  <circle cx="250" cy="270" r="110" fill="#E53935" stroke="#212121" stroke-width="8"/>
  <circle cx="250" cy="270" r="85" fill="#FAFAFA" stroke="#B0BEC5" stroke-width="4"/>
  <!-- Trống Tom nhỏ bên trái -->
  <rect x="150" y="110" width="80" height="65" rx="6" fill="#1E88E5" stroke="#212121" stroke-width="5"/>
  <!-- Trống Tom nhỏ bên phải -->
  <rect x="270" y="110" width="80" height="65" rx="6" fill="#1E88E5" stroke="#212121" stroke-width="5"/>
  <!-- Chũm chọe đồng bên trái (Cymbal) -->
  <ellipse cx="100" cy="110" rx="70" ry="16" fill="#FFD54F" stroke="#FFA000" stroke-width="4"/>
  <line x1="100" y1="110" x2="100" y2="380" stroke="#78909C" stroke-width="5"/>
  <!-- Chũm chọe đồng bên phải (Ride Cymbal) -->
  <ellipse cx="400" cy="100" rx="75" ry="18" fill="#FFD54F" stroke="#FFA000" stroke-width="4"/>
  <line x1="400" y1="100" x2="400" y2="380" stroke="#78909C" stroke-width="5"/>
</svg>'''),
            ("audio_microphone_vintage", "Microphone kim loại cổ điển Retro", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 500" width="300" height="500">
  <defs>
    <linearGradient id="micChrome" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#CFD8DC"/>
      <stop offset="50%" stop-color="#90A4AE"/>
      <stop offset="100%" stop-color="#455A64"/>
    </linearGradient>
  </defs>
  <!-- Đầu micro dạng lưới sọc ngang -->
  <rect x="90" y="50" width="120" height="170" rx="45" fill="url(#micChrome)" stroke="#263238" stroke-width="5"/>
  <!-- Các khe thoát âm cổ điển -->
  <line x1="110" y1="80" x2="190" y2="80" stroke="#263238" stroke-width="4"/>
  <line x1="105" y1="105" x2="195" y2="105" stroke="#263238" stroke-width="4"/>
  <line x1="100" y1="130" x2="200" y2="130" stroke="#263238" stroke-width="4"/>
  <line x1="105" y1="155" x2="195" y2="155" stroke="#263238" stroke-width="4"/>
  <line x1="110" y1="180" x2="190" y2="180" stroke="#263238" stroke-width="4"/>
  <!-- Vòng cung gá kẹp chữ U -->
  <path d="M 75 130 C 75 250 225 250 225 130" fill="none" stroke="#37474F" stroke-width="8"/>
  <!-- Trục đứng & đế tròn để bàn -->
  <rect x="142" y="245" width="16" height="150" fill="#37474F"/>
  <ellipse cx="150" cy="420" rx="80" ry="25" fill="#263238"/>
</svg>''')
        ]
    },
    "education": {
        "name": "Giáo dục & Học tập",
        "items": [
            ("edu_grad_cap", "Mũ tốt nghiệp cử nhân", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <defs>
    <linearGradient id="capDark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2C3E50"/>
      <stop offset="100%" stop-color="#1A252F"/>
    </linearGradient>
  </defs>
  <!-- Vòm mũ đội phía dưới -->
  <path d="M 150 210 Q 250 300 350 210 L 350 240 Q 250 330 150 240 Z" fill="#1A252F"/>
  <!-- Mặt quả trám mũ cử nhân -->
  <polygon points="250,80 470,160 250,230 30,160" fill="url(#capDark)" stroke="#111" stroke-width="4"/>
  <!-- Dây tua rua đỏ vinh danh -->
  <path d="M 250 160 Q 380 180 400 280" fill="none" stroke="#E74C3C" stroke-width="6"/>
  <polygon points="390,280 410,280 405,330 395,330" fill="#E74C3C"/>
  <circle cx="250" cy="160" r="10" fill="#F1C40F"/>
</svg>'''),
            ("edu_open_book", "Quyển sách tri thức mở", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350" width="500" height="350">
  <defs>
    <linearGradient id="bookPage" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#ECEFF1"/>
    </linearGradient>
  </defs>
  <!-- Bìa sách ngoài -->
  <path d="M 250 80 Q 140 50 30 70 L 30 270 Q 140 250 250 280 Q 360 250 470 270 L 470 70 Q 360 50 250 80 Z" fill="#1E88E5"/>
  <!-- Trang sách trái -->
  <path d="M 245 85 Q 145 60 45 80 L 45 260 Q 145 240 245 265 Z" fill="url(#bookPage)"/>
  <!-- Trang sách phải -->
  <path d="M 255 85 Q 355 60 455 80 L 455 260 Q 355 240 255 265 Z" fill="url(#bookPage)"/>
  <!-- Các dòng chữ minh họa -->
  <line x1="75" y1="120" x2="215" y2="120" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
  <line x1="75" y1="150" x2="215" y2="150" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
  <line x1="75" y1="180" x2="180" y2="180" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
  <line x1="285" y1="120" x2="425" y2="120" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
  <line x1="285" y1="150" x2="425" y2="150" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
  <line x1="285" y1="180" x2="390" y2="180" stroke="#90A4AE" stroke-width="4" stroke-linecap="round"/>
</svg>'''),
            ("edu_trophy", "Cúp vàng vinh danh hạng nhất", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 450" width="400" height="450">
  <defs>
    <linearGradient id="goldTrophy" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFF176"/>
      <stop offset="50%" stop-color="#FBC02D"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </linearGradient>
  </defs>
  <!-- Quai cúp hai bên -->
  <path d="M 120 120 C 30 120 30 240 130 250" fill="none" stroke="url(#goldTrophy)" stroke-width="20" stroke-linecap="round"/>
  <path d="M 280 120 C 370 120 370 240 270 250" fill="none" stroke="url(#goldTrophy)" stroke-width="20" stroke-linecap="round"/>
  <!-- Thân cúp hình phễu vàng -->
  <path d="M 100 80 L 300 80 L 270 240 C 250 280 150 280 130 240 Z" fill="url(#goldTrophy)" stroke="#E65100" stroke-width="4"/>
  <!-- Ngôi sao số 1 giữa cúp -->
  <polygon points="200,130 208,155 235,155 213,171 221,195 200,180 179,195 187,171 165,155 192,155" fill="#FFFFFF"/>
  <!-- Trục đỡ & bệ cúp gỗ đen -->
  <rect x="185" y="270" width="30" height="70" fill="url(#goldTrophy)"/>
  <rect x="120" y="340" width="160" height="60" rx="8" fill="#3E2723" stroke="#212121" stroke-width="4"/>
</svg>''')
        ]
    },
    "business": {
        "name": "Kinh doanh & Khởi nghiệp",
        "items": [
            ("biz_chart_up", "Biểu đồ tăng trưởng đột phá", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#42A5F5"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </linearGradient>
  </defs>
  <!-- Trục tọa độ -->
  <line x1="50" y1="350" x2="450" y2="350" stroke="#78909C" stroke-width="6" stroke-linecap="round"/>
  <!-- Các cột tăng dần -->
  <rect x="80" y="240" width="55" height="110" rx="6" fill="url(#barGrad)"/>
  <rect x="165" y="180" width="55" height="170" rx="6" fill="url(#barGrad)"/>
  <rect x="250" y="120" width="55" height="230" rx="6" fill="url(#barGrad)"/>
  <rect x="335" y="60" width="55" height="290" rx="6" fill="url(#barGrad)"/>
  <!-- Mũi tên tăng trưởng màu xanh lá -->
  <path d="M 60 260 L 180 190 L 270 140 L 410 40" fill="none" stroke="#00E676" stroke-width="8" stroke-linecap="round"/>
  <polygon points="410,40 370,50 395,80" fill="#00E676"/>
</svg>'''),
            ("biz_rocket", "Tên lửa cất cánh Startup", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
  <!-- Ngọn lửa đẩy tên lửa -->
  <polygon points="170,390 200,490 230,390" fill="#FF3D00"/>
  <polygon points="185,390 200,450 215,390" fill="#FFEA00"/>
  <!-- Cánh tên lửa hai bên -->
  <path d="M 130 310 L 80 390 L 150 370 Z" fill="#D32F2F"/>
  <path d="M 270 310 L 320 390 L 250 370 Z" fill="#D32F2F"/>
  <!-- Thân tên lửa thon dài -->
  <path d="M 200 40 C 140 140 140 330 140 380 L 260 380 C 260 330 260 140 200 40 Z" fill="#ECEFF1" stroke="#37474F" stroke-width="4"/>
  <!-- Đầu tên lửa đỏ -->
  <path d="M 200 40 C 170 90 160 150 160 180 L 240 180 C 240 150 230 90 200 40 Z" fill="#E53935"/>
  <!-- Cửa sổ tròn tàu vũ trụ -->
  <circle cx="200" cy="240" r="30" fill="#00B0FF" stroke="#37474F" stroke-width="6"/>
</svg>'''),
            ("biz_lightbulb_idea", "Bóng đèn ý tưởng sáng tạo", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 450" width="400" height="450">
  <defs>
    <radialGradient id="bulbGlow" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#FFEE58"/>
      <stop offset="80%" stop-color="#FDD835"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </radialGradient>
  </defs>
  <!-- Các tia sáng tỏa ra -->
  <line x1="200" y1="20" x2="200" y2="55" stroke="#FBC02D" stroke-width="6" stroke-linecap="round"/>
  <line x1="80" y1="70" x2="105" y2="95" stroke="#FBC02D" stroke-width="6" stroke-linecap="round"/>
  <line x1="320" y1="70" x2="295" y2="95" stroke="#FBC02D" stroke-width="6" stroke-linecap="round"/>
  <!-- Bầu thủy tinh bóng đèn -->
  <path d="M 200 70 C 130 70 95 125 95 180 C 95 230 140 265 145 310 L 255 310 C 260 265 305 230 305 180 C 305 125 270 70 200 70 Z" fill="url(#bulbGlow)" stroke="#F57F17" stroke-width="4"/>
  <!-- Đuôi ren xoắn kim loại -->
  <rect x="150" y="320" width="100" height="18" rx="6" fill="#B0BEC5"/>
  <rect x="160" y="344" width="80" height="18" rx="6" fill="#90A4AE"/>
  <rect x="175" y="368" width="50" height="18" rx="8" fill="#78909C"/>
</svg>''')
        ]
    },
    "tech": {
        "name": "Khoa học & Công nghệ",
        "items": [
            ("tech_robot_ai", "Robot trí tuệ nhân tạo AI", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="botGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#0091EA"/>
    </linearGradient>
  </defs>
  <!-- Ăng-ten phát tín hiệu -->
  <line x1="200" y1="40" x2="200" y2="90" stroke="#00E5FF" stroke-width="6"/>
  <circle cx="200" cy="35" r="14" fill="#FF4081"/>
  <!-- Đầu robot bo góc tương lai -->
  <rect x="80" y="90" width="240" height="200" rx="50" fill="url(#botGrad)" stroke="#006064" stroke-width="5"/>
  <!-- Màn hình mắt đen kính visor -->
  <rect x="110" y="140" width="180" height="70" rx="25" fill="#212121"/>
  <!-- Hai mắt phát sáng LED xanh neon -->
  <circle cx="160" cy="175" r="18" fill="#00E676"/>
  <circle cx="240" cy="175" r="18" fill="#00E676"/>
  <!-- Nụ cười vi mạch điện tử -->
  <path d="M 160 240 Q 200 265 240 240" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
</svg>'''),
            ("tech_cpu_chip", "Vi xử lý bán dẫn CPU", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <!-- Chân tiếp xúc mạ vàng (Pins) -->
  <g stroke="#FFD54F" stroke-width="6" stroke-linecap="round">
    <line x1="120" y1="40" x2="120" y2="80"/><line x1="160" y1="40" x2="160" y2="80"/><line x1="200" y1="40" x2="200" y2="80"/><line x1="240" y1="40" x2="240" y2="80"/><line x1="280" y1="40" x2="280" y2="80"/>
    <line x1="120" y1="320" x2="120" y2="360"/><line x1="160" y1="320" x2="160" y2="360"/><line x1="200" y1="320" x2="200" y2="360"/><line x1="240" y1="320" x2="240" y2="360"/><line x1="280" y1="320" x2="280" y2="360"/>
    <line x1="40" y1="120" x2="80" y2="120"/><line x1="40" y1="160" x2="80" y2="160"/><line x1="40" y1="200" x2="80" y2="200"/><line x1="40" y1="240" x2="80" y2="240"/><line x1="40" y1="280" x2="80" y2="280"/>
    <line x1="320" y1="120" x2="360" y2="120"/><line x1="320" y1="160" x2="360" y2="160"/><line x1="320" y1="200" x2="360" y2="200"/><line x1="320" y1="240" x2="360" y2="240"/><line x1="320" y1="280" x2="360" y2="280"/>
  </g>
  <!-- Bản mạch đế Silicon màu xanh rêu -->
  <rect x="80" y="80" width="240" height="240" rx="20" fill="#1B5E20" stroke="#0A380A" stroke-width="4"/>
  <!-- Lưng tản nhiệt kim loại mạ bạc -->
  <rect x="120" y="120" width="160" height="160" rx="12" fill="#ECEFF1" stroke="#90A4AE" stroke-width="3"/>
  <text x="200" y="210" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="#37474F" text-anchor="middle">ZENQ AI</text>
</svg>''')
        ]
    },
    "food": {
        "name": "Ẩm thực & Thức uống",
        "items": [
            ("food_vietnamese_coffee", "Cà phê phin sữa đá Việt Nam", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
  <!-- Ly thủy tinh cao trong suốt -->
  <path d="M 120 220 L 140 460 C 140 475 260 475 260 460 L 280 220 Z" fill="#ECEFF1" stroke="#90A4AE" stroke-width="4"/>
  <!-- Tầng sữa đặc trắng béo bên dưới -->
  <path d="M 137 420 L 140 460 C 140 475 260 475 260 460 L 263 420 Z" fill="#FFFDE7"/>
  <!-- Tầng cà phê phin đậm đà sánh mịn -->
  <path d="M 125 280 L 137 420 L 263 420 L 275 280 Z" fill="#3E2723"/>
  <!-- Những viên đá lạnh mát rượi -->
  <rect x="150" y="290" width="40" height="40" rx="6" fill="#B3E5FC" opacity="0.8"/>
  <rect x="210" y="320" width="40" height="40" rx="6" fill="#B3E5FC" opacity="0.8"/>
  <!-- Phin cà phê nhôm truyền thống phía trên ly -->
  <rect x="100" y="200" width="200" height="20" rx="4" fill="#CFD8DC" stroke="#78909C" stroke-width="3"/>
  <rect x="120" y="130" width="160" height="70" rx="4" fill="#B0BEC5" stroke="#78909C" stroke-width="3"/>
  <!-- Nắp phin -->
  <path d="M 110 130 L 200 95 L 290 130 Z" fill="#CFD8DC" stroke="#78909C" stroke-width="3"/>
  <circle cx="200" cy="90" r="10" fill="#90A4AE"/>
</svg>'''),
            ("food_banh_mi", "Bánh mì kẹp giòn rụm Việt Nam", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300" width="500" height="300">
  <defs>
    <linearGradient id="crustGold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFB74D"/>
      <stop offset="50%" stop-color="#FFA726"/>
      <stop offset="100%" stop-color="#E65100"/>
    </linearGradient>
  </defs>
  <!-- Lớp vỏ bánh mì giòn vàng ươm hình bầu dục -->
  <path d="M 50 150 C 50 70 450 70 450 150 C 450 230 50 230 50 150 Z" fill="url(#crustGold)" stroke="#BF360C" stroke-width="4"/>
  <!-- Vết rạch giòn nứt vỏ đặc trưng bánh mì Việt Nam -->
  <path d="M 120 120 Q 200 135 230 110" fill="none" stroke="#FFE082" stroke-width="8" stroke-linecap="round"/>
  <path d="M 270 120 Q 350 135 380 110" fill="none" stroke="#FFE082" stroke-width="8" stroke-linecap="round"/>
  <!-- Nhân rau thơm dưa leo và thịt kẹp thò ra -->
  <path d="M 100 160 Q 250 175 400 160" stroke="#4CAF50" stroke-width="12" stroke-linecap="round"/>
  <path d="M 140 168 Q 280 180 370 168" stroke="#E53935" stroke-width="10" stroke-linecap="round"/>
</svg>''')
        ]
    },
    "social": {
        "name": "Mạng xã hội & Biểu tượng cảm xúc",
        "items": [
            ("social_heart", "Trái tim yêu thích đỏ thắm", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="heartRed" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FF1744"/>
      <stop offset="100%" stop-color="#D50000"/>
    </linearGradient>
  </defs>
  <path d="M 200 360 C 90 270 30 190 30 120 C 30 50 90 20 150 20 C 180 20 200 40 200 40 C 200 40 220 20 250 20 C 310 20 370 50 370 120 C 370 190 310 270 200 360 Z" fill="url(#heartRed)"/>
</svg>'''),
            ("social_crown_gold", "Vương miện hoàng gia vàng óng", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350" width="500" height="350">
  <defs>
    <linearGradient id="crownGold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFEE58"/>
      <stop offset="60%" stop-color="#FDD835"/>
      <stop offset="100%" stop-color="#F57F17"/>
    </linearGradient>
  </defs>
  <!-- Thân vương miện hoàng tộc 5 chóp nhọn -->
  <polygon points="50,110 130,240 250,70 370,240 450,110 420,290 80,290" fill="url(#crownGold)" stroke="#E65100" stroke-width="4"/>
  <!-- Đai chân vương miện đính ngọc -->
  <rect x="70" y="280" width="360" height="45" rx="10" fill="#F57F17"/>
  <!-- 5 viên ngọc ruby trên đỉnh chóp -->
  <circle cx="50" cy="110" r="14" fill="#D50000"/>
  <circle cx="250" cy="70" r="18" fill="#2979FF"/>
  <circle cx="450" cy="110" r="14" fill="#D50000"/>
  <circle cx="150" cy="302" r="10" fill="#00E676"/>
  <circle cx="250" cy="302" r="12" fill="#D50000"/>
  <circle cx="350" cy="302" r="10" fill="#00E676"/>
</svg>''')
        ]
    }
}

def main():
    json_path = os.path.join(DATA_DIR, "graphics.json")
    with open(json_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    existing_categories = catalog.get("categories", [])
    cat_by_name = {c["name"]: c for c in existing_categories}

    total_added = 0

    for folder_key, cat_data in NEW_ASSETS.items():
        folder_dir = os.path.join(PUBLIC_DIR, folder_key)
        os.makedirs(folder_dir, exist_ok=True)

        cat_title = cat_data["name"]
        if cat_title not in cat_by_name:
            target_cat = {"name": cat_title, "items": []}
            existing_categories.append(target_cat)
            cat_by_name[cat_title] = target_cat
        else:
            target_cat = cat_by_name[cat_title]

        existing_item_ids = {it["id"] for it in target_cat["items"]}

        for item_id, item_name, svg_content in cat_data["items"]:
            file_name = f"{item_id}.svg"
            file_path = os.path.join(folder_dir, file_name)
            
            with open(file_path, "w", encoding="utf-8") as svg_file:
                svg_file.write(svg_content.strip())

            full_id = f"{folder_key}_{item_id}"
            item_url = f"{REPO_URL_BASE}/{folder_key}/{file_name}"

            if full_id not in existing_item_ids:
                target_cat["items"].append({
                    "id": full_id,
                    "name": item_name,
                    "url": item_url,
                    "type": "svg"
                })
                total_added += 1

    catalog["total"] = sum(len(c["items"]) for c in existing_categories)
    catalog["categories"] = existing_categories

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    # Sync to genofficepy/data/graphics.json as well
    genoffice_json = r"c:\Users\Danh\Desktop\genofficepy\data\graphics.json"
    if os.path.exists(os.path.dirname(genoffice_json)):
        with open(genoffice_json, "w", encoding="utf-8") as f:
            json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"Added {total_added} new graphics items! Total items in catalog: {catalog['total']}")

if __name__ == "__main__":
    main()
