bandNames = {}
bandTime = {}
totalTime = 0
while True:
    command = input()
    if command == "start of concert":
        break
    command = command.split("; ")
    cmd = command[0]

    if cmd == "Add":
        bandName = command[1]
        List = command[2].split(", ")
        if bandName not in bandNames.keys():
            bandNames[bandName] = []
            for member in List:
                if member not in bandNames[bandName]:
                    bandNames[bandName].append(member)
        else:
            for member in List:
                if member not in bandNames[bandName]:
                    bandNames[bandName].append(member)
    if cmd == "Play":
        bandName = command[1]
        time = int(command[2])
        if bandName not in bandTime.keys():
            bandTime[bandName] = time
        else:
            bandTime[bandName] += time
for i in bandTime.values():
    totalTime += i
bandTime = dict(sorted(bandTime.items(), key=lambda x: (-x[1], x[0])))
band = input()
print(f"Total time: {totalTime}")
for k, v in bandTime.items():
    print(f"{k} -> {v}")
for k, v in bandNames.items():
    if k == band:
        print(k)
        for i in v:
            print(f"=> {i}")
