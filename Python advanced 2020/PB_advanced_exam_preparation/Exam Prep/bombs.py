def find_position(matrix):
    """Finds position in matrix"""
    position = []
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] > 0:
                counter += 1
                position.append(matrix[row][col])
    return position, counter


size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]
line = [tuple([int(x) for x in x.split(",")]) for x in input().split()]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1),
              "up_left": (-1, -1), "up_right": (-1, 1), "down_left": (1, -1), "down_right": (1, 1)}

# [print(' '.join([str(x) for x in row])) for row in matrix]
# print(line)

for i in line:
    row = i[0]
    col = i[1]
    pos = [row, col]
    bomb = matrix[row][col]
    if 0 <= row < size and 0 <= col < size and bomb > 0:
        for d in directions:
            new_row = row + directions[d][0]
            new_col = col + directions[d][1]
            new_pos = [new_row, new_col]
            if 0 <= new_row < size and 0 <= new_col < size and matrix[new_row][new_col] > 0:
                killed = matrix[new_row][new_col]
                matrix[new_row][new_col] -= bomb

        matrix[row][col] = 0
print(f"Alive cells: {find_position(matrix)[1]}")
print(f"Sum: {sum(find_position(matrix)[0])}")
[print(' '.join([str(x) for x in row])) for row in matrix]
