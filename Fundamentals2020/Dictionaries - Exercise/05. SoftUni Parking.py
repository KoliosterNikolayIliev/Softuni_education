n = int(input())
registered = {}
for i in range(n):
    command = input().split(" ")
    desire = command[0]
    username = command[1]

    if desire == "register":
        license_plate = command[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            registered[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    if desire == "unregister":
        license_plate = command[1]
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            license_plate = registered.pop(username)
            print(f"{username} unregistered successfully")
for (username, license_plate) in registered.items():
    print(f"{username} => {license_plate}")
