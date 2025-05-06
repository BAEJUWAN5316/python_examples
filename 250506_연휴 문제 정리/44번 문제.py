
#44 44번 문제

data1 = float(input("숫자를 입력해주세요. : "))

if data1 >= int(data1)+0.5:
    print(f"가장 가까운 정수: {int(data1)+1}")

elif data1 < int(data1)+0.5:
    print(f"가장 가까운 정수: {int(data1)}")


data1 = float(input("숫자를 입력해주세요. : "))

print(f"가장 가까운 정수:{round(data1)}")
