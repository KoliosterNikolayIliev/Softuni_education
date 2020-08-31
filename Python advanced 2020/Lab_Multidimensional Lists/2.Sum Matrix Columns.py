rows, columns = [int(x) for x in input().split(", ")]
matrix = [[0] * columns for row in range(rows)]
for row in range(rows):
    lines = [int(x) for x in input().split()]
    for column in range(columns):
        matrix[row][column] = lines[column]
Sum = [0] * columns
for column in range(columns):
    for row in range(rows):
        Sum[column] += matrix[row][column]
    print(Sum[column])
