


'''
a = {"강사라다":1}
b= a.keys()
b = list(b)

if b.index("강사"):
    print(b)
'''

a = {"강사라다":1, "안사라다":2}
b = a.keys()
b = list(b)
lista = []

for ha in b:
    if "강사" in ha:
        lista.append(ha)

if len(ha) >= 1:
    print(lista[0])

else:
    print("없음")
