def is_valid_walk(walk):
    counter_ns = 0
    counter_ew = 0
    for dir in walk:
        if dir == 's':
            counter_ns += 1
        elif dir == 'n':
            counter_ns -= 1
        elif dir == 'w':
            counter_ew += 1
        elif dir == 'e':
            counter_ew -= 1

    return counter_ns == counter_ew == 0 and len(walk) == 10


print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
