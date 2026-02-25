tuple1 = (1, 2, 3, 4)
print(f"Original tuple: {tuple1}")
squared_tuple = tuple(map(lambda x: x ** 2, tuple1))
print(f"Squared tuple: {squared_tuple}")
