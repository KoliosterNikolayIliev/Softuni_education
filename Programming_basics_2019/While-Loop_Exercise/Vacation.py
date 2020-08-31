money_needed = float(input())
available_money = float(input())

days = 0
spending_counter = 0

while available_money < money_needed and spending_counter < 5:
    command = input()
    money = float(input())
    days += 1

    if command == 'save':
        available_money += money
        spending_counter = 0

    elif command == 'spend':
        available_money -= money
        spending_counter += 1
        if available_money < 0:
            available_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(f'{days}')

else:
    print(f'You saved the money for {days} days.')
