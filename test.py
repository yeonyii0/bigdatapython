# 감정 리스트
moods = {
    "1": "마음이 조용해지고 싶은 날",
    "2": "속이 답답하고 기분전환이 필요한 날",
    "3": "누군가와 따뜻한 이야기를 나누고 싶은 날",
    "4": "설레는 기분을 느끼고 싶은 날",
    "5": "감정이 무뎌진 것 같고 울고 싶은 날",
    "6": "혼자 있고 싶은 날",
    "7": "에너지가 넘치고 웃고 싶은 날",
    "8": "집중하고 몰입하고 싶은 날",
    "9": "아무 생각 없이 시간 때우고 싶은 날",
    "10": "그냥 아무거나 보고 싶은 날",
    "11": "저한테 맞는 기분이 없어요 더 많은 감정을 보여주세요. ➕"
}

extra_moods = {
    "12": "아무 이유 없이 외로운 날",
    "13": "가슴이 몽글몽글해지는 이야기가 보고 싶은 날",
    "14": "차분히 무언가에 몰입하고 싶은 날",
    "15": "인생의 의미가 살짝 헷갈리는 날",
    "16": "나를 다독여주는 이야기와 만나고 싶은 날",
    "17": "밤새워 보고 싶은 시리즈가 필요한 날",
    "18": "친구랑 같이 보기 좋은 콘텐츠를 찾는 날",
    "19": "연인과 분위기 좋은 콘텐츠를 고르고 싶은 날",
    "20": "가족이랑 함께 웃을 수 있는 걸 보고 싶은 날",
    "21": "비 오는 날, 창 밖 보며 보고 싶은 콘텐츠가 궁금한 날",
    "22": "몽환적인 분위기의 작품이 보고 싶은 날",
    "23": "잔혹하거나 현실적인 이야기가 당기는 날",
    "24": "무대 위 공연 같은 몰입감을 느끼고 싶은 날",
    "25": "아트 감성 충만한 인디 콘텐츠가 궁금한 날",
    "26": "영상미가 예쁜 작품을 찾고 싶은 날",
}

username = input("당신의 이름 또는 닉네임을 알려주세요😊: ")
ott_platforms = [
    "넷플릭스",  
    "디즈니+", 
    "웨이브", 
    "티빙", 
    "라프텔",]
ott_platforms.append("제가 찾는 플랫폼이 없어요😢")

print(f"\n🎥 {username}님께 최적화된 콘텐츠를 추천해드리기 위해,")
print("시청 가능한 OTT 플랫폼을 선택해주세요!\n")
for idx, p in enumerate(ott_platforms, 1):
    print(f"{idx}. {p}")

while True:
    user_input = input("\n해당 번호를 모두 입력해주세요 \n*복수선택 가능해요 (예:1,3)*: ")
    choices = [i.strip() for i in user_input.split(",")]
    
    if all(i.isdigit() and 1 <= int(i) <= len(ott_platforms) for i in choices):
        selected_indexes = [int(i) for i in choices]
        break
    else:
        print("\n숫자를 잘못 입력하셨어요.")
        print("1번 ~ 6번에서 골라 다시 입력해 주세요. 제가 기다리고 있을게요! 😊")
        print("*복수선택 가능합니다*")

# 체크: '찾는 플랫폼 없음' 선택 여부
has_missing_option = len(ott_platforms) in selected_indexes

# 최종 선택 목록
selected = [ott_platforms[i-1] for i in selected_indexes if i != len(ott_platforms)]

if selected:
    print(f"\n✅ {username}님이 선택한 OTT 플랫폼:")
    for p in selected:
        print(f"👉 {p}")

if has_missing_option:
    print("\n원하는 플랫폼이 목록에 없었군요...")
    print("아쉽게 해드려서 정말 죄송합니다🙇")
    print("무드픽은 더 다양한 콘텐츠와 플랫폼을 담기 위해 열심히 준비 중이에요.")
    print("조금만 기다려주시면, 더 만족스러운 무드픽이 되어 돌아올게요 💙")

    print("\n오늘은 어떤 기분이신가요? 😊\n")
for key, value in moods.items():
    print(f"{key}. {value}")

