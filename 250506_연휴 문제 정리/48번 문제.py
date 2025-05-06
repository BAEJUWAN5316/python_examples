
#48 48번 문제

data1 = input("문자를 넣어주세요. : ")

data2 = data1[::-1]

if data1 == data2:
    print(f"\'{data1}\'은 펠린드롬입니다.")
else:
    print(f"\'{data1}\'은 펠린드롬이 아닙니다.")