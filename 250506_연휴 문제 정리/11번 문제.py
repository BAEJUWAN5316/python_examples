
#11 11번 문제

a = input("1번 숫자를 입력해주세요. : ")
b = input("2번 숫자를 입력해주세요. : ")

print(f"교환 전: a = {a}, b = {b}")
a, b = b, a
print(f"교환 후: a = {a}, b = {b}")