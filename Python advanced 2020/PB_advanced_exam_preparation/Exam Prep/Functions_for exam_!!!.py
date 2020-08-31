# Reads matrix line by line from input. size is size of square matrix.
size = int(input())
matrix = [input().split() for x in range(size)]

matrix = []
[matrix.append([x for x in input()]) for x in range(size)] # if string is the input
# dictionary with directions for movement in matrix. Tuple (row, col)
directions = {"right": (0, 1), "down": (1, 0), "up": (-1, 0), "left": (0, -1)}

# printing matrix
[print(' '.join(row)) for row in matrix]

def Cloning(li1):
    """"Clones a list"""
    li_copy = []
    for x in range(len(li1)):
        for y in range(len(li1[x])):
            li_copy.append([])
            li_copy[x].append(li1[x][y])
    return li_copy

def modify_with_step(direction, s):
    """get new direction (row, col) with step. Returns coordinates
    direction is from dictionary with directions"""
    return direction[0] * s, direction[1] * s


def is_valid_change(new_position, object_position, size):
    """Checks if outside of matrix.Takes new position,
    current object position and size of matrix.
     Returns True or False"""
    new_row = object_position[0] + new_position[0]
    new_col = object_position[1] + new_position[1]
    return 0 <= new_row < size and 0 <= new_col < size


def is_valid(pos, size):
    """Checks if outside of matrix.Takes position, and size of matrix.
         Returns True or False"""
    return 0 <= pos[0] < size and 0 <= pos[1] < size


def is_free(new_pos, object_position, matrix):
    """Checks if specific symbol on coordinates.Takes position, and size of matrix.
             Returns True or False. In this case False if object at coordinates !="." """
    new_row = object_position[0] + new_pos[0]
    new_col = object_position[1] + new_pos[1]
    return matrix[new_row][new_col] == "."


def count_items(matrix):
    """Counts if items in input matrix"""
    items = 0
    for row in matrix:
        items += row.count("x")
    return items


def modify(row, col, matrix):
    """modifies item in matrix. can be shoot move, etc.Gets row col and matrix"""
    matrix[row][col] = "x"


def find_position_s(matrix):
    """Finds position in square matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "x":
                position = [row, col]
    return position

def find_position_ns(matrix, rows_count, cols_count, searched):
    """Finds position in matrix, searched is string"""
    position = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == searched:
                position = [row, col]
    return position

#Basic algorithm for traversing square matrix

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