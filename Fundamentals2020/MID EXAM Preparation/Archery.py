targets = [int(x) for x in input().split("|")]
points = 0
while True:
    command = input().split("@")
    cmd = command[0]

    if cmd == "Shoot Left":
        start = int(command[1])
        length = int(command[2])
        result = len(targets) - ((start + length) % len(targets))
        if 0 <= start < len(targets):
            targets[result] -= 5
            points += 5
        if targets[result]<5:
            points += targets[result]
            targets[result] = 0

    elif cmd == "Shoot Right":
        start = int(command[1])
        length = int(command[2])
        result = (start + length) % len(targets)
        if 0 <= start < len(targets):
            targets[result] -= 5
            points += 5

        if targets[result] < 5:
            points += targets[result]
            targets[result] = 0

    elif cmd == "Reverse":
        targets.reverse()
    elif cmd == "Game over":
        print(f"{' - '.join([str(x) for x in targets])}")
        print(f"Iskren finished the archery tournament with {points} points!")
        break
