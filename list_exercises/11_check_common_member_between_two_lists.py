first_list = input().strip("[]").split(", ")
first_list = list(map(int, first_list))
second_list = input().strip("[]").split(", ")
second_list = list(map(int, second_list))
common_element = 'None'
for element in first_list:
    if element in second_list:
        common_element = 'True'

print(common_element)
