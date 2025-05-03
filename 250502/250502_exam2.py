

#21 21번문제

data1, data2 = input("문장을 입력해주세요. : ").split()

print(data1.upper(), data2.upper())
print(data1.lower(), data2.lower())
print(data1.title(), data2.title())

data3 = data1.replace(data1[0],data1[0].upper())
data4 = data2.replace(data2[0],data2[0].upper())
print(data3, data4)



#22 22번문제

data1 = input("문장을 입력하세요. : ")

print(f"앞 3글자: {data1[0:3]}")
print(f"뒤 3글자: {data1[-2:]}")
print(f"거꾸로: {data1[::-1]}")


#23 23번문제

d1, d2, d3, d4, d5, d6 = input("문장을 입력하세요. : ").split()
data1 = input("찾을 단어를 입력하세요. : ")
data2 = d1+d2+d3+d4+d5+d6

print(f"단어 \'{data1}\'의 위치: {data2.find(data1)+1}")


#24 24번문제

data1 = input("문장을 입력하세요. : ")
data2 = input("문장에서 바꿀 문자를 입력하세요. : ")
data3 = input("바뀌게 될 문자를 입력하세요. : ")

print(data1.replace(data2, data3))



#25 25번문제

data1 = input("문장을 입력하세요. : ")
data2 = input("찾을 문자를 입력하세요. : ")
data3 = data1.count(data2,)

print(f"문자 \'{data2}\'의 출현 횟수: {data3}")



#26 26번문제       ???????????????????

mail1 = input("이메일을 입력해주세요. : ")

data1 = "user@example.com"

if mail1 == data1:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")


#27 27번문제

data1 = input("단어를 입력해주세요. : ")
data2 = int(input("원하는 글자 수를 입력해주세요. : "))

data3 = data2 - int(len(data1))

print(data1+("*"*data3))



#28 28번문제

data1 = input("텍스트를 입력해주세요. : ")

len1 = int(len(data1)/2) # 입력 텍스트 갯수의 절반값
len2 = len(data1)%2

len3 = data1[int(len1-1):int(len1)+1]
len4 = data1[int(len1):int(len1)+1]

if len2 == 0:
    print(len3)
elif len2 == 1:
    print(len4)    



#29 29번문제

data1 = input("문장을 입력해주세요. : ")

data1 = data1.replace("!","")
data1 = data1.replace("?","")
data1 = data1.replace(".","")
data1 = data1.replace(",","")
data1 = data1.replace("\'","")
data1 = data1.replace("\"","")

print(data1)


#30 30번문제

print("그녀가 말했다: \"안녕하세요!\"\n이름 나이 직업\n홍길동  30\t개발자\n안녕!\n반가워요!")



#31 31번문제

data1 = int(input("1_연산 할 숫자를 입력해주세요. : "))
data2 = int(input("2_연산 할 숫자를 입력해주세요. : "))
cul1 = input("두 수를 연산 할 안산자를 입력해주세요.(+, -, *, /) : ")

if cul1 == "+":
    print(f"{data1} + {data2} = {data1+data2}")
elif cul1 == "-":
    print(f"{data1} - {data2} = {data1-data2}")
elif cul1 == "*":
    print(f"{data1} * {data2} = {data1*data2}")
elif cul1 == "/":
    print(f"{data1} / {data2} = {data1/data2}")


#32 32번문제

data1 = int(input("금액(원)을 작성해주세요. : "))
tax1 = int(input("세율(%)을 작성해주세요. : "))

tax2 = tax1*0.01

print(f"세금: {float(data1*tax2)}원")
print(f"세후 금액: {float(data1 - (data1*tax2))}원")



#33 33번문제

data1 = input("True/False 중 하나를 입력해주세요_1 : ")
data2 = input("True/False 중 하나를 입력해주세요_2 : ")


data1 = bool(data1 == "True")
data2 = bool(data2 == "True")

print(data1)
print(data2)


if data1 == data2:
    print(f"{data1} AND {data2} ={data1}")
    print(f"{data1} OR {data2} = {data1}")
    print(f"NOT {data1} = {not(data1)}")
    print(f"NOT {data2} = {not(data2)}")

elif data1 != data2:
    print(f"{data1} AND {data2} = {data1 and data2}")
    print(f"{data1} OR {data2} = {data1 or data2}")
    print(f"NOT {data1} = {not(data1)}")
    print(f"NOT {data2} = {not(data2)}")



#34 34번문제

data1 = int(input("상품의 가격(원)을 입력해주세요. : "))
data2 = int(input("할인률(%)를 입력해주세요. : "))

sale1 = data2*0.01

print(f"할인 금액: {float(data1*sale1)}원")
print(f"최종 가격: {float(data1-(data1*sale1))}원")


#35 35번문제

data1 = int(input("첫 번째 수를 입력하세요. : "))
data2 = int(input("두 번째 수를 입력하세요. : "))
data3 = int(input("세 번째 수를 입력하세요. : "))

if data1 > data2 > data3:
    print(f"가장 큰 수: {data1}")
elif data1 > data3 > data2:
    print(f"가장 큰 수: {data1}")
