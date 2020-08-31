num_count = int(input())

o_sum = 0
e_sum = 0

for ind in range(num_count ):
    cur_num = int(input())
    if ind % 2 != 0:
        o_sum += cur_num
    else:
        e_sum += cur_num
if o_sum == e_sum:
    print('Yes')
    print(f'Sum = {e_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(e_sum - o_sum)}')
