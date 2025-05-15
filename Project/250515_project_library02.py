


# ----------------------------------클래스--------------------------------------
class LibrarySystem:
    
# login-------------------------------------------
    def __init__(self):
            self.users = {"1":"1"}  # 사용자 정보 저장용 딕셔너리
            self.logincheck = False
            self.books = [{"title":"원피스", "rented_by":"대여가능"},
                          {"title":"총균쇠", "rented_by": None},
                          {"title":"나루토", "rented_by": "대여가능"}]
            self.rent = []
            self.extend = True

    def login_first(self):
        self.username = input("반갑습니다! [1.회원가입/2.로그인] : ")
        if self.username == "1":
            return 1
        elif self.username == "2":
            return 2

    def signup(self):  # 회원가입 함수
        while True:
            username = input("아이디를 입력하세요: ")
            if username in self.users:
                print("❗ 이미 존재하는 아이디입니다.")
            elif len(username) <= 2:
                print("id는 세 글자 이상 입력해주세요.")
            else:
                self.name1 = username
                break
        while True:
            password = input("비밀번호를 입력하세요: ")
            if len(password) < 4:
                print("비밀번호는 네 자리 이상 입력해주세요.")
            else:
                self.password1 = password
                self.users = self.users|({self.name1:self.password1})
                print(f"🎉 {username}님, 회원가입이 완료되었습니다!")
                break

    def login(self):  # 로그인 함수
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        if username in self.users and self.users[username] == password:
            print(f"✅ {username}님, 로그인 성공!✅")
            self.logincheck = 1
        else:
            print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")

    def check(self): #로그인 성공여부 함수
        if self.logincheck == False:
            return False
        elif self.logincheck == True:
            return True
    
