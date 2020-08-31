password_initial = input()
commands = input().split()
what_one = commands[0]

while what_one != "Done":
    if what_one == "TakeOdd":
        middle = ""
        for i in range(len(password_initial)):
            if i % 2 == 1:
                middle += password_initial[i]
        password_initial = middle
        print(password_initial)
    elif what_one == "Cut":
        start_idx = int(commands[1])
        len_idx = int(commands[2])
        to_rem = password_initial[start_idx:len_idx + start_idx]

        password_initial = password_initial.replace(to_rem, "", 1)
        print(password_initial)


    elif what_one == "Substitute":
        substr = commands[1]
        replacement = commands[2]
        if substr in password_initial:
            password_initial = password_initial.replace(substr, replacement)
            print(password_initial)
        else:
            print("Nothing to replace!")
    commands = input().split()
    what_one = commands[0]
print(f"Your password is: {password_initial}")