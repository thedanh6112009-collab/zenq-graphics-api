import os
import json
import urllib.request
import re

CATEGORIES = [
    {
        "folder": "cloud",
        "name": "Mây & Khí quyển",
        "items": [
            ("cloud", "Mây trắng"),
            ("cloudy", "Nhiều mây"),
            ("cloud-sun", "Mây và mặt trời"),
            ("cloud-moon", "Mây và trăng đêm"),
            ("cloud-rain", "Mây mưa"),
            ("cloud-snow", "Mây tuyết rơi"),
            ("cloud-lightning", "Mây sấm sét"),
            ("cloud-fog", "Mây mù sương"),
            ("cloud-drizzle", "Mây mưa phùn"),
            ("cloud-hail", "Mây mưa đá"),
            ("cloud-download", "Tải về đám mây"),
            ("cloud-upload", "Tải lên đám mây"),
            ("cloud-cog", "Cấu hình đám mây"),
            ("cloud-moon-rain", "Mưa đêm"),
        ]
    },
    {
        "folder": "rain",
        "name": "Mưa & Giông bão",
        "items": [
            ("cloud-rain-wind", "Mưa bão gió lốc"),
            ("cloud-sun-rain", "Mưa rào có nắng"),
            ("umbrella", "Chiếc ô che mưa"),
            ("rainbow", "Cầu vồng"),
            ("wind", "Cơn gió thổi"),
            ("snowflake", "Bông tuyết trắng"),
            ("sun", "Mặt trời"),
            ("sun-medium", "Ánh nắng vàng"),
            ("sun-dim", "Nắng dịu"),
            ("thermometer", "Nhiệt kế"),
            ("thermometer-sun", "Nhiệt độ nóng"),
            ("thermometer-snowflake", "Nhiệt độ lạnh giá"),
            ("zap", "Tia chớp sấm sét"),
            ("tornado", "Cơn lốc xoáy"),
        ]
    },
    {
        "folder": "water",
        "name": "Sông ngòi & Nguồn nước",
        "items": [
            ("droplet", "Giọt nước"),
            ("droplets", "Nhiều giọt nước"),
            ("waves", "Sóng sông nước"),
            ("ship", "Thuyền lướt sóng"),
            ("anchor", "Mỏ neo bến sông"),
            ("fish", "Cá sông"),
            ("fish-symbol", "Biểu tượng loài cá"),
            ("life-buoy", "Phao cứu sinh"),
            ("bath", "Bồn nước thư giãn"),
            ("glass-water", "Ly nước mát"),
            ("cup-soda", "Đồ uống giải khát"),
            ("fuel", "Nhiên liệu lỏng"),
            ("droplet-percent", "Độ ẩm nước"),
            ("sailboat", "Thuyền buồm trên sông"),
        ]
    },
    {
        "folder": "nature",
        "name": "Thiên nhiên & Núi rừng",
        "items": [
            ("mountain", "Núi non trùng điệp"),
            ("mountain-snow", "Núi tuyết"),
            ("trees", "Rừng cây xanh"),
            ("sunset", "Hoàng hôn"),
            ("sunrise", "Bình minh"),
            ("compass", "La bàn định hướng"),
            ("tent", "Lều cắm trại"),
            ("flame", "Ngọn lửa ấm"),
            ("moon", "Mặt trăng"),
            ("moon-star", "Trăng và sao"),
            ("sparkles", "Ánh sáng lấp lánh"),
            ("sparkle", "Ngôi sao tỏa sáng"),
            ("telescope", "Kính thiên văn"),
            ("globe", "Quả địa cầu"),
            ("earth", "Trái Đất xanh"),
        ]
    },
    {
        "folder": "plants",
        "name": "Lá cây & Cây cỏ",
        "items": [
            ("leaf", "Chiếc lá xanh"),
            ("flower", "Bông hoa tươi"),
            ("flower-2", "Bông hoa nở rộ"),
            ("clover", "Cỏ 4 lá may mắn"),
            ("tree-pine", "Cây thông"),
            ("tree-deciduous", "Cây cổ thụ"),
            ("tree-palm", "Cây cọ dừa"),
            ("sprout", "Mầm cây đâm chồi"),
            ("wheat", "Bông lúa mạch"),
            ("apple", "Quả táo ngọt"),
            ("cherry", "Quả anh đào"),
            ("grape", "Chùm nho"),
            ("citrus", "Lát cam tươi"),
            ("carrot", "Củ cà rốt"),
            ("nut", "Hạt mầm"),
        ]
    },
    {
        "folder": "countries",
        "name": "Đất nước & Địa danh",
        "items": [
            ("flag", "Lá cờ quốc gia"),
            ("flag-triangle-right", "Cờ hiệu"),
            ("map", "Bản đồ thế giới"),
            ("map-pin", "Điểm đánh dấu vị trí"),
            ("map-pinned", "Ghim địa điểm"),
            ("navigation", "Điều hướng hành trình"),
            ("landmark", "Địa danh thắng cảnh"),
            ("castle", "Lâu đài kiến trúc"),
            ("building", "Tòa nhà cao tầng"),
            ("hotel", "Khách sạn"),
            ("church", "Công trình tôn giáo"),
            ("factory", "Khu công nghiệp"),
            ("store", "Cửa hàng"),
            ("school", "Trường học"),
            ("plane", "Chuyến bay quốc tế"),
        ]
    },
    {
        "folder": "people",
        "name": "Con người & Nghề nghiệp",
        "items": [
            ("user", "Người dùng"),
            ("users", "Nhóm người"),
            ("user-check", "Người dùng xác thực"),
            ("user-plus", "Thêm người"),
            ("user-round", "Hình đại diện"),
            ("contact", "Danh bạ"),
            ("graduation-cap", "Sinh viên cử nhân"),
            ("briefcase", "Nhân viên công sở"),
            ("stethoscope", "Bác sĩ y tế"),
            ("heart-handshake", "Bắt tay hợp tác"),
            ("award", "Giải thưởng vinh danh"),
            ("medal", "Huy chương trao tặng"),
            ("trophy", "Cúp vinh quang"),
            ("heart", "Tình cảm con người"),
            ("handshake", "Giao lưu hữu nghị"),
        ]
    },
    {
        "folder": "tools",
        "name": "Đồ vật & Dụng cụ",
        "items": [
            ("wrench", "Cờ lê sửa chữa"),
            ("hammer", "Búa đóng đinh"),
            ("scissors", "Kéo cắt thủ công"),
            ("pen-tool", "Bút vẽ vector"),
            ("pencil", "Bút chì phác thảo"),
            ("brush", "Cọ quét sơn"),
            ("paint-bucket", "Thùng sơn"),
            ("palette", "Bảng pha màu"),
            ("ruler", "Thước kẻ"),
            ("calculator", "Máy tính cầm tay"),
            ("camera", "Máy chụp ảnh"),
            ("clock", "Đồng hồ treo tường"),
            ("watch", "Đồng hồ đeo tay"),
            ("bell", "Chuông báo"),
            ("key", "Chìa khóa"),
            ("lock", "Ổ khóa bảo mật"),
            ("flashlight", "Đèn pin"),
            ("lightbulb", "Bóng đèn sáng tạo"),
            ("glasses", "Kính mắt"),
            ("book-open", "Sách mở"),
            ("coffee", "Tách cà phê"),
            ("shield", "Khiên bảo vệ"),
        ]
    },
    {
        "folder": "transport",
        "name": "Phương tiện giao thông",
        "items": [
            ("car", "Xe ô tô"),
            ("car-front", "Đầu xe ô tô"),
            ("bus", "Xe buýt"),
            ("bus-front", "Đầu xe buýt"),
            ("truck", "Xe tải"),
            ("bike", "Xe đạp thể thao"),
            ("train-front", "Tàu hỏa"),
            ("plane-takeoff", "Máy bay cất cánh"),
            ("plane-landing", "Máy bay hạ cánh"),
            ("rocket", "Tên lửa"),
            ("sailboat", "Thuyền buồm"),
            ("navigation-2", "Mũi tên định hướng"),
            ("gauge", "Đồng hồ tốc độ"),
            ("traffic-cone", "Cọc phân làn giao thông"),
            ("cable-car", "Cáp treo du lịch"),
        ]
    },
    {
        "folder": "animals",
        "name": "Thế giới động vật",
        "items": [
            ("bird", "Chim muông"),
            ("cat", "Mèo con"),
            ("dog", "Cún con"),
            ("rabbit", "Thỏ trắng"),
            ("fish", "Cá bơi"),
            ("bug", "Bọ cánh cứng"),
            ("snail", "Ốc sên"),
            ("paw-print", "Dấu chân thú"),
            ("feather", "Lông vũ chim"),
            ("egg", "Trứng ấp"),
            ("bone", "Khúc xương"),
            ("worm", "Sâu bọ"),
            ("shell", "Vỏ sò biển"),
            ("turtle", "Rùa biển"),
        ]
    }
]

