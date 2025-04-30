
ham = [0, 10, 10] # 친밀도, 포만감, 건강


print(f'''
****************
햄 스 터 키 우 기
****************
''')

name = input("햄스터의 이름을 지어주세요. : ")

print(f'''
햄스터의 친밀도를 30으로 만들어보세요.
각 수치는 [친밀도, 포만감, 건강]을 뜻합니다.
포만감, 건강이 0이 되면 게임오버입니다.
''')


p1 = f"햄스터 {name} 와(이와) 무엇을 하시겠습니까.[밥먹기/운동하기/점수보기] : "

s1 = f"{name}(이)는 밥을 맛있게 먹었습니다. 하지만 살이 쪘습니다. [친밀도+10 포만감+5 건강-2]"
s2 = f"{name}(이)는 쳇바퀴를 열심히 굴렸습니다. 하지만 배가 고파졌습니다. [친밀도+10 포만감-2 건강+5]"
s3 = f"축하합니다. 햄스터 {name}(이)와 친해졌습니다. *HAPPY ENDING"
s4 = f"햄스터 {name}(이)는 배가 고파 정신을 잃었습니다. *GAME OVER"
s5 = f"햄스터 {name}(이)는 더이상 힘이 없어 정신을 잃었습니다. *GAME OVER"

o1 = "밥먹기"
o2 = "운동하기"
o3 = "점수보기"
o4 = "에러"

bo = ham[0] < 30 and ham[1] > 0 and ham[2] > 0 # 계속진행
b1 = ham[0] >= 30 and ham[1] > 0 and ham[2] > 0 # 해피엔딩
b2 = ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0 # 포만감0
b3 = ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0 # 건강0

go1 = "error"

dateo = input(p1)
if dateo == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif dateo == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif dateo == o3:
    print(ham)


if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")


if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")



if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")


if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")



if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")



if ham[0] < 30 and ham[1] > 0 and ham[2]:
    date1 = input(p1)
elif ham[0] >= 30 and ham[1] > 0 and ham[2] > 0:
    date1 = o4
    print(s3)
elif ham[0] < 30 and ham[1] <= 0 and ham[2] >= 0:
    date1 = o4
    print(s4)
elif ham[0] < 30 and ham[1] >= 0 and ham[2] <= 0:
    date1 = o4
    print(s5)

if date1 == o1:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] + 5
    ham[2] = ham[2] - 2
    print(s1)
elif date1 == o2:
    ham[0] = ham[0] + 10
    ham[1] = ham[1] - 2
    ham[2] = ham[2] + 5
    print(s2)
elif date1 == o3:
    print(ham)
elif date1 == o4:
    print("")