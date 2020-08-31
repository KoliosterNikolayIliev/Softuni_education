qty = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

cost = 0
christmas_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        qty += 2
    if day % 2 == 0:
        cost += ornament_set * qty
        christmas_spirit += 5
    if day % 3 == 0:
        cost += (tree_garlands + tree_skirt) * qty
        christmas_spirit += 13
    if day % 5 == 0:
        cost += tree_lights * qty
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        cost += tree_lights + tree_skirt + tree_garlands
        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")
