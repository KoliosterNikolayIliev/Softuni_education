def multiply(a, b):
    return a * b


def add(a, b):
    return a + b

def divide(a, b):
    return a // b


def subtract(a, b):
    return a - b


def execute(a, b, operation):
    mapping = [
        ['multiply', multiply],
        ['add', add],
        ['divide', divide],
        ['subtract', subtract],
    ]
    for operation_name, fn in mapping:
        if operation_name == operation:
            return fn(a, b)


operation = input()
a = int(input())
b = int(input())

print(execute(a, b, operation))