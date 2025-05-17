

# lambda 표현식을 사용하여 이 리스트의 각 요소에 3을 곱하고 2를 더한 새로운 리스트를 반환하는 코드를 작성하세요.


nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))




data = [10, 20, 30, 40, 50]
a = list(map(lambda x: x * 3 + 2, data))
print(a)
