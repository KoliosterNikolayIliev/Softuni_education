fire_cells = input().split("#")
water = int(input())
cells = []
effort = 0
for n in range(len(fire_cells)):
    fire_cell = fire_cells[n].split(" = ")
    fire_type = fire_cell[0]
    value = int(fire_cell[1])
    if water == 0:
        break
    if fire_type == "High":
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                effort += value * 0.25
                cells.append(value)

    elif fire_type == "Medium":
        if 51 <= value <= 80:
            if water >= value:
                water -= value
                effort += value * 0.25
                cells.append(value)

    elif fire_type == "Low":
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                effort += value * 0.25
                cells.append(value)

print("Cells:")
for i in range(len(cells)):
    print(f" - {cells[i]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells)}")
