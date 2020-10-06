def delete_nth(order, max_e):
    lst = []
    for i in order:
        if lst.count(i) < max_e:
            lst.append(i)
    return lst

print(delete_nth([1,1,3,3,7,2,2,2,2],3))
