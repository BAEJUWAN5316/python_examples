

#21 21번문제
'''
data1, data2 = input("문장을 입력해주세요. : ").split()

print(data1.upper(), data2.upper())
print(data1.lower(), data2.lower())
print(data1.title(), data2.title())

data3 = data1.replace(data1[0],data1[0].upper())
data4 = data2.replace(data2[0],data2[0].upper())
print(data3, data4)
'''


#22 22번문제
'''
data1 = input("문장을 입력하세요. : ")

print(f"앞 3글자: {data1[0:3]}")
print(f"뒤 3글자: {data1[-2:]}")
print(f"거꾸로: {data1[::-1]}")
'''

#23 23번문제
'''
d1, d2, d3, d4, d5, d6 = input("문장을 입력하세요. : ").split()
data1 = input("찾을 단어를 입력하세요. : ")
data2 = d1+d2+d3+d4+d5+d6

print(f"단어 \'{data1}\'의 위치: {data2.find(data1)+1}")
'''

#24 24번문제
'''
data1 = input("문장을 입력하세요. : ")
data2 = input("문장에서 바꿀 문자를 입력하세요. : ")
data3 = input("바뀌게 될 문자를 입력하세요. : ")

print(data1.replace(data2, data3))
'''


#25 25번문제
'''
data1 = input("문장을 입력하세요. : ")
data2 = input("찾을 문자를 입력하세요. : ")
data3 = data1.count(data2,)

print(f"문자 \'{data2}\'의 출현 횟수: {data3}")
'''


#26 26번문제       ???????????????????
'''
mail1 = input("이메일을 입력해주세요. : ")

data1 = "user@example.com"

if mail1 == data1:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")
'''

#27 27번문제
'''
data1 = input("단어를 입력해주세요. : ")
data2 = int(input("원하는 글자 수를 입력해주세요. : "))

data3 = data2 - int(len(data1))

print(data1+("*"*data3))
'''


#28 28번문제
'''
data1 = input("텍스트를 입력해주세요. : ")

len1 = int(len(data1)/2) # 입력 텍스트 갯수의 절반값
len2 = len(data1)%2

len3 = data1[int(len1-1):int(len1)+1]
len4 = data1[int(len1):int(len1)+1]

if len2 == 0:
    print(len3)
elif len2 == 1:
    print(len4)    
'''


#29 29번문제
'''
data1 = input("문장을 입력해주세요. : ")

data1 = data1.replace("!","")
data1 = data1.replace("?","")
data1 = data1.replace(".","")
data1 = data1.replace(",","")
data1 = data1.replace("\'","")
data1 = data1.replace("\"","")

print(data1)
'''

#30 30번문제

print("그녀가 말했다: \"안녕하세요!\"\n이름 나이 직업\n홍길동  30\t개발자\n안녕!\n반가워요!")



