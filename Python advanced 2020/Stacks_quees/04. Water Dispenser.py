from _collections import deque

water = int(input())
name = input()
q = deque()
while name != "Start":
    q.append(name)
    name = input()

while q:

    command = input()
    if command.startswith("refill"):
        command = command.split()
        water += int(command[1])
    else:
        name = q.popleft()
        name_liters = int(command)
        if water < name_liters:
            print(f'{name} must wait')
        else:
            water -= name_liters
            print(f'{name} got water')
print(f'{water} liters left')
