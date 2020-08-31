def count_items(matrix):
    """Counts if items in input matrix"""
    items = 0
    for row in matrix:
        items += row.count("c")
    return items


def find_position(matrix):
    """Finds position in matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "s":
                position = [row, col]
    return position


size = int(input())
commands = (input().split())
matrix = [input().split() for x in range(size)]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}
start_pos = find_position(matrix)
total_coal = count_items(matrix)
coal_collected = 0
# [print(' '.join([str(x) for x in row])) for row in matrix]
# print(commands)
# print(start_pos)

while commands:
    command = commands.pop(0)
    new_pos = start_pos
    row_start = new_pos[0]
    col_start = new_pos[1]
    row_start += directions[command][0]
    col_start += directions[command][1]
    if 0 <= row_start < size and 0 <= col_start < size:
        new_pos = [row_start, col_start]
        start_pos = new_pos
        if matrix[row_start][col_start] == 'c':
            coal_collected += 1
            matrix[row_start][col_start] = '*'
            if coal_collected == total_coal:
                print(f"You collected all coals! ({row_start}, {col_start})")
                break
        elif matrix[row_start][col_start] == 'e':
            print(f"Game over! ({row_start}, {col_start})")
            break
        else:
            if not commands:
                print(f"{count_items(matrix)} coals left. ({row_start}, {col_start})")
                break
