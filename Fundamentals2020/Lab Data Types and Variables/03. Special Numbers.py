n = int(input())

for i in range(1, n + 1):
    digit_sum = 0
    for digit in str(i):
        digit_sum += int(digit)
    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f'{i} -> {is_special}')
