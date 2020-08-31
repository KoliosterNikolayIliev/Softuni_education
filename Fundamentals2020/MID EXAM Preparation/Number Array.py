numbers = [int(x) for x in input().split(" ")]
negative = []
positive = []
print_positive = []
while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Switch":
        index = int(command[1])
        if index in range(len(numbers)):
            numbers[index] *= -1
    elif cmd == "Change":
        index = int(command[1])
        value = int(command[2])
        if index in range(len(numbers)):
            del numbers[index]
            numbers.insert(index, value)

    elif cmd == "Sum":
        num = command[1]
        if num == "Negative":
            for i in range(len(numbers)):
                if numbers[i] < 0:
                    negative.append(numbers[i])
            print(sum(negative))
        elif num == "Positive":
            for i in range(len(numbers)):
                if numbers[i] >= 0:
                    positive.append(numbers[i])
            print(sum(positive))

        elif num == "All":
            print(sum(numbers))
    elif cmd == "End":
        break

for i in range(len(numbers)):
    if numbers[i] >= 0:
        print_positive.append(numbers[i])

print(f"{' '.join([str(x) for x in print_positive])}")
