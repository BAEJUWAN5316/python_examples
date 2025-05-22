
import json

with open("users.json", "r", encoding="utf-8") as f:
    dict1 = json.load(f)


class Jsontest:
    def register_user(self):
        print("\n회원 등록 시스템입니다.")
        select1 = input("이름을 입력하세요. : ")
        self.select1 = select1
        print(f"{self.select1}님 반갑습니다. 회원등록이 완료되었습니다.")
        self.dict_up = {select1:0}
        dict1.update(self.dict_up)

    def add_point(self):
        print(f"포인트 적립 시스템입니다.")
        select2_n = input("적립시킬 회원의 이름을 작성해주세요. : ")
        select2 = input("적립할 포인트를 작성해주세요. : ")
        dict1[select2_n] = dict1[select2_n] + int(select2)
        # dict1.update(self.dict_up)

    def see_point(self):
        print("회원 포인트 보기 시스템입니다.")
        print(dict1)

    def main(self):
        print("반갑습니다!")
        while True:
            print("1. 회원 등록")
            print("2. 포인트 적립")
            print("3. 회원 포인트 보기")
            print("4. 종료")
            data1 = input("사용할 기능을 선택해주세요. : ")

            if data1 == "1":
                self.register_user()
            elif data1 == "2":
                self.add_point()
            elif data1 == "3":
                self.see_point()
            elif data1 == "4":
                print("안녕히가세요!")
                break
            with open("users.json","w",encoding="utf-8") as f:
                json.dump(dict1,f,ensure_ascii=False)


user1 = Jsontest()

user1.main()






