import re

n = int(input())

for _ in range(n):
    line = input().split(":")
    pattern1 = r"([A-z ]+)( )|(([@|*])([A-Z]{1}[a-z]+)\4)"
    pattern2 = r" (\[([A-z])]\|)(\[([A-z])]\|)(\[([A-z])]\|)$"
    cmd = line[0]
    msg = line[1]
    match1 = re.match(pattern1, cmd)
    match2 = re.match(pattern2, msg)
    command = ''
    if match1 and match2:
        command = str(match1.group(5))
        if command == 'None':
            if "@" in cmd:
                cmd = cmd.split("@")
                command = cmd[1]
            else:
                cmd = cmd.split("*")
                command = cmd[1]
        message = str(match2.group(2)) + str(match2.group(4)) + str(match2.group(6))
        if len(command) >= 3:
            encrypted = []
            for i in message:
                encrypted.append(str(ord(i)))
            print(f"{command}: {' '.join(encrypted)}")
        else:
            print("Valid message not found!")
    else:
        print("Valid message not found!")
