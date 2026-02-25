tuple1 = (11, [22, 33], 44, 55)
print(f"Original tuple: {tuple1}")

for element in tuple1:
    if type(element) == list:
        for i in range(len(element)):
            if element[i] == 22:
                element[i] = 222

print(tuple1)