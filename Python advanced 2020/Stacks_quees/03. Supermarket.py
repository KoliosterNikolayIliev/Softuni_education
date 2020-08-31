from _collections import deque

q = deque()
while True:

    name = input()
    if name == "End":
        break
    if name !="Paid":
        q.append(name)
    else:
        while q:
            print(q.popleft())

print(f"{len(q)} people remaining.")


