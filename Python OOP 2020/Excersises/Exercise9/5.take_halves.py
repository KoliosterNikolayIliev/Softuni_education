def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            i = i / 2
            yield i

    def take(n, seq):
        ll = []
        x = 0
        for i in seq:
            ll.append(i)
            x += 1
            if x == n:
                break
        return ll

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
