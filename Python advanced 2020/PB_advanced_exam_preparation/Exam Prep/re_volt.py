def find_position_ns(matrix, rows_count, cols_count, searched):
    """Finds position in matrix, searched is string"""
    position = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == searched:
                position = [row, col]
    return position


size = int(input())
count_of_commands = int(input())
matrix = []
[matrix.append([x for x in input()]) for x in range(size)]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}
won = False

start_pos = find_position_ns(matrix, size, size, "f")
player = start_pos
for _ in range(count_of_commands):
    command = input()
    row_player = player[0]
    col_player = player[1]
    if matrix[player[0]][player[1]] not in 'BT':
        matrix[player[0]][player[1]] = '-'
    elif matrix[row_player][col_player] == 'F':
        matrix[row_player][col_player] = 'f'
        won = True
        break
    row_player += directions[command][0]
    col_player += directions[command][1]
    if 0 <= row_player < size and 0 <= col_player < size:
        new_player_pos = [row_player, col_player]
        player = new_player_pos
        if matrix[row_player][col_player] == 'F':
            matrix[row_player][col_player] = 'f'
            won = True
            break
    else:
        if 0 > row_player:
            row_player = size - 1
        elif size <= row_player:
            row_player = 0
        if 0 > col_player:
            col_player = size - 1
        elif size <= col_player:
            col_player = 0
        new_player_pos = [row_player, col_player]
        player = new_player_pos
        if matrix[row_player][col_player] == 'F':
            matrix[row_player][col_player] = 'f'
            won = True
            break

    if matrix[row_player][col_player] == 'B':
        row_player += directions[command][0]
        col_player += directions[command][1]
        if 0 <= row_player < size and 0 <= col_player < size:
            new_player_pos = [row_player, col_player]
            player = new_player_pos
            if matrix[row_player][col_player] == 'F':
                matrix[row_player][col_player] = 'f'
                won = True
                break
        else:
            if 0 > row_player:
                row_player = size - 1
            elif size <= row_player:
                row_player = 0
            if 0 > col_player:
                col_player = size - 1
            elif size <= col_player:
                col_player = 0
            new_player_pos = [row_player, col_player]
            player = new_player_pos
            if matrix[row_player][col_player] == 'F':
                matrix[row_player][col_player] = 'f'
                won = True
                break
        matrix[row_player][col_player] = 'f'
    if matrix[row_player][col_player] == 'T':
        row_player -= directions[command][0]
        col_player -= directions[command][1]
        if 0 <= row_player < size and 0 <= col_player < size:
            new_player_pos = [row_player, col_player]
            player = new_player_pos
            if matrix[row_player][col_player] == 'F':
                matrix[row_player][col_player] = 'f'
                won = True
                break
        else:
            if 0 > row_player:
                row_player = size - 1
            elif size <= row_player:
                row_player = 0
            if 0 > col_player:
                col_player = size - 1
            elif size <= col_player:
                col_player = 0
            new_player_pos = [row_player, col_player]
            player = new_player_pos
            if matrix[row_player][col_player] == 'F':
                matrix[row_player][col_player] = 'f'
                won = True
                break
        matrix[row_player][col_player] = 'f'
    elif matrix[row_player][col_player] == 'F':
        matrix[row_player][col_player] = 'f'
        won = True
        break
    else:
        matrix[row_player][col_player] = 'f'

if won:
    print("Player won!")
else:
    print("Player lost!")

[print(''.join(row)) for row in matrix]
