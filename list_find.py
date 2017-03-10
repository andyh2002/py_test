def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index


lst = [1, 2, 3, 4, 5]

print(list_find(lst, 6))




