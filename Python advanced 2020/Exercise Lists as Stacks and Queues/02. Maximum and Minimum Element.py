n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    cmd = int(command[0])

    if cmd == 1:
        number = int(command[1])
        stack.append(number)
    if cmd == 2:
        if stack:
            stack.pop()
    if cmd == 3:
        if stack:
            print(max(stack))
    if cmd == 4:
        if stack:
            print(min(stack))

stack = [str(x) for x in stack]
rev = []
for i in range(len(stack)):
    rev.append(stack.pop())
print(", ".join(rev))
