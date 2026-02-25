list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(list1)):
    list2 = list(list1[i])
    list2[-1] = 100
    list1[i] = tuple(list2)
print(list1)

