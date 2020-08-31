initial_list = input().split("!")

while True:
    command = input().split(" ")
    cmd = command[0]

    if cmd == "Urgent":
        item = command[1]
        if item not in initial_list:
            initial_list.insert(0, item)

    elif cmd == "Unnecessary":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)

    elif cmd == "Correct":
        oldItem = command[1]
        newItem = command[2]
        if oldItem in initial_list:
            initial_list[initial_list.index(oldItem)] = newItem

    elif cmd == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    elif cmd == "Go":
        break

print(', '.join(initial_list))
