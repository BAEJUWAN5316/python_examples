
# 도구 모아 섬 탈출하기!

#class

class Island:
    # 입벤토리
    def __init__(self):
        self.item1 = []

    # 메인
    def main(self):
        main1 = input("어디를 조사해보시겠습니까? [1.해변/2.동굴/3.숲/4.가방확인]")
        if main1 == "1":
            return "1"
        elif main1 =="2":
            return "2"
        elif main1 =="3":
            return "3"
        elif main1 =="4":
            return "4"
        
    # 해변
    def beach(self):
        print("\n당신은 해변에 도착했습니다. 무엇을 하시겠습니까? ")
        self.beach1 = input("무엇을 하시겠습니까? [1.바다 조사/2.해변 조사/3.돌아가기] : ")
        if self.beach1 == "1":
            for values in self.item1:
                if "도끼" in values:
                    print("\n바다는 파도를 철썩이며 빛나고 있습니다.")
                else:
                    return "1"
            return "1"
        elif self.beach1 == "2":
            for values in self.item1:
                if "큰 천" in values:
                    print("\n해변가는 평화롭습니다.")
                else:
                    return "2"
            return "2"
        elif self.beach1 == "3":
            return "3"
    
    def beach_s1(self):
        print("\n바다에 들어가 샅샅이 주변을 훑었습니다.")
        self.beachs1 = input("반짝이는 물건이 보입니다. 살펴보시겠습니까? [1.예/2.아니오] : ")
        if self.beachs1 == "1":
            print("\n반짝이는 물건은 [도끼]였습니다. 도끼를 가방에 넣었습니다.")
            self.item1.append("도끼")
            return "end"
        elif self.beachs1 == "2":
            print("\n다시 해변으로 돌아왔습니다.")
            return "keep"
        
    def beach_s2(self):
        print("\n해변을 걸어가며 주변을 둘러보고 있습니다.")
        self.beachs2 = input("무언가 움직이는 물체가 있습니다. 살펴보시겠습니까? [1.예/2.아니오] : ")
        if self.beachs2 == "1":
            print("\n움직이는 물체는 [천]입니다. 큰 천을 가방에 넣었습니다.")
            self.item1.append("큰 천")
            return "end"
        elif self.beachs2 == "2":
            print("\n다시 해변으로 돌아왔습니다.")
            return "keep"








island = Island()


# 구동

while True:

    #main
    sel1 = island.main()

    if sel1 == "1":
        while True:
            sel1_1 = island.beach()
            if sel1_1 == "1":
                sel1_2 = island.beach_s1()
                if sel1_2 == "end":
                    break
                elif sel1_2 == "keep":
                    pass
            elif sel1_1 == "2":
                sel1_3 = island.beach_s2()
                if sel1_3 == "end":
                    break
                elif sel1_3 == "keep":
                    pass





