rows, columns = [int(x) for x in input().split(", ")]
matrix = []
Sum = 0
for i in range(rows):
    c = [int(x) for x in input().split(", ")]
    matrix.append(c)
    Sum += sum(c)

print(Sum)
print(matrix)
