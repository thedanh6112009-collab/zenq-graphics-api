import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
DATA_DIR = os.path.join(BASE_DIR, "data")
REPO_URL_BASE = "https://zenq-graphics-api-online.vercel.app"

CUSTOM_SHOWCASE = {
    "vietnam": [
        ("vn_bunting_triangles", "Dây cờ tam giác lễ hội đỏ vàng", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250" width="800" height="250">
  <path d="M 20 60 Q 400 180 780 60" fill="none" stroke="#BDBDBD" stroke-width="3"/>
  <!-- Các lá cờ tam giác xen kẽ đỏ vàng -->
  <polygon points="90,85 140,80 115,160" fill="#FDD835"/>
  <polygon points="170,105 220,110 195,190" fill="#E53935"/>
  <polygon points="250,125 300,132 275,210" fill="#FDD835"/>
  <!-- Cờ đỏ sao vàng ở giữa -->
  <g transform="translate(360, 130)">
    <rect width="80" height="60" rx="3" fill="#DA251D"/>
    <polygon points="40,15 45,28 58,28 47,36 51,49 40,41 29,49 33,36 22,28 35,28" fill="#FFFF00"/>
  </g>
  <polygon points="490,132 540,125 515,210" fill="#FDD835"/>
  <polygon points="570,110 620,105 595,190" fill="#E53935"/>
  <polygon points="650,80 700,85 675,160" fill="#FDD835"/>
</svg>'''),
        ("vn_pagoda", "Chùa Một Cột truyền thống", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <!-- Cột trụ đá giữa hồ sen -->
  <rect x="225" y="320" width="50" height="130" fill="#78909C" stroke="#37474F" stroke-width="4"/>
  <!-- Bệ đỡ xà gỗ cong -->
  <polygon points="180,320 320,320 280,350 220,350" fill="#8D6E63"/>
  <!-- Thân chùa Một Cột gỗ đỏ -->
  <rect x="180" y="210" width="140" height="110" fill="#C62828" stroke="#8E0000" stroke-width="4"/>
  <rect x="220" y="240" width="60" height="80" fill="#3E2723"/>
  <!-- Mái chùa cong 4 góc đặc trưng kiến trúc Việt Nam -->
  <path d="M 120 215 C 190 220 310 220 380 215 C 390 190 350 170 310 165 L 190 165 C 150 170 110 190 120 215 Z" fill="#D84315"/>
  <!-- Đỉnh nóc ngói âm dương chùa -->
  <path d="M 190 165 L 250 90 L 310 165 Z" fill="#BF360C"/>
  <circle cx="250" cy="80" r="12" fill="#FFD54F"/>
  <!-- Mặt nước hồ sen xanh biếc -->
  <ellipse cx="250" cy="450" rx="200" ry="25" fill="#4FC3F7" opacity="0.6"/>
</svg>'''),
        ("vn_farmer", "Bác nông dân gặt lúa quê hương", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <!-- Nón lá che đầu -->
  <polygon points="250,90 360,200 140,200" fill="#FFE082" stroke="#B57C1E" stroke-width="4"/>
  <path d="M 140 200 Q 250 215 360 200 Z" fill="#B57C1E"/>
  <!-- Thân áo bà ba nâu chân chất -->
  <path d="M 190 205 L 170 330 L 330 330 L 310 205 Z" fill="#5D4037"/>
  <!-- Quần bà ba sẫm màu -->
  <rect x="185" y="330" width="55" height="120" rx="10" fill="#212121"/>
  <rect x="260" y="330" width="55" height="120" rx="10" fill="#212121"/>
  <!-- Bó lúa vàng trĩu hạt trên tay -->
  <path d="M 310 240 Q 380 220 420 260 Q 400 320 340 300 Z" fill="#FDD835" stroke="#F57F17" stroke-width="3"/>
  <path d="M 320 250 Q 390 230 410 270" stroke="#E65100" stroke-width="3" fill="none"/>
</svg>'''),
        ("vn_banh_chung", "Bánh chưng xanh Tết cổ truyền", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
  <defs>
    <linearGradient id="laDongGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4CAF50"/>
      <stop offset="50%" stop-color="#2E7D32"/>
      <stop offset="100%" stop-color="#1B5E20"/>
    </linearGradient>
  </defs>
  <!-- Vuông vắn bánh chưng xanh lá dong -->
  <rect x="80" y="80" width="340" height="340" rx="16" fill="url(#laDongGrad)" stroke="#0D3810" stroke-width="6"/>
  <!-- Dây lạt giang vàng buộc chữ thập -->
  <rect x="170" y="80" width="24" height="340" fill="#FFF59D" stroke="#FBC02D" stroke-width="2"/>
  <rect x="306" y="80" width="24" height="340" fill="#FFF59D" stroke="#FBC02D" stroke-width="2"/>
  <rect x="80" y="170" width="340" height="24" fill="#FFF59D" stroke="#FBC02D" stroke-width="2"/>
  <rect x="80" y="306" width="340" height="24" fill="#FFF59D" stroke="#FBC02D" stroke-width="2"/>
  <!-- Nút thắt lạt tre ở giữa -->
  <circle cx="182" cy="182" r="8" fill="#FBC02D"/>
  <circle cx="318" cy="182" r="8" fill="#FBC02D"/>
  <circle cx="182" cy="318" r="8" fill="#FBC02D"/>
  <circle cx="318" cy="318" r="8" fill="#FBC02D"/>
</svg>''')
    ],
    "music": [
        ("music_dotted_treble", "Khóa Sol hạt ngọc lấp lánh", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 500" width="300" height="500">
  <g fill="#546E7A">
    <!-- Thân khóa Sol kết từ các hạt cườm ngọc tròn đều -->
    <circle cx="150" cy="50" r="10"/><circle cx="165" cy="80" r="9"/><circle cx="170" cy="115" r="9"/>
    <circle cx="160" cy="150" r="9"/><circle cx="140" cy="185" r="9"/><circle cx="115" cy="220" r="9"/>
    <circle cx="95" cy="255" r="9"/><circle cx="85" cy="295" r="9"/><circle cx="95" cy="335" r="9"/>
    <circle cx="120" cy="365" r="9"/><circle cx="155" cy="375" r="9"/><circle cx="190" cy="360" r="9"/>
    <circle cx="215" cy="325" r="9"/><circle cx="215" cy="285" r="9"/><circle cx="195" cy="250" r="9"/>
    <circle cx="165" cy="235" r="9"/><circle cx="135" cy="250" r="9"/><circle cx="125" cy="280" r="9"/>
    <circle cx="140" cy="305" r="9"/><circle cx="165" cy="305" r="9"/><circle cx="180" cy="285" r="9"/>
    <!-- Trục thẳng -->
    <circle cx="150" cy="405" r="10"/><circle cx="140" cy="435" r="11"/><circle cx="125" cy="460" r="13"/>
  </g>
</svg>'''),
        ("music_pastel_melody", "Nốt nhạc phấn màu Pastel", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <!-- Nốt vàng pastel -->
  <ellipse cx="160" cy="270" rx="38" ry="26" transform="rotate(-20 160 270)" fill="#FFF59D"/>
  <rect x="186" y="80" width="14" height="190" rx="7" fill="#FFF59D"/>
  <!-- Nốt hồng pastel -->
  <ellipse cx="320" cy="330" rx="38" ry="26" transform="rotate(-20 320 330)" fill="#F8BBD0"/>
  <rect x="346" y="140" width="14" height="190" rx="7" fill="#F8BBD0"/>
  <!-- Nốt xanh ngọc pastel -->
  <ellipse cx="410" cy="220" rx="30" ry="22" transform="rotate(-20 410 220)" fill="#B2DFDB"/>
  <rect x="432" y="70" width="12" height="150" rx="6" fill="#B2DFDB"/>
  <path d="M 444 70 C 475 80 485 110 475 140 C 470 120 455 95 444 90 Z" fill="#B2DFDB"/>
</svg>'''),
        ("music_sheet_corner", "Góc khuông nhạc cổ điển", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="vintagePaper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#EED9A4"/>
      <stop offset="100%" stop-color="#D7CCC8"/>
    </linearGradient>
  </defs>
  <!-- Mảnh giấy rách góc cổ điển -->
  <path d="M 0 0 L 380 0 C 330 80 340 180 280 250 C 220 310 130 320 0 380 Z" fill="url(#vintagePaper)"/>
  <!-- 5 dòng kẻ khuông nhạc cổ -->
  <line x1="20" y1="50" x2="320" y2="50" stroke="#795548" stroke-width="2"/>
  <line x1="20" y1="70" x2="300" y2="70" stroke="#795548" stroke-width="2"/>
  <line x1="20" y1="90" x2="280" y2="90" stroke="#795548" stroke-width="2"/>
  <line x1="20" y1="110" x2="260" y2="110" stroke="#795548" stroke-width="2"/>
  <line x1="20" y1="130" x2="240" y2="130" stroke="#795548" stroke-width="2"/>
  <!-- Nốt nhạc cổ điển in trên giấy -->
  <ellipse cx="90" cy="110" rx="12" ry="8" transform="rotate(-20 90 110)" fill="#4E342E"/>
  <line x1="100" y1="55" x2="100" y2="110" stroke="#4E342E" stroke-width="3"/>
  <ellipse cx="160" cy="90" rx="12" ry="8" transform="rotate(-20 160 90)" fill="#4E342E"/>
  <line x1="170" y1="35" x2="170" y2="90" stroke="#4E342E" stroke-width="3"/>
</svg>''')
    ],
    "audio": [
        ("audio_girl_headphones", "Cô gái thư giãn nghe nhạc", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 450" width="400" height="450">
  <!-- Mái tóc nâu bồng bềnh -->
  <path d="M 120 160 C 120 70 280 70 280 160 C 280 260 330 320 320 360 C 310 390 280 390 280 390 C 280 390 260 270 260 250 L 140 250 C 140 270 120 390 120 390 C 120 390 90 390 80 360 C 70 320 120 260 120 160 Z" fill="#8D6E63"/>
  <!-- Khuôn mặt dễ thương -->
  <ellipse cx="200" cy="200" rx="75" ry="70" fill="#FFECB3"/>
  <!-- Đôi mắt nhắm thư thái -->
  <path d="M 160 200 Q 175 210 190 200" fill="none" stroke="#5D4037" stroke-width="4" stroke-linecap="round"/>
  <path d="M 210 200 Q 225 210 240 200" fill="none" stroke="#5D4037" stroke-width="4" stroke-linecap="round"/>
  <!-- Má hồng e ấp -->
  <ellipse cx="160" cy="218" rx="14" ry="8" fill="#FFAB91" opacity="0.7"/>
  <ellipse cx="240" cy="218" rx="14" ry="8" fill="#FFAB91" opacity="0.7"/>
  <!-- Nụ cười mỉm nhỏ -->
  <path d="M 195 228 Q 200 234 205 228" fill="none" stroke="#5D4037" stroke-width="3" stroke-linecap="round"/>
  <!-- Tai nghe chụp tai xanh pastel -->
  <path d="M 115 170 C 115 90 285 90 285 170" fill="none" stroke="#5C6BC0" stroke-width="14"/>
  <rect x="95" y="160" width="35" height="70" rx="16" fill="#3949AB"/>
  <rect x="270" y="160" width="35" height="70" rx="16" fill="#3949AB"/>
  <!-- Áo phông cam đỏ ấm áp -->
  <path d="M 125 310 C 125 280 275 280 275 310 L 300 440 L 100 440 Z" fill="#FF7043"/>
</svg>'''),
        ("audio_studio_room", "Phòng thu âm & Ban nhạc", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <!-- Căn phòng sàn gỗ ấm cúng -->
  <rect width="500" height="260" fill="#FFF8E1"/>
  <rect y="260" width="500" height="140" fill="#FFB74D"/>
  <!-- Cửa sổ ánh sáng -->
  <rect x="30" y="30" width="90" height="110" fill="#B3E5FC" stroke="#81D4FA" stroke-width="6"/>
  <!-- Đàn Piano điện ở góc tường -->
  <rect x="180" y="140" width="140" height="90" rx="6" fill="#212121"/>
  <rect x="190" y="180" width="120" height="20" fill="#FFFFFF"/>
  <line x1="205" y1="230" x2="205" y2="280" stroke="#212121" stroke-width="6"/>
  <line x1="295" y1="230" x2="295" y2="280" stroke="#212121" stroke-width="6"/>
  <!-- Đàn Guitar dựa tường -->
  <ellipse cx="140" cy="270" rx="25" ry="35" fill="#E65100"/>
  <rect x="136" y="180" width="8" height="60" fill="#795548"/>
  <!-- Dàn trống nhạc Rock -->
  <circle cx="380" cy="280" r="45" fill="#E53935" stroke="#212121" stroke-width="5"/>
  <ellipse cx="440" cy="210" rx="35" ry="10" fill="#FFD54F"/>
  <line x1="440" y1="210" x2="440" y2="330" stroke="#757575" stroke-width="4"/>
</svg>''')
    ]
}

def main():
    json_path = os.path.join(DATA_DIR, "graphics.json")
    with open(json_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    existing_categories = catalog.get("categories", [])
    cat_by_name = {c["name"]: c for c in existing_categories}

    total_added = 0

    for folder_key, items in CUSTOM_SHOWCASE.items():
        folder_dir = os.path.join(PUBLIC_DIR, folder_key)
        os.makedirs(folder_dir, exist_ok=True)

        # Find category
        target_cat = None
        for c in existing_categories:
            if folder_key in ["vietnam", "music", "audio"] and (c["name"].startswith("Việt Nam") if folder_key == "vietnam" else c["name"].startswith("Âm nhạc") if folder_key == "music" else c["name"].startswith("Nhạc cụ")):
                target_cat = c
                break

        if not target_cat:
            continue

        existing_ids = {it["id"] for it in target_cat["items"]}

        for item_id, item_name, svg_data in items:
            file_name = f"{item_id}.svg"
            file_path = os.path.join(folder_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as f_svg:
                f_svg.write(svg_data.strip())

            full_id = f"{folder_key}_{item_id}"
            item_url = f"{REPO_URL_BASE}/{folder_key}/{file_name}"

            if full_id not in existing_ids:
                target_cat["items"].append({
                    "id": full_id,
                    "name": item_name,
                    "url": item_url,
                    "type": "svg"
                })
                existing_ids.add(full_id)
                total_added += 1

    catalog["total"] = sum(len(c["items"]) for c in existing_categories)
    catalog["categories"] = existing_categories

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    genoffice_json = r"c:\Users\Danh\Desktop\genofficepy\data\graphics.json"
    with open(genoffice_json, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"Added {total_added} showcase items! Total catalog: {catalog['total']}")

if __name__ == "__main__":
    main()
