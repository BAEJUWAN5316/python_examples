import json
import time

with open("vocab.json","r",encoding="utf-8") as f:
    dict1 = json.load(f)



while True:
    print(f"\n기능을 선택하세요.")
    print(f"[1.단어 저장]")
    print(f"[2.저장된 단어 확인]")
    print(f"[3.저장된 단어 삭제]")
    print(f"[0. 나가기]")
    data1 = input("메뉴를 선택하세요. : ")

    if data1 == "1":
        key1 = input("\n영어 단어를 입력하세요. : ")
        value1 = input("단어의 뜻을 한글로 입력하세요. : ")
        dict1 = dict1|{key1:value1}
        with open("vocab.json","w",encoding="utf-8") as f:
            json.dump(dict1,f,ensure_ascii=False)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("저장이 완료되었습니다!")

    elif data1 == "2":
        print("")
        for i,v in enumerate(dict1,1):
            print(f"{i}. {v}/{dict1[v]}")

    elif data1 == "3":
        print("")
        for i,v in enumerate(dict1,1):
            print(f"{i}. {v}/{dict1[v]}")
        data2 = input("삭제 할 단어를 입력하세요. : ")
        dict1.pop(data2)
        with open("vocab.json","w",encoding="utf-8") as f:
            json.dump(dict1,f,ensure_ascii=False)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("삭제가 완료되었습니다!")

    elif data1 == "0":
        print("\n안녕히 가세요!")
        break
