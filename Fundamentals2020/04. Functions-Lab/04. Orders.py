def order(p, q):
    total = 0
    if p == 'coffee':
        total = coffee_price * q
    elif p == 'water':
        total = water_price * q
    elif p == 'coke':
        total = coke_price * q
    elif p == 'snacks':
        total = snacks_price * q
    return total


product = input()
qty = int(input())

coffee_price = 1.5
water_price = 1.0
coke_price = 1.4
snacks_price = 2.0

print(f'{order(product, qty):.2f}')
