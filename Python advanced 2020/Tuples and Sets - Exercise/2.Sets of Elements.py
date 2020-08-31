n, m = [int(x) for x in input().split()]
nset = set()
mset = set()
counter = 0
while True:
    x = int(input())
    counter += 1
    if counter <= n:
        nset.add(x)
    else:
        mset.add(x)
    if counter == m+n:
        break

[print(x) for x in mset.intersection(nset)]