while True:
    mood_input = input("\n당신의 오늘 기분에 가장 가까운 번호를 입력해주세요: ")

    if mood_input == "11":
        print("\n💡 더 다양한 감정을 보여드릴게요!\n")
        for key, value in extra_moods.items():
            print(f"{key}. {value}")
        mood_input = input("\n그중 하나를 선택해주세요 (예: 13): ")

    if mood_input in moods or mood_input in extra_moods:
        selected_mood = moods.get(mood_input, extra_moods.get(mood_input))
        print(f"\n✨ 선택된 감정: {selected_mood}")
        break
    else:
        print("\n⚠️ 입력이 올바르지 않아요. 다시 한 번 번호만 입력해주세요.")





        from genre_mapper import get_genre_codes_by_mood, moods, extra_moods
import requests
import random

ott_to_tmdb_id = {
    "넷플릭스": 8,
    "쿠팡플레이스": 356,
    "티빙": 619,
    "웨이브": 356,
    "디즈니+": 337,
    "라프텔": 675,
}

def get_or_recommendations(genre_codes, ott_ids, content_type="movie", n=5):
    if content_type == "movie":
        url = "https://api.themoviedb.org/3/discover/movie"
    else:
        url = "https://api.themoviedb.org/3/discover/tv"

    TMDB_API_KEY = "f9b4e7a89ca50f7b19b1c9a48e13bc04"
    params_base = {
        "api_key": TMDB_API_KEY,
        "with_watch_providers": "|".join(str(i) for i in ott_ids),
        "watch_region": "KR",
        "region": "KR",
        "language": "ko-KR",
        "sort_by": "popularity.desc",
        "page": 1,
    }
    all_results = []
    for genre in genre_codes:
        params = params_base.copy()
        params["with_genres"] = str(genre)
        res = requests.get(url, params=params)
        data = res.json()
        all_results += data.get("results", [])
    # 중복 제거 (id 기준)
    unique = {item['id']: item for item in all_results}.values()
    picks = random.sample(list(unique), min(n, len(unique)))
    for idx, item in enumerate(picks, 1):
        title = item.get("title") or item.get("name")
        overview = item.get("overview")
        vote = item.get("vote_average")
        print(f"\n[{idx}] {title}")
        print(f"⭐ 평점: {vote}")
        print(f"줄거리: {overview[:120]}...")
    return picks



username = input("당신의 이름 또는 닉네임을 알려주세요😊: ")
ott_platforms = [
    "넷플릭스",  
    "쿠팡플레이스", 
    "티빙", 
    "웨이브", 
    "디즈니+",
    "라프텔",]
ott_platforms.append("제가 찾는 플랫폼이 없어요😢")

print(f"\n🎥 {username}님께 최적화된 콘텐츠를 추천해드리기 위해,")
print("시청 가능한 OTT 플랫폼을 선택해주세요!\n")
for idx, p in enumerate(ott_platforms, 1):
    print(f"{idx}. {p}")

while True:
    user_input = input("\n해당 번호를 모두 입력해주세요 \n*복수선택 가능해요 (예:1,3)*: ")
    choices = [i.strip() for i in user_input.split(",") if i.strip() != ""]
    
    # 모두 정수인지, 1~len(ott_platforms) 사이인지 체크
    valid = True
    for i in choices:
        if not i.isdigit() or not (1 <= int(i) <= len(ott_platforms)):
            valid = False
            break

    if valid and choices:  # 올바른 값이 1개 이상일 때만!
        selected_indexes = [int(i) for i in choices]
        break
    else:
        print("\n⚠️ 숫자를 잘못 입력하셨어요.")
        print("1번 ~ 7번에서 골라 다시 입력해 주세요. 제가 기다리고 있을게요!😊")
        print("*복수선택 가능합니다*")

# 체크: '찾는 플랫폼 없음' 선택 여부
has_missing_option = len(ott_platforms) in selected_indexes

# 최종 선택 목록
selected = [ott_platforms[i-1] for i in selected_indexes if i != len(ott_platforms)]

if selected:
    print(f"\n✅ {username}님이 선택한 OTT 플랫폼:")
    for p in selected:
        print(f"👉 {p}")

if has_missing_option:
    print("\n원하는 플랫폼이 목록에 없군요...")
    print("아쉽게 해드려서 정말 죄송합니다🙇")
    print("무드픽은 더 다양한 콘텐츠와 플랫폼을 담기 위해 열심히 준비 중이에요.")
    print("조금만 기다려주시면, 더 만족스러운 무드픽이 되어 돌아올게요 💙")
    exit()

while True:
    print("\n어떤 유형의 콘텐츠를 추천받고 싶으신가요?")
    print("1. 영화만\n2. 시리즈물만\n3. 상관없어요")
    choice = input("번호를 입력하세요: ")
