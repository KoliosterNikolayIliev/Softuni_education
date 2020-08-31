tenths = list(range(0, 1001, 10))
cost = 0
spirit = 0
quant = int(input())
days = int(input())

for day in range(1, days + 1):
    if day % 11 == 0:
        quant += 2
    if day % 2 == 0:
        cost += quant * 2.00
        spirit += 5
    if day % 3 == 0:
        cost += quant * 3.00
        cost += quant * 5.00
        spirit += 13
    if day % 5 == 0:
        cost += quant * 15.00
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day in tenths:
        spirit -= 20
        cost += (3.00 + 5.00 + 15.00)

        if day == days:
            spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")