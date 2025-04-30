
'''
item = "아무것도 없음"
money = 10
level = 1


name = input("이름을 말해주세요 : ")
job = input("직업을 선택해주세요 [전사/마법사*미구현] : ")

print(f"캐릭터 이름이 {name}으로 설정되었습니다.")

game1 = input(f"{name}님은 초보자 마을에 도착했습니다. 어떤 걸 하시겠습니까? [사냥/상점] : ")

if game1 == "사냥":
    fight1 = input("토끼가 나타났습니다. 싸우시겠습니까? [싸우기/도망가기] : ")
elif game1 == "상점":
    shop1 = input("무기를 구매하시겠습니까? [단검 공격력5 -10원/롱소드 공격력10 -20원]")

if fight1 == "싸우기":
    fight2 = input(f"레벨업을 했습니다. 현재 레벨: {level+1} ")
elif fight1 == "도망가기":
    game1 = input(f"{name}님은 초보자 마을에 도착했습니다. 어떤 걸 하시겠습니까? [사냥/상점] : ")

if shop1 == "단검":
    shop2 = input("단검을 장착했습니다.")

'''

name = input("이름을 말해주세요 : ")

print(f'''
***********************************************************
{name} 당신은 어느날 눈을 떠보니 끝없는 외길 앞에 떨어졌습니다.
이 길의 끝에 과연 탈출구가 있을까요?
***********************************************************
''')

scene1 = input("길 위를 걸어가본다. [네/아니오] : ")

if scene1 == "네":
    scene2 = input("계속 걷던 당신은 두갈래 길을 만납니다. [왼쪽길/오른쪽길] : ")
elif scene1 == "아니오":
    print(f"{name} 당신은 굶어 죽었습니다. *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene2 == "왼쪽길":
    scene3 = input("그곳에선 한 노파를 만났습니다. 말을 걸까요? [건다/안건다] : ")
elif scene2 == "오른쪽길":
    print(f"{name} 당신은 보이지 않는 길을 걷다 낭떠러지로 떨어졌습니다. *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene3 == "건다":
    print(f"{name} 당신은 노파가 준 독극물을 마시고 쓰러졌습니다. *THE END")
elif scene3 == "안건다":
    scene4 = input("계속 걷다보니 물이 가득 차있는 물병이 있습니다. 물을 마시겠습니까? [마신다/안마신다] : ")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene4 == "마신다":
    scene5 = input("갈증이 나던 참에 맛있게 물을 마셨습니다. 그리고 계속 걸어가니 참새가 말을 걸어왔습니다. [대화한다/안한다] : ")
elif scene4 == "안마신다":
    print(f"{name} 당신은 계속 길을 걷다 탈수증상으로 쓰러졌습니다. *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene5 == "대화한다":
    scene6 = input("참새는 가위바위보를 해서 이기면 탈출 힌트를 주겠다고 합니다. [가위/바위/보] : ")
elif scene5 == "안한다":
    print(f"{name} 당신은 길을 걷다 지쳐 쓰러졌습니다. *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")



if scene6 == "가위":
    print(f"{name} 당신은 참새와 비겼습니다. 참새는 저 멀리 날아가버렸습니다.  *THE END")
elif scene6 == "바위":
    scene7 = input("승부에서 이겼습니다. 참새는 종을 조심하라고 말하곤 날아갔습니다. [계속간다] : ")
elif scene6 == "보":
    print(f"{name} 당신은 참새에게 졌습니다. 참새는 저 멀리 날아가버렸습니다.  *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene7 == "계속간다":
    scene8 = input("계속 걷다보니 \"출구\" 라는 말이 적힌 문이 나왔습니다. 문을 열어보시겠습니까? [연다/그냥간다] : ")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene8 == "연다":
    scene9 = input("문을 여는 순간 \"딸랑\"하고 종이 울리는 소리가 났습니다. 계속 가시겠습니까? [간다/나간다] : ")
elif scene8 == "그냥간다":
    print(f"{name} 당신은 끝없는 길을 걷다 지쳐 쓰려졌습니다. *THE END")
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")


if scene9 == "간다":
    print(f"{name} 당신은 종소리를 듣자마자 쓰러져 버렸습니다. *THE END")
elif scene9 == "나간다":
    print(f'''
******************************************************************
{name} 당신이 뒤를 돌아 나가자 당신이 원래 있던 곳으로 돌아왔습니다. 
축하합니다. 성공적으로 길을 빠져나왔습니다.
              **  T   H   E       E   N   D   **
******************************************************************
''')
else:
    print(f"{name} 올바르지 않은 선택은 실패를 초래합니다. *THE END")

