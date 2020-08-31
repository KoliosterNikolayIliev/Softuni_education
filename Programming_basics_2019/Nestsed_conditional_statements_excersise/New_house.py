flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0
discount = 0

if flower_type == 'Roses':
    price = 5
    if flower_count > 80:
        discount = 0.1
if flower_type == 'Dahlias':
    price = 3.8
    if flower_count > 90:
        discount = 0.15
if flower_type == 'Tulips':
    price = 2.8
    if flower_count > 80:
        discount = 0.15
if flower_type == 'Narcissus':
    price = 3
    if flower_count < 120:
        discount = -0.15
if flower_type == 'Gladiolus':
    price = 2.5
    if flower_count < 80:
        discount = -0.2

total_price = (price * flower_count) - (price*flower_count*discount)

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')
