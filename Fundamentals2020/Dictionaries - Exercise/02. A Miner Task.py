resources = {}
counter = 0
resource = ""

while True:
    qty = 0
    line = input()
    if line == "stop":
        break
    counter += 1
    if counter % 2 != 0:
        resource = line
    else:
        qty = int(line)
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += qty
for (resource, qty) in resources.items():
    print(f"{resource} -> {qty}")
