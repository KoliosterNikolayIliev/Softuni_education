budget = float(input())
season = input()

price = 0
place=''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        price = 0.3 * budget
    elif season == 'winter':
        place = 'Hotel'
        price = 0.7 * budget
    print(f'Somewhere in {destination}')
    print(f'{place} - {price:.2f}')

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        price = 0.4 * budget
    elif season == 'winter':
        place = 'Hotel'
        price = 0.8 * budget
    print(f'Somewhere in {destination}')
    print(f'{place} - {price:.2f}')

elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        place = 'Hotel'
        price = 0.9 * budget
    elif season == 'winter':
        place = 'Hotel'
        price = 0.9 * budget
    print(f'Somewhere in {destination}')
    print(f'{place} - {price:.2f}')