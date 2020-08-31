string = tuple(x for x in input())
letters = dict()

for i in string:
    if i not in letters:
        letters[i] = string.count(i)
letters = dict(sorted(letters.items(), key=lambda x: (x[0])))
[print(f'{k}: {v} time/s') for k, v in letters.items()]
