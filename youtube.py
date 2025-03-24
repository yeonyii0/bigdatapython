import requests
from bs4 import BeautifulSoup

# 유튜브 급상승 페이지 URL
url = 'https://www.youtube.com/feed/trending'

# 헤더 정보 (유튜브에서 봇 차단을 피하기 위해 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 요청 보내기
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 급상승 동영상 정보 추출 (예: 제목, 링크)
video_items = soup.find_all('ytd-video-renderer')

# 데이터 출력
for video in video_items:
    title = video.find('a', {'id': 'video-title'})
    if title:
        video_title = title.text
        video_url = 'https://www.youtube.com' + title['href']
        print(f"제목: {video_title}\nURL: {video_url}\n")
