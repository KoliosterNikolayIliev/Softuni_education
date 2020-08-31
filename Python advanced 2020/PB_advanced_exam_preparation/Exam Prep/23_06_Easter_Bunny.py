def find_position(matrix):
    """Finds position in matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "B":
                position = [row, col]
    return position


size = int(input())
field = [input().split() for x in range(size)]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}

bunny = find_position(field)
bunny_positions = {"right": [], "down": [], "up": [], "left": []}
sums = {"right": 0, "down": 0, "up": 0, "left": 0}
for d in directions:
    row_bunny = bunny[0]
    col_bunny = bunny[1]

    for i in range(size):
        row_bunny += directions[d][0]
        col_bunny += directions[d][1]
        if 0 <= row_bunny < size and 0 <= col_bunny < size:
            new_bunny_pos = [row_bunny, col_bunny]
            if field[row_bunny][col_bunny] == 'X':
                break
            bunny_positions[d].append(new_bunny_pos)
            sums[d] += int(field[row_bunny][col_bunny])

best_sum = -9999999999999999
best_pos = ""
for dir in sums:
    sum = sums[dir]
    if sum > best_sum:
        best_sum = sum
        best_pos = dir

print(best_pos)
for pos in bunny_positions[best_pos]:
    print(pos)
print(best_sum)

