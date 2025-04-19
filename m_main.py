import func

user_name = input("🌸 먼저 당신의 이름을 알려주세요: ")

# 사용자의 입력을 받아서 멜론 차트 출력 프로그램 만들기
# 각각 기능(함수)을 만들어서 메인 파일에서 코드 작성
print("==============================")
print(f"\n{user_name}님, 멜론 차트 서비스에 오신 걸 환영합니다!")
print("----------------------------------------")
print("1. 실시간 차트 TOP 100 보기")
print("2. 오늘의 인기곡 TOP 50")
print("3. 지금 가장 핫한 TOP 10")
print("4. AI가 골라주는 오늘의 추천곡")
print("5. 가수 곡 검색")
print("6. 차트 데이터를 파일로 저장")
print("----------------------------------------")
print("원하시는 기능을 선택해주세요 :)")
print("==============================")
#번호 선택
choice = input("👉 원하는 번호를 입력하세요:")

if choice == "1":
    func.m100()
elif choice == "2":
    func.m50()
elif choice == "3":
    func.m10()
elif choice == "4":
    func.m_random(user_name)
elif choice == "5":
    name = input("🔍 검색할 가수 이름을 입력하세요: ")
    func.search_by_singer(name, user_name)
elif choice == "6":
    func.save_to_file(user_name)
else:
    print("❗ 숫자를 잘못 입력하신 것 같아요! 1번부터 6번 중에서 골라주세요!")

