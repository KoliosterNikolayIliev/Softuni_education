def get_magic_triangle(n):
    ll = [[1] * x for x in range(1, n + 1)]
    for row in range(2, n):
        for col in range(1, row):
            ll[row][col] = ll[row - 1][col - 1] + ll[row - 1][col]
    return ll


get_magic_triangle(5)
