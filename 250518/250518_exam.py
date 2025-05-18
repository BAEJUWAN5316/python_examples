"""
#1
a = [1, 2, 3]
b = list(map(lambda x: x*2 , a))
print(b)
"""

"""
#2
a = ['hi', 'banana', 'ok']
lenn = list(map(lambda x : len(x), a))
print(lenn)
"""

"""
#3
a = [2, 4, 6]
squa = map(lambda x: x **2, a)
print(list(squa))
"""

"""
#4
a = [1, -2, 3, -4, 5]
abss = list(map(lambda x : abs(x), a))
print(abss)
"""

"""
#5
a = [1, 2, 3]
strr = list(map(lambda x : str(x), a))
print(strr)
"""

"""
#6
a = ['hello', 'world']
b = list(map(lambda x: x.upper(),a))
print(b)
"""

"""
#7
a = [1, 2, 3]
b = [4, 5, 6]

c = list(map(lambda x, y: x + y, a, b))
print(c)
"""

"""
#8
a = ['123', 'abc', '456']
b = list(map(lambda x: x.isdigit(), a))
print(b)
"""

"""
#9
a = [10, 20, 30]
b = list(map(lambda x : x - 5, a))
print(b)
"""

"""
#10
a = ['apple', 'banana', 'cat']
b = list(map(lambda x : x[0], a))
print(b)
"""

"""
#1
a = [5, 2, 8, 1, 9]
print(sorted(a))
"""

"""
#2
a = 'hello'
b = list(reversed(a))
c = "".join(b)
print(c)
"""

"""
#3
a = [10, 20, 30, 40, 50]
b = filter(lambda x: x>= 30,a)
print(list(b))
"""

"""
#4
a = [1, 2, 3]
b = list(map(lambda x:x**2,a))
print(b)
"""

"""
#5
a = ['apple', 'banana', 'cherry']
b = list(filter(lambda x: len(x) >= 6,a))
print(b)
"""

"""
#6
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = zip(a,b)
print(list(c))
"""

'''
# 7
a = [3, 6, 9]
b = [1, 2, 3]

def f(x):
    return x[0] * x[1]

c = list(map(f, zip(a, b)))
print(c)
'''

"""
#8
a = [3, 4, 5, 6]
b = list(reversed(a))
print(b)
"""

"""
#9
a = [5, 10, 15, 20]
b = filter(lambda x : x%3 == 0, a)
print(list(b))
"""

'''
# 10
a = ["Python", "Java", "C"]
b = sorted(a, key=lambda x: len(x))
print(b)
'''

'''
#1
a = [10, 20, 30]
print(sum(a))
'''

'''
#2
a = [5, 2, 9, 1]
print(max(a))
'''

'''
#3
a = [5, 2, 9, 1]
print(min(a))
'''

'''
#4
a = "applebanana"
print(max(a))
'''

'''
#5 
a = "applebanana"
print(min(a))
'''

'''
#6
a = [4, 5, 6]
b = iter(a)
print(next(b),next(b),next(b))
'''

'''
#7
a = range(1, 6)
print(sum(a))
'''

'''
#8
a = [7, 1, 8, 3]
b = max(a) - min(a)
print(b)
'''

'''
#9
a = [100, 90, 80, 70]
it = iter(a)           # 이터레이터 생성
max_value = next(it)   # 첫 번째 값을 초기값으로 설정

for val in it:
    if val > max_value:
        max_value = val

print(max_value)
'''


'''
#10
data1 = input("숫자를 공백을 두고 입력하세요: ").split()
a = sum(map(lambda x: int(x),data1))
print(a)
'''









