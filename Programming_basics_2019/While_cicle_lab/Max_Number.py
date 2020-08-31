import sys

number_count = int(input())

counter = 1
bigest_number = -sys.maxsize
while counter <= number_count:
    counter += 1
    number = int(input())
    if number > bigest_number:
        bigest_number = number
print(bigest_number)
