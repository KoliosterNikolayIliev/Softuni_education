positionU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
positionL = "abcdefghijklmnopqrstuvwxyz"
strings = input().split(" ")
stripped = []

sum = 0
for i in strings:
    if i != '':
        stripped.append(i)
for j in stripped:
    firstL = j[0]
    lastL = j[len(j) - 1]
    number = ''
    for x in range(1, len(j) - 1):
        number += j[x]

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
