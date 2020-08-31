rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())


while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    cmd = command[0]
    ind_row_1 = int(command[1])
    ind_col_1 = int(command[2])
    ind_row_2 = int(command[3])
    ind_col_2 = int(command[4])

    if cmd:
        for row in range(rows):
            if ind_row_1<=rows and ind_col_1<=cols:
                if ind_row_2 <= rows  and ind_col_2 <= cols :
                    x = matrix[ind_row_1][ind_col_1]
                    y = matrix[ind_row_2][ind_col_2]
                    matrix[ind_row_1][ind_col_1] = y
                    matrix[ind_row_2][ind_col_2] = x
                    for i in range(len(matrix)):
                        print(' '.join(matrix[i]))
                    break
                else:
                    print("Invalid input!")
                    break
            else:
                print("Invalid input!")
                break






