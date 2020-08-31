numbers = input().split()
numbers.sort(reverse=True)
number = ''

for i in numbers:
    number += i

print(number)
