indexes = input().split()

n = int(indexes[0])
s = int(indexes[1])
x = int(indexes[2])
stack = []
lst = input().split()

for i in lst:
    stack.append(int(i))

for _ in range(s):
    stack.pop()

if stack:
    if x not in stack:
        print(min(stack))
    else:
        print(True)
else:
    print(0)
