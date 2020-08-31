# 1. number of rooms
# 2. for number of rooms taken chairs
# 3. convert list of total chairs and people
# 4. count free chairs
# 5.if people more than chairs print message
# 6. at the end print free chairs only if there are no people wihout chairs

rooms = int(input())
total_free_chairs = 0
for room in range(1, rooms + 1):
    tokens = input().split()
    chairs_x = str(tokens[0])
    chairs_l = list(chairs_x)
    chairs = 0
    for i in range(1, len(chairs_l) + 1):
        if i > chairs:
            chairs = i
    people = int(tokens[1])
    free_chairs = chairs - people
    if free_chairs >= 0:
        total_free_chairs += free_chairs
    else:
        total_free_chairs = -1
    if people > chairs:
        print(f'{abs(free_chairs)} more chairs needed in room {room}')

if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
