a = [{"히":20,"age":30},{"기":20,"age":50}, {"부":20,"age":5}]


b = list(filter(lambda x : x["age"] >= 50, a))
print(b)