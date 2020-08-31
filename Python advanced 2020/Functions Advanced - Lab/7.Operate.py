def operate(operator, *args):
    if operator == "+" or operator == "-":
        result = 0
    else:
        result = 1
    for num in args:
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "/":
            result /= num
        else:
            result *= num
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
