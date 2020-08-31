from collections import deque

string = deque(input().split())
colours = []
all_colours = ["red", "yellow", "blue", "orange", "purple", "green"]
main_colours = ["red", "yellow", "blue"]
secondary_colours = {"orange": ["red", "yellow"], "purple": ["red", "blue"],
                     "green": ["yellow", "blue"]}

while string:
    sub_two = string.pop()
    if string:
        sub_one = string.popleft()
    else:
        sub_one = ""
    if_color = sub_one + sub_two
    color = sub_two+sub_one
    if color in all_colours:
        colours.append(color)
    elif if_color in all_colours:
        colours.append(if_color)
    elif color in secondary_colours:
        colours.append(color)
    elif if_color in secondary_colours:
        colours.append(color)

    else:
        sub_one = sub_one[:-1]
        sub_two = sub_two[:-1]
        index = len(string) // 2
        if sub_one:
            string.insert(index, sub_one)
        if sub_two:
            string.insert(index, sub_two)

for i in colours:
    if i in secondary_colours.keys():
        if secondary_colours[i][1] not in colours or secondary_colours[i][0] not in colours:
            colours.remove(i)

print(colours)
