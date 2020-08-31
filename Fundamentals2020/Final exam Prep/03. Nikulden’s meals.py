guests = {}
unliked = 0
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("-")
    cmd = command[0]
    guest = command[1]
    meal = command[2]

    if cmd == "Like":
        if guest not in guests.keys():
            guests[guest] = []
            guests[guest].append(meal)
        else:
            if meal not in guests[guest]:
                guests[guest].append(meal)

    elif cmd == "Unlike":
        if guest in guests.keys():
            if meal in guests[guest]:
                guests[guest].remove(meal)
                unliked += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            print(f"{guest} is not at the party.")

guests = dict(sorted(guests.items(), key=lambda x: (-(len(x[1])), x[0])))
for k, v in guests.items():
    print(f"{k}: {', '.join(v)}")
print(f"Unliked meals: {unliked}")
