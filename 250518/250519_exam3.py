
class LoginManager:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.log = Fin()

    def add1(self, num2):
        print(self.num + num2)

class Fin:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def add2(self, num2):
        print(self.num +100)

user1 = LoginManager("영수", 100)
user2 = LoginManager("철수", 250)
user3 = LoginManager("지민", 31)

user1.add1(30)
user1.log.add2("한국", 50)



'''
class Cart:
    def __init__(self):
        self.items = {}  # 딕셔너리로 물건과 가격 저장

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"{item}은 장바구니에 없습니다.")

    def get_total(self):
        return sum(self.items.values())

    def show_cart(self):
        if not self.items:
            print("장바구니가 비어 있습니다.")
        else:
            print("🛒 장바구니 내용:")
            for item, price in self.items.items():
                print(f"- {item}: {price}원")


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()  # 사용자마다 자신만의 Cart 객체를 가짐

    def add_to_cart(self, item, price):
        self.cart.add_item(item, price)
        print(f"{item}을(를) 장바구니에 추가했습니다.")

    def checkout(self):
        total = self.cart.get_total()
        print(f"{self.name}님의 총 결제 금액은 {total}원입니다.")
        self.cart = Cart()  # 장바구니 초기화 (결제 후 비우기)

u1 = User("지훈")

u1.add_to_cart("우유", 2000)
u1.add_to_cart("초콜릿", 1500)
u1.cart.show_cart()

u1.checkout()
u1.cart.show_cart()
'''