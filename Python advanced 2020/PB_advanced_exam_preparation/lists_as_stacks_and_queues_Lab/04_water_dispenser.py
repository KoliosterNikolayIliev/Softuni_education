from collections import deque

water_qty = int(input())
name = input()
q = deque()

while name != "Start":
    q.append(name)
    name = input()


while q:
    command = input()
    if command == "End":
        break
    command = command.split()
    if command[0] == "refill":
        water_qty += int(command[1])
    else:
        water = int(command[0])
        if water <= water_qty:
            water_qty -= water
            person = q.popleft()
            print(f"{person} got water")
        else:
            person = q.popleft()
            print(f"{person} must wait")
            q.append(person)

print(f"{water_qty} liters left")
