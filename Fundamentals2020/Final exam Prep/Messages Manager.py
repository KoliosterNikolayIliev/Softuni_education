capacity = int(input())

users = {}

while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("=")
    cmd = command[0]

    if cmd == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in users.keys():
            users[username] = [sent, received]

    elif cmd == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users.keys() and receiver in users.keys():
            users[sender][0] = users[sender][0] + 1
            users[receiver][1] = users[receiver][1] + 1
            if sum(users[sender]) >= capacity:
                users.pop(sender)
                print(f"{sender} reached the capacity!")
            if sum(users[receiver]) >= capacity:
                users.pop(receiver)
                print(f"{receiver} reached the capacity!")

    elif cmd == "Empty":
        username = command[1]
        if username == "All":
            users.clear()
        else:
            users.pop(username)

print(f"Users count: {len(users)}")
users = dict(sorted(users.items(), key=lambda x: (-(x[1][1]), x[0])))

for k, v in users.items():
    print(f"{k} - {sum(v)}")
