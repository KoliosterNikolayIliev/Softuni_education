string = input()

while True:
    command = input()
    if command == "Finish":
        break

    command = command.split(" ")
    cmd = command[0]

    if cmd == "Replace":
        currentChar = command[1]
        newChar = command[2]
        string = string.replace(currentChar, newChar)
        print(string)
    elif cmd == "Cut":
        startIndex = int(command[1])
        endIndex = int(command[2])
        if 0 <= startIndex <= endIndex < len(string):
            string = string.replace(string[startIndex:endIndex + 1], "", 1)
            print(string)
        else:
            print("Invalid indexes!")
    elif cmd == "Make":
        letters = command[1]
        if letters == "Upper":
            string = string.upper()
            print(string)
        if letters == "Lower":
            string = string.lower()
            print(string)
    elif cmd == "Check":
        word = command[1]
        if word in string:
            print(f"Message contains {word}")
        else:
            print(f"Message doesn't contain {word}")
    elif cmd == "Sum":
        startIndex = int(command[1])
        endIndex = int(command[2])
        if 0 <= startIndex <= endIndex < len(string):
            substring = string[startIndex:endIndex + 1]
            Sum = 0
            for i in substring:
                Sum += ord(i)
            print(Sum)
        else:
            print("Invalid indexes!")
