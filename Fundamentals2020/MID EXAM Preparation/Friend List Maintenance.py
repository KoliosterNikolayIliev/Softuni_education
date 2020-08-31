friends_list = input().split(", ")

while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Blacklist":
        name = command[1]
        if command[1] in friends_list:
            friends_list[friends_list.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif cmd == "Error":
        index = int(command[1])
        if friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
            print(f"{friends_list[index]} was lost due to an error.")
            friends_list[index] = "Lost"

    elif cmd == "Change":
        index = int(command[1])
        newName = command[2]
        if index in range(len(friends_list)):
            print(f"{friends_list[index]} changed his username to {newName}.")
            friends_list[index] = newName

    elif cmd == "Report":
        break
counter_b = 0
counter_l = 0
for i in range(len(friends_list)):
    if friends_list[i] == "Blacklisted":
        counter_b += 1
for i in range(len(friends_list)):
    if friends_list[i] == "Lost":
        counter_l += 1

print(f"Blacklisted names: {counter_b}")
print(f"Lost names: {counter_l}")
print(" ".join(friends_list))
