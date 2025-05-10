
# 5/10 토요일 과제

# 1번 문제
'''
data1 = input("1번 정수를 입력해주세요. : ")
data2 = input("2번 정수를 입력해주세요. : ")
data1 = int(data1)
data2 = int(data2)

print(f"1번 정수 [{data1}]와 2번 정수 [{data2}]를 더한 값은 [{data1 + data2}]입니다.")
'''


# 2번 문제
'''
data1 = input("문자열을 입력해주세요 . : ")

print(f"{data1[::-1]}")
'''

# 3번 문제
'''
data1 = input("숫자를 입력해주세요. : ")
data1 = int(data1)

if data1%2 == 0:
    print(f"{data1}은 [Even] 입니다.")

elif data1%2 != 0:
    print(f"{data1}은 [Odd] 입니다.")
'''


# 4번 문제
'''
data1 = [1, 2, 3, 4, 5]
num = 0

for data2 in data1:
    num += data2

print(num/5)
'''


# 5번 문제
'''
data1 = input("1번 리스트에 들어갈 내용을 공백 간격을 두고 입력해주세요. : ").split()
data2 = input("2번 리스트에 들어갈 내용을 공백 간격을 두고 입력해주세요. : ").split()

data1 = set(data1)
data2 = set(data2)

print(f"1번 리스트와 2번 리스트의 교집합은 {data1&data2} 입니다.")
'''


# 6번 문제

tu1 = (1, [2, 3], 4)

tu1[1][1] = 100

print(tu1)

    


