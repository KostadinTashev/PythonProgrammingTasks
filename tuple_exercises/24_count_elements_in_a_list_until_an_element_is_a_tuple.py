list1 = [10, 20, 30, (10, 20), 40]
before_tuple = 0
for element in list1:
    
    if type(element) == tuple:
        break
    else:
        before_tuple += 1
print(before_tuple)
