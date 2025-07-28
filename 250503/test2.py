def common_elements(list1, list2):
    list_all = []
    list1 = set(list1)
    list2 = set(list2)
    for a in list(list1):
        for b in list(list2):
            if a == b:
                list_all.append(a)
    return (list_all)

print(common_elements([1,2,3,3], [3,3,5,6,7,8]))