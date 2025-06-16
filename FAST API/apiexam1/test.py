a = {1:{"하":20, "나":30}, 2:{"사":50, "나":70}}

b = list(a.values())
c = False

for value in b:
    if value["나"] == 75:
        c = True

print(c)


# print(b)