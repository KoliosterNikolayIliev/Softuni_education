def fix_calendar(ll):
    for j in range(len(ll)):
        if j == len(ll) - 1:
            j = 0
        for i in range(len(ll)):
            if i == len(ll) - 1:
                i = 0
            while ll[i] > ll[i + 1]:
                ll[i], ll[i + 1] = ll[i + 1], ll[i]

    return ll


numbers = [3, 2, 1, 5, 10, 7, 8, 6, 9, 4]
fixed = fix_calendar(numbers)
print(fixed)
