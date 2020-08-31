import math

biscuits_day_w = int(input())
workers_c = int(input())
comp_bis_30 = int(input())

total_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += math.floor(0.75 * workers_c * biscuits_day_w)
    else:
        total_biscuits += workers_c * biscuits_day_w

difference = total_biscuits - comp_bis_30
percentage = difference / comp_bis_30 * 100

print(f"You have produced {total_biscuits:.0f} biscuits for the past month.")

if total_biscuits >= comp_bis_30:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")
