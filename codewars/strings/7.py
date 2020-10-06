def narcissistic(value):
    # Code away
    ll = [int(x) for x in str(value)]
    new_ll = sum([x**len(ll) for x in ll])
    return new_ll == value


print(narcissistic(1634))
