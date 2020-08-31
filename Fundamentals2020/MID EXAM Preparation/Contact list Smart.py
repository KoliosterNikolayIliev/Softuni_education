contacts = input().split(" ")

while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Add":
        name = command[1]
        index = int(command[2])
        if 0 <= index <= len(contacts):
            if name in contacts:
                contacts.insert(index, name)
            else:
                contacts.append(name)

    elif cmd == "Remove":
        index = int(command[1])
        if 0 <= index <= len(contacts):
            del contacts[index]

    elif cmd == "Export":
        start = int(command[1])
        stop = int(command[2])
        if start + stop < len(contacts):
            print(f"{' '.join([contacts[x] for x in range(start, (start + stop))])}")
        else:
            print(f"{' '.join([contacts[x] for x in range(start, len(contacts))])}")
    elif cmd == "Print":
        way = command[1]
        if way == "Normal":
            print(f"Contacts: {' '.join(contacts)}")
            break
        else:
            reversed_c = list(reversed(contacts))
            print(f"Contacts: {' '.join(reversed_c)}")
            break
