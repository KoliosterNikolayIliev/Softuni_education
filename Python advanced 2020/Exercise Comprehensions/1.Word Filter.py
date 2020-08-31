strings = [x for x in input().split()]
print("\n".join([x for x in strings if len(x) % 2 == 0]))
