# 입력 구현
'''
print("좋아하는 음식을 말해주세요.")
a = input()
b = a*10

print(f"당신이 좋아하는 음식은 {a}군요, {a}를 좋아하는 당신은")
print(f"[{a}{a}] 좋아하는 음식이니 두 번 말해봤어요.")
print(b,"열 번도 말해볼게요.")
print(a[0:1], "첫 번째 글자는 이거네요")
'''

'''
# 형변환
a = input("아무거나 입력해주세요.")

print(type(a)) 
b = int(a) #문자를 숫자로
print(type(b))

a = 1

print(type(str(a)))
'''

# 문자열 고유 기능
s = 'weniv CEO licat'
print(s.lower())
print(s.upper())

print(s.find("good")) #찾는 값이 없으면 -1이 나옴 #찾으면 찾은 위치가 나옴
# print(s.index("good")) #찾는 값이 없으면 에러가 나옴

print(s.find("weniv"))
print(s.find("licat"))

print(s.index("weniv"))
print(s.index("licat"))

print(s.count("i"))

s2 = s.replace("CEO", "CTO")

print(s2)

s3 = "weniv-corp"

s4,s5 = s3.split("-")
print(s4, s5)

'''
입력이 들어온다. 키 몸무게 성별 나이 이름
예시 180 60 남 25 김아무개
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
이름을 f-string통해 세 번 반복해서 출력
'''

'''
inf1 = input()
inf2, inf3, inf4, inf5, inf6 = inf1.split()
print("키 :",inf2)
print("몸무게 :",inf3)
print("성별 :",inf4)
print("나이 :",inf5)
print("이름 :",inf6)
print(f"{inf6}"*3)
'''

'''
s20 = ["modu","labs","good"]

print(" ".join(s20))


name = 'licat'
age = 29

print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))
print(f'제 이름은 {name}이고, 나이는 {age}살입니다.')

print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.

#bool 타입
a = 10>3 #참
b = True
C = False
print(type(a))
print(a)

# 형변환
a = 1
b = 0
c = -1
d = "okay"
f = ""

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))

print(a==b)

X = None
print(X)

result = 5 + 3
print(result) # 결과 : 8

result = 3 + 2.5
print(result) # 결과 : 5.5
'''

print(11/2)
print(10/2)
print(type(10/2))
print(11//2)
print(type(int(10/2)))