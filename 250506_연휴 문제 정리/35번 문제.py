
#35 35번 문제

data1 = int(input("첫 번째 수를 입력하세요. : "))
data2 = int(input("두 번째 수를 입력하세요. : "))
data3 = int(input("세 번째 수를 입력하세요. : "))

if data1 > data2 > data3:
    print(f"가장 큰 수: {data1}")
elif data1 > data3 > data2:
    print(f"가장 큰 수: {data1}")
elif data2 > data1 > data3:
    print(f"가장 큰 수: {data2}")
elif data2 > data3 > data1:
    print(f"가장 큰 수: {data2}")
elif data3 > data1 > data2:
    print(f"가장 큰 수: {data3}")
elif data3 > data2 > data1:
    print(f"가장 큰 수: {data3}")