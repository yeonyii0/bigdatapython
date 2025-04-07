import random
import time
import requests

# 멜론 100위 차트 API (2024년 기준, 변경될 가능성 있음)
url = "https://www.melon.com/chart/"

# 멜론은 User-Agent가 없으면 차단할 수 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text

    # BeautifulSoup으로 파싱
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # 제목과 가수 정보 찾기
    songs = soup.select("div.ellipsis.rank01 > span > a")  # 노래 제목
    artists = soup.select("div.ellipsis.rank02 > span")    # 가수 이름

    print("데이터를 가져오지 못했습니다.")

ai_song = random.choice(songs)

print(f"제가 추천한 곡은 {ai_song}입니다.")
