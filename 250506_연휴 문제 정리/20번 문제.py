
#20 20번 문제

on1 = int(input("온도를 입력해주세요."))
on2 = input("섭씨, 화씨 중에 선택해주세요. [C=섭씨/F=화씨] : ")

if on2 == "C":
    print(f"{float(on1)}ºC는 {float(on1*9/5 +32):.1f}ºF입니다.")

elif on2 =="F":
    print(f"{float(on1)}ºF는 {float((on1-32)*5/9):.1f}ºC입니다.")