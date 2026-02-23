first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
dividers = 0
for num in range(first_num, second_num + 1, 1):
    for divider in range(1, num + 1, +1):
        if num % divider == 0:
            dividers += 1
    if dividers == 2:
        print(num)
    dividers = 0