elif data2 > data1 > data3:
    print(f"가장 큰 수: {data2}")
elif data2 > data3 > data1:
    print(f"가장 큰 수: {data2}")
elif data3 > data1 > data2:
    print(f"가장 큰 수: {data3}")
elif data3 > data2 > data1:
    print(f"가장 큰 수: {data3}")


#36 36번문제

data1 = int(input("연도를 입력하세요. : "))

if data1%4 == 0 and data1%100 != 0 or data1%400 == 0:
    print(f"{data1}년은 윤년입니다.")
else:
    print(f"{data1}년은 윤년이 아닙니다.")



#37 37번문제

data1 = input("문자열을 입력하세요. : ")
data2 = input("위의 문자열에서 찾을 단어를 입력하세요. : ")

if data1.find(data2) >= 0:
    print(f"\"{data1}\"에 \"{data2}\"이(가) 포함되어 있습니다.")
elif data1.find(data2) < 0:
    print(f"\"{data1}\"에 \"{data2}\"이(가) 포함되어 있지 않습니다.")


#38 38번문제

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



#39 39번문제

data1 = input("4자리 숫자를 입력해주세요. : ")

data2 = int(data1[0]) + int(data1[1]) + int(data1[2]) + int(data1[3]) 
print(f"자릿수 합계: {data2}")


#40 40번문제

data1 = int(input("나이를 입력해주세요. : "))
data2 = input("회원이십니까? [Y/N] : ")

if data1 >= 19 and data2 == "N":
    print("입장료: 10000원")
elif data1 >= 19 and data2 == "Y":
    print("입장료: 8000원")
elif data1 < 19:
    print("입장료: 5000원")
'''

#41 41번문제            ?????????????????????????
'''
data1 = input("설정할 비밀번호를 입력해주세요. : ")

if len(data1) >= 8:
    print("안전한 비밀번호입니다.")
else:
    print("안전하지 않은 비밀번호입니다.")


data1 = input("설정할 비밀번호를 입력해주세요. : ")

if data1.find("0") >= 0:
    int1 = True
elif data1.find("1") >= 0:
    int1 = True
elif data1.find("2") >= 0:
    int1 = True
elif data1.find("3") >= 0:
    int1 = True
elif data1.find("4") >= 0:
    int1 = True
elif data1.find("5") >= 0:
    int1 = True
elif data1.find("6") >= 0:
    int1 = True
elif data1.find("7") >= 0:
    int1 = True
elif data1.find("8") >= 0:
    int1 = True
elif data1.find("9") >= 0:
    int1 = True
elif data1.find("0") < 0:
    int1 = False

if data1.find("a") >= 0:
    str1 = True
elif data1.find("b") >= 0:
    str1 = True
elif data1.find("c") >= 0:
    str1 = True
elif data1.find("d") >= 0:
    str1 = True
elif data1.find("e") >= 0:
    str1 = True
elif data1.find("f") >= 0:
    str1 = True
elif data1.find("g") >= 0:
    str1 = True
elif data1.find("h") >= 0:
    str1 = True
elif data1.find("i") >= 0:
    str1 = True
elif data1.find("j") >= 0:
    str1 = True
elif data1.find("k") >= 0:
    str1 = True
elif data1.find("l") >= 0:
    str1 = True
elif data1.find("m") >= 0:
    str1 = True
elif data1.find("n") >= 0:
    str1 = True
elif data1.find("o") >= 0:
    str1 = True
elif data1.find("p") >= 0:
    str1 = True
elif data1.find("q") >= 0:
    str1 = True
elif data1.find("r") >= 0:
    str1 = True
elif data1.find("s") >= 0:
    str1 = True
elif data1.find("t") >= 0:
    str1 = True
elif data1.find("u") >= 0:
    str1 = True
elif data1.find("v") >= 0:
    str1 = True
elif data1.find("w") >= 0:
    str1 = True
elif data1.find("x") >= 0:
    str1 = True
elif data1.find("y") >= 0:
    str1 = True
elif data1.find("z") >= 0:
    str1 = True
elif data1.find("A") >= 0:
    str1 = True
elif data1.find("B") >= 0:
    str1 = True
elif data1.find("C") >= 0:
    str1 = True
elif data1.find("D") >= 0:
    str1 = True
elif data1.find("E") >= 0:
    str1 = True
elif data1.find("F") >= 0:
    str1 = True
elif data1.find("G") >= 0:
    str1 = True
elif data1.find("H") >= 0:
    str1 = True
elif data1.find("I") >= 0:
    str1 = True
elif data1.find("J") >= 0:
    str1 = True
elif data1.find("K") >= 0:
    str1 = True
elif data1.find("L") >= 0:
    str1 = True
elif data1.find("M") >= 0:
    str1 = True
elif data1.find("N") >= 0:
    str1 = True
elif data1.find("O") >= 0:
    str1 = True
elif data1.find("P") >= 0:
    str1 = True
elif data1.find("Q") >= 0:
    str1 = True
elif data1.find("R") >= 0:
    str1 = True
elif data1.find("S") >= 0:
    str1 = True
elif data1.find("T") >= 0:
    str1 = True
