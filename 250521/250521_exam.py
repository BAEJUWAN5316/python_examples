import json

with open("names.json", "r", encoding="utf-8") as f:
    list1 = json.load(f)

while True:
    data1 = input("추가할 이름을 입력해주세요./0.종료/1.명단확인 : ")
    if data1 == "0":
          print("종료합니다.")
          break
    elif data1 == "1":
          print(list1)
    else:
        list1.append(data1)
        with open("names.json", "w", encoding="utf-8") as f:
            json.dump(list1, f, ensure_ascii=False)










