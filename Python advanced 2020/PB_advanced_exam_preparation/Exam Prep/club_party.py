from collections import deque

halls_capacity = int(input())
line = input().split()
halls = {}
letters = deque([])
while line:
    item = line[-1]
    if item.isalpha():
        letters.append(item)
        halls[item] = []
        line.pop()
    else:
        item = int(item)
        if halls:
            sumhal = sum(halls[letters[0]]) + item
            if sumhal <= halls_capacity:
                halls[letters[0]].append(item)
                line.pop()
            else:
                print(f"{letters[0]} -> {', '.join([str(x) for x in halls[letters[0]]])}")
                del halls[letters[0]]
                letters.popleft()
                if halls:
                    halls[letters[0]].append(item)
                    line.pop()
                else:
                    line.pop()
        else:
            line.pop()
