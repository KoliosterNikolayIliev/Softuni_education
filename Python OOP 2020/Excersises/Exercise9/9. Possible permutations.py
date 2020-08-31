from itertools import permutations


def possible_permutations(ll):
    a = list(permutations(ll))
    for i in a:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]