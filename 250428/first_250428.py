
# 정수


a = 10
b = 20
c = 0
d = -40

print(type(a), type(b), type(c), type(d))
print(int(9.333))

# 실수
number1 = 3.12
number2 = -0.12
print(type(number1), type(number2))

print(float(3))

# 무한대
x = float("inf")
x = float("-inf")

# 문자열
str1 = "abcd"
str2 = 'abcd'

str3 = '''
오늘은 4월 28일입니다.

5월이 멀지 않았네요.

'''

print(type(str3))
print(str3)

# 문자열 이어붙이기

str6 = "modu"
str7 = "labs"

print(str6+str7)
str8 = str6+str7
print(str8)

# 개인정보 출력해보기
## 1. 성, 이름 변수를 따로 만들어서 +로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {네이버, 구글}

name1 = "배"
name2 = "주완"
name3 = "901010"
name4 = "1231234"
name5 = "abcd1234"
name6 = "naver.com"
name7 = "gmail.com"
print("1.", name1+name2)
print("2.", name3+"-"+name4)
print("3.", name5+"@"+name6)
print("3.", name5+"@"+name7)

# 문자열 반복하기

'''
str10 = str1 * 10

test2 = "30"

print (str10)


# print(str1 * test2) = x 안 된다! test2가 문자라서!

print (str10+"입니다", + "어쩌고 저쩌고")
'''

# 오늘은 4월 28일입니다.
a = "4"
b = "28"

# 기본방식이라면
print ("오늘은" + a + "월" + b + "일입니다")

# f-string
# f"" 위랑 같다!
print(f"오늘은 {a}월 {b}일입니다.")

print(f"오늘은 {a}월 {b*10}일입니다.")

# 문자열 인덱싱

s = "life is good"
print(s[0])
print(s[3])
print(s[-1])

## IndexError: string index out of range
## 주민등록번호가 13자리
## print(d[13]) 이라고 치면 에러 뜬다!
## print("good!")

# 문자열 슬라이싱 [start:stop:step] step은 생략 가능

print(s[0:3]) #s[0:3:1]과 같음
print(s[0:4:2])

# 다양한 슬라이싱 방법

s = 'weniv CEO licat'

# 테스트
## ip adress = 172.100.200.100
'''
1. ip adress 문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다
3. step을 활용해서 172100200100이 나오게 하기
'''

# 1. 
s = "ip address = 172.100.200.100"
print(s[:10])

# 2.
a = s[13:16]
b = s[17:20]
c = s[21:24]
d = s[25:28]

# 3.
print(f"3. {a}{b}{c}{d}")