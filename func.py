import requests
from bs4 import BeautifulSoup
import random

def get_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.melon.com/"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"[💔 멜론 서버가 나랑 잠시 틀어졌어요... 상태 코드: {response.status_code}]")
        return []  # 차트 정보가 없으면 빈 리스트로 반환하고 함수 종료

    # 이후 코드는 멜론 차트 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    chart_rows = soup.select("tr.lst50") + soup.select("tr.lst100")

    result = []
    for row in chart_rows:
        rank = row.select_one("span.rank").text.strip()
        title = row.select_one("div.ellipsis.rank01 a").text.strip()
        singer = row.select_one("div.ellipsis.rank02 a").text.strip()
        result.append({
            "rank": rank,
            "title": title,
            "singer": singer
        })

    return result


def m100():
    chart = get_melon_chart()
    if not chart:  # ⛔ 차트를 못 가져왔을 경우
        return  # 아무것도 출력하지 않고 함수 종료!

    print("💚 선택해주셔서 감사합니다!")
    print("지금 가장 사랑받고 있는 실시간 TOP 100곡을 소개할게요!")
    print("[🎵 실시간 차트 TOP 100 보기]")
    for song in chart:
        print(f"{song['rank']}위: {song['title']} - {song['singer']}")

def m50():
    chart =get_melon_chart()
    if not chart:
        return

    print("💚 선택해주셔서 감사합니다!")
    print("지금 가장 사랑받고 있는 인기곡 TOP 50곡을 소개할게요!")
    print("[🎵 오늘의 인기곡 TOP 50]")
    for song in chart[:50]:
        print(f"{song['rank']}위: {song['title']} - {song['singer']}")

def m10():
    chart =get_melon_chart()
    if not chart:
        return

    print("💚 선택해주셔서 감사합니다!")
    print("지금 멜론에서 가장 뜨거운 인기곡 TOP 10을 소개할게요!🔥")
    print("[🔥 지금 가장 핫한 TOP 10]")
    for song in chart[:10]:
        print(f"{song['rank']}위: {song['title']} - {song['singer']}")

def m_random(user_name):
    chart =get_melon_chart()
    if not chart:
        return

    print("💚 선택해주셔서 감사합니다!")
    print(f"오늘 {user_name}님께 어울리는 노래를 하나 추천해드릴게요 🎧✨")
    print("------------------------------")
    
    song = random.choice(chart)
    print(f"💚 추천곡: {song['title']} - {song['singer']}")
    print("지금 한 번 들어보시는 건 어때요? 🎶")

def search_by_singer(name, user_name):
    chart = get_melon_chart()
    if not chart:
        return

    print("💚 입력해주셔서 감사합니다!")
    print(f"🔍 '{name}'의 곡을 찾아드릴게요!")
    print("------------------------------")

    found = False
    for song in chart:
        if name.lower() in song['singer'].lower():
            print(f"{song['rank']}위: {song['title']} - {song['singer']}")
            found = True

    if not found:
        print(f"😢 아쉽지만 '{name}'님의 곡은 현재 차트에 없어요...")
        print("🎤 다른 가수를 검색해보시겠어요?")
        again = input("👉 (네/아니오): ")

        if again.lower() in ['네', 'y', 'yes']:
            new_name = input("🔍 검색할 다른 가수 이름을 입력해주세요: ")
            search_by_singer(new_name, user_name)  # ✅ 여기서 user_name 꼭 같이 전달!
        else:
            print("💚 알겠습니다! 언제든 다시 검색해주세요 :)")

def save_to_file(user_name):
    chart = get_melon_chart()
    if not chart:
        return

    filename = "melon100.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for song in chart:
            f.write(f"{song['rank']}위: {song['title']} - {song['singer']}\n")

    print("💾 차트 저장이 완료되었어요!")
    print(f"{user_name}님을 위한 최신 멜론 TOP 100이 '{filename}'에 저장되었습니다 😊")
