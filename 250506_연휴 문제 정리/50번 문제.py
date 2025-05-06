
#50 50번 문제

ip1,ip2,ip3,ip4 = input("IP주소를 입력해주세요. : ").split(".")

ip1 = int(ip1)
ip2 = int(ip2)
ip3 = int(ip3)
ip4 = int(ip4)

if 0 <= ip1 <= 255:
    ip1 = "O"
else:
    ip1 = "X"

if 0 <= ip2 <= 255:
    ip2 = "O"
else:
    ip2 = "X"

if 0 <= ip3 <= 255:
    ip3 = "O"
else:
    ip3 = "X"

if 0 <= ip4 <= 255:
    ip4 = "O"
else:
    ip4 = "X"

if ip1 == "O" and ip2 == "O" and ip3 == "O" and ip4 == "O":
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")


data1 = input("ip를 쓰세요 : ").split(".")

data1[0] = int(data1[0])
data1[1] = int(data1[1])
data1[2] = int(data1[2])
data1[3] = int(data1[3])


if 0 <= data1[0] <= 255:
    data1[0] = "O"
else:
    data1[0] = "X"

if 0 <= data1[1] <= 255:
    data1[1] = "O"
else:
    data1[1] = "X"

if 0 <= data1[2] <= 255:
    data1[2] = "O"
else:
    data1[2] = "X"

if 0 <= data1[3] <= 255:
    data1[3] = "O"
else:
    data1[3] = "X"

if len(data1) != 4:
    print("유효하지 않은 IP 주소입니다.")

elif data1[0] == "O" and data1[1] == "O" and data1[2] == "O" and data1[3] == "O":
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")