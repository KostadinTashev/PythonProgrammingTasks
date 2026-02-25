colors = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

print("Check if 'White' present in said tuple of tuples!")
print(any('White' in t for t in colors))
print("Check if 'Olive' present in said tuple of tuples!")
print(any('Olive' in t for t in colors)) 