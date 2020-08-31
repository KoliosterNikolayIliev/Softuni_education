gifts = input().split(" ")

while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "OutOfStock":
        gift = command[1]
        if gift in gifts:
            for i in range(len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = "None"
    elif cmd == "Required":
        gift = command[1]
        index = int(command[2])
        if index in range(len(gifts)):
            gifts[index] = gift
    elif cmd == "JustInCase":
        gift = command[1]
        gifts.pop()
        gifts.append(gift)
    elif cmd == "No":
        break
print(f"{' '.join([gifts[x] for x in range(len(gifts)) if gifts[x] != 'None'])}")
