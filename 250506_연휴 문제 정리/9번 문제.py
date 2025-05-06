
#9 9번 문제

cm1 = int(input("키(cm)를 입력해주세요. : "))
kg1 = int(input("몸무게(kg)를 입력해주세요. : "))

bmi1 = kg1 / (cm1 * 0.01)**2

print(f"BMI : {bmi1:.2f}")