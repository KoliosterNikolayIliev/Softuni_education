import sys

number_count = int(input())

counter = 1
smallest_number = sys.maxsize
while counter <= number_count:
    counter += 1
    number = int(input())
    if number < smallest_number:
        smallest_number = number
print(smallest_number)
