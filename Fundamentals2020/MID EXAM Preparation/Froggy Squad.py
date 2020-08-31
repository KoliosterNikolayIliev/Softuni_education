frog_list = input().split(" ")

while True:
    order = input().split(" ")
    command = order[0]
    if command == "Join":
        name = order[1]
        frog_list.append(name)

    elif command == "Jump":
        name = order[1]
        index = int(order[2])
        if index in range(len(frog_list)):
            frog_list.insert(index, name)

    elif command == "Dive":
        index = int(order[1])
        if index in range(len(frog_list)):
            frog_list.pop(index)

    elif command == "First":
        count = int(order[1])
        if count <= len(frog_list):
            print(' '.join(frog_list[0:count]))
        else:
            print(' '.join(frog_list))

    elif command == "Last":
        count = int(order[1])
        if count <= len(frog_list):
            print(' '.join(frog_list[-count:]))
        else:
            print(' '.join(frog_list))

    elif command == "Print":
        if order[1] == "Normal":
            print(f"Frogs: {' '.join(frog_list)}")
            break
        elif order[1] == "Reversed":
            reversedList = reversed(frog_list)
            print(f"Frogs: {' '.join(reversedList)}")
            break
