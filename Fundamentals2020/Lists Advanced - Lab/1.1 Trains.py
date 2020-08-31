wagons_n = int(input())
train = [0] * wagons_n

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split(" ")
    instructions = tokens[0]

    if instructions == 'add':
        count = int(tokens[1])
        train[-1] += count
    elif instructions == 'insert':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] += count
    elif instructions == 'leave':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] -= count

print(train)