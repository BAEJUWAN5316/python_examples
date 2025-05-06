
#43 43번 문제

data1 = input("문장을 입력하세요. : ")
data1 = data1.lower()
num1 = 0
len1 = len(data1)
list1 = []
list2 = []
list3 = []

while True:
    if data1[num1] == "a":
        list1.append(data1[num1])
    elif data1[num1] == "e":
        list1.append(data1[num1])
    elif data1[num1] == "i":
        list1.append(data1[num1])
    elif data1[num1] == "o":
        list1.append(data1[num1])
    elif data1[num1] == "u":
        list1.append(data1[num1])
    elif data1[num1] == " ":
        list3.append(data1[num1])
    else:
        list2.append(data1[num1])
    
    num1 = num1 + 1

    if num1 == len1:
        break

alen = len(list1)
blen = len(list2)

print(f"모음 개수: {alen}")
print(f"자음 개수: {blen}")
