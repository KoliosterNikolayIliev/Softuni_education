import os

PATH_TO_DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
PATH_TO_DESKTOP_UNIX = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

'''Depending on your OS, this path may be different.
Please change it to reflect your environment.

os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

'''

path = input()

result_dict = {}

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split(".")[1]
        if extension not in result_dict:
            result_dict[extension] = []
        result_dict[extension].append(file)

result_str = ''

for k, v in sorted(result_dict.items()):
    result_str += f".{k}\n"
    for file in sorted(v):
        result_str += f'- - - {file}\n'
    # print(f"{k}:\n{[(f'- - - {x}', end='\n') for x in v]}")


fnl_loc = PATH_TO_DESKTOP + os.path.sep + "report.txt"

with open(fnl_loc, "w") as file:
    file.write(result_str)