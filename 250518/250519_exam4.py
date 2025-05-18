"""
class User:
    def __init__(self, name, age, city):
        self.name = name
        self.others = Profile(age, city)

    def name1(self):
        return "지민"

class Profile:
    def __init__(self,age,city):
        self.age = age
        self.city = city

    def get_city(self):
        return self.city

    def get_age(self):
        return self.age

user1 = User("지민", 24, "서울")

print(f"이름: {user1.name1()}")
print(f"나이: {user1.others.get_age()}")
print(f"도시: {user1.others.get_city()}")
"""

'''
class Library:
    def __init__(self, library, name, writer):
        self.library = library
        self.name = name
        self.writer = writer
        self.book = Book(name, writer)

    def title(self):
        return self.library

class Book:
    def __init__(self, name, writer):
        self.name = name
        self.writer = writer

    def book_title(self):
        return self.name
    
    def book_writer(self):
        return self.writer


user1 = Library("중앙도서관", "파이썬 배우기", "홍길동")

print(f"[{user1.title()}] 소장 도서: \'{user1.book.book_title()}\' - {user1.book.book_writer()}")
'''

'''
class Order:
    def __init__(self, num, menu, price):
        self.num = num
        self.menu = menu
        self.price = price
        self.item = Item(menu, price)

    def menu_num(self):
        return self.num


class Item:
    def __init__(self, menu, price):
        self.menu = menu
        self.price = price

    def item_menu(self):
        return self.menu
    
    def item_price(self):
        return self.price


user1 = Order(101, "치킨", 18000)

print(f"주문번호 {user1.menu_num()} - 상품: {user1.item.item_menu()} ({user1.item.item_price()}원)")
'''

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_summary(self):
        return f"{self.name} ({self.price}원)"


class Order:
    def __init__(self, order_number, item):
        self.order_number = order_number
        self.item = item  # Item 객체를 속성으로 포함

    def get_order_info(self):
        return f"주문번호 {self.order_number} - 상품: {self.item.get_summary()}"


# 주문 생성 (Item 객체를 먼저 만들고, Order에 전달)
item1 = Item("치킨", 18000)
order1 = Order(101, item1)

# 출력
print(order1.get_order_info())








