list_of_tuples1 = [(1, 2), (2, 3), (3, 4)]
list_of_lists1 = [list(t) for t in list_of_tuples1]
print("Converted list of lists:")
print(list_of_lists1)