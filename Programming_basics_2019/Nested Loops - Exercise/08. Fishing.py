x = int(input())
fish_counter = 0
stop = False
balance = 0

for i in range(x):

    name = input()

    if name == 'Stop':
        stop = True
        break

    weight = float(input())

    fish_counter += 1

    sum_fish = 0
    for letter in name:
        ascii_value = ord(letter)
        sum_fish += ascii_value

    sum_fish /= weight

    if fish_counter % 3 == 0:
        balance += sum_fish
    else:
        balance -= sum_fish

if not stop:
    print('Lyubo fulfilled the quota!')
if balance >= 0:
    print(f"Lyubo's profit from {fish_counter} fishes is {balance:.2f} leva.")
else:
    print(f'Lyubo lost {abs(balance):.2f} leva today.')
