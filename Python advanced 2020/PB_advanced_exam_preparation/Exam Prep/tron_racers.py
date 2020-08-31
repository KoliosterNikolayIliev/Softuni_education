def find_position_ns(matrix, rows_count, cols_count, searched):
    """Finds position in matrix, searched is string"""
    position = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == searched:
                position = [row, col]
    return position


def move(player_pos1,player_pos2, cmd1, cmd2, size, player1_name, player2_name):
    players = [player_pos1, player_pos2]
    for i in range(len(players)):
        if players[i] == player_pos2:
            player_pos = player_pos2
            player_name = player2_name
            cmd = cmd2
        elif players[i] == player_pos1:
            player_pos = player_pos1
            player_name = player1_name
            cmd = cmd1
        row_player = player_pos[0]
        col_player = player_pos[1]

        row_player += directions[cmd][0]
        col_player += directions[cmd][1]
        if 0 <= row_player < size and 0 <= col_player < size:
            new_player_pos = [row_player, col_player]
            matrix[row_player][col_player] = player_name
            player_pos = new_player_pos
            players[i] = player_pos
        return matrix, players


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

    # row_player = p1_pos[0]
    # col_player = p1_pos[1]
    #
    # row_player += directions[command1][0]
    # col_player += directions[command1][1]
    # if 0 <= row_player < size and 0 <= col_player < size:
    #     new_player_pos = [row_player, col_player]
    #     matrix[row_player][col_player] = 'f'
    #     p1_pos = new_player_pos
    matrix = move(p1_pos,p2_pos, command1, command2, size, 'f', 's')[0]
    p1_pos = move(p1_pos,p2_pos, command1, command2, size, 'f', 's')[1][0]
    p2_pos = move(p1_pos,p2_pos, command1, command2, size, 'f', 's')[1][1]
    [print(' '.join(row)) for row in matrix]
    print()
