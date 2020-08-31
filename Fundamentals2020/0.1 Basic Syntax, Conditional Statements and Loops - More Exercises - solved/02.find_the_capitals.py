string = input()
capitals = []
for i in range(len(string)):
    ch = string[i]
    if ch == ch.upper() and not ch.isdigit() and ch != " ":
        capitals.append(i)
print(capitals)