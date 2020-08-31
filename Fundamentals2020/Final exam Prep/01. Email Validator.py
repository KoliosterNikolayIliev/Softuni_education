email = input()

while True:
    command = input()
    if command == "Complete":
        break
    cmd = command.split(" ")
    cmd1 = cmd[0]

    if cmd1 == "Make":
        cmd2 = cmd[1]
        if cmd2 == "Upper":
            email = email.upper()
            print(email)
        else:
            email = email.lower()
            print(email)
    elif cmd1 == "GetDomain":
        count = int(cmd[1])
        print(email[(len(email) - count):])
    elif command == "GetUsername":
        if "@" in email:
            str_for_print = ""
            for i in email:
                if i != "@":
                    str_for_print += i
                else:
                    print(str_for_print)
                    break
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif cmd1 == "Replace":
        char = cmd[1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        assci = ""
        for j in email:
            print(ord(j), end=" ")
