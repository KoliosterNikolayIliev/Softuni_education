ticketsin = input().strip().split(", ")
tickets = []
counter1 = 1
symbol1 = ""
counter2 = 1
symbol2 = ""
for j in ticketsin:
    tickets.append(j.strip())

for i in tickets:
    if len(i) != 20:
        print("invalid ticket")

    half1 = i[:10]
    half2 = i[10:]

    for j in range(len(half1)):
        if half1[j] == '@' or half1[j] == '#' or half1[j] == '$' or half1[j] == '^':
            if 0 <= j < len(half1) - 1:
                if half1[j] == half1[j + 1]:
                    counter1 += 1
                    symbol1 = half1[j]
    for k in range(len(half2)):
        if half2[k] == '@' or half2[k] == '#' or half2[k] == '$' or half2[k] == '^':
            if 0 <= k < len(half2) - 1:
                if half2[k] == half2[k + 1]:
                    counter2 += 1
                    symbol2 = half2[k]

    if counter1 > counter2:
        counter = counter2
    else:
        counter = counter1
    if symbol1 == symbol2:
        if 6 <= counter1 < 10:
            print(f'ticket "{i}" - {counter}{symbol1}')
            counter1 = 1
            counter2 = 1
        elif counter1 == 10:
            print(f'ticket "{i}" - {counter}{symbol1} Jackpot!')
            counter1 = 1
            counter2 = 1
        else:
            print(f'ticket "{i}" - no match')
            counter1 = 1
            counter2 = 1
    else:
        print(f'ticket "{i}" - no match')
        counter1 = 1
        counter2 = 1
