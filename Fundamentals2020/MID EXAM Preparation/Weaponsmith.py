WeaponName = input().split("|")

while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Move":
        direction = command[1]
        if direction == "Left":
            index = int(command[2])
            if index in range(len(WeaponName)):
                if 0 < index <= len(WeaponName):
                    WeaponName.insert(index - 1, WeaponName.pop(index))

        elif direction == "Right":
            index = int(command[2])
            if index in range(len(WeaponName)):
                if index < len(WeaponName):
                    WeaponName.insert(index + 1, WeaponName.pop(index))
    elif cmd == "Check":
        number = command[1]
        if number == "Even":
            evens = []
            even_index = [int(x) for x in range(len(WeaponName)) if x % 2 == 0]
            for i in even_index:
                evens.append(WeaponName[i])
            print(f"{' '.join(evens)}")
        else:
            odds = []
            odd_index = [int(x) for x in range(len(WeaponName)) if x % 2 != 0]
            for i in odd_index:
                odds.append(WeaponName[i])
            print(f"{' '.join(odds)}")
    elif cmd == "Done":
        break
print(f"You crafted {''.join(WeaponName)}!")