# num1-----------------------------------------------------
    def show_books(self):
        print("")
        for num,title_book in enumerate(self.books,1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
    
# num2-----------------------------------------------------
    def renting_book(self):
        if len(self.books) == 0:
            print("대여중인 책이 없습니다.")
        else:
            print("")
            list_borrow = []
            for find_key in self.books:
                if "rented_by" in find_key:
                    if find_key["rented_by"] == None:
                        list_borrow.append(find_key["title"])
            for i,v in enumerate(list_borrow,1):
                print(f"{i}. {v} / 대여중")


# num3-----------------------------------------------------
    def add_book(self):
        book_title = input("책 제목을 입력해주세요.[0.취소하기]: ")
        if book_title == "0":
            pass
        else:
            book_add = {"title":book_title, "rented_by":"대여가능"}
            self.books.append(book_add)
            print(f"'{book_title}' 도서가 등록되었습니다.")

# num4-----------------------------------------------------
    def delete_book(self):
        print("")
        for num,title_book in enumerate(self.books,1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
        while True:
            book_number = input("삭제할 책 번호를 입력해주세요.[0.취소하기]: ")
            if book_number.isdigit() == True:
                if 1 <= int(book_number) <= len(self.books)+1:
                    self.books.pop(int(book_number)-1)
                    print("도서가 삭제되었습니다.")
                    break
                elif int(book_number) == 0:
                    break
                else:
                    print("존재하지 않는 책 번호입니다.")
            elif book_number.isdigit() == False:
                print("존재하지 않는 책 번호입니다.")

# num5-----------------------------------------------------
    def rent_book(self):
        print("")
        for num,title_book in enumerate(self.books,1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
        while True:
            book_number = input("대여할 책 번호를 입력해주세요.[0.취소하기]: ")
            if book_number.isdigit() == True:
                if 1 <= int(book_number) <= len(self.books)+1:
                    if self.books[int(book_number)-1]["rented_by"] == None:
                        print("이미 대여중인 책입니다.")
                    else:
                        self.books[int(book_number)-1]["rented_by"] = None
                        self.rent.append(self.books[int(book_number)-1]["title"])
                        print("도서가 대여되었습니다.")
                        print(self.rent)
                        break
                elif int(book_number) == 0:
                    break
                else:
                    print("존재하지 않는 책 번호입니다.")
            elif book_number.isdigit() == False:
                print("존재하지 않는 책 번호입니다.")

# num6-----------------------------------------------------
    def return_book(self):
        print("\n당신의 대여중인 책 목록")
        for i,v in enumerate(self.rent,1):
            print(f"{i}. {v} / 대여중")
        while True:
            book_number = input("반납할 책 번호를 입력해주세요.[0.취소하기]: ")
            if book_number.isdigit() == True:
                if 1 <= int(book_number) <= len(self.books)+1:
                    for value in self.books:
                        for i,v in value.items():
                            if v == self.rent[int(book_number)-1]:
                                pass
                    self.rent.pop(int(book_number)-1)
                    print("도서가 반납되었습니다.")
                    print(self.rent)
                    break
                elif int(book_number) == 0:
                    break
                else:
                    print("존재하지 않는 책 번호입니다.")
            elif book_number.isdigit() == False:
                print("존재하지 않는 책 번호입니다.")
        # 구현중....
        
    
# num7-----------------------------------------------------
    def extend_book(self):
        if len(self.rent) == 0:
            print("\n대여중인 책이 없습니다")
        elif len(self.rent) >= 1:
            if self.extend == True:
                print("\n대여중인 책의 반납기간이 연장되었습니다.")
                self.extend = False
            else:
                print("\n연장 횟수를 초과했습니다.(1회만 가능)")

# num8-----------------------------------------------------
    def please_book(self):
        please1 = input("신청하고 싶은 책을 입력해주세요.[0.취소하기] : ")
        if please1 == 0:
            print("\n책 신청이 취소되었습니다.")
        else:
            print(f"\n{please1}의 신청이 완료되었습니다.")

# num9-----------------------------------------------------
    def rent_me(self):
        if len(self.rent) == 0:
            print("\n대여중인 책이 없습니다.")
        elif len(self.rent) >= 1:
            print("\n내가 대여중인 책")
            for i, v in enumerate(self.rent,1):
                print(f"{i}. {v} / 대여중")

# num10-----------------------------------------------------
    def search_books(self):
        search1 = input("검색할 키워드를 입력해주세요.[0.취소하기] : ")
        if search1 ==0:
            pass
        else:
            search_list = []
            key_list = []
            search1.lower()
            for value in self.books:
                key_list.append(value)           
            for book_find in key_list:
                if search1 in book_find:
                    search_list.append(book_find)
                else:
                    pass
            if len(search_list) > 0:
                print(f"검색된 책은 {search_list[0]}입니다.")
            else:
                print("검색된 책은 없습니다.") # 구현중

# num0-----------------------------------------------------
    def logout(self):
        confirm = input("로그아웃 하시겠습니까? [1.네 / 2.아니요]")

        if confirm == "1":
            print("로그아웃 되었습니다.")
            self.users.clear() # 현재 사용자 정보 초기화
            return True
        elif confirm == "0":
            print("로그아웃이 취소되었습니다.")
            return False
        else:
            print("잘못된 입력입니다. 0 또는 1을 입력해주세요.")
            return False

    

# 인스턴스-----------------------------------------------------

num1 = LibrarySystem()



    
# ----------------------------------시퀀스--------------------------------------

# 로그인 시퀀스
while True:
    login1 = num1.login_first()
    if  login1 == 1:
        num1.signup()
    elif login1 == 2:
        num1.login()
    
    if num1.check() == True:
        break

# 메뉴 시퀀스
while True:
    print("\n----- 도서 대여 시스템 테스트 -----")
    print("1. 도서 목록 보기")
    print("2. 대출 중인 도서 목록 보기")
    print("3. 책 추가하기")
    print("4. 책 삭제하기")
    print("5. 책 대여하기")
    print("6. 책 반납하기")
    print("7. 대여 연장하기")
    print("8. 원하는 도서 신청하기")
    print("9. 내 대출 목록 보기")
    print("10. 책 검색하기")
    print("0. 로그아웃 하고 종료")

    data1 = input("할일을 선택하세요 : ")

    if data1 == "1":
        num1.show_books()
    
    elif data1 == "2":
        num1.renting_book()

    elif data1 == "3":
        num1.add_book()   

    elif data1 == "4":
        num1.delete_book()

    elif data1 == "5":
        num1.rent_book()

    elif data1 == "6":
        num1.return_book() #아직..

    elif data1 == "7":
        num1.extend_book()

    elif data1 == "8":
        num1.please_book()

    elif data1 == "9":
        num1.rent_me()

    elif data1 == "10":
        num1.search_books() #아직..

    elif data1 == "0":
        logout1 = num1.logout()
        if logout1 == True:
            break
    else:
        print("올바른 숫자를 입력해주세요.")

print("")
print("안녕히 가세요~")






                  
            