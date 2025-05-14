"""
class Car: # 차에 설계 도면 또는 차 공장, 클래스
    count = 0         # 멤버 또는 애트리뷰트
    max_speed = 300   # 멤버 또는 애트리뷰트
    max_people = 5    # 멤버 또는 애트리뷰트

    def start(self): # 메서드
        print('차가 출발합니다!')

    def stop(self): # 메서드
        print('차가 멈췄습니다!')

# 공장에서 생산된 자동차 modelx, modely 인스턴스
modelx = Car() # 인스턴스 = 클래스()
modely = Car()

modelx.start()
modelx.stop()
"""

# 1
"""
class Dog:

    def bark(self):
        print("멍멍!")

dog = Dog()

dog.bark()
"""

# 2
"""
class Robot:
    
    def hello(self):
        print("안녕하세요, 저는 로봇입니다")

robot1 = Robot()
robot2 = Robot()

robot1.hello()
robot2.hello()
"""


# 3
"""
class Person:
    
    def __init__(self, name):
        self.name = name
       
    
    def say_hello(self):
        print(f"안녕하세요, 저는 {self.name}입니다")


person1 = Person("해이")
person2 = Person("이루")

person1.say_hello()
person2.say_hello()
"""


# 4
"""
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def describe(self):
        print(f"이 차는 {self.color}색 {self.brand}입니다")


car = Car("초록", "벤츠")

car.describe()
"""


# 5
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_older_than(self, other1, other2):
        if self.age > other.age:
            print(f"{self.name}은 {other.name}보다 나이가 많습니다.")
        elif self.age < other.age:
            print(f"{other.name}은 {self.name}보다 나이가 많습니다.")
        else:
            print(f"{self.name}은 {other.name}와 나이가 같습니다.")
    

person1 = Person("김이웅", 30)
person2 = Person("안기구", 30)
person3 = Person("강가국", 80)

person1.say_older_than(person2, person3)
"""


# 6
"""
species = "물개"

class Animal:
    species = "동물"

    def speak(self):
        print(f"나는 {self.species}입니다")

animal = Animal()

animal.speak()
"""


# 7
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"저는 {self.grade}학년 {self.name}입니다.")


student1 = Student("김영웅", 1)
student2 = Student("이지훈", 3)
student3 = Student("양명훈", 6)

student1.introduce()
student2.introduce()
student3.introduce()
"""


# 8
"""
class Lamp:
    on = False
    print(on)

    def turn_on(self):
        self.on = True
        print("불을 켭니다")
        print(self.on)


lamp = Lamp()

lamp.turn_on()
"""


# 9
"""
class Counter:
    count = 0
    def __init__(self):
        self.count=0

    def increase(self):
        self.count += 1

    def show(self):
        print(self.count)


counter = Counter()

counter.increase()
counter.increase()
counter.increase()
counter.increase()
counter.show()
"""

# 10
"""
class Calculator:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)


calculator = Calculator(8,4)

calculator.add()
calculator.sub()
calculator.mul()
calculator.div()
"""

"""
class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.author}, {self.pages})"
    
    def __gt__(self, other):
        return self.pages > other.pages




book1 = Book("파이썬 기초", "김코딩", 200)
book2 = Book("자바 기초", "이자바", 300)

print(book1)
print(book2 > book1)
"""

'''
class Calculator:
    def __init__(self):
        self.x = []

    def add(self, a, b):
        self.x.append(f"{a} + {b} = {a+b}")
        return a + b

    def subtract(self, a, b):
        self.x.append(f"{a} - {b} = {a-b}")
        return a - b

    def multiply(self, a, b):
        self.x.append(f"{a} * {b} = {a*b}")
        return a * b

    def divide(self, a, b):
        self.x.append(f"{a} / {b} = {a/b}")
        return a / b

    def get_history(self):
        return self.x
    
    def get_last_result(self):
        return self.x[-1][-1]


calc = Calculator()

print(calc.add(5, 3))
print(calc.subtract(10, 7))
print(calc.multiply(4, 2))
print(calc.divide(9, 3))
print(calc.get_history())
print(calc.get_last_result())
'''

'''
class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append([name,score])

    def print_grades(self):
        print(self.students)

    def get_highest_grade(self):
        def f(x):
            return x[1]
        return sorted(self.students,key=f,reverse=True)[0]

    def get_average(self):
        def f(x):
            return x[1]
        return sum((map(f,self.students)))/len(self.students)





gradebook = GradeBook()

gradebook.add_student("김철수", 85)
gradebook.add_student("이영희", 92)
gradebook.add_student("박민수", 78)
gradebook.add_student("정지원", 95)

gradebook.print_grades()  #
print(f"최고 점수: {gradebook.get_highest_grade()}") 
print(f"평균 점수: {gradebook.get_average()}") 
'''

'''
class Lecture:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.list = []

    def add_student(self, student_name):
        
        if len(self.list) != self.max_students:
            self.list.append(student_name)

        elif len(self.list) == self.max_students:
            print("정원이 초과되었습니다.")

    def get_status(self):
        print(f"[{self.name}] 수강 인원: {len(self.list)} / {self.max_students}명")


lec = Lecture("파이썬 중급", 3)

lec.add_student("김민수")
lec.add_student("박지현")
lec.add_student("김지수")
lec.add_student("이지수")
lec.get_status()  #→ "수강 인원: 2 / 3명"
'''

'''
class Book:
    def __init__(self, book_name, writer, is_borrowed):
        self.book_name = book_name
        self.writer = writer
        self.is_borrowed = is_borrowed

    def borrow(self, user):
        if self.is_borrowed == 1:
            self.is_borrowed = 0
            print("대출 완료되었습니다.")
        elif self.is_borrowed == 0:
            print("이미 대출된 책입니다.")

    def return_book(self):
        self.is_borrowed = 1
        print("책이 반납되었습니다.")

class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        if book1




# 예시 실행:
book1 = Book("1984", "George Orwell", 1)

user1 = User("정연우")

user1.borrow_book(book1)  #→ "정연우님이 '1984'를 대출했습니다."
user1.borrow_book(book1)  #→ "이미 대출된 책입니다."
'''


class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        owner_list = []
        owner_list.append({self.owner:self.balance})

    def transfer_to(self, to_owner, won1):
        self.balance = self.balance - won1
        
    def withdraw(self, won2):
        self.balance





acc1 = BankAccount("김영희", 1000)
acc2 = BankAccount("이철수", 500)


'''
acc1.transfer_to(acc2, 300)
acc2.withdraw(100)

acc1.get_log() # → ["300원을 이철수에게 이체함"]
acc2.get_log() # → ["300원을 김영희로부터 받음", "100원 출금함"]
'''



