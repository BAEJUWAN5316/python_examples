import hashlib


password = input("비밀번호 입력: ")
hashed_pw = hashlib.sha256(password.encode()).hexdigest()
print(hashed_pw)

data1 = input("비교용 데이터 입력 : ")
hashed_pw2 = hashlib.sha256(data1.encode()).hexdigest()
if hashed_pw2 == hashed_pw:
    print("동일")
else:
    print("불일치")





