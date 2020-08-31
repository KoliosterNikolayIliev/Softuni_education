lst = input().split()
rev = []
for i in range(len(lst)):
    rev.append(lst.pop())
print(" ".join(rev))
