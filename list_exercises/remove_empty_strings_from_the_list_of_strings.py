list1 = ['Mike', "", 'Emma', 'Kelly', '', 'Brad']
for element in list1:
    if len(element) == 0:
        list1.remove(element)
print(list1)
