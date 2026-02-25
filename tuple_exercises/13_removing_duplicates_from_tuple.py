my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f'Original tuple: {my_tuple}')
print(f'Tuple with unique elements: {tuple(set(my_tuple))}')