# Fallback SVG definitions for any icon that cannot be downloaded from primary source
FALLBACKS = {
    "waves": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/></svg>',
    "droplet-percent": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/><path d="m9 17 6-6"/><circle cx="9.5" cy="11.5" r=".5" fill="#1E293B"/><circle cx="14.5" cy="16.5" r=".5" fill="#1E293B"/></svg>',
    "handshake": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m11 17 2 2a1 1 0 0 0 1.4 0l4.3-4.3a1 1 0 0 0 0-1.4l-2.6-2.6a1 1 0 0 0-1.4 0L13 12"/><path d="m18 10 3.5-3.5a1 1 0 0 0 0-1.4l-2.6-2.6a1 1 0 0 0-1.4 0L14 6"/><path d="m2 14 3.5 3.5a1 1 0 0 0 1.4 0L11 13.4"/><path d="m6 10-3.5 3.5a1 1 0 0 0 0 1.4l2.6 2.6a1 1 0 0 0 1.4 0L10 14"/></svg>',
    "turtle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="12" rx="6" ry="5"/><path d="M12 7v10"/><path d="M7 12h10"/><path d="M18 12c1.5 0 3-.5 3-2s-1.5-2-3-2"/><path d="M6 12c-1.5 0-3-.5-3-2s1.5-2 3-2"/><path d="m16 16 2 2"/><path d="m8 16-2 2"/><path d="m16 8 2-2"/><path d="m8 8-2-2"/></svg>'
}

