contacts = input().split(" ")
export = []
while True:
    export = []
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
        count = int(command[2])
        if start+count < len(contacts):
            for i in range(start, (start+count)):
                export.append(contacts[i])
            print(f"{' '.join([str(export[x]) for x in range(len(export))])}")
        else:
            for j in range(start, len(contacts)):
                export.append(contacts[j])
            print(f"{' '.join([str(export[x]) for x in range(len(export))])}")

    elif cmd == "Print":
        way = command[1]
        if way == "Normal":
            print(f"Contacts: {' '.join(contacts)}")
            break
        else:
            reversed_c = list(reversed(contacts))
            print(f"Contacts: {' '.join(reversed_c)}")
            break
