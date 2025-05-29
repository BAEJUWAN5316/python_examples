

#1 더하기
'''
list1 = [3, 5, 7, 1]

def solution(data):
    num = 0
    for value in data:
        if value%2 != 0:
            num += value
    return num

print(solution(list1))
'''


#2 곱하기
'''
list1 = [3, 5, 7, 1]

def solution(data):
    num = 0
    for value in data:
        if num == 0:
            num = 1
        num = num * value
    return num

print(solution(list1))
'''


#3 조건 덧셈
'''
list1 = [3, 5, 7, 1]
def solution(data):
    num = 0
    for value in data:
        if value%3 == 0:
            continue
        elif value%5 == 0:
            continue
        else:
            num += value
    return num

print(solution(list1))
'''


#4 크리스마스 쿠키
'''
list1 = ['쿠키 1개', '쿠키 2개', '쿠키 3개']
def solution(data):
    num = 0
    num += int(data[0][3]) * 1
    num += int(data[1][3]) * 2
    num += int(data[2][3]) * 3
    return num

print(solution(list1))
'''


#6 문자열 덧셈
'''
str1 = '1q2w3e4r'	
def solution(data):
    num = 0
    for value in data:
        if value.isdigit() == True:
            num += int(value)
    return num

print(solution(str1))
'''


#7 업무 우선순위
'''
list1 = [['A', 1], ['B', 2], ['C', 3]]
def solution(data):
    list_f = []
    sorted_list = sorted(data,key=lambda x : x[1])
    for value in sorted_list:
        list_f.append(value[0])
    return list_f

print(solution(list1))
'''


#8 두 점 사이의 거리
'''
list1 = [1, 10, 20, 25, 31, 40]
def solution(data):
    list_dot = []
    for value in range(len(data)):
        if value+1 == len(data):
            continue
        else:
            list_dot.append(data[value+1] - data[value])
    return [data[list_dot.index(min(list_dot))], data[list_dot.index(min(list_dot))+1]]

print(solution(list1))
'''


#9 수학은 내가 1등
'''
list1 = [{'이름': 'A', '국': 21, '영': 33, '수': 54}, {'이름': 'B', '국': 32, '영': 43, '수': 11}]
def solution(data):
    score_list = sorted(data, key=lambda x: x['수'],reverse=True)
    return score_list[0]['이름']

print(solution(list1))
'''


#10 게임 밸런스 조절
'''
list1 = [['Gray', 98, 92, 85, 97], ['Gom', 98, 30, 21, 60], ['Allosa', 98, 90, 99, 98]]
def solution(data):
    list_char = []
    for value in data:
        if value[1] + value[2] + value[3] + value[4] >= 350:
            list_char.append(value[0])
    list_char2 = sorted(list_char)
    return list_char2

print(solution(list1))
'''