users = {}
sideMembers = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    for i in command:
        if i == "|":
            command = command.split(" | ")
            forceSide = command[0]
            forceUser = command[1]
            if forceUser not in users:
                users[forceUser] = forceSide
            if forceSide not in sideMembers:
                sideMembers[forceSide] = 0
            break
        elif i == "-":
            command = command.split(" -> ")
            forceUser = command[0]
            forceSide = command[1]
            users[forceUser] = forceSide
            print(f"{forceUser} joins the {forceSide} side!")
            break
for i in users.values():
    sideMembers[i] += 1

sorted_sideMembers = dict(sorted(sideMembers.items(), key=lambda x: (-x[1], x[0])))
for (k, v) in sorted_sideMembers.items():
    if v > 0:
        print(f"Side: {k}, Members: {v}")
        for (key, value) in sorted(users.items()):
            if value == k:
                print(f"! {key}")
