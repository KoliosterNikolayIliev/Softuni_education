n = int(input())
tank = 255
waterfill = 0
for i in range(1, n+1):
    water_qty = int(input())
    tank_left = tank - water_qty
    while waterfill < tank:
        waterfill = waterfill + water_qty
        if waterfill > tank or i==n:
            break
    if i == n:
        print(waterfill)
    if water_qty > (tank_left-tank):
        print('Insufficient capacity!')