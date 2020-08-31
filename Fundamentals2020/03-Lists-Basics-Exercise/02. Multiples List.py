factor = int(input())
count = int(input())
cur_number = 1
numbers = []
while len(numbers) < count:

    if cur_number % factor == 0:
        numbers.append(cur_number)
    cur_number += 1

print(numbers)
