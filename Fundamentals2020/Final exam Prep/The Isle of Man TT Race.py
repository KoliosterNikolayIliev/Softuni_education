import re
code = ''
while True:
    line = input()
    pattern = r"(^[\#|\$|%|\*|&]\b)([A-z]+)\1=([0-9]+)!!(.+$)"  # Doesn't match the length.

    matches = re.match(pattern, line)
    if matches:
        if int(matches.group(3)) == len(matches.group(4)):
            i = matches.group(3)
            l = matches.group(4)
            for i in matches.group(4):
                code += chr(ord(i)+int(matches.group(3)))
            print(f"Coordinates found! {matches.group(2)} -> {code}")
            break
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")
