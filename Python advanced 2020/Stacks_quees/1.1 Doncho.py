def solve(str):
    stack = []
    reversed_string = ""
    for ch in str:
        stack.append(ch)
    while stack:
        reversed_string += stack.pop()
    return reversed_string


print(solve(input()))
