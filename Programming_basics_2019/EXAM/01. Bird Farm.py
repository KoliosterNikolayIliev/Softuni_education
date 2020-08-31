import math

egg_price = int(input())
chicken_count_first_month = int(input())
chicken_count_second_month = int(input())
chicken_count_third_month = int(input())

first_month_eggs = chicken_count_first_month * 20
second_month_eggs = 20 * (chicken_count_first_month + chicken_count_second_month)
third_month_eggs = 20 * (chicken_count_first_month + chicken_count_second_month + chicken_count_third_month)
total_eggs_count = first_month_eggs + second_month_eggs + third_month_eggs
Profit = total_eggs_count * 0.96 * egg_price / 100

print(f'Profit: {math.floor(Profit)} Lv.')
