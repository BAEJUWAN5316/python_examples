

# 로그인 관련 리스트
user = {"abc":"123"}
current_user = []

# 책 관련 리스트
books = {"총균쇠":"대여 가능", "원피스":"대여중"}
rented_by = {}


# 로그인 시퀀스

print(f'''
반갑습니다!
도서관 프로그램입니다.
로그인 후 이용해주세요.
계정이 없다면 회원가입을 한 후 이용해주세요.
''')

first = input("계정이 있습니까? [1.있다/2.없다] : ")

if first == "2":
    data1 = input("아이디를 설정해주세요. : ")
    data2 = input("비밀번호를 넣어주세요. : ")
    user = user|{data1:data2}
if first == "1":
    None
else:
    print("숫자 1 또는 2를 입력해주세요.")

while True:
    print("로그인 해주세요.")
    login1 = input("아이디를 입력해주세요. : ")
    login2 = input("비밀번호를 입력해주세요. : ")
    if  login1 in list(user.keys()):
        if user[login1] == login2:
            print("로그인이 완료되었습니다.")
            current_user.append(login1)
            break
        else:
            print("비밀번호가 일치하지 않습니다.")

    else:
        print("아이디가 일치하지 않습니다.")


#메뉴 호출

while True:
    print(f'''
[도서관 시스템 메뉴]
1. 도서 목록 보기
2. 대출 중인 도서 목록 보기
3. 책 추가하기
4. 책 삭제하기
5. 책 대여하기
6. 책 반납하기
7. 대여 연장하기
8. 원하는 도서 신청하기
9. 내 대출 목록 보기
10. 책 검색하기
0. 로그아웃 또는 종료  
''')
    
    select1 = input("사용하실 메뉴 번호를 입력해주세요. : ")

    if select1 == "1": #1번 선택시
        for num, book_name in enumerate(books):
            print(f"{num+1}. {book_name} / {books[book_name]}")

    elif select1 == "2":
        if len(rented_by) > 0:
            print("대출 중인 도서 목록")
            for num2, rent_name in enumerate(rented_by):
                print(f"{num2+1}. {rent_name}")
        elif len(rented_by) == 0:
            print("대여 중인 책이 없습니다.")
        


    elif select1 == "3":
        book_add = input("추가할 책의 이름을 입력하세요. : ")
        book_add = dict({book_add:"대여 가능"})
        books = books|book_add

    elif select1 == "4":
        book_del = input("삭제할 책의 이름을 입력하세요. : ")
        if book_del in books:
            books.pop(book_del)
        else:
            print("입력한 책은 존재하지 않습니다.")

    elif select1 == "5":
        for num, book_name in enumerate(books):
            print(f"{num+1}. {book_name} / {books[book_name]}")
        book_check = input("대여 할 책 이름을 입력하세요.")
        if book_check in books:
            if books[book_check] == "대여중":
                print("해당 책은 이미 대여중입니다.")
            elif books[book_check] == "대여 가능":
                print("해당 책을 대여했습니다.")
                books[book_check] = "대여중"
                book_check={book_check:login1}
                rented_by = rented_by|book_check
        else:
            print("입력한 책은 존재하지 않습니다.")

    elif select1 == "6":
        for num, book_name in enumerate(rented_by):
            print(f"{num+1}. {book_name}")
        return_book = input("반납할 책을 입력하세요. : ")
        if return_book in rented_by:
            books[return_book] = "대여 가능"
            rented_by.pop(return_book)
            print("해당 책을 반납했습니다.")
        else:
            print("입력한 책은 존재하지 않습니다.")

    elif select1 == "7":
        for num, book_name in enumerate(rented_by):
            print(f"{num+1}. {book_name}")
        if len(rented_by) > 0:
            return_book = input("대여 연장할 책을 입력하세요. : ")
            if return_book in rented_by:
                print("연장이 완료되었습니다.")
            else:
                print("입력한 책은 존재하지 않습니다.")
        elif len(rented_by) == 0:
            print("대여중인 책이 없습니다.")

    elif select1 == "8":
        book_want = input("추가를 원하는 책을 입력해주세요. : ")
        print(f"{book_want}을(를) 추가 할 수 있도록 최선을 다하겠습니다.")

    elif select1 == "9":
        print("현재 대여중인 책")
        for num, book_name in enumerate(rented_by):
            print(f"{num+1}. {book_name}")

    elif select1 == "10":
        books_copy = books.copy()
        for books_lower in books_copy:
            books_copy[books_lower].lower()

        search_books = input("검색 할 책 키워드를 입력해주세요. :")
        search_list = []
        search_list_not = []
        search_books.lower()
        book_search = books_copy.keys()
        book_search = list(book_search)
        for book_find in book_search:
            if search_books in book_find:
                search_list.append(book_find)
            else:
                search_list_not.append(book_find)
            
        if len(search_list) > 0:
            print(f"검색된 책은 {search_list[0]}입니다.")
        elif len(search_list_not) > 0 and len(search_list) <= 0:
            print("검색된 책은 없습니다.")
                
    elif select1 == "0":
        current_user.remove(login1)
        break
    
    else:
        print("올바른 번호를 입력해주세요.")

print("도서관 프로그램을 종료합니다.")
print("안녕히 가세요.")