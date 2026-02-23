nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
final_list = []
for num in nested_list:
    if type(num) == int:
        final_list.append(num)
    if type(num) == list:
        final_list.extend(num)
print(final_list)
