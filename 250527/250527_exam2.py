
#1 문자열 압축 문제

# data1 = input("문자열을 입력해주세요. : ")



#2 최빈값 구하기

a = [1,1,3,3,3,4,4,4,5,5,5,6,6,6,6,6,6,6,6,] # 입력될 리스트
b = {}

for value in a:
    b = b|{value:a.count(value)}
b = list(b.items())

def f(x):
    return x[1]

c = sorted(b,key=f,reverse=True)

list1 = []
for v in c:
    if c[0][1] == v[1]:
        list1.append(v)

def f(x):
    return x[0]

list2 = sorted(list1,key=f)

print(list2[0][0]) # 최종 출력

