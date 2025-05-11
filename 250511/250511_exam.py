
#인벤토리
# 통나무, 밧줄, 돛, 패들
# 도끼

inventory = []
ax = 0
wood = 0
rope = 0
sail = 0
paddle = 0
cave = 0


#무인도에서 탈출하기 게임

print(f'''
당신은 눈을 떠보니 처음 보는 섬에 있습니다.
어떻게 이 곳을 탈출해야 할까요?''')

while True:
    print(" ")
    print("주변을 둘러보니 숲, 바다, 동굴이 보입니다.")
    sel1 = input("무엇을 하시겠습니까? [1.숲으로 간다/2.바다로 간다./3동굴로 간다/4.가방 확인/5.탈출하기]")

    if sel1 == "1":
        se11_for = input("탈출을 위해선 숲의 나무를 잘라야 할 것 같습니다. 나무를 자르시겠습니까? [1.네/2.아니오]")
        if se11_for == "1":
            if ax == 0:
                print(" ")
                print("***도끼가 없으므로 나무를 자를 수 없습니다.")
            elif ax == 1:
                print(" ")
                print("***도끼로 나무를 잘라 통나무를 가져왔습니다. [+통나무]")
                inventory.append("통나무")
                wood = 1
                ax = 2
            elif ax == 2:
                print(" ")
                print("***통나무는 충분한 것 같습니다.")
        elif se11_for == "2":
            print(" ")
            print("***별 소득 없이 주둔지로 돌아왔습니다.")

    if sel1 == "2":
        if rope == 0:
            sel1_sea = input("넓은 바다 멀리 희미한 물체가 보입니다. 위험해 보이지만 확인하시겠습니까? [1.네/2.아니오]")
            if sel1_sea == "1":
                print(" ")
                print("***물체는 튼튼한 밧줄이었습니다. 가방에 밧줄을 넣었습니다. [+밧줄]")
                inventory.append("밧줄")
                rope = 1
            elif sel1_sea == "2":
                print(" ")
                print("***별 소득 없이 주둔지로 돌아왔습니다.")
        elif rope == 1:
            sel2_sea = input("해변가에 처음 보는 물체가 떠내려온 것 같습니다. 확인하시겠습니까? [1.네/2.아니오]")
            if sel2_sea == "1":
                print(" ")
                print("***떠내려 온 물체는 돛으로 사용할 수 있는 큰 텐트였습니다. [+돛]")
                inventory.append("돛")
                sail = 1
                rope = 2
            elif sel2_sea == "2":
                print(" ")
                print("***별 소득 없이 주둔지로 돌아왔습니다.")
        elif rope == 2:
            print(" ")
            print("***멀고 먼 망망대해만 눈에 가득 담깁니다.")

    if sel1 == "3":
        if ax == 0:
            sel1_cave = input("동굴 안쪽에서 무언가 반짝이는 물건이 있습니다. 확인하시겠습니까? [1.네/2.아니오]")
            if sel1_cave == "1":
                print(" ")
                print("***반짝이는 물건은 도끼였습니다. 도끼를 가방에 넣었습니다. [+도끼]")
                inventory.append("도끼")
                ax = 1
            elif sel1_cave == "2":
                print(" ")
                print("***별 소득 없이 주둔지로 돌아왔습니다.")
        elif (ax == 1 or ax == 2) and cave == 0:
            sel2_cave = input("동굴 입구에서 아까 보지 못 했던 물건이 보입니다. 확인하시겠습니까? [1.네/2.아니오]")
            if sel2_cave == "1":
                print(" ")
                print("***배를 앞으로 나가게 할 수 있는 패들이 있었습니다. 패들을 가방에 넣었습니다. [+패들]")
                inventory.append("패들")
                paddle = 1
                cave = 1
            elif sel2_cave == "2":
                print(" ")
                print("***별 소득 없이 주둔지로 돌아왔습니다.")
        elif (ax == 1 or ax == 2) and cave == 1:
            print(" ")
            print("***어둡고 축축한 동굴에 다시 가고싶지 않습니다.")
            
    if sel1 == "4":
        print(" ")
        print("***현재 가방에 있는 물건")
        print(inventory)

    if sel1 == "5":
        if wood == 1 and rope == 2 and sail == 1 and paddle == 1:
            print(" ")
            print("****축하합니다. 당신은 주어진 재료로 배를 만들어 섬을 탈출했습니다.****")
            break

        else:
            print(" ")
            print("***아직 배를 만들어 탈출하기엔 재료가 부족합니다.")

print("**플레이 해주셔서 감사합니다.**")








