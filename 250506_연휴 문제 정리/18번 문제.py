
#18 18번 문제

int1 = int(input("숫자를 입력하세요. : "))
int2 = int1%2

if int2 == 0:
    print(f"{int1}은(는) 짝수입니다.")
elif int2 == 1:
    print(f"{int1}은(는) 홀수입니다.")