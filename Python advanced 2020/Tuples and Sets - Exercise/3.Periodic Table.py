n = int(input())
unique = set()
for _ in range(n):
    elements = input().split()
    for element in elements:
        unique.add(element)
[print(x) for x in unique]