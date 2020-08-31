line = input()
password = ""
rawpassword = ""
flag = False
while True:
    command = input()
    if command == "Done":
        break
    elif command == "TakeOdd":
        for i in range(len(line)):
            if i % 2 != 0:
                password += line[i]
        print(password)
    command = command.split(" ")
    cmd = command[0]
    if password == "":
        password = line

    if cmd == "Cut":
        index = int(command[1])
        length = int(command[2])
        if password == "":
            password = line
            flag = True
        substring = password[index:(index + length)]
        password = password.replace(substring, "", 1)
        if flag:
            rawpassword=password
            print(rawpassword)
        print(password)

    elif cmd == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")

