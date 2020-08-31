positionU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
positionL = "abcdefghijklmnopqrstuvwxyz"
strings = input().split()

sum = 0

for i in strings:
    firstL = i[0]
    lastL = i[- 1]
    number = i[1:-1]

    if firstL.isupper():
        x = positionU.index(firstL) + 1
        number = float(number) / x
    elif firstL.islower():
        x = positionL.index(firstL) + 1
        number = float(number) * x
    if lastL.isupper():
        x = positionU.index(lastL) + 1
        number = float(number) - x
    elif lastL.islower():
        x = positionL.index(lastL) + 1
        number = float(number) + x
    sum += float(number)
print(f"{sum:.2f}")
