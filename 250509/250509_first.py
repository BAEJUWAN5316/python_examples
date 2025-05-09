# CRUD     Create Read Update Delete
#          만들기 읽기 바꾸기 지우기
# 백엔드 언어! 가능한 네 가지!

# 리스트는 crud 다 가능
# 튜플은 r 만 가능


# 셋(set) 자료구조
"""
a = {1, 2, 3, 1}
print(a)

print(len(a))
"""

# 형변환도 가능하다!

a = [ 1, 1 ,1, 2, 2, 3]
#중복된 값을 없애줘

b = set(a)
print(b)

#이걸 다시 리스트로 바꿔줘
c = list(b)
print(c)


c = ["a", 1, 2, 3, 1, "a"]

d = set(c)

e = list(d)
print(e)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"합집합 : {set1 | set2}")
print(f"교집합 : {set1 & set2}")
print(f"차집합 : {set1 - set2}")
print(f"차집합 : {set2 - set1}")


# set 수정 가능

fruits = {'apple', 'banana', 'cherry'}

fruits.add('orange')

print(fruits)

fruits.remove('apple')
print(fruits)


print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")




