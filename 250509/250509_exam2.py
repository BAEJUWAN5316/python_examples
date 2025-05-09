
# 5*5 움직이는 별 만들기


list1 = ["☆ ","☆ ","☆ ","☆ ","☆ "]
list2 = ["☆ ","☆ ","☆ ","☆ ","☆ "]
list3 = ["☆ ","☆ ","★ ","☆ ","☆ "]
list4 = ["☆ ","☆ ","☆ ","☆ ","☆ "]
list5 = ["☆ ","☆ ","☆ ","☆ ","☆ "]

list_all = [list1, list2, list3, list4,list5]


print(f'''
*******************
별 움 직 이 기 게 임
*******************
      
방향을 지시하여 별을 움직여보세요!)
''')

# 좌표 출력하기
star_x = 1
star_y = 0

for y in list_all:
        star_y += 1
        for x in y:
            if x != "★ ":
                star_x += 1
                
            if star_x == 6:
                star_x = 1
            elif x == "★ ":
                break
        if x == "★ ":
            break

# 별 이름 짓기
name = input("별의 이름을 지어주세요! : ")

# 별 이동 수
num = 0

# 발생 멘트
ment = "- - - - - - - - - - - - - - - - - - - - -"


# 방향 전환
while True:
    print(" ")
    print("- - - - - - - - - - - - - - - - - - - - -")
    print(f"               {"".join(list1)}")
    print(f"               {"".join(list2)}")
    print(f"               {"".join(list3)}")
    print(f"               {"".join(list4)}")
    print(f"               {"".join(list5)}")
    print(ment)

    move1 = input("이동할 방향을 입력하세요. [8:상/2:하/4:좌/6:우/5:그만하기] : ")
    

    if move1 == "8":
        if star_y == 1:
            ment = "- - 더 이상 위로 이동할 수 없습니다. - -"
        else:
            list_all[star_y-1][star_x-1] = "☆ "
            star_y -= 1
            list_all[star_y-1][star_x-1] = "★ "
            num += 1
            ment = "- - - - - - - - - - - - - - - - - - - - -"
            
        
    elif move1 == "2":
        if star_y == 5:
            ment = "- - 더 이상 아래로 이동할 수 없습니다. - -"
        else:
            list_all[star_y-1][star_x-1] = "☆ "
            star_y += 1
            list_all[star_y-1][star_x-1] = "★ "
            num += 1
            ment = "- - - - - - - - - - - - - - - - - - - - -"

    elif move1 == "4":
        if star_x == 1:
            ment = "- - 더 이상 왼쪽으로 이동할 수 없습니다. - -"
        else:
            list_all[star_y-1][star_x-1] = "☆ "
            star_x -= 1
            list_all[star_y-1][star_x-1] = "★ "
            num += 1
            ment = "- - - - - - - - - - - - - - - - - - - - -"

    elif move1 == "6":
        if star_x == 5:
            ment = "- - 더 이상 오른쪽으로 이동할 수 없습니다. - -"
        else:
            list_all[star_y-1][star_x-1] = "☆ "
            star_x += 1
            list_all[star_y-1][star_x-1] = "★ "
            num += 1
            ment = "- - - - - - - - - - - - - - - - - - - - -"


    if move1 == "5":
        break

print("************************************")
print(f"{name}별은 {num}번 움직였습니다!")

if num >= 30:
    print(f"{name}별은 찬란한 빛을 내며 엄청난 열기를 뿜습니다!")
elif num >= 20:
    print(f"{name}별은 뜨겁게 달아올랐습니다!")
elif num >= 10:
    print(f"{name}별은 약간 온기가 생겼습니다..!")
elif num >= 5:
    print(f"{name}별은 아직 차갑습니다...")
elif num > 0:
    print(f"{name}별의 얼음은 그대로입니다...")
elif num == 0:
    print(f"차가운 {name}별은 얼음별입니다...")

print("************************************")




