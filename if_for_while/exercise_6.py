number = int(input('Enter a number: '))
digits = 0
while number != 0:
    number //= 10
    digits += 1
print(f"Total digits of number are: {digits}")

