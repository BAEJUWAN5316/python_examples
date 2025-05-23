#영화 예매 시스템 만들기

class User:
    def __init__(self, user):
        self.user1 = user
        

class Theater:
    def __init__(self, all_seat):
        self.all_seat = all_seat
        self.reserved = []
        self.list = [1,2,3,4,5,6,7,8,9,10]

    def reserve_seat(self, user, seat_no):
        if seat_no in self.list:
            self.user = user
            self.seat_no = seat_no
            for value in self.list:
                if value == seat_no:
                    self.list.remove(seat_no)
                    self.reserved.append(seat_no)
            print(f"{self.user.user1}님, 좌석 {self.seat_no}번이 예약되었습니다.")
        else:
            print("해당 좌석이 이미 예매중이거나 올바른 좌석 선택이 아닙니다.")

    def show_reserved(self):
        sorted_list = sorted(self.reserved)
        print(f"현재 예약된 좌석:{sorted_list}")

    def show_available(self):
        print(f"남은 좌석 수: {len(self.list)}")


user1 = User("지민")
theater = Theater(10)

theater.reserve_seat(user1, 3)
theater.reserve_seat(user1, 5)

theater.show_reserved()
theater.show_available()





