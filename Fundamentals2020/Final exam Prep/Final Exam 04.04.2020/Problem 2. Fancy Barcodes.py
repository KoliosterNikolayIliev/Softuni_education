import re

n = int(input())

for _ in range(n):
    line = input()
    pattern = r"^(@\#+\b)([A-Z]{1}([a-zA-Z|0-9]{4,})([A-Z]))(@\#+)"
    matches = re.match(pattern, line)
    if matches:
        text = matches.group(2)
        group = ""
        for i in text:
            if i.isdigit():
                group += i
        if group == "":
            group = "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
