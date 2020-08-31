n = int(input())
students_grades = {}

for i in range(n):
    student, grade = input(), float(input())
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

st_average_grade = dict((key, sum(value) / len(value)) for (key, value) in students_grades.items())
filtered_average = dict((key, value) for (key, value) in st_average_grade.items() if value >= 4.5)
sorted_av_gr = dict(sorted(filtered_average.items(), key=lambda x: -x[1]))

for (key, value) in sorted_av_gr.items():
    print(f"{key} -> {value:.2f}")
