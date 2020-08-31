n = int(input())
bunny_pos = []
new_bunny_pos = []
matrix = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
sum_of_eggs = 0
for i in range(n):
    row = input().split()
    matrix.append(row)
    for j in range(n):
        if row[j] == "B":
            bunny_pos = [i, j]

for row in range(len(matrix)):
    for col in range(len(matrix[row]))
        if