
# 369 박수 횟수 세기

data1 = input("369게임의 숫자 하나를 입력해주세요 : ")
num = 0
len1 = len(data1)
clap = []


while True:
    if data1[num] == "3" or data1[num] == "6" or data1[num] == "9":
        clap.append("X")
        num = num + 1
    else:
        num = num + 1
    
    if num == len1:
        break

if "X" in clap:
    print("".join(clap))

else:
    print(data1)


# 369 박수 횟수 세기2

data1 = input()
num = 1
len1 = len(data1)
list1 = []


while True:
    data1 = int(data1)  #인풋값을 숫자로 바꿈
    data2 = data1 - (data1 - num)   # 인풋숫자를 1부터 넣을래
    list1.append(str(data2)) # 위의 숫자를 list1에 추가할래
    num = num + 1 # num의 숫자가 하나 커져

    if num - 1 == data1:
        break

if "3" in list1:
    list1[list1.index("3")] = "X"
if "6" in list1:
    list1[list1.index("6")] = "X"
if '9' in list1:
    list1[list1.index("9")] = "X"
if '13' in list1:
    list1[list1.index('13')] = "X"
if '16' in list1:
    list1[list1.index('16')] = "X"
if '19' in list1:
    list1[list1.index('19')] = "X"
if '23' in list1:
    list1[list1.index('23')] = "X"
if '26' in list1:
    list1[list1.index('26')] = "X"
if '29' in list1:
    list1[list1.index('29')] = "X"

list2 = " ".join(list1)

print(list2)


# 공백을 두고 3 값을 받고 각 값의 합과 평균을 출력하고 평균은 소수점 셋째 자리에서 반올림, 둘째자리까지 출력해라

da1, da2, da3 = input().split()
da1 = int(da1)
da2 = int(da2)
da3 = int(da3)

cal1 = da1 + da2 + da3
cal2 = (da1 + da2 + da3)/3

print(f"{cal1} {round(cal2,2):.2f}")


# 정수를 입력하고 1부터 입력한 정수까지 1씩 커지며 더하고 그 값이 입력 정수와 같거나 작으면 마지막으로 입력한 정수를 출력

data1 = input()
data1 = int(data1)
num = 1
list1 = []

while True:
    data2 = data1 - (data1 - num)
    list1.append(data2)
    num = num + 1
    
    if sum(list1) >= data1:
        break

print(list1[-1])


yy, mm, dd = input().split(".")

print(f"{dd}-{mm}-{yy}")