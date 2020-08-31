ticketsin = input().strip().split(", ")
tickets = []
for j in ticketsin:
    tickets.append(j.strip())

for i in tickets:
    if len(i) != 20:
        print("invalid ticket")
        continue
    counter1 = 0
    symbol1 = ""
    counter2 = 0
    symbol2 = ""
    half1 = i[:10]
    half2 = i[10:]

    for j in range(len(half1)):
        if half1[j] == '@' or half1[j] == '#' or half1[j] == '$' or half1[j] == '^':
            counter1 += 1
            symbol1 = half1[j]
    for k in range(len(half2)):
        if half2[k] == '@' or half2[k] == '#' or half2[k] == '$' or half2[k] == '^':
            counter2 += 1
            symbol2 = half2[k]

    if counter1 > counter2:
        counter = counter2
    else:
        counter = counter1

        if 6 <= counter1 < 10 and symbol1 == symbol2:
            print(f'ticket "{i}" - {counter}{symbol1}')

        elif counter1 == 10 and symbol1 == symbol2:
            print(f'ticket "{i}" - {counter}{symbol1} Jackpot!')

        else:
            print(f'ticket "{i}" - no match')


