
#21 21번 문제

data1, data2 = input("문장을 입력해주세요. : ").split()

print(data1.upper(), data2.upper())
print(data1.lower(), data2.lower())
print(data1.title(), data2.title())

data3 = data1.replace(data1[0],data1[0].upper())
data4 = data2.replace(data2[0],data2[0].upper())
print(data3, data4)