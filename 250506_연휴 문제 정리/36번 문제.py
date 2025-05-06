
#36 36번 문제

data1 = int(input("연도를 입력하세요. : "))

if data1%4 == 0 and data1%100 != 0 or data1%400 == 0:
    print(f"{data1}년은 윤년입니다.")
else:
    print(f"{data1}년은 윤년이 아닙니다.")