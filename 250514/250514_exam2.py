
#1
'''
data1 = [1, 1, 3]

list1 = []

def is_all_positive(a):
    for x in a:
        if x > 0:
            list1.append(True)
        elif x <= 0:
            list1.append(False)
    return all(list1)

print(is_all_positive(data1))
'''

#2
'''
data1 = [1, 4, 5]

list1 = []

def has_even(a):
    for x in a:
        if x%2 == 0:
            list1.append(True)
        elif x <= 0:
            list1.append(False)
    return any(list1)

print(has_even(data1))
'''

'''
#3
list1 = [1, 2, 3]
def convert_to_str(a):
    print(list(map(str,a)))

convert_to_str(list1)
'''


#4
'''
list1 = []
def ascii_codes(a):
    for _,str1 in enumerate(a):
        list1.append(str1)
    print(list(map(ord,list1)))
    

ascii_codes("abc")
'''


#5
'''
names = ["철수", "영희"]
scores = [85, 92]

def pair_names_scores(names, scores):
    print([(names[0],scores[0]),(names[1],scores[1])])


pair_names_scores(names, scores)
'''


#6
'''
def format_score(a):
    print(f"점수: {a}점")

format_score(85)
'''


#7
'''
def longest_word(a):
    list1 = a.split()
    list2 = []
    for b in list1:
        list2.append(len(b))
    num = list2.index(max(list2))
    print(list1[num])

data1 = input("문장을 입력하세요. : ")
longest_word(data1)
'''


#8
'''
list1 = [4, 8, 2, 10]

def analyze_list(a):
    list2 = []
    list2.append(sum(list1))
    list2.append(max(list1))
    list2.append(min(list1))
    print(list2)

analyze_list(list1)
'''


#9
'''
def convert(a):
    if type(a) == str:
        a = ord(a)
    elif type(a) == int:
        a = chr(a)
    print(a)

data1 = 65
convert(data1)
'''

#10
'''
list1 = ["banana", "apple", "cherry"]

def numbered_reverse_sorted(a):
    list2 = []
    b = sorted(a,reverse=True)
    for num1,num2 in enumerate(b,1):
        list2.append(f"{num1}. {num2}")
    print(list2)



numbered_reverse_sorted(list1)
'''

#1 다시
'''
list1 = [1, 1, 1]

def has_even(a):
    return any(x%2 == 0 for x in a)

print(has_even(list1))
'''



