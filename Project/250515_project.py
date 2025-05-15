
# logout 기능


current_user = ["abc123"]
books = [{"title":"원피스", "rented_by":"대여가능"},{"title":"aa", "rented_by": None}]

class library:

    # def __init__(self):
    #     self.data1 = data1

    # 1- 3
    def logout(self, current_user):
        confirm = input("로그아웃 하시겠습니까? [1.네 / 2.아니요]")

        if confirm == "1":
            print("로그아웃 되었습니다.")
            current_user.clear() # 현재 사용자 정보 초기화
            return True
        elif confirm == "0":
            print("로그아웃이 취소되었습니다.")
            return False
        else:
            print("잘못된 입력입니다. 0 또는 1을 입력해주세요.")
            return False

    # 2- 1
    def show_books(self, num):
        for num,title_book in enumerate(books,1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
            
    
data1 = library()
data2 = library()

# 테스트

while True:
    sel1 = input("원하는 메뉴를 선택하세요 [1.도서목록 / 2.로그아웃 및 종료] : ")

    if sel1 == "1":
        data2.show_books(sel1)

    elif sel1 == "2":
        data1.logout(current_user)
        






f0 = input("로그아웃 하시겠습니까? [1.네 / 2.아니요]")
f2 = "1"

data1.logout(f0)
data2.show_books(f2)








