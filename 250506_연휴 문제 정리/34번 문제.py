
#34 34번 문제

data1 = int(input("상품의 가격(원)을 입력해주세요. : "))
data2 = int(input("할인률(%)를 입력해주세요. : "))

sale1 = data2*0.01

print(f"할인 금액: {float(data1*sale1)}원")
print(f"최종 가격: {float(data1-(data1*sale1))}원")