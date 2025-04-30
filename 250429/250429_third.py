'''
# if 문
age = 20
height = 101

if age > 18 and height >= 150:
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")

print("안녕하세요.")

# if ~ else 구문 = if가 참이 아니면 else 구문을 실행하는 것


age = 20

if age >= 30:
    print("30대 이상입니다.")
else:
    print("30대가 아닙니다.")


# if ~ elif ~ else 구문

age = 20

if age <= 19:
    print("청소년입니다.")

elif age < 30:
    print("성인입니다.")

else:
    print("30대 이상입니다.")
'''


day1 = input("생년월일을 yyyy mm dd 양식으로 작성해주세요 : ")

day2, day3, day4 = day1.split()
day5=int(day2)

ja = day5%2

if ja == 1:
    print("홀수 년도에 테어났습니다.")

else:
    print("짝수 년도에 태어났습니다")