def fetch_svg_content(icon_id):
    sources = [
        f"https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/{icon_id}.svg",
        f"https://raw.githubusercontent.com/twbs/icons/main/icons/{icon_id}.svg",
        f"https://raw.githubusercontent.com/feathericons/feather/master/icons/{icon_id}.svg"
    ]
    for url in sources:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = resp.read().decode("utf-8")
                if "<svg" in data and ("<path" in data or "<circle" in data or "<rect" in data):
                    return data
        except Exception:
            pass
    if icon_id in FALLBACKS:
        return FALLBACKS[icon_id]
    return None

def normalize_svg(svg_content):
    # Ensure stroke is a crisp dark slate #1E293B by default if stroke is currentColor
    svg_content = svg_content.replace('stroke="currentColor"', 'stroke="#1E293B"')
    if 'stroke="' not in svg_content and '<svg' in svg_content:
        svg_content = svg_content.replace('<svg', '<svg stroke="#1E293B"')
    return svg_content.strip()

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    public_dir = os.path.join(base_dir, "public")
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    catalog_categories = []
    total_downloaded = 0

    repo_raw_base = "https://raw.githubusercontent.com/thedanh6112009-collab/zenq-graphics-api/main/public"

    for cat in CATEGORIES:
        folder_name = cat["folder"]
        category_title = cat["name"]
        cat_dir = os.path.join(public_dir, folder_name)
        os.makedirs(cat_dir, exist_ok=True)

        cat_items = []
        for icon_id, vi_name in cat["items"]:
            file_name = f"{icon_id}.svg"
            file_path = os.path.join(cat_dir, file_name)

            svg_text = None
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    svg_text = f.read()

            if not svg_text or len(svg_text) < 30:
                print(f"Fetching [{folder_name}] {icon_id}...")
                raw_svg = fetch_svg_content(icon_id)
                if raw_svg:
                    svg_text = normalize_svg(raw_svg)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(svg_text)
                    print(f"  -> Saved {file_name}")
                else:
                    print(f"  -> FAILED to find {icon_id}!")
                    continue

            total_downloaded += 1
            item_id = f"{folder_name}_{icon_id.replace('-', '_')}"
            item_url = f"{repo_raw_base}/{folder_name}/{file_name}"
            cat_items.append({
                "id": item_id,
                "name": vi_name,
                "url": item_url,
                "type": "svg"
            })

        if cat_items:
            catalog_categories.append({
                "name": category_title,
                "items": cat_items
            })

    catalog_data = {
        "version": "2.0",
        "total": total_downloaded,
        "categories": catalog_categories
    }

    json_path = os.path.join(data_dir, "graphics.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"COMPLETED: Downloaded & organized {total_downloaded} SVG graphics!")
    print(f"Categories: {len(catalog_categories)}")
    print(f"Catalog saved to: {json_path}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
