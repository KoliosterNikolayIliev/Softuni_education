import sys

n = int(input())
biggest_number = -sys.maxsize
smallest_number = sys.maxsize
for digit in range(n):
    number = int(input())
    n += 1
    if number > biggest_number:
        biggest_number = number

    if number < smallest_number:
        smallest_number = number
print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')
