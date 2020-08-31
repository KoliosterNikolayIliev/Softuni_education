n = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(n)]
flattened = [num for j in matrix for num in j]
print(flattened)