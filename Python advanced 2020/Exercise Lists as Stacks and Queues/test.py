expression = input()
brackets = []

for i in range(len(expression)):
    if expression[i] == "(":
        brackets.append(i)
    elif expression[i] == ")":
        start_index = brackets.pop()
        print(expression[start_index:i + 1])