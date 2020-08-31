from _collections import deque

people = deque(input().split())
index = 0
n = int(input())

while people:
    person = people.popleft()
    index += 1
    if index == n:
        index = 0
        if people:
            print(f"Removed {person}")
        else:
            print(f"Last is {person}")
    else:
        people.append(person)
