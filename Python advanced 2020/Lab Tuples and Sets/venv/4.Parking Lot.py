n = int(input())

parking = set()
for _ in range(n):
    command = input().split(", ")
    direction = command[0]
    car = command[1]
    if direction == "IN":
        if car not in parking:
            parking.add(car)
    elif direction == "OUT":
        if car in parking:
            parking.remove(car)
if parking:
    [print(x) for x in parking]
else:
    print("Parking Lot is Empty")

# parking_lot = set()
#
# commands_count = int(input())
#
# for _ in range(commands_count):
#     (command, car) = input().split(', ')
#     if command == 'IN':
#         parking_lot.add(car)
#     else:
#         parking_lot.remove(car)
#
# if parking_lot:
#     [print(car) for car in parking_lot]
# else:
#     print('Parking Lot is Empty')