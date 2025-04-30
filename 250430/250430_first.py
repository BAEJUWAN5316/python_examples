


'''
split() 활용

a, b 변수를 활용,
키, 몸무게를 입력받는다.

키와 몸무게를 나눈 나머지를 출력한다.

조건문을 활용해서

키(a)가 130 이상이면 a, 150이상이면 b, 170이상이면 c 180이상이면 d를 출력하세요

'''

'''
cm, kg = input("키와 몸무게를 입력해주세요. : ").split()
cm = int(cm)
kg = int(kg)

cm%kg
print (cm % kg)


if cm >= 180:
    print("d")

elif cm >= 170:
    print("c")

elif cm >= 150:
    print("b")

elif cm >= 130:
    print("a")
'''

'''
a = input("시험 점수를 입력해주세요.(0~100점 사이) : ")
a = int(a)

if a >= 90:
    print("A")

elif a >= 80:
    print("B")

elif a >= 70:
    print("C")

elif a >= 60:
    print("D")

else:
    print("F")
'''


## and or 연산활용

'''
a = 10
b = 20

if a ==10 and b == 20:
    print("good")
else:
    print("no")
'''

'''
a, b, c를 입력받는다.
a가 100이고 b가 200이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도저도 아니면 c를 출력

'''

'''
a = int(input("숫자를 입력해주세요_1"))
b = int(input("숫자를 입력해주세요_2"))
c = int(input("숫자를 입력해주세요_3"))

if a == 100 and b >= 200:
    print("a")

elif b == 1:
    print("b")

else:
    print("c")
'''

dice1, dice2, dice3 = input("주사위 숫자 세 개를 입력해주세요. : ").split()
dice1 = int(dice1)
dice2 = int(dice2)
dice3 = int(dice3)

if dice1 == dice2 == dice3:
    print(10000 + dice1*1000)

elif dice1 == dice2 or dice2 == dice3 or dice1 == dice3:
    if dice1 == dice2:
        print(1000 + dice1*100)
    elif dice1 == dice3:
        print(1000 + dice3*100)
    elif dice2 == dice3:
        print(1000 + dice3*100)

elif dice1 != dice2 != dice3:
    c = max(dice1, dice2, dice3)
    print(c*100)

'''
if a != b and b!= c and a != c:
    temp = a
    if b > temp:
        temp = b
    if c > temp:
        temp = c
    price = temp*100

    print(price)
'''
