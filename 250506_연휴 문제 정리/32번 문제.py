
#32 32번 문제

data1 = int(input("금액(원)을 작성해주세요. : "))
tax1 = int(input("세율(%)을 작성해주세요. : "))

tax2 = tax1*0.01

print(f"세금: {float(data1*tax2)}원")
print(f"세후 금액: {float(data1 - (data1*tax2))}원")