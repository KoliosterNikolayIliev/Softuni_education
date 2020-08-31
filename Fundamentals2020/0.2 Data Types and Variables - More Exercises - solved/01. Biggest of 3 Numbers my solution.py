number1 = int(input())
number2 = int(input())
number3 = int(input())

max_number = 0

if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number1 and number2 > number3:
    max_number = number2
elif number3 > number2 and number3 > number1:
    max_number = number3
print(max_number)
