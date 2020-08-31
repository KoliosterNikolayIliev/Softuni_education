companies = {}
id_comp = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    Id = command[1]
    company = command[0]
    if company not in companies:
        companies[company] = []
    if Id not in companies[company]:
        companies[company].append(Id)

for (key, value) in sorted(companies.items()):
    print(f"{key}")
    for (k, v) in sorted(companies.items()):
        if k == key:
            print("--", '\n-- '.join(map(str, v)))
