n = int(input())
unique = []
for i in range(n):
    name = input()
    unique.append(name)
[print(x) for x in set(unique)]