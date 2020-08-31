numbers_as_strings = input().split(' ')
numbers = []
opposite_numbers = []

for number in numbers_as_strings:
    numbers.append(int(number))
for i in numbers:
    i *= -1
    opposite_numbers.append(i)

print(opposite_numbers)
