from collections import deque


def find_strongest_eggs(*args):
    sublist = []
    spare = []
    strongest = []

    for i in range(args[1]):
        if args[1] > 1:
            sublist.append([])
            [sublist[i].append(x) for x in args[0] if args[0].index(x) % 2 == 0 and i % 2 == 0]
            [sublist[i].append(x) for x in args[0] if args[0].index(x) % 2 != 0 and i % 2 != 0]
        else:
            [sublist.append(x) for x in args[0]]
            break

    if args[1] > 1:
        index_middle = int(len(sublist[0]) / 2)

    else:
        index_middle = int(len(sublist) / 2)
        spare.append(sublist)
        spare.append([])
        sublist = spare

    for j in range(len(sublist)):
        if len(sublist[j]) == 0:
            if j == 1:
                break
        index_list = deque(sublist[j])
        if sublist[j][index_middle - 1] < sublist[j][index_middle] > sublist[j][index_middle + 1]:
            while len(index_list) > 1:
                left_egg = index_list.popleft()
                right_egg = index_list.pop()
                if right_egg > left_egg:
                    strongest.append(sublist[j][index_middle])
                    break
    return strongest


    return sublist


test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
