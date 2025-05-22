

class User:
    def borrowed_books(self):
        pass

class Library:
    def __init__(self,booklist):
        self.booklist = booklist
        self.mylist = []

    def books(self):
        print("보유중인 책 목록입니다.")
        for i,v in enumerate(self.booklist, 1):
            print(f"{i}. {v}")

    def borrow_book(self):
        for i,v in enumerate(self.booklist, 1):
            print(f"{i}. {v}")
        borrow1 = input("대여하실 책의 번호를 입력해주세요. : ")
        self.booklist = self.booklist.pop(int(borrow1)-1)

    def return_book(self):
        if len(self.mylist) == 0:
            print("대여중인 책이 없습니다.")
        else:
            for i,v in enumerate(self.mylist, 1):
                print(f"{i}. {v}")
            borrow2 = input("반납하실 책의 번호를 입력해주세요. : ")
            self.mylist.remove(int(borrow2)-1)
            self.booklist.append(v)

class Main:
    def __init__(self):
        self.user = User()
        self.library = Library(["파이썬", "알고리즘", "자료구조"])

    def main(self):
        print("반갑습니다. 중앙도서관입니다.")
        while True:
            print("\n중앙도서관 시스템")
            print("1. 보유 책 목록")
            print("2. 책 대여하기")
            print("3. 책 반납하기")
            print("4. 대여중인 책 목록")
            print("0. 시스템 종료")
            data1 = input("사용하실 기능을 번호로 입력해주세요. : ")

            if data1 == "1":
                self.library.books()
            elif data1 == "2":
                self.library.borrow_book()
            elif data1 == "3":
                self.library.return_book()
            elif data1 == "4":
                pass
            elif data1 == "0":
                print("안녕히 가세요!")
                break


user1 = Main()

user1.main()




