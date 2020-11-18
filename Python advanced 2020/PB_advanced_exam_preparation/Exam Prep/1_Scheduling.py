d = [int(x) for x in input().split(',')]
index = int(input())

task = d[index]
tasks = []

while task in d:
    x = min(d)
    tasks.append(x)
    d.remove(x)

print(sum(tasks))
