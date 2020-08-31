chest = input().split("|")
command = input()
while command != "Yohoho!":

    command = command.split()
    if command[0] == 'Loot':
        items = command[1:]
        [chest.insert(0, x) for x in items if x not in chest]
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(chest):
            chest.append(chest.pop(index))
    elif command[0] == 'Steal':
        count = int(command[1])
        if count > len(chest):
            count = len(chest)
        stolen = chest[len(chest) - count:]
        chest = chest[:len(chest) - count]
        print(", ".join(stolen))
    command = input()

if len(chest) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = sum([len(x) for x in chest])/len(chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
