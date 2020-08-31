numbers = list(map(int, input().split(', ')))
group = 10
while len(numbers) > 0:
    filtered = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num > group]
    print(f"Group of {group}'s: {filtered}")
    group += 10
