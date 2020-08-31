bad_grades_count = int(input())

failed_attempts = 0
solved_problems_count = 0
grade_sum = 0
last_problem = ''
has_failed = True

while failed_attempts < bad_grades_count:
    problem_name = input()

    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    grade_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

    if grade <= 4:
        failed_attempts += 1

if has_failed:
    print(f'You need a break, {bad_grades_count} poor grades.')

else:
    print(f'Average score: {(grade_sum / solved_problems_count):.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')
