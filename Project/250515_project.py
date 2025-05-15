
# logout 기능


current_user = ["abc123"]
books = [{"title":"원피스", "rented_by":"대여가능"},{"title":"aa", "rented_by": None}]

class library:

    # def __init__(self):
    #     self.data1 = data1

    # 1- 3
    def logout(self, num1):
        if num1 == "1":
            print("로그아웃 되었습니다.")
            current_user.clear()
        elif num1 == "0":
            pass

    # 2- 1
    def show_books(self, num):
        for num,title_book in enumerate(books,1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
            
    


data1 = library()
data2 = library()

f0 = input("로그아웃 하시겠습니까? [1.네 / 2.아니요]")
f2 = "1"

data1.logout(f0)
data2.show_books(f2)








