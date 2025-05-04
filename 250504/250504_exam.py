
# while을 이용한 문재 재풀이

#16 16번 문제
'''
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
'''

#19 19번문제

'''

data1 = input("단어들을 공백으로 구분하여 입력하세요: ").split()
re1 = ",".join(data1)
print(re1)
'''

#26 26번문제
'''
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
'''

#33 33번문제
'''
bool1 = input("불리언 값을 입력해주세요_1 : ")
bool2 = input("불리언 값을 입력해주세요_2 : ")

if bool1 == "True":
    bool1 = True
elif bool1 == "False":
    bool1 = False

if bool2 == "True":
    bool2 = True
elif bool2 == "False":
    bool2 = False

and1 = bool1 and bool2
or1 = bool1 or bool2
not1 = not bool1
not2 = not bool2

print(f"{bool1} AND {bool2} = {and1}")
print(f"{bool1} OR {bool2} = {or1}")
print(f"NOT {bool1} = {not1}")
print(f"NOT {bool2} = {not2}")
'''

#39 39번문제
'''
data1 = input("숫자를 입력해주세요 : ")
len1 = len(data1)
num = 0
hop1 = 0


while True:
    hop1 = hop1 + int(data1[num])
    num = num + 1

    if num == len1:
        break

print(f"자릿수 합계: {hop1}")
'''

#41 41번문제
'''
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
'''

#49 49번문제

data1 = input("문자를 넣어주세요. : ")
num = 0
len1 = len(data1)
list1 = []

while True:
    ord1 = ord(data1[num])
    if 88 <= ord1 <= 90:
        ord1 = ord1-23
    
    elif 120 <= ord1 <= 122:
        ord1 = ord1-23
    else:
        ord1 = ord1 + 3

    chr1 = chr(ord1)
    list1.append(chr1)
    num = num + 1

    if num == len1:
        break

print(f"암호화: {"".join(list1)}")







