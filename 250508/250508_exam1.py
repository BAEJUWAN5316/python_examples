'''
list1 = ["ㅇ", "ㅇ", "ㅇ", "ㅇ", "ㅇ"]
list2 = ["ㅇ", "ㅇ", "ㅇ", "ㅇ", "ㅇ"]
list3 = ["ㅇ", "ㅇ", "ㅊ", "ㅇ", "ㅇ"]
list4 = ["ㅇ", "ㅇ", "ㅇ", "ㅇ", "ㅇ"]
list5 = ["ㅇ", "ㅇ", "ㅇ", "ㅇ", "ㅇ"]
all_list = [list1, list2, list3, list4, list5]

point_x = -1
point_y = -1


for y in range(5):
    for x in range(5):
        if all_list[x][y] == "ㅊ":
            point_x = x
            point_y = y
            break

        point_x != -1
        break
'''


# 백준 10214 baseball 문제

num = 0
gamenum = 0
list1 = []

data1 = input("경기 횟수를 입력해주세요 : ")
data1 = int(data1)
game = 1

y = 0
k = 0

while True:

    if num != data1:
        while True:
            if gamenum != 9:
                y_score, k_score = input(f"{game}차 경기의 {gamenum+1}회차 점수를 입력해주세요. [Y득점 K득점] : ").split()
                y_score = int(y_score)
                k_score = int(k_score)
                
                y = y + y_score
                k = k + k_score
                
                gamenum = gamenum + 1
            
            elif gamenum == 9:
                gamenum = 0
                game = game + 1
                num = num + 1
                print("")
                print("다음 게임")
                break

        if y == k:
            result1 = "Draw"
            list1.append(result1)
        
        elif y > k:
            result1 = "Yonsei"
            list1.append(result1)

        elif y < k:
            result1 = "Corea"
            list1.append(result1)

        y = 0
        k = 0
            
    elif num == data1:
        break

print("경기 끝")

num2 = 0

while True:
    print(f"{num2+1}회차 승리 팀 : {list1[num2]}")

    num2 = num2 + 1

    if num2 == data1:
        break

    








