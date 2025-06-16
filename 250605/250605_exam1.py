
line1 = [["☆ ","☆ ","☆ ","☆ ","☆ "],
        ["☆ ","☆ ","☆ ","※ ","☆ "],
        ["☆ ","☆ ","★ ","☆ ","☆ "],
        ["☆ ","☆ ","☆ ","☆ ","☆ "],
        ["☆ ","☆ ","☆ ","☆ ","☆ "],]
moved_star = 0
change_star = False
while True:
    print("")
    print("".join(line1[0]))
    print("".join(line1[1]))
    print("".join(line1[2]))
    print("".join(line1[3]))
    print("".join(line1[4]))
    move1 = input("움직일 방향을 선택하세요. [4.좌/6.우/8.상/2.하/0.나가기]")
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    for star_y in range(5):
        for star_x in range(5):
            if line1[star_y][star_x] == "★ ":
                x = star_x
                y = star_y
    
    if move1 == "6":
        if x == 4:
            print("우측으로 더이상 움직일 수 없습니다.")
        else:
            line1[y][x] = "☆ "
            line1[y][x+1] = "★ "
            moved_star += 1
    elif move1 == "4":
        if x == 0:
            print("좌측으로 더이상 움직일 수 없습니다.")
        else:
            line1[y][x] = "☆ "
            line1[y][x-1] = "★ "
            moved_star += 1
    elif move1 == "8":
        if y == 0:
            print("위쪽으로 더이상 움직일 수 없습니다.")
        else:
            line1[y][x] = "☆ "
            line1[y-1][x] = "★ "
            moved_star += 1
    elif move1 == "2":
        if y == 4:
            print("아래쪽으로 더이상 움직일 수 없습니다.")
        else:
            line1[y][x] = "☆ "
            line1[y+1][x] = "★ "
            moved_star += 1
    elif move1 == "0":
        break
    else:
        print("올바른 방향을 입력해주세요.")

    for star_y in range(5):
        for star_x in range(5):
            if line1[star_y][star_x] == "※ ":
                print("별이 진화했습니다!")
                change_star = True
                break

if change_star == True:
    while True:
        print("")
        print("".join(line1[0]))
        print("".join(line1[1]))
        print("".join(line1[2]))
        print("".join(line1[3]))
        print("".join(line1[4]))
        move1 = input("움직일 방향을 선택하세요. [4.좌/6.우/8.상/2.하/0.나가기]")
        x = 0
        y = 0
        x2 = 0
        y2 = 0
        for star_y in range(5):
            for star_x in range(5):
                if line1[star_y][star_x] == "※ ":
                    x = star_x
                    y = star_y
        
        if move1 == "6":
            if x == 4:
                print("우측으로 더이상 움직일 수 없습니다.")
            else:
                line1[y][x] = "☆ "
                line1[y][x+1] = "※ "
                moved_star += 1
        elif move1 == "4":
            if x == 0:
                print("좌측으로 더이상 움직일 수 없습니다.")
            else:
                line1[y][x] = "☆ "
                line1[y][x-1] = "※ "
                moved_star += 1
        elif move1 == "8":
            if y == 0:
                print("위쪽으로 더이상 움직일 수 없습니다.")
            else:
                line1[y][x] = "☆ "
                line1[y-1][x] = "※ "
                moved_star += 1
        elif move1 == "2":
            if y == 4:
                print("아래쪽으로 더이상 움직일 수 없습니다.")
            else:
                line1[y][x] = "☆ "
                line1[y+1][x] = "※ "
                moved_star += 1
        elif move1 == "0":
            break
        else:
            print("올바른 방향을 입력해주세요.")
    

print(f"\n별의 이동 횟수: {moved_star}")
if moved_star >= 20:
    print("별은 뜨겁게 활활 타오릅니다!")
elif moved_star >= 15:
    print("별은 뜨거워졌습니다!")
elif moved_star >= 10:
    print("별에는 온기가 돕니다..!")
elif moved_star >= 5:
    print("별은 아직 차갑습니다...")
elif moved_star >= 3:
    print("별의 곳곳에 얼음이 보입니다...")
elif moved_star == 0:
    print("별에게는 아무 일도 일어나지 않았습니다...")
