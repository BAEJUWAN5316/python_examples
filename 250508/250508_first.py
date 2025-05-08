# if 반복문

"""
data1 = input("짜장/짬뽕 중에 선택해주세요. : ")

if data1 == "짜장":
    data2 = input("불짜장/간짜장/쟁반짜장 중에 선택해주세요. : ")

    if "쟁반" in data2:
        print("쟁반짜장을 주문했습니다.")
    else:
        print("주문 불가입니다.")

elif data1 == "짬뽕":
    print("짬뽕을 주문했습니다.")

else:
    print("짜장, 짬뽕 중에 선택해주세요.")
"""


# 리스트 복습
"""
c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]

print(c[2])
print(c[4][3][0:2])
"""

"""
li = []

li.append(1)
li.append(2)
li.append([1, 2])
li[2].append("good")
li.clear()

print(li)
"""

"""
#1
list1 = []

#2
list1.append(1)
list1.append(2)
list1.append([1, 2])

#3
print(list1)

#4
list1.clear()

#5
print(list1)

#7
list1.append("a")
list1.append([4, 5])

list2 = list1.copy()
list2.append("new")

print(list1)
print(list2)
"""

"""
b = [1, 2, 3, [1, 2, 3, 1]]

print(b[2])
print(b[3][2])
print(b.count(1) + b[3].count(1))
"""


# extend
'''
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = "good"
d = ["dodoo"]
'''

# [1,2,3,4,5,6,7,8]로 바꾸려면?
"""
a.extend(b)

print(a)
print(b)
b.extend(c)

print(b)

b.extend(d)

print(b)
"""

# insert
"""
a = [1, 2, 3, 4, 5]

a.insert(0,0)

print(a)
"""

# pop > 하나 추출
'''
a = [1, 2, 3]
b = a.pop(1)

print(a)
print(b)
'''

# remove(값)
'''
c = [1, 2, 3, 1, 1]

c. remove(1)
print(c)
'''

"""
animal1 = ["팬더", "기린", "토끼", "수박", "곰", "망고", "호랑이"]

animal1.insert(3, "코뿔소")

fruit1 = animal1.pop(4)
print(fruit1)

animal1.remove("망고")
print(animal1)
"""


'''
a = [1, 2, 3, 4, 5]
b = a.copy()
b.reverse()

print(b)
'''
#reversed 는 원본데이터를 훼하지 않고 복사한다!
'''
a = [1, 2, 3, 4, 5]
b = (list(reversed(a)))
'''

'''
c = [1, 2, 3, 4, 5]
print(c[::-1])
'''



# a.sort()
# print(a)
'''
a = [5, 4, 3, 2, 1]

b = sorted(a)
print(b)
'''
#sorted(리스트,reverse=False)가 평소의 상태!
#sorted(리스트,reverse=True) = 내림차순 정렬이라는 뜻!


#1번 문제

books = ["파이썬 기초", "데이터 과학 입문", "알고리즘의 이해", "머신러닝 실전", "파이썬 기초"]
print(books)


#2번 문제

count1 = books.count("파이썬 기초")
print(count1)

books.append("웹 개발의 시작")
books.insert(2,"데이터베이스 설계")

new_books = ["인공지능 개론","클라우드 컴퓨팅"]
books.extend(new_books)
print(books)


#3번 문제

books.remove("파이썬 기초")
last_book = books.pop(-1)
print(last_book)

books = sorted(books,reverse=True)
print(books)


#4번문제

top_books = books[0:3]

reversed_selection = list(reversed(books[1:5]))

print(top_books)
print(reversed_selection)

books.clear()
print(books)
