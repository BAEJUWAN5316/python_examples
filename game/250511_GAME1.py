


# RPG 게임만들기

import random


# 스탯

level1 = 1

job1 = "전사"
status1 = {"힘":10, "민첨":10, "경험치":0}
point1 = {"체력":50, "마력":20} # 깎여야 할 체력
point2 = {"체력":50, "마력":20} # 현재 총 체력
attack1 = [5, 6, 7, 8, 9, 12]
inven1 = {"무기":["없음"], "소모품":["없음"]}
money1 = 0

list1 = []
list2 = []


# 아이템

sword1 = {"단검":10, "대검":20}
drink = {"빨간물약":20, "파란물약":10}


# 몬스터
mon_list = ["다람쥐", "토끼", "늑대"]
mon1 = {"다람쥐":{"체력":15, "공격력":[1, 2, 3, 5], "경험치":10, "돈":10, "리셋체력":15}}
mon2=  {"토끼":{"체력":10, "공격력":[1, 2], "경험치":5, "돈":10, "리셋체력":10}}
mon3=  {"늑대":{"체력":30, "공격력":[4, 5, 6, 8], "경험치":30, "돈":30, "리셋체력":30}}


# 메세지
level_up = "*******축하합니다! 레벨이 1올랐습니다!*******"




while True:
    #몬스터
    battle1 = random.choice(mon_list)


    '''
    for level2 in range(30,36):
        if level2 == status1["경험치"]:
            level1 +=1
            print(level_up)
    for level2 in range(100,106):
        if level2 == status1["경험치"]:
            level1 +=1
            print(level_up)
    for level2 in range(200,206):
        if level2 == status1["경험치"]:
            level1 +=1
            print(level_up)
            '''





    '''
    if status1["경험치"] >= 200:
        level1 +=1
        print(level_up)
    elif status1["경험치"] >= 100:
        level1 +=1
        print(level_up)
    elif status1["경험치"] >= 30:
        level1 +=1
        print(level_up)
        '''


    if point1["체력"] <= 0:
        print(" ")
        print("***체력이 0이 되었습니다. 플레이어는 가진 아이템을 모두와 절반의 돈을 잃습니다.***")
        inven1 = {"무기":["없음"], "소모품":["없음"]}
        point1 = {"체력":50, "마력":20}
        money1 = int(money1/2)


    print(" ")
    print(f"[현재 상태]")
    print(f"[레벨: {level1}]")
    print(f"[체력: {point1["체력"]} 마력: {point1["마력"]} 돈: {money1}] 경험치: {status1['경험치']}")
    message1 = input("플레이어의 행동을 고르세요 [1.사냥하기/2.상점가기/3.상태보기/4.끝내기]")

    if message1 == "1":
        print(" ")
        print(f"{battle1}이(가) 나타났다!")
        print(" ")
        while True:
            message2 = input(f"{battle1}는 공격태세를 갖췄다! [1.공격/2.소모품 사용하기/3.도망가기]")
            if battle1 == "다람쥐":
                enemy1 = mon1
            elif battle1 == "토끼":
                enemy1 = mon2
            elif battle1 == "늑대":
                enemy1 = mon3
            
            if message2 == "1":
                print("플레이어는 공격을 했다!")
                enemy1[list(enemy1.keys())[0]]["체력"] -= random.choice(attack1)
                point1["체력"] -= random.choice(enemy1[list(enemy1.keys())[0]]["공격력"])
                print(f"{list(enemy1.keys())[0]}의 체력은 {enemy1[list(enemy1.keys())[0]]["체력"]}만큼 남았다!")
                print(f"플레이어의 체력은 {point1["체력"]}만큼 남았다!")
            elif message2 == "2":
                print(f"현재 가진 소모품")
                print(inven1["소모품"])
                drink1 = input(f"어떤 소모품을 사용하시겠습니까? 왼쪽부터 1번")

                '''
                for drink2 in range(len(inven1["소모품"])):
                    if drink1 == drink2:
                        inven1["소모품"][drink2-1]
                        '''
                #소모품 만드는 중
            elif message2 == "3":
                print(" ")
                print("플레이어는 도망쳤다!")
                enemy1[list(enemy1.keys())[0]]["체력"] = enemy1[list(enemy1.keys())[0]]["리셋체력"]
                break

            if enemy1[list(enemy1.keys())[0]]["체력"] <= 0:
                print(" ")
                print(f"{list(enemy1.keys())[0]}은 쓰러졌다!")
                status1["경험치"] += enemy1[list(enemy1.keys())[0]]["경험치"]
                money1 += enemy1[list(enemy1.keys())[0]]["돈"]
                enemy1[list(enemy1.keys())[0]]["체력"] = enemy1[list(enemy1.keys())[0]]["리셋체력"]
                print(f"플레이어는 경험치를 {enemy1[list(enemy1.keys())[0]]["경험치"]}만큼 획득했다!")
                print(f"플레이어는 돈을 {enemy1[list(enemy1.keys())[0]]["돈"]}만큼 획득했다!")

                for level2 in range(30,36):
                    if level2 == status1["경험치"]:
                        level1 +=1
                        point2["체력"] +=10
                        point2["마력"] +=15
                        point1["체력"] = point2["체력"]
                        point1["마력"] = point2["마력"]
                        print(level_up)
                for level2 in range(100,106):
                    if level2 == status1["경험치"]:
                        level1 +=1
                        point2["체력"] +=10
                        point2["마력"] +=15
                        point1["체력"] = point2["체력"]
                        point1["마력"] = point2["마력"]
                        print(level_up)
                for level2 in range(200,206):
                    if level2 == status1["경험치"]:
                        level1 +=1
                        point2["체력"] +=10
                        point2["마력"] +=15
                        point1["체력"] = point2["체력"]
                        point1["마력"] = point2["마력"]
                        print(level_up)
                break




    elif message1 == "4":
        print(" ")
        print("테스트 종료")
        break

print("테스트를 종료합니다.")

            



