import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'  # 멜론의 최신 차트 URL로 확인 필요

# 헤더 설정 (멜론은 User-Agent 확인을 통해 봇 접근을 차단할 수 있으므로 설정이 필요할 수 있음)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트의 노래 제목과 아티스트를 찾습니다.
#lst50 #frm > div > table > tbody #lst50
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))
    

print("====================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("====================")
# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")
# 여기서 부터는 n은 숫자(정수)

# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
    #수집한 데이터를 출력합니다.
    for i in range(100):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

#else:
#    print("1이 아닙니다")
# 만약에 2를 입력하면 
# 멜론 50 출력
elif n == "2":
    print('멜론 50')
    for i in range(50):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
elif n == "3":
    print('멜론 10')
    for i in range(10):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
elif n == "4":
    ai_song = random.choice(songs)
    print(f"오늘의 추천곡: {ai_song[1]}-{ai_song[2]}")
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야 함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
elif n == "5":
    artist = input("가수 이름을 입력하세요: ")
    if artist =="아이유":
        print("아이유 노래 리스트: 좋은날, 무릎, 밤편지")
    elif artist =="쏜애플":
        print("쏜애플 노래 리스트: 시퍼런 봄, 매미는 비가 와도 운다, 석류")
    elif artist =="에스파":
        print("에스파 노래 리스트: Whiplash, Next Level, Supernove")
    elif artist =="데이식스":
        print("데이식스 노래 리스트: 예뻤어, HAPPY, 한 페이지가 될 수 있게")
    elif artist =="아이브":
        print("아이브 노래 리스트: LOVE DIVE, After LIKE, I AM")
    else:
        print(f"{artist}의 노래 리스트를 찾을 수 없습니다")

# ...

else:
    print("1~5까지의 숫자를 입력하세요")