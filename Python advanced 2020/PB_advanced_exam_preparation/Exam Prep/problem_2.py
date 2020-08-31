def find_position(matrix, name):
    """Finds position in square matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == name:
                position = [row, col]
    return position


size = int(input())
matrix = []
[matrix.append([x for x in input()]) for x in range(size)]
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}
food_eaten = 0

snake = find_position(matrix, 'S')
snake_pos = snake
while True:
    if food_eaten == 10:
        print("You won! You fed the snake.")
        break
    command = input()
    row_snake = snake_pos[0]
    col_snake = snake_pos[1]

    row_snake += directions[command][0]
    col_snake += directions[command][1]
    if 0 <= row_snake < size and 0 <= col_snake < size:
        matrix[snake_pos[0]][snake_pos[1]] = '.'
        if matrix[row_snake][col_snake] == 'B':
            matrix[row_snake][col_snake] = '.'
            new_snake_pos = find_position(matrix, 'B')
            snake_pos = new_snake_pos
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
        else:
            if matrix[row_snake][col_snake] == '*':
                food_eaten += 1
            matrix[snake_pos[0]][snake_pos[1]] = '.'
            new_snake_pos = [row_snake, col_snake]
            snake_pos = new_snake_pos
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
    else:
        matrix[snake_pos[0]][snake_pos[1]] = '.'
        print("Game over!")
        break
print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in matrix]
