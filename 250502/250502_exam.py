

#1 1번문제
'''
name1 = input("이름을 입력해주세요. : ")
print(f"안녕하세요, {name1}님!")
'''


#2 2번문제
'''
hello1 = input("\"안녕\"이라고 작성해주세요 : ")
print(hello1*3)
'''

#3 3번문제
'''
age1 = int(input("출생년도를 yyyy로 입력해주세요 : "))
age2 = 2025 - age1

print(f'당신의 나이는 {age2}세입니다.')
'''

#4 4번문제
'''
pi1 = float(input("반지름의 길이를 입력해주세요."))
pi2 = 3.14*pi1**2
print(f"반지름이 {pi1}인 원의 넓이: {pi2}")
'''

#5 5번문제
'''
data1 = int(input("시속(km/h)을 입력해주세요. : "))
data2 = int(input("시간(h)을 입력해주세요. : "))
data3 = data1*data2
print(f"총 이동 거리: {data3}km")
'''

#6 6번문제
'''
data1 = input("\"안녕하세요.\"라고 입력해주세요. : ")
data2 = input("\"반갑습니다.\"라고 입력해주세요. : ")
print(f"{data1} {data2}")
'''

#7 7번문제
'''
in1 = int(input("인치를 입력해주세요. : "))
cm1 = in1 * 2.54
print(f"{in1}인치는 {cm1}센티미터입니다.")
'''

#8 8번문제
'''
pay1 = int(input("식사 금액(원)을 작성해주세요 : "))
tip1 = int(input("팁 비율(%)을 작성해주세요. : "))

tip2 = pay1 * (tip1 * 0.01)
pay2 = pay1 + tip2

tip2 = int(tip2)
pay2 = int(pay2)


print(f"팁 금액: {tip2}원")
print(f"총 지불 금액: {pay2}원")
'''

#9 9번문제
'''
cm1 = int(input("키(cm)를 입력해주세요. : "))
kg1 = int(input("몸무게(kg)를 입력해주세요. : "))

bmi1 = kg1 / (cm1 * 0.01)**2

print(f"BMI : {bmi1:.2f}")
'''

#10 10번문제
'''
a,b,c,d,e = input("5개의 숫자를 공백간격을 두고 입력해주세요. : ").split()
print(f"첫 번째 숫자: {a}")
print(f"마지막 숫자: {e}")
'''

#11 11번문제
'''
a = input("1번 숫자를 입력해주세요. : ")
b = input("2번 숫자를 입력해주세요. : ")

print(f"교환 전: a = {a}, b = {b}")
a, b = b, a
print(f"교환 후: a = {a}, b = {b}")
'''

#12 12번문제
'''
data1 = input("문자를 입력해주세요. : ")

print(f"문자열 길이: {len(data1)}")
print(f"첫 글자: {data1[0]}")
print(f"마지막 글자: {data1[-1]}")
'''

#13 13번문제       ????????????????????
'''
r1 = "안녕하세요"
result1 = r1.romanizer()
print(result1)
'''

#14 14번문제
'''
pi1 = float(input("실수를 입력해주세요. : "))
print(f"{pi1:.2f}")
'''

#15 15번문제
'''
age1 = int(input("나이를 입력해주세요. : "))

if age1 >= 65:
    print("노년")
elif age1 >= 35:
    print("중장년")
elif age1 >= 19:
    print("청년")
else:
    print("미성년자")
'''

#16 16번문제
'''
ip1 = input("문장을 입력해주세요. : ")

space1 = 0
int1 = 0
str1 = 0


data1 = ip1[0]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[1]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[2]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[3]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[4]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[5]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[6]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[7]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[8]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[9]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[10]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[11]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[12]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[13]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[14]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

data1 = ip1[15]
if data1 == " ":
    space1 = space1 + 1
elif data1.isdigit():
    int1 = int1 + 1
elif data1.isalpha:
    str1 = str1 + 1

print(f"공백 수: {space1}")
print(f"숫자 수: {int1}")
print(f"문자 수: {str1}")
'''

'''
ip1 = input("문장을 입력해주세요. : ")

space1 = 0
int1 = 0
str1 = 0


data1 = ip1[0]
if data1 == " ":
    space1 = space1 + 1
elif data1 == "0":
    int1 = int1 + 1
elif data1 == "1":
    int1 = int1 + 1
elif data1 == "2":
    int1 = int1 + 1
elif data1 == "3":
    int1 = int1 + 1
elif data1 == "4":
    int1 = int1 + 1
elif data1 == "5":
    int1 = int1 + 1
elif data1 == "6":
    int1 = int1 + 1
elif data1 == "7":
    int1 = int1 + 1
elif data1 == "8":
    int1 = int1 + 1
elif data1 == "9":
    int1 = int1 + 1
elif type(data1) == str:
    str1 = str1 + 1


print(f"공백 수: {space1}")
print(f"숫자 수: {int1}")
print(f"문자 수: {str1}")
'''


#17 17번문제
'''
data1 = input("데이터를 입력해주세요. : ")

if data1 == "0":
    data1 = 1
    print((data1 < 1))

elif data1 == "1":
    print(bool(data1))

elif data1 == " ":
    data1 = 1
    print((data1 < 1)) 

elif data1 == "hello":
    print(bool(data1))

elif data1 == "O":
    print(bool(data1))

elif data1 == "False":
    print(bool(data1))
'''

#18 18번문제
'''
int1 = int(input("숫자를 입력하세요. : "))
int2 = int1%2

if int2 == 0:
    print(f"{int1}은(는) 짝수입니다.")
elif int2 == 1:
    print(f"{int1}은(는) 홀수입니다.")
'''

#19 19번문제
'''
f1, f2, f3, f4 = input("과일 네가지를 공란으로 구분하여 입력해주세요. : ").split()
print(f"{f1},{f2},{f3},{f4}")
'''

#20 20번문제

on1 = int(input("온도를 입력해주세요."))
on2 = input("섭씨, 화씨 중에 선택해주세요. [C=섭씨/F=화씨] : ")

if on2 == "C":
    print(f"{float(on1)}ºC는 {float(on1*9/5 +32):.1f}ºF입니다.")

elif on2 =="F":
    print(f"{float(on1)}ºF는 {float((on1-32)*5/9):.1f}ºC입니다.")









