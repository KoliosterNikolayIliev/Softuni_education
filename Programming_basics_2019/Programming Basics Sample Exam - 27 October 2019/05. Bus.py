int_pasengers = int(input())
stops_count = int(input())


for i in range(stops_count):

    get_off = int(input())
    get_in = int(input())
    int_pasengers -= get_off
    int_pasengers += get_in

    if i % 2 == 0:
         get_off += 2

    else:
        get_in += 2

print(int_pasengers)
