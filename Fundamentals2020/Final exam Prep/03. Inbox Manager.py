users = dict()

while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("->")
    cmd = command[0]
    username = command[1]

    if cmd == "Add":
        if username in users.keys():
            print(f"{username} is already registered")
        else:
            users[username] = []
    elif cmd == "Send":
        Email = command[2]
        users[username].append(Email)
    elif cmd == "Delete":
        if username in users:
            users.pop(username)
        else:
            print(f"{username} not found!")
users = dict(sorted(users.items(), key=lambda x: (-(len(x[1])), x[0])))
print(f"Users count: {len(users)}")
for k, v in users.items():
    print(k)
    for i in v:
        print(f"- {i}")
