
#11 평균 점수 카운팅
'''
list1 = [[92, 85, 97], [30, 21, 60], [90, 99, 98], [0, 0, 0], [81, 80, 88, 83]]

def solution(data):
    num = 0
    for value in data:
        if sum(value)/len(value) >= 80:
            num += 1
    return num

print(solution(list1))
'''


#13 도서관 책 연도별 정렬
'''
list1 = [['Moby Dick', 'To Kill a Mockingbird', '1984'], 
        {'Moby Dick': 1851, 'To Kill a Mockingbird': 1960, '1984': 1949}]
def solution(data):
    list_book = data[1].items()
    list_book = list(list_book)
    sorted_book = sorted(list_book,key= lambda x : x[1])
    list_sbook = []
    for value in sorted_book:
        list_sbook.append(value[0])
    return list_sbook

print(solution(list1))
'''


#14 도서관 책 코드별 정렬
'''
dict1 = {'AX21': 'Moby Dick', 'BX32': '1984', 'CX14': 'To Kill a Mockingbird'}
def solution(data):
    books = data.items()
    books = list(books)
    s_books = sorted(books, key= lambda x : x[0])
    list_b = []
    for value in s_books:
        list_b.append(value[1])
    return list_b

print(solution(dict1))
'''


#15 위니브 회의 시간표 정렬
'''
list1 = ['01:00 PM', '11:30 AM', '12:45 PM', '09:00 AM', '12:00 AM']
def solution(data):
    list_p = []
    list_a = []
    for value in data:
        if value[6] == "P":
            list_p.append(value)
        elif value[6] == "A":
            list_a.append(value)
    list_p.sort()
    list_a.sort()
    list_p.reverse()
    list_a.reverse()

    list_p12 = []
    list_a12 = []

    for value in list_p:
        if value[0:2] == "12":
            value2 = list_p.pop(0)
            list_p12.append(value2)
    for value in list_a:
        if value[0:2] == "12":
            value2 = list_a.pop(0)
            list_a12.append(value2)

    list_p.sort()
    list_a.sort()
    list_p12.sort()
    list_a12.sort()

    return list_a12+list_a+list_p12+list_p

print(solution(list1))
'''


