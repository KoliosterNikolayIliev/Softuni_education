paintings = input().split(" ")

while True:
    command = input().split(" ")
    cmd = command[0]

    if cmd == "Change":
        paintingNumber = command[1]
        changedNumber = command[2]
        if paintingNumber in paintings:
            paintings[paintings.index(paintingNumber)] = changedNumber

            # paintings = [x.replace(paintingNumber, changedNumber) for x in paintings]


    elif cmd == "Hide":
        paintingNumber = command[1]
        if paintingNumber in paintings:
            paintings.remove(paintingNumber)
    elif cmd == "Switch":
        paintingNumber = command[1]
        paintingNumber2 = command[2]
        if paintingNumber in paintings and paintingNumber2 in paintings:
            a, b = paintings.index(paintingNumber), paintings.index(paintingNumber2)
            paintings[b], paintings[a] = paintings[a], paintings[b]

    elif cmd == "Insert":
        place = int(command[1])
        paintingNumber = command[2]
        if place in range(len(paintings)):
            paintings.insert(place + 1, paintingNumber)
    elif cmd == "Reverse":
        paintings.reverse()
    elif cmd == "END":
        break
print(" ".join([str(x) for x in paintings]))
