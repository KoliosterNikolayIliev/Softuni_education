stat_pirate_ship = input().split('>')
stat_warship = input().split('>')
max_health = int(input())

int_warship = [int(i) for i in stat_warship]
int_pirate_ship = [int(i) for i in stat_pirate_ship]
pirate_ship = True
command = ""
while True:
    command = input()
    if command != "Retire" and command != "Status":
        tokens = command.split()

        if tokens[0] == "Fire":
            index = int(tokens[1])
            damage = int(tokens[2])
            if 0 <= index < len(int_warship):
                int_warship[index] -= damage
                if int_warship[index] <= 0:
                    print("You won! The enemy ship has sunken.")
                    break

        elif tokens[0] == "Defend":
            start_index = int(tokens[1])
            end_index = int(tokens[2])
            damage = int(tokens[3])
            if 0 <= start_index < len(int_pirate_ship) and 0 <= end_index < len(int_pirate_ship):
                for i in range(start_index, end_index + 1):
                    health = int_pirate_ship[i] - damage
                    if health > 0:
                        del int_pirate_ship[i]
                        int_pirate_ship.insert(i, health)
                    else:
                        pirate_ship = False
                        print("You lost! The pirate ship has sunken.")
                        break
            pass
        elif tokens[0] == "Repair":
            index = int(tokens[1])
            add_health = int(tokens[2])
            if 0 <= index < len(int_pirate_ship):
                health = int_pirate_ship[index] + add_health
                if health > max_health:
                    health = max_health
                del int_pirate_ship[index]
                int_pirate_ship.insert(index, health)

    elif command == "Status":
        count = []
        for i in int_pirate_ship:
            if i < 0.2 * max_health:
                count.append(i)
        print(f"{len(count)} sections need repair.")
    if not pirate_ship:
        break
    elif command == "Retire":
        print(f"Pirate ship status: {sum(int_pirate_ship)}")
        print(f"Warship status: {sum(int_warship)}")

        break
