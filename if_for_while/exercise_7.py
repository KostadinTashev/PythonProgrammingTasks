number = int(input("Enter a number: "))
for i in range(0, number + 1, 1):
    for j in range(number - i, 0, -1):
        print(j, end=' ')
    print("")