elif data1.find("U") >= 0:
    str1 = True
elif data1.find("V") >= 0:
    str1 = True
elif data1.find("W") >= 0:
    str1 = True
elif data1.find("X") >= 0:
    str1 = True
elif data1.find("Y") >= 0:
    str1 = True
elif data1.find("Z") >= 0:
    str1 = True
elif data1.find("a") < 0:
    str1 = False

if int1 and str1 and len(data1) >= 8:
    print("안전한 비밀번호입니다.")
else:
    print("안전하지 않은 비밀번호입니다.")



#42 42번문제

d1, d2, d3 = input("문장을 입력하세요. : ").split()
print(d1[::-1], d2[::-1], d3[::-1])



#43 43번문제

data1 = input("문장을 입력하세요.")

str1 = ["a", "e", "i", "o", "u"]

mo1 = 0
ja1 = 0

data2 = data1.split()
data3 = len(data2) - 1


if data1[0].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[0].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[0].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[0].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[0].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[1].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[1].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[1].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[1].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[1].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[2].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[2].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[2].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[2].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[2].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[3].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[3].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[3].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[3].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[3].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0
    
if data1[4].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[4].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[4].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[4].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[4].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[5].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[5].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[5].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[5].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[5].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[6].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[6].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[6].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[6].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[6].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[7].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[7].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[7].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[7].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[7].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[8].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[8].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[8].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[8].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[8].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[9].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[9].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[9].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[9].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[9].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

if data1[10].find(str1[0]) >= 0:
    mo1 = mo1 + 1
elif data1[10].find(str1[1]) >=0:
    mo1 = mo1 + 1
elif data1[10].find(str1[2]) >=0:
    mo1 = mo1 + 1
elif data1[10].find(str1[3]) >=0:
    mo1 = mo1 + 1
elif data1[10].find(str1[4]) >=0:
    mo1 = mo1 + 1
else:
    mo1 = mo1 + 0

print(f"모음 개수: {mo1}")
print(f"자음 개수: {len(data1)-mo1-data3}")


#44 44번문제

# data1 = float(input("숫자를 입력해주세요. : "))

# if data1 >= int(data1)+0.5:
    # print(f"가장 가까운 정수: {int(data1)+1}")

# elif data1 < int(data1)+0.5:
    # print(f"가장 가까운 정수: {int(data1)}")


data1 = float(input("숫자를 입력해주세요. : "))

print(f"가장 가까운 정수:{round(data1)}")



#45 45번문제

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



#46 46번문제

data1, data2 = input("파일명과 확장자를 입력하세요. : ").split(".")
print(f"확장자: {data2}")


#47 47번문제

data1 = input("문자를 입력해주세요. : ")

num1 = data1.count("a")
num2 = data1.count("b")
num3 = data1.count("c")

print(f"a{num1}b{num2}c{num3}")



#48 48번문제

data1 = input("문자를 넣어주세요. : ")

data2 = data1[::-1]

if data1 == data2:
    print(f"\'{data1}\'은 펠린드롬입니다.")
else:
    print(f"\'{data1}\'은 펠린드롬이 아닙니다.")



#49 49번문제

data1 = input("문자를 입력하세요. : ")

ord0 = ord(data1[0])
ord1 = ord(data1[1])
ord2 = ord(data1[2])
ord3 = ord(data1[3])
ord4 = ord(data1[4])

chr0 = chr(ord0+3)
chr1 = chr(ord1+3)
chr2 = chr(ord2+3)
chr3 = chr(ord3+3)
chr4 = chr(ord4+3)

print(chr0+chr1+chr2+chr3+chr4)
'''

#50 50번문제
'''
ip1,ip2,ip3,ip4 = input("IP주소를 입력해주세요. : ").split(".")

ip1 = int(ip1)
ip2 = int(ip2)
ip3 = int(ip3)
ip4 = int(ip4)

if 0 <= ip1 <= 255:
    ip1 = "O"
else:
    ip1 = "X"

if 0 <= ip2 <= 255:
    ip2 = "O"
else:
    ip2 = "X"

if 0 <= ip3 <= 255:
    ip3 = "O"
else:
    ip3 = "X"

if 0 <= ip4 <= 255:
    ip4 = "O"
else:
    ip4 = "X"

if ip1 == "O" and ip2 == "O" and ip3 == "O" and ip4 == "O":
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")


data1 = input("ip를 쓰세요 : ").split(".")

data1[0] = int(data1[0])
data1[1] = int(data1[1])
data1[2] = int(data1[2])
data1[3] = int(data1[3])


if 0 <= data1[0] <= 255:
    data1[0] = "O"
else:
    data1[0] = "X"

if 0 <= data1[1] <= 255:
    data1[1] = "O"
else:
    data1[1] = "X"

if 0 <= data1[2] <= 255:
    data1[2] = "O"
else:
    data1[2] = "X"

if 0 <= data1[3] <= 255:
    data1[3] = "O"
else:
    data1[3] = "X"

if len(data1) != 4:
    print("유효하지 않은 IP 주소입니다.")

elif data1[0] == "O" and data1[1] == "O" and data1[2] == "O" and data1[3] == "O":
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")


