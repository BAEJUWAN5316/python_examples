def make_fuction():
    # i는 지역변수
    base = 10 # 매 make_function 호출 시 마다 생성

    # 함수를 동적으로 생성
    # func = lambda number: number + base

    def func(number):
        return number + base

    return func

ret1 = make_fuction()
print(ret1(1))

ret2 = make_fuction()
ret3 = make_fuction()