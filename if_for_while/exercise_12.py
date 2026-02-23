first_num = 0
second_num = 1
loop_times = 10
for i in range(loop_times):
    print(first_num, end=' ')
    result = first_num + second_num
    first_num = second_num
    second_num = result