divisor = int(input())
bound = int(input())

while not bound % divisor == 0:
    bound = bound - 1
print(bound)
