# 기능테스트 방법

# 무슨 기능을 만들 지 정의
# 함수의 이름을 정의
# 테스트를 먼저 작성합니다
def mysum(a: int, b: int) -> int:
    '''
    두 인자의 합을 반환합니다
    '''
    # docstring이라고 한다
    # if a ==1 and b == 2:
    #     return 3
    return a + b


# 실패할 것 같은걸 아래처럼 해서 실행해봄
