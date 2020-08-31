num = input()
non_prime_sum = 0
prime_sum = 0

while num != 'stop':
    num = int(num)
    if num < 0:
        print('Number is negative.')
        num = input()
        continue

    not_prime = False

    for current_num in range(2, num):
        if num % current_num == 0:
            not_prime = True
            break

    if not_prime:
        non_prime_sum += num

    else:
        prime_sum += num

    num = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
