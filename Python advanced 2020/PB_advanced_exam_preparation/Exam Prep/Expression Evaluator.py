from collections import deque
from operator import add, sub, mul, floordiv


def operation(operator):
    if operator == "*":
        operator = mul
    elif operator == "/":
        operator = floordiv
    elif operator == "-":
        operator = sub
    elif operator == "+":
        operator = add
    dd = deque(temporary_list)
    for i in range(len(deque(dd))):
        while len(dd) > 1:
            a = dd.popleft()
            b = dd.popleft()
            res = operator(a, b)
            dd.appendleft(res)
    return dd[0]


line = deque(input().split())
temporary_list = []
operators = ("*", "+", "-", "/")

while line:
    if len(line) == 1 and line[0] not in operators:
        break
    el = line.popleft()
    if el not in operators:
        temporary_list.append(int(el))

    else:
        result = operation(el)
        line.appendleft(str(result))
        temporary_list.clear()

print(line[0])
