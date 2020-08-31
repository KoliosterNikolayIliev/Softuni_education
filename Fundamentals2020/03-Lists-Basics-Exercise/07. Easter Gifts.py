gifts = input().split(' ')
str_print = " "
command = input()

while not command == "No Money":
    tokens = command.split(' ')

    if tokens[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == tokens[1]:
                gifts[i] = "None"

    elif tokens[0] == "Required":
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = tokens[1]

    elif tokens[0] == "JustInCase":
        index_2 = max([len(gifts) - 1])
        gifts.remove(gifts[index_2])
        gifts.append(tokens[1])

    command = input()

for j in gifts:
    if "None" in gifts:
        gifts.remove('None')


str_print = str_print.join(gifts)

print(str_print)
