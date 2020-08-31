movie_budget = float(input())
winguard_count = int(input())
wear_price = float(input())

decor_price = movie_budget * 0.1
wear_sum = wear_price * winguard_count
if winguard_count >= 150:
    wear_sum = wear_sum * 0.9
else:
    wear_sum == wear_sum

movie_price = decor_price + wear_sum

if winguard_count > 150:
    wear_sum = wear_sum * 0.9

money_left = movie_budget - movie_price

if money_left >= 0:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')

else:
    print('Not enough money!')
    print(f'Wingard needs {abs(money_left):.2f} leva more.')
