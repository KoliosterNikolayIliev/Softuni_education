def Cloning(li1):
    li_copy = []
    for x in range(len(li1)):
        for y in range(len(li1[x])):
            li_copy.append([])
            li_copy[x].append(li1[x][y])
    return li_copy


def find_position(matrix, rows_count, cols_count, searched):
    """Finds position in matrix, searched is string"""
    position = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == searched:
                position = [row, col]
    return position


data = input().split()
rows_count = int(data[0])
cols_count = int(data[1])
directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
matrix = []
win = False
dead1 = ""
dead2 = ""
[matrix.append([x for x in input()]) for x in range(rows_count)]
matrix_bun = Cloning(matrix)
line = [x for x in input()]

player = find_position(matrix, rows_count, cols_count, 'P')
start_pos = player
for d in line:
    if win:
        break
    if dead1 != "" or dead2 != "":
        break
    row_player = start_pos[0]
    col_player = start_pos[1]

    n_row_player = row_player + directions[d][0]
    n_col_player = col_player + directions[d][1]
    if 0 <= n_row_player < rows_count and 0 <= n_col_player < cols_count:
        matrix[row_player][col_player] = '.'
        new_player_pos = [n_row_player, n_col_player]
        start_pos = new_player_pos
        if matrix[n_row_player][n_col_player] == '.':
            matrix[n_row_player][n_col_player] = 'P'
        else:
            dead1 = f"dead: {n_row_player} {n_col_player}"
            # lost = True
    else:
        matrix[row_player][col_player] = '.'
        won = f"won: {row_player} {col_player}"
        win = True
    for i in range(rows_count):
        for j in range(cols_count):
            if matrix_bun[i][j] == 'B':
                pos_b = [i, j]
                for x in directions:
                    new_bun_r = pos_b[0] + directions[x][0]
                    new_bun_c = pos_b[1] + directions[x][1]
                    if 0 <= new_bun_r < rows_count and 0 <= new_bun_c < cols_count:
                        if matrix[new_bun_r][new_bun_c] == '.':
                            matrix[new_bun_r][new_bun_c] = 'B'
                        if matrix[new_bun_r][new_bun_c] == 'P':
                            matrix[new_bun_r][new_bun_c] = 'B'
                            dead2 = f"dead: {new_bun_r} {new_bun_c}"


    matrix_bun = Cloning(matrix)

[print(''.join(row)) for row in matrix]
if win:
    print(won)
elif dead1 != "":
    print(dead1)
else:
    print(dead2)
