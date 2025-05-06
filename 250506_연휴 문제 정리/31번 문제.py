
#31 31번 문제

data1 = int(input("1_연산 할 숫자를 입력해주세요. : "))
data2 = int(input("2_연산 할 숫자를 입력해주세요. : "))
cul1 = input("두 수를 연산 할 안산자를 입력해주세요.(+, -, *, /) : ")

if cul1 == "+":
    print(f"{data1} + {data2} = {data1+data2}")
elif cul1 == "-":
    print(f"{data1} - {data2} = {data1-data2}")
elif cul1 == "*":
    print(f"{data1} * {data2} = {data1*data2}")
elif cul1 == "/":
    print(f"{data1} / {data2} = {data1/data2}")