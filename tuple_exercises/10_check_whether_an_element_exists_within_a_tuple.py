tuple1 = 2, 4, 5, 6, 2, 3, 4, 4, 7
searched_number = int(input("Enter a number: "))
if searched_number in tuple1:
    print(f'{searched_number} is in the tuple')
else:
    print(f'{searched_number} is not in the tuple')
