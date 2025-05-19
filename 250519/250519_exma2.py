

import json

# json으로 score.txt 데이터 베이스 불러오기
try:
    with open("score.txt", "r", encoding="utf-8") as f:
        list1 = json.load(f)
except FileNotFoundError:
    list1 = []

while True:
    # 기능 시작
    print("-기능 선택-")
    print("1. 계정추가")
    print("2. 기능 확인")
    print("3. 계정 리스트 확인")
    print("0. 나가기")
    data1 = input("기능을 선택해주세요. : ")

    if data1 == "1":
        print("계정추가 기능입니다.")
        id1 = input("추가 할 계정의 이름을 설정해주세요. : ")
        pw1 = input("추가 할 계정의 비밀번호를 설정해주세요. : ")
        pw1 = int(pw1)
        list1.append({id1:pw1})

        # json으로 score.txt 데이터 베이스에 추가된 자료 저장하기
        with open("score.txt", "w", encoding="utf-8") as f:
            json.dump(list1, f, ensure_ascii=False)

    elif data1 == "2":
        print("기능 확인하겠습니다.")
        func1 = input("찾을 계정 이름을 입력해주세요. : ")
        for name1 in list1:
            if list(name1.keys())[0] == func1:
                print("찾았다")

    elif data1 == "3":
        print("계정 리스트를 확인하겠습니다.")
        for i,v in enumerate(list1,1):
            print(f"{i}. {list(v.keys())[0]}")

    elif data1 == "0":
        print("감사합니다!")
        break
