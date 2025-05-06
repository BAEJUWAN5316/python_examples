

#13 13번문제


name1, name2 = input("성과 이름을 공백 간격을 두고 입력해주세요. : ").split()
num = 0
num2 = 0
len1 = len(name1)
len2 = len(name2)

list1 = []
list2 = []

while True:
    if name1 == "안":
        list1.append("A")
    elif name1 == "양" or name1 == "연":
        list1.append("Y")
    elif name1 == "복" or name1 == "부" or name1 == "배":
        list1.append("B")
    elif 44032 <= ord(name1[num]) <= 44619:
        list1.append("K")
    elif 45196 <= ord(name1[num]) <= 45771:
        list1.append("N")
    elif 45772 <= ord(name1[num]) <= 46347:
        list1.append("D")
    elif 446924 <= ord(name1[num]) <= 47499:
        list1.append("R")
    elif 47500 <= ord(name1[num]) <= 48075:
        list1.append("M")
    elif 48076 <= ord(name1[num]) <= 48651:
        list1.append("P")
    elif 49228 <= ord(name1[num]) <= 49803:
        list1.append("S")
    elif 50380 <= ord(name1[num]) <= 50955:
        list1.append("L")
    elif 50956 <= ord(name1[num]) <= 51531:
        list1.append("J")
    elif 52108 <= ord(name1[num]) <= 52683:
        list1.append("C")
    elif 53260 <= ord(name1[num]) <= 53835:
        list1.append("T")
    elif 53836 <= ord(name1[num]) <= 54411:
        list1.append("P")
    elif 54412 <= ord(name1[num]) <= 55203:
        list1.append("H")

    num = num + 1

    if num == len1:
        break


while True:
    if name2[num2] == "안":
        list2.append("A")
    elif name2[num2] == "양" or name2[num2] == "연" or name2[num2] == "용":
        list2.append("Y")
    elif name2[num2] == "복" or name2[num2] == "부" or name2[num2] == "배":
        list2.append("B")
    elif name2[num2] == "완":
        list2.append("W")
    elif name2[num2] == "길":
        list2.append("G")
    elif 44032 <= ord(name2[num2]) <= 44619:
        list2.append("K")
    elif 45196 <= ord(name2[num2]) <= 45771:
        list2.append("N")
    elif 45772 <= ord(name2[num2]) <= 46347:
        list2.append("D")
    elif 446924 <= ord(name2[num2]) <= 47499:
        list2.append("R")
    elif 47500 <= ord(name2[num2]) <= 48075:
        list2.append("M")
    elif 48076 <= ord(name2[num2]) <= 48651:
        list2.append("P")
    elif 49228 <= ord(name2[num2]) <= 49803:
        list2.append("S")
    elif 50380 <= ord(name2[num2]) <= 50955:
        list2.append("L")
    elif 50956 <= ord(name2[num2]) <= 51531:
        list2.append("J")
    elif 52108 <= ord(name2[num2]) <= 52683:
        list2.append("C")
    elif 53260 <= ord(name2[num2]) <= 53835:
        list2.append("T")
    elif 53836 <= ord(name2[num2]) <= 54411:
        list2.append("P")
    elif 54412 <= ord(name2[num2]) <= 55203:
        list2.append("H")

    break

fname = "".join(list1)
nname = "".join(list2)

print(f"이니셜: {fname}.{nname}.")