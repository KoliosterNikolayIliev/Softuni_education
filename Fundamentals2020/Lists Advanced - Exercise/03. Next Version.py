current_version = list(map(int, input().split('.')))

current_version[2] += 1
if current_version[2] == 10:
    current_version[2] = 0
    current_version[1] += 1
    if current_version[1] == 10:
        current_version[1] = 0
        current_version[0] += 1

# print(f'{str(current_version[0])}.{str(current_version[1])}.{str(current_version[2])}')
print('.'.join(map(str, current_version)))