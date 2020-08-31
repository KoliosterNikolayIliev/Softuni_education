conditions = input().split('#')
water = int(input())

effort = []
fire = []

for i in range(0, len(conditions)):
    cell = str(conditions[i]).split(' = ')

    if str(cell[0]) == 'High' and 81 <= int(cell[1]) <= 125:
        if water >= int(cell[1]):
            water = water - int(cell[1])
            effort.append(0.25 * int(cell[1]))
            fire.append(int(cell[1]))

    if cell[0] == 'Medium' and 51 <= int(cell[1]) <= 80:
        if water >= int(cell[1]):
            water = water - int(cell[1])
            effort.append(0.25 * int(cell[1]))
            fire.append(int(cell[1]))

    if cell[0] == 'Low' and 1 <= int(cell[1]) <= 50:
        if water >= int(cell[1]):
            water = water - int(cell[1])
            effort.append(0.25 * int(cell[1]))
            fire.append(int(cell[1]))

total_effort = sum(effort)
total_fire = sum(fire)

print("Cells:")
for j in fire:
    print(f' - {j}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
