
#38 38번 문제

data1 = int(input("점수를 입력하세요.(0~100) : "))

if data1 >= 90:
    print(f"학점: A")
elif data1 >= 80:
    print(f"학점: B")
elif data1 >= 70:
    print(f"학점: C")
elif data1 >= 60:
    print(f"학점: D")
else:
    print(f"학점: F")
