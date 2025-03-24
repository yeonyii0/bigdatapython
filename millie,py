import requests
from bs4 import BeautifulSoup

# 밀리의 서재 순위 페이지 URL
url = 'https://www.millie.co.kr/books/ranking'  # 실제 밀리의 서재 순위 페이지 URL로 변경 필요

# 요청 보내기
response = requests.get(url)

# 응답 상태 코드 확인
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 책 순위 목록 추출 (실제 HTML 구조에 맞게 수정 필요)
    book_items = soup.find_all('div', {'class': 'book-item'})  # 실제 책 아이템 클래스로 수정 필요

    # 책 제목과 링크 출력
    for book in book_items:
        title = book.find('a', {'class': 'book-title'})  # 제목이 있는 태그
        if title:
            book_title = title.text.strip()
            book_url = 'https://www.millie.co.kr' + title['href']
            print(f"제목: {book_title}\nURL: {book_url}\n")
else:
    print("밀리의 서재 페이지를 가져오는 데 실패했습니다.")
