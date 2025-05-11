
# 5/10 토요일 과제

# 1번 문제
'''
data1 = "admin"
data2 = "user"
pw1 = "1234"

log1 = input("아이디를 입력하세요. : ")
log2 = input("비밀번호를 입력하세요. : ")

if (log1 == "admin" or log1 == "user") and log2 == pw1:
    print("로그인 성공")

else:
    print("로그인 실패")
'''


# 2번 문제
'''
data1 = input("설정할 비밀번호를 입력해주세요. : ")
list1 = []

if len(data1) < 8:
    print("8자 이상 설정해주세요.")

elif len(data1) >= 8:
    for data2 in data1:
        if data2 == "!":
            list1.append(1)
        elif data2 == "#":
            list1.append(1)

    if len(list1) >= 1:
        print("유효한 비밀번호")

    elif len(list1) == 0:
        print("유효하지 않음")
'''


# 3번 문제
'''
data1 = input("피라미드 층 수를 입력해주세요. : ")
data1 = int(data1)

for pi1 in range(1,data1+1):
    print(pi1*"*")
'''


# 4번 문제
'''
dic1 = {"key1":[6, 5, 10, 15, 2, 486, 1]}
list1 = sorted(dic1["key1"],reverse=True)

print(list1)
'''




# 5번 문제
'''
for x in range(2,10):
    print(" ")
    print(f"구구단 {x}단")
    for y in range(1,10):
        print(f"{x} X {y} = {x*y}")
'''


# 개인 문제

x = input("영수증에 적힌 총 금액을 적어주세요. : ")
n = input("구매한 품목의 총 갯수를 적어주세요. : ")
x = int(x)
n = int(n)
cost1 = 0

for data1 in range(1,n+1):
    item1, item2 = input(f"{data1}번 물품의 가격과 개수를 공백을 두고 적어주세요. : ").split()
    item1 = int(item1)
    item2 = int(item2)

    cost1 = cost1 + (item1 * item2)

if x == cost1:
    print("Yes")
elif x != cost1:
    print("No")





