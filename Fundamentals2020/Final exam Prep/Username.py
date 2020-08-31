username = input()

while True:
    command = input()
    if command == "Sign up":
        break

    tokens = command.split(" ")
    cmd = tokens[0]

    if cmd == "Case":
        cmd2 = tokens[1]
        if cmd2 == "lower":
            username = username.lower()
        else:
            username = username.upper()
        print(username)

    elif cmd == "Reverse":
        start = int(tokens[1])
        end = int(tokens[2]) + 1
        if 0 <= start <= end and start < end <= len(username):
            result = username[start:end]
            result = result[::-1]
            print(result)

    elif cmd == "Cut":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif cmd == "Replace":
        char = tokens[1]
        username = username.replace(char, "*")
        print(username)
    elif cmd == "Check":
        char = tokens[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
