import math

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

result1 = (n1 + n2) / n3
result2 = math.floor(result1)
result = result2 * n4
print(f'{result:.0f}')
