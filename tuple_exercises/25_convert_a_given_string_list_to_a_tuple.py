original_string = 'python 3.0'
print(f"Original string is: {original_string}")
tuple1 = tuple(x for x in original_string if x != ' ')
print(tuple1)
