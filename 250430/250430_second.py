
'''
a = "good"

b = "a" in a

print(len("10"))


a = 10
b = 20
c = 20

li = [10, 20, 30, 40]

'''

'''
x = [1, 2, 3]
y = ['apple', 'banana', 'cherry',1 ]
t = ['a', ['c','d'],'c']
z =  2 in [1, 2, [1, 2, 3]]
print(z)
'''

'''
#리스트
li = [1, 2, ["대한", "민국", [56, "Korea"], 34], "만세"]
print(len(li))

t = [1,2,3,[4,5,6]]
print(t[3])

t2 = [1,2,3,[4,5,[2,31]],1]
print(t2[3][2][0:2])

# print(t2[10000])


#수정

t2[0] = 5
print(t2)

t3 = [5,4,3,[2,1]]

t3[0] = 1
t3[1] = 2
t3[3][0] = 4
t3[3][1] = 5
print(t3)
'''

t4 = []

t4.append(1)
print(t4)

t4.append(2) #appen는 리스트의 뒤에 붙인다. 리스트가 이미 있으면 어펜드로 넣은 데이터는 맨 뒤로!
print(t4)

t4.clear() # 해당 리스트의 데이터를 다 지운다.
print(t4)

t4.append(3)
t4.remove(3) # 리스트 안에서 3이란 겂을 찾아 지운다.
print(t4)

t4 = [5,4,3,2,1] 
t4.sort() # 오름차순 정렬 > 하지만 오리지날 데이터를 바꾸면 안 된다!
print(t4)

# 리스트 만들 때 방법
a = [1, 2]
b = list()
# 두 개가 같다
print(str(a))

data = t4.pop() #t4 리스트에서 제일 오른쪽 값을 추출해서 data 변수에 저장