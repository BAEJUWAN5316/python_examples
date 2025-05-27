# # def decorator(func):
# #     def wrapper():
# #         print("함수를 실행하기 전에 알려줘!")
# #         func()
# #     return wrapper

# # @decorator
# # def say_hello():
# #     print("안녕!")

# # say_hello()


# # #1 

# # def decorator(func):
# #     def wrapper():
# #         print("안녕하세요!")
# #         func()
# #     return wrapper

# # @decorator
# # def say_hello():
# #     print("나는 파이썬을 좋아해!")

# # say_hello()


# #2

# # def decorator(func):
# #     def wrapper():
# #         func()
# #         print("감사합니다!")
# #     return wrapper

# # @decorator
# # def say_name():
# #     print("제 이름은 주완이에요.")

# # say_name()


# #3
# # def decorator1(func):
# #     def wrapper():
# #         print("시작합니다!")
# #         func()
# #         print("끝났어요!")
# #     return wrapper

# # @decorator1
# # def work():
# #     print("열심히 일하는 중...")


# # work()



# #2
# user_logged_in = False

# def login_required(func):
#     def wrapper():
#         if user_logged_in == True:
#             func()
#         elif user_logged_in == False:
#             print("로그인이 필요합니다!")
#     return wrapper


# @login_required
# def view_profile():
#     print("프로필을 보여줍니다.")

# view_profile()



# #3

# def repeat(func, num):
#     def wrapper():
#         for a in range(num):
#             func()
#     return wrapper




# @repeat(3)
# def greet():
#     print("안녕하세요!")

# 희현문제 1번


def student_grade_manager():
    students = {}
    student_data = [("김철수",85),("이영희",92),("박민수",78),("최지영",88)]
    while True:
        print("1. 학생 추가")
        print("2. 전체 학생의 평균 계산")
        print("3. 80점 이상인 학생들만 출력")
        print("4. 점수 순으로 학생 순위 출력")
        print("5. 종료")
        sel_m = input("메뉴를 선택하세요 : ")
    
        if sel_m == "1":
            for i,v in enumerate(student_data,1):
                print(f"{i}. {v[0]}/{v[1]}")
            sel1 = input("추가 할 학생의 번호를 입력하세요. : ")
            sel1 = int(sel1)
            students = students|{student_data[sel1-1][0]:student_data[sel1-1][1]}
            student_data.pop(sel1-1)
            print(students)
            print(f"{student_data[sel1-1][0]}학생이 추가되었습니다.")
        
        elif sel_m == "2":
            if sum(list(students.values())) == 0:
                print("등록된 학생이 없습니다.")
            else:
                print(f"전체 학생의 평균 점수 : {sum(list(students.values()))/len(students)}")

        elif sel_m == "3":
            if len(students) == 0:
                print("등록된 학생이 없습니다.")
            else:
                print(students)
                sorted_list = sorted(students, key=lambda x: x[1])
                print(sorted_list)


    



    # 학생 데이터 초기화
    #1. 학생 추가
    #2. 전체 학생의 평균 점수 계산
    #3. 80점 이상인 학생들만 출력
    #점수 순으로 정렬(내림차순)
    #4. 점수 순으로 학생 순위 출력
    #전체 학생을 점수 순으로 정렬

#실행
student_grade_manager()




# 희현문제 2번
'''
lista = [1, 11, 111, 1111]
listb = [10, 21, 31, 101]
listc = []

def solution(list1):
    list2 = []
    for a in list1:
        a = str(a)
        list2.append(a)
    list3 = "".join(list2)
    c = list3.count("1")
    return c

print(solution(lista))
'''
