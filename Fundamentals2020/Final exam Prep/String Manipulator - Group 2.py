string = input()

while True:
    command = input()
    if command == "Done":
        break
    elif command == "Uppercase":
        string = string.upper()
        print(string)

    command = command.split(" ")
    cmd = command[0]
    if cmd == "Change":
        char = command[1]
        replacement = command[2]
        string = string.replace(char, replacement)
        print(string)

    elif cmd == "Includes":
        word = command[1]
        if word in string:
            print(True)
        else:
            print(False)

    elif cmd == "End":
        word = command[1]
        print(f"{string.endswith(word)}")

    elif cmd == "FindIndex":
        char = command[1]
        for i in range(len(string)):
            if string[i] == char:
                print(i)
                break

    elif cmd == "Cut":
        start = int(command[1])
        length = int(command[2])
        string = string[start:]
        string = string[:length]
        print(string)
