numbers = [int(n.strip()) for n in input().split(',')]
even_number_indexes = [index for index, number in enumerate(numbers) if number % 2 == 0]
print(even_number_indexes)