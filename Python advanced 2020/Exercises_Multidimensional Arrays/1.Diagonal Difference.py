n = int(input())

matrix = []
sum_primary = 0
sum_secondary = 0
for i in range(n):
    row = input().split()
    matrix.append([int(x) for x in row])

for j in range(n):
    sum_primary += matrix[j][j]
    sum_secondary += matrix[j][n-1-j]

print(abs(sum_primary-sum_secondary))

