import math

party_size = int(input())
days = int(input())
money = 0

for i in range(1, days + 1):
    money += 50
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    money -= 2 * party_size

    if i % 3 == 0:
        money -= 3 * party_size
    if i % 5 == 0:
        money += 20 * party_size
        if i % 3 == 0:
            money -= 2 * party_size

print(f"{party_size} companions received {math.floor(money / party_size)} coins each.")
