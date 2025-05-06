
#23 23번 문제

d1, d2, d3, d4, d5, d6 = input("문장을 입력하세요. : ").split()
data1 = input("찾을 단어를 입력하세요. : ")
data2 = d1+d2+d3+d4+d5+d6

print(f"단어 \'{data1}\'의 위치: {data2.find(data1)+1}")