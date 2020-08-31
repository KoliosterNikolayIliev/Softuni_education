participants = {}
submissions = {}
results = {}
banned = False
username = ""
while True:
    line = input()
    if line == "exam finished":
        break
    line = line.split("-")
    if line[1] == "banned":
        banned = True
        username = line[0]
        continue
    username = line[0]
    language = line[1]
    points = line[2]

    if username not in participants:
        participants[username] = []
    participants[username].append([language, points])
    submissions[language] = 0
    for i in participants.values():
        for k in i:
            if language in k:
                submissions[language] += 1
    if username not in results:
        results[username] = 0
    for j in participants.values():
        for n in j:
            if points in n:
                if int(points) > results[username]:
                    results[username] = int(points)

if banned:
    results.pop(username)

sorted_results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
print("Results:")
for k, v in sorted_results.items():
    print(f"{k} | {v}")

print("Submissions:")
for key, value in sorted_submissions.items():
    print(f"{key} - {value}")
