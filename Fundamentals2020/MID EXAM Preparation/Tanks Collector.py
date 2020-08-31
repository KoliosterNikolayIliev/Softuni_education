tank_list = input().split(", ")
n = int(input())

for i in range(n):
    command = input().split(", ")
    cmd = command[0]
    if cmd == "Add":
        tankName = command[1]
        if tankName in tank_list:
            print("Tank is already bought")
        else:
            tank_list.append(tankName)
            print("Tank successfully bought")

    elif cmd == "Remove":
        tankName = command[1]
        if tankName not in tank_list:
            print("Tank not found")
        else:
            tank_list.remove(tankName)
            print("Tank successfully sold")

    elif cmd == "Remove At":
        index = int(command[1])
        if index in range(len(tank_list)):
            tank_list.pop(index)
            print("Tank successfully sold")
        else:
            print("Index out of range")

    elif cmd == "Insert":
        index = int(command[1])
        tankName = command[2]
        if index in range(len(tank_list)):
            if tankName in tank_list:
                print("Tank is already bought")
            else:
                tank_list.insert(index, tankName)
                print("Tank successfully bought")
        else:
            print("Index out of range")

print(", ".join(tank_list))
