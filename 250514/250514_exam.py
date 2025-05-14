# 1번
"""
def print_name(a):
    print(f"내 이름은 {a}입니다")


a = input("이름을 작성해주세요. : ")
print_name(a)
"""

# 2번
"""
def double(a):
    a = int(a)
    return a*2

a = input("2배로 계산 할 숫자를 입력하세요. : ")
print(double(a))
"""

# 3번
"""
def add(a,b):
    a = int(a)
    b = int(b)
    return a + b

a,b = input("숫자 두 개를 공백을 두고 입력해주세요. : ").split()
print(add(a,b))
"""

# 4번

'''
def string_Length(st1):
    return len(st1)


data1 = input("문자를 입력하세요. : ")

print(string_Length(data1))
'''

#5번
'''
def is_even(int1):
    return int(int1) % 2 == 0

data1 = input("숫자를 입력하세요. : ")
print(is_even(data1))
'''


#6번
'''
def total(x):
    return sum(x)

data1 = [1, 2, 3, 4, 5]
data2 = [5, 6, 7]
print(total(data1))
'''

#7번
'''
def first_Latter(x):
    return x[0]

data1 = input("문자를 입력하세요.")
print(first_Latter(data1))
'''

#8번
'''
def to_upper(x):
    return x.upper()

data1 = input("영문을 입력해주세요. : ")
print(to_upper(data1))
'''

#9번
'''
def max_num(x):
    return max(x)

data1 = [3, 7, 500, 9]
print(max_num(data1))
'''

#10번
'''
def bigger(a,b):
    if data1 >= data2:
        return a
    else:
        return b

data1, data2 = input("두 수를 입력해주세요. : ").split()
print(bigger(data1, data2))
'''
'''
#11번

def filter_even(a):
    return a%2 == 0
    

a = [1, 2, 3, 4, 5, 6]

print(list(filter(filter_even,a)))
'''

#12번
'''
students = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 78}
]

def sort_by_score(students):
    return students["score"]


a = sorted(students,key=sort_by_score,reverse = True)
print(a)
'''
'''
list1 = []

def average(x):
    return sum(x)/len(x)

while True:
    data1 = input("숫자들을 공백을 두고 입력해주세요. : ")
    

    if data1 != "0":
        data1 = int(data1)
        list1.append(data1)
    elif data1 == "0":
        break
    elif data1 == '':
        print("숫자가 없습니다")
    else:
        print("숫자가 없습니다")


print(average(list1))
'''
