target=int(input())

command=input()
income=0
price=0
take_money=False

while not command=='closed' :


    if command=='haircut' or command == 'color':
        command=input()

        if command == 'mens':
            take_money =True
            price = 15
        elif command == 'ladies':
            take_money = True
            price = 20
        elif command == 'kids':
            take_money = True
            price = 10
        elif command == 'touch up':
            take_money = True
            price = 20
        elif command == 'full color':
            take_money = True
            price = 30
    income += price

    if income>=target:
        break
    command = input()
if income>=target:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target-income}lv. more.")
print(f"Earned money: {income}lv.")










