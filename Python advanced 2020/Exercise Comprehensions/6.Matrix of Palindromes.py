r, c = [int(x) for x in input().split()]

matrix = [[f"{chr(row)}{chr(row + col)}{chr(row)}" for col in range(c)] for row in range(97, 97 + r)]

[print(' '.join(row)) for row in matrix]
