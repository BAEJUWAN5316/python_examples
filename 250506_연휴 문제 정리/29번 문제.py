
#29 29번 문제

data1 = input("문장을 입력해주세요. : ")

data1 = data1.replace("!","")
data1 = data1.replace("?","")
data1 = data1.replace(".","")
data1 = data1.replace(",","")
data1 = data1.replace("\'","")
data1 = data1.replace("\"","")

print(data1)