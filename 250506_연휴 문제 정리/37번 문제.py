
#37 37번 문제

data1 = input("문자열을 입력하세요. : ")
data2 = input("위의 문자열에서 찾을 단어를 입력하세요. : ")

if data1.find(data2) >= 0:
    print(f"\"{data1}\"에 \"{data2}\"이(가) 포함되어 있습니다.")
elif data1.find(data2) < 0:
    print(f"\"{data1}\"에 \"{data2}\"이(가) 포함되어 있지 않습니다.")