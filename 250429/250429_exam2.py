'''
#6048
a, b = input("a b의 양식으로 두 수를 입력하세요. 첫 번째 숫자가 작은 지 큰 지 알려드립니다. : ").split()
print(bool(a < b))


#6049
a, b = input("a b의 양식으로 두 수를 입력하세요. 두 수가 같은지 아닌지 알려드립니다. : ").split()
print(bool(a == b))


#6050
a, b = input("a b의 양식으로 두 수를 입력하세요. 두 번째 숫자가 크거나 같은지 알려드립니다. : ").split()
print(bool(a <= b))


#6051
a, b = input().split()
print(bool(a != b))


#6052
a, b = input().split()
print(bool(a != b))
'''

'''
#6067
num1 = input()
num1 = int(num1)

if ((num1 < 0) and (num1%2 == 0)):
    print("A")

elif (num1 < 0) and (num1%2 != 0):
    print("B")

elif (num1%2 == 0):
    print("C")

elif (num1%2 != 0):
    print("D")
'''

a = "531681"
print(len(a))