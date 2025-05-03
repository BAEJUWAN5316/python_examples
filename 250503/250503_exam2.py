
# rpg 게임

lev = 1 #레벨
sc1 = 0 #경험치
mo1 = 0 #돈
inv1 = ["무기 없음"] #인벤토리
sta = 1 #공격력

item1 = "단검"
item2 = "언월도"


print(f'''
rpg 만들기
''')


name = input("모험가 이름을 정해주세요. : ")

while True:
    print("")
    print(f"[레벨:{lev}]")
    data1 = input(f"{name}님, 무엇을 하시겠습니까? [1_사냥, 2_상점, 3_상태보기]")
    if data1 == "1":
        data2 = input("다람쥐가 나타났습니다. [1_공격, 2_도망]")
        if data2 == "1":
            print("경험치를 10, 돈 5원을 얻었습니다.")
            sc1 = sc1 + 10
            mo1 = mo1 + 5
            if sc1 == 20:
                lev = lev + 1
            elif sc1 == 40:
                lev = lev + 1
            elif sc1 == 60:
                lev = lev + 1
            elif sc1 == 80:
                lev = lev + 1
        elif data2 == "2":
            print("도망갔습니다.")
    elif data1 == "2":
        data2 = input("물건을 구매하시겠습니까? [1_단검<공격력 +5>/10원, 2_사지않는다]")
        if data2 == "1" and mo1 >= 10:
            print("단검을 구매했습니다.")
            inv1[0] = item1
            sta = sta+5
        elif data2 == "1" and mo1 < 10:
            print("돈이 부족합니다.")
    elif data1 == "3":
        print("")
        print(f"[레벨:{lev}, 경험치:{sc1}, 돈:{mo1}]")
        print(f"[공격력: {sta}, 현재 장착 무기: <{inv1[0]}>]")
    if lev == 5:
        print("")
        data1 = input("**레벨이 5가 되었습니다. 다음 마을로 넘어갑니다. [1_네]")
        if data1 == "1":
            break
        else:
            break
print("다음 마을로 넘어갑니다.")



while True:
    print("")
    print(f"[레벨:{lev}]")
    data1 = input(f"{name}님, 무엇을 하시겠습니까? [1_사냥, 2_상점, 3_상태보기]")
    if data1 == "1":
        data2 = input("늑대가 나타났습니다. [1_공격, 2_도망]")
        if data2 == "1":
            print("경험치를 20, 돈 10원을 얻었습니다.")
            sc1 = sc1 + 20
            mo1 = mo1 + 10
            if sc1 == 120:
                lev = lev + 1
            elif sc1 == 160:
                lev = lev + 1
            elif sc1 == 200:
                lev = lev + 1
            elif sc1 == 220:
                lev = lev + 1
            elif sc1 == 260:
                lev = lev + 1
        elif data2 == "2":
            print("도망갔습니다.")
    elif data1 == "2":
        data2 = input("물건을 구매하시겠습니까? [1_언월도<공격력 +10>/100원, 2_사지않는다]")
        if data2 == "1" and mo1 >= 100:
            print("언월도를 구매했습니다.")
            inv1[0] = item2
            sta = sta+10
        elif data2 == "1" and mo1 < 100:
            print("돈이 부족합니다.")
    elif data1 == "3":
        print("")
        print(f"[레벨:{lev}, 경험치:{sc1}, 돈:{mo1}]")
        print(f"[공격력: {sta}, 현재 장착 무기: <{inv1[0]}>]")
    if lev == 10:
        break




print("")
print("베타버전은 여기까지 입니다.")







