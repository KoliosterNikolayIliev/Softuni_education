from collections import deque

males = deque(reversed([int(x) for x in input().split()]))
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male = males[0]
    female = females[0]

    if male <= 0:
        males.popleft()

    elif female <= 0:
        females.popleft()

    elif male % 25 == 0:
        males.popleft()
        if males:
            males.popleft()
    elif female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif male == female:
        males.popleft()
        females.popleft()
        matches += 1
    else:
        if females:
            females.popleft()
            males[0] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
