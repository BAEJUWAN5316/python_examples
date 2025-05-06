
#33 33번 문제

bool1 = input("불리언 값을 입력해주세요_1 : ")
bool2 = input("불리언 값을 입력해주세요_2 : ")

if bool1 == "True":
    bool1 = True
elif bool1 == "False":
    bool1 = False

if bool2 == "True":
    bool2 = True
elif bool2 == "False":
    bool2 = False

and1 = bool1 and bool2
or1 = bool1 or bool2
not1 = not bool1
not2 = not bool2

print(f"{bool1} AND {bool2} = {and1}")
print(f"{bool1} OR {bool2} = {or1}")
print(f"NOT {bool1} = {not1}")
print(f"NOT {bool2} = {not2}")