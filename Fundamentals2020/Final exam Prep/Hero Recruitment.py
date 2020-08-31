heroes = {}
herforsort = {}
while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "End":
        break
    hero = command[1]

    if cmd == "Enroll":
        if hero not in heroes.keys():
            heroes[hero] = []
        else:
            print(f"{hero} is already enrolled.")
    elif cmd == "Learn":
        spell = command[2]
        if hero in heroes.keys():
            if spell not in heroes[hero]:
                heroes[hero].append(spell)
            else:
                print(f"{hero} has already learnt {spell}.")
        else:
            print(f"{hero} doesn't exist.")

    elif cmd == "Unlearn":
        spell = command[2]
        if hero in heroes.keys():
            if spell in heroes[hero]:
                heroes[hero].remove(spell)
            else:
                print(f"{hero} doesn't know {spell}.")
        else:
            print(f"{hero} doesn't exist.")

for k in heroes.keys():
    herforsort[k] = int(len(heroes[k]))
sorted_heroes = dict(sorted(herforsort.items(), key=lambda x: (-x[1], x[0])))
print("Heroes:")
for key in sorted_heroes.keys():
    print(f"== {key}: {', '.join(heroes[key])}")
