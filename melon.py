from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome(ChromeDriverManager().install())

# 멜론 차트 페이지 열기
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(5)  # 페이지 로딩 대기

# 순위, 노래 제목, 아티스트 추출
titles = driver.find_elements(By.CSS_SELECTOR, "tr .rank01 a")
artists = driver.find_elements(By.CSS_SELECTOR, "tr .rank02 a")

# 데이터 출력
for i in range(10):  # 상위 10위만 출력
    print(f"{i+1}위: {titles[i].text} - {artists[i].text}")

# 드라이버 종료
driver.quit()
