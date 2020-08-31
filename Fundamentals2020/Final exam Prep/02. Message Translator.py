import re

n = int(input())

for _ in range(n):
    line = input().split(":")
    pattern1 = r"(![A-Z]{1}[a-z]+!)"
    pattern2 = r"(\[[A-z]+\])"
    cmd = line[0]
    msg = line[1]
    match1 = re.match(pattern1, cmd)
    match2 = re.match(pattern2, msg)

    if match1 and match2:
        command = str(match1.group(1))
        message = str(match2.group(1))
        command = command[1:len(command) - 1]
        message = message[1:len(message) - 1]
        if len(command) >= 3 and len(message) >= 8:
            encrypted = []
            for i in message:
                encrypted.append(str(ord(i)))
            print(f"{command}: {' '.join(encrypted)}")
        else:
            print("The message is invalid")
    else:
        print("The message is invalid")