from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casing = reversed([int(x) for x in input().split(', ')])
bomb_casing = deque(bomb_casing)
bomb_types = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
counter = 0
success = False
while bomb_effect and bomb_casing:
    bomb_part_one = bomb_effect[0]
    bomb_part_two = bomb_casing[0]
    sum_materials = bomb_part_one + bomb_part_two
    if sum_materials in bomb_types:
        bomb_pouch[bomb_types[sum_materials]] += 1
        bomb_effect.popleft()
        bomb_casing.popleft()
    else:
        bomb_casing[0] -= 5
    if bomb_pouch['Datura Bombs'] >= 3 and bomb_pouch['Cherry Bombs'] >= 3 and bomb_pouch['Smoke Decoy Bombs'] >= 3:
        success = True
        break

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effect])}')
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casing])}')
else:
    print("Bomb Casings: empty")

[print(f"{k}: {v}") for k, v in sorted(bomb_pouch.items())]
