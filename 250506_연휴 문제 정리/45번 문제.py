
#45 45번 문제

yy, mm, dd = input("연월일을 yyyy-mm-dd 형식으로 입력해주세요. : ").split("-")

yy = int(yy)
mm = int(mm)
dd = int(dd)


if dd >=32:
    print("유효하지 않은 날짜입니다.")
elif mm >= 13:
    print("유효하지 않은 날짜입니다.")
elif (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and (1 <= dd <= 31):
    print("유효한 날짜입니다.")
elif (yy%4 == 0) and (yy%100 != 0):
    if mm == 2 and (1 <= dd <= 29):
        print("유효한 날짜입니다.")
    elif mm == 2 and dd > 29:
        print("유효하지 않은 날짜입니다.")
elif mm == 2 and (1 <= dd <= 28):
    print("유효한 날짜입니다.")
elif mm == 2 and (dd > 28):
    print("유효하지 않은 날짜입니다.")
elif (mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11) and (1 <= dd <= 30):
    print("유효한 날짜입니다.")
elif (mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11) and (dd > 30):
    print("유효하지 않은 날짜입니다.")

else:
    print("에러")