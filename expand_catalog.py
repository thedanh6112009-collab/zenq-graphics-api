import os
import json
import urllib.request
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
DATA_DIR = os.path.join(BASE_DIR, "data")
REPO_URL_BASE = "https://zenq-graphics-api-online.vercel.app"

LUCIDE_BASE = "https://raw.githubusercontent.com/lucide-icons/lucide/main/icons"

EXPANDED_CATEGORIES = [
    {
        "folder": "music",
        "name": "Âm nhạc & Giai điệu",
        "icons": [
            ("music", "Nốt nhạc đơn", None),
            ("music-2", "Nốt nhạc đôi", None),
            ("music-3", "Nốt nhạc cách điệu", None),
            ("music-4", "Ký hiệu âm nhạc", None),
            ("disc", "Đĩa than phát nhạc", None),
            ("disc-2", "Đĩa CD xoay", None),
            ("disc-3", "Đĩa hát Vinyl", None),
            ("radio", "Máy Radio bắt sóng", None),
            ("mic", "Microphone thu âm", None),
            ("mic-2", "Micro phòng thu", None),
            ("volume-2", "Âm lượng sống động", None),
            ("sliders", "Bàn trộn âm Mixer", None),
            ("speaker", "Loa thùng công suất", None),
            ("guitar", "Cần đàn Guitar", None),
            ("drum", "Dàn trống gõ", None),
            ("audio-lines", "Dải tần số âm thanh", None),
            ("audio-waveform", "Sóng âm Waveform", None),
            ("cassette-tape", "Băng từ Cassette", None),
        ]
    },
    {
        "folder": "education",
        "name": "Giáo dục & Học tập",
        "icons": [
            ("graduation-cap", "Mũ tốt nghiệp", None),
            ("book", "Quyển sách", None),
            ("book-open", "Sách mở trang", None),
            ("book-open-check", "Sách hoàn thành", None),
            ("book-marked", "Dấu trang sách", None),
            ("library", "Thư viện trường", None),
            ("pencil", "Bút chì phác thảo", None),
            ("pen", "Bút mực", None),
            ("pen-tool", "Bút vẽ Vector", None),
            ("highlighter", "Bút dạ quang nhớ dòng", None),
            ("eraser", "Gôm tẩy chì", None),
            ("ruler", "Thước kẻ học trò", None),
            ("school", "Ngôi trường học", None),
            ("award", "Bằng khen danh dự", None),
            ("medal", "Huy chương vinh danh", None),
            ("trophy", "Chiếc cúp vàng", None),
            ("microscope", "Kính hiển vi", None),
            ("test-tube", "Ống nghiệm", None),
            ("flask-conical", "Bình tam giác thí nghiệm", None),
            ("flask-round", "Bình cầu hóa học", None),
            ("globe", "Quả địa cầu học tập", None),
            ("backpack", "Ba lô đến trường", None),
        ]
    },
    {
        "folder": "business",
        "name": "Kinh doanh & Khởi nghiệp",
        "icons": [
            ("trending-up", "Tăng trưởng vọt", None),
            ("bar-chart-2", "Biểu đồ cột doanh thu", None),
            ("bar-chart-3", "Biểu đồ so sánh", None),
            ("pie-chart", "Biểu đồ tròn thị phần", None),
            ("line-chart", "Đường xu hướng", None),
            ("dollar-sign", "Đồng tiền Đô la", None),
            ("coins", "Chồng tiền vàng", None),
            ("wallet", "Ví tiền tài chính", None),
            ("credit-card", "Thẻ tín dụng", None),
            ("banknote", "Tờ tiền giấy", None),
            ("briefcase", "Cặp tài liệu doanh nghiệp", None),
            ("building", "Tòa cao ốc văn phòng", None),
            ("landmark", "Ngân hàng quốc gia", None),
            ("scale", "Cán cân công lý", None),
            ("handshake", "Hợp tác thành công", None),
            ("target", "Mục tiêu chiến lược", None),
            ("rocket", "Tên lửa bứt phá", None),
            ("lightbulb", "Ý tưởng sáng chế", None),
            ("receipt", "Hóa đơn thanh toán", None),
        ]
    },
    {
        "folder": "tech",
        "name": "Khoa học & Công nghệ",
        "icons": [
            ("cpu", "Chip vi xử lý CPU", None),
            ("bot", "Trí tuệ nhân tạo Bot AI", None),
            ("brain", "Tư duy nơ-ron", None),
            ("code", "Mã nguồn lập trình", None),
            ("terminal", "Dòng lệnh Terminal", None),
            ("database", "Cơ sở dữ liệu", None),
            ("server", "Máy chủ đám mây", None),
            ("hard-drive", "Ổ cứng lưu trữ", None),
            ("laptop", "Máy tính xách tay", None),
            ("smartphone", "Điện thoại thông minh", None),
            ("tablet", "Máy tính bảng", None),
            ("monitor", "Màn hình Retina", None),
            ("wifi", "Sóng mạng không dây", None),
            ("bluetooth", "Kết nối Bluetooth", None),
            ("satellite", "Vệ tinh không gian", None),
            ("satellite-dish", "Chảo vệ tinh", None),
            ("qr-code", "Mã quét QR", None),
            ("shield-check", "Bảo mật an toàn", None),
            ("circuit-board", "Bo mạch điện tử", None),
            ("zap", "Năng lượng điện cao áp", None),
        ]
    },
    {
        "folder": "food",
        "name": "Ẩm thực & Thức uống",
        "icons": [
            ("coffee", "Tách cà phê nóng", None),
            ("cup-soda", "Cốc nước giải khát", None),
            ("wine", "Ly rượu vang", None),
            ("beer", "Cốc bia tươi", None),
            ("cake", "Bánh ngọt sinh nhật", None),
            ("pizza", "Miếng Pizza", None),
            ("sandwich", "Bánh mì Sandwich kẹp", None),
            ("cookie", "Bánh quy sô-cô-la", None),
            ("apple", "Quả táo tươi", None),
            ("cherry", "Quả cherry mọng", None),
            ("banana", "Nải chuối chín", None),
            ("croissant", "Bánh sừng bò bơ", None),
            ("utensils", "Bộ dao nĩa", None),
            ("utensils-crossed", "Thìa nĩa đan chéo", None),
            ("chef-hat", "Nón đầu bếp", None),
        ]
    },
    {
        "folder": "social",
        "name": "Mạng xã hội & Biểu tượng cảm xúc",
        "icons": [
            ("heart", "Trái tim yêu thích", None),
            ("heart-handshake", "Gắn kết yêu thương", None),
            ("thumbs-up", "Ngón tay Like tuyệt vời", None),
            ("thumbs-down", "Ngón tay không thích", None),
            ("star", "Ngôi sao 5 cánh", None),
            ("star-half", "Nửa sao đánh giá", None),
            ("message-circle", "Bong bóng tin nhắn", None),
            ("message-square", "Khung chat trò chuyện", None),
            ("messages-square", "Nhiều cuộc trò chuyện", None),
            ("send", "Gửi tin nhắn đi", None),
            ("share-2", "Chia sẻ mạng xã hội", None),
            ("bell", "Chuông thông báo", None),
            ("bell-ring", "Chuông đang reo", None),
            ("bookmark", "Lưu bài viết", None),
            ("smile", "Mặt cười hạnh phúc", None),
            ("laugh", "Cười tươi rạng rỡ", None),
            ("sparkles", "Ánh sáng diệu kỳ", None),
            ("flame", "Ngọn lửa xu hướng Hot", None),
            ("crown", "Vương miện VIP", None),
            ("gift", "Hộp quà bất ngờ", None),
            ("badge-check", "Huy hiệu xác minh tích xanh", None),
        ]
    },
    {
        "folder": "health",
        "name": "Y tế, Sức khỏe & Thể thao",
        "icons": [
            ("activity", "Biểu đồ nhịp tim", None),
            ("heart-pulse", "Tim đập khỏe mạnh", None),
            ("stethoscope", "Ống nghe y tế", None),
            ("pill", "Viên thuốc con nhộng", None),
            ("cross", "Dấu thập y tế", None),
            ("ambulance", "Xe cấp cứu y tế", None),
            ("thermometer", "Nhiệt kế thủy ngân", None),
            ("syringe", "Ống tiêm vắc-xin", None),
            ("shield-plus", "Bảo vệ sức khỏe", None),
            ("dumbbell", "Tạ tập Gym thể hình", None),
            ("bike", "Xe đạp rèn luyện", None),
        ]
    }
]

