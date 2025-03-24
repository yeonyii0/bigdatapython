from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 드라이버 설정 (Service 객체 사용)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 유튜브 인기 급상승 페이지 열기
driver.get("https://www.youtube.com/feed/trending")
time.sleep(5)  # 페이지 로딩 대기

# 인기 동영상 제목과 채널명 추출
videos = driver.find_elements(By.CSS_SELECTOR, "h3 a#video-title")
channels = driver.find_elements(By.CSS_SELECTOR, "ytd-channel-name a")

# 데이터 출력
for i in range(10):  # 상위 10개만 출력
    print(f"{i+1}위: {videos[i].text} - {channels[i].text}")

# 드라이버 종료
driver.quit()

