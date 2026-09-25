import requests

# 4 link playlist nguồn
links = [
    "https://bdshtp.github.io/gavang_playlist/gavang.m3u",
    "https://bdshtp.github.io/cola_playlist/cola.m3u",
    "https://bdshtp.github.io/biaom_playlist/biaom.m3u",
    "https://bdshtp.github.io/khandai_playlist/khandai.m3u",
]

OUTPUT_FILE = "allfb.m3u"

def fetch_and_combine():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("#EXTM3U\n")
        for idx, url in enumerate(links, start=1):
            try:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
                lines = resp.text.splitlines()
                for line in lines:
                    # bỏ header thừa
                    if not line.startswith("#EXTM3U"):
                        # thêm group-title để phân biệt nguồn
                        if line.startswith("#EXTINF"):
                            line = line.replace(
                                "#EXTINF:-1",
                                f'#EXTINF:-1 group-title="Source {idx}"'
                            )
                        out.write(line + "\n")
                print(f"✅ Đã gộp playlist từ {url}")
            except Exception as e:
                print(f"⚠️ Lỗi khi tải {url}: {e}")

if __name__ == "__main__":
    fetch_and_combine()
    print(f"🎉 Đã tạo {OUTPUT_FILE}")
