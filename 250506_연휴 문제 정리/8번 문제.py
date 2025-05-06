
#8 8번 문제

pay1 = int(input("식사 금액(원)을 작성해주세요 : "))
tip1 = int(input("팁 비율(%)을 작성해주세요. : "))

tip2 = pay1 * (tip1 * 0.01)
pay2 = pay1 + tip2

tip2 = int(tip2)
pay2 = int(pay2)


print(f"팁 금액: {tip2}원")
print(f"총 지불 금액: {pay2}원")