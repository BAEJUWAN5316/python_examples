# 비교연산
'''
x, y = 10, 100

print(x==y) # 두 개가 같은가?

x, y = 10, 10
print(x>y) # x가 y보다 초과인가?
print(x>=y) # x가 y이상인가?

print(x<y) # 미만
print(x<=y) # 이하

print("apple" < "banana") # 결과는 트루

print(5 < x < 15) # 결과 true

'''

'''
a, b = input("키와 몸무게를 써주세요").split()
print(int(a) <= 130, "키 미만")
print(int(b) >= 10, "정상")
'''

'''
a = "good"
print(len(a)) # len은 변수의 문자 수를 가져온다
'''

'''
str1 = input("문자를 넣어주세요_1 : ")
str2 = input("문자를 넣어주세요_2 : ")
'''




j = 10.52999999999

print(f"j의 값은 {j:.2f}")


money = 1000000000000000000000

print(f"{money:,}") # 3자리 수로 , 찍어서 출력


f = input("소수점 아래의 수가 있는 실수를 입력해주세요. : ")
f2 = float(f)
print(f"소수점 아래 4번째까지 표시하면 {f2:.4f}입니다.")


mo1 = input("현재 통장 잔액을 입력해주세요. : ")
mo2 = int(mo1)
print(f"현재 당신의 통장 잔액은 {mo2:,}원 입니다.")




