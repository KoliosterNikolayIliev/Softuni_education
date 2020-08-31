num = input()
lenght = len(num)

for ind in range(lenght, 0, -1):
    current_num = int(num[ind - 1])

    if current_num == 0:
        print('ZERO')
        continue

    ascii_char = chr(current_num + 33)

    for column in range(current_num):
        print(ascii_char, end='')
    print()
