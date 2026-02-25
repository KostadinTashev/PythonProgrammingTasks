list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(list1)

list1 = [t for t in list1 if not (isinstance(t, tuple) and len(t) == 0)]

print(list1)
