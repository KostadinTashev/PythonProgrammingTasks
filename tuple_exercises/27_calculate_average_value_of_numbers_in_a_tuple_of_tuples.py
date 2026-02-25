tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(f"Original tuple is: {tuple1}")
list1 = []
for element in tuple1:
    average = sum(element) / len(element)
    list1.append(average)
print(f"Average is: {list1}")