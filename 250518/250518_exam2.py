

#1


'''
#2 
a = "abcdef"

def f(x):
    return x[1::2]

print(f(a))
'''

'''
#3
a = [1, 2, 3, 4, 5]
def f(x):
    b = 0
    list1 = []
    for c in a:
        b = b + c
        list1.append(b)
    return list1
print(f(a))
'''

'''
#4
a = "2024-05-15"
def f(x):
    b = x.split("-")
    c = f"{b[2]}/{b[1]}/{b[0]}"
    return c
print(f(a))
'''

'''
#5
a = ["apple", "banana", "pear"]

def f(x):
    return len(x)

b = sorted(a,key=f,reverse=True)
c = f"{b[0]} {len(b[0])}"
print(c)
'''

'''
#6
import collections
a = [10, 20, 30, 40, 50]

d = collections.deque(a)
d.rotate(1)

print(list(d))
'''

'''
#7
a = input("숫자를 입력하세요 : ").split()

def f(x):
    c = 0
    for b in a:
        b = int(b)
        c = c + b
    return c / len(a)
print(f(a))
'''

'''
#8
a = ['서울', '부산', '인천']

def f(x):
    for i,v in enumerate(x):
        print(f"{i}: {v}")

f(a)
'''

'''
#9
class Student:
    def __init__(self, name, score1):
        self.name = name
        self.score1 = score1

    def score(self):
        if self.score1 >= 90:
            print(f"{self.name}님의 등급은 A입니다.")
        elif self.score1 >= 70:
            print(f"{self.name}님의 등급은 B입니다.")
        elif self.score1 >= 50:
            print(f"{self.name}님의 등급은 C입니다.")
        else:
            print(f"{self.name}님의 등급은 F입니다.")

student = Student("지민", 91)

student.score()
'''

'''
#10
class Account:
    def __init__(self,name,money1):
        self.name = name
        self.money1 = money1

    def send(self, money2):
        print(f"출금 후 잔액: {self.money1 - money2}")

    def gave(self,money3):
        print(f"입금 후 잔액: {self.money1 + money3 }")

account1 = Account("철수",10000)

account1.gave(3000)
account1.send(5000)
'''




    







