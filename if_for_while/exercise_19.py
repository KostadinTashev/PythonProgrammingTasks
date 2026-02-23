for number in range(1, 11):
    print(f"multiplication table of: {number}")
    for multiplication_number in range(1, 11):
        print(f"{number * multiplication_number}", end=" ")
    print()
