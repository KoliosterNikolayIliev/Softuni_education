tank_capacity = 255
n = int(input())

tank_fill = 0
for i in range(n):
    add_water = int(input())
    if tank_fill + add_water > tank_capacity:
        print('Insufficient capacity!')
    else:
        tank_fill += add_water
print(tank_fill)
