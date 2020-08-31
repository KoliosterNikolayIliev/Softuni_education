days = int(input())
budget = float(input())
people = int(input())
fuel = float(input())
food = float(input())
room = float(input())


if people > 10:
    room *= 0.75

current_expenses = days * people * (food+room)
for day in range(1, days + 1):
    if current_expenses>budget:
        break
    distance = float(input())
    fuel_expenses = fuel * distance
    current_expenses += fuel_expenses
    if day % 3 == 0 or day % 5 == 0:
        current_expenses *= 1.4
    elif day % 7 == 0:
        current_expenses -= current_expenses / people
money = budget - current_expenses
if current_expenses <= budget:
    print(f"You have reached the destination. You have {(abs(money)):.2f}$ budget left.")
else:
    print(f"Not enough money to continue the trip. You need {(abs(money)):.2f}$ more.")
