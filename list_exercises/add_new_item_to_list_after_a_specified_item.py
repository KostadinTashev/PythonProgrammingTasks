list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
for element in list1:
    if type(element) == list:
        for item in element:
            if type(item) == list:
                for item1 in item:
                    if item1 == 6000:
                        item.append(7000)
print(list1)