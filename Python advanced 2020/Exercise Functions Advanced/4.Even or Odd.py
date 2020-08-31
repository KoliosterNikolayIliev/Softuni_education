def even_odd(*args):
    even_lst = []
    odd_lst = []
    command = args[-1]
    for i in args:
        if str(i).isdigit():
            if i % 2 == 0:
                even_lst.append(i)
            else:
                odd_lst.append(i)
    if command == "even":
        return even_lst
    else:
        return odd_lst


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
