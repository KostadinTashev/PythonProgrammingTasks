tuple1 = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuple1)
list1 = list(tuple1)
list1.remove('r')
tuple1 = tuple(list1)
print(tuple1)
