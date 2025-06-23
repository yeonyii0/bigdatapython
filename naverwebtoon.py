import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ✅ 드라이버 경로 입력 (자동으로 Chrome 드라이버를 다운로드하고 경로를 설정합니다.)
# driver_path = "C:/Users/User/Desktop/chromedriver.exe"  # 이전 경로는 주석 처리합니다.
# service = Service(driver_path)  # 이전 service 설정은 주석 처리합니다.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ✅ 요일 매핑
weekdays = {
    "1": "mon", "2": "tue", "3": "wed", "4": "thu", "5": "fri", "6": "sat", "7": "sun",
    "월": "mon", "화": "tue", "수": "wed", "목": "thu", "금": "fri", "토": "sat", "일": "sun"
}

# ✅ 요일 선택 안내
print("📆 요일을 선택하세요:")
print("1. 월  2. 화  3. 수  4. 목  5. 금  6. 토  7. 일")

# ✅ 사용자 요일 입력
weekday_input = input("\n🔢 요일 번호 또는 한글을 입력하세요: ").strip()

# ✅ 입력한 요일이 유효한지 확인
weekday_code = weekdays.get(weekday_input)
if not weekday_code:
    print("❌ 잘못된 요일 입력입니다.")
    driver.quit()
    exit()

# ✅ 해당 요일 웹툰 페이지로 이동
url = f"https://comic.naver.com/webtoon?week={weekday_code}"
driver.get(url)
time.sleep(2)

# ✅ 웹툰 목록 가져오기
webtoons = driver.find_elements(By.CSS_SELECTOR, "ul.img_list li a.title")
webtoon_data = []

for w in webtoons:
    title = w.text
    href = w.get_attribute("href")
    if title and href and (title, href) not in webtoon_data:
        webtoon_data.append((title.strip(), href.strip()))

# ✅ 웹툰 목록 출력
print(f"\n📚 {weekday_input}요일 웹툰 목록:")
for i, (title, _) in enumerate(webtoon_data):
    print(f"{i+1}. {title}")

# ✅ 사용자 선택
try:
    choice = int(input("\n🔢 보고 싶은 웹툰 번호를 입력하세요: ")) - 1
    if 0 <= choice < len(webtoon_data):
        selected = webtoon_data[choice]
        print(f"\n🎉 선택한 웹툰: {selected[0]}")
        print(f"🔗 링크: {selected[1]}")
    else:
        print("❌ 유효하지 않은 번호입니다.")
except ValueError:
    print("❌ 숫자를 입력해 주세요.")

# ✅ 종료
driver.quit()