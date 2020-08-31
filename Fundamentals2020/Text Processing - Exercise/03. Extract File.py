path = input().split(chr(92))
for i in range(len(path)):
    if "." in path[i]:
        file = path[i].split(".")
        filename = file[0]
        extension = file[1]
        print(f"File name: {filename}")
        print(f"File extension: {extension}")
