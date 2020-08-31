def find_strongest_eggs(*args):
    seq = args[0]
    num = args[1]
    sub_lists = [seq[i::num] for i in range(num)]
    strong_eggs = []
    for l in sub_lists:
        middle = int(len(l) / 2)
        first_half = l[:middle]
        second_half = l[middle + 1:]
        if l[middle - 1] < l[middle] > l[middle + 1]:
            if [True for i, j in zip(first_half, second_half) if i < j]:
                strong_eggs.append(l[middle])

    return strong_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
