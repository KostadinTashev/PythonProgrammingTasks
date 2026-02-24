my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
my_list = [x for (i, x) in enumerate(my_list) if i not in (0, 4, 5)]
print(my_list)
