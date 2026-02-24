my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list = [element for element in my_list if type(element) == int]
print(f"Original list: {my_list}")
print(f"Numbers only: {new_list}")
