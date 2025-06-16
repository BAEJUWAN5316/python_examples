# 가영문제 1

def solution():
    data1 = input("숫자를 입력하세요.")
    data1 = int(data1)
    result1= [i**2 for i in range(1,data1+1) if i%2 == 0]
    return result1

print(solution())
