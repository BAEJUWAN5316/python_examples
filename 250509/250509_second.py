

'''
# 딕셔너리 dict()

# key:value 형태로 만들어져 있다.

my_dict = {"me":"길동"}
# me 는 key
# 길동은 값
# :을 중괄호 안에 넣으면 이건 dict로 보는구나 라고 인식!

my_dict2 = dict()
my_dict2_1 = dict([("one","하나"),("two","둘")])
my_dict2_2 = dict(("me", "길동"))
# 이건 튜플 기준으로 키, 값이 나뉜다!

my_dict3 = {'me':[1,2,3], "me2":"good"}
# value(값) 란에는 여러 타입이 들어갈 수 있다
# 여러 개의 딕셔너리를 넣을 수도 있다.
'''

'''

# 데이터 추가

dict4 = dict()
dict4["max"] = "노잼"
# max가 키, 노잼이 값
# 키에도 여러 타입이 되는데 거의 문자열만 사용한다!


data1 = dict()
data1["key1"] = [1, 2, "삼"]
data1["key2"] = ("a", "b", (4, 5))
data1["key3"] = {"key3-1":(1,(2,3),6)}
data1["key4"] = {1, 2, 3}
data1["key5"] = "방가루"

print(data1)

# 데이터 출력하기
a = data1["key5"]

print(a)

# 데이터 수정하기
data1["key5"] = "우하하"
print(data1)
'''

person = {'name': 'licat', 'age': 25, 'height': 165.5}

person['name'] = "Juwan"
person["weight"] = 500

print(person)


# 데이터 삭제하기

del person['height']
print(person)


# person['height'] = None #키는 남기고 값은 없애고 싶을 때

data = {"key":[1, 2, 3]}
print(data["key"])

data["key"].remove(3)
print(data["key"])

b = {"good1":{"good2":[1, 2, 3,[1, 2, 3]]}}

b["good1"]["good2"][3].append(4)
print(b)

person = {'name':"licat", "age" : 25, "city" : "seoul"}

# get 이란 기능

city = person.get('city',"없는뎅")
print(city)

city2 = person.get('city2',"없는뎅")
print(city2)


# 키만 가져오려면!

person_keys = person.keys()
print(list(person_keys)[1])


# value 만 가져오려면

person_keys = person.values()
print(list(person_keys))


# 전체를 추출하려면

person_items = person.items()
print(list(person_items))

a = person.pop("age") # age라는 키에 있는 값을 a에 저장 > 지운 값을 기억(저장) 할 수 있다!