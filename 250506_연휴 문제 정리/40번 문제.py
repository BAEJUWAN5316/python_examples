
#40 40번 문제

data1 = int(input("나이를 입력해주세요. : "))
data2 = input("회원이십니까? [Y/N] : ")

if data1 >= 19 and data2 == "N":
    print("입장료: 10000원")
elif data1 >= 19 and data2 == "Y":
    print("입장료: 8000원")
elif data1 < 19:
    print("입장료: 5000원")