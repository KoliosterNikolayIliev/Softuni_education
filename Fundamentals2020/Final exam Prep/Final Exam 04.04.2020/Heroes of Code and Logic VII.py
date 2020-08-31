n = int(input())

heroes = {}

for _ in range(n):
    hero_data = input().split(" ")
    name = hero_data[0]
    hp = int(hero_data[1])
    mp = int(hero_data[2])
    heroes[name] = [hp, mp]

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    cmd = command[0]
    if cmd == "CastSpell":
        name = command[1]
        mp_needed = int(command[2])
        spell = command[3]
        if heroes[name][1] >= mp_needed:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif cmd == "TakeDamage":
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[name][0] -= damage
        if heroes[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
    elif cmd == "Recharge":
        name = command[1]
        amount = int(command[2])
        current = heroes[name][1]
        maxamount = 200
        heroes[name][1] += amount
        if heroes[name][1] > maxamount:
            amount = maxamount - current
            heroes[name][1] = amount + current
        print(f"{name} recharged for {amount} MP!")

    elif cmd == "Heal":
        name = command[1]
        amount = int(command[2])
        current = heroes[name][0]
        maxamount = 100
        heroes[name][0] += amount
        if heroes[name][0] > maxamount:
            amount = maxamount - current
            heroes[name][0] = amount + current
        print(f"{name} healed for {amount} HP!")

heroes = dict(sorted(heroes.items(), key=lambda x: (-(x[1][0]), x[0])))
for k, v in heroes.items():
    print(k)
    print(f"  HP: {v[0]}")
    print(f"  MP: {v[1]}")
