nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(f"Nested list: {nested_list}")
for element in nested_list:
    for number in element:
        if number == 55:
            print(f"The number {number} is in {element}")
        