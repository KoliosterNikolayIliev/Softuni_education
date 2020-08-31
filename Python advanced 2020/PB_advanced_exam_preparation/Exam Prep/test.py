from collections import deque

halls_capacity = int(input())
line = input().split()
halls = {}
filled_halls = {}
letters = deque([])
reservations = []
counter = 0
while line:
    item = line.pop()
    if item.isalpha():
        letters.append(item)
    elif letters:
        reservations.append(item)

reservations.reverse()

for i in letters:
    halls[i] = []

while reservations:
    reservation = reservations.pop()
    hall_sum = sum(halls[letters[0]]) + int(reservation)

    if hall_sum <= halls_capacity:
        halls[letters[0]].append(int(reservation))
    else:
        # for_print1 = letters[0]
        # for_print2 = ', '.join([str(x) for x in halls[letters[0]]])
        # print(f"{for_print1} -> {for_print2}"


        if halls:
            del halls[letters[0]]
            letters.popleft()
            halls[letters[0]].append(int(reservation))

