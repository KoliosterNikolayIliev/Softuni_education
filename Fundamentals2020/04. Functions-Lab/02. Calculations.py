input_operator = input()
first_num = int(input())
second_num = int(input())


def calculate(num1, num2, operator):
    result = None
    if operator == 'multiply':
        result = num1 * num2
        return result
    if operator == 'divide':
        result = int(num1 / num2)
        return result
    if operator == 'add':
        result = num1 + num2
        return result
    if operator == 'subtract':
        result = num1 - num2
        return result


print(calculate(first_num, second_num, input_operator))
