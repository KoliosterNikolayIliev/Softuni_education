name = input()

counter = 1
grade = 0
sum = 0
while counter <= 12:
    grade = float(input())
    if grade >= 4:
        counter += 1
        sum += grade

print(f'{name} graduated. Average grade: {(sum / 12):.2f}')
