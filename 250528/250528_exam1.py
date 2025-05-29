#1 은빈1문제

# 1)
'''
def solution():
    data1 = input("숫자를 입력하세요. : ")
    data1 = int(data1)
    result = 0
    for num in range(data1+1):
        if num%2 ==0:
            result = result + num
    return result

print(solution())
'''

# 2)
# def solution():
#     data1 = input("숫자를 입력하세요. : ")
#     data1 = int(data1)


#2 은빈2문제
# list1 = [1,2,3,4,5,2,4,3,5,15,8,9,7,0,1,89,2]
# n = 2

# 1)
# print(list1.count(2))

# 2)
# from collections import Counter
# print((Counter(list1))[2])

# count가 낫지 않을까? 굳이굳이 from으로 가져와서 쓰면 더 메모리를 쓰지 않으려나??

'''
# 가영 1문제

# 정수 n 이 주어질 때, n 이하의 홀수들의 평균을 구해서 return 하도록 solution 함수를 완성하세요.

# [ 조건 ]
# n은 1 이상의 자연수,
# 평균은 소수점 이하 첫째 자리까지 출력(소수점 자리 반올림),
# [ 풀이 방식 ]
# 리스트 컴프리헨션과 sum()/ len()을 이용하여 구하기

def solution():
    data1 = input("1이상의 정수를 입력하세요. : ")

    data1 = int(data1)
    list1 = []
    # for i in range(data1+1):
    #     if i % 2 != 0:
    #         list1.append(i)
    # return round(sum(list1)/len(list1),1)

    list1 = [i for i in range(data1+1) if i % 2 !=0]
    return round(sum(list1)/len(list1),1)

print(solution())
'''



# 가영 2문제
# 학생 이름과 점수가 담긴 딕셔너리 scores가 주어질 때, 
# 가장 점수가 높은 학생의 이름을 return 하도록 solution 함수를 완성하세요.

# [ 조건 ]
# 딕셔너리의 key는 문자열(이름), value는 정수(점수),
# 최고 점수를 받은 학생이 여럿일 경우 아무나 리턴,

# [ 풀이 방식 ]
# max() 함수와 lambda를 사용하여 구하기


scores = {"철수": 85, "영희": 92, "민수": 78, "영지": 88}

def solution():
    result1 = scores.items()
    # print(result1)

    result1 = list(result1)
    # print(result1)

    result2 = max(result1, key=lambda x: x[1])
    print(result2)

    # print(result2[0])

    # return max(result1, key=lambda x: x[1])[0]

solution()
# print(solution())



# 효은 1문제
'''
class Student:
    
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        return sum(self.scores)/len(self.scores)
    
    def get_info(self):
        return f"이름: {self.name}, 평균 점수: {self.get_average()}"
        
s1 = Student("김민수", [80, 90])

s1.add_score(70)
print(s1.get_info())
'''

# 효은 2문제
'''
list1 = [['제주시 C동 사라봉길 31', '제주시 B동 백록담길 63', '제주시 A동 한라산길 61'], 
        {'A동': 63005, 'B동': 63007, 'C동': 63002}]

def solution(data):
    list2 = sorted(list((data[1]).items()),key=lambda x : x[1])
    result = []    
    for a in list2:
        for b in data[0]:
            if a[0] in b:
                result.append(b)
    return result

print(solution(list1))
'''
