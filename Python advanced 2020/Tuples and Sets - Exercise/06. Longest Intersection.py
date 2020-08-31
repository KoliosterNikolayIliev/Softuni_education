n = int(input())
intersections = dict()
for _ in range(n):
    data = input().split("-")
    indexes_1 = data[0].split(",")
    indexes_2 = data[1].split(",")
    start_1 = int(indexes_1[0])
    end_1 = int(indexes_1[1])
    start_2 = int(indexes_2[0])
    end_2 = int(indexes_2[1])
    set_1 = set()
    set_2 = set()
    for i in range(start_1, end_1 + 1):
        set_1.add(i)
    for j in range(start_2, end_2 + 1):
        set_2.add(j)

    intersection = list(set_1.intersection(set_2))
    if intersection not in intersections.items():
        intersections[len(intersection)] = intersection
max_key = max(intersections.keys())
max_val = intersections[max_key]
print(f"Longest intersection is {max_val} with length {max_key}")
