list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
new_list = []
for element in list_of_lists:
    for number in element:
        new_list.append(number)
print(f"Original list: {list_of_lists}")
print(f"Flattened list: {new_list}")
