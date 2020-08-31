needed_exp = float(input())
count_of_battles = int(input())

gained_exp = 0
counter = 0
for i in range(1, count_of_battles+1):
    exp = float(input())
    if i % 3 == 0:
        exp = exp * 1.15
    if i % 5 == 0:
        exp = exp * 0.9
    gained_exp += exp
    counter += 1
    if gained_exp >= needed_exp:
        print(f"Player successfully collected his needed experience for {counter} battles.")
        break
if gained_exp < needed_exp:
    print(f"Player was not able to collect the needed experience, {(needed_exp - gained_exp):.2f} more needed.")
