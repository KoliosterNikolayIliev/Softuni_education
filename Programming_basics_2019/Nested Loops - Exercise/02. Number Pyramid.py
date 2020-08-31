n = int(input())
output = ''
counter = 0
found = False

for row in range(1, n + 1):
    for column in range(1, row + 1):
        counter += 1

        output += f'{counter} '
        if counter == n:
            found = True
            break

    if found:
        break
    output += '\n'

print(output)
