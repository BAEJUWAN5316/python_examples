
# and 연산

## 다른 언어에서는
# a && b

'''
a = True
b = True

c = a and b

d = 10 > 5 and 10 < 5

f = 10 >= 10 or False # 앞에 이미 true가 있으니 뒤에 값이 무엇이 오던 true가 성립.

f = False and True and True 
print(f)

f2 = (False or True) and True
print(f2)

f3 = not ((False or True) and True)
print(f3)

a = 10
b = 20

c = a!=b # a b는 서로 다르니? 라고 묻는 것!
'''

'''
a = int(input())
b = int(input())
c = int(input())

#True
print(((a>=10)or(b>5))and(c<5))

#False
print((a>1)and(b>=1)and(c>2))
'''

'''
a = 10

a = a +10 # a +=10
'''

# 멤버 연산
'''
st = "modulabs is good"

sta = "good" in st # "good" 이 st변수 안에 있니?
sta2 = "good" not in st # "good"이 st 변수 안에 없니?

# split

a = " a b c"
'''

f1 = input("숫자 세 개를 공백을 두고 입력해주세요 : ")
f2, f3, f4 =f1.split()
print(f"{int(f2)+int(f3)+int(f4)} {((int(f2)+int(f3)+int(f4))/3):.3f}")
