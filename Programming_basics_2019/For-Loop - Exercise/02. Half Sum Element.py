import sys

max_number = -sys.maxsize
sum_numbers = 0

numbers_count = int(input())

for i in range(numbers_count):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum_numbers += current_number

sum_numbers -= max_number
if sum_numbers == max_number:
    print('Yes')
    print(f'Sum = {sum_numbers}')
else:
    print('No')
    print(f'Diff = {abs(max_number - sum_numbers)}')
