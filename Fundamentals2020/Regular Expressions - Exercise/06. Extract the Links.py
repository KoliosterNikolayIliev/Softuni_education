import re

pattern = r'(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)'

while True:
    line = input()
    if not line:
        break
    matches = [x[0] for x in re.findall(pattern, line)]
    for match in matches:
        print(match)

