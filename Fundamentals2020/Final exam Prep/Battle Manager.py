people = {}

while True:
    command = input()
    if command == "Results":
        break
    command = command.split(":")
    cmd = command[0]

    if cmd == "Add":
        personName = command[1]
        health = int(command[2])
        energy = int(command[3])
        if personName not in people.keys():
            people[personName] = [health, energy]
        else:
            people[personName][0] += health
            # people[personName][1] += energy
    elif cmd == "Attack":
        attacker = command[1]
        defender = command[2]
        damage = int(command[3])
        if attacker in people.keys() and defender in people.keys():
            people[defender][0] -= damage
            people[attacker][1] -= 1
            if people[defender][0] <= 0:
                del people[defender]
                print(f"{defender} was disqualified!")
            if people[attacker][1] <= 0:
                del people[attacker]
                print(f"{attacker} was disqualified!")

    elif cmd == "Delete":
        username = command[1]
        if username == "All":
            people.clear()
        else:
            if username in people.keys():
                del people[username]

count = len(people)
people = dict(sorted(people.items(), key=lambda x: (-(x[1][0]), x[0])))
print(f"People count: {count}")
for k, v in people.items():
    print(f"{k} - {v[0]} - {v[1]}")
