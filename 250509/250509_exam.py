
# 딕셔너리 사용하기


# 음식으로 해보자

'''
food = {"음식":{"과일":["사과", "수박",{"포도":["거봉", "샤인머스켓"]}],"채소":["오이", "상추", {"배추":["양배추", "알배추"]}], "고기":["양고기", "돼지고기", {"소고기":["등심", "안심"]}]}}

print(food["음식"]["고기"][2]["소고기"][0])
'''

#반복문 문제

#코드업 1081
'''
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

for dice1 in range(1,num1+1):
    for dice2 in range(1,num2+1):
        print(dice1, dice2)
'''

'''
data1 = {"a": [1, 2, 3], "b": [4, 5, 6]}

for key in data1:
    for num in data1[key]:
        print(num)
'''

#11
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num%2 == 0:
        even_numbers.append(num)

print(even_numbers)
'''


#12
'''
degree1 = input("온도(섭씨)를 입력하세요. : ")
degree1 = int(degree1)

if degree1 >= 100:
    print("수증기")

elif 0 <= degree1 < 100:
    print("물")

elif degree1 < 0:
    print("얼음")

else:
    print("올바른 온도를 입력해주세요.")
'''


# 13
'''
scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}

all = scores.values()
all = list(all)
num = 0
print(all)

for cal1 in all:

   num =  num + cal1

print(num/4)
'''


#14
'''
data1 = "HOT DOG FRIEND"

data1 = data1.lower()
list1 = []
list2 = []

for data2 in data1:
    if data2 == " ":
        list2.append(data2)

    else:
        list1.append(data2)

result1 = "".join(list1)

print(result1)
'''


#15
'''
data1 = input("숫자를 입력하세요. : ")
data1 = int(data1)
num = 0

list1 = []
list2 = []


for cal1 in range(1,data1+1):
    if cal1%3 == 0:
        list2.append(cal1)

    else:
        list1.append(cal1)


for cal2 in list1:
    num = num + cal2

print(num)
'''


#16





