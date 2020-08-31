import math

sushi_type = input()
restaurant_name = input()
plates_count = int(input())
order = input()

price = 0
delivery = False
if sushi_type == 'sashimi':
    if restaurant_name == 'Sushi Zone':
        price = 4.99
    elif restaurant_name == 'Sushi Time':
        price = 5.49
    elif restaurant_name == 'Sushi Bar':
        price = 5.25
    elif restaurant_name == 'Asian Pub':
        price = 4.5

elif sushi_type == 'maki':
    if restaurant_name == 'Sushi Zone':
        price = 5.29
    elif restaurant_name == 'Sushi Time':
        price = 4.69
    elif restaurant_name == 'Sushi Bar':
        price = 5.55
    elif restaurant_name == 'Asian Pub':
        price = 4.8

elif sushi_type == 'uramaki':
    if restaurant_name == 'Sushi Zone':
        price = 5.99
    elif restaurant_name == 'Sushi Time':
        price = 4.49
    elif restaurant_name == 'Sushi Bar':
        price = 6.25
    elif restaurant_name == 'Asian Pub':
        price = 5.5

elif sushi_type == 'temaki':
    if restaurant_name == 'Sushi Zone':
        price = 4.29
    elif restaurant_name == 'Sushi Time':
        price = 5.19
    elif restaurant_name == 'Sushi Bar':
        price = 5.75
    elif restaurant_name == 'Asian Pub':
        price = 5.5

total_price = math.ceil(plates_count * price)
#if order == 'Y':
    #delivery = True
    #total_price *= 1.2


if restaurant_name == 'Sushi Zone' or restaurant_name == 'Sushi Time' or restaurant_name == 'Sushi Bar' or restaurant_name == 'Asian Pub':
    if order == 'Y':
        delivery = True
        total_price *= 1.2
    print(f'Total price: {total_price:.0f} lv.')

else:
    print(f'{restaurant_name} is invalid restaurant!')