def fetch_svg(icon_name):
    url = f"{LUCIDE_BASE}/{icon_name}.svg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode("utf-8")
            if "<svg" in content:
                content = content.replace('stroke="currentColor"', 'stroke="#1E293B"')
                if 'stroke="' not in content and '<svg' in content:
                    content = content.replace('<svg', '<svg stroke="#1E293B"')
                return content.strip()
    except Exception as e:
        pass
    return None

def main():
    json_path = os.path.join(DATA_DIR, "graphics.json")
    with open(json_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    existing_categories = catalog.get("categories", [])
    cat_by_name = {c["name"]: c for c in existing_categories}

    total_added = 0

    for cat_spec in EXPANDED_CATEGORIES:
        folder_key = cat_spec["folder"]
        folder_dir = os.path.join(PUBLIC_DIR, folder_key)
        os.makedirs(folder_dir, exist_ok=True)

        cat_title = cat_spec["name"]
        if cat_title not in cat_by_name:
            target_cat = {"name": cat_title, "items": []}
            existing_categories.append(target_cat)
            cat_by_name[cat_title] = target_cat
        else:
            target_cat = cat_by_name[cat_title]

        existing_item_ids = {it["id"] for it in target_cat["items"]}

        for icon_id, item_name, _ in cat_spec["icons"]:
            file_name = f"{icon_id}.svg"
            file_path = os.path.join(folder_dir, file_name)

            if not os.path.exists(file_path):
                svg_data = fetch_svg(icon_id)
                if svg_data:
                    with open(file_path, "w", encoding="utf-8") as f_out:
                        f_out.write(svg_data)
                else:
                    print(f"Skipped {icon_id} (not found)")
                    continue

            full_id = f"{folder_key}_{icon_id.replace('-', '_')}"
            item_url = f"{REPO_URL_BASE}/{folder_key}/{file_name}"

            if full_id not in existing_item_ids:
                target_cat["items"].append({
                    "id": full_id,
                    "name": item_name,
                    "url": item_url,
                    "type": "svg"
                })
                existing_item_ids.add(full_id)
                total_added += 1

    catalog["total"] = sum(len(c["items"]) for c in existing_categories)
    catalog["categories"] = existing_categories

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    genoffice_json = r"c:\Users\Danh\Desktop\genofficepy\data\graphics.json"
    with open(genoffice_json, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Successfully added {total_added} graphics icons!")
    print(f"Total categories: {len(existing_categories)}")
    print(f"Total catalog items: {catalog['total']}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
