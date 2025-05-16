
# class fin:
#     def __init__(self):
#         self.b = [1, 2, 3]
        

#     def pri(self):
#         print(self.b)

#     def add(self):
#         self.g = 6
#         self.b.append(self.g)
#         print(self.b)

# go1 = fin()
# go2 = fin()

# while True:
#     da = input("입력해 : ")
#     if da == "1":
#         go1.add()

#     elif da== "2":
#         go1.pri()


a = [{"하나":1, "둘":2},{"셋":3, "넷":4}]
list1= []

# for value in a:
#     list1.append(str(value.values))
# print(list1)

for keys in a:
    list1.append(list(keys.keys()))

print(list1)