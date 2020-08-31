events = input().split('|')
initial_energy = 100
initial_coins = 100
energy = 0
completed = True

for event in events:
    item = event.split('-')

    item1 = item[0]
    number = int(item[1])
    if item1 == 'rest':
        if initial_energy < 100:
            energy = number
            initial_energy += energy
        else:
            energy = 0
        print(f'You gained {energy} energy.')
        print(f'Current energy: {initial_energy}.')
    elif item1 == 'order':
        if initial_energy - 30 >= 0:
            initial_coins += number
            initial_energy = initial_energy - 30
            print(f'You earned {number} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
    else:

        ingredient = item1
        cost = number
        if initial_coins - cost > 0:
            initial_coins -= cost
            print(f'You bought {ingredient}.')
        else:
            print(f'Closed! Cannot afford {ingredient}.')
            completed = False
            break

if completed:
    print('Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {initial_energy}')
