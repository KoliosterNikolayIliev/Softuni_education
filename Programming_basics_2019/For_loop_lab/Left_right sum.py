num_count = int(input())

l_sum = 0
r_sum = 0

for ind in range(num_count * 2):
    cur_num = int(input())
    if ind < num_count:
        l_sum += cur_num
    else:
        r_sum += cur_num
if l_sum == r_sum:
    print(f'Yes, sum = {l_sum}')
else:
    print(f'No, diff = {abs(l_sum - r_sum)}')
