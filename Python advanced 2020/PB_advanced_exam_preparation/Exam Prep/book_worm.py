def find_position(matrix):
    """Finds position in matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                position = [row, col]
                break
    return position


string = input()
size = int(input())
matrix = []
[matrix.append([x for x in input()]) for x in range(size)]
n = int(input())

directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}

worm = find_position(matrix)
current_pos = worm
for i in range(n):
    command = input()
    row_worm = current_pos[0]
    col_worm = current_pos[1]

    if command in directions:
        row_worm += directions[command][0]
        col_worm += directions[command][1]
        if 0 <= row_worm < size and 0 <= col_worm < size:
            new_worm_pos = [row_worm, col_worm]
            matrix[current_pos[0]][current_pos[1]] = '-'
            current_pos = new_worm_pos
            if matrix[row_worm][col_worm] != '-':
                string += matrix[row_worm][col_worm]
            matrix[row_worm][col_worm] = 'P'


        else:
            if string:
                string = string[:-1]
print(string)
[print(''.join(row)) for row in matrix]
