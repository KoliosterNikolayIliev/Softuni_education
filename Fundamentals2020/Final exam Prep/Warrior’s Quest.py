input_string = input()

while True:
    command = input()
    if command == "For Azeroth":
        break
    cmd = command.split(" ")
    if command == "GladiatorStance":
        input_string = input_string.upper()
        print(input_string)
    elif command == "DefensiveStance":
        input_string = input_string.lower()
        print(input_string)
    elif cmd[0] == "Dispel":
        index = int(cmd[1])
        letter = cmd[2]
        if 0 <= index < len(input_string):
            input_string = input_string.replace(input_string[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif cmd[0] == "Target":
        if cmd[1] == "Change":
            input_string = input_string.replace(cmd[2], cmd[3],)
            print(input_string)
        elif cmd[1] == "Remove":
            input_string = input_string.replace(cmd[2], '', 1)
            print(input_string)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")
