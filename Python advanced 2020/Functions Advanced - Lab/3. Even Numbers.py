seq = [int(x) for x in input().split()]

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))