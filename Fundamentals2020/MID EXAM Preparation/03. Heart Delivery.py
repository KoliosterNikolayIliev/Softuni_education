hearts_house = [int(x) for x in input().split("@")]
index = 0
valent_count = 0
while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Love!":
        break
    length = int(command[1])
    index += length
    if index >= len(hearts_house):
        index = 0

    if hearts_house[index] > 0:
        hearts_house[index] -= 2
        if hearts_house[index] == 0:
            valent_count += 1
            print(f"Place {index} has Valentine's day.")
    elif hearts_house[index] == 0:
        # valent_count += 1
        print(f"Place {index} already had Valentine's day.")

print(f"Cupid's last position was {index}.")
if valent_count >= len(hearts_house):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(hearts_house)-valent_count} places.")

