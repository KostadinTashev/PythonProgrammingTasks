number = int(input("Enter a number:"))
terms = int(input("Enter number of terms:"))
numbers = []
for num in range(1, terms + 1):
    current_number = str(number) * num
    numbers.append(int(current_number))
print(sum(numbers))
