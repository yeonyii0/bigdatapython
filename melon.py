import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    """
    멜론 차트 페이지를 스크래핑하여 노래 순위, 제목, 가수 정보를 리스트로 반환하는 함수.
    """
    # 멜론 Top 100 차트 페이지 (접속 시점에 따라 URL이 변경될 수 있음)
    url = "https://www.melon.com/chart/index.htm"

    # 브라우저 헤더를 흉내내어 요청 (사이트 보안 정책을 우회하기 위해 종종 필요)
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/90.0.4430.212 Safari/537.36"),
        "Referer": "https://www.melon.com/",
    }

    # 요청 보내기
    res = requests.get(url, headers=headers)

    # 응답 상태 확인 (200이면 정상)
    if res.status_code != 200:
        print("멜론 페이지에 접속할 수 없습니다. (Status Code:", res.status_code, ")")
        return []

    # HTML 파싱
    soup = BeautifulSoup(res.text, "html.parser")

    # 멜론 차트 테이블에서 노래 정보가 담긴 태그를 찾습니다.
    # 2023년 기준, 멜론 차트 순위는 <tr class="lst50">, <tr class="lst100"> 형태로 나뉨
    chart_rows = soup.select("tr.lst50") + soup.select("tr.lst100")

    result = []

    # 각 곡 정보를 순회하며 추출
    for row in chart_rows:
        # 순위
        rank_tag = row.select_one("span.rank")
        rank = rank_tag.text.strip() if rank_tag else "N/A"

        # 곡 제목
        title_tag = row.select_one("div.ellipsis.rank01 a")
        title = title_tag.text.strip() if title_tag else "N/A"

        # 가수 정보
        singer_tag = row.select_one("div.ellipsis.rank02 a")
        singer = singer_tag.text.strip() if singer_tag else "N/A"

        # 앨범 정보
        album_tag = row.select_one("div.ellipsis.rank03 a")
        album = album_tag.text.strip() if album_tag else "N/A"

        # 결과를 리스트에 추가
        result.append({
            "rank": rank,
            "title": title,
            "singer": singer,
            "album": album
        })

    return result

def main():
    chart_data = get_melon_chart()
    if not chart_data:
        print("차트 정보를 가져오지 못했습니다.")
    else:
        # 간단하게 상위 10곡만 출력 예시
        for song in chart_data[:10]:
            print(f"{song['rank']}위: {song['title']} - {song['singer']} (앨범: {song['album']})")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    """
    멜론 차트 페이지를 스크래핑하여 노래 순위, 제목, 가수, 앨범 정보를 리스트로 반환하는 함수.
    """
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

    # 멜론 차트 테이블에서 노래 정보가 담긴 태그를 찾음
    chart_rows = soup.select("tr.lst50") + soup.select("tr.lst100")

    result = []

    for row in chart_rows:
        rank_tag = row.select_one("span.rank")
        title_tag = row.select_one("div.ellipsis.rank01 a")
        singer_tag = row.select_one("div.ellipsis.rank02 a")
        album_tag = row.select_one("div.ellipsis.rank03 a")

        rank = rank_tag.text.strip() if rank_tag else None
        title = title_tag.text.strip() if title_tag else None
        singer = singer_tag.text.strip() if singer_tag else None
        album = album_tag.text.strip() if album_tag else None

        result.append({
            "rank": rank,
            "title": title,
            "singer": singer,
            "album": album
        })

    return result

def main():
    chart_data = get_melon_chart()
    if not chart_data:
        print("차트 정보를 가져오지 못했습니다.")
    else:
        print("[멜론 Top 100 차트 정보]")
        for song in chart_data:
            # 랭크, 타이틀, 가수를 한 줄에 출력
            print(f"{song['rank']}위 | {song['title']} | {song['singer']}")

        # 필요하다면 앨범 정보도 함께 출력할 수 있습니다.
        # 예: print(f"{song['rank']}위 | {song['title']} - {song['singer']} (앨범: {song['album']})")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    """
    멜론 차트 페이지를 스크래핑하여
    노래 순위, 제목, 가수, 좋아요(Like) 수(예시)를 리스트로 반환하는 함수.
    """
    # 멜론 Top100 차트 주소 (2023년 기준)
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/90.0.4430.212 Safari/537.36"),
        "Referer": "https://www.melon.com/",
    }

    # 멜론 페이지 요청
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print("멜론 페이지에 접속할 수 없습니다. (Status Code:", res.status_code, ")")
        return []

    # HTML 파싱
    soup = BeautifulSoup(res.text, "html.parser")

    # 멜론 차트에서 곡 정보를 담은 태그를 탐색: lst50, lst100
    chart_rows = soup.select("tr.lst50") + soup.select("tr.lst100")

    result = []

    for row in chart_rows:
        # 순위
        rank_tag = row.select_one("span.rank")
        # 곡 제목
        title_tag = row.select_one("div.ellipsis.rank01 a")
        # 가수
        singer_tag = row.select_one("div.ellipsis.rank02 a")
        # 좋아요 수(좋아요 박스 안 .cnt 태그에 숫자만 들어있는 경우)
        like_tag = row.select_one("span.cnt")

        rank = rank_tag.get_text(strip=True) if rank_tag else None
        title = title_tag.get_text(strip=True) if title_tag else None
        singer = singer_tag.get_text(strip=True) if singer_tag else None

        # 예시) 좋아요 수는 "총건수 00,000" 형태일 수 있으므로 숫자만 추출
        if like_tag:
            like_text = like_tag.get_text(strip=True)
            # "총건수"라는 단어가 포함되어 있을 수 있으므로, 이를 제거/가공해 숫자만 남기기
            # 예) "총건수 30,949" -> "30949"
            like_number = like_text.replace("총건수", "").replace(",", "").strip()
        else:
            like_number = None

        # 수집한 정보 저장
        result.append({
            "rank": rank,
            "title": title,
            "singer": singer,
            "like_count": like_number
        })

    return result

def main():
    chart_data = get_melon_chart()
    if not chart_data:
        print("차트 정보를 가져오지 못했습니다.")
    else:
        print("[멜론 Top 100 차트 정보 (좋아요 수 포함)]")
        # 상위 10개만 예시 출력
        for song in chart_data[:10]:
            # 랭크, 제목, 가수, 좋아요 수를 한 줄에 출력
            print(f"{song['rank']}위 | {song['title']} | {song['singer']} | 좋아요: {song['like_count']}")

if __name__ == "__main__":
    main()
    