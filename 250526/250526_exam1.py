
#1 
data1 = input("문자열을 입력해주세요. : ").split()
data2 = set(data1)
data2 = list(data2)
sort1 = sorted(data2)
print(sort1)


#2
data1 = "hello world hello python python is great"
data2 = data1.split()
dict1 = {}

for v1 in data2:
    num1 = data1.count(v1)
    dict1 = dict1|{v1:num1}

print(dict1)


#3
class Animal:
    def make_sound(self, one):
        self.one = one
        if one == "개":
            print(f"Dog: 멍멍!")
        elif one == "고양이":
            print(f"Cat: 야옹~")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

user = Dog()
user = Cat()

user.make_sound("개")
user.make_sound("고양이")


