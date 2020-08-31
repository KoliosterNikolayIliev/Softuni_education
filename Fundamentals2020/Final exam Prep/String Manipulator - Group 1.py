input_string = input()

while True:
    command = input()
    if command == "End":
        break
    if command == "Lowercase":
        input_string = input_string.lower()
        print(input_string)

    command = command.split(" ")
    cmd = command[0]

    if cmd == "Translate":
        char = command[1]
        replacement = command[2]
        if char in input_string:
            input_string = input_string.replace(char, replacement)
            print(input_string)

    elif cmd == "Includes":
        string = command[1]
        if string in input_string:
            print(True)
        else:
            print(False)

    elif cmd == "Start":
        str = command[1]
        if input_string[:len(str)] == str:
            print(True)
        else:
            print(False)

    elif cmd == "FindIndex":
        char = command[1]
        z = []
        for i in range(len(input_string)):
            if input_string[i] == char:
                z.append(i)
        print(max(z))

    elif cmd == "Remove":
        startIndex = int(command[1])
        count = int(command[2])
        result = input_string.replace(input_string[startIndex:startIndex+count], '')
        print(result)
