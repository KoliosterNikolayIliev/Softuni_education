e_eff1 = int(input())
e_eff2 = int(input())
e_eff3 = int(input())
people_count_per_e = int(input())

total_eff = e_eff1 + e_eff2 + e_eff3
time = 0

while people_count_per_e > 0:
    time += 1
    if time % 4 == 0:
        time += 1
    people_count_per_e -= total_eff

print(f"Time needed: {time}h.")
