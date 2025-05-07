# 별 움직이기 게임
'''
list1 = ["☆ ", "☆ ", "☆ ", "☆ ", "☆ "]
list2 = ["☆ ", "☆ ", "☆ ", "☆ ", "☆ "]
list3 = ["☆ ", "☆ ", "★ ", "☆ ", "☆ "]
list4 = ["☆ ", "☆ ", "☆ ", "☆ ", "☆ "]
list5 = ["☆ ", "☆ ", "☆ ", "☆ ", "☆ "]

count1 = 0
print("")
print("***************")
print("*별*움*직*이*기*")
print("*방향을 움직여 별을 움직여보세요~*")
print("***************")
print("")
print("- - - - - -")
print("".join(list1))
print("".join(list2))
print("".join(list3))
print("".join(list4))
print("".join(list5))
print("- - - - - -")
while True:
    num1 = list1.index("★ ")

    print("")
    
    data1 = input("방향을 입력하세요. [4:좌 / 6:우 / 5:그만할래요]: ")
    print("")
    print("- - - - - -")
    data1 = int(data1)

    if num1 == 0 and data1 == 4:
        print(join1)
        print("우측으로만 이동 가능합니다.")
    elif num1 ==4 and data1 == 6:
        print(join1)
        print("좌측으로만 이동 가능합니다.")

    elif data1 == 6:
        list1[num1] = "☆ "
        list1[num1+1] = "★ "
        join1 = "".join(list1)
        count1 = count1 + 1
        print(join1)

    elif data1 == 4:
        list1[num1] = "☆ "
        list1[num1-1] = "★ "
        join1 = "".join(list1)
        count1 = count1 + 1
        print(join1)
    
    elif data1 == 5:
        break

    else:
        join1 = "".join(list1)
        print(join1)
        print("4 또는 6을 입력하세요.")

    print("- - - - - -")

print("********************************")
print(f"별은 총 {count1}번 움직였습니다.")
if count1 > 15:
    print("별은 아주 뜨겁습니다!")
elif count1 >= 10:
    print("별은 빨갛게 달아올랐습니다!")
elif count1 >= 5:
    print("별에서 열기가 느껴집니다.")
elif count1 >= 1:
    print("별에서는 냉기만이 가득합니다.")
else:
    print("별은 차갑게 얼어붙어있습니다.")

print("********************************")
'''

#5*5 로도 만들어보자


