
#47 47번 문제

data1 = input("문자를 입력해주세요. : ")

num1 = data1.count("a")
num2 = data1.count("b")
num3 = data1.count("c")

print(f"a{num1}b{num2}c{num3}")


'''
data1 = input("문자를 입력해주세요. : ")
num1 = 0
num2 = 1
len1 = len(data1)
alist = ["a"]
blist = ["b"]
clist = ["c"]
wholelist = []


while True:

    if num2 >= len1:
        break

    if data1[num1] == data1[num2] == "a":
        alist.append(data1[num1])
    elif data1[num1] == data1[num2] == "b":
        blist.append(data1[num1])
    elif data1[num1] == data1[num2] == "c":
        clist.append(data1[num1])

    num1 = num1 + 1

    if  num2 == len1:
        num2 = num2 + 0
    elif num2 != len1:
        num2 = num2 + 1


    if num1 == len1:
        break

if len(blist) == 1:
    blist.remove("b")

if len(clist) == 1:
    clist.remove("c")


print(f"a{len(alist)}b{len(blist)}c{len(clist)}")
'''

'''
data1 = input("문자열을 입력하세요. : ")
len1 = len(data1)
num = 0
list1 = []

while True:
    list1.append(data1[num])
    num = num + 1

    if num == len1:
        break
'''

