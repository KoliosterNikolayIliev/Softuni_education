roads = {}

while True:
    command = input()
    if command == "END":
        break

    command = command.split("->")
    cmd = command[0]
    if cmd == "Add":
        road = command[1]
        racer = command[2]
        if road not in roads.keys():
            roads[road] = []
        roads[road].append(racer)

    elif cmd == "Move":
        currentRoad = command[1]
        racer = command[2]
        nextRoad = command[3]
        if currentRoad in roads.keys() and nextRoad in roads.keys():
            if racer in roads[currentRoad]:
                roads[currentRoad].remove(racer)
                roads[nextRoad].append(racer)
    elif cmd == "Close":
        road = command[1]
        if road in roads.keys():
            del roads[road]
roads = dict(sorted(roads.items(), key=lambda x: (-len(x[1]), x[0])))
print("Practice sessions:")
for k, v in roads.items():
    print(k)
    print("++"+'\n++'.join(map(str, v)))
