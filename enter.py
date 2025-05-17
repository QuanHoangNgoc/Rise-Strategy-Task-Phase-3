INPUT_DATA = 'craw_data/input_data.csv'

province_path = 'output/scored_provinces.csv'
region_path = 'output/scored_regions.csv'

USE_MINMAX_SCORE = True

regions_data = {
    "Northern Highlands": [
        "Phu Tho", "Thai Nguyen", "Bac Giang", "Son La", "Lao Cai", "Hoa Binh",
        "Lang Son", "Yen Bai", "Ha Giang", "Tuyen Quang", "Lai Chau", "Bac Kan",
        "Cao Bang", "Dien Bien"
    ],
    "Mekong River Delta": [
        "Dong Thap", "Can Tho", "An Giang", "Tien Giang", "Kien Giang", "Ben Tre",
        "Long An", "Tra Vinh", "Vinh Long", "Ca Mau", "Soc Trang", "Hau Giang",
        "Bac Lieu"
    ],
    "Southeast": [
        "Dong Nai", "Binh Duong", "Ba Ria - Vung Tau (BR - VT)", "Binh Phuoc",
        "Tay Ninh", "Ho Chi Minh City (HCMC)"
    ],
    "Central Highlands": [
        "Lam Dong", "Dak Lak", "Gia Lai", "Dak Nong", "Kon Tum"
    ],
    "Central Coast": [
        "Thanh Hoa", "Nghe An", "Da Nang", "Khanh Hoa", "Thua Thien Hue (TT-Hue)",
        "Binh Dinh", "Quang Nam", "Quang Ngai", "Binh Thuan", "Ha Tinh",
        "Ninh Thuan", "Quang Tri", "Phu Yen", "Quang Binh"
    ],
    "Red River Delta": [
        "Hai Phong", "Hai Duong", "Quang Ninh", "Bac Ninh", "Thai Binh",
        "Vinh Phuc", "Nam Dinh", "Hung Yen", "Ninh Binh", "Ha Nam", "Ha Noi"
    ]
}

manual_name_mapping = {
    "Thái Bình": "Thai Binh",
    "Hà Giang": "Ha Giang",
    "Cao Bằng": "Cao Bang",
    "Điện Biên": "Dien Bien",
    "Bến Tre": "Ben Tre",
    "Nam Định": "Nam Dinh",
    "Sóc Trăng": "Soc Trang",
    "Lai Châu": "Lai Chau",
    "Lạng Sơn": "Lang Son",
    "Hà Nam": "Ha Nam",
    "Bắc Kạn": "Bac Kan",
    "Tuyên Quang": "Tuyen Quang",
    "Sơn La": "Son La",
    "Bạc Liêu": "Bac Lieu",
    "Nghệ An": "Nghe An",
    # Đặc biệt: Huế trong CSV -> Thua Thien Hue trong regions_data
    "Huế": "Thua Thien Hue (TT-Hue)",
    "An Giang": "An Giang",
    "Quảng Bình": "Quang Binh",
    "Yên Bái": "Yen Bai",
    "Phú Yên": "Phu Yen",
    "Cà Mau": "Ca Mau",
    "Gia Lai": "Gia Lai",
    "Đắk Lắk": "Dak Lak",
    "Vĩnh Long": "Vinh Long",
    "Tiền Giang": "Tien Giang",
    "Phú Thọ": "Phu Tho",
    "Đồng Tháp": "Dong Thap",
    "Đắk Nông": "Dak Nong",
    "Hoà Bình": "Hoa Binh",
    "Kon Tum": "Kon Tum",
    "Kiên Giang": "Kien Giang",
    "Hậu Giang": "Hau Giang",
    "Quảng Nam": "Quang Nam",
    "Thanh Hóa": "Thanh Hoa",
    "Hà Tĩnh": "Ha Tinh",
    "Bình Định": "Binh Dinh",
    "Quảng Trị": "Quang Tri",
    "Bình Thuận": "Binh Thuan",
    "Lào Cai": "Lao Cai",
    "Trà Vinh": "Tra Vinh",
    "Khánh Hòa": "Khanh Hoa",
    "Ninh Thuận": "Ninh Thuan",
    "TP. Cần Thơ": "Can Tho",          # Đặc biệt
    "Tây Ninh": "Tay Ninh",
    "Lâm Đồng": "Lam Dong",
    "Bắc Giang": "Bac Giang",
    "Ninh Bình": "Ninh Binh",
    "Quảng Ngãi": "Quang Ngai",
    "Long An": "Long An",
    "Hải Dương": "Hai Duong",
    "Bình Phước": "Binh Phuoc",
    "Hưng Yên": "Hung Yen",
    "Đà Nẵng": "Da Nang",
    "Thái Nguyên": "Thai Nguyen",
    "Vĩnh Phúc": "Vinh Phuc",
    "Đồng Nai": "Dong Nai",
    "Bắc Ninh": "Bac Ninh",
    "Hà Nội": "Ha Noi",
    "Thành phố Hồ Chí Minh": "Ho Chi Minh City (HCMC)",  # Đặc biệt
    "Bình Dương": "Binh Duong",
    "Hải Phòng": "Hai Phong",
    "Quảng Ninh": "Quang Ninh",
    "Bà Rịa – Vũng Tàu": "Ba Ria - Vung Tau (BR - VT)"  # Đặc biệt
}


def get_map_provice_region():
    province_to_region_map_raw = {}
    for region, provinces in regions_data.items():
        for province in provinces:
            province_to_region_map_raw[province] = region

    final_province_to_region_map = {}
    for csv_name, lookup_name in manual_name_mapping.items():
        if lookup_name in province_to_region_map_raw:
            final_province_to_region_map[csv_name] = province_to_region_map_raw[lookup_name]
        else:
            print(
                f"[!] WAR: Dont find region for province '{lookup_name}' ('{csv_name}').")

    return final_province_to_region_map


PROVICE_TO_REGION_MAP = get_map_provice_region()
# print(PROVICE_TO_REGION_MAP)
