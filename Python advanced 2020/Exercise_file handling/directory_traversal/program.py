import os

path = input()
file_types = {}
for root, directories, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        file_extension = file.split(".")[-1]
        if file_extension not in file_types:
            file_types[file_extension] = []
        file_types[file_extension].append(file)

string = ""

for k, v in sorted(file_types.items()):
    string += f".{k}\n"
    for f_name in sorted(v):
        string += f"- - - {f_name}\n"

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
location = desktop + os.path.sep + "report.txt"
print(location)
with open(location, "w") as file:
    file.write(string)
