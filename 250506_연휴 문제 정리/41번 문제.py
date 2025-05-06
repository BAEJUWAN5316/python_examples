
#41 41번 문제

data1 = input("비밀번호를 설정해주세요. : ")
num =0
len1 = len(data1)

str1 = "no"
int1 = "no"


while True:
    if data1[num] == "0":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "1":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "2":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "3":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "4":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "5":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "6":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "7":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "8":
        int1 = "yes"
        num = num + 1
    elif data1[num] == "9":
        int1 = "yes"
        num = num + 1
    else:
        str1 = "yes"
        num = num + 1

    if num == len1:
        break

if str1 == "yes" and int1 == "yes":
    print("안전한 비밀번호입니다.")
else:
    print("안전하지 않은 비밀번호입니다.")