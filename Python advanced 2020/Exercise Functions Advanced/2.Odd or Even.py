def odd(ll):
    length = len(ll)
    odd_sum = 0
    for i in ll:
        if i % 2 != 0:
            odd_sum += i
    print(odd_sum * length)


def even(ll):
    length = len(ll)
    even_sum = 0
    for i in ll:
        if i % 2 == 0:
            even_sum += i
    print(even_sum * length)


command = input()
lst = [int(x) for x in input().split()]

if command == "Odd":
    odd(lst)
else:
    even(lst)
