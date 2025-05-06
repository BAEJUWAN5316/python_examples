
#28 28번 문제

data1 = input("텍스트를 입력해주세요. : ")

len1 = int(len(data1)/2) # 입력 텍스트 갯수의 절반값
len2 = len(data1)%2

len3 = data1[int(len1-1):int(len1)+1]
len4 = data1[int(len1):int(len1)+1]

if len2 == 0:
    print(len3)
elif len2 == 1:
    print(len4)  