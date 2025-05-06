
#49 49번 문제

data1 = input("문자를 넣어주세요. : ")
num = 0
len1 = len(data1)
list1 = []

while True:
    ord1 = ord(data1[num])
    if 88 <= ord1 <= 90:
        ord1 = ord1-23
    
    elif 120 <= ord1 <= 122:
        ord1 = ord1-23
    else:
        ord1 = ord1 + 3

    chr1 = chr(ord1)
    list1.append(chr1)
    num = num + 1

    if num == len1:
        break

print(f"암호화: {"".join(list1)}")