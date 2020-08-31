budget = int(input())
season = input()
fishermen = int(input())

price = 0
discount = 0
if season == 'Spring':
    price = 3000
elif season == 'Summer':
    price = 4200
elif season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fishermen <= 6:
    discount = 0.1
elif 7 <= fishermen <= 11:
    discount = 0.15
elif fishermen >= 12:
    discount = 0.25

total_price = price - (price * discount)

if (fishermen % 2) == 0 and season != 'Autumn':
    discount2 = 0.05
    total_price = total_price - (total_price * discount2)

if budget >= total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')
