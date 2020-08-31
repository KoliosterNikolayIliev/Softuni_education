import os

path = input()
report = {}
sep_count = path.count(os.path.sep)

for root, directories, files in os.walk(path):
    if root.count(os.path.sep) - sep_count > 1:
        continue
    for file in files:
        extension = file.split(".")[-1]
        if extension not in report:
            report[extension] = []
        report[extension].append(file)

report = dict(sorted(report.items(), key=lambda y: (y[0], y[1])))

windows_desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") + os.path.sep + "report.txt"
linux_desktop_path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop") + os.path.sep + "report.txt"

# change windows_desktop_path to linux_desktop_path if you are using Linux
with open(windows_desktop_path, "w") as file:
    for k, v in report.items():
        file.write(f".{k}\n")
        for x in v:
            file.write(f"---{x}\n")
