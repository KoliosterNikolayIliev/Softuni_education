destination = input()
while destination != 'End':
    money_needed = float(input())
    savings = 0
    while savings < money_needed:
        current_sum = float(input())
        savings += current_sum
    print(f'Going to {destination}!')
    destination = input()
