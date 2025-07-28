


def common_elements(list1, list2):
    list_all = []
    for a in list1:
        for b in list2:
            if a == b:
                list_all.append(a)
    list_all = set(list_all)
    return list(list_all)

print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
print(common_elements(['python', 'django', 'orm'], ['orm', 'python']))
print(common_elements([1, 2, 3], [4, 5, 6]) )