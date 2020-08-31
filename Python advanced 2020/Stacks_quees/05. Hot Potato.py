from _collections import deque

list_of_people = input().split()
index = 0
people = deque()
for i in list_of_people:
    people.append(i)
n = int(input())


while people:
    person = people.popleft()
    index += 1
    if index == n:
        index=0
        if people:
            print(f"Removed {person}")
        else:
            print(f"Last is {person}")
    else:
        people.append(person)
