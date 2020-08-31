init_list = [x.split() for x in [x for x in input().split('|')]]
print(' '.join([x for i in reversed(init_list) for x in i]))
