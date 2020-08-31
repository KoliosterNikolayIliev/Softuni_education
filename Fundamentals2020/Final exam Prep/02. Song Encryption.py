import re

while True:
    command = input()
    if command == "end":
        break
    pattern = r"^([A-Z]{1}[a-z\' ]+):([A-Z ]+)\b"
    match = re.match(pattern, command)

    if match:
        kur = command.split(":")
        artist = kur[0]
        song = kur[1]
        key = len(artist)
        encrypted = ''
        for i in command:
            if not i.isalpha():
                if i == ':':
                    i = '@'
                encrypted += i
            else:
                if i.islower():
                    if (ord(i) + key) <= ord('z'):
                        encrypted += chr(ord(i) + key)
                    else:
                        encrypted += chr(ord('a')+(ord(i)-ord('z')) + (key-1))
                else:
                    if (ord(i) + key) <= ord('Z'):
                        encrypted += chr(ord(i) + key)
                    else:
                        encrypted += chr(ord('A')+(ord(i)-ord('Z')) + (key-1))

        print(f"Successful encryption: {encrypted}")
    else:
        print("Invalid input!")
