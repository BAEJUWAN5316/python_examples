#1 키오스크 시스템
'''
class LoginManager:
    def login(self, id, pw):
        if id == "admin" and pw == "1234":
            print("로그인 성공")
        else:
            print("로그인 실패")


class MenuManager:
    def show_menu(self):
        self.list1 = ['라면', '김밥', '삼각김밥']
        print(self.list1)

class OrderManager:
    def order(self, item):
            print(f"{item} 주문 완료")

class KioskSystem:
    def __init__(self):
        self.loginmanager = LoginManager()
        self.menumanager = MenuManager()
        self.ordermanager = OrderManager()


user1 = KioskSystem()

print("반갑습니다 키오스크입니다.")
print("선택하실 기능을 번호로 입력해주세요.")

while True:
    print("1. 로그인하기")
    print("2. 메뉴 확인하기")
    print("3. 주문하기")
    select1 = input("번호를 입력해주세요. : ")

    if select1 == "1":
        select1_1 = input("아이디를 입력해주세요.")
        select1_2 = input("비밀번호를 입력해주세요.")
        user1.loginmanager.login(select1_1,select1_2)
    elif select1 == "2":
        user1.menumanager.show_menu()
    elif select1 == "3":
        select3_1 = input("주문할 메뉴를 입력해주세요")
        user1.ordermanager.order(select3_1)
    elif select1 == "0":
        break

print("안녕히 가세요!")
'''

#2 온라인 강의 수강 시스템 만들기

class UserManager:
    def register(self):
        print("사용자 등록을 하겠습니다")
        name1 = input("이름을 입력해주세요. : ")
        num1 = input("학번을 입력해주세요. : ")
        self.list1 = []
        self.list1.append({name1:num1})

class CourseManager:
    def list_courses(self):
        course_list = ["Python", "HTML", "AI"]
        print("수강 가능 수업")
        for i,v in enumerate(course_list,1):
            print(f"{i}. {v}")

class EnrollmentManager:
    def enroll(self):
        sel1 = input("수강 할 강좌를 입력해주세요. : ")
        print(f"{sel1}강좌가 수강신청되었습니다.")

class OnlineSystem:
    usermanager = UserManager()
    coursemanager = CourseManager()
    enrollmentmanager = EnrollmentManager()

    def start(self):
        print("--수강 시스템--")
        print("1. 사용자 등록하기")
        print("2. 수강 가능 수업 확인하기")
        print("3. 수강신청하기")
        print("0. 종료하기")
        data1 = input("번호를 선택하세요.")
        return data1
    
    def run(self):
        while True:
            a = self.start()
            if a == "1":
                self.usermanager.register()
            elif a == "2":
                self.coursemanager.list_courses()
            elif a == "3":
                self.enrollmentmanager.enroll()
            elif a == "0":
                print("감사합니다!")
                break

user1 = OnlineSystem()

# while True:
#     a = user1.start()
#     if a == "1":
#         user1.usermanager.register()
#     elif a == "2":
#         user1.coursemanager.list_courses()
#     elif a== "3":
#         user1.enrollmentmanager.enroll()
#     elif a == "0":
#         break

user1.run()




