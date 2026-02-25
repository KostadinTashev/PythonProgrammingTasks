list1 = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
dict1 = {}
for key, value in list1:
    dict1.setdefault(key, []).append(value)
print(dict1)