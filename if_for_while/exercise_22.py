first_num = int(input())
second_num = int(input())
first_num_list = []
second_num_list = []
for digit in str(first_num):
    first_num_list.append(int(digit))
for digit in str(abs(second_num)):
    second_num_list.append(int(digit))
print(f"Largest digit in {first_num}: {max(first_num_list)}")
print(f"Smallest digit in {first_num}: {min(first_num_list)}")

print(f"Largest digit in {second_num}: {max(second_num_list)}")
print(f"Smallest digit in {second_num}: {min(second_num_list)}")
