cards = input().split(":")
new_cards = []
while True:
    command = input().split(" ")
    cmd = command[0]

    if cmd == "Add":
        name = command[1]
        if name in cards:
            new_cards.append(name)
        else:
            print("Card not found.")
    elif cmd == "Insert":
        name = command[1]
        index = int(command[2])
        if name in cards and index in range(len(cards)):
            new_cards.insert(index, name)
        else:
            print("Error!")
    elif cmd == "Remove":
        name = command[1]
        if name in new_cards:
            new_cards.remove(name)
        else:
            print("Card not found.")

    elif cmd == "Swap":
        name1 = command[1]
        name2 = command[2]
        a, b = new_cards.index(name1), new_cards.index(name2)
        new_cards[b], new_cards[a] = new_cards[a], new_cards[b]

    elif cmd == "Shuffle":
        new_cards.reverse()
    elif cmd == "Ready":
        break
print(" ".join(new_cards))
