import re

n = int(input())

for _ in range(n):
    line = input()
    pattern1 = r"(^\$[A-Z]{1}[a-z]+\$:[ ]\[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$)"
    pattern2 = r"(^%[A-Z]{1}[a-z]+%:[ ]\[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$)"
    kur = line.split(": ")
    tag = kur[0]

    if "$" in tag and len(tag) >= 5 and tag[0] == tag[len(tag)-1]:
        matches1 = re.match(pattern1, line)
        if matches1 is not None:
            undecrypted = matches1.group(2) + matches1.group(3) + matches1.group(4)
            decrypted = chr(int(matches1.group(2)))+chr(int(matches1.group(3)))+chr(int(matches1.group(4)))
            print(f"{tag[1:len(tag)-1]}: {decrypted}")
        else:
            print("Valid message not found!")
    elif "%" in tag and len(tag) >= 5 and tag[0] == tag[len(tag)-1]:
        matches2 = re.match(pattern2, line)
        if matches2 is not None:
            decrypted = chr(int(matches2.group(2)))+chr(int(matches2.group(3)))+chr(int(matches2.group(4)))
            print(f"{tag[1:len(tag)-1]}: {decrypted}")
        else:
            print("Valid message not found!")
    else:
        print("Valid message not found!")
