rows = int(input('Enter the number of rows: '))

for i in range(1, rows):
    print('* ' * i)
print('* ' * rows)
for j in range(rows - 1, 0, -1):
    print('* ' * j)
