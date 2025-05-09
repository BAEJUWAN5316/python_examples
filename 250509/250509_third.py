

'''
num = 0
s = [1, 2, "즐", 4]

for i in s:
    print(i)
'''
    
'''
for i in range(0,10,-1): # 0부터 4999까지 어떤 순회 가능한 데이터를 만든다.
    print(i)
'''

# range(10,51) 이라고 하면 10~50까지의 거리를 측정한다.
# range(1,11,2) 이라고 하면 1 3 5 7 9 이라고 나온다 : 1~10까지 2계단씩 점프

'''
#!
for a in range(1,101):
    print(a)

#2
for a in range(2,51,2):
    print(a)

#3
for a in range(10,-2,-1):
    print(a)
'''

num = 0

for i in range(3):
    for j in range(2):
        for o in range(2):
            num = num + 1

print(num)








