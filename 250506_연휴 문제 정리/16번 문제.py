#16 16번 문제

data1 = input("문자열을 입력해주세요. : ")
len1 = len(data1)
a = 0

space1 = 0
int1 = 0
str1 = 0


while True:
    if data1[a] == " ":
        space1 = space1 + 1
    elif data1[a] == "0":
        int1 = int1 + 1
    elif data1[a] == "1":
        int1 = int1 + 1
    elif data1[a] == "2":
        int1 = int1 + 1
    elif data1[a] == "3":
        int1 = int1 + 1
    elif data1[a] == "4":
        int1 = int1 + 1
    elif data1[a] == "5":
        int1 = int1 + 1
    elif data1[a] == "6":
        int1 = int1 + 1
    elif data1[a] == "7":
        int1 = int1 + 1
    elif data1[a] == "8":
        int1 = int1 + 1
    elif data1[a] == "9":
        int1 = int1 + 1
    else:
        str1 = str1 + 1
    
    a = a + 1

    if a == len1:
        break

print(f"공백 수 : {space1}")
print(f"숫자 수 : {int1}")
print(f"문자 수 : {str1}")