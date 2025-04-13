import requests
from bs4 import BeautifulSoup
import random

def get_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/90.0.4430.212 Safari/537.36"),
        "Referer": "https://www.melon.com/",
    }

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print("멜론 페이지에 접속할 수 없습니다. (Status Code:", res.status_code, ")")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    chart_rows = soup.select("tr.lst50") + soup.select("tr.lst100")

    result = []
    for row in chart_rows:
        rank_tag = row.select_one("span.rank")
        title_tag = row.select_one("div.ellipsis.rank01 a")
        singer_tag = row.select_one("div.ellipsis.rank02 a")
        album_tag = row.select_one("div.ellipsis.rank03 a")
        like_tag = row.select_one("span.cnt")

        rank = rank_tag.get_text(strip=True) if rank_tag else "N/A"
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        singer = singer_tag.get_text(strip=True) if singer_tag else "N/A"
        album = album_tag.get_text(strip=True) if album_tag else "N/A"

        if like_tag:
            like_text = like_tag.get_text(strip=True)
            like_number = like_text.replace("총건수", "").replace(",", "").strip()
        else:
            like_number = "N/A"

        result.append({
            "rank": rank,
            "title": title,
            "singer": singer,
            "album": album,
            "like_count": like_number
        })

    return result

def main():
    chart_data = get_melon_chart()
    if not chart_data:
        print("차트 정보를 가져오지 못했습니다.")
    else:
        print("[🎵 멜론 Top 100 차트 중 랜덤 추천 🎲]")
        random_song = random.choice(chart_data)
        print(f"오늘의 추천곡은...\n{random_song['title']} - {random_song['singer']} 🎧")
        print(f"(앨범: {random_song['album']} | 좋아요 수: {random_song['like_count']})\n")

        print("[전체 차트 보기]")
        for song in chart_data:
            print(f"{song['rank']}위: {song['title']} - {song['singer']} (앨범: {song['album']})")

if __name__ == "__main__":
    main()
