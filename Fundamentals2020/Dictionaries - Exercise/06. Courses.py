courses = {}
st_course = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course = command[0]
    name = command[1]
    st_course[name] = course
    if course not in courses:
        courses[course] = 1
    else:
        courses[course] += 1

courses = dict(sorted(courses.items(), key=lambda x: -x[1]))
for (key, value) in courses.items():
    print(f"{key}: {value}")
    for (k, v) in sorted(st_course.items()):
        if v == key:
            print(f"-- {k}")
