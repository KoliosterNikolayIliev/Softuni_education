import math

year = input()
p = int(input())
h = int(input())

total_days = 0
total_days += (48 - h) * 3 / 4
total_days += h

total_days += p * 2 / 3

if year == 'leap':
    total_days = total_days * 1.15

    print(math.floor(total_days))

elif year == 'normal':
    total_days = total_days
    print(math.floor(total_days))
