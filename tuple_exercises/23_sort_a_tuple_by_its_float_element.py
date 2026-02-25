list1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list1.sort(key=lambda x: x[1], reverse=True)
print(list1)
