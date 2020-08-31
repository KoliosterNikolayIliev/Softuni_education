def find_position_ns(matrix, rows_count, cols_count, searched):
    """Finds position in matrix, searched is string"""
    position = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == searched:
                position = [row, col]
    return position


size = int(input())
matrix = []
[matrix.append([x for x in input()]) for x in range(size)]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}

p1_start_pos = find_position_ns(matrix, size, size, "f")
p2_start_pos = find_position_ns(matrix, size, size, "s")
p1_pos = p1_start_pos
p2_pos = p2_start_pos
while True:
    command = input().split()
    command1 = command[0]
    command2 = command[1]

    row_player1 = p1_pos[0]
    col_player1 = p1_pos[1]
    row_player2 = p2_pos[0]
    col_player2 = p2_pos[1]

    row_player1 += directions[command1][0]
    col_player1 += directions[command1][1]
    row_player2 += directions[command2][0]
    col_player2 += directions[command2][1]
    if 0 <= row_player1 < size and 0 <= col_player1 < size:
        new_player1_pos = [row_player1, col_player1]
        if matrix[row_player1][col_player1] == 's':
            matrix[row_player1][col_player1] = 'x'
            break

        else:
            matrix[row_player1][col_player1] = 'f'
            p1_pos = new_player1_pos
    else:  # kur1
        if 0 > row_player1:
            row_player1 = size - 1
        elif size <= row_player1:
            row_player1 = 0
        if 0 > col_player1:
            col_player1 = size - 1
        elif size <= col_player1:
            col_player1 = 0
        new_player1_pos = [row_player1, col_player1]
        if matrix[row_player1][col_player1] == 's':
            matrix[row_player1][col_player1] = 'x'
            break

        else:
            matrix[row_player1][col_player1] = 'f'
            p1_pos = new_player1_pos
    # kraj kur 1

    if 0 <= row_player2 < size and 0 <= col_player2 < size:
        new_player2_pos = [row_player2, col_player2]
        if matrix[row_player2][col_player2] == 'f':
            matrix[row_player2][col_player2] = 'x'
            break
        else:
            matrix[row_player2][col_player2] = 's'
            p2_pos = new_player2_pos

    else:  # kur2
        if 0 > row_player2:
            row_player2 = size - 1
        elif size <= row_player2:
            row_player2 = 0
        if 0 > col_player2:
            col_player2 = size - 1
        elif size <= col_player2:
            col_player2 = 0
        new_player2_pos = [row_player2, col_player2]
        if matrix[row_player2][col_player2] == 'f':
            matrix[row_player2][col_player2] = 'x'
            break
        else:
            matrix[row_player2][col_player2] = 's'
            p2_pos = new_player2_pos
        # kraj kur 2
[print(''.join(row)) for row in matrix]
