adventure_days = int(input())
players_count = int(input())
groups_energy = float(input())
water_day_person = float(input())
food_day_person = float(input())

total_food = adventure_days * players_count * food_day_person
total_water = adventure_days * players_count * water_day_person
cur_food = 0

for day in range(1, adventure_days + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss
    if groups_energy <= 0:
        break

    if day % 3 == 0:
        groups_energy *= 1.1
        cur_food = total_food / players_count
        total_food -= cur_food

    if day % 2 == 0:
        groups_energy *= 1.05
        total_water *= 0.7

if groups_energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
