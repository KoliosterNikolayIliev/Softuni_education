# n = int(input())
#
# matrix = []
# sum_primary = 0
# sum_secondary = 0
# primary = []
# secondary = []
# for i in range(n):
#     row = input().split(", ")
#     matrix.append([int(x) for x in row])
#
# for j in range(n):
#     sum_primary += matrix[j][j]
#     primary.append(matrix[j][j])
#     sum_secondary += matrix[j][n-1-j]
#     secondary.append(matrix[j][n-1-j])
#
# print(f"First diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum_primary}")
# print(f"Second diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum_secondary}")

n = int(input())

matrix = [[int(j) for j in input().split(", ")] for i in range(n)]
primary = [matrix[j][j] for j in range(n)]
secondary = [matrix[j][n-1-j] for j in range(n)]

print(f"First diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Second diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")