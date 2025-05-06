
#27 27번 문제

data1 = input("단어를 입력해주세요. : ")
data2 = int(input("원하는 글자 수를 입력해주세요. : "))

data3 = data2 - int(len(data1))

print(data1+("*"*data3))