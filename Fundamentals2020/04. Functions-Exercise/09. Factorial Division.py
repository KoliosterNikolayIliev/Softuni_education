def factorial(n):
    for i in range(n, 1, -1):
        n *= (i - 1)
    return n


def factorial_div(a, b):
    result = factorial(a) / factorial(b)
    return f'{result:.2f}'


a = int(input())
b = int(input())

print(factorial_div(a, b))
