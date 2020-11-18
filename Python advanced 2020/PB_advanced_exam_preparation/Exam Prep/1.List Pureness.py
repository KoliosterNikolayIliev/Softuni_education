from _collections import deque


def best_list_pureness(*args):
    list = deque(args[0])
    K = args[1]
    pureness_list = []
    pure = 0
    rot = 0
    for _ in range(K):
        x = sum([list[x] * x for x in range(len(list))])
        pureness_list.append(x)
        y = list.pop()
        list.appendleft(y)
        pure = max(pureness_list)
        rot = pureness_list.index(pure)
    return f'Best pureness {pure} after {rot} rotations'
#
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
