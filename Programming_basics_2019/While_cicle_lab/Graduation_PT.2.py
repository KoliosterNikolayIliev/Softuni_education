name = input()

counter = 1
grade = 0
sum = 0
graduated=True

while counter <= 12:
    grade = float(input())

    if grade >= 4:
        counter += 1
        sum += grade
    else:
        print(f'{name} has been excluded at {counter} grade')
        graduated=False
        break

if graduated:
    print(f'{name} graduated. Average grade: {(sum / 12):.2f}')

