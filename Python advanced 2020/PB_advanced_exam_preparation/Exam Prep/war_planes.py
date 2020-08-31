def get_pos(dir_changes, s):
    return [x * s for x in dir_changes]


def is_valid(pos, plane_pos, size):
    new_row = plane_pos[0] + pos[0]
    new_col = plane_pos[1] + pos[1]
    return 0 <= new_row < size and 0 <= new_col < size


def shoot(r, c, f):
    f[r][c] = 'x'


def is_free(pos, plane_pos, matrix):
    new_row = plane_pos[0] + pos[0]
    new_col = plane_pos[1] + pos[1]
    return matrix[new_row][new_col] == '.'


def get_current_targets(matrix):
    targets = 0
    for row in matrix:
        targets += row.count("t")
    return targets


n = int(input())
plane = []
targets_count = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

field = [[x for x in input().split()] for x in range(n)]

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == "p":
            plane = [i, j]
        elif field[i][j] == "t":
            targets_count += 1

m = int(input())

for _ in range(m):
    command = input().split()
    step = int(command[2])
    direction = command[1]
    command = command[0]
    direction_changes = directions[direction]
    get_position = get_pos(direction_changes, step)

    if command == 'shoot':

        if is_valid(get_position, plane, n):
            shoot_row = plane[0] + get_position[0]
            shoot_col = plane[1] + get_position[1]
            shoot(shoot_row, shoot_col, field)

            if get_current_targets(field) == 0:
                print(f"Mission accomplished! All {targets_count} targets destroyed.")
                break


    else:

        if is_valid(get_position, plane, n) and is_free(get_position, plane, field):
            field[plane[0]][plane[1]] = '.'
            plane[0] += get_position[0]
            plane[1] += get_position[1]
            field[plane[0]][plane[1]] = 'p'

targets_left = get_current_targets(field)
if targets_left > 0:
    print(f"Mission failed! {targets_left} targets left.")

[print(' '.join(row)) for row in field]
