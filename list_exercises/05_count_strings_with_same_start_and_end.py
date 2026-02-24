list_of_strings = ['abc', 'xyz', 'aba', '1221']
counter = 0
for string in list_of_strings:
    if len(string) > 1 and string[0] == string[-1]:
        counter += 1

print(counter)
