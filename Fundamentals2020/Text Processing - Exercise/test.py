ticketsin = input().strip().split(", ")
tickets = []
counter = 0
symbol = ""

for j in ticketsin:
    tickets.append(j.strip())

for i in tickets:
    if len(i) == 20:

        for j in range(len(i)):
            if i[j] == '@' or i[j] == '#' or i[j] == '$' or i[j] == '^':
                # if 0 <= j < len(i) - 1:
                #     if i[j] == i[j + 1]:
                counter += 1
                symbol = i[j]
        counter = counter // 2
        if 6 <= counter < 10:
            print(f'ticket "{i}" - {counter:.0f}{symbol}')
            counter = 0
        elif counter == 10:
            print(f'ticket "{i}" - {counter:.0f}{symbol} Jackpot!')
            counter = 0
        else:
            print(f'ticket "{i}" - no match')
            counter = 0
    else:
        print("invalid ticket")
        counter = 0

