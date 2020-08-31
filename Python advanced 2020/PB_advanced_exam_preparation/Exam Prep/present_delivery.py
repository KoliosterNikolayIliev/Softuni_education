def find_position(matrix):
    """Finds position in matrix"""
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "S":
                position = [row, col]
    return position


def count_items(matrix):
    """Counts if items in input matrix"""
    items = 0
    for row in matrix:
        items += row.count("V")
    return items


presents_count = int(input())
happy_kids = 0
size = int(input())
matrix = [input().split() for x in range(size)]
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

santa = find_position(matrix)
current_pos = santa

while True:
    if presents_count == 0:
        break
    command = input()
    if command == 'Christmas morning':
        break
    row_santa = current_pos[0]
    col_santa = current_pos[1]

    row_santa += directions[command][0]
    col_santa += directions[command][1]
    if 0 <= row_santa < size and 0 <= col_santa < size:
        new_santa_pos = [row_santa, col_santa]
        if matrix[row_santa][col_santa] == 'V':
            presents_count -= 1
            happy_kids += 1

        elif matrix[row_santa][col_santa] == 'C':
            matrix[current_pos[0]][current_pos[1]] = '-'
            current_pos = new_santa_pos
            matrix[row_santa][col_santa] = 'S'
            for d in directions:
                row_santa = current_pos[0]
                col_santa = current_pos[1]
                row_santa += directions[d][0]
                col_santa += directions[d][1]
                if matrix[row_santa][col_santa] in 'VX':
                    if matrix[row_santa][col_santa] == 'V':
                        happy_kids += 1
                    presents_count -= 1
                    matrix[row_santa][col_santa] = '-'
                    if presents_count == 0:
                        break
            continue
        matrix[current_pos[0]][current_pos[1]] = '-'
        current_pos = new_santa_pos
        matrix[row_santa][col_santa] = 'S'

kids = count_items(matrix)
if presents_count == 0 and kids > 0:
    print("Santa ran out of presents!")
[print(' '.join(row)) for row in matrix]

if kids > 0:
    print(f'No presents for {kids} nice kid/s.')
else:
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
