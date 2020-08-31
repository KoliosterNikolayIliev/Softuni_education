from statistics import mean
n = int(input())
students = {}
for _ in range(n):
    student = input().split()
    name = student[0]
    grade = student[1]
    if name not in students:
        students[name] = []

    students[name].append(grade)

for k, v in students.items():

    f_grade = [float(x) for x in v]
    average = mean(f_grade)
    print(f"{k} -> {' '.join(v)} (avg: {average:.2f})")