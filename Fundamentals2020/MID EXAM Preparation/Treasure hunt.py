chest = input().split("|")
command = input()
while command != "Yohoho!":

    command = command.split()
    if command[0] == 'Loot':
        del command[0]
        for item in command:
            if item not in chest:
                chest.insert(0, item)
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(chest):
            chest.append(chest.pop(index))
        else:
            continue

    elif command[0] == 'Steal':
        count = int(command[1])
        stolen = []
        if count <= len(chest):
            for i in range(count):
                stolen.append(chest.pop())
        else:
            for i in range(len(chest)):
                stolen.append(chest.pop())
        stolen.reverse()
        print(", ".join(stolen))
    command = input()
value_sum = 0
for item in chest:
    value_sum += len(item)

if len(chest) > 0:
    average_treasure_gain = value_sum / len(chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
