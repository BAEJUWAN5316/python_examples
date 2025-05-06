
#39 39번 문제

data1 = input("숫자를 입력해주세요 : ")
len1 = len(data1)
num = 0
hop1 = 0


while True:
    hop1 = hop1 + int(data1[num])
    num = num + 1

    if num == len1:
        break

print(f"자릿수 합계: {hop1}")