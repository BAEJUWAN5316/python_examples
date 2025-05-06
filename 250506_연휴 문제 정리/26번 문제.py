
#26 26번 문제

data1 = input("이메일을 작성해주세요. : ")
num = 0
mail1 = 0

while True:
    if len(data1) != num:
        if data1[num] != "@":
            num = num + 1
        elif data1[num] == "@":
            mail1 = 1
            num = num + 1

    if len(data1) == num:
        break

if mail1 == 0:
    print("유효하지 않은 이메일 주소입니다.")
elif mail1 == 1:
    print("유효한 이메일 주소입니다.")