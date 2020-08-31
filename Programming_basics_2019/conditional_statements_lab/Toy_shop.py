exc_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_count = puzzle_count + dolls_count + bears_count + minion_count + truck_count

sum_puzzle = puzzle_count * 2.6
sum_dolls = dolls_count * 3.0
sum_bears = bears_count * 4.10
sum_minion = minion_count * 8.20
sum_truck = truck_count * 2.0

total_sum = sum_bears + sum_puzzle + sum_dolls + sum_minion + sum_truck

if total_count >= 50:
    total_sum = total_sum * 0.75
    total_sum = total_sum * 0.9
elif total_count < 50:
    total_sum = total_sum
    total_sum = total_sum * 0.9

money_left = total_sum - exc_price

if money_left >= 0:
    print('Yes! ' + f'{total_sum - exc_price:.2f}' + ' lv left.')
else:
    print('Not enough money! ' + f'{abs(money_left):.2f} ' + 'lv needed.')
